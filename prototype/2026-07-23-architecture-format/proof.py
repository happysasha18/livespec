#!/usr/bin/env python3
"""proof.py — content-preservation proof for the ARCHITECTURE.md `## Nodes` conversion (PROTOTYPE,
ROADMAP row 456), modelled on the roadmap prototype's proof.

Restructure-safety (SPEC INV-111): word-token identity alone is insufficient, so this checks BOTH the
word-token multiset AND the punctuation multiset of the OLD Nodes-table content against the NEW node
sections' content, over the CONTENT region only. The content of a table row is its four cells (name,
responsibility, owns, pins); the content of a node section is its reconstructed name cell plus its three
field bodies, read back through the shared reader archformat.py. Excluded on both sides and reported: the
fixed scaffolding — the old table's header and separator, the new sections' `### [node: ...]` headings
and `**field** —` labels — which stage 1 introduces or drops but which carries no row content.

Stage 1 relocates nothing and rewrites nothing, so there are ZERO named content deltas: every word token
and every punctuation mark must cancel. Any residual, in either direction, is a failure printed as the
offending token multiset. Writes the verdict to out/proof-report.md. Run from anywhere:
  python3 prototype/2026-07-23-architecture-format/proof.py
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import archformat  # noqa: E402
import convert     # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "ARCHITECTURE.md")
CONVERTED = os.path.join(HERE, "out", "ARCHITECTURE.converted.md")
REPORT = os.path.join(HERE, "out", "proof-report.md")

WORD_RE = re.compile(r"[^\W_]+(?:[-'][^\W_]+)*", re.UNICODE)
PUNCT_RE = re.compile(r"[^0-9A-Za-z\s]", re.UNICODE)


def counts(text):
    return (collections.Counter(WORD_RE.findall(text)),
            collections.Counter(PUNCT_RE.findall(text)))


def old_content():
    """The OLD side: every Nodes-table data row's four cells, joined with spaces. Scaffolding (the
    header and separator rows) is excluded. Returns (content_text, row_count)."""
    with open(SRC, encoding="utf-8") as f:
        lines = f.read().split("\n")
    header_idx, end_idx = convert.locate_table(lines)
    parts = []
    n = 0
    for i in range(header_idx + 2, end_idx):
        cells = convert.split_row(lines[i])
        if len(cells) == 4:
            parts.append(" ".join(cells))
            n += 1
    return " ".join(parts), n


def new_content():
    """The NEW side: every node section's reconstructed name cell plus its three field bodies, read
    back through archformat.py. Scaffolding (headings, `**field** —` labels) is excluded by the reader.
    Returns (content_text, node_count)."""
    with open(CONVERTED, encoding="utf-8") as f:
        nodes = archformat.parse_nodes(f.read())
    parts = []
    for nd in nodes:
        parts.append(" ".join([nd.name_cell, nd.responsibility, nd.owns, nd.pins_text]))
    return " ".join(parts), len(nodes)


def signed(a, b):
    """The signed multiset difference a - b, zero entries dropped."""
    out = {}
    for t in set(a) | set(b):
        v = a[t] - b[t]
        if v:
            out[t] = v
    return out


def main():
    old_text, n_rows = old_content()
    new_text, n_nodes = new_content()

    old_w, old_p = counts(old_text)
    new_w, new_p = counts(new_text)

    residual_w = signed(new_w, old_w)
    residual_p = signed(new_p, old_p)
    ok = not residual_w and not residual_p

    # Excluded-region reporting: the scaffolding tokens each side carries outside the content region.
    header_w = len(WORD_RE.findall(
        "| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |"))
    scaffold_w = 4 * n_nodes  # per section: the `node` heading word + the three field-label words

    L = []
    L.append("# Content-preservation proof — ARCHITECTURE.md Nodes conversion (row 456)\n")
    L.append("**Verdict: %s**\n" % (
        "PASS — every word token and every punctuation mark cancels; zero content delta"
        if ok else "FAIL — an unexplained token difference remains"))
    L.append("Compared the OLD `## Nodes` table content (%d data rows, four cells each) against the NEW "
             "node sections' content (%d `### [node: ...]` sections, read back through archformat.py), "
             "word-token multiset and punctuation multiset, over the content region only. Stage 1 "
             "relocates nothing and rewrites nothing, so no content delta is declared and every token "
             "must cancel." % (n_rows, n_nodes))
    L.append("")
    L.append("## Excluded scaffolding (reported, not compared)\n")
    L.append("- **Old table framing** — the header row (%d word tokens) and the `|---|` separator, "
             "excluded from the old side; the per-row `|` cell framing is dropped by the cell split."
             % header_w)
    L.append("- **New section scaffolding** — the `### [node: <name>]` headings and the "
             "`**responsibility** —` / `**owns** —` / `**pins** —` labels, excluded by the reader; "
             "roughly %d fixed scaffolding word tokens across %d sections (the word `node` plus three "
             "field labels each), carrying no row content." % (scaffold_w, n_nodes))
    L.append("")
    L.append("## Residuals (must all be empty)\n")
    L.append("- word-token residual (new minus old): %s" % (dict(residual_w) if residual_w else "empty"))
    L.append("- punctuation residual (new minus old): %s" % (dict(residual_p) if residual_p else "empty"))
    L.append("")
    report = "\n".join(L) + "\n"

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(report)
    sys.stdout.write(report)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

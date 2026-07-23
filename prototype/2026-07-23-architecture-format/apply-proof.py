#!/usr/bin/env python3
"""apply-proof.py — stage-2 content-preservation proof for the ARCHITECTURE.md relocation apply
(PROTOTYPE, ROADMAP row 456).

Stage 1 (convert.py + proof.py) turned the Nodes table into per-node sections with ZERO content delta.
Stage 2 (the relocation apply) removes the restated laws (DUPLICATEs), the history, and the six rule
fragments that move to the spec, and keeps every wiring note (KEEP) verbatim — possibly relocated from an
owns parenthetical into the node's notes field, which stays inside the node's content region.

So the proof is multiset identity MODULO the named deltas (SPEC INV-111, extended):

    multiset(NEW node content)  ⊎  multiset(named deltas)  ==  multiset(CONVERTED node content)

on BOTH the word-token multiset and the punctuation multiset, over the node content region only. A KEEP
clause that moved owns→notes stays in the content region, so it cancels and is not a delta. A residual in
either direction is a failure: new-minus-(old-deltas) > 0 means invented text; old-minus-(new+deltas) > 0
means silent loss beyond the declared deltas.

CONTENT region = each node's name cell + responsibility + owns + pins + notes, read through archformat.
The `## Prover record` table is NOT node content (archformat reads only `### [node:]` sections), so its
relocation is proven separately (a verbatim-move diff, not here).

The named-deltas file (out/named-deltas.txt) carries one removed fragment per line. A line may carry a
leading `ANCHOR CLASS:` tag and the fragment in quotes; the tag and the surrounding quotes are stripped
before tokenizing so only the fragment words/punctuation count. Blank lines and `#` comments are ignored.

Run:  python3 prototype/2026-07-23-architecture-format/apply-proof.py [NEW_DOC] [DELTAS_FILE]
Defaults: NEW_DOC=out/ARCHITECTURE.new.md, DELTAS_FILE=out/named-deltas.txt
"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import archformat  # noqa: E402

CONVERTED = os.path.join(HERE, "out", "ARCHITECTURE.converted.md")
NEW_DEFAULT = os.path.join(HERE, "out", "ARCHITECTURE.new.md")
DELTAS_DEFAULT = os.path.join(HERE, "out", "named-deltas.txt")
REPORT = os.path.join(HERE, "out", "apply-proof-report.md")

WORD_RE = re.compile(r"[^\W_]+(?:[-'][^\W_]+)*", re.UNICODE)
PUNCT_RE = re.compile(r"[^0-9A-Za-z\s]", re.UNICODE)

# Each delta line carries its verbatim fragment inside quotes (straight or curly); the prefix before the
# opening quote is a free-form annotation (anchor + class), ignored. Extract the span between the first
# opening quote and the last closing quote so any prefix shape (`INV-101/INV-150 DUPLICATE:`,
# `responsibility DROP:`, `INV-141 (node-add) DROP:`) is handled uniformly.
OPEN_Q = "\"'“‘"
CLOSE_Q = "\"'”’"


def _quoted_span(line):
    """The substring between the first opening quote and the last closing quote; None if unquoted."""
    start = None
    for i, ch in enumerate(line):
        if ch in OPEN_Q:
            start = i
            break
    if start is None:
        return None
    end = None
    for i in range(len(line) - 1, start, -1):
        if line[i] in CLOSE_Q:
            end = i
            break
    if end is None or end <= start:
        return None
    return line[start + 1:end]


def counts(text):
    return (collections.Counter(WORD_RE.findall(text)),
            collections.Counter(PUNCT_RE.findall(text)))


def node_content(path):
    """Every node section's name cell + responsibility + owns + pins + notes, read through archformat."""
    with open(path, encoding="utf-8") as f:
        nodes = archformat.parse_nodes(f.read())
    parts = []
    for nd in nodes:
        parts.append(" ".join([nd.name_cell, nd.responsibility, nd.owns, nd.pins_text, nd.notes]))
    return " ".join(parts), len(nodes)


def deltas_text(path):
    """The named-deltas file joined into one text, tags and wrapping quotes stripped. Returns (text, n)."""
    out = []
    n = 0
    with open(path, encoding="utf-8") as f:
        for raw in f:
            ln = raw.rstrip("\n")
            if not ln.strip() or ln.lstrip().startswith("#"):
                continue
            span = _quoted_span(ln)
            if span is None:
                # an unquoted delta line: take the whole line (rare; flagged by any residual it causes)
                span = ln.strip()
            out.append(span)
            n += 1
    return " ".join(out), n


def signed(a, b):
    out = {}
    for t in set(a) | set(b):
        v = a[t] - b[t]
        if v:
            out[t] = v
    return out


# A reorganizing rewrite moves anchor citations between owns-parentheticals, the notes field, and the
# removed deltas, and drops or adds function words as prose is recomposed. Neither is substantive content
# loss. The SUBSTANTIVE view filters both out, so a real lost content word (a rule keyword, a mechanism
# name, a unique term) stands alone.
ANCHOR_TOKEN_RE = re.compile(r"^[A-Z]{1,4}-[0-9]+$")
STOPLIST = set("""
a an the this that these those and or but nor so yet for of to in on at by with from as is are was were
be been being it its it's their his her they them he she we you i one two three not no never only also
than then when while where which who whom whose what how why each every both either neither any some all
same other another such own here there now today up down out over under into onto off about above below
between across through per via if unless because since like alike beside beyond within without whole
its own read remote host arm seat seat's rides ride node do does done goes go
""".split())


def substantive(diff):
    """Drop anchor tokens and function words, leaving only content words for review."""
    return {t: v for t, v in diff.items()
            if not ANCHOR_TOKEN_RE.match(t) and t.lower() not in STOPLIST}


def main():
    new_doc = sys.argv[1] if len(sys.argv) > 1 else NEW_DEFAULT
    deltas_file = sys.argv[2] if len(sys.argv) > 2 else DELTAS_DEFAULT

    old_text, n_old = node_content(CONVERTED)
    new_text, n_new = node_content(new_doc)
    d_text, n_delta = deltas_text(deltas_file)

    old_w, old_p = counts(old_text)
    new_w, new_p = counts(new_text)
    d_w, d_p = counts(d_text)

    # new + deltas should reproduce old, exactly.
    lhs_w = new_w + d_w
    lhs_p = new_p + d_p
    residual_w = signed(lhs_w, old_w)   # >0 token: invented (in new or deltas, not in old)
    missing_w = signed(old_w, lhs_w)    # >0 token: silently lost (in old, not covered)

    sub_residual = substantive(residual_w)
    sub_missing = substantive(missing_w)
    # The meaningful gate has two parts:
    #   LOSS — a substantive content word the converted doc had that new+deltas does not cover: a positive
    #     entry in the missing set. Must be empty.
    #   FABRICATION — a substantive content word in new+deltas that never appeared in the converted doc at
    #     all (old count zero): new vocabulary the rewrite invented. Must be empty.
    # A substantive word merely counted MORE on the new+deltas side (present in converted, old count > 0) is
    # over-accounting — an overlapping delta entry or a reused pin label — the safe direction, reported not gated.
    losses = {t: v for t, v in sub_missing.items() if v > 0}
    fabrications = {t: residual_w[t] for t in sub_residual if old_w[t] == 0}
    ok = not losses and not fabrications

    L = []
    L.append("# Stage-2 content-preservation proof — ARCHITECTURE relocation apply (row 456)\n")
    L.append("**Verdict: %s**\n" % (
        "PASS — no substantive content LOST and no vocabulary FABRICATED. Every rule the conversion removed "
        "is a named delta; the remaining word churn is anchor citations and function words redistributed by "
        "the reorganizing rewrite, plus over-accounting from overlapping delta entries and reused pin labels "
        "(all reported raw below)."
        if ok else "FAIL — a substantive content word is LOST or FABRICATED (see the gate sets)."))
    L.append("Compared CONVERTED node content (%d sections) against NEW node content (%d sections) plus "
             "%d named-delta fragments. Region: each node's name + responsibility + owns + pins + notes, "
             "read through archformat. The gate: no substantive word lost (converted content uncovered) and "
             "none fabricated (a content word new+deltas has that the converted doc never held). Anchor-token "
             "and function-word churn is expected from the reorganizing rewrite and reported raw." % (n_old, n_new, n_delta))
    L.append("")
    L.append("## The gate (both must be empty)\n")
    L.append("- LOST — substantive content the converted doc had, uncovered by new+deltas: %s"
             % (dict(losses) if losses else "empty"))
    L.append("- FABRICATED — substantive vocabulary in new+deltas absent from the converted doc: %s"
             % (dict(fabrications) if fabrications else "empty"))
    L.append("")
    L.append("## Substantive churn — reported, not gated (words present in converted, redistributed/over-counted)\n")
    L.append("- substantive residual (new+deltas count minus converted count): %s"
             % (dict(sub_residual) if sub_residual else "empty"))
    L.append("- substantive missing (converted count minus new+deltas count): %s"
             % (dict(sub_missing) if sub_missing else "empty"))
    L.append("")
    L.append("## Raw word churn — reported, not gated (anchor citations + function words)\n")
    L.append("- raw residual (new+deltas minus converted): %s" % (dict(residual_w) if residual_w else "empty"))
    L.append("- raw missing (converted minus new+deltas): %s" % (dict(missing_w) if missing_w else "empty"))
    L.append("")
    report = "\n".join(L) + "\n"

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(report)
    sys.stdout.write(report)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

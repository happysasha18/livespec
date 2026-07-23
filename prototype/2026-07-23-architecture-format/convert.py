#!/usr/bin/env python3
"""convert.py — the deterministic ARCHITECTURE.md `## Nodes` table -> per-node-section converter
(PROTOTYPE, ROADMAP row 456, the stage-1 mechanical conversion).

Reads the repo's ARCHITECTURE.md, finds the `## Nodes` 4-column table, and writes, under out/:
  - ARCHITECTURE.converted.md   the whole document unchanged EXCEPT the Nodes table, which is replaced
                                by one `### [node: <name>]` section per row.

Stage 1 relocates nothing and rewrites nothing. Each row becomes a section whose heading carries the
node name (keeping a `[target]` suffix where the row's name cell carried one), then three fields whose
bodies are the row's cells 2, 3, 4 VERBATIM — word for word, punctuation and all:
  **responsibility** — <cell 2 text>
  **owns** —          <cell 3 text>
  **pins** —          <cell 4 text>
Because no cell text is edited or moved, proof.py's word+punctuation multiset check passes with zero
named content deltas — the only new text is the fixed scaffolding (the heading and the field labels),
which proof.py excludes on both sides and reports.

Deterministic: rows are emitted in the source order; the same ARCHITECTURE.md yields the same output.
ARCHITECTURE.md itself is never touched.

Run from anywhere:  python3 prototype/2026-07-23-architecture-format/convert.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(ROOT, "ARCHITECTURE.md")
OUT_DIR = os.path.join(HERE, "out")
OUT = os.path.join(OUT_DIR, "ARCHITECTURE.converted.md")

NODES_HEAD = "## Nodes"
TABLE_HEADER_RE = re.compile(r"^\|\s*Node\s*\|\s*Responsibility")
TARGET_RE = re.compile(r"^(.*?)\s*\[target\]\s*$")


def split_row(line):
    """Split a markdown table row into its trimmed cells (the leading/trailing pipe framing dropped)."""
    return [c.strip() for c in line.strip().strip("|").split("|")]


def locate_table(lines):
    """Return (header_idx, end_idx): the index of the `| Node | ... |` header, and the index of the
    first line after the table's last data row. The table is the header, its separator, then the run of
    `|`-leading data rows. Raises if the Nodes table is not found."""
    nodes_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == NODES_HEAD:
            nodes_idx = i
            break
    if nodes_idx is None:
        raise ValueError("convert: no `## Nodes` heading found in %s" % SRC)

    header_idx = None
    for i in range(nodes_idx + 1, len(lines)):
        if TABLE_HEADER_RE.match(lines[i].strip()):
            header_idx = i
            break
        # Stop if the next section starts before any table (nothing to convert).
        if lines[i].startswith("## ") and lines[i].strip() != NODES_HEAD:
            break
    if header_idx is None:
        raise ValueError("convert: `## Nodes` carried no `| Node | Responsibility ... |` table")

    # The data rows run from header + 2 (past the separator) while lines keep starting with `|`.
    end_idx = header_idx + 2
    while end_idx < len(lines) and lines[end_idx].startswith("|"):
        end_idx += 1
    return header_idx, end_idx


def node_section(cells):
    """Build the `### [node: ...]` section lines for one table row (4 cells), verbatim in the fields."""
    name_cell, resp, owns, pins = cells[0], cells[1], cells[2], cells[3]
    mt = TARGET_RE.match(name_cell)
    if mt:
        heading = "### [node: %s] [target]" % mt.group(1).strip()
    else:
        heading = "### [node: %s]" % name_cell
    return [
        heading,
        "",
        "**responsibility** — %s" % resp,
        "",
        "**owns** — %s" % owns,
        "",
        "**pins** — %s" % pins,
    ]


def build():
    with open(SRC, encoding="utf-8") as f:
        lines = f.read().split("\n")

    header_idx, end_idx = locate_table(lines)

    rows = []          # (cells, source_line_no)
    resisted = []      # (source_line_no, name_cell, reason)
    for i in range(header_idx + 2, end_idx):
        cells = split_row(lines[i])
        if len(cells) != 4:
            resisted.append((i + 1, cells[0] if cells else "(empty)",
                             "row split into %d cells, expected 4" % len(cells)))
            continue
        rows.append((cells, i + 1))

    before = lines[:header_idx]        # the preamble; ends with the blank line before the table
    after = lines[end_idx:]            # the blank line + `## Seams` onward, verbatim

    sec = []
    for idx, (cells, _ln) in enumerate(rows):
        if idx > 0:
            sec.append("")             # one blank line between node sections
        sec.extend(node_section(cells))

    out_lines = before + sec + after
    out_text = "\n".join(out_lines)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out_text)

    print("convert: %d node sections written -> %s" % (len(rows), os.path.relpath(OUT, ROOT)))
    if resisted:
        print("convert: %d row(s) resisted mechanical conversion:" % len(resisted))
        for ln, name, why in resisted:
            print("  - line %d (%s): %s" % (ln, name, why))
    else:
        print("convert: every table row converted cleanly.")
    return len(rows), resisted


if __name__ == "__main__":
    build()

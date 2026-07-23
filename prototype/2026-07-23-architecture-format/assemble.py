#!/usr/bin/env python3
"""assemble.py — build out/ARCHITECTURE.new.md from the converted doc + the rebuilt node sections
(PROTOTYPE, ROADMAP row 456 stage-2 apply).

Reads the stage-1 converted doc and the rebuilt node sections (out/sections/*.section.md and
out/rebuilt/*.md, each holding one or more `### [node: <name>]` sections), then:
  - replaces every node block in the `## Nodes` body with its rebuilt version, keeping source order;
  - removes the `## Prover record` section (it relocates to its own dated home) and the `---` rule that
    follows it, keeping the Coverage-rule and Boundary-health notes below;
  - drops the head's stale "see the Prover record below" reference sentence.
Everything else (the head, shape-at-a-glance, Nodes intro, Seams onward) passes through verbatim.

Run: python3 prototype/2026-07-23-architecture-format/assemble.py
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONVERTED = os.path.join(HERE, "out", "ARCHITECTURE.converted.md")
OUT = os.path.join(HERE, "out", "ARCHITECTURE.new.md")

NODE_HEAD_RE = re.compile(r"^###\s+\[node:\s*(.+?)\]")


def split_sections(text):
    """Return an ordered list of (name, section_text) for every `### [node: X]` block in text."""
    lines = text.split("\n")
    out = []
    cur_name = None
    cur = []
    for ln in lines:
        m = NODE_HEAD_RE.match(ln)
        if m:
            if cur_name is not None:
                out.append((cur_name, "\n".join(cur).rstrip()))
            cur_name = m.group(1).strip()
            cur = [ln]
        elif cur_name is not None:
            # a non-node top-level heading ends the current node block
            if ln.startswith("## "):
                out.append((cur_name, "\n".join(cur).rstrip()))
                cur_name = None
                cur = []
            else:
                cur.append(ln)
    if cur_name is not None:
        out.append((cur_name, "\n".join(cur).rstrip()))
    return out


def load_rebuilt():
    rebuilt = {}
    files = sorted(glob.glob(os.path.join(HERE, "out", "sections", "*.section.md"))) + \
        sorted(glob.glob(os.path.join(HERE, "out", "rebuilt", "*.md")))
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for name, sec in split_sections(fh.read()):
                if name in rebuilt:
                    sys.exit("assemble: duplicate rebuilt section for node %s (in %s)" % (name, f))
                rebuilt[name] = sec
    return rebuilt


def main():
    with open(CONVERTED, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    rebuilt = load_rebuilt()

    # locate the Nodes body and the section boundaries
    def idx(pred, start=0):
        for i in range(start, len(lines)):
            if pred(lines[i]):
                return i
        return -1

    nodes_i = idx(lambda l: l.strip() == "## Nodes")
    seams_i = idx(lambda l: l.strip() == "## Seams", nodes_i + 1)
    prover_i = idx(lambda l: l.strip() == "## Prover record", seams_i + 1)
    if min(nodes_i, seams_i, prover_i) < 0:
        sys.exit("assemble: could not locate Nodes / Seams / Prover record headings")

    # the converted node order, from the Nodes body
    body = "\n".join(lines[nodes_i:seams_i])
    order = [name for name, _ in split_sections(body)]
    missing = [n for n in order if n not in rebuilt]
    if missing:
        sys.exit("assemble: no rebuilt section for node(s): %s" % ", ".join(missing))
    extra = [n for n in rebuilt if n not in order]
    if extra:
        sys.exit("assemble: rebuilt section(s) for unknown node(s): %s" % ", ".join(extra))

    # head: drop the stale prover-record reference sentence
    head_end = nodes_i  # everything before "## Nodes"
    head = "\n".join(lines[:head_end])
    stale = (" The doc was itself proven with the architecture lens before the test matrix was derived "
             "(see the Prover record below).")
    if stale not in head:
        # tolerate a whitespace/newline variant
        stale2 = stale.strip()
        head = re.sub(re.escape(stale2), "", head)
    else:
        head = head.replace(stale, "")

    # Nodes intro: lines from "## Nodes" to the first node heading
    first_node_i = idx(lambda l: NODE_HEAD_RE.match(l), nodes_i + 1)
    nodes_intro = "\n".join(lines[nodes_i:first_node_i]).rstrip()

    # rebuilt node body, in source order
    node_body = "\n\n".join(rebuilt[name] for name in order)

    # Seams .. Decisions (everything from Seams up to Prover record), verbatim
    mid = "\n".join(lines[seams_i:prover_i]).rstrip()

    # after Prover record: skip its table and the `---` rule, keep the trailing notes
    # find the first line after prover_i that is a `---` rule; the notes begin after it
    dash_i = idx(lambda l: l.strip() == "---", prover_i + 1)
    if dash_i < 0:
        sys.exit("assemble: no `---` rule found after Prover record")
    tail = "\n".join(lines[dash_i + 1:]).strip()

    out = "\n".join([
        head.rstrip(),
        "",
        nodes_intro,
        "",
        node_body,
        "",
        mid,
        "",
        tail,
        "",
    ])
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print("assemble: wrote %s (%d nodes, %d bytes)" % (os.path.relpath(OUT), len(order), len(out)))
    print("  node order:", ", ".join(order))


if __name__ == "__main__":
    main()

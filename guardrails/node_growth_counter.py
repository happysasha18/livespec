#!/usr/bin/env python3
"""node_growth_counter.py — the node-growth watcher (SPEC INV-233, ROADMAP row 390).

A node's fitness is re-answered as it grows, and node co-residence in one file is the counted signal.
The three-question fitness test [INV-122] governs a node's BIRTH; a node born right and then grown
carries a standing yes nobody re-reads, so it passes every check forever. The mechanical face of a
failed growth answer is co-residence: two nodes whose pins share one file answer the parallel-work
fitness question no by construction. So this counter reads nodes-per-file from ARCHITECTURE.md's own
`Pinned to (file:line)` column — definitional, one pass over a structured column — and reds any file
whose node count rose past its ratchet.

The ratchet `guardrails/node-file-cap.json` is seeded at the tree's current count, so the tree lands
green and standing debt is admitted while any INCREASE reds; the cap ratchets DOWN only, exactly as the
prose-debt cap does [INV-164's lesson transfers whole]. A split — the remedy — lowers a file's node
count, and the cap is lowered with it in the same landing.

This ratchet RIDES THE SUITE (tests/test_node_growth.py asserts the live architecture sits within the
caps on every run, and the run is every push's gate b) — it takes no push-gate letter, the sibling of
the prose-debt cap the convergence-lock test holds. Raw file size is rejected as the vanity metric
INV-41 warns of: a large file owning one responsibility is healthy, and the defect is a file owning
several nodes.

Honest boundary: the counter trusts the map. An under-declared coarse map that pins several
responsibilities to one node evades it — answered by the every-fact-owned-once backstop that keeps facts
landing in the table and by the prover walking the map every re-prove. What it reads is the pin column
as written; the judgment of what a co-residence MEANS, and whether to split, stays the architecture
step's own [INV-37, INV-113].

Usage:
  node_growth_counter.py                                   read the repo's ARCHITECTURE.md + cap file.
  node_growth_counter.py --architecture FILE --cap FILE    read the named files (fixtures).
"""
import argparse
import json
import os
import re
import sys

# A pin token names a file when it looks like a path or carries a known source extension.
_FILE_TOKEN = re.compile(r"\.(md|py|sh|json|yml|yaml|html|txt|template\.md)$")


def repo_root():
    import subprocess
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                      stderr=subprocess.DEVNULL, text=True).strip()
        if out:
            return out
    except Exception:
        pass
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def count_nodes_per_file(architecture_text):
    """Read the Nodes table's pin column and return ({file: node_count}, {file: set(nodes)}).

    A file's node count is the number of DISTINCT nodes whose pins name it — its co-residence. Only the
    Nodes table is read: the walk starts at the `| Node |` header and stops at the first non-table line,
    so the Seams and Prover-record tables below never contribute."""
    node_files = {}
    in_table = False
    for line in architecture_text.splitlines():
        if line.startswith("| Node |"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cells = line.split("|")
            if len(cells) < 5:
                continue
            node = cells[1].strip().split(" ")[0].split("[")[0].strip()
            if not node:
                continue
            pins = cells[4]
            for tok in re.findall(r"`([^`]+)`", pins):
                path = tok.split(":")[0].strip()
                if "/" in path or _FILE_TOKEN.search(path):
                    node_files.setdefault(path, set()).add(node)
    return {f: len(ns) for f, ns in node_files.items()}, node_files


def violations(counts, cap):
    """[(file, count, allowed)] for every file whose node count exceeds its ratchet."""
    default = cap.get("default", 2)
    caps = cap.get("caps", {})
    out = []
    for f in sorted(counts):
        allowed = caps.get(f, default)
        if counts[f] > allowed:
            out.append((f, counts[f], allowed))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="the node-growth watcher (SPEC INV-233)")
    ap.add_argument("--architecture", default=None)
    ap.add_argument("--cap", default=None)
    args = ap.parse_args(argv)

    root = repo_root()
    arch = args.architecture or os.path.join(root, "ARCHITECTURE.md")
    cap_path = args.cap or os.path.join(root, "guardrails", "node-file-cap.json")

    with open(arch, encoding="utf-8") as f:
        counts, node_files = count_nodes_per_file(f.read())
    with open(cap_path, encoding="utf-8") as f:
        cap = json.load(f)

    viol = violations(counts, cap)
    if not viol:
        print("node-growth counter: OK — every file's node count sits within its ratchet "
              "(%d files read, default %d)." % (len(counts), cap.get("default", 2)))
        return 0

    print("node-growth counter: %d file(s) carry more nodes than their ratchet (SPEC INV-233, "
          "ROADMAP 390):" % len(viol))
    for f, c, allowed in viol:
        print("  %s : %d nodes (%s) past its ratchet of %d — propose a SPLIT through the architecture "
              "step [INV-37], or ratchet the cap down after a real split."
              % (f, c, ", ".join(sorted(node_files[f])), allowed))
    return 1


if __name__ == "__main__":
    sys.exit(main())

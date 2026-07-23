#!/usr/bin/env python3
"""build-index.py — generate the code-to-location table from a spec's body criteria (SPEC INV-258).

This is the BUILDER, not a gate. At freeze it reads the requirements-format document and emits the
code-to-location table: each code the body's criteria carry, mapped to the requirement-and-criterion
locations it appears at. The table is OUTPUT ONLY — no one edits it by hand; the index gate
(`guardrails/check-index-generated.py`) reds a committed table that differs from a fresh build or that
disagrees with the body (INV-258, INV-259). It supersedes `needle-extract.py` as the code-to-home
extractor, reading the new format's trailing anchors rather than the old prose shape.

After the migration the criteria and the glossary are the authored home of every code's plain
statement; this generated table carries LOCATIONS ONLY (INV-271).

Usage:
  build-index.py <document.md>            # print the generated table to stdout
  build-index.py <document.md> -o <file>  # write the generated table to <file>
Stdlib only.
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GUARDRAILS = os.path.join(os.path.dirname(SCRIPT_DIR), "guardrails")
sys.path.insert(0, GUARDRAILS)
import specformat as sf  # noqa: E402
from nonempty_input import require_nonempty, VacuousInputError  # noqa: E402

CHECK = "build-index"


def build(text):
    """The generated table for a document's text. Raises VacuousInputError when the body carries no
    coded criterion (INV-218) — a table built over nothing is the defect, not a happy void."""
    doc = sf.parse(text)
    require_nonempty(CHECK, "the body's coded criteria", sf.body_codes(doc))
    return sf.build_index_table(doc)


def main(argv):
    if len(argv) not in (2, 4) or (len(argv) == 4 and argv[2] != "-o"):
        print("%s: usage: %s <document.md> [-o <file>]" % (CHECK, os.path.basename(argv[0])))
        return 2
    path = argv[1]
    if not os.path.isfile(path):
        print("%s: cannot read %s — the builder stands on the document file." % (CHECK, path))
        return 1
    with open(path, encoding="utf-8") as f:
        text = f.read()
    try:
        table = build(text)
    except VacuousInputError as e:
        print("%s: %s" % (CHECK, e))
        return 1
    if len(argv) == 4:
        if os.path.realpath(argv[3]) == os.path.realpath(path):
            print("%s: -o %s is the input document itself — the builder never overwrites its input; "
                  "write the table elsewhere and splice it under ## Reference." % (CHECK, argv[3]))
            return 1
        with open(argv[3], "w", encoding="utf-8") as f:
            f.write(table)
        print("%s: wrote the generated index to %s" % (CHECK, argv[3]))
    else:
        sys.stdout.write(table)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

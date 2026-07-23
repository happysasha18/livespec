#!/usr/bin/env python3
"""check-matrix-reference.py — the generated matrix-Reference gate (SPEC INV-273, INV-269).

UNARMED until the row-477 conversion delivery converts TEST_MATRIX.md to the format-family member and
splices in the generated `## Reference` section; it arms in that same delivery (INV-272). The matrix is
named on the command line.

THE LAW: the matrix's `## Reference` section maps each spec anchor to the matrix rows covering it,
built from the body rows at freeze and output only (INV-273). This gate holds three faults, the sibling
shape of the generated-index gate (`guardrails/check-index-generated.py`):

  - DRIFT: the committed Reference differs from a fresh build off the current body — a hand edit, or a
    body that moved without a rebuild. Reds, since the Reference is not hand-kept.
  - BODY HAS AN ANCHOR THE REFERENCE MISSES: an anchor on a body row absent from the committed
    Reference. Reds, naming the anchor.
  - REFERENCE HAS AN ANCHOR NO BODY ROW CARRIES: an anchor in the committed Reference carried by no
    body row — an empty home. Reds, naming the anchor.

It declares its expected-non-empty input with the shared guard (INV-218): a body that parses to zero
converted rows reds by name rather than passing over nothing.

Usage:
  check-matrix-reference.py <matrix.md>
Exit 0 when the committed Reference equals the fresh build and body and Reference agree (printing the
reach line, INV-269); exit 1 naming each fault. Stdlib only.
"""
import importlib.util
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)
import specformat as sf  # noqa: E402 — green_reach + code_sort_key, the family's shared helpers
from nonempty_input import require_nonempty, VacuousInputError  # noqa: E402

import re  # noqa: E402

CHECK = "check-matrix-reference"
REFERENCE_HEAD = "## Reference"
# A line-anchored `## Reference` heading — never an inline mention in the preamble prose.
REFERENCE_SPLIT_RE = re.compile(r"(?m)^## Reference *$")


def _load_builder():
    """Load the (hyphen-named) builder module so the gate reuses its ONE parser — no re-implemented
    reader drifting from its sibling (the same one-reader discipline specformat.py holds for the
    index gates)."""
    path = os.path.join(REPO_ROOT, "scripts", "build-matrix-reference.py")
    spec = importlib.util.spec_from_file_location("build_matrix_reference", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _committed_table(section_text):
    """The markdown table lines of a committed `## Reference` section (leading `|`), so the intro
    sentence around the table never perturbs the drift comparison."""
    return "\n".join(l for l in section_text.splitlines() if l.strip().startswith("|"))


def main(argv):
    if len(argv) != 2:
        print("%s: usage: %s <matrix.md>" % (CHECK, os.path.basename(argv[0])))
        return 2
    matrix_path = argv[1]
    if not os.path.isfile(matrix_path):
        print("%s: cannot read %s — the gate stands on the matrix file." % (CHECK, matrix_path))
        return 1
    with open(matrix_path, encoding="utf-8") as f:
        text = f.read()

    b = _load_builder()

    try:
        require_nonempty(CHECK, "the matrix body rows", b.parse_rows(text))
    except VacuousInputError as e:
        print("%s: %s" % (CHECK, e))
        return 1

    if not REFERENCE_SPLIT_RE.search(text):
        print("%s: %s carries no '## Reference' section — the conversion splices it under the body "
              "with scripts/build-matrix-reference.py." % (CHECK, os.path.basename(matrix_path)))
        return 1

    section = REFERENCE_SPLIT_RE.split(text, 1)[1]
    fresh = b.build_reference_table(text)
    committed = _committed_table(section)
    body = b.body_anchors(text)
    committed_codes = b.table_anchors(section)

    problems = []
    if committed.strip() != fresh.strip():
        problems.append("the committed Reference differs from a fresh build off the current body — the "
                        "section is generated output, never hand-kept; rebuild it with "
                        "scripts/build-matrix-reference.py (INV-273).")
    missing = sorted(body - committed_codes, key=sf.code_sort_key)
    if missing:
        problems.append("%d anchor(s) on a body row are absent from the committed Reference "
                        "(INV-273): %s" % (len(missing), ", ".join(missing)))
    orphan = sorted(committed_codes - body, key=sf.code_sort_key)
    if orphan:
        problems.append("%d anchor(s) in the committed Reference are carried by no body row — an "
                        "empty home (INV-273): %s" % (len(orphan), ", ".join(orphan)))

    if problems:
        print("%s: %d Reference fault(s) in %s:" % (CHECK, len(problems), os.path.basename(matrix_path)))
        for p in problems:
            print("  - %s" % p)
        return 1

    n_rows = len(b.parse_rows(text))
    print(sf.green_reach(CHECK, [os.path.basename(matrix_path)], n_rows, n_rows,
                         "committed Reference equals the fresh build; %d anchors agree body-to-table"
                         % len(body)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

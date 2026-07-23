"""Generated-index symmetry — the standing suite test for PRODUCT_SPEC.md's closing code table
(ROADMAP row 196 lineage; re-aimed at the requirements format by row 445, SPEC INV-258/INV-259/INV-271).

The old `### Formal index` (hand-kept anchor/summary/section rows) retired at the row-445 conversion:
the closing table is now GENERATED output (`scripts/build-index.py`), embedded under `## Reference` and
committed as `PRODUCT_SPEC.index.md`, carrying locations only (INV-271). Its drift/agreement gate is
`guardrails/check-index-generated.py` (gate x), proven on the real tree by
tests/test_index_generated.py. This file keeps the two structural checks that gate does not own —
index<->body anchor symmetry over ALL body brackets (prose cross-references included, not only
criterion anchors) and per-prefix numbering density — plus their standing red-proof.

RETIRED with a named successor: the old cross-reference check (codes cited inside an index row's
SUMMARY resolve) — the generated table carries no summary text, and the drift check
(check-index-generated INV-258) already pins the table to a fresh build, which cannot emit a dangling
code. Successor pair: test_formal_index.check_cross_references -> check-index-generated /
tests/test_index_generated.py.

Zero dependencies beyond the stdlib and the sibling traceability helpers. Run:
    python3 -m pytest tests/test_formal_index.py -q
Every check reads the SHIPPED PRODUCT_SPEC.md on disk; the red-proof alone works on a copy.
"""

import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_traceability import read, expand, ANCHOR_TOKEN  # noqa: E402

INDEX_HEADING = "## Reference"

# Per-prefix numbering gaps pinned as EXPECTED (a NEW hole fails, these do not). Each gap names its
# reason, so a retired code cannot silently widen the set:
#   D-3, D-5 — decided decisions whose dated decided-ness moved out of the spec body at the row-445
#   conversion (no-history, INV-253): their substance is normative criteria under E-7 (the too-heavy-
#   surface rule) and E-13/E-16 (settings ladder + thin loader); the codes carry no criterion anchor.
#   D-6 — an open decision recorded in DECISIONS.md, cited in the body only on a [GAP: ...] line,
#   which is not a criterion anchor, so the generated table carries no D-6 row (INV-258).
EXPECTED_GAPS = {"D": [3, 5, 6]}


# --------------------------------------------------------------------------- parsers (text-in)
# Every parser takes the spec TEXT (not a path) so the red-proof can feed a mutated copy.

def index_rows(spec_text):
    """[(anchor, locations)] from the generated table's data rows under ## Reference."""
    index_part = spec_text.split(INDEX_HEADING, 1)[1]
    return re.findall(r"^\| (%s) \| (.*?) \|$" % ANCHOR_TOKEN, index_part, re.M)


def index_codes(spec_text):
    """Every index anchor, ranges expanded (T-1..T-7 -> T-1 … T-7)."""
    codes = set()
    for anchor, _locations in index_rows(spec_text):
        codes.update(expand(anchor))
    return codes


def _keep_token(tok):
    """A bracket token that is a real index code. Excluded by class:
      - `F-x` feature tags belong to the feature-COVERAGE trace (SPEC E-29/INV-73), never the table.
      - `D-x` decision codes: their record home is DECISIONS.md (the row-445 conversion moved the
        open-decisions section there); a D-code may ride a body [GAP: ...] line without a criterion
        anchor, so the generated table legitimately carries only the criterion-anchored D-codes.
    Not reached because they fail ANCHOR_TOKEN: `[default]`, `[target]`, `[GAP: ...]` prose, `[HH:MM]`
    — none carry a PREFIX-NUMBER, while any real code sharing the bracket is still lifted
    (anchors can share: `[T-14, INV-19]`)."""
    return not tok.startswith("F-") and not tok.startswith("D-")


def body_anchor_tokens(spec_text):
    """Every code used as a bracket anchor in the BODY (everything before ## Reference), ranges
    expanded. Anchors can share a bracket, so each bracket is scanned for every code-token."""
    body = spec_text.split(INDEX_HEADING, 1)[0]
    toks = set()
    for inside in re.findall(r"\[([^\[\]]*)\]", body):
        for tok in re.findall(ANCHOR_TOKEN, inside):
            if _keep_token(tok):
                toks.update(expand(tok))
    return toks


# --------------------------------------------------------------------------- checks (raise on defect)

def check_symmetry(spec_text):
    """Index <-> body anchor symmetry, both directions:
      - every expanded index code is anchored at least once in the body, and
      - every body bracket anchor (D-/F- classes aside, per _keep_token) is listed in the table."""
    idx = {c for c in index_codes(spec_text) if _keep_token(c)}
    body = body_anchor_tokens(spec_text)
    missing_in_body = sorted(idx - body)   # an index code no body clause anchors
    orphan_in_body = sorted(body - idx)    # a body anchor the table never lists
    assert not missing_in_body, \
        "index codes never anchored in the body: %s" % missing_in_body
    assert not orphan_in_body, \
        "body bracket anchors absent from the generated index: %s" % orphan_in_body


def check_numbering(spec_text):
    """Per prefix with numeric suffixes: no anchor TOKEN keyed twice (build-index emits one row per
    token, so a doubled row is a hand edit), and no numbering gap beyond the pinned EXPECTED_GAPS."""
    tokens = [anchor for anchor, _locations in index_rows(spec_text)]
    doubled = sorted({t for t in tokens if tokens.count(t) > 1})
    assert not doubled, "an anchor token keyed by two table rows (a hand edit): %s" % doubled
    per_prefix = {}
    for anchor in tokens:
        for code in expand(anchor):
            m = re.match(r"([A-Z]+)-(\d+)$", code)
            if m:
                per_prefix.setdefault(m.group(1), set()).add(int(m.group(2)))
    gaps = {}
    for prefix, nums in per_prefix.items():
        full = set(range(min(nums), max(nums) + 1))
        g = sorted(full - nums)
        if g:
            gaps[prefix] = g
    assert gaps == EXPECTED_GAPS, \
        "index numbering gaps changed (a new hole?): got %s, pinned %s" % (gaps, EXPECTED_GAPS)


# --------------------------------------------------------------------------- tests (on the real spec)

class TestFormalIndex(unittest.TestCase):
    def spec(self):
        return read("PRODUCT_SPEC.md")

    def test_committed_index_equals_embedded_table(self):
        """The committed PRODUCT_SPEC.index.md and the table embedded under ## Reference are one
        artifact in two places; a drift between them is a hand edit (INV-258). The committed file's
        agreement with a FRESH BUILD is gate x's own check (tests/test_index_generated.py)."""
        committed = [l for l in read("PRODUCT_SPEC.index.md").splitlines()
                     if l.startswith("| ")]
        embedded = [l for l in self.spec().split(INDEX_HEADING, 1)[1].splitlines()
                    if l.startswith("| ")]
        self.assertEqual(committed, embedded,
                         "PRODUCT_SPEC.index.md and the spec's embedded ## Reference table drifted")

    def test_index_and_body_anchor_symmetry(self):
        check_symmetry(self.spec())

    def test_index_numbering_contiguous(self):
        check_numbering(self.spec())

    def test_the_checks_catch_seeded_defects(self):
        """RED-PROOF, standing: seed each defect class into a copy of the real spec and assert the
        owning check fires, keeping the red for both checks alive forever."""
        spec = self.spec()

        # Defect 1 — remove one index row. E-22 is anchored in the body, so dropping its table row
        # leaves an orphan the symmetry check must catch.
        self.assertIn("[E-22", spec.split(INDEX_HEADING, 1)[0],
                      "fixture assumption broke: E-22 not anchored in body")
        removed = re.sub(r"(?m)^\| E-22 \|.*\n", "", spec)
        self.assertEqual(removed.count("\n| E-22 |"), 0, "E-22 index row not removed")
        with self.assertRaises(AssertionError):
            check_symmetry(removed)

        # Defect 2 — double one row. A second M-3 row is a hand edit the numbering check must see.
        m3 = re.search(r"(?m)^\| M-3 \|.*\n", spec).group(0)
        duped = spec.replace(m3, m3 + m3, 1)
        with self.assertRaises(AssertionError):
            check_numbering(duped)

        # And the un-mutated spec passes both (the green baseline the red-proof sits beside).
        check_symmetry(spec)
        check_numbering(spec)


if __name__ == "__main__":
    unittest.main(verbosity=2)

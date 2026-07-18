"""Formal-index symmetry — the standing suite test for PRODUCT_SPEC.md's closing index
(ROADMAP row 196; SPEC E-14/E-15 traceability territory, mechanized).

Tonight's manual index audit (2026-07-10) was fully clean, but four of its five checks
existed only as a hand-walk. This file makes three of them re-run at every suite pass, and
pins the fourth's red-proof forever by seeding synthetic defects into a copy of the spec and
asserting each check catches its own defect. Summary-drift stays the prover's judgment call —
no machine owns it, and this file does not pretend to.

Zero dependencies beyond the stdlib and the sibling traceability helpers. Run:
    python3 -m pytest tests/test_formal_index.py -q
Every check reads the SHIPPED PRODUCT_SPEC.md on disk; the red-proof alone works on a copy.
"""

import os
import re
import sys
import unittest

# Reuse the traceability suite's proven helpers rather than re-deriving them (row 196 brief):
#   read()               — repo-root file reader
#   expand()             — "T-1..T-7" -> [T-1 ... T-7]; a plain anchor passes through
#   spec_index_anchors() — the on-disk index anchors, ranges expanded (raw list, set)
#   ANCHOR_TOKEN         — the code-token regex "PREFIX-NUMBER" (+ optional range tail)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_traceability import read, expand, spec_index_anchors, ANCHOR_TOKEN  # noqa: E402

INDEX_HEADING = "### Formal index"

# The current index carries NO numbering gaps (computed 2026-07-10 across every prefix). This
# is the pinned expected gap set: a NEW hole fails the numbering check, while any historical gap
# that ever existed would be listed here with its reason so it does not hard-fail. Today: none.
EXPECTED_GAPS = {}  # e.g. {"INV": [63]} would pin a retired-code hole; empty = a fully dense index.
# Reconciled at the integration of the 2026-07-18 three-lane run: lanes landed INV-215, INV-216, INV-217
# onto a main already carrying INV-213/214, so INV-213..217 are contiguous and the index is dense again.


# --------------------------------------------------------------------------- parsers (text-in)
# Every parser takes the spec TEXT (not a path) so the red-proof can feed a mutated copy.

def index_rows(spec_text):
    """[(anchor, summary, section)] from the Formal index table's data rows."""
    index_part = spec_text.split(INDEX_HEADING, 1)[1]
    return re.findall(r"^\| (%s) \| (.*?) \| (.*?) \|$" % ANCHOR_TOKEN, index_part, re.M)


def index_codes(spec_text):
    """Every index anchor, ranges expanded (T-1..T-7 -> T-1 … T-7)."""
    codes = set()
    for anchor, _summary, _section in index_rows(spec_text):
        codes.update(expand(anchor))
    return codes


def _keep_token(tok):
    """A bracket token that is a real Formal-index anchor, vs the conventions the manual
    audit found are NOT index codes. ANCHOR_TOKEN already requires a PREFIX-NUMBER shape, so
    the pure-word tags never reach here; the one live exclusion is the feature layer:
      - `[feature: F-x]` heading tags belong to the feature-COVERAGE trace (SPEC E-29/INV-73),
        a separate traceability layer above the anchor matrix — never the Formal index. Any
        F-prefixed token (F-x today, a hypothetical F-1 tomorrow) is excluded here.
    Not reached because they fail ANCHOR_TOKEN, hence never tokens, documented so a future
    reader does not re-add them: `[default]`, `[target]`, `[target: ...]`, `[target, E-6]`
    (the E-6 inside DOES count — a genuine cross-ref anchor), `[HH:MM]`, `[~]`, `[-suffix]`,
    and bare file references — none carry a PREFIX-NUMBER, so ANCHOR_TOKEN skips them while
    still lifting any real code sharing the bracket (anchors can share: `[T-14, INV-19]`)."""
    return not tok.startswith("F-")


def body_anchor_tokens(spec_text):
    """Every code used as a bracket anchor in the BODY prose (everything before the Formal
    index heading), ranges expanded. Anchors can share a bracket, so each bracket is scanned
    for every code-token it holds."""
    body = spec_text.split(INDEX_HEADING, 1)[0]
    toks = set()
    for inside in re.findall(r"\[([^\[\]]*)\]", body):
        for tok in re.findall(ANCHOR_TOKEN, inside):
            if _keep_token(tok):
                toks.update(expand(tok))
    return toks


# --------------------------------------------------------------------------- checks (raise on defect)
# Each raises AssertionError on the defect it owns, so the red-proof can assert it fires.

def check_symmetry(spec_text):
    """Index <-> body anchor symmetry, both directions:
      - every expanded index code is anchored at least once in the body prose, and
      - every body bracket anchor is listed in the index."""
    idx = index_codes(spec_text)
    body = body_anchor_tokens(spec_text)
    missing_in_body = sorted(idx - body)   # an index code no body clause anchors
    orphan_in_body = sorted(body - idx)    # a body anchor the index never lists
    assert not missing_in_body, \
        "index codes never anchored in the body prose: %s" % missing_in_body
    assert not orphan_in_body, \
        "body bracket anchors absent from the Formal index: %s" % orphan_in_body


def check_numbering(spec_text):
    """Per prefix with numeric suffixes: no duplicate numbers, and no gap beyond the pinned
    EXPECTED_GAPS set (a NEW gap fails)."""
    per_prefix = {}
    for anchor, _summary, _section in index_rows(spec_text):
        for code in expand(anchor):
            m = re.match(r"([A-Z]+)-(\d+)$", code)
            if m:
                per_prefix.setdefault(m.group(1), []).append(int(m.group(2)))
    dups = {}
    gaps = {}
    for prefix, nums in per_prefix.items():
        seen = sorted(nums)
        d = sorted({n for n in seen if seen.count(n) > 1})
        if d:
            dups[prefix] = d
        full = set(range(min(seen), max(seen) + 1))
        g = sorted(full - set(seen))
        if g:
            gaps[prefix] = g
    assert not dups, "duplicate index numbers within a prefix: %s" % dups
    assert gaps == EXPECTED_GAPS, \
        "index numbering gaps changed (a new hole?): got %s, pinned %s" % (gaps, EXPECTED_GAPS)


def check_cross_references(spec_text):
    """Every code cited inside an index row's summary text resolves to an existing index code
    (F-x feature tags excluded, as they are not index codes)."""
    idx = index_codes(spec_text)
    unresolved = []
    for anchor, summary, _section in index_rows(spec_text):
        for tok in re.findall(ANCHOR_TOKEN, summary):
            if not _keep_token(tok):
                continue
            for code in expand(tok):
                if code not in idx:
                    unresolved.append((anchor, code))
    assert not unresolved, \
        "index summaries cite codes absent from the index: %s" % unresolved


# --------------------------------------------------------------------------- tests (on the real spec)

class TestFormalIndex(unittest.TestCase):
    def spec(self):
        return read("PRODUCT_SPEC.md")

    def test_index_and_body_anchor_symmetry(self):
        spec = self.spec()
        # Bind to the reused on-disk helper: our text-parametrized parser agrees with it.
        self.assertEqual(index_codes(spec), spec_index_anchors()[1],
                         "index_codes() drifted from test_traceability.spec_index_anchors()")
        check_symmetry(spec)

    def test_index_numbering_contiguous(self):
        check_numbering(self.spec())

    def test_index_cross_references_resolve(self):
        check_cross_references(self.spec())

    def test_the_checks_catch_seeded_defects(self):
        """RED-PROOF, standing: seed each defect class into a copy of the real spec and assert
        the owning check fires. This keeps the red for all three checks alive forever, instead
        of a one-off manual mutation run."""
        spec = self.spec()

        # Defect 1 — remove one index row. E-22 is anchored in the body prose ([E-22] in the
        # decision-page clause), so dropping its index row leaves an orphan the symmetry check
        # must catch.
        self.assertIn("[E-22]", spec.split(INDEX_HEADING, 1)[0], "fixture assumption broke: [E-22] not in body")
        removed = re.sub(r"(?m)^\| E-22 \|.*\n", "", spec)
        self.assertEqual(removed.count("\n| E-22 |"), 0, "E-22 index row not removed")
        with self.assertRaises(AssertionError):
            check_symmetry(removed)

        # Defect 2 — duplicate one code. Insert a second M-3 index row; the numbering check
        # must see M-3 twice.
        m3 = re.search(r"(?m)^\| M-3 \|.*\n", spec).group(0)
        duped = spec.replace(m3, m3 + m3, 1)
        with self.assertRaises(AssertionError):
            check_numbering(duped)

        # Defect 3 — add a dangling cross-reference. Append a fake code to an index summary; it
        # resolves to nothing, so the cross-reference check must fire.
        dangling = re.sub(r"(?m)^(\| S-0 \| [^|]*?)( \|)", r"\1 [Z-999]\2", spec, count=1)
        self.assertIn("[Z-999]", dangling, "dangling cross-reference not seeded")
        with self.assertRaises(AssertionError):
            check_cross_references(dangling)

        # And the un-mutated spec passes all three (the green baseline the red-proof sits beside).
        check_symmetry(spec)
        check_numbering(spec)
        check_cross_references(spec)


if __name__ == "__main__":
    unittest.main(verbosity=2)

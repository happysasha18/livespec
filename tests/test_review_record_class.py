"""The review-record class is declared once (SPEC INV-156, ROADMAP row 323).

The prover record and the design-review record were declared mirror siblings, but the
skill-creator craft-walk record and the verify-by-deed audit — the same kind of pass —
were never named members of a class. INV-156 declares the class once, names every review
pass's record a member, and states verify's deliberate difference (its outcome lands in
the landing record, not a dated file of this class).

Zero dependencies beyond the stdlib; run from the repo root:
  python3 -m pytest -q tests
"""

import unittest

from conftest import read_flat


class TestReviewRecordClass(unittest.TestCase):
    def setUp(self):
        self.spec = read_flat("PRODUCT_SPEC.md")

    def test_review_record_class_declared(self):
        self.assertIn("Every review pass writes its record of one class.", self.spec,
                      "the review-record class clause is missing from the spec body")
        self.assertIn("[INV-156]", self.spec, "INV-156 has no body owner")

    def test_names_every_member(self):
        # every review pass is named a member (or the named difference) with its anchor
        for phrase, anchor in (
            ("the prover's spec re-check", "[INV-140]"),
            ("the design review", "[INV-141]"),
            ("the periodic adversarial audit", "[INV-145]"),
            ("the verify-by-deed audit", "[INV-46]"),
        ):
            self.assertIn(phrase, self.spec, "review-record class does not name member: %s" % phrase)
            self.assertIn(anchor, self.spec, "member anchor missing: %s" % anchor)
        # the whole-pack skill-creator craft walk rides the audit member
        self.assertIn("skill-creator craft walk", self.spec, "the craft walk is not named")
        # the shared dated-file shape names each home
        for home in ("`docs/prover/`", "`docs/design-review/`", "`docs/audit/`"):
            self.assertIn(home, self.spec, "class shape does not name the record home: %s" % home)

    def test_states_verify_difference(self):
        self.assertIn("the verify-by-deed audit is the one deliberate difference", self.spec.lower(),
                      "verify's deliberate difference from the class is not stated")
        self.assertIn("in the landing record's own accounting rather than a dated file of this class",
                      self.spec, "verify's difference is not stated as landing-record vs a dated class file")
        # the per-landing skill-creator review shares verify's landing-record home, not a class file
        self.assertIn("the per-landing skill-creator review it runs", self.spec,
                      "the per-landing skill-creator review is not placed with verify")

    def test_formal_index_and_ownership(self):
        self.assertIn("| INV-156 |", self.spec, "INV-156 has no Formal-index row")
        # the class is declared once; the two pack-owned record skills point at it, never restate it
        pp = read_flat("skills/product-prover/SKILL.md")
        dr = read_flat("skills/design-reviewer/SKILL.md")
        for body, who in ((pp, "product-prover"), (dr, "design-reviewer")):
            self.assertIn("review-record class", body, "%s does not point at the class" % who)
            self.assertIn("INV-156", body, "%s does not cite INV-156" % who)


if __name__ == "__main__":
    unittest.main()

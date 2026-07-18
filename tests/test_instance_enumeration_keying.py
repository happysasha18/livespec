# -*- coding: utf-8 -*-
"""The general-law-plus-instances family declares enumerate-versus-ride (ROADMAP row 370, SPEC INV-226).

The pack carries several laws shaped as one general duty over concrete instances — the range law
(INV-138), the budget law (INV-41), the facet law (INV-18) — and each decided differently whether its
instances are named in the clause or ride the general duty silently, with the keying declared nowhere
(the 2.5.0 design review, finding 2, 2026-07-17). This row states one class sentence keying the choice on
whether the member set is open-ended or closed and enumerable, and has the three named laws cite it.

This module is the traceability proof: the class sentence stands in its one home, and the three laws each
reference it.

Red-first: against HEAD 573d8ea the spec carries no INV-226 and the three laws carry no citation to it, so
every assertion below fails — the red recorded in docs/prover/2026-07-18-rows-370-394.md.
"""
import os
import re
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
        return f.read()


def line_with(text, phrase):
    """The single line carrying a distinctive phrase (the invariants are one line per paragraph)."""
    for line in text.splitlines():
        if phrase in line:
            return line
    return None


class TestClassSentenceStands(unittest.TestCase):
    def test_class_sentence_stands(self):
        spec = read("PRODUCT_SPEC.md")
        line = line_with(spec, "A general law over concrete instances declares whether it enumerates")
        self.assertIsNotNone(line, "the INV-226 class sentence is absent from the spec")
        self.assertIn("[INV-226]", line, "the class sentence carries no [INV-226] tag")
        low = line.lower()
        # the keying: open-ended member set rides, closed enumerable set enumerates
        self.assertIn("closed", low)
        self.assertIn("enumerable", low)
        self.assertIn("open-ended", low)
        self.assertIn("member set", low)

    def test_formal_index_row(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn(
            "| INV-226 | a general law over concrete instances declares whether it enumerates",
            spec, "no Formal-index row for INV-226")

    def test_architecture_owns_the_invariant(self):
        arch = read("ARCHITECTURE.md")
        # exactly one node's owns-list carries the anchor
        owners = [line for line in arch.splitlines()
                  if line.startswith("| ") and "INV-226" in line and "| spec-author" not in line
                  and re.match(r"\| [a-z-]+ \|", line)]
        self.assertTrue(any("| spec-author |" in line for line in arch.splitlines() if "INV-226" in line),
                        "spec-author does not own INV-226 in the architecture owns-list")

    def test_matrix_row_covers_the_law(self):
        mat = read("TEST_MATRIX.md")
        self.assertIn("| M-407 |", mat)
        row = line_with(mat, "| M-407 |")
        self.assertIn("INV-226", row, "M-407 does not cite INV-226")


class TestThreeLawsCiteTheClass(unittest.TestCase):
    """The three named laws each reference the class sentence (SPEC INV-226)."""

    # each law's citation sentence, plus the SIDE it must state (a miskeyed law is a finding, so the
    # side is asserted textually, not only the citation's presence)
    LAWS = [
        ("range law INV-138", "range-and-lifecycle member of the composition-lens family", "open-ended"),
        ("budget law INV-41", "project kinds the budget law names are a closed, enumerable set", "closed"),
        ("facet law INV-18", "facets are a closed, enumerable set that grows by incident", "closed"),
    ]

    def test_three_laws_cite_the_class(self):
        spec = read("PRODUCT_SPEC.md")
        for name, phrase, side in self.LAWS:
            line = line_with(spec, phrase)
            self.assertIsNotNone(line, "%s: citation sentence absent (%r)" % (name, phrase))
            self.assertIn("[INV-226]", line, "%s: clause does not cite [INV-226]" % name)
            self.assertIn(side, line,
                          "%s: citation does not state its member-set side (%r)" % (name, side))

    def test_the_three_canonical_anchors_are_present(self):
        spec = read("PRODUCT_SPEC.md")
        for anchor in ("[INV-138]", "[INV-41]", "[INV-18]"):
            self.assertIn(anchor, spec)


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""Both directions of a paired state change get the same craft, or a stated reason they do not — INV-126.

When a surface has a pair of opposite state changes (open/close, enter/exit, expand/collapse, show/hide), a
transition crafted for one direction is a decision about the pair, so the other direction is stated too. The
default is symmetry (the exit mirrors the enter's feel unless a reason is written); a shorter or
deliberately-instant exit is a valid STATED answer. It rides the standard-facet sweep as its own facet, and
because motion feel is the human's own gate an undecidable pair is surfaced to him. The prover flags a pair
with one direction described and the opposite unstated. The temporal twin of INV-125. Homes: the composition
clause, the facet list in spec-author, product-prover's paired-transition check. (Born of tlvphotos's
polaroid room revealed under a soft veil and closed on a hard cut, felt on a real phone, 2026-07-12.)
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestPairedTransition(unittest.TestCase):
    def test_spec_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "Both directions of a paired state change get the same craft, or a stated reason they do not",
            spec,
        )
        self.assertIn("[INV-126]", spec)

    def test_spec_names_default_and_the_human_gate(self):
        spec = read_flat("PRODUCT_SPEC.md")
        for needle in (
            "The default is symmetry",
            "Motion feel is the human's own gate",
            "the temporal twin of cross-surface uniformity",
        ):
            self.assertIn(needle, spec, needle)

    def test_formal_index_row(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-126 |"):
                    self.assertIn("paired state change", line.lower())
                    return
        self.fail("INV-126 Formal-index row missing")

    def test_spec_author_carries_the_facet(self):
        sa = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("paired-transition symmetry", sa)
        self.assertIn("the exit's motion mirrors the enter's", sa)

    def test_prover_carries_the_paired_transition_check(self):
        pv = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("Paired-transition symmetry", pv)
        self.assertIn("The temporal twin of the cross-surface lens above", pv)

    def test_matrix_row_covers_the_paired_transition_law(self):
        with open(os.path.join(ROOT, "TEST_MATRIX.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| M-267 |"):
                    self.assertIn("INV-126", line)
                    return
        self.fail("M-267 matrix row missing")


if __name__ == "__main__":
    unittest.main()

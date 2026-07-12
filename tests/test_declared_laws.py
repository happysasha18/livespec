"""Declared cross-cutting laws: one home, a prover station, an author habit — M-237 (SPEC INV-101, row 223).

His 2026-07-10 ~10:38 word from the worked miss: analytics covered some beats while whole
surfaces emitted nothing, and only his eye found it. The spec names its cross-cutting laws in
one declared-laws home; every new surface's section states its line against each declared law
(the clause or a dated exemption) before the prover reads it; the prover's station enumerates
every surface and transition per declared law. String rows on the three homes.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestDeclaredLaws(unittest.TestCase):

    def test_the_home_and_the_packs_own_list(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("declared-laws home", spec)
        self.assertIn("the declared laws are three", spec)
        self.assertIn("dated exemption", spec)

    def test_the_prover_station(self):
        prover = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("Declared cross-cutting laws", prover)
        self.assertIn("dated exemption", prover)
        self.assertIn("ranks as a broken invariant", prover)

    def test_the_author_habit(self):
        author = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("declared-laws home", author)
        self.assertIn("before the prover", author)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-101]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-101 |"):
                    self.assertIn("dated exemption", line)
                    return
        self.fail("INV-101 index row missing")


if __name__ == "__main__":
    unittest.main()

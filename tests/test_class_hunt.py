"""A confirmed bug drives a class hunt before it closes — INV-124.

Four moves, not one: (1) name the defect abstractly and go FIND the un-seen siblings, fixing all in the
same change; (2) check the architecture for a structural cause; (3) check the spec — a spec silent on the
broken behaviour is the real defect, fixed first so the prover can flag it; (4) escalate to the human when
the class boundary needs his read. The product-prover carries the class lens for the same questions. The
four moves are the bug door's close condition. Homes: the F-bug spec clause, build-pipeline's bug entry,
product-prover's class lens, base rule 14. (Born of the exhibition's pinch-zoom bug — one report turned
into five live siblings, 2026-07-12.)
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestClassHunt(unittest.TestCase):
    def test_base_rule_14_goes_and_finds_the_class(self):
        base = read_flat("skills/live-spec-base/SKILL.md")
        self.assertIn("go find the class, sweep the look-alikes", base)
        self.assertIn("the siblings not yet seen", base)
        self.assertIn("escalate to the human when the class boundary needs his read", base)

    def test_spec_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("A confirmed bug drives a class hunt before it closes", spec)
        self.assertIn("[INV-124]", spec)

    def test_spec_names_the_four_moves(self):
        spec = read_flat("PRODUCT_SPEC.md")
        for needle in (
            "search every surface",
            "a structural cause",
            "fix the spec first so the prover can flag it",
            "the class boundary needs the human's read",
        ):
            self.assertIn(needle, spec, needle)

    def test_formal_index_row(self):
        # The generated index carries locations only (SPEC INV-271); "class hunt" prose lives in the
        # body criterion (asserted above). Here the index must map INV-124 to at least one location.
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-124 |"):
                    self.assertRegex(line, r"R\d+\.\d+")
                    return
        self.fail("INV-124 index row missing")

    def test_build_pipeline_bug_entry_drives_the_hunt(self):
        bp = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("A confirmed bug drives a class hunt before it closes (SPEC INV-124)", bp)
        self.assertIn("The hunt is four moves:", bp)

    def test_prover_carries_the_class_lens(self):
        pv = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("Class lens", pv)
        self.assertIn("the document-side face of the confirmed-bug class hunt", pv)

    def test_matrix_row_covers_the_class_hunt(self):
        with open(os.path.join(ROOT, "TEST_MATRIX.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| M-265 |"):
                    self.assertIn("INV-124", line)
                    return
        self.fail("M-265 matrix row missing")


if __name__ == "__main__":
    unittest.main()

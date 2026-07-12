"""A cross-surface policy is stated at the surface-class level and held uniform — INV-125.

When a decision governs an interaction KIND that lives on several sibling surfaces (a gesture policy, an
affordance, an input-to-action mapping), the spec states it once at the surface-class level and enumerates
the surfaces it governs; a policy written for one surface while siblings exist is a spec defect. The prover
writes itself the check (enumerate the surfaces of that kind from the surface registry, flag any the clause
does not cover); a product with a DOM instantiates the completeness guardrail to assert the policy across
every registered sibling root. The preventive twin of the class hunt (INV-124). Homes: the composition
clause, product-prover's cross-surface-policy lens, build-pipeline's completeness guardrail. (Born of
tlvphotos's pinch-zoom policy shipped for the walk alone, 2026-07-12.)
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestCrossSurfacePolicy(unittest.TestCase):
    def test_spec_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "A cross-surface policy is stated at the surface-class level and held uniform across its siblings",
            spec,
        )
        self.assertIn("[INV-125]", spec)

    def test_spec_names_the_class_rule_and_the_two_holds(self):
        spec = read_flat("PRODUCT_SPEC.md")
        for needle in (
            "the clause names the class and enumerates the surfaces it governs",
            "is a spec defect",
            "enumerates the surfaces of that kind from the surface registry",
            "the preventive twin of the class hunt",
        ):
            self.assertIn(needle, spec, needle)

    def test_formal_index_row(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-125 |"):
                    self.assertIn("surface-class", line.lower())
                    return
        self.fail("INV-125 Formal-index row missing")

    def test_prover_carries_the_cross_surface_lens(self):
        pv = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("Cross-surface policy uniformity", pv)
        self.assertIn("The preventive twin of the class lens above", pv)

    def test_build_pipeline_completeness_holds_uniformity(self):
        bp = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("cross-surface policy uniformity (SPEC INV-125)", bp)
        self.assertIn("EVERY registered sibling root", bp)

    def test_matrix_row_covers_the_uniformity_law(self):
        with open(os.path.join(ROOT, "TEST_MATRIX.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| M-266 |"):
                    self.assertIn("INV-125", line)
                    return
        self.fail("M-266 matrix row missing")


if __name__ == "__main__":
    unittest.main()

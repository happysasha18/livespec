"""The full pass proves the architecture beside the spec (SPEC INV-116, row 271).

Every milestone gate [M-1] and every push gate [M-6] runs the product-prover over
ARCHITECTURE.md as well as PRODUCT_SPEC.md, so the design-level seams meet the same
structured review the spec gets. The taste call: commit-time freshness only, no content-grep
— the guardrail side of this (tests/test_guardrails.py) proves the freshness mechanics; this
file proves the spec says so.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestArchitectureProvedAtFullPass(unittest.TestCase):
    def test_full_architecture_reprove_phrase(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("full architecture re-prove", spec)

    def test_both_documents_named_phrase(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("PRODUCT_SPEC.md and ARCHITECTURE.md", spec)

    def test_spec_anchor(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-116]", spec)

    def test_spec_anchor_and_index(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-116 |") and "INV-116" in line and "architecture" in line.lower():
                    return
        self.fail("INV-116 index row missing or does not carry both INV-116 and architecture")


if __name__ == "__main__":
    unittest.main()

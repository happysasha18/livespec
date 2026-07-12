"""The full pass compaction discipline (SPEC INV-115, row 272).

Compact means there is no redundant information: a fact lives once, in one home, with a
pointer from everywhere else that needs it. A pass removes only redundancy and keeps
anything whose removal would change the meaning or a reader's understanding. Compaction is
per-item judgment, kin to the removal-accounting duty (INV-109).
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestCompactionDiscipline(unittest.TestCase):
    def test_fact_lives_once_phrase(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("a fact lives once, in one home", spec)

    def test_removal_keeps_meaning_phrase(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "whose removal would change the meaning or a reader's understanding", spec
        )

    def test_per_item_judgment_phrase(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("compaction is per-item judgment", spec)

    def test_spec_anchor(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-115]", spec)

    def test_spec_anchor_and_index(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-115 |") and "INV-115" in line and "compact" in line.lower():
                    return
        self.fail("INV-115 index row missing or does not carry both INV-115 and compact")


if __name__ == "__main__":
    unittest.main()

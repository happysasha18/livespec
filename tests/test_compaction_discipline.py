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


class TestCompactionIsContinuous(unittest.TestCase):
    """INV-164 (the 2.0 method rule): compaction runs at every push, held by a mechanical gate, not
    saved for the milestone; and the deeper rule — a machine-verifiable quality is a gate, not a
    habit. This is the fix for the spec bloating when compaction ran milestone-only (2026-07-15)."""

    def test_machine_verifiable_is_a_gate_not_a_habit(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("any quality a machine can verify is wired as a blocking gate", spec)
        self.assertIn("a quality left to attention is a defect of the method", spec)

    def test_compaction_is_continuous(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-164]", spec)
        self.assertIn("run at every push", spec)

    def test_index_row_present(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-164 |") and "compaction runs continuously" in line:
                    return
        self.fail("INV-164 index row missing or not carrying the continuous-compaction claim")

    def test_base_rulebook_carries_the_principle(self):
        """The method rule reaches every project through the base rulebook (rule 30, SPEC INV-164)."""
        base = read_flat("skills/live-spec-base/SKILL.md")
        self.assertIn("A quality a machine can verify is enforced by a gate", base)
        self.assertIn("A quality left to attention is a defect of the method", base)
        self.assertIn("SPEC INV-164", base)

    def test_build_pipeline_carries_compaction_every_pass(self):
        """Baked into build-pipeline: compaction is a station run every pass (SPEC INV-164)."""
        pipe = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("INV-164", pipe)


if __name__ == "__main__":
    unittest.main()

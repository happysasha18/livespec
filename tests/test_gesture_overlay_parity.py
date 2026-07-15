"""INV-165 — the design review's standing motion-parity lens (the tlvphotos pinch miss, 2026-07-15).

A gesture / overlay / motion spec triggers a standing lens the design review runs by construction,
naming three same-kind groups the bottom-up similarity lens (INV-141) can miss: entry mirrors exit,
every object type behaves alike, every position behaves alike. Landed as the capstone fix for a real
review miss: a shipped pinch whose desktop entry did not mirror its exit, a phone pinch-out that would
not fly the picture home, and a door picture that behaved differently by slot — none surfaced by a
review that carried only the bottom-up lens.
"""
import os
import unittest

from conftest import ROOT, read_flat


def _read(rel):
    return open(os.path.join(ROOT, rel), encoding="utf-8").read()


class TestGestureOverlayParityLens(unittest.TestCase):
    def test_spec_clause_names_the_three_groups(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("standing motion-parity lens", spec)
        # entry mirrors exit
        self.assertIn("entry mirrors exit", spec)
        self.assertIn("the way out is the way in reversed", spec)
        # every object type behaves alike, each to its own rectangle
        self.assertIn("every object type the gesture acts on behaves alike", spec)
        self.assertIn("lands back on its own on-screen rectangle", spec)
        # every position behaves alike
        self.assertIn("every position behaves alike", spec)

    def test_spec_anchor_and_index_row(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-165]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-165 |") and "motion-parity lens" in line:
                    return
        self.fail("INV-165 Formal-index row missing or not carrying the motion-parity lens")

    def test_design_reviewer_skill_carries_the_lens(self):
        skill = _read("skills/design-reviewer/SKILL.md")
        self.assertIn("standing motion-parity lens", skill)
        self.assertIn("SPEC INV-165", skill)
        for group in ("Entry mirrors exit", "Every object type behaves alike",
                      "Every position behaves alike"):
            self.assertIn(group, skill, "design-reviewer lens missing group: %s" % group)
        # it is registered as the echo channel's second producer
        self.assertIn("two producers", skill)

    def test_architecture_owns_165_under_design_reviewer(self):
        arch = _read("ARCHITECTURE.md")
        for line in arch.splitlines():
            if line.startswith("| design-reviewer |") and "INV-165" in line:
                return
        self.fail("the design-reviewer node does not own INV-165")

    def test_matrix_row_present(self):
        with open(os.path.join(ROOT, "TEST_MATRIX.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| M-314 |") and "INV-165" in line:
                    return
        self.fail("M-314 (INV-165) matrix row missing")


if __name__ == "__main__":
    unittest.main()

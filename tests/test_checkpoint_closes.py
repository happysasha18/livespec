"""A landing closes the checkpoints it shipped — M-240 (SPEC INV-107, row 226).

The closing half of the checkpoint law. The audit (2026-07-10) found two engine checkpoints still
reading "not started" after everything in them shipped, so a resuming session would have redone done
work. A landing that ships a checkpoint's items flips that checkpoint to its closed state in the same
landing; a checkpoint whose items all live in git history is stale by definition. String rows on the
law's two homes (the spec breakpoint clause + base rule 6) plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestCheckpointClosesLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/live-spec-base/SKILL.md")

    def test_closing_half_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "A landing that ships a checkpoint's items flips that checkpoint "
                "to its closed state in the same landing",
                body,
                home,
            )
            self.assertIn("so a returning session never reopens finished work", body, home)

    def test_stale_checkpoint_is_a_defect_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "A checkpoint whose items all live in git history is stale by definition "
                "and reads as a resume defect",
                body,
                home,
            )

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-107]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-107 |"):
                    self.assertIn("landing", line)
                    return
        self.fail("INV-107 index row missing")


if __name__ == "__main__":
    unittest.main()

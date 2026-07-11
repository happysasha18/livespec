"""A test's expected value derives independently of the code under test — M-238 (SPEC INV-102, row 224).

His 2026-07-10 ~11:00 word, from row 220's audit (item 3): green suites missed real walk bugs because
tests recomputed the code's own formula as the expected value, so the assertion only proved the code
equal to itself. A test's expected value must come from an independent source — a hand-computed
constant, an independent derivation, or a recorded real output reviewed by a human. String rows on the
law's two homes plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestMirrorAssertionBanLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/test-author/SKILL.md")

    def test_independence_stated_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("derives independently of the code under test", body, home)
            self.assertIn("a mirror that can never catch the formula being wrong", body, home)

    def test_legal_sources_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "a hand-computed constant, an independent derivation, or a recorded real output",
                body,
                home,
            )

    def test_boundary_stated_in_spec(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("A round-trip or property test over the outputs is legal", spec)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-102]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-102 |"):
                    self.assertIn("mirror", line)
                    return
        self.fail("INV-102 index row missing")


if __name__ == "__main__":
    unittest.main()

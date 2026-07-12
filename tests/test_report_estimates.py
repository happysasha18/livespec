"""Time estimates said, then settled — matrix row M-222 (SPEC INV-93, row 232).

His 2026-07-10 ~11:36 word, raised ~13:20 after a session reported estimates loosely: every ask
gets an honest time range at its echo, long work is explained up front in plain steps, a long
stretch occasionally says how much remains, and the landing report settles estimate against
actual. String rows on the two homes: the spec clause and the communicator skill.
"""

import os
import unittest

from conftest import ROOT, read


class TestTimeEstimatesLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/communicator/SKILL.md")

    def test_estimate_at_the_echo(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("honest time range", body, home)
            self.assertIn("never a guess dressed as a promise", body, home)

    def test_long_work_explained_and_tracked(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("explained up front in plain steps", body, home)
            self.assertIn("roughly how much remains", body, home)

    def test_landing_settles_estimate_against_actual(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("estimate beside the actual", body, home)

    def test_spec_anchor_and_index(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("[INV-93]", spec)
        self.assertIn("| INV-93 |", spec)


if __name__ == "__main__":
    unittest.main()

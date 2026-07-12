"""Detached work stays visible — matrix row M-232 (SPEC INV-35 tightened, row 248).

His 2026-07-10 ~17:10 word from the track-coach window: twice a multi-minute background run
went silent and read as lost. A detached operation (a background command or a delegated worker
the chat does not stream) expected past ~2 minutes opens with a START line, keeps a beat every
~2 minutes or per stage, and closes with a DONE digest. String rows on the two homes: the spec
clause and the communicator skill.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestDetachedWorkVisibility(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/communicator/SKILL.md")

    def test_cadence_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("expected to run past ~2 minutes detached", body, home)
            self.assertIn("START line", body, home)
            self.assertIn("every ~2 minutes or at each stage", body, home)
            self.assertIn("DONE digest", body, home)

    def test_the_trap_is_named(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("shows in no agent panel", body, home)
            self.assertIn("reads as lost", body, home)

    def test_mechanism_free_visibility_required(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("visibility is the requirement", body, home)

    def test_spec_index_row_carries_the_cadence(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-35 |"):
                    self.assertIn("START line", line)
                    self.assertIn("DONE digest", line)
                    return
        self.fail("INV-35 index row missing")


if __name__ == "__main__":
    unittest.main()

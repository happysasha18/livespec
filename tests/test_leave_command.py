"""The leave-command reaches a shutdown-safe stop — matrix row M-224 (SPEC INV-95, row 235).

His 2026-07-10 ~13:30 word from the cafe: one spoken leave-word makes the session wind down —
workers halted or landed (a sleeping machine kills them mid-write), every lane at its checkpoint,
green work committed, and one closing line says the machine is safe to power off plus what
resumes where. String rows on the three homes: the spec clause, the communicator's reporting
rules, and the base checkpoint rule.
"""

import os
import unittest

from conftest import ROOT, read


class TestLeaveCommandLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/communicator/SKILL.md")

    def test_leave_word_reaches_a_safe_stop(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("leave-word", body, home)
            self.assertIn("shutdown-safe", body, home)

    def test_workers_halted_before_the_machine_sleeps(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("halted or run to their landing", body, home)
        # the base checkpoint rule carries the same duty at the lane level
        base = read("skills/live-spec-base/SKILL.md")
        self.assertIn("leave-word", base)

    def test_closing_line_says_safe_and_what_resumes(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("safe to power off", body, home)
            self.assertIn("what resumes where", body, home)

    def test_never_said_early(self):
        # the never side: the closing line only after every point holds
        for home in self.HOMES:
            body = read(home)
            self.assertIn("only when every point above holds", body, home)

    def test_spec_anchor_and_index(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("[INV-95]", spec)
        self.assertIn("| INV-95 |", spec)


if __name__ == "__main__":
    unittest.main()

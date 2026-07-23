"""Time estimates said, then settled — matrix row M-222 (SPEC INV-93, row 232).

His 2026-07-10 ~11:36 word, raised ~13:20 after a session reported estimates loosely: every ask
gets an honest time range at its echo, long work is explained up front in plain steps, a long
stretch occasionally says how much remains, and the landing report settles estimate against
actual. String rows on the two homes: the spec clause and the communicator skill.
"""

import os
import unittest

from conftest import ROOT, read, read_flat


class TestTimeEstimatesLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/communicator/SKILL.md")

    def test_estimate_at_the_echo(self):
        # PRODUCT_SPEC.md's rewrite dropped the emphatic "never a guess dressed as a
        # promise" line, stating the same property plainly ("stating an unknown as
        # unknown"); the communicator skill keeps the original phrase verbatim.
        unknown_needles = {
            "PRODUCT_SPEC.md": "stating an unknown as unknown",
            "skills/communicator/SKILL.md": "never a guess dressed as a promise",
        }
        for home in self.HOMES:
            body = read(home)
            self.assertIn("honest time range", body, home)
            self.assertIn(unknown_needles[home], body, home)

    def test_long_work_explained_and_tracked(self):
        # PRODUCT_SPEC.md's rewrite states the heartbeat property as "how much time
        # remains" rather than "roughly how much remains"; the skill keeps the original.
        remains_needles = {
            "PRODUCT_SPEC.md": "how much time remains",
            "skills/communicator/SKILL.md": "roughly how much remains",
        }
        for home in self.HOMES:
            body = read(home)
            self.assertIn("explained up front in plain steps", body, home)
            self.assertIn(remains_needles[home], body, home)

    def test_landing_settles_estimate_against_actual(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("estimate beside the actual", body, home)

    def test_spec_anchor_and_index(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("[INV-93]", spec)
        self.assertIn("| INV-93 |", spec)


class TestCriticalPathEstimateDiscipline(unittest.TestCase):
    """Row 311 — the time-estimation discipline (his 2026-07-14 word: improve the estimates).

    Estimates ran far too long because the range was read as the SUM of the work; heavy worker
    fan-out makes the wall-clock the parallel CRITICAL PATH. Three teeth, homed in the communicator
    skill (the named home of INV-93's echo and report rules): the range reads the critical path as
    the wall-clock; the landing retrospective names why estimate and actual matched or missed; and
    that retrospective persists across sessions so the next range is informed by the accumulated
    record of estimate against actual.
    """

    COMM = "skills/communicator/SKILL.md"

    def test_range_reads_the_parallel_critical_path(self):
        body = read_flat(self.COMM)
        self.assertIn("parallel critical path", body)
        self.assertIn("add ~0 wall-clock", body)
        self.assertIn("a sum of every step overstates the finish", body)

    def test_landing_retrospective_names_why(self):
        body = read_flat(self.COMM)
        self.assertIn("names why they matched or missed", body)

    def test_cross_session_calibration(self):
        body = read_flat(self.COMM)
        self.assertIn("persists across sessions in the agent's memory", body)
        self.assertIn("accumulated record of estimate against actual", body)


if __name__ == "__main__":
    unittest.main()

"""The writing register lives in a references/ file loaded on demand — row 266.

communicator's body had nearly tripled (679 lines); the 16-rule writing register plus its 10-point
verification checklist — a self-contained sub-system — moved to references/writing-register.md, loaded
on demand (skill-creator's pattern for heavy material). The body keeps a pointer and the two loudest
rules; the pre-report walk still resolves to the register's new home.
"""

import os
import unittest

from conftest import ROOT, read_flat

SKILL = os.path.join(ROOT, "skills", "communicator", "SKILL.md")
REGISTER = os.path.join(ROOT, "skills", "communicator", "references", "writing-register.md")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


class TestCommunicatorRegisterExtracted(unittest.TestCase):
    def test_reference_file_exists_with_all_sixteen_rules(self):
        body = read(REGISTER)
        for n in range(1, 17):
            self.assertIn(f"(rule {n})", body, f"register reference missing rule {n}")

    def test_reference_file_carries_the_ten_point_checklist(self):
        body = read(REGISTER)
        self.assertIn("First-use check", body)
        self.assertIn("Scissors scan (rule 15)", body)
        self.assertIn("Structure check (rule 16)", body)

    def test_body_points_at_the_reference_and_dropped_the_bulk(self):
        body = read(SKILL)
        self.assertIn("references/writing-register.md", body)
        # the checklist bulk no longer sits in the body
        self.assertNotIn("Cold-reader check", body)
        self.assertNotIn("Read-aloud test", body)

    def test_body_keeps_the_two_loudest_rules(self):
        flat = read_flat("skills/communicator/SKILL.md")
        self.assertIn("Never the contrast frame", flat)
        self.assertIn("State rules positively", flat)

    def test_pre_report_walk_resolves_to_the_register_home(self):
        # step 1 of the pre-report walk names the register's new home
        flat = read_flat("skills/communicator/SKILL.md")
        self.assertIn("open [`references/writing-register.md`](references/writing-register.md)", flat)


if __name__ == "__main__":
    unittest.main()

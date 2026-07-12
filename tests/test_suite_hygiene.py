"""Tests clean up after themselves; test files are born in a temp home — M-236 (SPEC INV-100, row 222).

His 2026-07-10 ~10:46 word (tests must clean up — a matrix-template law) plus the ~14:11 placement
half (the 42-files-in-Downloads incident): every test removes what it creates, a suite run leaves
the machine as it found it, test files are born in a temp home and user-visible folders are never
a test's workspace. String rows on the law's homes plus the leak check's own presence.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestSuiteHygieneLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/test-author/SKILL.md")

    def test_cleanup_half_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("removes what it creates", body, home)
            self.assertIn("leaves the machine as it found it", body, home)
            self.assertIn("a leak is a defect of the test", body, home)

    def test_placement_half_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("never a test's workspace", body, home)
            self.assertIn("download directory is pointed at the temp home", body, home)

    def test_template_carries_the_checklist_item(self):
        tpl = read_flat("templates/TEST_MATRIX.template.md")
        self.assertIn("removes what it creates", tpl)
        self.assertIn("temp home", tpl)

    def test_the_leak_check_stands(self):
        conftest = read_flat("tests/conftest.py")
        self.assertIn("suite_leaves_no_trace", conftest)
        self.assertIn("livespec-test-", conftest)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-100]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-100 |"):
                    self.assertIn("leak", line)
                    return
        self.fail("INV-100 index row missing")


if __name__ == "__main__":
    unittest.main()

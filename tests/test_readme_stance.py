"""The README states the feels boundary as the method's own position — M-250 (rides INV-84/INV-83, row 242).

Born of gate h (SPEC INV-97, this repo attached as its own first host) correctly blocking a
README-only push (2026-07-12): `check_tests_present.py` reds on any user-facing diff (README.md is a
registered `user_facing_globs` entry) that touches nothing under tests/, whether or not the row mints
an invariant or matrix row. Row 242 is prose-only (INV-84 clean-writer authorship, INV-83 the pre-show
register lint) and mints no new spec clause — this string pin exists solely to satisfy that gate, not
because the row needed a new law. It pins the clean writer's paragraph appended to the README's "Why
live-spec, when BMAD…" critique block, before "## Known issues".
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestReadmeStanceParagraph(unittest.TestCase):
    def test_stance_paragraph_present(self):
        body = read_flat("README.md")
        self.assertIn("A spec owns what a project can write down and test.", body)
        self.assertIn("The method answers taste by routing", body)
        self.assertIn(
            "The photo-portfolio project stays cited here as the case that taught the boundary.",
            body,
        )

    def test_stance_paragraph_before_known_issues(self):
        with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
            text = f.read()
        stance_idx = text.find("A spec owns what a project can write down and test.")
        known_issues_idx = text.find("## Known issues")
        self.assertGreater(stance_idx, -1, "stance paragraph not found")
        self.assertGreater(known_issues_idx, -1, "## Known issues heading not found")
        self.assertLess(
            stance_idx, known_issues_idx,
            "stance paragraph must sit before the Known-issues heading",
        )


if __name__ == "__main__":
    unittest.main()

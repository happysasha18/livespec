"""Every skill-kind landing walks skill-creator's review — matrix row M-235 (SPEC INV-99, row 219).

His 2026-07-10 ~10:26 word, raised ~10:29: every skill goes through skill-creator, always — the
work-kind classifier is the trigger. The verify step of a skill-kind wish additionally runs the
installed skill-creator's review of the touched skill; findings fold or get rejected by name in
the landing record. String rows on the two homes: the spec clause and the pipeline's work-kind
table (verify row, skill column).
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestSkillKindReview(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/build-pipeline/SKILL.md")

    def test_walk_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("skill-creator", body, home)
            self.assertIn("does the skill load when it should", body, home)

    def test_findings_fold_by_name(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("folded or rejected by name in the landing record", body, home)

    def test_classifier_is_the_trigger(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("The classifier is the trigger", spec)
        self.assertIn("mood plays no part", spec)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-99]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-99 |"):
                    self.assertIn("skill-creator", line)
                    return
        self.fail("INV-99 index row missing")


if __name__ == "__main__":
    unittest.main()

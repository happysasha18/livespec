"""Every landed queue row carries its delegation accounting, and a suite check reads the queue — M-241 (SPEC INV-103, row 254).

His 2026-07-12 ~00:27 word: a landed row's status cell records its delegation — what went to a worker
with a rough saving, or a stood-down line naming why the senior kept the work; the duty binds the
orchestrator seat whatever model leads. Prose alone did not hold the routing rule until he asked what
stops the glitch. Beyond the string needles on the law's two homes, the ROADMAP scan is the mechanical
check itself: every row landed 2026-07-12 or later must carry the line.
"""

import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANDED = re.compile(r"\*\*landed (20\d\d-\d\d-\d\d)")
BINDS_FROM = "2026-07-12"


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestDelegationLineLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/build-pipeline/SKILL.md")

    def test_law_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("the landed row's status cell", body, home)
            self.assertIn("a suite check reads it", body, home)
            self.assertIn("a landed row without the line goes red", body, home)
            self.assertIn("binds the orchestrator seat regardless of", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-103]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-103 |"):
                    self.assertIn("delegation", line)
                    return
        self.fail("INV-103 index row missing")

    def test_every_forward_landed_row_carries_the_line(self):
        checked = 0
        with open(os.path.join(ROOT, "ROADMAP.md"), encoding="utf-8") as f:
            for line in f:
                m = LANDED.search(line)
                if not m or m.group(1) < BINDS_FROM:
                    continue
                cells = line.split("|")
                status = next((c for c in cells if "**landed" in c), "")
                self.assertIn(
                    "delegation",
                    status.lower(),
                    "landed-forward row missing its delegation line: " + line[:70],
                )
                checked += 1
        self.assertGreater(checked, 0, "no forward-landed rows found to scan")


if __name__ == "__main__":
    unittest.main()

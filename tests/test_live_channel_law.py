"""The live-channel law: a behavioural rule that breaks mid-turn twice earns a live channel — M-246 (SPEC INV-108, row 256).

His 2026-07-12 ~00:39-00:40 word (why a recurring rule lives in a file read once, and that it must be
written into live-spec) plus the worked proof: the routing rule lived in once-read files since June and
broke mid-turn until the every-prompt hook line and the after-the-fact suite check landed (rows 253/254,
2026-07-12), the same cure that killed invented clock stamps. String rows on the law's two homes plus the
spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestLiveChannelLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/live-spec-base/SKILL.md")

    def test_law_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("earns a live channel", body, home)
            self.assertIn("every-prompt hook line", body, home)
            self.assertIn("mechanical after-the-fact check", body, home)
            self.assertIn("once-read", body, home)

    def test_worked_proof_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("the same cure that killed invented clock stamps", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-108]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-108 |"):
                    self.assertIn("live channel", line)
                    return
        self.fail("INV-108 index row missing")


if __name__ == "__main__":
    unittest.main()

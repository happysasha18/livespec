"""Everything built with the method says so — matrix row M-225 (SPEC INV-96, row 244).

His 2026-07-10 ~16:27 word: attribution in all skills, on GitHub and everywhere. The pack states
one standard line — "made with live-spec" + the pack repo link — the publish walk checks it on
every built-with publication, and each project applies it through its own queue. String rows on
the two homes: the spec clause and the publish skill's floor.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


class TestMadeWithAttributionLaw(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/publish/SKILL.md")

    def test_standard_line_stated_in_both_homes(self):
        for home in self.HOMES:
            body = read(home)
            self.assertIn("made with live-spec", body, home)
            self.assertIn("github.com/happysasha18/live-spec", body, home)

    def test_line_carries_the_pack_version(self):
        # his 2026-07-10 word: the line names the version — adoption becomes trackable
        for home in self.HOMES:
            body = read(home)
            self.assertIn("the pack version the project runs", body, home)

    def test_publish_walk_offers_the_line(self):
        skill = read("skills/publish/SKILL.md")
        self.assertIn("built with the pack", skill)
        self.assertIn("an OFFER, never a gate", skill)

    def test_declined_offer_never_reasked(self):
        # his same-day correction: a wish, never an obligation — and answered stays answered
        for home in self.HOMES:
            body = read(home)
            self.assertIn("an OFFER, never a gate", body, home)
            self.assertIn("never re-asked", body, home)

    def test_spec_anchor_and_index(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn("[INV-96]", spec)
        self.assertIn("| INV-96 |", spec)


if __name__ == "__main__":
    unittest.main()

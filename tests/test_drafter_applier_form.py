"""The drafter-applier pipeline is the standard colliding-rows form — M-242 (SPEC INV-49, row 255).

Born live 2026-07-12: the law batch all touched the spec/matrix/version chain, so landings serialized
under the pen, and the queue still moved at two rows an hour once a drafter worker prepared the next
row's edit strings while the applier landed the current one. String needles on the pipeline's text.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = "skills/build-pipeline/SKILL.md"


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestDrafterApplierForm(unittest.TestCase):
    def test_form_named_in_the_pipeline(self):
        body = read_flat(HOME)
        self.assertIn("the penless DRAFT stage overlaps the current landing", body)
        self.assertIn(
            "a drafter worker at the judgment tier prepares the next row's exact edit strings", body
        )

    def test_born_live_and_cited(self):
        body = read_flat(HOME)
        self.assertIn("still moved at two rows an hour", body)
        self.assertIn("[T-18, INV-39, INV-49]", body)


if __name__ == "__main__":
    unittest.main()

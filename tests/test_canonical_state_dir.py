"""One canonical state directory; worktree isolation by default on overlap — M-244 (SPEC INV-105, row 227).

The audit found a ghost `.livespec` dir with a different profile beside the real `.live-spec` (two
competing truths), and overlapping write-sets ran unisolated (2026-07-10). The law: the canonical state
directory is named `.live-spec`, once; a near-miss dir found at attach or resume is a red finding retired
to the attic under a manifest line; and worktree isolation is the default when two lanes' write-sets
overlap. String rows on the law's three homes plus the INV-105 anchor and index.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestCanonicalStateDirLaw(unittest.TestCase):
    def test_canonical_name_in_both_attach_and_spec(self):
        for home in ("PRODUCT_SPEC.md", "adopt/ADOPT.md"):
            body = read_flat(home)
            self.assertIn("the canonical state directory is named", body, home)

    def test_lookalike_retired_to_attic(self):
        for home in ("PRODUCT_SPEC.md", "adopt/ADOPT.md"):
            body = read_flat(home)
            self.assertIn("near-miss directory found at attach or resume is a red finding", body, home)
            self.assertIn("to the attic under a manifest line", body, home)

    def test_worktree_default_in_both_fence_homes(self):
        for home in ("PRODUCT_SPEC.md", "skills/live-spec-base/SKILL.md"):
            body = read_flat(home)
            self.assertIn("worktree isolation is the default when two lanes' write-sets overlap", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-105]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-105 |"):
                    self.assertIn("canonical", line)
                    return
        self.fail("INV-105 index row missing")


if __name__ == "__main__":
    unittest.main()

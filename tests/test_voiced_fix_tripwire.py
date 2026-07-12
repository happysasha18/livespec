"""A fix touching a spec-backed literal owes its docs and test the same session — M-239 (SPEC INV-104, row 225).

Born of the row 220 audit (2026-07-10): one-line fixes touching spec-backed literals kept shipping
without same-session doc sync. The rules already existed (docs travel with the change; the red-first
small-fix path); the gap was a tripwire at build-pipeline's bug and skip doors, so the door step itself
asks whether the edit touches a spec-backed literal or clause, and a yes routes the docs-and-test duty
into the same session mechanically. His 2026-07-10 ~11:00 word queued row 225; landed 2026-07-12. String
rows on the law's two homes plus the spec anchor and its index row.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestVoicedFixTripwire(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/build-pipeline/SKILL.md")

    def test_tripwire_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("does this edit touch a spec-backed literal or clause", body, home)

    def test_binds_docs_and_test_same_session(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("the docs and the test land in the same session", body, home)

    def test_reads_content_not_diff_size(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("tripwire reads the edit's content", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-104]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-104 |"):
                    self.assertIn("literal", line)
                    return
        self.fail("INV-104 index row missing")


if __name__ == "__main__":
    unittest.main()

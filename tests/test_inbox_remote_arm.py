"""The inbox door has a remote arm — M-251 (SPEC INV-112, row 247).

The owner thought the cloud seat through mid-session on 2026-07-10: today's inbox law assumes a shared
filesystem, and a cloud session, a scheduled routine, or another machine reaches a repo only through git.
The remote arm states the deposit — one new file in inbox/, committed touching inbox/ only with the source
named, then pushed — under a per-repo grant recorded in the host profile like the push grant. A seat with no
grant fails honestly: it names the grant it lacks and hands the owner the one action that supplies it. String
rows on the law's three prose homes plus the spec anchor and its index row.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestInboxRemoteArm(unittest.TestCase):
    HOMES = (
        "PRODUCT_SPEC.md",
        "inbox/README.md",
        "adopt/ADOPT.md",
    )

    def test_remote_arm_in_all_prose_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("A remote seat reaches a repo only through git", body, home)
            self.assertIn("under a per-repo grant", body, home)
            self.assertIn("recorded in the host profile like the push grant", body, home)

    def test_honest_failure_in_all_prose_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("fails honestly", body, home)
            self.assertIn("hands the owner the one action", body, home)

    def test_deposit_stays_inbox_only(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("committed touching inbox/ only", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-112]", spec)
        self.assertIn("holds no bar over the deposit", spec)
        self.assertIn("owes the fence and no re-check record", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-112 |"):
                    self.assertIn("remote arm", spec)
                    self.assertIn("grant", spec)
                    return
        self.fail("INV-112 index row missing")


if __name__ == "__main__":
    unittest.main()

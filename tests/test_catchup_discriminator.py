"""The catch-up routing carries its version-delta discriminator — M-248 (SPEC INV-110, row 239).

The track-coach audit (2026-07-10 ~14:19) found the trigger wordings would justify the heavy
catch-up walk where a host queue row is the truth: a pure docs-layout pass with no pack-version
delta fell into the gap. The routing states the discriminator in one sentence — the walk fires
only when the host's recorded package version is behind the current package VERSION — carried in
both homes: the spec's skill-behaviour paragraph and the guide's "When to run this".
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestCatchupDiscriminator(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "MIGRATION.md")

    def test_discriminator_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "fires only when the host's recorded package version is behind the current package VERSION",
                body,
                home,
            )
            self.assertIn(
                "no version delta is the host's own queue row through its pipeline",
                body,
                home,
            )

    def test_trigger_wordings_read_as_examples(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("The trigger wordings are examples under this test", body, home)
            self.assertIn("A wording never decides the routing", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-110]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-110 |"):
                    self.assertIn("version", line)
                    return
        self.fail("INV-110 index row missing")


if __name__ == "__main__":
    unittest.main()

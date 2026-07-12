"""A restructure/migration merge gate judges the delta, in three parts — M-253 (SPEC INV-114, row 258).

The tlvphotos window's word, 2026-07-12 ~01:28 («надо переписать правила … пойми откуда пришло»): the pack
states no law today for what a restructure merge's equivalence proof consists of or how prover findings
route, so each session invents its own bar. Tonight that produced a wrong one — the orchestrator
over-sharpened his spoken «prover finds nothing both sides» into «any finding parks the merge» and parked a
strictly-improving merge on the OLD side's pre-existing clarity debts, which he corrected live: the gate
judges the DELTA. The law in three parts: (1) load-bearing token identity old-versus-new modulo the
per-chunk named deltas plus the punctuation-multiset check (INV-111); (2) the full suite green on the
merged tree (INV-39); (3) a full prover pass on both sides whose blocking set is delta-scoped — an
unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change.
Pre-existing findings equal on both sides route to queue rows in the same landing and never block. And a
session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as
its own interpretation. String rows on the law's three homes plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestRestructureMergeGateLaw(unittest.TestCase):
    HOMES = (
        "PRODUCT_SPEC.md",
        "skills/product-prover/SKILL.md",
        "skills/build-pipeline/SKILL.md",
    )

    def test_merge_gate_judges_the_delta_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("merge gate judges the delta", body, home)
            self.assertIn("blocking set is delta-scoped", body, home)

    def test_preexisting_findings_route_not_block_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "route to queue rows in the same landing and never block", body, home
            )

    def test_say_the_bar_back_duty_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "says the sharpened form back and marks it as its own interpretation",
                body,
                home,
            )

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-114]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-114 |"):
                    self.assertIn("delta", line)
                    return
        self.fail("INV-114 index row missing")


if __name__ == "__main__":
    unittest.main()

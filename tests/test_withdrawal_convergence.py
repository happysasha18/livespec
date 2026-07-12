"""A withdrawn decision converges — after two withdrawals the recommended option is taken as a surfaced
[default]. INV-130 (row 285, prover F6).

An answered question closes forever [INV-59], but a withdrawn decision re-asks "in plainer terms" [INV-9]
with no cap, so a genuine taste call could loop unbounded. The fix bounds it: after the SECOND withdrawal of
the same decision the session takes the recommended option as a `[default]` surfaced in the landing report
(silence stays consent, INV-31), the same convergence an answered question already has. Homes: the
decision-page clause + Formal index, and communicator's rule 10. String level, matrix M-271.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestWithdrawalConvergence(unittest.TestCase):
    def test_spec_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn(
            "A withdrawn decision converges: after two withdrawals the recommended option is taken as a surfaced",
            spec,
        )
        self.assertIn("[INV-130]", spec)

    def test_spec_states_the_bound_and_its_kin(self):
        spec = read_flat("PRODUCT_SPEC.md")
        for needle in (
            "after two withdrawals",
            "taken as a surfaced `[default]`",
            "silence stays consent",
            "the same convergence an answered question already has",
        ):
            self.assertIn(needle, spec, needle)
        # the bound is stated beside both kin invariants
        self.assertIn("[INV-59]", spec)

    def test_formal_index_row(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-130 |"):
                    self.assertIn("withdraw", line.lower())
                    return
        self.fail("INV-130 Formal-index row missing")

    def test_communicator_rule_carries_the_bound(self):
        cm = read_flat("skills/communicator/SKILL.md")
        self.assertIn("after the second withdrawal of the same decision (SPEC INV-130)", cm)


if __name__ == "__main__":
    unittest.main(verbosity=2)

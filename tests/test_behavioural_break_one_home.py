"""One home for behavioural-rule break records — row 264 (SPEC INV-11, INV-23, INV-108).

The once-read-rules sweep (INV-108's first walk) found its own input split: the problem ledger
PROBLEMS.md held most behavioural-rule breaks, but the routing/delegation rule's breaks lived in
ROADMAP rows 253/254/256 and the journal, so a future sweep had to read two sources. This routes a
standing rule's mid-turn break to one home — the ledger — with the live-channel landing pointing
back, so the sweep reads one source.
"""

import os
import unittest

from conftest import ROOT, read_flat

SPEC = "PRODUCT_SPEC.md"
PROBLEMS = os.path.join(ROOT, ".live-spec", "PROBLEMS.md")


class TestBehaviouralBreakOneHome(unittest.TestCase):
    def test_seam_law_names_the_ledger_as_the_one_home(self):
        spec = read_flat(SPEC)
        self.assertIn("the single home the once-read-rules sweep", spec)

    def test_inv108_clause_states_one_home(self):
        spec = read_flat(SPEC)
        self.assertIn("A rule's mid-turn breaks are recorded in one home", spec)

    def test_ledger_carries_the_routing_break(self):
        with open(PROBLEMS, encoding="utf-8") as f:
            body = f.read()
        self.assertIn("routing/delegation rule broke mid-turn despite its once-read home", body)


if __name__ == "__main__":
    unittest.main()

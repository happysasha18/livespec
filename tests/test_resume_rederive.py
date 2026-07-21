"""INV-247 — a deferred item's own state is re-derived from the code before its work resumes (ROADMAP 430).

A method discipline with no mechanical gate: these checks assert the SHIPPED law stands in the spec,
the formal index, and the base rulebook, and that it stays distinct from the queue-take trigger re-scan
(INV-129) rather than folding into it. Zero dependencies; run from the repo root:
    python3 -m pytest -q tests/test_resume_rederive.py
Red proven against HEAD 31a2bb3, where none of these strings exist yet.
"""

import re
import unittest

from conftest import read


class ResumeRederive(unittest.TestCase):
    def test_inv247_spec_clause_stands(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertIn(
            "A deferred item's own state is re-derived from the code before its work resumes.",
            spec,
            "the INV-247 clause title is missing from the product spec",
        )
        # the clause carries its trailing anchor and names the act it owes
        clause = spec.split(
            "A deferred item's own state is re-derived from the code before its work resumes.", 1
        )[1][:2600]
        self.assertIn("[INV-247]", clause, "the INV-247 clause carries no trailing anchor")
        self.assertIn("reads the code the item touches", clause)
        self.assertIn("re-derives the item's real current state", clause)

    def test_inv247_formal_index_row(self):
        spec = read("PRODUCT_SPEC.md")
        self.assertTrue(
            re.search(r"^\| INV-247 \|.*Throwing a wish \|$", spec, re.M),
            "no INV-247 row under 'Throwing a wish' in the Formal index",
        )

    def test_inv247_base_rule_states_the_reread(self):
        skill = read("skills/live-spec-base/SKILL.md")
        self.assertRegex(
            skill,
            r"34\. \*\*A deferred item's own state is re-derived from the code before its work resumes \(SPEC INV-247\)\.\*\*",
            "base rule 34 does not state the resume re-derivation law",
        )
        # the description's rule count moved with the added rule
        self.assertIn("thirty-four rules in the body", skill)
        self.assertNotIn("thirty-three rules in the body", skill)

    def test_inv247_distinct_from_queue_take_rescan(self):
        """The law must stand beside INV-129, not collapse into it: one reads the returning
        trigger, the other the item's own internals."""
        spec = read("PRODUCT_SPEC.md")
        clause = spec.split(
            "A deferred item's own state is re-derived from the code before its work resumes.", 1
        )[1][:2600]
        # it cites INV-129 as the sibling and draws the read-the-trigger / read-the-internals line
        self.assertIn("[INV-129]", clause, "the clause does not situate itself beside the trigger re-scan")
        self.assertIn("re-reads the taken item's own internals", clause)
        # and it answers the mechanical-net question rather than leaving it silent
        self.assertIn("No sound push gate holds it", clause)


if __name__ == "__main__":
    unittest.main()

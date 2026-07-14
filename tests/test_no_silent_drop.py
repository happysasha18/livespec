"""A rewrite that removes substance names every removal in its landing report — M-247 (SPEC INV-109, row 233).

His 2026-07-10 ~12:10 word, after a night docs pass compressed the README's account of why live-spec
stands beside BMAD, Kiro, and spec-kit to one pointer line: a sound thought is never silently dropped —
a removal of substance is at least questioned, of himself or of the owner, in case it is needed later,
with no per-line paralysis. A restyle that removes a section, an argument, a rationale, or a worked
example lists every removal in its landing report with one line of judgment each; a removal the rewriter
cannot justify becomes a question. The rule scopes to substance and leaves line-level wording free.
String rows on the law's three homes plus the spec anchor and its index row.
"""

import os
import unittest

from conftest import ROOT, read_flat


class TestNoSilentDropLaw(unittest.TestCase):
    # build-pipeline reduced to a pointer at the one home (R6 compaction, 2026-07-14);
    # the full rule text lives in the spec and its owning skill, communicator.
    HOMES = (
        "PRODUCT_SPEC.md",
        "skills/communicator/SKILL.md",
    )

    def test_removal_rule_in_both_full_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("lists every removal in its landing report", body, home)
            self.assertIn("one line of judgment each", body, home)
            self.assertIn(
                "A removal the rewriter cannot justify becomes a question", body, home
            )
            self.assertIn("Never a silent cut of substance", body, home)

    def test_build_pipeline_points_at_the_one_home(self):
        bp = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("(SPEC INV-109)", bp, "build-pipeline lost the INV-109 anchor")
        self.assertIn("communicator rule 6", bp,
                      "build-pipeline no longer points at the removal-accounting's one home")

    def test_scope_carveout_in_both_full_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("line-level wording", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-109]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-109 |"):
                    self.assertIn("removal", line)
                    return
        self.fail("INV-109 index row missing")


if __name__ == "__main__":
    unittest.main()

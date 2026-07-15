"""Request-layer classifier at the pipeline's door — the closed door set + entry-layer criterion
+ the one-plain-question fallback (INV-151), the deferral-must-justify-itself clause (INV-152), and
the unification stated once (INV-153).

Design settled by the Fable audit (scratchpad fable-prover-vs-designreview-audit.md, sections 6-10),
the companion of the property->review routing that landed the same session (INV-150). String rows on
the shipped homes: the spec clauses, the build-pipeline door step, and the base rulebook.
"""

import unittest

from conftest import read, read_flat, read_all, read_all_flat


class TestRequestClassifierEntryLayer(unittest.TestCase):
    """INV-151 — a request enters at the highest document its change reaches; the door set is
    closed; a request matching no kind is one plain question."""

    def test_entry_layer_criterion_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("highest document in the derivation chain", spec)
        self.assertIn("the set is closed", spec)
        self.assertIn("[INV-151]", spec)

    def test_one_plain_question_fallback(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("matches no kind", spec)
        self.assertIn("one plain question", spec)

    def test_closed_set_at_the_build_pipeline_door(self):
        bp = read_all_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("The door set is CLOSED", bp)
        self.assertIn("highest document in the derivation chain", bp)
        self.assertIn("one plain question", bp)
        for kind in ("product behaviour", "docs-only", "settings ladder",
                     "inbox wish", "method", "sketch", "research", "feedback"):
            self.assertIn(kind, bp, "closed-set entry missing at the door: %r" % kind)

    def test_intake_moment_back_check(self):
        bp = read_all_flat("skills/build-pipeline/SKILL.md")
        # A phrase unique to the new door-step wiring, so this test is genuinely red
        # before the classifier lands (the bare "at intake" already existed elsewhere).
        self.assertIn("spec-motion tripwire fires", bp)
        self.assertIn("lifts it to the spec at the door", bp)

    def test_inv151_index_and_ownership(self):
        rows = read("PRODUCT_SPEC.md").splitlines()
        self.assertTrue(any(l.startswith("| INV-151 |") for l in rows),
                        "INV-151 index row missing")
        self.assertIn("INV-151", read_flat("ARCHITECTURE.md"))


class TestDeferralJustifiesItself(unittest.TestCase):
    """INV-152 — a held work item is re-tested by derivability; a marker that cannot name its
    human-only fact defaults to the seat. Base rulebook home + spec clause."""

    def test_deferral_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("A deferral must justify itself", spec)
        self.assertIn("re-tested by derivability every time it is touched", spec)
        self.assertIn("defaults to the seat", spec)
        self.assertIn("[INV-152]", spec)

    def test_lives_in_the_base_rulebook(self):
        base = read_flat("skills/live-spec-base/SKILL.md")
        self.assertIn("A deferral must justify itself", base)
        self.assertIn("SPEC INV-152", base)
        self.assertIn("needs-the-human's-word marker", base)

    def test_base_description_counts_the_rule(self):
        base = read_flat("skills/live-spec-base/SKILL.md")
        self.assertIn("twenty-nine rules", base)

    def test_inv152_index_and_ownership(self):
        rows = read("PRODUCT_SPEC.md").splitlines()
        self.assertTrue(any(l.startswith("| INV-152 |") for l in rows),
                        "INV-152 index row missing")
        self.assertIn("INV-152", read_flat("ARCHITECTURE.md"))


class TestUnificationStatedOnce(unittest.TestCase):
    """INV-153 — request, property, and work item are one routing principle: every incoming thing
    routes to the home whose declared sentence governs it, and a thing that pins to no home is
    itself the finding."""

    def test_unification_clause_stands(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("routes to the home whose declared sentence governs it", spec)
        self.assertIn("pins to no home is itself the finding", spec)
        self.assertIn("[INV-153]", spec)

    def test_names_all_three_controls(self):
        flat = read_flat("PRODUCT_SPEC.md")
        idx = flat.find("routes to the home whose declared sentence governs it")
        self.assertGreater(idx, -1, "unification clause absent")
        region = flat[idx:idx + 1400]
        for anchor in ("INV-150", "INV-151", "INV-152"):
            self.assertIn(anchor, region,
                          "the unification clause does not cite %s" % anchor)

    def test_inv153_index_and_ownership(self):
        rows = read("PRODUCT_SPEC.md").splitlines()
        self.assertTrue(any(l.startswith("| INV-153 |") for l in rows),
                        "INV-153 index row missing")
        self.assertIn("INV-153", read_flat("ARCHITECTURE.md"))


if __name__ == "__main__":
    unittest.main()

"""Every person-facing scenario heading carries its tag — an untagged H3 is mechanically red. INV-132
(row 283, prover F4).

INV-73's reverse direction ("every scenario carries its tag") was not mechanically enforceable as written:
the checker could not tell an untagged NEW scenario from a legitimately-untagged machinery, rules, or
reference section, so an untagged scenario could ship green and uncovered. The fix is a heading convention:
every H3 heading in PRODUCT_SPEC.md carries EITHER a `[feature: F-x]` tag (it is a person-facing scenario,
mapped by the feature-coverage trace) OR the explicit `[not a scenario]` marker (it states machinery, a
rule, or reference — legitimately untagged). An H3 that carries neither is unambiguously red, so a new
scenario whose tag was forgotten cannot ship uncovered. Homes: the heading-convention clause + Formal
index, and spec-author. This is the traceability guardrail's teeth for the reverse direction; matrix M-273.
"""

import os
import re
import unittest

from conftest import ROOT, read, read_flat

SCENARIO_MARKER = "[not a scenario]"


def h3_tag_gaps(spec_text):
    """H3 headings that are neither `[feature: F-x]`-tagged nor `[not a scenario]`-marked. An ambiguous
    (untagged, unmarked) H3 is a scenario whose tag may have been forgotten (SPEC INV-132)."""
    gaps = []
    for m in re.finditer(r"^### (.*)$", spec_text, re.M):
        heading = m.group(1).strip()
        # A valid tag ends the heading with `[feature: F-x]`: a feature id is `F-` plus
        # alphanumerics/hyphens (so a numeric id like `F-12` counts), and a heading may
        # carry several comma-separated ids (`[feature: F-a, F-b]`) — all validly tagged.
        if re.search(r"\[feature:\s*F-[a-z0-9-]+(?:\s*,\s*F-[a-z0-9-]+)*\s*\]\s*$", heading):
            continue
        if heading.endswith(SCENARIO_MARKER):
            continue
        gaps.append(heading)
    return gaps


class TestScenarioHeadingTag(unittest.TestCase):
    def test_every_h3_is_tagged_or_marked(self):
        gaps = h3_tag_gaps(read("PRODUCT_SPEC.md"))
        self.assertEqual(
            gaps, [],
            "H3 headings neither `[feature: F-x]`-tagged nor `[not a scenario]`-marked "
            "(an untagged scenario, or a machinery section missing its marker): %s" % gaps,
        )

    def test_untagged_h3_goes_red(self):
        """The never side, permanent: an untagged, unmarked H3 (a forgotten scenario tag) is caught, and a
        properly marked or tagged one is spared."""
        spec = read("PRODUCT_SPEC.md")
        seeded = spec + "\n### A brand new scenario nobody tagged\n\nBody.\n"
        self.assertIn("A brand new scenario nobody tagged", h3_tag_gaps(seeded),
                      "the checker missed an untagged, unmarked H3 — no teeth")
        marked = spec + "\n### Some machinery section  %s\n\nBody.\n" % SCENARIO_MARKER
        self.assertNotIn("Some machinery section", " ".join(h3_tag_gaps(marked)),
                         "the checker flagged a legitimately marked machinery section")
        tagged = spec + "\n### A real scenario  [feature: F-demo]\n\nBody.\n"
        self.assertNotIn("A real scenario", " ".join(h3_tag_gaps(tagged)),
                         "the checker flagged a properly feature-tagged scenario")

    def test_numeric_and_multi_feature_headings_are_accepted(self):
        """A feature id may be numeric (`F-12`) and a heading may carry several features
        (`[feature: F-a, F-b]`) — both are validly tagged, never reddened, while a truly
        untagged/unmarked heading stays red (SPEC INV-132's mechanism, hardened)."""
        spec = read("PRODUCT_SPEC.md")
        numeric = spec + "\n### A numeric-id scenario  [feature: F-12]\n\nBody.\n"
        self.assertNotIn("A numeric-id scenario", " ".join(h3_tag_gaps(numeric)),
                         "the checker flagged a validly numeric-id-tagged scenario (F-12)")
        multi = spec + "\n### A multi-feature scenario  [feature: F-a, F-b]\n\nBody.\n"
        self.assertNotIn("A multi-feature scenario", " ".join(h3_tag_gaps(multi)),
                         "the checker flagged a validly multi-feature-tagged scenario (F-a, F-b)")
        # the never side holds: an untagged, unmarked heading is still red
        untagged = spec + "\n### Still nobody tagged this one\n\nBody.\n"
        self.assertIn("Still nobody tagged this one", h3_tag_gaps(untagged),
                      "widening the recognizer must not swallow a genuinely untagged heading")

    def test_spec_states_heading_convention(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("every H3 heading in this spec carries either its `[feature: F-x]` tag", spec)
        self.assertIn("the explicit `[not a scenario]` marker", spec)
        self.assertIn("An H3 that carries neither is unambiguously red", spec)
        self.assertIn("[INV-132]", spec)

    def test_formal_index_row(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-132 |"):
                    self.assertIn("not a scenario", line.lower())
                    return
        self.fail("INV-132 Formal-index row missing")

    def test_spec_author_carries_heading_convention(self):
        sa = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("[not a scenario]", sa)
        self.assertIn("untagged, unmarked H3 is unambiguously red", sa)


if __name__ == "__main__":
    unittest.main(verbosity=2)

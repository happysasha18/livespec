"""A project kind carries its own DESIGN PRINCIPLES, and the verify pass runs them — M-278
(SPEC INV-136, row 298).

Beside its concrete layers and proof kinds (SPEC INV-135), a project kind names a set of design
principles — checkable design rules the kind's products must hold, of the family of cross-surface
policy uniformity (INV-125) and paired-transition symmetry (INV-126). The pack ships a per-kind
starter set (the ARCHITECTURE per-kind design-principles table); a founding that records a VISUAL
kind declares its design principles in the host profile on a `project.design-principles` line, and a
founding check reds a visual kind recorded with none. The frontend starter set gathers the visitor
walk, the feel pass scaled to a whole site, and motion/scroll feel plus its founding design
principle — the interactive-overlap rule. The verify feel pass reads the declared design principles;
the interactive-overlap rule's pixel/DOM projection runs in the ADOPTING project's own suite.

The founding check is red-proven against a visual kind-only fixture (a kind with layers and proofs but
no declared design principles goes red), while a non-visual kind with none passes.
"""

import os
import re
import unittest

from conftest import ROOT, read, read_flat

KIND = re.compile(r"(?m)^\s*[-*]?\s*`?project\.kind:\s*(.+)$")
PRINCIPLES = re.compile(r"(?m)^\s*[-*]?\s*`?project\.design-principles:")

# A kind whose products have a screen a hand touches — the design-principles law binds these.
# Matched at WORD boundaries, never as bare substrings: a bare "ui" substring would misclassify
# "build tool", "test suite", "guide", "requirements" (each contains the letters u-i mid-word);
# the boundary keeps the standalone kind token "ui" while leaving those alone.
VISUAL_TOKENS = (
    "frontend", "front-end", "fullstack", "full-stack", "static site", "static-site",
    "photo", "gallery", "visual", "website", "web app", "web-app", "web page", "web ui",
    "ui", "gui", "mobile app", "mobile", "desktop app", "dashboard", "ios", "android",
    "site", "landing page", "portfolio", "spa",
)
_VISUAL_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(t) for t in VISUAL_TOKENS) + r")\b", re.IGNORECASE)


def kind_is_visual(kind_value):
    return _VISUAL_RE.search(kind_value) is not None


def design_principles_complete(profile_text):
    """The founding check: a profile that records a VISUAL project.kind must also declare its
    design principles on a `project.design-principles` line. A non-visual kind (or no kind at all)
    carries no such requirement. Returns (ok, reason)."""
    m = KIND.search(profile_text)
    if not m:
        return True, "no project.kind recorded — nothing to complete"
    if not kind_is_visual(m.group(1)):
        return True, "non-visual kind — design principles not required by this law"
    if not PRINCIPLES.search(profile_text):
        return False, "visual project.kind recorded with no declared project.design-principles"
    return True, "visual kind declares its design principles"


# --- fixtures: a visual kind with and without principles, and a non-visual kind ---
FIXTURE_VISUAL_WITH = """# Host profile — tlvphotos
- `project.kind: photo portfolio (fullstack, static-first)`
- `project.layers: content · rendering engine · deployment`
- `project.proofs: a byte-diff of the baked output · the owner's eye-walk`
- `project.design-principles: the visitor walk · the feel pass · motion feel · the interactive-overlap rule`
"""

FIXTURE_VISUAL_WITHOUT = """# Host profile — a half-founded visual project
- `project.kind: fullstack app`
- `project.layers: frontend · backend · store`
- `project.proofs: unit tests · browser renders · the owner's walk`
"""

FIXTURE_NONVISUAL_WITHOUT = """# Host profile — the promotion campaign
- `project.kind: prose / promotion campaign`
- `project.layers: message · channels · assets`
- `project.proofs: the register lint · the owner's review`
"""


class TestFoundingDesignPrinciples(unittest.TestCase):
    def test_visual_kind_with_design_principles_passes(self):
        ok, reason = design_principles_complete(FIXTURE_VISUAL_WITH)
        self.assertTrue(ok, "a visual kind that declares its design principles should pass: " + reason)

    def test_visual_kind_without_design_principles_goes_red(self):
        ok, reason = design_principles_complete(FIXTURE_VISUAL_WITHOUT)
        self.assertFalse(ok, "a visual kind with no declared design principles must be flagged")
        self.assertIn("project.design-principles", reason)

    def test_nonvisual_kind_without_design_principles_passes(self):
        ok, reason = design_principles_complete(FIXTURE_NONVISUAL_WITHOUT)
        self.assertTrue(ok, "a non-visual kind is not required to declare design principles: " + reason)

    def test_founding_check_has_teeth(self):
        """Red-first proof: the check catches the missing declaration. A naive check that only
        looked at project.kind (never at design-principles) would let the visual-without fixture
        escape — this asserts our check does not."""
        naive_escapes = KIND.search(FIXTURE_VISUAL_WITHOUT) is not None  # a kind IS recorded
        self.assertTrue(naive_escapes, "fixture must record a kind for the teeth proof to be meaningful")
        ok, _ = design_principles_complete(FIXTURE_VISUAL_WITHOUT)
        self.assertFalse(ok, "the check must red where a naive kind-only check would pass")

    def test_ui_lookalike_kinds_are_not_misclassified_visual(self):
        """A bare-substring detector would read the letters 'ui' inside build/suite/guide/requirements
        and falsely redden these non-visual kinds. The word-boundary detector must leave them alone."""
        for kind in ("code / build tool", "CLI · a test suite runner", "a style guide generator",
                     "requirements engine", "a fluid dynamics library"):
            profile = "- `project.kind: %s`\n- `project.layers: a · b · c`\n" % kind
            ok, reason = design_principles_complete(profile)
            self.assertTrue(ok, "'%s' must not be classified visual (no design-principles required): %s"
                            % (kind, reason))

    def test_real_visual_kinds_are_caught(self):
        """Visual kinds named without the fullstack/static-site words must still be required to
        declare design principles — a mobile app, a desktop dashboard, an iOS client all have a
        screen a hand touches."""
        for kind in ("a mobile app", "desktop dashboard", "iOS client", "a photo gallery",
                     "marketing landing page"):
            profile = "- `project.kind: %s`\n- `project.layers: a · b · c`\n" % kind
            ok, reason = design_principles_complete(profile)
            self.assertFalse(ok, "'%s' is visual and declares no design principles — must be flagged" % kind)

    def test_live_host_profile_is_not_falsely_reddened(self):
        """live-spec's own host is a skill pack (non-visual) — the law does not require it to declare
        design principles, and the check must not falsely redden it."""
        ok, reason = design_principles_complete(read(".live-spec/profile.md"))
        self.assertTrue(ok, "live-spec's non-visual host must not be reddened: " + reason)


class TestDesignPrinciplesLaw(unittest.TestCase):
    def test_spec_clause_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("A project kind also carries its own design principles", spec)
        self.assertIn("interactive controls that belong to different layers occupy separate screen space", spec.lower())
        self.assertIn("[INV-136]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-136 |"):
                    self.assertIn("design principle", line.lower())
                    self.assertIn("project.design-principles", line)
                    return
        self.fail("INV-136 Formal-index row missing")

    def test_architecture_has_per_kind_design_principles_table(self):
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn("Design principles by project.kind", arch)
        for needle in ("the visitor walk", "the feel pass", "project.design-principles"):
            self.assertIn(needle, arch, "ARCHITECTURE per-kind design-principles table lost: %s" % needle)

    def test_frontend_starter_set_names_interactive_overlap(self):
        """The shipped frontend starter set names the interactive-overlap principle in full."""
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn(
            "Interactive controls that belong to different layers occupy separate screen space",
            arch, "the frontend starter set does not name the interactive-overlap rule")
        # the non-interactive allowance is stated as its own sentence
        self.assertIn("may overlap anything freely", arch)

    def test_adopting_project_pixel_projection_specified(self):
        """The overlap check's testable projection is specified for the ADOPTING project, not faked
        in live-spec's own suite."""
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn("pointer-events:none", arch)
        self.assertIn("adopting project", arch.lower())

    def test_verify_feel_pass_reads_design_principles(self):
        bp = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("declared design principle", bp,
                      "build-pipeline's verify feel pass does not read the declared design principles")
        self.assertIn("INV-136", bp)

    def test_spec_author_reads_declared_design_principles(self):
        sa = read_flat("skills/spec-author/SKILL.md")
        self.assertIn("declared design principle", sa,
                      "spec-author does not read the declared design principles")
        self.assertIn("INV-136", sa)

    def test_adopt_founding_prompts_design_principles(self):
        adopt = read_flat("adopt/ADOPT.md")
        self.assertIn("project.design-principles", adopt)
        self.assertIn("INV-136", adopt)

    def test_prover_carries_the_interactive_overlap_lens(self):
        # the deposit asked for the overlap rule as a spec-time prover lens, sibling to the
        # cross-surface and paired-transition lenses; the verify-time design principle is its
        # floor, this lens catches it earlier on the spec (SPEC INV-136)
        pv = read_flat("skills/product-prover/SKILL.md")
        self.assertIn("Interactive-overlap across layers", pv)
        self.assertIn("retract the lower layer's chrome", pv)
        self.assertIn("[INV-136]", pv)

    def test_spec_and_index_home_the_prover_lens(self):
        spec = read_flat("PRODUCT_SPEC.md")
        # the clause states the prover carries the spec-time lens for the overlap blind spot
        self.assertIn("The prover carries the spec-time lens for this blind spot", spec)
        # the Formal-index row's homes list names the prover lens as a home
        self.assertIn("product-prover's interactive-overlap lens", spec)


if __name__ == "__main__":
    unittest.main()

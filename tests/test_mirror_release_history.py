"""The release-history stamp: every mirror's README carries the pack's own version story.

scripts/sync-mirrors.sh rebuilds standalone mirror repos from skills/<name>/ and already stamps
an attribution line (SPEC INV-96) on each mirror's README.md and SKILL.md. This adds a second,
richer stamp: a generated "## Release history" section, computed once from the PACK's own git
log (never hand-written, never stale) and appended to the mirror's README.md only — right before
the attribution line, which stays the last thing in the file. A --print-release-history mode
prints just that section and exits without touching any repo, so the generation logic is testable
without cloning a mirror or reaching GitHub.
"""
import os
import subprocess
import unittest

from conftest import ROOT


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class TestMirrorReleaseHistory(unittest.TestCase):
    # The generator reads the PACK's own git log, so the by-deed test needs the real clone;
    # a scratch copy of the tree (gate b's meta-run) has no .git and skips this one by its
    # declared precondition — the string tests below still run there.
    @unittest.skipUnless(
        os.path.isdir(os.path.join(ROOT, ".git")),
        "release-history generation reads git history; scratch copies carry none",
    )
    def test_print_mode_emits_real_history(self):
        result = subprocess.run(
            ["bash", "scripts/sync-mirrors.sh", "--print-release-history"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        output = result.stdout

        self.assertIn("## Release history", output)

        lines = output.splitlines()
        self.assertTrue(
            any(line.startswith("- 2.1.1 · 2026-07-16 — the day-after sweep") for line in lines),
            "expected the newest release's line, generated from its own bump commit",
        )
        self.assertIn(
            "- 2.0.0 · 2026-07-16 — the readability + compaction release",
            output,
        )
        # the dedupe keeps the OLDEST commit per version (the bump commit itself) — a newer
        # follow-up commit for the same 2.0.0 ("2.0.0: prover record covers the pushed state")
        # must lose and never surface in the generated section
        self.assertNotIn("prover record", output)
        # a trailing parenthetical group on the subject line is stripped from the story text
        self.assertNotIn("(rows 354/356/357/358)", output)
        # exactly one line for 2.0.0 — the dedupe collapsed the two matching commits to one
        self.assertEqual(output.count("- 2.0.0 "), 1)

        # the cut point is paren-aware: 1.0.9's subject has its first ": " INSIDE
        # "(his word: the line doubles as the adoption tracker)" — a plain string cut would
        # stop mid-parenthetical and leave a dangling, unclosed "(his word" fragment
        self.assertNotIn("(his word", output)
        self.assertIn(
            "- 1.0.9 · 2026-07-10 — the attribution line carries the pack version",
            lines,
        )
        # 0.5.0's remaining story after the (paren-aware) cut ends with a trailing
        # parenthetical group of its own, which must also be stripped
        self.assertIn(
            "- 0.5.0 · 2026-07-05 — preventive audit run + folded",
            lines,
        )

    def test_banner_is_the_kinds_third_declared_member(self):
        # The design review's 2.2.0 finding: the sync writes THREE generated blocks onto a
        # mirror (banner · release history · attribution); all three are declared members of
        # one kind, each pinned by a test. This pins the banner — the spec arm was red before
        # the INV-181 clause named the kind.
        script = read("scripts/sync-mirrors.sh")
        self.assertIn("banner_for", script)
        self.assertIn("Read-only mirror", script)

        spec = read("PRODUCT_SPEC.md")
        self.assertIn("read-only banner", spec)
        self.assertIn("three members", spec)

    def test_loop_stamps_before_attribution(self):
        script = read("scripts/sync-mirrors.sh")

        self.assertIn("stamp_release_history", script)
        self.assertIn("## Release history", script)

        release_call = script.index('stamp_release_history "$mirror_dir/README.md"')
        attribution_call = script.index('stamp_attribution "$mirror_dir/README.md"')
        self.assertLess(
            release_call,
            attribution_call,
            "release history must be stamped before attribution, which stays last",
        )

        # SKILL.md gets no release history: the only stamp_release_history call in the loop
        # body targets README.md, never SKILL.md
        self.assertNotIn('stamp_release_history "$mirror_dir/SKILL.md"', script)


if __name__ == "__main__":
    unittest.main()

"""Guardrails suite — the pack's own git-hook gates, mechanized (ROADMAP row 3).

Zero dependencies beyond the stdlib; run from the repo root:
  python3 -m unittest discover tests -v

Asserts the SHIPPED guardrails/ scripts on disk, and exercises each gate's check
logic both against the real repo state (must be green today) and against scratch
fixtures (must fail the way the gate promises to fail).
"""

import json
import os
import shutil
import stat
import subprocess
import tempfile
import unittest

from conftest import ROOT
GUARDRAILS = os.path.join(ROOT, "guardrails")


def run(args, cwd=None, extra_env=None):
    env = dict(os.environ)
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        args, cwd=cwd or ROOT, capture_output=True, text=True, env=env
    )


class TestGuardrailFilesShip(unittest.TestCase):
    HOOKS = ("pre-commit", "pre-push")
    SCRIPTS = (
        "check-prover-record.sh",
        "check-tests.sh",
        "check-matrix-coverage.sh",
        "fence-refresh.sh",
        "install.sh",
    )

    def test_hooks_and_scripts_exist_and_executable(self):
        for name in self.HOOKS + self.SCRIPTS:
            path = os.path.join(GUARDRAILS, name)
            self.assertTrue(os.path.isfile(path), "missing guardrails file: %s" % name)
            mode = os.stat(path).st_mode
            self.assertTrue(mode & stat.S_IXUSR, "%s is not executable" % name)

    def test_readme_ships(self):
        path = os.path.join(GUARDRAILS, "README.md")
        self.assertTrue(os.path.isfile(path))
        self.assertGreater(os.path.getsize(path), 200, "README suspiciously small")

    def test_fence_ignored_by_git(self):
        gitignore = os.path.join(ROOT, ".gitignore")
        with open(gitignore, encoding="utf-8") as f:
            body = f.read()
        self.assertIn(".live-spec-fence", body)


class TestGateA_ProverRecord(unittest.TestCase):
    """Gate (a): a committed prover record dated today must exist."""

    def test_real_repo_passes(self):
        if os.environ.get("LIVE_SPEC_SCRATCH"):
            self.skipTest("real-repo state check — meaningless in a git-less scratch copy")
        result = run([os.path.join(GUARDRAILS, "check-prover-record.sh")])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK (prover record)", result.stdout)

    def test_missing_record_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            empty_prover_dir = os.path.join(tmp, "docs", "prover")
            os.makedirs(empty_prover_dir)
            result = run([
                os.path.join(GUARDRAILS, "check-prover-record.sh"),
                empty_prover_dir,
                "2026-07-05",
            ])
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("FAIL (prover record)", result.stdout)

    def _init_repo(self, tmp):
        run(["git", "init", "-q"], cwd=tmp)
        run(["git", "config", "user.email", "a@example.com"], cwd=tmp)
        run(["git", "config", "user.name", "a"], cwd=tmp)

    def _write(self, tmp, relpath, content):
        path = os.path.join(tmp, relpath)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def _commit_all(self, tmp, msg):
        run(["git", "add", "-A"], cwd=tmp)
        run(["git", "commit", "-q", "-m", msg], cwd=tmp)

    def test_stale_record_fails(self):
        """A record committed BEFORE the last PRODUCT_SPEC.md change is stale (row 61,
        SPEC M-6): the gate must refuse it even though it is dated today and
        committed — gate (a)'s original checks alone would wrongly pass this."""
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            self._write(tmp, "PRODUCT_SPEC.md", "spec v1\n")
            self._commit_all(tmp, "spec v1")
            self._write(tmp, "docs/prover/2026-07-05-x.md", "prover record for v1\n")
            self._commit_all(tmp, "record for v1")
            self._write(tmp, "PRODUCT_SPEC.md", "spec v2 — changed after the record\n")
            self._commit_all(tmp, "spec v2, no new record")
            result = run(
                [os.path.join(GUARDRAILS, "check-prover-record.sh"), "docs/prover", "2026-07-05"],
                cwd=tmp,
            )
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("predates the last PRODUCT_SPEC.md change", result.stdout)

    def test_record_with_spec_same_commit_passes(self):
        """A record committed in the SAME commit as the PRODUCT_SPEC.md change it
        covers is fresh, not stale — this is the normal push shape."""
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            self._write(tmp, "PRODUCT_SPEC.md", "spec v1\n")
            self._commit_all(tmp, "spec v1")
            self._write(tmp, "PRODUCT_SPEC.md", "spec v2\n")
            self._write(tmp, "docs/prover/2026-07-05-x.md", "prover record for v2\n")
            self._commit_all(tmp, "spec v2 + its record, same commit")
            result = run(
                [os.path.join(GUARDRAILS, "check-prover-record.sh"), "docs/prover", "2026-07-05"],
                cwd=tmp,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class TestGateB_Tests(unittest.TestCase):
    """Gate (b): the test suite must be green (also covers gate c, anchor ownership).

    Both checks here run against a SCRATCH COPY of the whole repo (test_traceability.py
    resolves its fixture paths — PRODUCT_SPEC.md, ARCHITECTURE.md, etc. — relative to the repo
    root, so a bare copy of tests/ alone would 404 on every one of them). The copy
    keeps test_guardrails.py — architecture pins and BUILT matrix rows now reference
    it, so a copy without it is not a green repo — and recursion is cut by an env
    guard instead: the inner run gets LIVE_SPEC_SCRATCH=1, under which these two
    scratch-suite tests skip themselves (one level of nesting, never a fork bomb).
    """

    def _scratch_tests_dir(self, tmp):
        dest = os.path.join(tmp, "repo")
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        return os.path.join(dest, "tests")

    def _skip_if_inner(self):
        if os.environ.get("LIVE_SPEC_SCRATCH"):
            self.skipTest("inner scratch run — recursion guard")

    def test_real_content_passes(self):
        self._skip_if_inner()
        with tempfile.TemporaryDirectory() as tmp:
            scratch_tests = self._scratch_tests_dir(tmp)
            result = run([os.path.join(GUARDRAILS, "check-tests.sh"), scratch_tests],
                         extra_env={"LIVE_SPEC_SCRATCH": "1"})
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("OK (tests)", result.stdout)

    def test_broken_suite_fails(self):
        self._skip_if_inner()
        with tempfile.TemporaryDirectory() as tmp:
            scratch_tests = self._scratch_tests_dir(tmp)
            target = os.path.join(scratch_tests, "test_traceability.py")
            with open(target, encoding="utf-8") as f:
                content = f.read()
            broken = content.replace(
                "self.assertGreater(len(raw), 40",
                "self.assertGreater(len(raw), 999999",
            )
            self.assertNotEqual(content, broken, "fixture edit did not match — test is stale")
            with open(target, "w", encoding="utf-8") as f:
                f.write(broken)
            result = run([os.path.join(GUARDRAILS, "check-tests.sh"), scratch_tests],
                         extra_env={"LIVE_SPEC_SCRATCH": "1"})
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("FAIL (tests)", result.stdout)


class TestGateD_MatrixCoverage(unittest.TestCase):
    """Gate (d): TEST_MATRIX.md's coverage-validation checklist must be fully checked."""

    def test_real_matrix_passes(self):
        result = run([os.path.join(GUARDRAILS, "check-matrix-coverage.sh")])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK (matrix)", result.stdout)

    def test_unchecked_box_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            scratch_matrix = os.path.join(tmp, "TEST_MATRIX.md")
            with open(os.path.join(ROOT, "TEST_MATRIX.md"), encoding="utf-8") as f:
                content = f.read()
            broken = content.replace(
                "- [x] No row cites a spec anchor or node that no longer exists",
                "- [ ] No row cites a spec anchor or node that no longer exists",
                1,
            )
            self.assertNotEqual(content, broken, "fixture edit did not match — matrix text changed")
            with open(scratch_matrix, "w", encoding="utf-8") as f:
                f.write(broken)
            result = run([os.path.join(GUARDRAILS, "check-matrix-coverage.sh"), scratch_matrix])
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("FAIL (matrix)", result.stdout)
            self.assertIn("- [ ]", result.stdout)

    def test_missing_file_fails(self):
        result = run([
            os.path.join(GUARDRAILS, "check-matrix-coverage.sh"),
            "/nonexistent/TEST_MATRIX.md",
        ])
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL (matrix)", result.stdout)


class TestGateE_PrototypeFence(unittest.TestCase):
    """Gate (e): a PROD file must not reference into a fenced prototype/ home
    (SPEC INV-17) — the prototype fence catches structural wiring (a prod file
    naming a fenced file); narrative mentions (JOURNAL.md, docs/, etc.) are excluded.
    """

    def _init_repo(self, tmp):
        run(["git", "init", "-q"], cwd=tmp)
        run(["git", "config", "user.email", "a@example.com"], cwd=tmp)
        run(["git", "config", "user.name", "a"], cwd=tmp)

    def _write(self, tmp, relpath, content):
        path = os.path.join(tmp, relpath)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def _commit_all(self, tmp):
        run(["git", "add", "-A"], cwd=tmp)
        run(["git", "commit", "-q", "-m", "scratch"], cwd=tmp)

    def test_real_repo_passes(self):
        if os.environ.get("LIVE_SPEC_SCRATCH"):
            self.skipTest("real-repo state check — meaningless in a git-less scratch copy")
        result = run([os.path.join(GUARDRAILS, "check-prototype-fence.sh")])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK (prototype fence)", result.stdout)

    def test_prod_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            self._write(tmp, "prototype/sketch.html", "<html>sketch</html>\n")
            self._write(tmp, "index.html", '<script src="prototype/sketch.html"></script>\n')
            self._commit_all(tmp)
            result = run([os.path.join(GUARDRAILS, "check-prototype-fence.sh"), tmp])
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("FAIL (prototype fence)", result.stdout)
            self.assertIn("index.html", result.stdout)
            self.assertIn("prototype/sketch.html", result.stdout)

    def test_narrative_mention_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            self._write(tmp, "prototype/sketch.html", "<html>sketch</html>\n")
            self._write(tmp, "JOURNAL.md", "Tried prototype/sketch.html today, promising.\n")
            self._write(tmp, "docs/note.md", "See prototype/sketch.html for the sketch.\n")
            self._commit_all(tmp)
            result = run([os.path.join(GUARDRAILS, "check-prototype-fence.sh"), tmp])
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("OK (prototype fence)", result.stdout)

    def test_empty_prototype_dir_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            os.makedirs(os.path.join(tmp, "prototype"), exist_ok=True)
            self._write(tmp, "readme.txt", "ordinary file, nothing fenced here.\n")
            self._commit_all(tmp)
            result = run([os.path.join(GUARDRAILS, "check-prototype-fence.sh"), tmp])
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("OK (prototype fence)", result.stdout)


class TestPrePush(unittest.TestCase):
    """pre-push wires the four check scripts together. It is NOT executed here:
    it calls check-tests.sh with no argument, which defaults to the real tests/
    dir — the very dir this file lives in — so running it from inside a test
    would make a running suite re-invoke itself (and its own re-invocation)
    without end. pre-push's real-repo behaviour is proven by a direct manual
    run outside the suite (recorded in the row-3 checkpoint); here we only
    assert its wiring is intact.
    """

    def test_pre_push_calls_all_four_checks(self):
        with open(os.path.join(GUARDRAILS, "pre-push"), encoding="utf-8") as f:
            body = f.read()
        for script in (
            "check-prover-record.sh",
            "check-tests.sh",
            "check-push-reach.sh",
            "check-matrix-coverage.sh",
            "check-prototype-fence.sh",
        ):
            self.assertIn(script, body, "pre-push no longer wires in %s" % script)
        self.assertIn("gate c", body.lower())


class TestPreCommitFence(unittest.TestCase):
    """Gate: the concurrent-edit fence (SPEC INV-11), opt-in via .live-spec-fence."""

    def _init_repo(self, tmp):
        run(["git", "init", "-q"], cwd=tmp)
        run(["git", "config", "user.email", "a@example.com"], cwd=tmp)
        run(["git", "config", "user.name", "a"], cwd=tmp)
        hooks_dir = os.path.join(tmp, ".git", "hooks")
        shutil.copy(os.path.join(GUARDRAILS, "pre-commit"), os.path.join(hooks_dir, "pre-commit"))
        os.chmod(os.path.join(hooks_dir, "pre-commit"), 0o755)
        with open(os.path.join(tmp, "f.txt"), "w") as f:
            f.write("hi\n")
        run(["git", "add", "f.txt"], cwd=tmp)
        run(["git", "commit", "-q", "-m", "init"], cwd=tmp)

    def _commit_more(self, tmp, msg):
        with open(os.path.join(tmp, "f.txt"), "a") as f:
            f.write(msg + "\n")
        run(["git", "add", "f.txt"], cwd=tmp)
        return run(["git", "commit", "-q", "-m", msg], cwd=tmp)

    def test_unarmed_fence_passes_silently(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            result = self._commit_more(tmp, "no fence")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_armed_matching_head_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            refresh = run([os.path.join(GUARDRAILS, "fence-refresh.sh")], cwd=tmp)
            self.assertEqual(refresh.returncode, 0, refresh.stdout + refresh.stderr)
            self.assertTrue(os.path.isfile(os.path.join(tmp, ".live-spec-fence")))
            result = self._commit_more(tmp, "fenced, matches")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_armed_stale_head_blocks_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            with open(os.path.join(tmp, ".live-spec-fence"), "w") as f:
                f.write("0" * 40 + "\n")
            result = self._commit_more(tmp, "should be blocked")
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("COMMIT BLOCKED", result.stdout + result.stderr)


class TestInstallScript(unittest.TestCase):
    def test_install_copies_hooks_into_scratch_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            run(["git", "init", "-q"], cwd=tmp)
            scratch_guardrails = os.path.join(tmp, "guardrails")
            shutil.copytree(GUARDRAILS, scratch_guardrails)
            result = run(["./install.sh"], cwd=scratch_guardrails)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for hook in ("pre-commit", "pre-push"):
                dest = os.path.join(tmp, ".git", "hooks", hook)
                self.assertTrue(os.path.isfile(dest), "%s not installed" % hook)
                self.assertTrue(os.stat(dest).st_mode & stat.S_IXUSR)
            # idempotent: re-running does not error
            result2 = run(["./install.sh"], cwd=scratch_guardrails)
            self.assertEqual(result2.returncode, 0, result2.stdout + result2.stderr)
            # does not arm the fence
            self.assertFalse(os.path.isfile(os.path.join(tmp, ".live-spec-fence")))


if __name__ == "__main__":
    unittest.main(verbosity=2)


class TestGateF_SkillLoadability(unittest.TestCase):
    """Gate (f): every shipped skill LOADS — frontmatter parses, name matches its
    folder, description + metadata version present, a 'when NOT to use' section
    scopes it negatively (row 80). Red-first proven on a broken scratch skill."""

    def test_real_repo_passes(self):
        result = run([os.path.join(GUARDRAILS, "check-skill-loadability.sh"),
                      os.path.join(ROOT, "skills")])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_broken_skill_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = os.path.join(tmp, "broken")
            os.makedirs(bad)
            with open(os.path.join(bad, "SKILL.md"), "w") as f:
                f.write("---\nname: wrongname\n---\nno negative section\n")
            result = run([os.path.join(GUARDRAILS, "check-skill-loadability.sh"), tmp])
            self.assertEqual(result.returncode, 1, "broken skill must turn the gate RED")
            self.assertIn("does not match its folder", result.stdout)
            self.assertIn("no 'when NOT to use' section", result.stdout)

    def test_missing_skills_dir_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run([os.path.join(GUARDRAILS, "check-skill-loadability.sh"), tmp])
            self.assertEqual(result.returncode, 1, "empty skills dir must fail, not pass silently")


class TestGateG_PinDrift(unittest.TestCase):
    """Gate (g): architecture pins must not rot (SPEC E-14, row 90) — file-missing or
    beyond-EOF is RED; label-not-near-line is reported drift (RED under --strict)."""

    def test_real_repo_passes(self):
        result = run([os.path.join(GUARDRAILS, "check-pin-drift.sh"),
                      os.path.join(ROOT, "ARCHITECTURE.md")])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            arch = os.path.join(tmp, "ARCHITECTURE.md")
            with open(arch, "w") as f:
                f.write("## Nodes\n| n | r | E-1 | `ghost.py:5` (spine) |\n## Seams\n")
            result = run([os.path.join(GUARDRAILS, "check-pin-drift.sh"), arch])
            self.assertEqual(result.returncode, 1, "missing pinned file must be RED")
            self.assertIn("pinned file missing", result.stdout)

    def test_label_drift_strict_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, "code.py")
            with open(target, "w") as f:
                f.write("\n" * 100)
            arch = os.path.join(tmp, "ARCHITECTURE.md")
            with open(arch, "w") as f:
                f.write("## Nodes\n| n | r | E-1 | `code.py:50` (nonexistent-symbol) |\n## Seams\n")
            soft = run([os.path.join(GUARDRAILS, "check-pin-drift.sh"), arch])
            self.assertEqual(soft.returncode, 0, "non-strict drift must report, not block")
            self.assertIn("DRIFT", soft.stdout)
            strict = run([os.path.join(GUARDRAILS, "check-pin-drift.sh"), arch, "--strict"])
            self.assertEqual(strict.returncode, 1, "strict drift must be RED")


class TestGateTimeFence(unittest.TestCase):
    """Row 104 (M-110, INV-24 second arm): an added line pairing today's date with a
    clock time later than the commit moment goes red at pre-commit."""

    def _run_check(self, line, today="2026-01-01", now="12:00"):
        import subprocess, tempfile, os
        script = os.path.join(ROOT, "guardrails", "check-future-times.sh")
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(["git", "init", "-q", d], check=True)
            p = os.path.join(d, "note.md")
            with open(p, "w") as f:
                f.write(line + "\n")
            subprocess.run(["git", "-C", d, "add", "note.md"], check=True)
            return subprocess.run(
                ["bash", script],
                cwd=d,
                env={**os.environ, "CHECK_TODAY": today, "CHECK_NOW": now},
                capture_output=True, text=True)

    def test_future_time_today_goes_red(self):
        r = self._run_check("landed 2026-01-01 13:00, session 99")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)

    def test_past_time_today_stays_green(self):
        r = self._run_check("landed 2026-01-01 11:00, session 99")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_other_day_time_stays_green(self):
        r = self._run_check("landed 2025-12-31 13:00 (quoted past incident)")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_mixed_history_line_stays_green(self):
        """F9: a line mixing today's date with QUOTED times of other moments
        (a ledger occurrence list) is legal — only the ADJACENT stamp shape trips."""
        r = self._run_check(
            'occurrences: 2025-12-31 (stamps "23:50"/"23:58" corrected), '
            '2026-01-01 ~11:00 (fourth catch; the "13:40" quote stays legal)')
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_adjacent_future_stamp_still_red_after_narrowing(self):
        r = self._run_check("queued 2026-01-01 ~13:05, session 99")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)


class TestGateReachMap(unittest.TestCase):
    """Row 147 (M-142, INV-45): the reach map's deciding script — a prose-only diff
    stands the suite down; tested documents, unknown files, and empty diffs fall to
    FULL by construction."""

    SCRIPT = os.path.join(GUARDRAILS, "check-push-reach.sh")

    def reach(self, files):
        return run(["bash", self.SCRIPT], extra_env={"REACH_FILES": files})

    def test_prose_only_diff_stands_suite_down(self):
        r = self.reach("README.md\ndocs/research/example.md")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_tested_documents_stay_full_reach(self):
        for f in ("PRODUCT_SPEC.md", "TEST_MATRIX.md", "ARCHITECTURE.md", "ROADMAP.md",
                  "skills/publish/SKILL.md", "tests/test_traceability.py",
                  "guardrails/pre-push", "JOURNAL.md", "NEXT_STEPS.md"):
            r = self.reach("README.md\n" + f)
            self.assertEqual(r.returncode, 1, "%s must force FULL, got: %s" % (f, r.stdout))

    def test_unknown_and_empty_fall_to_full(self):
        self.assertEqual(self.reach("something/new-place.txt").returncode, 1)
        self.assertEqual(self.reach("\n").returncode, 1)


class TestPytestFromRoot(unittest.TestCase):
    """Row 106 (M-143): a stranger's `python3 -m pytest` from the repo root must
    collect the real suite cleanly and never trip over the scaffold template."""

    def test_pytest_collects_clean_from_root(self):
        import sys
        r = run([sys.executable, "-m", "pytest", "--collect-only", "-q"], cwd=ROOT)
        self.assertEqual(r.returncode, 0, (r.stdout or "")[-2000:] + (r.stderr or "")[-2000:])
        self.assertNotIn("test_scaffold.template", r.stdout,
                         "the scaffold template must never be collected")


class TestGateHygieneContract(unittest.TestCase):
    """Row 114 (M-145, INV-47): the gate contract — a typed failure line on a
    blocking gate's red, a declared blocking/advisory taxonomy, all-or-nothing
    writes; the reach decider exempt by name."""

    def _init_repo(self, tmp):
        run(["git", "init", "-q"], cwd=tmp)
        run(["git", "config", "user.email", "a@example.com"], cwd=tmp)
        run(["git", "config", "user.name", "a"], cwd=tmp)

    def _write(self, tmp, relpath, content):
        path = os.path.join(tmp, relpath)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def _commit_all(self, tmp):
        run(["git", "add", "-A"], cwd=tmp)
        run(["git", "commit", "-q", "-m", "scratch"], cwd=tmp)

    def test_readme_states_contract(self):
        with open(os.path.join(GUARDRAILS, "README.md"), encoding="utf-8") as f:
            body = f.read()
        for needle in ('"severity"', "blocking or advisory", "before writing any",
                       "check-push-reach.sh", "INV-47"):
            self.assertIn(needle, body, "guardrails README missing: %s" % needle)

    def test_prototype_fence_emits_typed_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._init_repo(tmp)
            self._write(tmp, "prototype/sketch.html", "<html>sketch</html>\n")
            self._write(tmp, "index.html", '<script src="prototype/sketch.html"></script>\n')
            self._commit_all(tmp)
            result = run([os.path.join(GUARDRAILS, "check-prototype-fence.sh"), tmp])
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            json_line = None
            for line in result.stdout.splitlines():
                if line.startswith("{"):
                    json_line = line
                    break
            self.assertIsNotNone(json_line, "no typed JSON failure line found in: " + result.stdout)
            payload = json.loads(json_line)
            self.assertEqual(
                set(payload.keys()), {"severity", "code", "message", "fix"},
                "typed failure line has unexpected keys: %r" % (payload,)
            )
            self.assertEqual(payload["severity"], "error")
            self.assertEqual(payload["code"], "prototype-fence")


class TestCIMirror(unittest.TestCase):
    """Row 14 (M-154, SPEC M-5): the CI mirror ships — the same gate scripts as a
    second net; the reach map stays a local optimization."""

    def test_workflow_ships_and_mirrors_the_gates(self):
        path = os.path.join(ROOT, ".github", "workflows", "gates.yml")
        self.assertTrue(os.path.isfile(path), "gates.yml missing")
        with open(path, encoding="utf-8") as f:
            body = f.read()
        for needle in ("pytest", "check-prover-record.sh", "check-matrix-coverage.sh",
                       "check-pin-drift.sh", "check-skill-loadability.sh",
                       "check-prototype-fence.sh", "fetch-depth: 0"):
            self.assertIn(needle, body, "gates.yml missing: %s" % needle)

    def test_readme_carries_the_mirror_guidance(self):
        with open(os.path.join(GUARDRAILS, "README.md"), encoding="utf-8") as f:
            body = f.read()
        for needle in ("CI mirror", "second net", "never redefines"):
            self.assertIn(needle, body, "guardrails README missing: %s" % needle)

    def test_machine_local_pins_skip_in_ci_only(self):
        """The CI net must not false-red on pins that live only on the author's
        machine (~/.claude/...), while the local run stays strict (row 14's first
        live CI run caught exactly this)."""
        if os.environ.get("LIVE_SPEC_SCRATCH"):
            self.skipTest("machine-local pin behaviour — meaningless in a git-less scratch copy")
        script = os.path.join(GUARDRAILS, "check-pin-drift.sh")
        in_ci = run([script], extra_env={"CI": "true", "HOME": "/nonexistent-ci-home"})
        self.assertEqual(in_ci.returncode, 0, in_ci.stdout + in_ci.stderr)
        self.assertIn("machine-local pin, absent in CI; skipped", in_ci.stdout)
        local = run([script], extra_env={"CI": "", "HOME": "/nonexistent-ci-home"})
        self.assertEqual(local.returncode, 1,
                         "outside CI a missing machine-local pin must stay a hard FAIL")


class TestPreShowLint(unittest.TestCase):
    """Row 170 (M-177, INV-28 mechanical arm): the pre-show lint catches a human-facing
    line that OPENS with an internal handle (a spec code or a row/session number) before
    the human sees it — the leak that put 'Rows 166 …' at the head of a chat report."""

    SCRIPT = os.path.join(ROOT, "scripts", "preshow-lint.py")

    def _lint(self, text):
        return subprocess.run(["python3", self.SCRIPT, "-"], input=text,
                              capture_output=True, text=True)

    def test_leading_handle_goes_red(self):
        for bad in ("Rows 166 and 148 await your word.",
                    "INV-70 landed and pushed.",
                    "- row 170 is the durable fix.",
                    "M-176 pins the test."):
            r = self._lint(bad)
            self.assertEqual(r.returncode, 1, "should flag a leading handle: %r" % bad)
            self.assertIn("leading-handle", r.stdout)

    def test_outcome_led_and_trailing_anchor_pass(self):
        for good in ("The live board is now just chat narration, no HTML (row 166).",
                     "A guard catches jargon before you see it (INV-28).",
                     "The feature map is readable on demand."):
            r = self._lint(good)
            self.assertEqual(r.returncode, 0,
                             "outcome-led / trailing-anchor text must pass: %r\n%s" % (good, r.stdout))


class TestSpecStyleLint(unittest.TestCase):
    """The mechanical arm of the SPEC prose register (docs/spec-style.md): the durable fix for the
    hand-rewrite drift that kept re-styling the spec into an ugly voice. It flags the register tells
    a reader caught late — a rule that defines by exclusion ('X does not become Y') before saying
    what it is, machine jargon, ALL-CAPS shout, the «X — not Y» scissors — so a section is driven to
    clean against a machine at any length, not against a human's patience."""

    SCRIPT = os.path.join(ROOT, "scripts", "spec-style-lint.py")

    def _lint(self, text):
        return subprocess.run(["python3", self.SCRIPT, "-"], input=text,
                              capture_output=True, text=True)

    def test_register_tells_go_red(self):
        cases = [
            ("Several open picks do not become a serialized questionnaire.", "negation-opener"),
            ("The map is not a separate document.", "negation-opener"),
            ("A wish carries a serialized questionnaire of open picks.", "machine-jargon"),
            ("The card shows the outcome — not the mechanism.", "scissors"),
        ]
        for text, code in cases:
            r = self._lint(text)
            self.assertEqual(r.returncode, 1, "should flag %s: %r\n%s" % (code, text, r.stdout))
            self.assertIn(code, r.stdout, "expected %s for %r\n%s" % (code, text, r.stdout))

    def test_legit_register_passes_clean(self):
        # a PROHIBITION ("does not ask" / "never re-carves") is correct register (R4), not a tell;
        # a noun-negative ("no design decision inside") and a fronted condition are fine too.
        for good in ("The walk does not ask how long a wish will take.",
                     "A restructure verdict never re-carves in passing.",
                     "Quick win: low effort, immediate value, no design decision inside.",
                     "When the classifier cannot call a size, it asks the human at intake.",
                     "Each question is a card, the recommended answer marked, with room to write a different one."):
            r = self._lint(good)
            self.assertEqual(r.returncode, 0,
                             "correct-register prose must pass clean: %r\n%s" % (good, r.stdout))

    def test_soft_signals_warn_but_do_not_fail(self):
        # caps-shout and second-person are advisory: printed, but exit 0 (they do not block a gate
        # the way an ERROR does — the whole un-converted spec still carries them).
        r = self._lint("You open the page and it CHANGES the queue.")
        self.assertEqual(r.returncode, 0, "warn-only text must exit 0\n%s" % r.stdout)
        self.assertIn("second-person", r.stdout)
        self.assertIn("caps-shout", r.stdout)

    def test_converted_intake_section_is_clean(self):
        # the calibration section, converted this session, is the standing gold: it must stay clean
        # of register ERRORS, so a regression in the linter OR in the section trips here.
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            spec = f.read()
        lines = spec.splitlines()
        start = next(i for i, l in enumerate(lines) if l.startswith("#### Intake:"))
        end = next(i for i in range(start + 1, len(lines))
                   if lines[i].startswith(("#### ", "### ", "## ")))
        section = "\n".join(lines[start:end])
        r = self._lint(section)
        self.assertEqual(r.returncode, 0,
                         "the converted intake section must stay register-clean:\n%s" % r.stdout)

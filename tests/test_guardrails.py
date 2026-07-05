"""Guardrails suite — the pack's own git-hook gates, mechanized (ROADMAP row 3).

Zero dependencies beyond the stdlib; run from the repo root:
  python3 -m unittest discover tests -v

Asserts the SHIPPED guardrails/ scripts on disk, and exercises each gate's check
logic both against the real repo state (must be green today) and against scratch
fixtures (must fail the way the gate promises to fail).
"""

import os
import shutil
import stat
import subprocess
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUARDRAILS = os.path.join(ROOT, "guardrails")


def run(args, cwd=None):
    return subprocess.run(
        args, cwd=cwd or ROOT, capture_output=True, text=True
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


class TestGateB_Tests(unittest.TestCase):
    """Gate (b): the test suite must be green (also covers gate c, anchor ownership).

    Both checks here run against a SCRATCH COPY of the whole repo (test_traceability.py
    resolves its fixture paths — SPEC.md, ARCHITECTURE.md, etc. — relative to the repo
    root, so a bare copy of tests/ alone would 404 on every one of them) with
    test_guardrails.py itself excluded from the copy. Pointing check-tests.sh at the
    real tests/ dir (which contains this very file) would make a running test
    re-invoke the whole suite, including itself, forever — a fork bomb, not a check.
    Gate (b)'s real-repo behaviour is proven directly by manual runs (recorded in the
    row-3 checkpoint), not re-executed recursively from inside the suite it would be
    discovering.
    """

    def _scratch_tests_dir(self, tmp):
        dest = os.path.join(tmp, "repo")
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        scratch_tests = os.path.join(dest, "tests")
        os.remove(os.path.join(scratch_tests, "test_guardrails.py"))
        return scratch_tests

    def test_real_content_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            scratch_tests = self._scratch_tests_dir(tmp)
            result = run([os.path.join(GUARDRAILS, "check-tests.sh"), scratch_tests])
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("OK (tests)", result.stdout)
            self.assertIn("Ran 20 tests", result.stdout + result.stderr)

    def test_broken_suite_fails(self):
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
            result = run([os.path.join(GUARDRAILS, "check-tests.sh"), scratch_tests])
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


class TestPrePush(unittest.TestCase):
    """pre-push wires the three check scripts together. It is NOT executed here:
    it calls check-tests.sh with no argument, which defaults to the real tests/
    dir — the very dir this file lives in — so running it from inside a test
    would make a running suite re-invoke itself (and its own re-invocation)
    without end. pre-push's real-repo behaviour is proven by a direct manual
    run outside the suite (recorded in the row-3 checkpoint); here we only
    assert its wiring is intact.
    """

    def test_pre_push_calls_all_three_checks(self):
        with open(os.path.join(GUARDRAILS, "pre-push"), encoding="utf-8") as f:
            body = f.read()
        for script in ("check-prover-record.sh", "check-tests.sh", "check-matrix-coverage.sh"):
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

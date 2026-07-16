"""INV-175 — the installed gate is the source gate, held by a config-health check.

A gate lives twice: source in guardrails/ travels with the repo, the installed copy in
.git/hooks/ actually runs. They drift the moment an install is skipped — the worked instance:
on 2026-07-16 the installed pre-push was missing gates k (freeze) and l (muted launch) that the
source carried. The check reds on a missing or drifted installed hook and names the one fix;
it runs inside the suite so even a stale pre-push surfaces the drift (self-healing); a checkout
with no installed hooks by design (CI) skips by name. The commit fence gains a second arm: a
file both staged and carrying unstaged modifications is a fence stop on the shared index.
"""
import json
import os
import subprocess
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = os.path.join(REPO, "guardrails", "check-config-health.sh")


def run_check(cwd, env_extra=None):
    env = dict(os.environ)
    env.pop("GITHUB_ACTIONS", None)
    env.pop("CI", None)  # the CI runner sets both; the temp-repo tests exercise the non-CI arm
    if env_extra:
        env.update(env_extra)
    return subprocess.run(["bash", CHECK], cwd=cwd, capture_output=True, text=True, env=env)


def make_repo(tmp, install=("pre-commit", "pre-push"), drift=None):
    subprocess.run(["git", "init", "-q", tmp], check=True)
    gdir = os.path.join(tmp, "guardrails")
    os.makedirs(gdir)
    for name in ("pre-commit", "pre-push"):
        with open(os.path.join(gdir, name), "w") as f:
            f.write("#!/bin/sh\nexit 0\n")
    hooks = os.path.join(tmp, ".git", "hooks")
    for name in install:
        body = "#!/bin/sh\nexit 0\n" if drift != name else "#!/bin/sh\n# stale\nexit 0\n"
        with open(os.path.join(hooks, name), "w") as f:
            f.write(body)
        os.chmod(os.path.join(hooks, name), 0o755)
    return tmp


class TestConfigHealth(unittest.TestCase):
    def test_this_repo_installed_hooks_match_source(self):
        if os.environ.get("LIVE_SPEC_SCRATCH"):
            self.skipTest("scratch copy installs no hooks by design")
        r = run_check(REPO)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_missing_installed_hook_reds(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_repo(tmp, install=("pre-commit",))
            r = run_check(tmp)
            self.assertEqual(r.returncode, 1)
            self.assertIn("config-health", r.stdout)
            self.assertIn("guardrails/install.sh", r.stdout)

    def test_drifted_installed_hook_reds(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_repo(tmp, drift="pre-push")
            r = run_check(tmp)
            self.assertEqual(r.returncode, 1)
            self.assertIn("pre-push", r.stdout)

    def test_matching_hooks_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_repo(tmp)
            r = run_check(tmp)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_ci_checkout_skips_by_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_repo(tmp, install=())
            r = run_check(tmp, env_extra={"GITHUB_ACTIONS": "true"})
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("skip", r.stdout.lower())


class TestStagedVsWorktreeFenceArm(unittest.TestCase):
    def _repo_with_precommit(self, tmp):
        subprocess.run(["git", "init", "-q", tmp], check=True)
        subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t"], check=True)
        subprocess.run(["git", "-C", tmp, "config", "user.name", "t"], check=True)
        gdir = os.path.join(tmp, "guardrails")
        os.makedirs(gdir)
        src = os.path.join(REPO, "guardrails", "pre-commit")
        with open(src) as f:
            body = f.read()
        dst = os.path.join(tmp, ".git", "hooks", "pre-commit")
        with open(dst, "w") as f:
            f.write(body)
        os.chmod(dst, 0o755)

    def test_staged_file_with_unstaged_edits_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._repo_with_precommit(tmp)
            p = os.path.join(tmp, "a.txt")
            open(p, "w").write("one\n")
            subprocess.run(["git", "-C", tmp, "add", "a.txt"], check=True)
            open(p, "a").write("two\n")  # unstaged edit on a staged file
            r = subprocess.run(["git", "-C", tmp, "commit", "-m", "x"],
                               capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("staged", (r.stdout + r.stderr).lower())

    def test_clean_staged_commit_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._repo_with_precommit(tmp)
            p = os.path.join(tmp, "a.txt")
            open(p, "w").write("one\n")
            subprocess.run(["git", "-C", tmp, "add", "a.txt"], check=True)
            r = subprocess.run(["git", "-C", tmp, "commit", "-m", "x"],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()

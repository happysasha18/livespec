"""The lane's branch-and-merge road (SPEC E-34, T-23, INV-198..201; ROADMAP rows 386, 412).

A lane's isolated copy is a git worktree holding a branch of its own, cut from the claim
commit on main, penless while it rolls, landed by fast-forward from a rebased branch, and
torn down at its landing.

Two kinds of fact live here and they get two honest treatments.

The document law — the branch's name, the walk's order, the pen's reach, the vendored line —
is a string assertion against the shipped spec, live-spec's own rendered rung.

The road's central claim is a different animal: INV-198 says git ITSELF refuses another
worktree's attempt to move a branch a tree holds checked out, which is why "holding the pen
is the sole right to move main" needs no gate the pack writes. That claim is about a real
engine's runtime behaviour, and no string assertion against a shipped file can see it — the
spec's sentence would read exactly the same on the day git stopped refusing. So those rows
are proven by deed on a real two-worktree repo built in the system temp home (SPEC INV-100:
the suite's own prefix, erased at teardown), and the probe is hermetic — the user's global
and system git config are switched off, so the run reads git's defaults rather than this
machine's habits (SPEC INV-155).

The boundary is pinned beside the guarantee on purpose. Git's refusal covers the three
porcelain roads an agent walks by habit and leaves named doors open, and a suite that pinned
only the happy three would certify a guarantee wider than the one git actually gives.
"""

import os
import shutil
import subprocess
import tempfile
import unittest

from conftest import ROOT, read_flat


def _git(cwd, *args):
    """Run git hermetically: the machine's own global/system config never speaks here."""
    env = dict(os.environ)
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_SYSTEM": os.devnull,
        "GIT_AUTHOR_NAME": "livespec-test",
        "GIT_AUTHOR_EMAIL": "livespec-test@example.invalid",
        "GIT_COMMITTER_NAME": "livespec-test",
        "GIT_COMMITTER_EMAIL": "livespec-test@example.invalid",
        "GIT_TERMINAL_PROMPT": "0",
    })
    proc = subprocess.run(("git",) + args, cwd=cwd, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


class _ProbeRepo(unittest.TestCase):
    """A real repo in two worktrees: the primary tree holds main, a lane worktree holds lane/x.

    This is the shape INV-198 legislates, so every deed below runs against the real thing.
    setUp asserts the probe IS that shape before any test reads it — a probe that quietly
    failed to build would hand every assertion below a vacuous pass (ROADMAP row 384).
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="livespec-test-lane-")
        self.main_tree = os.path.join(self.tmp, "primary")
        self.lane_tree = os.path.join(self.tmp, "lane")
        os.makedirs(self.main_tree)
        self.run_ok(self.main_tree, "init", "-q", "-b", "main")
        self.commit(self.main_tree, "f", "one\n", "one")
        self.run_ok(self.main_tree, "worktree", "add", "-q", self.lane_tree, "-b", "lane/x")
        self.commit(self.lane_tree, "g", "two\n", "two")

        self.lane_sha = self.rev("HEAD", self.lane_tree)
        self.main_sha = self.rev("main", self.lane_tree)
        self.assertNotEqual(self.lane_sha, self.main_sha,
                            "probe did not build: the lane never diverged from main")
        _, listing = _git(self.lane_tree, "worktree", "list")
        self.assertIn("[main]", listing,
                      "probe did not build: no tree holds main, which is the very condition "
                      "INV-198's guarantee rests on")
        _, status = _git(self.main_tree, "status", "--short")
        self.assertEqual(status.strip(), "",
                         "probe did not build: the primary tree is dirty before any test ran")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_ok(self, cwd, *args):
        rc, out = _git(cwd, *args)
        self.assertEqual(rc, 0, "probe setup failed: git %s -> %s" % (" ".join(args), out))
        return out

    def commit(self, tree, name, body, message):
        with open(os.path.join(tree, name), "w", encoding="utf-8") as fh:
            fh.write(body)
        self.run_ok(tree, "add", name)
        self.run_ok(tree, "commit", "-qm", message)

    def rev(self, ref, cwd=None):
        rc, out = _git(cwd or self.lane_tree, "rev-parse", ref)
        self.assertEqual(rc, 0, "rev-parse %s: %s" % (ref, out))
        return out.strip()


class TestGitRefusesAnotherWorktreeMovingMain(_ProbeRepo):
    """M-373 (INV-198), by deed: the pen's central clause, enforced by the tool itself.

    Verified on a probe repo 2026-07-17, and re-verified here at every run — because this is
    the one fact the road leans on that no document can hold up.
    """

    def test_checkout_of_a_checked_out_main_is_refused_by_name(self):
        rc, out = _git(self.lane_tree, "checkout", "main")
        self.assertNotEqual(rc, 0, "the lane checked out main while the primary tree held it")
        self.assertIn("already used by worktree", out,
                      "git refused for some other reason than the worktree holding main: %s" % out)
        self.assertEqual(self.rev("HEAD"), self.lane_sha, "the lane's HEAD moved off its own branch")

    def test_force_update_of_a_checked_out_main_is_refused_by_name(self):
        rc, out = _git(self.lane_tree, "branch", "-f", "main", self.lane_sha)
        self.assertNotEqual(rc, 0, "the lane force-moved main while the primary tree held it")
        self.assertIn("cannot force update the branch", out,
                      "git refused for some other reason: %s" % out)
        self.assertEqual(self.rev("main"), self.main_sha, "main moved under the primary tree")

    def test_push_to_a_checked_out_main_is_refused_by_name(self):
        rc, out = _git(self.lane_tree, "push", ".", "HEAD:main")
        self.assertNotEqual(rc, 0, "the lane pushed to main while the primary tree held it")
        self.assertIn("refusing to update checked out branch", out,
                      "git refused for some other reason: %s" % out)
        self.assertEqual(self.rev("main"), self.main_sha, "main moved under the primary tree")

    def test_the_push_refusal_is_not_bought_off_with_force(self):
        """--force is the first thing a stuck agent reaches for, so the refusal is pinned against it."""
        rc, out = _git(self.lane_tree, "push", "--force", ".", "HEAD:main")
        self.assertNotEqual(rc, 0, "--force bought off the refusal")
        self.assertIn("refusing to update checked out branch", out)
        self.assertEqual(self.rev("main"), self.main_sha, "main moved under the primary tree")


class TestTheRefusalsBoundary(_ProbeRepo):
    """M-374 (INV-198), by deed: where the tool's guarantee stops.

    INV-198 names the guarantee's condition — the primary tree holds main — and marks the
    config-health check that asserts it [target]. These deeds are why that check is owed, and
    they pin the doors git leaves open, so the road never reads as wider than the tool it rests on.
    Each of these going red would be good news: it would mean git closed a door and the law can grow.
    """

    def test_the_refusals_lapse_when_no_tree_holds_main(self):
        self.run_ok(self.main_tree, "checkout", "-q", "--detach", "HEAD")
        rc, out = _git(self.lane_tree, "branch", "-f", "main", self.lane_sha)
        self.assertEqual(rc, 0, "git kept refusing though no tree held main: %s" % out)
        self.assertEqual(self.rev("main"), self.lane_sha,
                         "main did not move once no tree held it — INV-198's guarantee would not "
                         "rest on the primary tree holding main, and its config-health check "
                         "would be moot")

    def test_update_ref_walks_past_every_refusal(self):
        """git's plumbing carries no worktree check at all, and plumbing is what a script reaches for."""
        rc, out = _git(self.lane_tree, "update-ref", "refs/heads/main", self.lane_sha)
        self.assertEqual(rc, 0, "update-ref failed for an unrelated reason: %s" % out)
        self.assertEqual(self.rev("main"), self.lane_sha,
                         "update-ref no longer moves a checked-out main — git closed the door and "
                         "INV-198's guarantee is wider than it was when this was written")

    def test_update_ref_leaves_the_primary_tree_inconsistent(self):
        """The damage the porcelain refusals name in their own error text, done silently."""
        self.run_ok(self.lane_tree, "update-ref", "refs/heads/main", self.lane_sha)
        _, status = _git(self.main_tree, "status", "--short")
        self.assertNotEqual(status.strip(), "",
                            "the primary tree read clean after its branch moved under it")

    def test_the_checkout_refusal_carries_a_documented_override_flag(self):
        rc, out = _git(self.lane_tree, "checkout", "--ignore-other-worktrees", "main")
        self.assertEqual(rc, 0, "--ignore-other-worktrees no longer overrides the refusal: %s" % out)

    def test_the_push_refusal_is_a_config_default_rather_than_a_law(self):
        self.run_ok(self.main_tree, "config", "receive.denyCurrentBranch", "ignore")
        rc, out = _git(self.lane_tree, "push", ".", "HEAD:main")
        self.assertEqual(rc, 0, "the push stayed refused under denyCurrentBranch=ignore: %s" % out)
        self.assertEqual(self.rev("main"), self.lane_sha,
                         "main did not move though the config said to allow it")


class TestLaneIntegrationMechanics(_ProbeRepo):
    """M-375 (INV-199) and M-376 (INV-200), by deed: the gate's own check and the tool's conflict net."""

    def merge_base_equals_main_tip(self):
        """INV-199's gate check, run exactly as the spec states it."""
        base = self.rev("HEAD", self.lane_tree)
        rc, out = _git(self.lane_tree, "merge-base", "main", "HEAD")
        self.assertEqual(rc, 0, "merge-base failed: %s" % out)
        base = out.strip()
        return base == self.rev("main", self.lane_tree)

    def test_merge_base_check_separates_a_stale_lane_from_a_rebased_one(self):
        self.assertTrue(self.merge_base_equals_main_tip(),
                        "a lane cut from main's tip read as stale before main ever moved")
        # another lane lands: main moves under this one
        self.commit(self.main_tree, "h", "three\n", "three")
        self.assertFalse(self.merge_base_equals_main_tip(),
                         "a lane that has not rebased read as rebased — the landing gate would "
                         "run on a stale tree, which is the exact thing the check stands against")
        self.run_ok(self.lane_tree, "rebase", "main")
        self.assertTrue(self.merge_base_equals_main_tip(),
                        "a rebased lane still read as stale — the check would red every landing")

    def test_a_rebased_lane_fast_forwards_main_with_no_merge_commit(self):
        self.commit(self.main_tree, "h", "three\n", "three")
        self.run_ok(self.lane_tree, "rebase", "main")
        self.run_ok(self.main_tree, "merge", "--ff-only", "lane/x")
        _, parents = _git(self.main_tree, "rev-list", "--parents", "-n", "1", "main")
        self.assertEqual(len(parents.split()), 2,
                         "main's tip carries more than one parent — a merge commit's second "
                         "parent breaks INV-39's one-row landing commit")
        self.assertEqual(self.rev("main", self.main_tree), self.rev("lane/x", self.main_tree),
                         "the fast-forward did not land the lane's work on main")

    def test_git_halts_a_rebase_on_a_textual_conflict(self):
        self.commit(self.main_tree, "f", "the pen's line\n", "main edits f")
        self.commit(self.lane_tree, "f", "the lane's line\n", "lane edits f")
        rc, out = _git(self.lane_tree, "rebase", "main")
        self.assertNotEqual(rc, 0, "the rebase sailed through a textual conflict")
        self.assertIn("CONFLICT", out.upper(), "git halted for some other reason: %s" % out)
        self.run_ok(self.lane_tree, "rebase", "--abort")

    def test_two_worktrees_share_one_ref_store_so_a_foreign_claim_needs_no_fetch(self):
        """T-18/INV-198: the pen's arbitration reads a foreign session's claim the moment it looks."""
        self.commit(self.main_tree, "queue", "row 1: in-work\n", "claim row 1")
        claim = self.rev("main", self.main_tree)
        self.assertEqual(self.rev("main", self.lane_tree), claim,
                         "the lane read a stale main — a foreign session's claim commit would "
                         "need a fetch, and INV-2's ancestry ordering could not read it")
        rc, out = _git(self.lane_tree, "log", "-1", "--format=%s", "main")
        self.assertEqual(rc, 0, out)
        self.assertIn("claim row 1", out, "the lane could not read the foreign claim's own commit")


class TestLaneTeardown(_ProbeRepo):
    """M-382 (INV-199), by deed: teardown's refusal is the thing that protects a parked lane's work."""

    def test_teardown_is_refused_on_a_worktree_holding_uncommitted_work(self):
        with open(os.path.join(self.lane_tree, "unfinished.txt"), "w", encoding="utf-8") as fh:
            fh.write("a parked lane's half-done work\n")
        rc, out = _git(self.main_tree, "worktree", "remove", self.lane_tree)
        self.assertNotEqual(rc, 0, "teardown erased a lane worktree holding uncommitted work")
        self.assertIn("contains modified or untracked files", out,
                      "teardown refused for some other reason: %s" % out)
        self.assertTrue(os.path.isdir(self.lane_tree), "the lane's tree was removed anyway")

    def test_the_teardown_refusal_carries_a_force_override(self):
        """The boundary beside the guarantee: the refusal is a default, and --force walks past it."""
        with open(os.path.join(self.lane_tree, "unfinished.txt"), "w", encoding="utf-8") as fh:
            fh.write("a parked lane's half-done work\n")
        rc, out = _git(self.main_tree, "worktree", "remove", "--force", self.lane_tree)
        self.assertEqual(rc, 0, "--force no longer overrides the teardown refusal: %s" % out)
        self.assertFalse(os.path.isdir(self.lane_tree), "the lane's tree survived a forced removal")


class TestLaneBranchLaw(unittest.TestCase):
    """M-372 / M-373 / M-375 / M-376 / M-377: the document law, at live-spec's rendered rung."""

    def test_spec_names_the_worktree_mechanism_and_the_branch_name(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("The mechanism is a git worktree holding a branch of its own", spec)
        self.assertIn("`lane/<row>-<slug>`", spec)
        self.assertIn("git branch --list 'lane/*'", spec)

    def test_spec_grants_a_worker_lane_its_worktree_with_no_gate(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn('`isolation: \"worktree\"`', spec)
        self.assertIn("carries no gate", spec)

    def test_the_claim_commits_to_main_and_the_spec_states_why(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("A lane branch is born from the claim commit, on main", spec)
        self.assertIn("orders two claims by git ancestry", spec)
        self.assertIn("each read themselves as first", spec)

    def test_the_pen_moves_main_and_the_lane_branch_is_penless(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("holding the pen is the sole right to move main", spec)
        self.assertIn("that traffic is penless", spec)

    def test_the_pen_keeps_the_documents_and_the_spec_states_why(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("the collision the pen prevents was never textual", spec)
        self.assertIn("no suite reads a proof", spec)

    def test_the_landing_is_rebase_then_gate_then_fast_forward(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("A lane lands by fast-forward from a rebased branch", spec)
        self.assertIn("the branch's merge-base with main equals main's tip", spec)

    def test_teardown_and_the_stale_lane_check(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("Teardown is refused on a worktree holding uncommitted work", spec)
        self.assertIn("a lane worktree or a lane branch with no open row reds in the config-health gate", spec)

    def test_the_semantic_residual_is_named_rather_than_papered_over(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("Git halts the rebase on a textual conflict", spec)
        self.assertIn("a fact no test covers", spec)
        self.assertIn("matrix gap", spec)

    def test_the_vendored_line_cites_inv105_rather_than_restating_it(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("cites INV-105's condition rather than restating it", spec)
        self.assertIn("keeps the condition's one home", spec)
        self.assertIn("A line in the machine-wide instruction file would reach every project", spec)

    def test_every_new_anchor_carries_an_index_row(self):
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as fh:
            index = [line for line in fh if line.startswith("| ")]
        for anchor in ("E-34", "T-23", "INV-198", "INV-199", "INV-200", "INV-201"):
            rows = [line for line in index if line.startswith("| %s |" % anchor)]
            self.assertEqual(len(rows), 1, "%s owes exactly one Formal index row" % anchor)


if __name__ == "__main__":
    unittest.main()

"""The standalone mirrors sync automatically, from two homes — the local push gate and the CI net.

The pack is the single source of truth for every skill; a standalone skill (e.g. product-prover)
also lives as its own read-only mirror repo, updated only by scripts/sync-mirrors.sh. Left to a hand,
that sync drifts: a mirror was found one version behind the pack on 2026-07-13. So the sync is wired to
run on its own from both nets that already guard a push — the local pre-push hook (this developer's
machine) and the CI workflow (any machine, after the gates pass). The CI arm is token-gated: it skips
gracefully until a MIRROR_SYNC_TOKEN secret with write access to the mirror repos is present. Extends
the push gate (SPEC M-6) and the attribution/mirror mechanism (SPEC INV-96)."""
import os
import unittest
from conftest import ROOT


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class TestMirrorAutosync(unittest.TestCase):
    def test_local_prepush_syncs_on_a_green_gate(self):
        hook = read("guardrails/pre-push")
        # runs the one sync script, never a second scheme
        self.assertIn("scripts/sync-mirrors.sh", hook)
        # non-blocking: the sync sits in the green-gate path and warns rather than failing the push
        self.assertIn("mirror sync (non-blocking)", hook)
        # the sync must sit AFTER the blocked-push exit, so a blocked push never reaches a mirror
        blocked = hook.index("PUSH BLOCKED")
        sync = hook.index("scripts/sync-mirrors.sh")
        self.assertLess(blocked, sync, "mirror sync must run only past the blocked-push gate")

    def test_ci_job_syncs_after_the_gates(self):
        ci = read(".github/workflows/gates.yml")
        self.assertIn("sync-mirrors:", ci)
        # runs only after the gates pass, only on a push to main
        self.assertIn("needs: gates", ci)
        self.assertIn("refs/heads/main", ci)
        # calls the one source-of-truth script, never a reimplementation
        self.assertIn("scripts/sync-mirrors.sh", ci)

    def test_ci_arm_is_key_gated_and_skips_gracefully(self):
        ci = read(".github/workflows/gates.yml")
        # auth is a per-mirror SSH deploy key held as a secret
        self.assertIn("MIRROR_SYNC_DEPLOY_KEY", ci)
        # a missing key is a clean skip, never a red CI (honest-failure by name, SPEC INV-112)
        self.assertIn("skipping mirror sync", ci)
        # CI reaches the mirror over SSH (the deploy key), the script's MIRROR_SSH path
        self.assertIn("MIRROR_SSH=1", ci)


if __name__ == "__main__":
    unittest.main()

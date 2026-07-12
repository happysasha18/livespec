"""The convergence locks hold by test, never by attention (row 217, M-214..216).

Three locks the audit found attention-held, now each held by a test:
frozen norms are content-fingerprinted; the register lint's pattern set only
grows; the debt cap only ratchets downward. Changing any guarded value is
LEGAL only as a deliberate, visible edit to its manifest/floor — in the same
commit, named in the landing.
"""
import hashlib
import importlib.util
import json
import os
import unittest

from conftest import ROOT
NORMS_DIR = os.path.join(ROOT, "docs", "norms")
NORMS_MANIFEST = os.path.join(ROOT, "scripts", "norms-manifest.json")
LINT = os.path.join(ROOT, "scripts", "preshow-register-lint.py")
LINT_FLOOR = os.path.join(ROOT, "scripts", "register-lint-floor.json")
DEBT_CAP = os.path.join(ROOT, "scripts", "spec-debt-cap.json")


class TestConvergenceLocks(unittest.TestCase):

    def test_norm_fingerprints(self):
        """M-214: every frozen norm's content matches its recorded fingerprint,
        and every norm file is fingerprinted — a norm never drifts silently."""
        manifest = json.load(open(NORMS_MANIFEST))["sha256"]
        on_disk = sorted(f for f in os.listdir(NORMS_DIR) if not f.startswith("."))
        self.assertEqual(sorted(manifest), on_disk,
                         "docs/norms/ and the manifest disagree on the norm set")
        for name, recorded in manifest.items():
            actual = hashlib.sha256(
                open(os.path.join(NORMS_DIR, name), "rb").read()).hexdigest()
            self.assertEqual(actual, recorded,
                             "a frozen norm drifted from its fingerprint: %s "
                             "(a deliberate change updates the manifest in the "
                             "same commit and names why)" % name)

    def test_register_lint_pattern_floor(self):
        """M-215: the register lint's pattern set only grows — one per caught
        leak; the floor file pins the reached count."""
        floor = json.load(open(LINT_FLOOR))["min_patterns"]
        spec = importlib.util.spec_from_file_location("preshow_lint", LINT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        count = len(mod.PATTERNS)
        self.assertGreaterEqual(
            count, floor,
            "the register lint's pattern set SHRANK below its reached floor "
            "(%d < %d) — patterns are never removed, the set only grows" % (count, floor))
        self.assertGreaterEqual(floor, 17, "the floor itself was lowered — illegal")

    def test_debt_cap_only_downward(self):
        """M-216: the prose-debt caps ratchet downward only. The reached values
        are pinned HERE; raising a cap means editing this test — a deliberate,
        visible act, never a quiet json touch."""
        cap = json.load(open(DEBT_CAP))
        self.assertLessEqual(cap["max_waivers"], 0,
                             "max_waivers was raised above the reached ratchet value")
        self.assertLessEqual(cap["max_redundancy_open"], 0,
                             "max_redundancy_open was raised above the reached ratchet value")


if __name__ == "__main__":
    unittest.main()

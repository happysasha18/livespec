"""The bytes-per-criterion ratchet gate (SPEC INV-264, INV-265).

`guardrails/check-size-ratchet.py` computes a document's bytes-per-criterion and compares it to the
recorded bound in `guardrails/spec-ratchet.json`. The shipped config is UNSEEDED (bound null) — the
gate passes with its stated reason until the migration-end freeze seeds it (INV-264 criterion 3). A
seeded bound the document exceeds reds; a bound at or above it passes. UNARMED (INV-270).
"""
import json
import os
import subprocess
import tempfile
import unittest

from conftest import ROOT

GATE = os.path.join(ROOT, "guardrails", "check-size-ratchet.py")
FX = os.path.join(ROOT, "tests", "fixtures", "specformat")
MINI = os.path.join(FX, "mini_good.md")
REAL_CONFIG = os.path.join(ROOT, "guardrails", "spec-ratchet.json")


def run(doc, config=None):
    env = dict(os.environ)
    if config is not None:
        env["RATCHET_CONFIG"] = config
    return subprocess.run(["python3", GATE, doc], capture_output=True, text=True, env=env)


class TestSizeRatchetGate(unittest.TestCase):
    def test_gate_and_config_ship(self):
        self.assertTrue(os.path.isfile(GATE))
        self.assertTrue(os.path.isfile(REAL_CONFIG), "the ratchet config does not ship")

    def test_shipped_config_is_unseeded(self):
        cfg = json.load(open(REAL_CONFIG, encoding="utf-8"))
        self.assertIsNone(cfg.get("bytes_per_criterion"),
                          "the shipped ratchet bound is seeded — it must stay null until the "
                          "migration-end freeze records it (INV-264 c3)")
        self.assertTrue(cfg.get("reason", "").strip(), "the unseeded config states no reason")

    def test_unseeded_bound_passes_with_a_stated_reason(self):
        r = run(MINI, REAL_CONFIG)
        self.assertEqual(r.returncode, 0, "the gate red on an unseeded bound:\n%s" % r.stdout)
        self.assertIn("not yet seeded", r.stdout)
        self.assertIn("bytes/criterion", r.stdout)

    def test_bound_above_the_document_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "high.json")
            json.dump({"bytes_per_criterion": 10000, "governs": "x"}, open(cfg, "w"))
            r = run(MINI, cfg)
            self.assertEqual(r.returncode, 0, "the gate red under a high bound:\n%s" % r.stdout)
            self.assertIn("reach:", r.stdout)

    def test_bound_below_the_document_reds(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "low.json")
            json.dump({"bytes_per_criterion": 20, "governs": "x"}, open(cfg, "w"))
            r = run(MINI, cfg)
            self.assertNotEqual(r.returncode, 0, "passed a document above the bound:\n%s" % r.stdout)
            self.assertIn("above the recorded bound", r.stdout)

    def test_gate_not_wired_into_pre_push_or_ci(self):
        with open(os.path.join(ROOT, "guardrails", "pre-push"), encoding="utf-8") as f:
            self.assertNotIn("check-size-ratchet", f.read())
        with open(os.path.join(ROOT, ".github", "workflows", "gates.yml"), encoding="utf-8") as f:
            self.assertNotIn("check-size-ratchet", f.read())


if __name__ == "__main__":
    unittest.main()

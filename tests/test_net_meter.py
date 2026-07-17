"""Every net keeps its own liveness numbers, and a silent net is read rather than trusted — row 391.

The law (SPEC INV-202): every net — a hook or a guard that watches for something — records its own two
numbers, how often it RAN and how often it FIRED. A net with ZERO runs reds by name as a broken trigger
(its condition sits where the work never passes). A net with many runs and ZERO fires over a declared
window surfaces as a RETIREMENT CANDIDATE whose retirement is the human's call, never auto-retired. Kin of
row 384 (a check that looked at nothing is not a pass) and INV-41 (the number names its watcher).

This is the pack-side arm of the personal layer's `~/.claude/hooks/hook-meter.py`. The shared shape is
`guardrails/net_meter.py`: a transparent wrapper that records one JSON line per net invocation, plus a
`--report` reader that aggregates runs/fires per net against a declared roster and gives the three readings
— broken (zero runs, reds by name), retirement candidate (silent over the declared window, surfaced for the
human's word), and live.

Red-proven: before `guardrails/net_meter.py` exists this module fails to load. Once it exists, the readings
and exit codes are proven against synthetic records and a real wrapped net.
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

from conftest import ROOT, read_flat


def _load_meter():
    path = os.path.join(ROOT, "guardrails", "net_meter.py")
    spec = importlib.util.spec_from_file_location("net_meter", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


NM = _load_meter()


class TestReadings(unittest.TestCase):
    """The three readings, derived from a net's two numbers against a declared window."""

    def test_zero_runs_reads_broken(self):
        reading, broken, candidate = NM.classify(runs=0, fires=0, window=20)
        self.assertTrue(broken, "a net that never ran is a broken trigger")
        self.assertFalse(candidate)
        self.assertIn("broken", reading.lower())

    def test_silent_over_window_is_a_retirement_candidate(self):
        reading, broken, candidate = NM.classify(runs=50, fires=0, window=20)
        self.assertFalse(broken, "a net that runs is not broken")
        self.assertTrue(candidate, "many runs, zero fires over the window is a retirement candidate")
        self.assertIn("retirement candidate", reading.lower())
        self.assertIn("human", reading.lower(), "the retirement is the human's call")

    def test_silent_below_window_is_not_yet_a_candidate(self):
        # the window is load-bearing: below it, silence is too little to read.
        reading, broken, candidate = NM.classify(runs=3, fires=0, window=20)
        self.assertFalse(broken)
        self.assertFalse(candidate, "below the declared window a silent net is not yet a candidate")

    def test_firing_net_reads_live(self):
        reading, broken, candidate = NM.classify(runs=50, fires=7, window=20)
        self.assertFalse(broken)
        self.assertFalse(candidate)
        self.assertEqual(reading, "live")


SYNTH_RECORDS = [
    {"net": "scissors-scan", "event": "Stop", "fired": True, "hits": 2},
    {"net": "scissors-scan", "event": "Stop", "fired": False, "hits": 0},
    # clock-hook ran many times and never fired — a retirement candidate over a small window.
    *[{"net": "clock-hook", "event": "Stop", "fired": False, "hits": 0} for _ in range(6)],
    # future-times-guard never appears in the log at all — a zero-run net, seen only via the roster.
]


class TestReport(unittest.TestCase):
    def test_report_reds_a_zero_run_net_by_name(self):
        roster = ["scissors-scan", "clock-hook", "future-times-guard"]
        result = NM.report(SYNTH_RECORDS, roster=roster, window=5)
        self.assertIn("future-times-guard", result.broken,
                      "a roster net with no runs reds as a broken trigger")
        # reds BY NAME: the net's name is in the printed lines.
        joined = "\n".join(result.lines)
        self.assertIn("future-times-guard", joined)
        self.assertNotEqual(result.exit_code, 0, "a zero-run net makes the check red")

    def test_report_surfaces_a_silent_net_without_reddening(self):
        roster = ["scissors-scan", "clock-hook"]
        result = NM.report(SYNTH_RECORDS, roster=roster, window=5)
        self.assertIn("clock-hook", result.retirement_candidates,
                      "a net silent over the declared window surfaces as a retirement candidate")
        self.assertEqual(result.exit_code, 0,
                         "a silent net is surfaced for the human's word, never an auto-red")
        self.assertNotIn("clock-hook", result.broken)

    def test_report_reads_a_firing_net_as_live(self):
        roster = ["scissors-scan"]
        result = NM.report(SYNTH_RECORDS, roster=roster, window=5)
        self.assertNotIn("scissors-scan", result.broken)
        self.assertNotIn("scissors-scan", result.retirement_candidates)
        self.assertEqual(result.exit_code, 0)


class TestWrapRecordsByDeed(unittest.TestCase):
    """The recording is proven by driving the real wrapper over a real net, not trusted from prose."""

    def _run_wrapped(self, net_body, log_path):
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, dir=os.path.dirname(log_path)) as nf:
            nf.write(net_body)
            net_path = nf.name
        env = dict(os.environ, NET_METER_LOG=log_path)
        proc = subprocess.run(
            [sys.executable, os.path.join(ROOT, "guardrails", "net_meter.py"),
             "--wrap", "watcher", sys.executable, net_path],
            input='{"hook_event_name": "Stop"}', capture_output=True, text=True, env=env,
        )
        os.unlink(net_path)
        return proc

    def test_a_firing_and_a_quiet_run_are_both_recorded(self):
        with tempfile.TemporaryDirectory() as d:
            log_path = os.path.join(d, "net-meter.jsonl")
            # a net that FIRES: it exits non-zero (a guard that caught something).
            self._run_wrapped("import sys; sys.exit(1)", log_path)
            # a net that stays QUIET: exits 0, says nothing.
            self._run_wrapped("import sys; sys.exit(0)", log_path)
            records = [json.loads(line) for line in open(log_path, encoding="utf-8")]
            self.assertEqual(len(records), 2, "one log line per invocation")
            self.assertEqual([r["net"] for r in records], ["watcher", "watcher"])
            self.assertEqual([r["fired"] for r in records], [True, False],
                             "the wrapper records which run fired and which stayed quiet")

    def test_the_wrapper_is_transparent_to_the_nets_exit_code(self):
        with tempfile.TemporaryDirectory() as d:
            log_path = os.path.join(d, "net-meter.jsonl")
            proc = self._run_wrapped("import sys; sys.exit(3)", log_path)
            self.assertEqual(proc.returncode, 3, "the wrapper exits with the net's own code")


class TestSpecAndIndex(unittest.TestCase):
    def test_spec_states_the_law(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("INV-202", spec)
        # the law names both numbers and all three readings.
        self.assertRegex(spec, r"runs?\b.*\bfires?\b|fires?\b.*\bruns?\b")
        self.assertIn("retirement candidate", spec)

    def test_formal_index_row(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertRegex(spec, r"\| INV-202 \|")

    def test_architecture_owns_the_invariant(self):
        arch = read_flat("ARCHITECTURE.md")
        self.assertIn("INV-202", arch)

    def test_matrix_row_covers_the_law(self):
        matrix = read_flat("TEST_MATRIX.md")
        self.assertIn("INV-202", matrix)


if __name__ == "__main__":
    unittest.main()

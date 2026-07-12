"""The cross-cut counter flags a node pair that crosses the threshold, for the MINOR audit — row 293.

The boundary-health law (SPEC INV-128) states the bar and the signal: a right node boundary keeps a
typical request in one node, and repeated cross-cutting landings on the same node pair are the signal that
a boundary sits in the wrong place. INV-128 deferred the mechanical half — the cross-cut counter — to a
follow-on row. This is it: a counter reads the closed queue's cross-cutting landings and counts, per
unordered node pair, how many cross-cutting changes touched both nodes; a pair reaching the threshold
within the window is FLAGGED for the MINOR audit as a boundary-move candidate (the mechanized form of
"seen twice, own it", base rule 19, applied to boundaries). The flag is an audit signal, never a per-push
red — a boundary moves only through the architecture step and its re-prove (SPEC INV-37).

Red-proven on a synthetic queue: a pair cross-cut at or above the threshold is flagged; a pair below it is
not; the threshold moves the line.
"""

import importlib.util
import os
import unittest

from conftest import ROOT, read_flat


def _load_counter():
    path = os.path.join(ROOT, "guardrails", "crosscut_counter.py")
    spec = importlib.util.spec_from_file_location("crosscut_counter", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CC = _load_counter()


# A synthetic closed queue: each entry is the set of nodes one cross-cutting landing touched.
SYNTH_QUEUE = [
    {"spec", "architecture"},
    {"spec", "architecture", "matrix"},
    {"spec", "architecture"},
    {"communicator", "spec"},
    {"build-pipeline", "guardrails"},
    {"build-pipeline", "guardrails"},
]


class TestCrossCutCounter(unittest.TestCase):
    def test_over_threshold_pair_is_flagged(self):
        flagged = dict((tuple(sorted(k)), v) for k, v in CC.count_pairs(SYNTH_QUEUE, threshold=3).items())
        self.assertIn(("architecture", "spec"), flagged,
                      "a pair cross-cut 3 times must be flagged at threshold 3")
        self.assertEqual(flagged[("architecture", "spec")], 3)

    def test_below_threshold_pair_is_not_flagged(self):
        flagged = dict((tuple(sorted(k)), v) for k, v in CC.count_pairs(SYNTH_QUEUE, threshold=3).items())
        # build-pipeline/guardrails cross-cut only twice — below threshold 3
        self.assertNotIn(("build-pipeline", "guardrails"), flagged)
        # spec/matrix co-occur once
        self.assertNotIn(("matrix", "spec"), flagged)

    def test_threshold_moves_the_line(self):
        at_two = dict((tuple(sorted(k)), v) for k, v in CC.count_pairs(SYNTH_QUEUE, threshold=2).items())
        self.assertIn(("build-pipeline", "guardrails"), at_two,
                      "at threshold 2 the twice-cut pair is flagged")
        self.assertIn(("architecture", "spec"), at_two)

    def test_flagged_pairs_sorted_highest_first(self):
        ranked = CC.flagged_pairs(SYNTH_QUEUE, threshold=2)
        counts = [c for _, c in ranked]
        self.assertEqual(counts, sorted(counts, reverse=True), "flagged pairs must rank highest count first")
        self.assertEqual(ranked[0], (("architecture", "spec"), 3))

    def test_empty_queue_flags_nothing(self):
        self.assertEqual(CC.count_pairs([], threshold=3), {})

    def test_roadmap_adapter_reads_crosscutting_rows(self):
        known = ["spec", "architecture", "matrix", "communicator"]
        text = (
            "| 1 | wish | small | **landed 2026-07-12; footprint: cross-cutting** touches spec and architecture | done |\n"
            "| 2 | wish | small | **landed 2026-07-12; footprint: single-module** spec only | done |\n"
            "| 3 | wish | small | **landed 2026-07-12; footprint: cross-cutting** spec, architecture, matrix | done |\n"
        )
        landings = CC.crosscut_landings_from_roadmap(text, known)
        self.assertEqual(len(landings), 2, "only the two cross-cutting rows contribute landings")
        flagged = CC.count_pairs(landings, threshold=2)
        self.assertIn(frozenset(("architecture", "spec")),
                      set(frozenset(k) for k in flagged),
                      "the pair named in both cross-cutting rows reaches threshold 2")


class TestCrossCutCounterLaw(unittest.TestCase):
    def test_architecture_states_bar_signal_and_counter(self):
        arch = read_flat("ARCHITECTURE.md")
        for needle in (
            "Boundary health",
            "a typical request lands in one node",
            "SPEC INV-128",
            "INV-37",
            "cross-cut counter",
        ):
            self.assertIn(needle, arch, "ARCHITECTURE boundary-health lost: %s" % needle)
        self.assertIn("guardrails/crosscut_counter.py", arch,
                      "ARCHITECTURE does not name the landed cross-cut counter check")

    def test_build_pipeline_minor_gate_runs_the_counter(self):
        bp = read_flat("skills/build-pipeline/SKILL.md")
        self.assertIn("cross-cut counter", bp,
                      "build-pipeline's MINOR gate does not run the cross-cut counter")


if __name__ == "__main__":
    unittest.main()

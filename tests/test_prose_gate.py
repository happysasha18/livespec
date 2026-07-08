"""Tests for the durable prose-quality DONE-GATE (docs/prose-quality-gate-design.md).

These lock the MECHANISM (promotion, exemptions, waivers, redundancy pre-check, LLM-judge protocol,
the unified gate). The SPEC-CONTENT tests (every needle lints clean; no anchor hides in a blockquote;
SPEC.md passes the whole gate) land after the whole-document rewrite, since the current SPEC still
carries the register warnings the rewrite removes.
"""
import datetime
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)
import gate_common  # noqa: E402


def run(script, *args, stdin=None):
    return subprocess.run(["python3", os.path.join(SCRIPTS, script), *args],
                          input=stdin, capture_output=True, text=True)


class TestSpecStyleLintGate(unittest.TestCase):
    def test_default_keeps_soft_signals_advisory(self):
        r = run("spec-style-lint.py", "-", stdin="You open it and it CHANGES the queue.\n")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("second-person", r.stdout)
        self.assertIn("caps-shout", r.stdout)

    def test_gate_promotes_soft_signals_to_errors(self):
        r = run("spec-style-lint.py", "--gate", "-", stdin="You open it and it CHANGES the queue.\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("second-person", r.stdout)
        self.assertIn("caps-shout", r.stdout)

    def test_gate_exempts_user_story_and_blockquote(self):
        for text in ("**User story:** as the owner, you report a bug and you see it fixed.\n",
                     "> You can read this informative note however you like.\n"):
            r = run("spec-style-lint.py", "--gate", "-", stdin=text)
            self.assertEqual(r.returncode, 0, "exempt region must pass gate: %r\n%s" % (text, r.stdout))

    def test_gate_scissors_is_global_even_in_blockquote(self):
        r = run("spec-style-lint.py", "--gate", "-", stdin="> the card shows the outcome — not the mechanism.\n")
        self.assertEqual(r.returncode, 1, "scissors is global, no exemption\n%s" % r.stdout)
        self.assertIn("scissors", r.stdout)

    def test_gate_new_rules_fire(self):
        r = run("spec-style-lint.py", "--gate", "-",
                stdin="Simply open it.\nThe card will show the queue.\n")
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("reassurance", r.stdout)
        self.assertIn("future-narration", r.stdout)


class TestWaiverMechanism(unittest.TestCase):
    def _w(self, **kw):
        base = {"id": "w1", "rule": "second-person", "file": "SPEC.md", "snippet": "you know",
                "reason": "r", "owner": "a", "date": "2026-07-08", "expiry": "2026-07-30"}
        base.update(kw)
        return base

    def test_active_waiver_matches_by_snippet(self):
        w = self._w()
        m = gate_common.match_waiver("second-person", "SPEC.md", "past what you know to ask",
                                     [w], today=datetime.date(2026, 7, 10))
        self.assertIsNotNone(m)

    def test_expired_waiver_does_not_match(self):
        w = self._w(expiry="2026-07-09")
        m = gate_common.match_waiver("second-person", "SPEC.md", "past what you know to ask",
                                     [w], today=datetime.date(2026, 7, 20))
        self.assertIsNone(m, "an expired waiver must not suppress — it reverts to a hard error")

    def test_wrong_rule_or_file_does_not_match(self):
        w = self._w()
        self.assertIsNone(gate_common.match_waiver("caps-shout", "SPEC.md", "you know", [w]))
        self.assertIsNone(gate_common.match_waiver("second-person", "OTHER.md", "you know", [w]))

    def test_live_waiver_file_schema_and_bounded_expiry(self):
        path = os.path.join(SCRIPTS, "spec-waivers.json")
        waivers = gate_common.load_waivers(path)
        for w in waivers:
            for field in gate_common.WAIVER_FIELDS:
                self.assertTrue(w.get(field), "waiver %s missing %s" % (w.get("id"), field))
            d = datetime.date.fromisoformat(w["date"])
            e = datetime.date.fromisoformat(w["expiry"])
            self.assertLessEqual((e - d).days, gate_common.MAX_WAIVER_DAYS,
                                 "waiver %s expiry exceeds %d days" % (w["id"], gate_common.MAX_WAIVER_DAYS))


class TestDebtRatchet(unittest.TestCase):
    def test_waivers_within_cap(self):
        cap = json.load(open(os.path.join(SCRIPTS, "spec-debt-cap.json")))
        waivers = gate_common.load_waivers(os.path.join(SCRIPTS, "spec-waivers.json"))
        self.assertLessEqual(len(waivers), cap["max_waivers"],
                             "waiver count exceeds the committed ratchet cap")


class TestRedundancyPrecheck(unittest.TestCase):
    def test_seeded_duplicate_fires(self):
        text = ("The classifier assigns each wish exactly one door at intake.\n\n"
                "At intake the classifier assigns every wish exactly one door.\n")
        r = run("spec-redundancy-precheck.py", "-", stdin=text)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("REDUNDANCY", r.stdout)

    def test_distinct_sentences_pass(self):
        text = "The classifier doors a wish.\n\nThe prover reads committed law only.\n"
        r = run("spec-redundancy-precheck.py", "-", stdin=text)
        self.assertEqual(r.returncode, 0, r.stdout)


class TestJudgeProtocol(unittest.TestCase):
    def test_rubric_hash_is_pinned(self):
        sys.path.insert(0, SCRIPTS)
        import importlib.util
        spec = importlib.util.spec_from_file_location("specjudge", os.path.join(SCRIPTS, "spec-judge.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertEqual(mod.PINNED_RUBRIC_SHA256, mod.rubric_sha256(),
                         "judge-rubric.md changed without re-pinning its sha256 in spec-judge.py")

    def test_malformed_output_is_invalid(self):
        with tmpfile("not json") as jf, tmpfile("doc\n") as doc:
            r = run("spec-judge.py", "--verify", doc, jf)
            self.assertEqual(r.returncode, 2, r.stdout)

    def test_selftest_miss_is_invalid(self):
        out = json.dumps({"findings": [
            {"criterion": "C2", "severity": "definite", "quote": "You can skip the rest of this section."}]})
        with tmpfile(out) as jf, tmpfile("doc\n") as doc:
            r = run("spec-judge.py", "--verify", doc, jf)
            self.assertEqual(r.returncode, 2, "missing a seed must be INVALID\n%s" % r.stdout)

    def test_hallucinated_quote_discarded_and_real_survives(self):
        out = json.dumps({"findings": [
            {"criterion": "C1", "severity": "definite", "quote": "At the door, the gate refuses a defect."},
            {"criterion": "C2", "severity": "definite", "quote": "You can skip the rest of this section."},
            {"criterion": "C3", "severity": "definite", "quote": "Simply ignore the footnotes for now."},
            {"criterion": "C2", "severity": "definite", "quote": "You may leave whenever you wish."},
            {"criterion": "C1b", "severity": "likely", "quote": "a span absent from the document"}]})
        with tmpfile(out) as jf, tmpfile("You may leave whenever you wish.\n") as doc:
            r = run("spec-judge.py", "--verify", doc, jf)
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn('"surviving":1', r.stdout)
            self.assertIn('"discarded":1', r.stdout)


class TestDoneGate(unittest.TestCase):
    def test_missing_judge_is_red(self):
        with tmpfile("The gate blocks a defect at the door.\n") as doc:
            r = run("spec-done-gate.py", doc)
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("DONE-GATE: RED", r.stdout)

    def test_all_conditions_green(self):
        out = json.dumps({"findings": [
            {"criterion": "C1", "severity": "definite", "quote": "At the door, the gate refuses a defect.",
             "duplicate_of": "The gate refuses a defect at the door."},
            {"criterion": "C2", "severity": "definite", "quote": "You can skip the rest of this section."},
            {"criterion": "C3", "severity": "definite", "quote": "Simply ignore the footnotes for now."}]})
        with tmpfile("The gate blocks a defect at the door.\n") as doc, tmpfile(out) as jf:
            r = run("spec-done-gate.py", "--judge", jf, doc)
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertIn("DONE-GATE: GREEN", r.stdout)


import contextlib
import tempfile


@contextlib.contextmanager
def tmpfile(content):
    fd, path = tempfile.mkstemp(suffix=".md")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        yield path
    finally:
        os.unlink(path)


if __name__ == "__main__":
    unittest.main()

"""Tests for the style lint's two explicit tiers (INV-166, docs/spec-style.md "Two tiers").

The UNIVERSAL tier (negation-opener, scissors, machine-jargon) is the plainness every live-spec
document holds whatever its register — it binds every host's gate. The PACK-REGISTER tier
(caps-shout, second-person, reassurance, future-narration) is the pack's own reference-documentation
taste, a host adopts on its own word. `--tier universal` runs the universal tier as the gate and
leaves the register tier advisory; `--tier full` runs the union (identical to `--gate`, which stays
as its alias — tests/test_convergence_locks.py calls `--gate` and must keep working unchanged).

Red-first: before the `--tier` flag existed, every `--tier ...` invocation below fell through the
old naive argv filter (`[a for a in argv[1:] if not a.startswith("--")]`), which drops the literal
`--tier` token but keeps its value (`universal`/`full`/`bogus`) as a second positional argument
alongside the file — so the old script rejected all of them as a usage error (exit 2, "usage: ...")
rather than running the intended tier. Verified by running this scenario against a saved copy of the
pre-edit script.
"""
import os
import subprocess
import unittest

from conftest import ROOT
SCRIPTS = os.path.join(ROOT, "scripts")
LINT = os.path.join(SCRIPTS, "spec-style-lint.py")


def run(*args, stdin=None):
    return subprocess.run(["python3", LINT, *args], input=stdin, capture_output=True, text=True)


SCISSORS_TEXT = "the card shows the outcome — not the mechanism.\n"
CAPS_ONLY_TEXT = "It CHANGES the queue.\n"
SECOND_PERSON_TEXT = "You open it and read the result.\n"


class TestScissorsBindsEveryTier(unittest.TestCase):
    """The universal law binds everywhere: a scissors phrase is an error in every mode."""

    def test_scissors_reds_in_default(self):
        r = run("-", stdin=SCISSORS_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("scissors", r.stdout)

    def test_scissors_reds_under_tier_universal(self):
        r = run("--tier", "universal", "-", stdin=SCISSORS_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("scissors", r.stdout)

    def test_scissors_reds_under_tier_full(self):
        r = run("--tier", "full", "-", stdin=SCISSORS_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("scissors", r.stdout)

    def test_scissors_reds_under_gate(self):
        r = run("--gate", "-", stdin=SCISSORS_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("scissors", r.stdout)


class TestCapsShoutIsPackRegister(unittest.TestCase):
    """caps-shout is pack-register taste: advisory at the universal floor, a blocking error once a
    host adopts the pack's own register (full/gate)."""

    def test_universal_leaves_caps_advisory(self):
        r = run("--tier", "universal", "-", stdin=CAPS_ONLY_TEXT)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn('"errors":0', r.stdout)
        self.assertIn("caps-shout", r.stdout)  # still visible, as a warning

    def test_full_promotes_caps_to_error(self):
        r = run("--tier", "full", "-", stdin=CAPS_ONLY_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("caps-shout", r.stdout)

    def test_gate_promotes_caps_to_error(self):
        r = run("--gate", "-", stdin=CAPS_ONLY_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("caps-shout", r.stdout)


class TestSecondPersonIsPackRegister(unittest.TestCase):
    """second-person is pack-register taste, same split as caps-shout."""

    def test_universal_leaves_second_person_advisory(self):
        r = run("--tier", "universal", "-", stdin=SECOND_PERSON_TEXT)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn('"errors":0', r.stdout)

    def test_full_promotes_second_person_to_error(self):
        r = run("--tier", "full", "-", stdin=SECOND_PERSON_TEXT)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("second-person", r.stdout)


class TestGateIsAnAliasForTierFull(unittest.TestCase):
    """--gate and --tier full are the same tier — identical error counts on a mixed sample carrying
    a universal tell, a pack-register tell, and a gate-only tell together."""

    MIXED = ("You open it — not the raw feed. It simply CHANGES the queue.\n"
              "The card will show the outcome.\n")

    def test_gate_and_tier_full_agree(self):
        gate_r = run("--gate", "-", stdin=self.MIXED)
        full_r = run("--tier", "full", "-", stdin=self.MIXED)
        self.assertEqual(gate_r.returncode, full_r.returncode)
        self.assertEqual(gate_r.stdout, full_r.stdout)


class TestUnknownTierRejected(unittest.TestCase):
    def test_bogus_tier_exits_nonzero_with_message(self):
        r = run("--tier", "bogus", "-", stdin="hi\n")
        self.assertNotEqual(r.returncode, 0, r.stdout)
        self.assertIn("bogus", r.stderr)


if __name__ == "__main__":
    unittest.main()

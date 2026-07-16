"""The suite wall-time budget's mechanical net (SPEC INV-41, INV-164, ROADMAP row 361).

guardrails/check-suite-budget.sh reads a captured pytest run's own tail duration line against
the budget row ARCHITECTURE.md states for "full suite wall-time", and reds past the budget
naming both the measured and the budgeted figure — the fix for a budget claim (once <= 60 s)
drifting silently behind the real measured number (~95 s) with nothing machine-reading it.

These tests write a SYNTHETIC log to a temp file (never the real suite's own log — these are
red/green fixtures), cleaned up by tempfile.TemporaryDirectory's own teardown (SPEC INV-100)."""
import os
import re
import subprocess
import tempfile

from conftest import ROOT, read

GUARD = os.path.join(ROOT, "guardrails", "check-suite-budget.sh")


def _budget_from_architecture():
    """The figure the guardrail itself must read, parsed independently here so a drift between
    the script's own parser and the architecture's row is caught by this test, not assumed."""
    arch = read("ARCHITECTURE.md")
    for line in arch.splitlines():
        if line.strip().startswith("| full suite wall-time |"):
            m = re.search(r"≤\s*(\d+)", line)
            assert m, "full suite wall-time row has no readable '≤ <int>' figure: %r" % line
            return m.group(1)
    raise AssertionError("ARCHITECTURE.md has no 'full suite wall-time' budget row")


def _write_log(tmp, body):
    path = os.path.join(tmp, "suite.log")
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    return path


def _run(log_path):
    return subprocess.run(["bash", GUARD, log_path], capture_output=True, text=True)


def test_guardrail_ships():
    assert os.path.isfile(GUARD), "guardrails/check-suite-budget.sh missing"


def test_slow_log_reds_naming_both_numbers():
    budget = _budget_from_architecture()
    with tempfile.TemporaryDirectory() as tmp:
        log = _write_log(tmp, "941 passed in 9999.00s (2:46:39)\n")
        r = _run(log)
        out = r.stdout + r.stderr
        assert r.returncode == 1, out
        assert "9999" in out, out
        assert budget in out, out


def test_fast_log_passes():
    budget = _budget_from_architecture()
    with tempfile.TemporaryDirectory() as tmp:
        log = _write_log(tmp, "941 passed in 1.00s\n")
        r = _run(log)
        out = r.stdout + r.stderr
        assert r.returncode == 0, out
        assert "1.00" in out, out
        assert budget in out, out


def test_unreadable_log_reds():
    with tempfile.TemporaryDirectory() as tmp:
        log = _write_log(tmp, "no duration line here, just noise\n")
        r = _run(log)
        out = (r.stdout + r.stderr).lower()
        assert r.returncode == 1, out
        assert "unreadable" in out, out

#!/usr/bin/env python3
"""spec-done-gate.py — the single definition of "done" for spec prose (docs/prose-quality-gate-design.md).

"0 lint errors" was being mistaken for "done" while the done-set was smaller than the set of known defect
classes. This runs the conjunction that actually means done for a gated file, and prints GREEN only when
ALL hold. It is the one fixed target a "humanize" pass and a "restyle" pass must both satisfy — which ends
the oscillation, because a warm/second-person pass can no longer pass.

Conditions (this script runs the prose-quality conjunction; "suite green" + needle tests + waiver-hygiene +
debt-ratchet are enforced by the pytest classes in tests/, run separately):
  1. spec-style-lint.py --gate → 0 errors (waived allowed).
  2. spec-redundancy-precheck.py → open == 0 (resolved or waived).
  3. LLM judge → self-test passed AND 0 surviving definite/likely findings (requires --judge OUTPUT.json;
     without it the gate is RED with "judge pending", never silently green).
  4. anchor multiset unchanged vs --baseline (a git ref) when given.

Usage: spec-done-gate.py [--baseline GITREF] [--judge JUDGEOUT.json] FILE...
Exit 0 = GREEN · exit 1 = RED.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ANCHOR_RE = re.compile(r"\[([A-Za-z][\w.-]*(?:\s*,\s*[A-Za-z][\w.-]*)*)\]")


def _summary(stdout):
    """Parse the trailing JSON summary line a gate script prints."""
    for ln in reversed(stdout.strip().splitlines()):
        ln = ln.strip()
        if ln.startswith("{") and ln.endswith("}"):
            try:
                return json.loads(ln)
            except ValueError:
                pass
    return {}


def _run(script, *args):
    r = subprocess.run(["python3", os.path.join(HERE, script), *args],
                       capture_output=True, text=True)
    return r, _summary(r.stdout)


def anchor_multiset(text):
    from collections import Counter
    c = Counter()
    for m in ANCHOR_RE.finditer(text):
        for tok in m.group(1).split(","):
            c[tok.strip()] += 1
    return c


def check_file(path, baseline=None, judge=None):
    conds = []

    _, s = _run("spec-style-lint.py", "--gate", path)
    conds.append(("style-lint --gate errors==0", s.get("errors", 1) == 0, s))

    _, s = _run("spec-redundancy-precheck.py", path)
    conds.append(("redundancy open==0", s.get("open", 1) == 0, s))

    if judge:
        r, s = _run("spec-judge.py", "--verify", path, judge)
        ok = (r.returncode == 0 and s.get("selftest") == "passed" and s.get("surviving", 1) == 0)
        conds.append(("judge selftest+0 surviving", ok, s))
    else:
        conds.append(("judge (needs --judge OUTPUT.json)", False, {"note": "pending"}))

    if baseline:
        cur = open(path, encoding="utf-8").read()
        try:
            base = subprocess.run(["git", "show", "%s:%s" % (baseline, os.path.basename(path))],
                                  cwd=HERE, capture_output=True, text=True).stdout
            same = anchor_multiset(cur) == anchor_multiset(base)
        except Exception:
            same = False
        conds.append(("anchor multiset == %s" % baseline, same, {}))
    return conds


def main(argv):
    baseline = judge = None
    files = []
    it = iter(argv[1:])
    for a in it:
        if a == "--baseline":
            baseline = next(it)
        elif a == "--judge":
            judge = next(it)
        elif not a.startswith("--"):
            files.append(a)
    if not files:
        sys.stderr.write("usage: spec-done-gate.py [--baseline GITREF] [--judge JUDGEOUT] FILE...\n")
        return 2

    all_green = True
    for path in files:
        print("== DONE-GATE: %s ==" % path)
        for name, ok, s in check_file(path, baseline, judge):
            print("  [%s] %s%s" % ("GREEN" if ok else "RED", name,
                                   "" if ok else "  → %s" % json.dumps(s)))
            all_green = all_green and ok
    print("DONE-GATE: GREEN" if all_green else "DONE-GATE: RED")
    return 0 if all_green else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

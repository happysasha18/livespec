#!/usr/bin/env python3
"""spec-judge.py — protocol harness for the LLM-as-judge redundancy + register pass.

This script is NOT the judge. The judgment is a FRESH spawned agent (Opus at max reasoning, pack NOT
loaded), given the whole document in one context so it sees cross-section duplication. This harness only
(a) emits the exact prompt the agent must judge, and (b) verifies the agent's returned JSON mechanically,
so the LLM is never trusted as a black box.

Reliability discipline (LLM judges are internally consistent yet often invalid — high reproducibility
coexists with severe bias; no judge is uniformly reliable):
  - The rubric is LOCKED: its sha256 is pinned here and checked before every emit; a changed rubric aborts.
  - Every finding must carry a VERBATIM quote; --verify discards any finding whose quote is not found in the
    real document (a hallucinated finding cannot block or hide).
  - A SELF-TEST canary is appended to the emitted prompt: three planted defects the agent does not know are
    seeds. --verify fails the run as INVALID (not green) unless all three are caught — a green is trusted
    only on a run where the judge demonstrably fired.

Usage:
  spec-judge.py --emit-prompt DOCFILE            # → stdout: rubric + line-numbered doc + seeded self-test
  spec-judge.py --verify DOCFILE JUDGE_OUTPUT.json   # exit 0 = green, 1 = findings, 2 = invalid/self-test fail
"""
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RUBRIC_PATH = os.path.join(HERE, "judge-rubric.md")
WAIVER_PATH = os.path.join(HERE, "spec-waivers.json")

# sha256 of judge-rubric.md — the rubric cannot drift silently; edit both in a reviewed commit.
PINNED_RUBRIC_SHA256 = "2405f1fae918f4ea72cd23371e2794714a27f70d3cee79d3745b4513a646e9f4"

SELFTEST_BEGIN = "<!-- JUDGE-SELFTEST-BEGIN -->"
SELFTEST_END = "<!-- JUDGE-SELFTEST-END -->"

# Three planted defects. The agent judges them blind; --verify confirms each was caught before trusting
# any green. Each seed is "covered" when any of its texts appears (verbatim, whitespace-normalized) among
# the findings' quote/duplicate_of spans.
SEEDS = [
    {"id": "seed-redundancy", "criterion": "C1",
     "texts": ["The gate refuses a defect at the door.",
               "At the door, the gate refuses a defect."]},
    {"id": "seed-reader-address", "criterion": "C2",
     "texts": ["You can skip the rest of this section."]},
    {"id": "seed-reassurance", "criterion": "C3",
     "texts": ["Simply ignore the footnotes for now."]},
]


def _norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def rubric_sha256():
    with open(RUBRIC_PATH, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _assert_rubric():
    got = rubric_sha256()
    if PINNED_RUBRIC_SHA256 != "__PINNED__" and got != PINNED_RUBRIC_SHA256:
        sys.stderr.write("spec-judge: rubric hash mismatch — judge-rubric.md changed without re-pinning.\n"
                         "  expected %s\n  got      %s\n" % (PINNED_RUBRIC_SHA256, got))
        sys.exit(3)


def emit_prompt(docfile):
    _assert_rubric()
    rubric = open(RUBRIC_PATH, encoding="utf-8").read()
    doc = open(docfile, encoding="utf-8").read()
    numbered = "\n".join("L%d: %s" % (i, ln) for i, ln in enumerate(doc.splitlines(), 1))
    seed_block = "\n\n".join(t for s in SEEDS for t in s["texts"])
    out = []
    out.append(rubric.rstrip())
    out.append("\n\n## DOCUMENT (line-numbered for reference; quote the text WITHOUT the `Lnn:` prefix)\n")
    out.append(numbered)
    out.append("\n\n" + SELFTEST_BEGIN)
    out.append("The following short paragraph is part of the document under audit; judge it too.\n")
    out.append(seed_block)
    out.append(SELFTEST_END + "\n")
    return "\n".join(out)


def verify(docfile, judgefile):
    doc_norm = _norm(open(docfile, encoding="utf-8").read())
    try:
        data = json.load(open(judgefile, encoding="utf-8"))
        findings = data["findings"]
        assert isinstance(findings, list)
    except Exception as e:                                   # malformed / absent → fail closed (RED)
        print("spec-judge: INVALID — judge output is not valid {findings:[...]} JSON (%s)" % e)
        return 2

    # collect all quoted spans (normalized) across findings
    quoted = set()
    for f in findings:
        for key in ("quote", "duplicate_of"):
            if f.get(key):
                quoted.add(_norm(f[key]))

    # self-test: every seed must be covered by some quoted span
    missed = []
    for s in SEEDS:
        if not any(any(_norm(t) in q or q in _norm(t) for q in quoted) for t in s["texts"]):
            missed.append(s["id"])
    if missed:
        print("spec-judge: INVALID — self-test canary missed %s; judge untrustworthy this run." % missed)
        return 2

    seed_norms = [_norm(t) for s in SEEDS for t in s["texts"]]
    waivers = gate_common.load_waivers(WAIVER_PATH)

    real, hallucinated, waived = [], [], []
    for f in findings:
        q = _norm(f.get("quote", ""))
        if not q:
            continue
        if any(q in sn or sn in q for sn in seed_norms):
            continue                                          # a seed finding — used for self-test only
        if q not in doc_norm:
            hallucinated.append(f)                            # quote not in the real doc — discard
            continue
        sev = (f.get("severity") or "").lower()
        if sev not in ("definite", "likely"):
            continue                                          # nits are advisory
        w = gate_common.match_waiver("spec-judge", docfile, f.get("quote", ""), waivers)
        (waived if w else real).append(f)

    for f in real:
        print("JUDGE [%s %s] L%s: %s  (%s)"
              % (f.get("criterion"), f.get("severity"), f.get("line_hint"),
                 f.get("quote", "")[:100], f.get("why", "")))
    if hallucinated:
        print("spec-judge: discarded %d finding(s) with a quote not present in the document." % len(hallucinated))
    if waived:
        print("spec-judge: WAIVED (dated debt): %d finding(s)." % len(waived))
    print('{"code":"spec-judge","selftest":"passed","surviving":%d,"waived":%d,"discarded":%d}'
          % (len(real), len(waived), len(hallucinated)))
    return 1 if real else 0


def main(argv):
    if len(argv) >= 3 and argv[1] == "--emit-prompt":
        sys.stdout.write(emit_prompt(argv[2]))
        return 0
    if len(argv) >= 4 and argv[1] == "--verify":
        return verify(argv[2], argv[3])
    sys.stderr.write("usage: spec-judge.py --emit-prompt DOCFILE | --verify DOCFILE JUDGE_OUTPUT.json\n")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))

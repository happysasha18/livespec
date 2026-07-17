#!/usr/bin/env python3
"""Judge the outgoing text against the register laws that name a CLASS.

ROADMAP row 416. The literal overlay beside this file (scissors-personal.json) covers the
phrases someone thought of; the laws it serves name classes — an intensifier carrying no
information, a thing named by denying its neighbour, a sentence grading the reader's remark.
A list cannot cover a class, so each escape earns one more pattern while the next word walks
through. Probed 2026-07-17: four empty intensifiers passed the 22-pattern list untouched.

So this asks a model instead. It hands the text and the law to the cheapest tier and takes back
the offending sentences. The literal list stays as the free first pass for what it does cover.

Contract: reads a hook payload on stdin, writes a Stop-hook JSON decision on stdout, exits 0.
It NEVER blocks on its own failure — a judge that cannot reach a model, or answers slowly, or
answers in a shape this script cannot read, stands down and says so in its record. A guard that
reds when its own machinery breaks trains the guarded to route around it.

Repo home: hooks/register-judge.py; installed copy: ~/.claude/hooks/.
"""
import json
import os
import subprocess
import sys

MODEL = os.environ.get("REGISTER_JUDGE_MODEL", "claude-haiku-4-5-20251001")
TIMEOUT_S = float(os.environ.get("REGISTER_JUDGE_TIMEOUT", "25"))
MIN_CHARS = 120

LAW = """You are a register judge for one person's working chat. Judge the TEXT below against three
laws. Each law names a CLASS, so judge by meaning rather than by matching words.

LAW 1 — no empty intensifier. A word or phrase that inflates a statement while adding no
information is banned. It reads as performing conviction in place of carrying a fact. Examples of
the class, in any language: "really", "actually", "truly", "in fact", "genuinely", "this changes
everything", "at its core", any adjective grading how important a result is. A word that carries a
FACT stays: "three lanes" is a fact, "really important" is not.

LAW 2 — no naming a thing by denying its neighbour. The frame "X, not Y" / "X — not Y" / «X, а не Y»
is banned when the denied half adds nothing the reader did not already have. A contrast between two
things that BOTH genuinely exist and are both live for the reader is legitimate and passes.

LAW 3 — no grading the person. A sentence whose content is a verdict on the reader's remark rather
than an answer to it is banned: "good question", "you caught that exactly", "you're right" as an
opener, "fair point". Confirming a FACT the reader asserted passes, because that is information.

Return STRICT JSON, nothing else, no prose, no code fence:
{"offences": [{"quote": "<the offending sentence, verbatim from the text, at most 100 chars>",
"law": 1|2|3, "why": "<at most 12 words: what it adds nothing to>"}]}

An empty list is the right answer for a clean text, and it is the answer most texts deserve.
Judge only what the text says to the person. Ignore file paths, code, command output, and any
text the author is QUOTING rather than asserting.

TEXT:
"""


def last_assistant_text(path):
    """The final assistant message of the transcript, as plain text."""
    if not path or not os.path.exists(path):
        return ""
    try:
        with open(path) as fh:
            lines = fh.read().splitlines()
    except OSError:
        return ""
    for line in reversed(lines):
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("type") != "assistant" or rec.get("isSidechain"):
            continue
        blocks = rec.get("message", {}).get("content", [])
        text = "".join(
            b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text"
        )
        if text.strip():
            return text
    return ""


def judge(text):
    """Ask the model. Returns (offences, error) — error set means the judge stood down."""
    try:
        proc = subprocess.run(
            # No --bare: it strips the environment the launch needs and the run reports itself
            # as logged out (probed 2026-07-17). --tools "" keeps the judge from acting.
            ["claude", "-p", "--model", MODEL, "--tools", ""],
            input=LAW + text,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_S,
        )
    except FileNotFoundError:
        return [], "no claude binary on PATH"
    except subprocess.TimeoutExpired:
        return [], "judge timed out at %gs" % TIMEOUT_S
    if proc.returncode != 0:
        return [], "judge exited %d: %s" % (proc.returncode, proc.stderr.strip()[:120])
    out = proc.stdout.strip()
    if out.startswith("```"):
        out = out.strip("`").split("\n", 1)[-1].rsplit("```", 1)[0]
    try:
        parsed = json.loads(out)
    except ValueError:
        return [], "judge answered in no readable shape: %s" % out[:120]
    offences = parsed.get("offences")
    if not isinstance(offences, list):
        return [], "judge answered without an offences list"
    # Only an offence quoting the text itself is real; a hallucinated quote is no evidence.
    return [o for o in offences if isinstance(o, dict) and o.get("quote", "@@") in text], None


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        sys.exit(0)
    if payload.get("stop_hook_active"):  # never loop
        sys.exit(0)
    text = last_assistant_text(payload.get("transcript_path", ""))
    if len(text.strip()) < MIN_CHARS:
        sys.exit(0)
    offences, error = judge(text)
    if error:
        # Stand down loudly enough that a silent net is read rather than trusted [row 391].
        sys.stderr.write("register-judge stood down: %s\n" % error)
        sys.exit(0)
    if not offences:
        sys.exit(0)
    lines = "\n".join(
        "  · %s\n      [law %s] %s" % (o["quote"], o.get("law", "?"), o.get("why", ""))
        for o in offences[:5]
    )
    reason = (
        "REGISTER JUDGE — the reply carries text that adds no information:\n"
        + lines
        + "\n\nRestate each as a plain positive sentence carrying its fact, and send the correction "
        "now. If one of them genuinely informs, say which and why in one line and continue."
    )
    print(json.dumps({"decision": "block", "reason": reason, "suppressOutput": True}))
    sys.exit(0)


if __name__ == "__main__":
    main()

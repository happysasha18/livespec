#!/usr/bin/env python3
"""conduct-judge.py — the CONDUCT surface's judge: it reads what the seat DID (SPEC INV-241).

The register judge reads what the seat SAID — the turn's outgoing text — and holds a register class a
fixed word-list cannot. Its twin failure the text never shows is the seat's ACTS: whether it briefed a
long authored artifact or a deep read out to a worker, whether each unit of work went to the cheapest
sufficient tier, whether it kept pulling unblocked work or idled after a landing. No text arm can see an
act. This judge generalizes the register judge from the turn's OUTPUT TEXT to the turn's ACTION TRACE:
the ordered record of which tools the seat called this turn, read from the `tool_use` events in the
transcript. The trace is rendered to quotable plain text (one line per tool call) and handed, with the
orchestration law, to the same one model call, so the reused hallucination guard has spans to match.

It REUSES the register judge's mechanism unchanged — `register_judge_core.judge` supplies the judge
frame, the one model call, the hallucination guard, and the stand-down-on-its-own-breakage contract
[SPEC INV-203]. This file adds only the trace-reading arm around that core.

Contract: reads a Stop-hook payload on stdin, writes a Stop-hook JSON decision on stdout, exits 0. An
EMPTY trace — a chat-only turn with no tool call — has no act to judge and exits 0 silently. It NEVER
blocks on its own breakage: no binary, a timeout, a non-zero exit, or an unreadable law/trace stands the
judge down and says so on stderr, never blocking on its own failure.

Its verdict lands in a DISTINCT per-session slot (~/.claude/hooks/.judge/<session>.conduct.json, written
by conduct-judge-collect.sh), kept apart from the register judge's <session>.json so a turn that trips
both judges never has one verdict overwrite the other [SPEC INV-241].

Opt-in and OFF by default: reading a transcript and resting on a model call, it stays OUT of the
deterministic suite and push gate — a host turns it on by adding its two arms to their own settings.json.

Repo home: hooks/conduct-judge.py; installed copy: ~/.claude/hooks/ (beside register_judge_core.py).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import register_judge_core as core  # noqa: E402

# The per-person STRICTNESS is a parameter this judge READS but does not own — its home is the future
# parameters registry [SPEC INV-241]. Until that registry ships, the judge reads a built-in default a
# host overrides by environment, the way the register judge grounds its own tunables.
DEFAULT_STRICTNESS = os.environ.get("CONDUCT_JUDGE_STRICTNESS", "normal")

# The file tools whose input carries a file path worth showing in the trace line.
_FILE_TOOLS = {"Edit", "Write", "Read", "NotebookEdit", "MultiEdit"}


def law_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "conduct-law.md")


def load_law_body(path=None):
    """The orchestration law body the model judges the trace against (SPEC INV-241): four members —
    worker-routing, lean-orchestrator, pull-unblocked-work-and-never-idle, classify-the-subtask. Kept in
    a file beside this hook. Unreadable -> "" so main stands the judge down (a missing law is the judge's
    own breakage, never a red)."""
    if path is None:
        path = law_path()
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read().strip()
    except OSError:
        return ""


def strictness_note(level):
    """Fold the built-in strictness default into the prompt, without depending on any unbuilt registry."""
    return (
        "STRICTNESS — judge at the '%s' level. At 'lenient' red only a clear, unambiguous violation; at "
        "'normal' red a violation a reasonable reviewer would name from the trace; at 'strict' red a "
        "borderline act too. This is a built-in default read from CONDUCT_JUDGE_STRICTNESS until the "
        "parameters registry owns it.\n\n" % level
    )


def orchestration_law(level=None):
    """The full law body handed to the judge: the strictness note followed by the four-member law."""
    level = DEFAULT_STRICTNESS if level is None else level
    body = load_law_body()
    if not body:
        return ""
    return strictness_note(level) + body


def _is_tool_result(rec):
    """A type:"user" record carrying tool_result blocks is the harness reporting a tool's output, not a
    human turn — the same boundary test the register judge uses."""
    content = rec.get("message", {}).get("content", [])
    if not isinstance(content, list):
        return False
    return any(isinstance(b, dict) and b.get("type") == "tool_result" for b in content)


def _authored_size(name, inp):
    """An approximate SIZE signal for the content this call authors (Write/Edit/NotebookEdit) or the range
    it reads (Read), so LAW 1 (worker-routing) and LAW 2 (lean-orchestrator) — which turn on a LONG
    authored artifact versus a glance-sized inline edit — can be decided from the trace alone. Without it a
    one-line edit and a 500-line inline Write render identically. Returns a short "~N lines" tag, or ""."""
    text = None
    if name == "Write":
        text = inp.get("content")
    elif name == "Edit":
        text = inp.get("new_string")
    elif name == "NotebookEdit":
        text = inp.get("new_source")
    elif name == "MultiEdit":
        edits = inp.get("edits")
        if isinstance(edits, list):
            text = "\n".join(e.get("new_string", "") for e in edits if isinstance(e, dict))
    if isinstance(text, str) and text:
        lines = text.count("\n") + 1
        return "~%d line%s" % (lines, "" if lines == 1 else "s")
    if name == "Read":
        limit = inp.get("limit")
        if isinstance(limit, int) and limit:
            return "~%d lines" % limit
    return ""


def _summarize(name, inp):
    """A short, quotable summary of one tool call's input, for the trace line after the tool name."""
    if not isinstance(inp, dict):
        return ""
    if name in _FILE_TOOLS:
        fp = inp.get("file_path") or inp.get("notebook_path") or ""
        base = os.path.basename(fp) if fp else ""
        size = _authored_size(name, inp)
        if size:
            return "%s (%s)" % (base, size) if base else "(%s)" % size
        return base
    if name in ("Agent", "Task"):
        d = inp.get("description") or inp.get("subagent_type") or inp.get("prompt") or ""
        return d.strip().splitlines()[0][:80] if d else ""
    if name == "Bash":
        d = inp.get("description") or inp.get("command") or ""
        return d.strip().splitlines()[0][:80] if d else ""
    # Any other tool: a compact hint from the first stringy input value, else nothing.
    for v in inp.values():
        if isinstance(v, str) and v.strip():
            return v.strip().splitlines()[0][:80]
    return ""


def render_call(name, inp):
    """One tool call -> one quotable trace line: "Edit PRODUCT_SPEC.md" / "Agent: draft spec-delta"."""
    name = name or "tool"
    summary = _summarize(name, inp)
    if not summary:
        return name
    sep = ": " if name in ("Agent", "Task", "Bash") else " "
    return name + sep + summary


def render_trace(calls):
    """Render the ordered (name, input) calls to plain text, one line per call, so the reused
    hallucination guard has verbatim spans to match against the model's quoted evidence."""
    return "\n".join(render_call(name, inp) for name, inp in calls)


def conduct_reason(offences):
    """The block message: a forward-looking behavioural correction [SPEC INV-241]. It names each missed
    act so the seat holds the law from the NEXT turn, and asks for a redo only where the act still stands
    cheaply reversible, since a finished turn's acts already committed. Reuses the offence shape core
    produced (quote = the offending trace line, law, why); only the human-facing framing is conduct's."""
    lines = "\n".join(
        "  · %s\n      [law %s] %s" % (o.get("quote", ""), o.get("law", "?"), o.get("why", ""))
        for o in offences[:5]
    )
    return (
        "CONDUCT JUDGE — the action trace broke a standing orchestration law:\n"
        + lines
        + "\n\nHold the named law from the next turn: route the heavy unit to a worker, keep the seat lean, "
        "pull the next unblocked item, do the mechanical subtask yourself. Redo now only where the act "
        "still stands cheaply reversible; otherwise carry the correction forward. If one flag is wrong, "
        "say which and why in one line and continue."
    )


def action_trace(path):
    """The ordered ACTION TRACE for THIS turn: every assistant `tool_use` block since the last real human
    message, as (tool_name, tool_input) pairs, in call order.

    The boundary is the register judge's own: walk back to the last type:"user" record that carries real
    human text, skipping tool_result user records (in a real transcript every tool result is itself a
    type:"user" record). Everything assistant after that boundary is this turn; its tool_use blocks are
    the acts to judge. A tool_result user record is not an act and is skipped.
    """
    if not path or not os.path.exists(path):
        return []
    try:
        with open(path) as fh:
            records = []
            for line in fh:
                try:
                    records.append(json.loads(line))
                except ValueError:
                    continue
    except OSError:
        return []
    start = 0
    for i in range(len(records) - 1, -1, -1):
        rec = records[i]
        if rec.get("type") == "user" and not rec.get("isSidechain") and not _is_tool_result(rec):
            start = i + 1
            break
    calls = []
    for rec in records[start:]:
        if rec.get("type") != "assistant" or rec.get("isSidechain"):
            continue
        blocks = rec.get("message", {}).get("content", [])
        if not isinstance(blocks, list):
            continue
        for b in blocks:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                calls.append((b.get("name", ""), b.get("input", {})))
    return calls


def main():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        sys.exit(0)
    if payload.get("stop_hook_active"):  # never loop
        sys.exit(0)
    calls = action_trace(payload.get("transcript_path", ""))
    if not calls:  # EMPTY-TRACE SKIP: a chat-only turn has no act to judge
        sys.exit(0)
    law = orchestration_law()
    if not law:  # the law itself is unreadable — stand down, never red
        sys.stderr.write("conduct-judge stood down: orchestration law unreadable\n")
        sys.exit(0)
    rendered = render_trace(calls)
    offences, error = core.judge(rendered, law, surface="conduct")
    if error:
        # Stand down loudly enough that a silent net is read rather than trusted [SPEC INV-202].
        sys.stderr.write("conduct-judge stood down: %s\n" % error)
        sys.exit(0)
    if not offences:
        sys.exit(0)
    reason = conduct_reason(offences)
    print(json.dumps({"decision": "block", "reason": reason, "suppressOutput": True}))
    sys.exit(0)


if __name__ == "__main__":
    main()

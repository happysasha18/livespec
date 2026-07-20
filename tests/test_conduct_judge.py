# -*- coding: utf-8 -*-
"""The conduct judge reads what the seat DID — the action trace (SPEC INV-241).

The register judge holds a register class by handing a turn's TEXT to a model that reads meaning. Its twin
failure the text never shows is the seat's ACTS. This module drives the conduct judge that generalizes the
register judge from the turn's output text to the turn's ACTION TRACE — the ordered `tool_use` events —
judged against the standing orchestration laws.

It REUSES the register judge's mechanism: register_judge_core supplies the one model call, the
hallucination guard, and the stand-down contract. So, exactly as in test_register_judge.py, nothing here
calls a live model — the VERDICT logic is driven against a STUBBED model output (a canned subprocess
result and canned parse input), the stand-down is driven by faking a missing binary, and the trace
extraction / rendering / empty-skip / slot-path facts are real and deterministic.

Red-first: before hooks/conduct-judge.py exists, this module fails to import — that is the red.
"""
import importlib.util
import io
import json
import os
import subprocess
import sys

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = os.path.join(REPO, "hooks")


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sys.path.insert(0, HOOKS)
core = _load(os.path.join(HOOKS, "register_judge_core.py"), "register_judge_core")
conduct = _load(os.path.join(HOOKS, "conduct-judge.py"), "conduct_judge_hook")

CONDUCT_HOOK = os.path.join(HOOKS, "conduct-judge.py")
COLLECT = os.path.join(HOOKS, "conduct-judge-collect.sh")
REPORT = os.path.join(HOOKS, "conduct-judge-report.sh")


def _transcript(tmp_path, records):
    """Write raw record dicts as JSONL and return the path."""
    p = tmp_path / "transcript.jsonl"
    with open(p, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return str(p)


def _assistant_text(text, mid="a"):
    return {"type": "assistant",
            "message": {"role": "assistant", "id": mid, "content": [{"type": "text", "text": text}]}}


def _assistant_tool(name, inp, mid="a"):
    return {"type": "assistant",
            "message": {"role": "assistant", "id": mid,
                        "content": [{"type": "tool_use", "id": "t_" + mid, "name": name, "input": inp}]}}


def _human(text):
    return {"type": "user", "message": {"role": "user", "content": text}}


def _tool_result(tid, out):
    return {"type": "user",
            "message": {"role": "user",
                        "content": [{"type": "tool_result", "tool_use_id": tid, "content": out}]}}


# ---- (a) trace extraction: ordered tool_use since the last human message, tool_result skipped ---------

def test_action_trace_extracts_tool_uses_in_order(tmp_path):
    """The assistant tool_use blocks since the last real human message yield the ordered tool list; the
    tool_result user record between them is not an act and is skipped."""
    path = _transcript(tmp_path, [
        _human("go"),
        _assistant_tool("Edit", {"file_path": "/x/PRODUCT_SPEC.md"}, "a1"),
        _tool_result("t_a1", "ok"),                                   # a tool RESULT, not an act
        _assistant_tool("Agent", {"description": "draft spec-delta"}, "a2"),
        _assistant_tool("Bash", {"command": "python3 -m pytest -q"}, "a3"),
    ])
    calls = conduct.action_trace(path)
    names = [n for n, _ in calls]
    assert names == ["Edit", "Agent", "Bash"], names


def test_action_trace_scopes_to_the_current_turn(tmp_path):
    """Only tool_use blocks AFTER the last human message belong to this turn."""
    path = _transcript(tmp_path, [
        _human("first"),
        _assistant_tool("Read", {"file_path": "/x/OLD.md"}, "a0"),   # prior turn, out of scope
        _human("second"),
        _assistant_tool("Write", {"file_path": "/x/NEW.md"}, "a1"),
    ])
    names = [n for n, _ in conduct.action_trace(path)]
    assert names == ["Write"], names


def test_action_trace_boundary_skips_tool_result_user_records(tmp_path):
    """The human-turn boundary is the real human user record, not a tool_result user record — so a
    tool_use earlier in the turn is still gathered rather than cut off at the last tool_result."""
    path = _transcript(tmp_path, [
        _human("go"),
        _assistant_tool("Write", {"file_path": "/x/A.md"}, "a1"),
        _tool_result("t_a1", "done"),
        _assistant_tool("Write", {"file_path": "/x/B.md"}, "a2"),
    ])
    names = [n for n, _ in conduct.action_trace(path)]
    assert names == ["Write", "Write"], names


# ---- (b) rendering to quotable text ------------------------------------------------------------------

def test_render_trace_is_quotable_one_line_per_call():
    """Each call renders to one quotable line (>= the core quote floor), so the reused hallucination guard
    has verbatim spans to match: "Edit PRODUCT_SPEC.md" / "Agent: draft spec-delta"."""
    calls = [
        ("Edit", {"file_path": "/repo/PRODUCT_SPEC.md"}),
        ("Agent", {"description": "draft spec-delta"}),
        ("Bash", {"command": "python3 -m pytest -q"}),
    ]
    rendered = conduct.render_trace(calls)
    lines = rendered.splitlines()
    assert lines[0] == "Edit PRODUCT_SPEC.md"
    assert lines[1] == "Agent: draft spec-delta"
    assert lines[2].startswith("Bash: ")
    for ln in lines:
        assert len(ln) >= core.MIN_QUOTE_CHARS, ln
    # a rendered line is a verbatim span the core guard can match back out of the trace text
    assert core.matched_span("Edit PRODUCT_SPEC.md", rendered) == "Edit PRODUCT_SPEC.md"


def test_render_carries_a_size_signal_for_authored_content():
    """LAW 1/2 turn on a LONG authored artifact vs a glance-sized inline edit, so the rendered trace must
    carry a size signal: a big inline Write shows its size, a one-line edit shows a small one — a 1-line
    edit and a 500-line inline Write must NOT render identically. The line stays one-per-call and quotable."""
    big = "\n".join("body line %d" % i for i in range(420))
    big_line = conduct.render_call("Write", {"file_path": "/x/BIG.md", "content": big})
    small_line = conduct.render_call("Edit", {"file_path": "/x/BIG.md", "new_string": "one small line"})
    assert big_line == "Write BIG.md (~420 lines)", big_line
    assert "~420 lines" in big_line
    # the one-line edit's size is small (a glance), never the long-artifact number
    assert "~1 line" in small_line and "420" not in small_line
    # a deep Read range is signalled too, so a big inline read is visible to LAW 2
    assert "~1500 lines" in conduct.render_call("Read", {"file_path": "/x/HUGE.md", "limit": 1500})
    # both stay single-line and above the core quote floor (quotable evidence)
    for ln in (big_line, small_line):
        assert "\n" not in ln and len(ln) >= core.MIN_QUOTE_CHARS


# ---- (c) EMPTY-TRACE skip: a chat-only turn exits 0 with no verdict ----------------------------------

def test_empty_trace_skips_exit_zero_no_verdict(tmp_path):
    """A turn with assistant text but no tool_use has no act to judge: the hook exits 0 and writes no
    verdict on stdout. (It never even reaches the model call.)"""
    path = _transcript(tmp_path, [
        _human("just chatting"),
        _assistant_text("Here is a plain answer with no tool calls.", "a1"),
    ])
    assert conduct.action_trace(path) == []
    payload = json.dumps({"transcript_path": path, "session_id": "s-empty"})
    proc = subprocess.run([sys.executable, CONDUCT_HOOK], input=payload,
                          capture_output=True, text=True)
    assert proc.returncode == 0
    assert proc.stdout.strip() == "", "an empty trace must produce no verdict on stdout"


# ---- (d) DISTINCT verdict slot: .conduct.json, never the register slot -------------------------------

def test_verdict_slot_is_the_distinct_conduct_slot():
    """Both arms use <session>.conduct.json, never the register judge's bare <session>.json slot, so a
    turn tripping both judges never has one verdict overwrite the other."""
    collect = open(COLLECT, encoding="utf-8").read()
    report = open(REPORT, encoding="utf-8").read()
    assert "${SESSION}.conduct.json" in collect
    assert "${SESSION}.conduct.json" in report
    # neither arm targets the register judge's undecorated slot
    assert "${SESSION}.json" not in collect.replace("${SESSION}.conduct.json", "")
    assert "${SESSION}.json" not in report.replace("${SESSION}.conduct.json", "")


# ---- (e) stand-down on a broken / missing model binary leaves no verdict, never reds -----------------

def test_judge_stands_down_when_no_binary(monkeypatch):
    """No claude on PATH stands the shared core down with an error — the conduct judge inherits it."""
    def _boom(*a, **k):
        raise FileNotFoundError("no claude")
    monkeypatch.setattr(core.subprocess, "run", _boom)
    offences, error = core.judge("Edit PRODUCT_SPEC.md", conduct.orchestration_law())
    assert offences == [] and "no claude binary" in error


def test_hook_stands_down_on_broken_binary_never_reds(tmp_path):
    """End to end: a non-empty trace with the model binary absent (empty PATH) leaves NO verdict on stdout
    and exits 0 — a guard that reds on its own breakage would train the seat to route around it."""
    path = _transcript(tmp_path, [
        _human("go"),
        _assistant_tool("Write", {"file_path": "/x/BIG.md"}, "a1"),
    ])
    empty = tmp_path / "nobin"
    empty.mkdir()
    env = dict(os.environ, PATH=str(empty))          # no `claude` reachable
    payload = json.dumps({"transcript_path": path, "session_id": "s-broken"})
    proc = subprocess.run([sys.executable, CONDUCT_HOOK], input=payload,
                          capture_output=True, text=True, env=env)
    assert proc.returncode == 0
    assert proc.stdout.strip() == "", "a stand-down must leave no verdict"
    assert "stood down" in proc.stderr


# ---- (f) VERDICT logic against a STUBBED model output ------------------------------------------------

# A trace with a clear violation: a long artifact authored INLINE (a run of Edits + a Write the seat typed
# itself) with NO Agent dispatch — worker-routing (law 1) broken.
VIOLATION_TRACE = conduct.render_trace([
    ("Edit", {"file_path": "/repo/PRODUCT_SPEC.md"}),
    ("Edit", {"file_path": "/repo/PRODUCT_SPEC.md"}),
    ("Edit", {"file_path": "/repo/ARCHITECTURE.md"}),
    ("Write", {"file_path": "/repo/TEST_MATRIX.md"}),
])

# A clean trace: the drafting is DISPATCHED to a worker, the read delegated, the seat keeps only orchestration.
CLEAN_TRACE = conduct.render_trace([
    ("Agent", {"description": "draft spec-delta for the new surface"}),
    ("Agent", {"description": "review the drafted spec"}),
    ("Bash", {"command": "python3 -m pytest -q"}),
])


def test_violation_trace_reds_under_a_stubbed_model():
    """Handed the model's verdict quoting an offending trace line, the judge keeps the offence (the quote
    is a verbatim span of the rendered trace)."""
    canned = json.dumps({"offences": [
        {"quote": "Write TEST_MATRIX.md", "law": 1, "why": "long artifact authored inline, no dispatch"}]})
    offences, error = core.parse_offences(canned, VIOLATION_TRACE)
    assert error is None
    assert len(offences) == 1 and offences[0]["quote"] == "Write TEST_MATRIX.md"


def test_violation_reds_through_the_full_judge_call(monkeypatch):
    """The whole core.judge path with the model STUBBED (a canned subprocess result) reds the violation —
    no live binary touched."""
    canned = json.dumps({"offences": [
        {"quote": "Edit ARCHITECTURE.md", "law": 1, "why": "deep authoring kept on the seat"}]})
    monkeypatch.setattr(core.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, 0, stdout=canned, stderr=""))
    offences, error = core.judge(VIOLATION_TRACE, conduct.orchestration_law())
    assert error is None and len(offences) == 1
    assert offences[0]["quote"] == "Edit ARCHITECTURE.md"


def test_clean_trace_draws_an_empty_verdict(monkeypatch):
    """A trace that dispatched the drafting and delegated the read draws an empty verdict from the judge."""
    monkeypatch.setattr(core.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, 0, stdout='{"offences": []}', stderr=""))
    offences, error = core.judge(CLEAN_TRACE, conduct.orchestration_law())
    assert error is None and offences == []


def test_hallucinated_trace_quote_is_dropped():
    """A quote not verbatim in the rendered trace is no evidence and is dropped (the reused guard)."""
    canned = json.dumps({"offences": [{"quote": "the seat idled forever", "law": 3, "why": "x"}]})
    offences, error = core.parse_offences(canned, VIOLATION_TRACE)
    assert error is None and offences == []


# ---- (D3) the block-emit path: main() writes the forward-looking conduct verdict on stdout -----------

def test_main_emits_the_conduct_block_end_to_end(monkeypatch, tmp_path, capsys):
    """Drive main() end to end with the model STUBBED (one offence), a violation transcript on stdin, and
    assert stdout carries {"decision":"block", ...} whose reason is the FORWARD-LOOKING conduct message
    (names the missed law, "next turn", redo-only-if-reversible) — NOT the register judge's block_reason.
    (RED-first: gut conduct_reason's emission and this reds.)"""
    big = "\n".join("body line %d" % i for i in range(500))
    inp = {"file_path": "/repo/BIG.md", "content": big}
    offending_line = conduct.render_call("Write", inp)      # the exact line main() will render
    path = _transcript(tmp_path, [
        _human("go"),
        _assistant_tool("Write", inp, "a1"),                # a long artifact authored inline, no dispatch
    ])
    canned = json.dumps({"offences": [
        {"quote": offending_line, "law": 1, "why": "long artifact authored inline, no dispatch"}]})
    monkeypatch.setattr(conduct.core.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, 0, stdout=canned, stderr=""))
    payload = json.dumps({"transcript_path": path, "session_id": "s-emit"})
    monkeypatch.setattr(sys, "stdin", io.StringIO(payload))

    with pytest.raises(SystemExit) as ex:
        conduct.main()
    assert ex.value.code == 0

    out = capsys.readouterr().out.strip()
    obj = json.loads(out)
    assert obj["decision"] == "block"
    assert obj.get("suppressOutput") is True
    reason = obj["reason"]
    assert "CONDUCT JUDGE" in reason
    assert offending_line in reason                          # the missed act is named
    assert "next turn" in reason                             # forward-looking correction
    assert "reversible" in reason                            # redo only where cheaply reversible
    # it is the conduct message, NOT the register judge's block_reason wording
    assert "Restate each as a plain positive sentence" not in reason
    assert "carries lines that add no information" not in reason


def test_main_stays_silent_on_a_clean_trace(monkeypatch, tmp_path, capsys):
    """The counterpart: a clean trace with an empty verdict emits NOTHING on stdout and exits 0."""
    inp = {"description": "draft the spec-delta"}
    path = _transcript(tmp_path, [_human("go"), _assistant_tool("Agent", inp, "a1")])
    monkeypatch.setattr(conduct.core.subprocess, "run",
                        lambda *a, **k: subprocess.CompletedProcess(a, 0, stdout='{"offences": []}', stderr=""))
    monkeypatch.setattr(sys, "stdin",
                        io.StringIO(json.dumps({"transcript_path": path, "session_id": "s-clean"})))
    with pytest.raises(SystemExit) as ex:
        conduct.main()
    assert ex.value.code == 0
    assert capsys.readouterr().out.strip() == ""


# ---- The law body: exactly the four members, oriented to the ACTION TRACE ----------------------------

def test_orchestration_law_names_the_four_members():
    """The law body carries exactly the four members and orients the model to judge the ACTION TRACE."""
    body = conduct.load_law_body().lower()
    assert "worker-routing" in body
    assert "lean-orchestrator" in body
    assert "pull-unblocked-work-and-never-idle" in body
    assert "classify-the-subtask" in body
    assert "action trace" in body
    # exactly four laws
    import re
    assert re.findall(r"LAW (\d+) —", conduct.load_law_body()) == ["1", "2", "3", "4"]


def test_law_3_and_4_carry_the_partial_evidence_note():
    """LAW 3 (idle-after-landing) and LAW 4 (classify-the-subtask) each note the trace gives only PARTIAL
    evidence — they lean on the net-meter and human review window and red only on a clear-cut case. The
    honesty note is scoped to those two; LAW 1/2 (which the trace CAN decide) do not carry it."""
    body = conduct.load_law_body()
    assert body.lower().count("partial evidence") == 2
    assert body.count("clear-cut case") == 2
    assert "net-meter" in body and "human review window" in body
    # LAW 1 / LAW 2 section (before LAW 3) carries no such hedge — the trace decides them.
    laws_1_2 = body.split("LAW 3")[0]
    assert "partial evidence" not in laws_1_2.lower()


def test_strictness_folds_the_env_default_into_the_law(monkeypatch):
    """The built-in strictness default (CONDUCT_JUDGE_STRICTNESS) folds into the prompt body, depending on
    no unbuilt registry."""
    law = conduct.orchestration_law(level="strict")
    assert "STRICTNESS" in law and "'strict'" in law
    assert "worker-routing" in law.lower()


# ---- (g) classification: the conduct hooks are in the library, not wired -----------------------------

def test_conduct_hooks_are_classified_library_not_wired():
    """conduct-judge.py and both arms (and the law file) live under hooks/, so gate v requires each be
    classified — they are LIBRARY (opt-in, off by default), never wired into the pack's settings.json."""
    decl = json.load(open(os.path.join(REPO, "guardrails", "judge-hooks.json")))
    lib = set(decl.get("library", []))
    wired = set(decl.get("wired", {}))
    for stem in ("conduct-judge", "conduct-judge-collect", "conduct-judge-report", "conduct-law"):
        assert stem in lib, "%s must be classified in the library" % stem
        assert stem not in wired, "%s must NOT be wired (opt-in, off by default)" % stem

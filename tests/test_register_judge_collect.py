# -*- coding: utf-8 -*-
"""The judge's async arms deliver a verdict (ROADMAP rows 416/418, corrections 2026-07-17).

The chat judge is asynchronous: a Stop arm (register-judge-collect.sh) backgrounds the model call and
returns at once; a UserPromptSubmit arm (register-judge-report.sh) reads the verdict the next turn. These
tests drive both arms with a STUBBED judge (a fake register-judge.py that sleeps, then writes a verdict),
so nothing here needs a live `claude` binary.

Red-first: against the pre-correction collect script the verdict file is DESTROYED — the script waits on
a PID that is not its child, finds the still-empty .part, and removes it while the judge writes into the
unlinked inode. So `test_collect_delivers_the_verdict_file` times out with no verdict (the live symptom:
~/.claude/hooks/.judge held only .err files, zero verdicts). After the fix one subshell owns both the
write and the rename, so the verdict lands.
"""
import json
import os
import subprocess
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOOKS = os.path.join(REPO, "hooks")
COLLECT = os.path.join(HOOKS, "register-judge-collect.sh")
REPORT = os.path.join(HOOKS, "register-judge-report.sh")

SESSION = "test-session-abc"
REASON = "REGISTER JUDGE — the text carries lines that add no information:\n  · stub"

# A fake judge: read the payload off stdin, sleep long enough that a same-instant .part check finds it
# empty (the race the bug depended on), then write the verdict to stdout the way the real judge does.
FAKE_JUDGE = (
    "#!/usr/bin/env python3\n"
    "import sys, time, json\n"
    "sys.stdin.read()\n"
    "time.sleep(1.5)\n"
    "sys.stdout.write(json.dumps({'decision': 'block', 'reason': %r, 'suppressOutput': True}))\n"
    % REASON
)


def _scratch_home(tmp_path, judge_body=FAKE_JUDGE):
    home = tmp_path / "home"
    hooks = home / ".claude" / "hooks"
    hooks.mkdir(parents=True)
    (hooks / "register-judge.py").write_text(judge_body, encoding="utf-8")
    return str(home)


def _run(script, home, payload):
    env = dict(os.environ)
    env["HOME"] = home
    return subprocess.run(["sh", script], input=json.dumps(payload), text=True,
                          capture_output=True, env=env)


def _wait_for(path, timeout=8.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if os.path.exists(path):
            return True
        time.sleep(0.1)
    return False


def test_collect_delivers_the_verdict_file(tmp_path):
    """The Stop arm returns at once, and the backgrounded judge's verdict LANDS (is not destroyed)."""
    home = _scratch_home(tmp_path)
    verdict = os.path.join(home, ".claude", "hooks", ".judge", "%s.json" % SESSION)
    part = verdict + ".part"
    r = _run(COLLECT, home, {"session_id": SESSION})
    assert r.returncode == 0
    assert _wait_for(verdict), "the verdict file must appear — the async arm must not destroy it"
    # the intermediate .part is renamed away, never left behind
    assert not os.path.exists(part)
    body = json.load(open(verdict))
    assert body["reason"] == REASON


def test_report_arm_reads_and_consumes_the_verdict(tmp_path):
    """The report arm surfaces the verdict's reason to the model, then deletes the one-shot verdict."""
    home = _scratch_home(tmp_path)
    verdict = os.path.join(home, ".claude", "hooks", ".judge", "%s.json" % SESSION)
    assert _run(COLLECT, home, {"session_id": SESSION}).returncode == 0
    assert _wait_for(verdict)
    r = _run(REPORT, home, {"session_id": SESSION})
    assert r.returncode == 0
    assert "add no information" in r.stdout
    assert "judged while you waited" in r.stdout  # the report arm's own reframing
    assert not os.path.exists(verdict), "a consumed verdict is deleted, never re-reported"


def test_empty_judge_output_leaves_no_stale_part(tmp_path):
    """A judge that writes nothing (stood down) leaves neither a verdict nor a dangling .part."""
    silent = "#!/usr/bin/env python3\nimport sys\nsys.stdin.read()\n"  # writes nothing to stdout
    home = _scratch_home(tmp_path, judge_body=silent)
    jdir = os.path.join(home, ".claude", "hooks", ".judge")
    verdict = os.path.join(jdir, "%s.json" % SESSION)
    part = verdict + ".part"
    assert _run(COLLECT, home, {"session_id": SESSION}).returncode == 0
    time.sleep(2.0)
    assert not os.path.exists(verdict)
    assert not os.path.exists(part)

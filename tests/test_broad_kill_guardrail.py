"""INV-162 (ROADMAP 334) — a cleanup kill targets the test resource uniquely (a recorded PID/process
group or an install path), never a broad NAME pattern that can match the human's own program.

Born of a real incident: a test-cleanup's broad `pkill chrome` / `pkill chrome_crashpad_handler` closed
the user's REAL browser mid-session, destroying work state outside git (base rule 17). The general law:
a cleanup acts only on what this run provably owns, never a shared resource in current use.

The mechanical net is `guardrails/check-broad-kill.sh`: it reds if any tracked script kills a browser by
a broad name without a path scope. These tests assert the guardrail exists, passes the clean repo, reds a
planted forbidden pattern (red-first), and lets a path-scoped kill through; and that the spec and the
worker-briefing guidance state the rule. Landed 2026-07-15."""
import os
import subprocess
import tempfile
from conftest import ROOT, read

GUARD = os.path.join(ROOT, "guardrails", "check-broad-kill.sh")


def _run(target=None):
    cmd = ["bash", GUARD] + ([target] if target else [])
    return subprocess.run(cmd, capture_output=True, text=True)


def test_guardrail_ships():
    assert os.path.isfile(GUARD), "guardrails/check-broad-kill.sh missing"


def test_guardrail_passes_the_clean_repo():
    # the pack's own harness kills only by os.killpg on its recorded pid — no pkill/killall of a browser
    # name anywhere — so the real repo is green.
    r = _run()
    assert r.returncode == 0, r.stdout + r.stderr


def test_guardrail_reds_on_a_broad_kill():
    # red-first: a script that pkills a bare browser name is the footgun that closed the user's Chrome.
    with tempfile.TemporaryDirectory() as d:
        bad = os.path.join(d, "cleanup.sh")
        with open(bad, "w") as f:
            f.write('#!/usr/bin/env bash\npkill -9 -f "chrome_crashpad_handler"\npkill -9 chrome\n')
        r = _run(bad)
        assert r.returncode != 0, "guardrail passed a broad `pkill chrome` — the footgun is unguarded"
        assert "INV-162" in (r.stdout + r.stderr)


def _reds(line, ext=".sh"):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "cleanup" + ext)
        with open(p, "w") as f:
            f.write("#!/usr/bin/env bash\n" + line + "\n")
        return _run(p).returncode != 0


def test_guardrail_catches_every_evasion():
    # the ways a broad kill slipped past the first cut (prover F1–F3), each must now red.
    dangerous = [
        'pkill -9 chrome',                                  # the founding incident
        'pkill -9 -f "chrome_crashpad_handler"',            # the founding incident
        'killall Chrome',                                   # killall, not pkill (F2)
        'killall "Google Chrome"',                          # quoted name (F2)
        'kill -9 $(pgrep chrome)',                          # kill via command substitution (F2)
        'pgrep chrome | xargs kill -9',                     # pipe to kill (F2)
        'pkill -9 chrome  # cleanup ~/.cache/puppeteer leftovers',  # path only in a COMMENT (F1)
    ]
    for line in dangerous:
        assert _reds(line), "guardrail let a broad kill through: %r" % line
    # subprocess form in python (F2), and a JS teardown (F3) must red too
    assert _reds('subprocess.run(["pkill", "chrome"])', ".py"), "python pkill slipped"
    assert _reds('execSync("pkill -9 chrome")', ".js"), "JS teardown slipped (F3 — .js unscanned)"


def test_guardrail_allows_the_safe_forms():
    # a bare pgrep that does NOT kill, a pid-scoped python kill, and an install-path kill are all fine.
    safe = [
        'pgrep chrome  # just list them, no kill',          # listing only, no kill verb near a name
        'os.killpg(self.proc.pid, signal.SIGKILL)',         # kills its own recorded process group
        'pkill -9 -f "$HOME/.cache/puppeteer/chrome/.*chrome"',  # path-scoped install target
    ]
    for line in safe:
        assert not _reds(line), "guardrail false-flagged a safe line: %r" % line


def test_guardrail_allows_a_path_scoped_kill():
    # the legal form: a kill scoped to the test browser's install path or its own user-data-dir is fine.
    with tempfile.TemporaryDirectory() as d:
        ok = os.path.join(d, "cleanup.sh")
        with open(ok, "w") as f:
            f.write('#!/usr/bin/env bash\n'
                    '# reap only Chrome-for-Testing under the puppeteer cache, by install path\n'
                    'pkill -9 -f "$HOME/.cache/puppeteer/chrome/.*chrome"\n')
        r = _run(ok)
        assert r.returncode == 0, r.stdout + r.stderr


def test_spec_states_the_cleanup_ownership_law():
    spec = read("PRODUCT_SPEC.md")
    assert "[INV-162]" in spec
    assert "never a shared resource" in spec or "only on what THIS run provably created and owns" in spec
    # the forbidden broad patterns are named
    assert "chrome_crashpad_handler" in spec


def test_shared_install_path_is_not_a_safe_kill_target():
    # ROADMAP 335 (track-coach cross-session collision): an install path is safe only when
    # unique to this run; where sessions share a path the recorded process group is the sole
    # safe target, the one identity that always stays inside this run.
    spec = read("PRODUCT_SPEC.md")
    assert "unique to this run" in spec
    assert "recorded PID or process group is the only target that always stays inside this run" in spec


def test_worker_briefing_carries_the_constraint():
    # a briefed worker inherits the constraint, so it never reinvents a broad `pkill chrome`.
    bp = read("skills/build-pipeline/SKILL.md")
    assert "INV-162" in bp

"""INV-157's third net — a tracked script that drives a real headless browser must launch it MUTED.

The pack's own two nets for INV-157 (the shipped template's string-check, the consumer's by-deed
process-group diff) never HEAR a divergent fork's sound: a project that hand-rolls or forks its own
browser launch instead of adopting `templates/headless_harness.py` [INV-158] can play audio during a
test run and neither net catches it — tlvphotos did exactly this. The third net is a guardrail,
`guardrails/check-muted-launch.sh`, that reds a file whose CODE carries both a browser-LAUNCH signal
(`--headless`, `--remote-debugging-port`, `puppeteer.launch`, `chromium.launch`) and a code INVOCATION
token (`subprocess`, `Popen`, `.launch(`, and kin) with no `mute-audio` anywhere in that code. The check
is FILE-level, not per-line, because a real launch's arg list often spans multiple lines; it reads the
comment-stripped code on both the launch and the mute side, so a mute flag named only in a comment cannot
satisfy it, and a docstring that merely NAMES a flag with no real invocation is not flagged.

These tests assert the guardrail exists, passes the clean repo, reds a planted unmuted launch (red-first)
including a multi-line arg list, lets a muted launch and a launch-free file through, and — the two
regressions the fresh-eyes audit found — reds a launch whose only mute flag sits in a COMMENT, and passes
a file that only NAMES the flags in a docstring with no invocation. And that the spec states the net."""
import os
import subprocess
import tempfile
from conftest import ROOT, read

GUARD = os.path.join(ROOT, "guardrails", "check-muted-launch.sh")


def _run(target=None):
    cmd = ["bash", GUARD] + ([target] if target else [])
    return subprocess.run(cmd, capture_output=True, text=True)


def _scan(body, name="probe.py"):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, name)
        with open(p, "w") as f:
            f.write(body)
        return _run(p)


def test_guardrail_ships():
    assert os.path.isfile(GUARD), "guardrails/check-muted-launch.sh missing"


def test_guardrail_passes_the_clean_repo():
    # the pack's own real launcher is templates/headless_harness.py, which carries --mute-audio —
    # no tracked script drives a browser unmuted, so the real repo is green.
    r = _run()
    assert r.returncode == 0, r.stdout + r.stderr


def test_reds_on_an_unmuted_headless_launch():
    # red-first: a real headless-Chrome launch (subprocess invocation + flags) with no mute flag is
    # the footgun that played sound during a tlvphotos test run.
    r = _scan(
        "import subprocess\n"
        "subprocess.Popen(['chrome', '--headless', '--remote-debugging-port=9222'])\n"
    )
    assert r.returncode != 0, "guardrail passed an unmuted headless launch — the footgun is unguarded"
    assert "INV-157" in (r.stdout + r.stderr)


def test_allows_a_muted_launch():
    r = _scan(
        "import subprocess\n"
        "subprocess.Popen(['chrome', '--headless', '--remote-debugging-port=9222', '--mute-audio'])\n"
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_allows_a_file_with_no_launch():
    r = _scan('import os\nprint("no browser here")\n', name="helper.py")
    assert r.returncode == 0, r.stdout + r.stderr


def test_catches_a_multiline_arg_list_without_mute():
    # proves the file-level design: the launch flags sit on separate lines from the invocation, no
    # single line carries both a launch signal and mute-audio, yet the file drives an unmuted browser.
    r = _scan(
        "import subprocess\n"
        "args = [\n"
        "    'chrome',\n"
        "    '--headless',\n"
        "    '--remote-debugging-port=9222',\n"
        "    '--disable-gpu',\n"
        "]\n"
        "subprocess.Popen(args)\n"
    )
    assert r.returncode != 0, "guardrail missed a multi-line unmuted launch — it is checking per-line"
    assert "INV-157" in (r.stdout + r.stderr)


def test_allows_multiline_args_with_mute():
    r = _scan(
        "import subprocess\n"
        "args = [\n"
        "    'chrome',\n"
        "    '--headless',\n"
        "    '--remote-debugging-port=9222',\n"
        "    '--mute-audio',\n"
        "]\n"
        "subprocess.Popen(args)\n"
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_comment_only_mute_still_reds():
    # the fresh-eyes audit's highest finding: a mute flag named only in a COMMENT must NOT satisfy the
    # mute check — the file still launches a real browser unmuted and plays sound. This red went GREEN
    # (wrongly passed) before the mute check was moved onto the comment-stripped code.
    r = _scan(
        "import subprocess\n"
        "# TODO: someday add --mute-audio here\n"
        "subprocess.Popen(['chrome', '--headless', '--remote-debugging-port=9222'])\n"
    )
    assert r.returncode != 0, "a comment-only --mute-audio satisfied the mute check — sound plays unheard"
    assert "INV-157" in (r.stdout + r.stderr)


def test_names_flags_in_docstring_without_launch_passes():
    # the audit's false-positive finding: a file that merely NAMES the launch flags in a docstring, with
    # no real invocation, must NOT red — else every doc/test naming the flag needs a hardcoded exclusion.
    r = _scan('"""This module documents the --headless and --remote-debugging-port flags."""\nx = 1\n')
    assert r.returncode == 0, "a docstring naming the flags was falsely flagged as an unmuted launch"


def test_jsx_puppeteer_launch_unmuted_reds():
    # coverage widened to .jsx/.tsx (a React test harness): a puppeteer launch with no mute flag reds.
    r = _scan(
        "const b = await puppeteer.launch({ args: ['--headless', '--remote-debugging-port=9222'] });\n",
        name="harness.jsx",
    )
    assert r.returncode != 0, "an unmuted puppeteer.launch in a .jsx harness slipped past the guardrail"
    assert "INV-157" in (r.stdout + r.stderr)


def test_spec_states_the_third_net():
    spec = read("PRODUCT_SPEC.md")
    assert "A third net catches the divergent harness" in spec


def test_js_comment_only_mute_still_reds():
    # batch audit 2026-07-16, F2: the comment strip was `#`-only, so a JS `// --mute-audio` comment
    # above a real unmuted launch satisfied the mute check. Per-extension stripping closes it.
    r = _scan(
        "// TODO: someday add --mute-audio here\n"
        "const b = await puppeteer.launch({ args: ['--headless', '--remote-debugging-port=9222'] });\n",
        name="harness.js",
    )
    assert r.returncode != 0, "a JS comment-only --mute-audio satisfied the mute check"
    assert "INV-157" in (r.stdout + r.stderr)


def test_js_block_comment_mute_still_reds():
    r = _scan(
        "/* --mute-audio lives here in prose */\n"
        "const b = await puppeteer.launch({ args: ['--headless', '--remote-debugging-port=9222'] });\n",
        name="harness.ts",
    )
    assert r.returncode != 0, "a TS block-comment --mute-audio satisfied the mute check"


def test_js_real_mute_still_passes():
    r = _scan(
        "const b = await puppeteer.launch({ args: ['--headless', '--mute-audio', '--remote-debugging-port=9222'] });\n",
        name="harness.js",
    )
    assert r.returncode == 0, "a really muted JS launch was falsely flagged"

"""INV-242 — the landing-refreshed-map gate.

NEXT_STEPS.md is the resume file (LIVE STATE + queue only); a commit that lands a ROADMAP row
(flips its Status cell to `landed`) but leaves NEXT_STEPS.md untouched hands the next session a
stale map. `guardrails/check-landing-next-steps.py` reds such a commit by name and prints the
flipped row number(s) and the fix. A commit that closes a row to `declined` / `deferred` /
`superseded`, or touches ROADMAP.md prose without a status flip, owes nothing.

Report-shape via the commit graph, not the working tree: it rides the suite only (its test IS its
push-gate coverage) and is NOT wired into guardrails/pre-push.
"""
import os
import subprocess

from conftest import ROOT, read

CHECK = os.path.join(ROOT, "guardrails", "check-landing-next-steps.py")

ROADMAP_HEADER = (
    "| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
    "|---|---|---|---|---|\n"
)


def _roadmap_row(num, status, wish="Some wish"):
    return ROADMAP_HEADER + "| %d | %s | small | %s | Some decision |\n" % (num, wish, status)


def _git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout


def _init_repo(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q", ".")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    return repo


def _write(repo, name, content):
    (repo / name).write_text(content)


def _commit(repo, msg):
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", msg)
    return _git(repo, "rev-parse", "HEAD").strip()


def _run_check(repo, base_sha):
    env = dict(os.environ)
    env["LIVE_SPEC_DIFF_BASE"] = base_sha
    return subprocess.run(["python3", CHECK], cwd=str(repo), capture_output=True, text=True, env=env)


def test_reds_landing_commit_without_next_steps(tmp_path):
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "open"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", _roadmap_row(7, "**landed 2026-07-20**"))
    _commit(repo, "land row 7, no NEXT_STEPS touch")

    r = _run_check(repo, base)
    out = r.stdout + r.stderr
    assert r.returncode != 0, out
    assert "7" in out
    assert "INV-242" in out


def test_passes_landing_commit_that_touches_next_steps(tmp_path):
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "open"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", _roadmap_row(7, "**landed 2026-07-20**"))
    _write(repo, "NEXT_STEPS.md", "state\nrow 7 landed\n")
    _commit(repo, "land row 7, with NEXT_STEPS refresh")

    r = _run_check(repo, base)
    assert r.returncode == 0, r.stdout + r.stderr


def test_passes_non_landing_commit(tmp_path):
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "open"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    # prose-only edit: same status, no landed flip, no NEXT_STEPS touch
    _write(repo, "ROADMAP.md", _roadmap_row(7, "open", wish="Some wish, revised prose"))
    _commit(repo, "prose edit, no status flip")

    r = _run_check(repo, base)
    assert r.returncode == 0, r.stdout + r.stderr


def test_passes_decline_deferred_superseded_close(tmp_path):
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "open"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", _roadmap_row(7, "declined 2026-07-20"))
    _commit(repo, "decline row 7, no NEXT_STEPS touch")

    r = _run_check(repo, base)
    assert r.returncode == 0, r.stdout + r.stderr


def test_reds_landing_with_escaped_pipe_in_wish(tmp_path):
    # A properly-escaped `\|` inside the wish cell must not shift the column count and hide the
    # Status cell — the checker splits on unescaped pipes only (adversarial audit 2026-07-20).
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "open", wish=r"a wish with an escaped \| pipe"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md",
           _roadmap_row(7, "**landed 2026-07-20**", wish=r"a wish with an escaped \| pipe"))
    _commit(repo, "land row 7 with an escaped pipe in the wish, no NEXT_STEPS touch")

    r = _run_check(repo, base)
    out = r.stdout + r.stderr
    assert r.returncode != 0, out
    assert "7" in out
    assert "INV-242" in out


def test_real_repo_range_refreshes_next_steps():
    # Live-tree enforcement: run the checker over THIS repo's real BASE..HEAD, so the law is
    # enforced against real commits in-suite (the far-tier / node-growth live-test pattern), not
    # fixtures alone. A real landing commit that skipped NEXT_STEPS reds the suite and, since the
    # suite is gate b, blocks the push.
    env = dict(os.environ)
    env.pop("LIVE_SPEC_DIFF_BASE", None)
    r = subprocess.run(["python3", CHECK], cwd=ROOT, capture_output=True, text=True, env=env)
    assert r.returncode == 0, (
        "a landing commit in this repo's range did not refresh NEXT_STEPS.md:\n" + r.stdout + r.stderr)


def test_checker_not_wired_into_pre_push():
    assert "check-landing-next-steps" not in read("guardrails/pre-push")


# --- the NEW trigger: the live-body law's closing-commit move (SPEC INV-276, ROADMAP row 480) ---

_ARCHIVE = "docs/queue-archive/rotated-ROADMAP-2026-07.md"
_ARCHIVE_HEADER = (
    "# Rotated ROADMAP rows — 2026-07\n\n"
    "| # | Wish (plain words) | Class | Status | Decision / acceptance |\n"
    "|---|---|---|---|---|\n"
)


def _archive_row(num, status, wish="Some wish"):
    return _ARCHIVE_HEADER + "| %d | %s | small | %s | Some decision |\n" % (num, wish, status)


def _write_sub(repo, name, content):
    p = repo / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def test_new_trigger_landed_move_without_next_steps_reds(tmp_path):
    # A closing commit REMOVES row 7 from the body and ADDS it to the archive with a *landed* status,
    # and does not touch NEXT_STEPS.md — the new trigger reds.
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "*in-work 2026-07-23*"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", ROADMAP_HEADER)  # row 7 gone from the body
    _write_sub(repo, _ARCHIVE, _archive_row(7, "*landed %s; door: feature; delegation: kept*" % _today()))
    _commit(repo, "close row 7 into the month archive, no NEXT_STEPS touch")

    r = _run_check(repo, base)
    out = r.stdout + r.stderr
    assert r.returncode != 0, out
    assert "7" in out
    assert "INV-242" in out


def test_new_trigger_landed_move_with_next_steps_passes(tmp_path):
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "*in-work 2026-07-23*"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", ROADMAP_HEADER)
    _write_sub(repo, _ARCHIVE, _archive_row(7, "*landed %s*" % _today()))
    _write(repo, "NEXT_STEPS.md", "state\nrow 7 landed\n")
    _commit(repo, "close row 7 into the archive, with NEXT_STEPS refresh")

    r = _run_check(repo, base)
    assert r.returncode == 0, r.stdout + r.stderr


def _today():
    import datetime
    return datetime.date.today().isoformat()


def test_new_trigger_relocation_of_old_landed_row_is_exempt(tmp_path):
    # A move whose archived status landed two or more days before the commit's own date is a
    # historical relocation — a conversion or an override fold — and owes no NEXT_STEPS refresh:
    # the map was refreshed at that old landing (SPEC INV-242's carve).
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "*queued* 2026-07-06"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", ROADMAP_HEADER)
    _write_sub(repo, _ARCHIVE, _archive_row(7, "**landed 2026-07-06 ~13:52, session 14** — whole"))
    _commit(repo, "relocate the historically landed row 7, no NEXT_STEPS touch")

    r = _run_check(repo, base)
    assert r.returncode == 0, r.stdout + r.stderr


def test_new_trigger_declined_move_is_exempt(tmp_path):
    # A row leaving the body as *declined* (no landed token in the archived status) owes nothing.
    repo = _init_repo(tmp_path)
    _write(repo, "ROADMAP.md", _roadmap_row(7, "*queued 2026-07-23*"))
    _write(repo, "NEXT_STEPS.md", "state\n")
    base = _commit(repo, "base")

    _write(repo, "ROADMAP.md", ROADMAP_HEADER)
    _write_sub(repo, _ARCHIVE, _archive_row(7, "*declined 2026-07-23*"))
    _commit(repo, "decline row 7 into the archive, no NEXT_STEPS touch")

    r = _run_check(repo, base)
    assert r.returncode == 0, r.stdout + r.stderr

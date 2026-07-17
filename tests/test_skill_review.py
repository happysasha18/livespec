"""A push that changes a skill reds until its skill-creator review is on record
(SPEC INV-208, ROADMAP 419).

Alexander asked for this on 2026-07-17 ~18:26: he leans on the session to remember to run
Anthropic's skill-creator review whenever a skill is modified, and the session forgets, so a
reminder does not hold — he wants a blocking gate. When a diff about to be pushed changes a
skill's body, the push reds unless a skill-creator review record for that change is committed.

The gate mirrors the shape of guardrails/check-prover-record.sh: it reads the push range
(LIVE_SPEC_DIFF_BASE / origin/main / HEAD~1), finds substantive changes under skills/, and
requires a fresh committed record under docs/skill-review/ that names each changed skill and
carries the review's verdict.

The one carve-out that must NOT red: a pure version-frontmatter stamp. scripts/stamp-versions.py
writes `  version: X.Y.Z` into every skill's frontmatter and the `live-spec-base (vX.Y.Z)`
base-reference at each version bump — that is a machine-stamped copy of one fact, not a change to
the skill's instructions, so it owes no skill-creator review.
"""
import os
import subprocess
import tempfile

from conftest import ROOT, read

GATE = os.path.join(ROOT, "guardrails", "check-skill-review.sh")
REVIEW_DIR = os.path.join(ROOT, "docs", "skill-review")


def _run(args, cwd=None, extra_env=None):
    env = dict(os.environ)
    if extra_env:
        env.update(extra_env)
    return subprocess.run(args, cwd=cwd or ROOT, capture_output=True, text=True, env=env)


# --- a scratch repo, so the behavioural proofs never depend on the real repo's HEAD ---

def _init_repo(tmp):
    _run(["git", "init", "-q"], cwd=tmp)
    _run(["git", "config", "user.email", "a@example.com"], cwd=tmp)
    _run(["git", "config", "user.name", "a"], cwd=tmp)


def _write(tmp, relpath, content):
    path = os.path.join(tmp, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def _commit_all(tmp, msg):
    _run(["git", "add", "-A"], cwd=tmp)
    _run(["git", "commit", "-q", "-m", msg], cwd=tmp)


def _head(tmp):
    return _run(["git", "rev-parse", "HEAD"], cwd=tmp).stdout.strip()


SKILL_V1 = "---\nname: demo\nmetadata:\n  version: 1.0.0\n---\n\n# demo\n\nStep one: do the thing.\n"
# a body change (a new instruction line) — substantive
SKILL_BODY_CHANGED = (
    "---\nname: demo\nmetadata:\n  version: 1.0.0\n---\n\n# demo\n\nStep one: do the thing.\n"
    "Step two: do the other thing.\n"
)
# only the frontmatter version line moved (and the base reference) — the stamp diff, NOT substantive
SKILL_STAMP_ONLY = (
    "---\nname: demo\nmetadata:\n  version: 2.0.0\n---\n\n# demo\n\nStep one: do the thing.\n"
)
SKILL_V1_WITH_BASEREF = (
    "---\nname: demo\nmetadata:\n  version: 1.0.0\n---\n\n# demo (`live-spec-base` (v1.0.0))\n\n"
    "Step one: do the thing.\n"
)
SKILL_STAMP_ONLY_BASEREF = (
    "---\nname: demo\nmetadata:\n  version: 2.0.0\n---\n\n# demo (`live-spec-base` (v2.0.0))\n\n"
    "Step one: do the thing.\n"
)

RECORD = (
    "# Skill review — demo\n\nSKILL-REVIEW\n\nSkill: demo\n\n"
    "Reviewer: skill-creator (Anthropic)\n\nVerdict: passes — description and body reviewed.\n"
)


# --- the gate ships ---

def test_gate_ships():
    assert os.path.isfile(GATE), "guardrails/check-skill-review.sh missing"


def test_review_dir_ships():
    assert os.path.isdir(REVIEW_DIR), "docs/skill-review/ home missing"


def test_template_ships():
    tmpl = os.path.join(ROOT, "templates", "skill-review.template.md")
    assert os.path.isfile(tmpl), "templates/skill-review.template.md missing"
    text = read("templates/skill-review.template.md")
    assert "SKILL-REVIEW" in text and "Verdict:" in text and "Skill:" in text


# --- behaviour: the three red-proofs the row names ---

def test_body_change_without_record_reds(self=None):
    """A skill BODY changed but no review record exists → the push reds."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1)
        _commit_all(tmp, "skill v1")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_BODY_CHANGED)
        _commit_all(tmp, "skill body changed, no review")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 1, r.stdout + r.stderr
        assert "FAIL (skill review)" in r.stdout
        assert "demo" in r.stdout


def test_version_stamp_only_does_not_red():
    """A pure version-frontmatter stamp (and its base-reference) is not a substantive change,
    so it owes no skill-creator review — the gate passes even with no record."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1)
        _commit_all(tmp, "skill v1")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_STAMP_ONLY)
        _commit_all(tmp, "version bump stamp only")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 0, r.stdout + r.stderr


def test_version_stamp_with_baseref_does_not_red():
    """The bump also rewrites the `live-spec-base (vX.Y.Z)` base reference; that line change is
    still a pure stamp and owes no review."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1_WITH_BASEREF)
        _commit_all(tmp, "skill v1")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_STAMP_ONLY_BASEREF)
        _commit_all(tmp, "version bump stamp + baseref")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 0, r.stdout + r.stderr


def test_body_change_with_matching_record_passes():
    """A substantive skill change WITH a committed, matching review record passes quiet."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1)
        _commit_all(tmp, "skill v1")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_BODY_CHANGED)
        _write(tmp, "docs/skill-review/2026-07-17-demo.md", RECORD)
        _commit_all(tmp, "skill body changed + its review, same commit")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 0, r.stdout + r.stderr


def test_stale_record_does_not_cover_a_later_change():
    """A review committed BEFORE the last skill change is stale — it does not cover a change
    made after it, exactly as the prover-record gate refuses a record older than its spec."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1)
        _write(tmp, "docs/skill-review/2026-07-17-demo.md", RECORD)
        _commit_all(tmp, "skill v1 + its review")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_BODY_CHANGED)
        _commit_all(tmp, "skill body changed again, review not refreshed")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 1, r.stdout + r.stderr
        assert "FAIL (skill review)" in r.stdout


def test_record_must_be_committed_not_untracked():
    """A review record sitting untracked in the working tree does not count — it must be
    committed, mirroring the prover-record gate's tracked-file rule."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1)
        _commit_all(tmp, "skill v1")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_BODY_CHANGED)
        _commit_all(tmp, "skill body changed, no review committed")
        _write(tmp, "docs/skill-review/2026-07-17-demo.md", RECORD)  # written, never committed
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 1, r.stdout + r.stderr


def test_no_skill_change_passes():
    """A push that touches no skill owes nothing — the gate stands down by name."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "PRODUCT_SPEC.md", "spec v1\n")
        _commit_all(tmp, "spec v1")
        base = _head(tmp)
        _write(tmp, "PRODUCT_SPEC.md", "spec v2 — a non-skill change\n")
        _commit_all(tmp, "spec v2")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 0, r.stdout + r.stderr


def test_record_missing_verdict_reds():
    """The record's minimal shape includes a Verdict line; a record naming the skill but
    carrying no verdict does not satisfy the gate."""
    with tempfile.TemporaryDirectory() as tmp:
        _init_repo(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_V1)
        _commit_all(tmp, "skill v1")
        base = _head(tmp)
        _write(tmp, "skills/demo/SKILL.md", SKILL_BODY_CHANGED)
        _write(tmp, "docs/skill-review/2026-07-17-demo.md",
               "# Skill review — demo\n\nSKILL-REVIEW\n\nSkill: demo\n\n(no verdict yet)\n")
        _commit_all(tmp, "skill body changed + a record with no verdict")
        r = _run([GATE], cwd=tmp, extra_env={"LIVE_SPEC_DIFF_BASE": base})
        assert r.returncode == 1, r.stdout + r.stderr


# --- wired into the push chain, both nets ---

def test_gate_wired_into_pre_push():
    assert "check-skill-review.sh" in read("guardrails/pre-push"), \
        "pre-push does not wire the skill-review gate"


def test_gate_mirrored_in_ci():
    assert "check-skill-review.sh" in read(".github/workflows/gates.yml"), \
        "the CI mirror does not run the skill-review gate"


def test_ci_mirror_carries_every_local_gate():
    """Gate-chain hygiene (folded into row 419): every local pre-push gate script is mirrored
    in CI. The drift this catches: gates p (touchpoint-kind) and q (board) were missing from
    gates.yml before this row synced them."""
    ci = read(".github/workflows/gates.yml")
    for script in ("check-touchpoint-kind.py", "check-board.py",
                   "check-authority-anchor.py", "check-skill-review.sh"):
        assert script in ci, "%s is in the local pre-push chain but not mirrored in CI" % script


# --- traceability across the four documents ---

def test_spec_states_the_law():
    spec = read("PRODUCT_SPEC.md")
    assert "[INV-208]" in spec
    assert "check-skill-review.sh" in spec
    assert "docs/skill-review" in spec


def test_formal_index_row():
    assert "| INV-208 |" in read("PRODUCT_SPEC.md")


def test_architecture_owns_the_invariant():
    arch = read("ARCHITECTURE.md")
    assert "INV-208" in arch
    assert "check-skill-review.sh" in arch


def test_matrix_row_covers_the_law():
    matrix = read("TEST_MATRIX.md")
    assert "M-389" in matrix
    assert "INV-208" in matrix

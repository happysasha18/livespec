# Skill-creator review records

This directory is the home for skill-creator review records. When a push substantively changes a
skill under `skills/`, the push gate `guardrails/check-skill-review.sh` (gate s, SPEC INV-208) reds
unless a committed record here covers that change. Alexander asked for the blocking gate on
2026-07-17 ~18:26: the session kept forgetting to run Anthropic's skill-creator review after a skill
edit, so the habit became a machine.

A pure version-frontmatter stamp — the `version:` line and the `live-spec-base (vX.Y.Z)` reference
that `scripts/stamp-versions.py` rewrites at every version bump — is not a substantive change and
owes no review; the gate exempts it by construction.

## A record's minimal shape

Save one file per landing that changed a skill, dated, named for the skill(s) it covers:
`docs/skill-review/YYYY-MM-DD-<skill>.md`. It carries, at minimum:

- a standalone `SKILL-REVIEW` marker line (the self-declaration shape the gate reads);
- a `Skill: <name>` line for each skill reviewed (the directory name under `skills/`);
- a `Verdict:` line carrying the skill-creator review's outcome.

Everything else — the findings, what was folded, what was rejected and why — is free prose beneath.
The template `templates/skill-review.template.md` is the starting form. The gate checks that a
committed record naming the changed skill, carrying the marker and a verdict, exists and is at least
as new as the skill's last change; a stale earlier review does not cover a later change.

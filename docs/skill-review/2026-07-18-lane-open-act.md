# Skill review — build-pipeline, live-spec-base (the lane-open act)

SKILL-REVIEW

Skill: build-pipeline
Skill: live-spec-base

Date: 2026-07-18
Reviewer: skill-creator (Anthropic)

Verdict: passes; both edits reviewed and folded — each states the lane-open act at the
altitude its skill owns, cites SPEC INV-214/INV-49, and adds no new triggering surface.

## What changed

- **build-pipeline** (Trains section): a new paragraph "Opening a lane is an act you PERFORM,
  not narration you emit (SPEC INV-214)" naming the performable steps (`scripts/open-lane.sh`,
  the staged flip, the cap refusal, the claim commit on main, the lane worktree, the worker
  delegation) and the recorded "serial by the graph" discipline; and the Trains intro
  de-hardcodes "three" to the profile-declared `lanes.cap`.
- **live-spec-base** (rule 7's lanes sub-rules + package-defaults table): a new sub-rule
  "The lane-open act"; the "three lanes under one pen" sub-rule re-homed to `lanes.cap`; and a
  new `lanes.cap` row in the package-defaults table (default 3, the owner's value in his profile).

## Findings

- **Altitude (folded, no change needed).** build-pipeline states the act operationally (the
  steps a session runs); live-spec-base states it as one of the numbered lane sub-rules and
  registers the setting in the defaults table. Neither restates the other at length — the
  operational walk lives once in build-pipeline, the setting lives once in the defaults table,
  and the spec (INV-214) is the normative home both cite. One home per fact holds.
- **Description/triggering (none).** No skill `description` frontmatter changed; the edits are
  body law, so the skills' trigger surfaces are untouched and no eval drift is expected.
- **No new coined names (folded).** "The lane-open act" names a mechanism in plain words; no
  metaphor or invented term introduced.
- **Version stamp:** no skill-version bump this landing (the pack stays 2.6.3); the changes are
  body law carried under the pack's existing version, and the record ships in the same commit.

# Skill evals — behaviour tests for the pack's own skills (SPEC E-19, ROADMAP row 94)

A skill is a promise about BEHAVIOUR, so its test is behavioural: a scenario where a session without the
skill demonstrably errs, and the same session with the skill corrects it — the skill's own red-first
test ("no skill without a failing test"). One file per working skill in this directory; the required set
derives from `skills/` itself (everything but the base rulebook), enforced by
`tests/test_traceability.py::test_skill_evals_present` — a fifth working skill is red until its eval
exists.

## How an eval file is shaped

Each `evals/<skill>.md` carries four sections, all mandatory (the suite checks them):

- **## Scenario** — the exact prompt, verbatim, both arms (bare and with-skill).
- **## Criteria** — the named behaviours the skill promises, one row each, scored per run:
  `MET BARE` (the bare run already did it) · `RED` (the bare run missed it) · `GREEN` (the with-skill
  run did it). The skill's proven value is the RED→GREEN rows, nothing else.
- **## The red** — plain words: what the bare run actually got wrong, with the dated run record.
- **## Re-run** — how to repeat both arms (worker tier, prompt source, where the record lands).

Run records are dated, append-only files in `docs/evals/` — a re-run adds a record, never rewrites one.
Evals re-run at milestones (the M-1 list carries the item) and at any landing that changes a skill's own
behaviour; a pin- or version-only sweep owes no re-run.

## The honest boundary — read before trusting any red

On a machine where the pack is installed, **there is no truly bare session**: the machine-global loader
(`~/.claude/CLAUDE.md`) and the personal profile feed the method into every agent that boots — the first
run (2026-07-05) proved it, when "bare" workers produced near-method output with zero tool uses. So a
red here is **bare-of-the-SKILL, not bare-of-the-loader**: it measures the skill's marginal value over
everything else the machine already teaches. Score per named criterion; a criterion the loader-fed bare
run already meets is recorded `MET BARE` — never claimed as the skill's win. A clean-machine red
(no pack installed) would be stronger; running one is a candidate for the CI mirror (row 14).

## Authoring rule — the scenario speaks like the human

A scenario states the wish the way its human states it ("clicking a photo opens it enlarged, with
arrows") and MAY place discoverable context nearby — but never enumerates the facets or failure modes in
the prompt. A prompt that lists "phones, two windows, files renamed externally" has already done the
skill's job and contaminates the red (first-run lesson: the spec-author scenario did exactly this, and
the bare run covered exactly those hints — recorded in its file). When a criterion needs context to be
discoverable, put it in the world (a repo file, a spec the scenario cites), not in the task sentence.

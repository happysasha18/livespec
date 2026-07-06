# Eval — product-prover (SPEC E-19)

## Scenario

Both arms review the same planted-hole spec; the with-skill arm first reads
`skills/product-prover/SKILL.md` and runs FULL mode. The spec under review (verbatim):

> # Track Player — spec
> The player plays a track with play/pause and a volume slider. The user can mute any of 4 stems
> (drums, bass, vocals, other); mute states persist in localStorage and restore on reload. The app has
> two views: Simple (play/pause and volume only) and Detailed (adds the 4 stems with mute buttons).
> Switching views is instant. Export: the user clicks "Export mix" — the app renders the current mix to
> a WAV in the background and shows a download link when ready.

Planted holes: view×persisted-mute composition (mute set in Detailed, invisible in Simple) · export
liveness (no failure/timeout) · export snapshot-vs-live race · localStorage across two windows ·
version-N-1 stored state.

## Criteria

| Criterion (the skill's promise) | bare | with-skill |
|---|---|---|
| Finds the view×persistence composition hole (the stranding bug) | MET BARE | GREEN (F2, must-fix, with the view-ladder reading recommended) |
| Finds the export liveness hole (no failure path) | MET BARE | GREEN (F6) |
| Severity triage: must-fix / should-clarify / worth-considering on every finding | RED — no severities; a reader can't sort blockers from musings | GREEN — every finding tagged |
| Four-part findings: headline · quoted source pin · operational consequence · concrete action | RED — flowing essay, no per-finding actions or pins | GREEN |
| The model extracted first + "What I assumed" stated | RED — assumptions implicit | GREEN — states/entities/actors + 5 named assumptions |
| Coverage tables (CRUD / invariants-per-state) or a named N/A | RED — absent | GREEN — tables + named authorization skip |
| Paste-ready properties for the author (Phase 5) | RED — prose advice only | GREEN — 5 paste-ready invariant sentences |
| Substance beyond the bare run | — | GREEN — found the end-of-track dead-end (F5) the bare run missed entirely |
| The run names its MODE aloud with the modes list intact — FULL here, CROSS-LINK for surface adds, FEATURE-FIT for one feature's intake delta (SPEC INV-29, added 2026-07-06) | RED (2026-07-06 push re-run) — no triage, no mode | GREEN (same re-run) — "Running FULL mode per the product-prover skill (v0.1.9)" |

## The red

The bare run (bare run: 2026-07-05, Sonnet worker, zero tool uses — record
`docs/evals/2026-07-05-first-run/bare-product-prover.md`) found most planted holes — strong substance,
loader-fed — but delivered them as an undifferentiated essay: no severities, no traceable four-part
findings, no stated assumptions, no coverage tables, no paste-ready sentences; an author reading it
cannot tell what blocks the build from what is a musing, and it missed the end-of-track dead-end. The
with-skill run (same day, record `with-skill-product-prover.md`) ran the full phase walk, tagged 11
findings by severity, stated its assumptions, and closed with five sentences the author can paste
straight into the spec — plus the F5 dead-end the bare run never saw.

## Re-run

One Sonnet worker per arm. Bare arm: the spec + "review this before we build; do not invoke any tools
or skills". With-skill arm: "First read skills/product-prover/SKILL.md and work strictly by it (FULL
mode)" + the same spec. Score per criterion; append the dated record to `docs/evals/`.

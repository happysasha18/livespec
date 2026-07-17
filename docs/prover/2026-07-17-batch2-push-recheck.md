# Prover — batch push re-check (2026-07-17, short form per INV-61)

A push re-check for a batch of five unpushed commits. No product delta of its own; this record re-runs the
full suite and the full push gate so the batch can leave the machine.

## The batch

Five commits stand ahead of origin/main (`git log --oneline c4511f2..HEAD`):

- `607d40a` row 408: the waiting list — everything waiting for his eyes has a home that outlives the scroll
- `df9a276` ROADMAP 415: a decision recorded as the person's names its exchange (INV-207)
- `8a0209f` ROADMAP 415 fix: invert the hollow authority gate — feed the read-back, reach the surfaces, strike the live fabrication
- `a730606` ROADMAP 419: a skill change reds until its skill-creator review is on record (INV-208)
- `46f39a5` ROADMAP 415 fix (follow-up): allowlist the per-name authority-anchor fixture

## Suite

Full run: 1248 passed, zero failures (`python3 -m pytest -q`).

## Row 415 was found hollow, then redesigned and fixed

`df9a276` first landed INV-207 and its record (docs/prover/2026-07-17-row415-authority-anchor.md) reported
its own sweep clean — "zero genuine unanchored attributions". A Fable adversarial review the same session
falsified that claim and two design choices under it:

- **The founding fabrication was standing live.** ROADMAP.md row 386's cell carried "His ranking, kept:
  this matters more than the communication layer, and it waits until the communication layer has run in
  the field" — the exact sentence Alexander struck on read-back as never said. The first sweep read a
  ROADMAP row as its unit and counted the row anchored if a date sat anywhere in the row, so a date
  elsewhere in the same giant cell let the unanchored sentence through.
- **The gate spared exactly the surfaces the incident used.** The first build scanned only declared
  DECISION-RECORD surfaces and named NEXT_STEPS.md and ROADMAP.md by name to spare them — the two surfaces
  where the fabrication actually lived.
- **The read-back had no feed.** `DECISIONS.md` existed as a surface but no skill instructed a session to
  write an anchored entry to it or to strike what the person never said; working sessions load skills, not
  PRODUCT_SPEC.md, so the rule was invisible where it needed to act.

The fix (`8a0209f`) struck the fabrication in ROADMAP row 386 and rewrote the cell in the pack's own voice
(no scheduling attributed to him — confirmed live at ROADMAP.md's row-386 cell), added the struck entry to
DECISIONS.md with its correction note, and inverted the gate: push mode now hard-blocks unanchored entries
on declared decision-record surfaces (deterministic, false-positive-free) and reports the churny surfaces
(NEXT_STEPS.md, ROADMAP.md) as an advisory sweep feeding the read-back, rather than sparing them. The
read-back is stated as the load-bearing defence — a text gate cannot tell a live fabrication from live
narration when both carry a plausible date; `DECISIONS.md`, read on Alexander's own clock, is where he
strikes what he never said. The rule itself now lives in two skills so a working session is actually
instructed to feed the read-back: `skills/live-spec-base/SKILL.md` (rule 13's authority-anchor arm) and
`skills/build-pipeline/SKILL.md` (the drafting-a-decision step), each carrying the anchor-or-pack-voice
split and the `DECISIONS.md` feed, with a skill-creator review record at
`docs/skill-review/2026-07-17-live-spec-base-build-pipeline.md` (gate s) — verified directly against the
committed diff and the gate s pre-push output, both of which name build-pipeline, not communicator; the
row 415 prover record's own correction section names `skills/communicator/SKILL.md` and a
`...-communicator.md` review file for this same arm, which does not match the committed tree and reads as
a stale reference to an earlier draft of the fix. This is a narrative slip in that record's prose, not a
gap in the shipped mechanism — the actual files, the actual gate, and the actual review record all agree
with each other and are what gate s checks.

Four record-surface evasions were closed red-first in the same fix: a typed "STRUCK" word no longer
silences a live bullet, a bullet under a note-region marker or above the first marker is scanned, a
fabrication written as a paragraph is scanned, and a legitimate multi-line entry no longer false-positives.
Each is fixture-backed under `guardrails/authority-anchor-fixtures/` and re-verified directly in this
re-check: `record-evasion-typed-struck.md`, `record-evasion-paragraph.md`, `record-evasion-note-region.md`,
and `record-evasion-above-marker.md` each exit non-zero (FAIL) against `check-authority-anchor.py`, as
they must. Full detail, including the scope tradeoff between a hard gate and the advisory sweep, lives in
docs/prover/2026-07-17-row415-authority-anchor.md's "Corrections after adversarial review 2026-07-17"
section.

## Rows 408 and 419 landed clean

Both prover records verdict HOLDS with zero must-fix and no adversarial corrections:
docs/prover/2026-07-17-row408-waiting-list.md and docs/prover/2026-07-17-row419-skill-review-gate.md.

## Gate result

`guardrails/pre-push` exits 0: all gates green, push allowed. Gate k (compaction freeze) read GREEN against
the existing local baseline with no drift — no re-freeze was needed for this batch. Gate r
(authority-anchor) is green by design: it reports advisory candidates on ROADMAP.md and NEXT_STEPS.md for
human sweep and hard-blocks only unanchored decision-record entries, none of which are unanchored on the
current tree. Gate s (skill review) confirms fresh review records for both build-pipeline and live-spec-base.

## Verdict

The batch is push-ready.

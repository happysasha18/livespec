# Skill review — feedback-intake (the receiving sweep fences the `.draft` mid-write deposit)

`SKILL-REVIEW`

Skill: feedback-intake (the inbox receiving-sweep discipline)
Date: 2026-07-21
Reviewer: skill-creator review method applied against the diff from a fresh read (live-spec-base v3.6.0)

Verdict: passes — an additive change to one existing sweep bullet, no frontmatter or description touched, so triggering is unaffected; the addition sits in the right home and matches the surrounding register.

## What changed

The inbox deposit protocol (INV-249) added the atomic-write discipline: a deposit is written under a `.draft` name and renamed to its final name only once complete. feedback-intake owns the receiving sweep, so its sweep bullet gained the fence: the sweep reads only a complete deposit, passes over a `.draft`-suffixed file a neighbour may still be writing (so it never harvests or removes a mid-write deposit), and reaps a `.draft` that is stale across a full sweep (unchanged modification time, its writer gone) the way it removes a harvested file, so an abandoned draft never lingers.

## Checks walked

- **Description / triggering:** unchanged — no frontmatter edit. The sweep is reached through the existing inbox-sweep flow, not a new trigger. Correct.
- **Home fit:** feedback-intake owns the inbox receiving sweep, so the sweep's `.draft`-skip and the stale-draft reap belong here. The write-side of the protocol (the `.draft`-then-rename how-to) correctly lives in inbox/README.md, and the mechanical gate agreement lives in guardrails/check-earned-message.py; this skill carries only the sweep's half. The split holds, one home per fact.
- **Register:** the addition obeys the pack's documentation register — plain words, positive sentences, no contrast-frame scissors, no leading internal code. The trailing anchor `(SPEC INV-249)` sits at the end.
- **Redundancy:** the sweep bullet does not restate the write-side protocol (that is the README's) nor the gate fence (that is the guardrail's); it states only what the sweep itself does with a `.draft` file.
- **Consistency:** the fence and the reap are consistent with the spec clause (INV-249) and the README protocol — a mid-write file is passed over, a stale orphan is reaped, a routed complete deposit is left earned in place (INV-247).

## Note

The adversarial correctness of the protocol as a whole (does `.draft`-then-rename actually close the race, does the gate agree with the sweep, is the collision law fenced) is judged by the fresh-context prover audit recorded under docs/prover/2026-07-21-inv249-inbox-deposit-protocol.md; this review covers the feedback-intake skill's own change — the sweep fence — for quality and home fit.

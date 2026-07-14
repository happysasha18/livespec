# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-14 — the whole queue cleared and pushed)
**PACK v1.3.0, PROVER v1.1.1** (rows 311-314 were skill-patch/rule changes, no pack bump). **Suite 659
green whole; all committed and pushed under Alexander's standing grant** (his 2026-07-14 word: push on
green when confident). Read this, then wipe memory; every landing's full story lives in JOURNAL + ROADMAP.

**What landed this batch.** The whole queue is done: rows 310-314, the cheap backlog (302, 307-309), and
inbox hygiene. Row 310 (the design-review pass, INV-141/142) shipped the prior movement. This batch closed
four more, each born of one of Alexander's mid-session steers:
- **Row 311** — better time estimates: wall-clock-with-parallelism + a cross-session обещал→вышло
  calibration log + a landing retrospective, homed in communicator's echo/report rules. communicator
  1.0.12→1.0.13. Commit `0667120`.
- **Row 312** — the README now states plainly there's no command surface to learn; the onboarding card
  turned out to be the wrong home (a settings card), so the README carries it. Commit `3e1dc62`.
- **Row 313** — one unified emoji done/remaining report format, communicator rule 9, reconciling two
  prior legends into one. communicator 1.0.11→1.0.12. Commit `79db54e`.
- **Row 314** — a brief-time disjoint-write-set check before a second concurrent writer spawns (the
  tlvphotos worker-collision gap), extending ACT-3/INV-11 — no new invariant. Independent opus prove.
  build-pipeline 1.0.25→1.0.26, live-spec-base 1.0.12→1.0.13 (base-pin ripple, all 8 skills). Commit
  `15fe3e0`.

## ⟨DECIDE⟩ — two taste-call defaults I set (overturn either if you meant otherwise)
1. **Scoped design review at every surface add** (vs milestone-only). The born-of miss arrived as a
   surface add, and the scoped form (the new surface's elements against the existing inventory) is cheap
   by construction — so I default to running it on every surface add rather than deferring to the next
   MINOR gate. Overturnable to milestone-only.
2. **The v1 echo channel holds exactly ONE producer** (the same-kind divergence). The design memo framed
   two producers; the independent prove showed the second — a "likely-missed edge" the running product
   reaches — is the INV-72/138 blank-answer class the existing lenses already treat as BLOCKING, which
   would collide with the never-blocks promise. So I narrowed v1 to one producer; a later producer earns
   its own clause and wish row. Overturnable if you want the wider channel now.

## Queue (take at a queue-take — all QUEUED, none blocking)
- **Row 261** — GitHub Issues as the strangers' wish door: still a DECIDE, awaiting Alexander's word.
- The one real remote deposit still owes its live run.
- The tlvphotos impersonal-voice wish sits in its own inbox.

## OWNER-HELD (needs your hand — no autonomous move taken)
- **`~/.claude/CLAUDE.md` says "its seven working skills"** — now stale (the pack is eight working +
  base, since row 310). This is a host-side file on your machine, outside this project's tree, so this
  window does NOT edit it — it is your one out-of-tree edit ("seven working skills" → "eight working
  skills").

## Standing habits (always-on)
- When a method skill changes, run a fresh-eyes adversarial pass (INV-46); a MILESTONE earns the deep
  Fable whole-spec + architecture pass. `date` before any stamp. Shipped docs stay impersonal
  (INV-118/120), provenance in JOURNAL. Delegation by base rule 5 → INV-69; the lead dispatches its
  discovery reads (base rule 25 → INV-137). Public READMEs edited ONLY via a fresh clean-context agent
  (bilingual safety).
- No self-certification (INV-94) · plain words, codes trail (INV-28) · say-what-it-is, no contrast frames
  · inbox swept first · one lane one commit · a delegated run's verdict is the suite log's tail (INV-80).
- Next free codes: read the live Formal index before minting (INV-142 consumed; codes consume in landing
  order, reservations dead).

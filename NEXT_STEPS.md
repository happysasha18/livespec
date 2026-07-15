# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 ~21:20 — 1.10.1 LANDED on green (push on green); queue drained to one idea; suite 800; pack v1.10.1)
**PACK v1.10.1** (PATCH) — INV-100 / INV-157 sharpened (ROADMAP 333): the harness launch sweep now clears
its own stale TEMP litter by prefix + age (an old ownerless dir a killed run left before recording an
owner; a young one left alone), because the system temp is not self-purging on macOS — the harness owns
its litter across runs; a temp glut is surfaced loudly. Born of a real 78 GB `$TMPDIR` leak that read as
product reds. Red-proven, short-form [INV-61].
**PACK v1.10.0** — INV-162 (ROADMAP 334, HIGH safety): a cleanup acts only on what THIS run provably owns
and never a shared resource in current use; a kill targets uniquely by owned identity or install path,
never a broad name pattern reaching the human's own program. Born of a real incident — a broad `pkill
chrome` closed Alexander's real browser (base rule 17). Net: guardrail `check-broad-kill.sh` in the push
gate (CI gate j + local) + worker-briefing; the MINOR-gate prover found five net evasions, all folded.
Unifies browser + orphan reap (330/331) + temp sweep (333). Records under `docs/prover/2026-07-15-334-*`.

### PRIOR (history in JOURNAL): 1.9.0 feedback-collector, the pack's third arrow (321) · 1.8.0 forward-binding law → one home + test-infrastructure family → a class + harness net hardened (322/326/328/329/330/331) · 1.7.0 the pack owns the browser harness (327).

## Queue (ROADMAP)
- **332** (idea, not a build) Lift the ship-the-shape / host-owns-the-instance split to its own invariant —
  minimal half landed in E-26 (329); formalizing optional, surface only if a third site re-derives it or he asks.

## Standing habits / OWNER-HELD
- **Memory can be wiped** — the whole story is in JOURNAL + the prover/design-review records + ROADMAP.
- Version bumps are NOT owner-reserved (Alexander confirmed 2026-07-15): cut them on green; standing push
  authorization holds. The deep independent audit runs by default as quality, not on his word.
- On a failure: the root/infrastructure fix first, never a blind retry or a pointwise patch [INV-155 kin].
- **Pushing depends on the session's permission mode.** Under the global `bypassPermissions` a plain
  `git push` to an existing repo runs free (v1.6.1 pushed with no block, 2026-07-15). Only the narrow set of
  truly-dangerous outward acts stays hard-blocked above bypass — `gh repo create`, force-push of rewritten
  history, self-editing settings.json (the agent's one hard boundary). A session launched in a stricter mode
  than the global default may still hold an ordinary push for an explicit go.
- Next free codes: INV-163, M-312, E-31, T-22 (334 used INV-162 + M-311).

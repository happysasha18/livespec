# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 ~20:55 — 1.10.0 READY (green, prover running; push on green); a cleanup touches only what it owns — INV-162, HIGH safety; suite 795; pack v1.10.0)
**PACK v1.10.0** — INV-162 (ROADMAP 334, HIGH safety): a cleanup acts only on what THIS run provably owns
and never a shared resource in current use by another party — the class is any shared resource (process ·
temp dir · port · file · lock · display), the test is current use (a knowable live PID / recorded owner /
install path / lock is checked before touching). A kill targets uniquely by owned identity or install path
(`~/.cache/puppeteer/...`), never a broad name pattern reaching the human's own program (bare `chrome` /
`chrome_crashpad_handler` forbidden). Born of a real incident — a broad `pkill chrome` closed Alexander's
real browser (base rule 17). Unifies the browser + orphan reap (330/331) + temp sweep (333). Net: a new
guardrail `check-broad-kill.sh` in the push gate + worker-briefing; red-proven. Prover pass in flight
(`docs/prover/2026-07-15-334-cleanup-ownership.md`).

### PRIOR (history in JOURNAL): 1.9.0 feedback-collector, the pack's third arrow (321) · 1.8.0 forward-binding law → one home + test-infrastructure family → a class + harness net hardened (322/326/328/329/330/331) · 1.7.0 the pack owns the browser harness (327).

## Queue (ROADMAP)
- **333** (take next) The temp-hygiene law has a false macOS non-goal ($TMPDIR is not self-purging) and temp cleanup is
  skipped on a killed run — a 78GB leak read as product reds. Kill INV-100's false non-goal; unconditional
  temp cleanup; a retroactive startup sweep every launch by prefix+age (Alexander: the primary defense,
  self-maintaining, kill-surviving); a full-temp warning. Then consumers adopt by update [INV-158].
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

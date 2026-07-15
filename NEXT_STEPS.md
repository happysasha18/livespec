# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 ~20:05 — 1.9.0 READY (green, prover folded, audit ran; push on green); the pack grows a third arrow — feedback-collector; suite 789; pack v1.9.0)
**PACK v1.9.0** — a MINOR adding a NEW node/sub-skill **feedback-collector** (ROADMAP 321), the pack's
outbound feedback arm. On a rare genuinely-strong reaction with the host's `feedback-upstream` flag on,
the pack OFFERS (positive consent every time, the deliberate opposite of silence-is-consent) to draft a
distilled non-public "upstream note" to the pack's authors and deposit it in the gitignored `outbox/`; it
never sends — delivery is the human's own step. Off by default; a downstream host opts in, the authors'
origin machine stays off. Distinct from feedback-intake (the inverse arrow) and the measurement family.
Alexander approved the taste sample before the full build. Cross-link prover folded five blocking defects
(undeclared outbox home, false non-overlap with intake, unmechanized origin-machine promise, a mis-cite,
the offer-record schema); a fresh-eyes audit ran. Record `docs/prover/2026-07-15-321-feedback-collector.md`.

### PRIOR: 1.8.0 (forward-binding law → one home, test-infrastructure family → a class, harness net hardened; ROADMAP 322/326/328/329/330/331; records under docs/prover/2026-07-15-1.8.0-minor-gate.md + design-review + audit).
**PACK v1.8.0** — a MINOR that cleared the whole open queue from the 1.7.0 gate plus older debt. INV-159
states the forward-binding law once in its own text and every "binds forward" cite is repointed at it off
the silent roots (INV-15 / T-16-kin / A-3 / INV-21-kin), held by a standing net that reds on any uncited
"binds forward" — the net caught a stray (INV-43) the hand-repoint missed (322). INV-160 declares the
suite-honesty / test-infrastructure family (INV-77/78/79/80/100/102/155/157/158) one class with a stated
net-parity, INV-77 the boundary member (328). The shipped harness template gained a cross-workspace launch
sweep, respects a host's SIG_IGN, and ships a by-deed orphan net (`orphan_guard`/`surviving_orphans`)
scoped to the process's own launches (330/331); CI on the Node-24 action majors (326); E-26 states the
scanner's per-project split and cites the family it joins (329). The MINOR gate ran three adversarial
passes as workers — a full prover (HOLDS-WITH-FIXES), a design review, an independent code+spec audit —
catching what green missed: INV-159's body claimed absent cites (blocking, folded), the orphan net's
sibling-process false-red (folded by process-scope), INV-160's parity casting INV-77's manual row as a
run net (folded). Records: `docs/prover/2026-07-15-1.8.0-minor-gate.md`,
`docs/design-review/2026-07-15-1.8.0.md`, `docs/audit/2026-07-15-1.8.0-audit.md`.

## Queue (ROADMAP)
- **334** (HIGH — safety, reaches outside git; take next) A cleanup kill/removal must never destroy a
  SHARED resource in current use by another party. Born of a real incident: a test-cleanup's broad `pkill`
  (`chrome`, `chrome_crashpad_handler`) closed Alexander's REAL browser mid-session. The general law
  (his framing): a cleanup removes/kills only what THIS run provably created and owns, and never a shared
  resource (process · temp dir · port · file · lock · display) in current use — where ownership/use is
  KNOWABLE (a live PID, a recorded owner, an install path, a lock), check it first. Unifies 334 (browser) +
  330/331 (orphans) + 333 (temp dir); the harness already embodies it via owner-pid liveness. State it in the
  harness law + worker-briefing guidance + base rule 17; a guardrail reds a forbidden broad kill pattern.
- **333** The temp-hygiene law has a false macOS non-goal ($TMPDIR is not self-purging) and temp cleanup is
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
- Next free codes: INV-162, M-311, E-31, T-22 (321 used E-30/T-21/INV-161 + M-308/309/310).

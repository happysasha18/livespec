# Prover record — the seven small design holes (rows 173-179), SHORT-FORM

Date: 2026-07-09 (session 29, the 1.0 RUN item 3). Mode: SHORT-FORM (INV-61 — small prose/skill delta,
no new surface, no new anchor; each edit clarifies an EXISTING invariant). These rows discharge findings
F4–F10 raised by the full re-prove `docs/prover/2026-07-09-full-reprove-session29-body.md`; this record
confirms each clause now stands and opens no new hole.

## Previous records clean
The full re-prove's folds (F1–F3) landed; F4–F10 were queued as rows 173-179 and are closed here. No other
unfolded prover row is outstanding.

## The delta, one line per hole
- **173 (F5)** — the milestone gate (M-1) now re-scans every deferred queue row's revisit trigger; a fired
  trigger returns the row to the runnable queue [INV-1]. Home: the rhythm's milestone-gate list.
- **174 (F6)** — T-9 criterion 6: on resume a parked feature re-fences and re-proves its delta against the
  now-committed truth, the way INV-39's later lane does; never integrated blind. Postcondition updated.
- **175 (F7)** — a milestone gate is one indivisible pen-stage; a bug arriving mid-gate waits for it to
  finish rather than preempting a half-run audit, then takes the pen the moment the milestone lands. The
  one exception to "a bug cuts at the end of the current pen-stage" [T-9, T-18].
- **176 (F8)** — the milestone-hold state is named distinctly: **held-for-milestone**, quiesced at a clean
  checkpoint like a park but named apart from bug-**parked** because nothing failed; resumes in landing
  order once the milestone lands [T-18].
- **177 (F9)** — the lane-claim back-off tie-breaker: "later" is a total order — git ancestry (descendant
  backs off), and on a genuine concurrent claim the lower inbox session token breaks the tie; exactly one
  backs off, mutual back-off impossible [INV-11].
- **178 (F10)** — the tight rung states the rollback: a batch-end red bisects to the culprit, reverts the
  batch to its last green base, re-applies the clean landings, and holds the culprit out for its fix — HEAD
  never sits red across a breakpoint [M-6].
- **179 (F4)** — ARCHITECTURE prose fixed: INV-67 now reads as communicator's own (the showing channel
  matches the seat), the INV-24 chat-arm wiring note kept separate; the mechanical owns-every-anchor-once
  check stays green (INV-67's token was already in communicator's cell).

## New-hole check
No new anchor introduced; every clause references an existing one (INV-1, INV-39, T-9, T-18, INV-11, M-6).
The owns-every-anchor-once and matrix-coverage checks stay green. Each clause carries a string-level test
(`TestSmallDesignHoles`). No cross-section seam opened.

Verdict: FOLD — all seven closed, no must-fix, no new finding. Suite 213 → 220 green.

# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 ~17:40 — 1.7.0 READY (committed; push on green); the pack owns the browser test harness; suite 773; pack v1.7.0)
**PACK v1.7.0** — a MINOR: the pack now ships a canonical headless-browser test harness and states the
rule for it (INV-157/158, ROADMAP 327). A browser test run launches muted (no sound on the machine) and
cleans up after itself — an unconditional whole-group reap on teardown plus a boot-aware launch sweep of
its own crash leftovers — and a consumer adopts the one shipped template `templates/headless_harness.py`
by updating the pack rather than maintaining a private copy. The MINOR gate ran three adversarial passes
(full prover HOLDS-WITH-FIXES, design review, Fable code audit) that caught five real defects a green
suite missed — a teardown reap skipped on a killed run, a net satisfiable by a docstring, a launch sweep
unsafe across a reboot — all folded; four recommendations queued (328–331). Records:
`docs/prover/2026-07-15-1.7.0-minor-gate.md`, `docs/design-review/2026-07-15-1.7.0.md`,
`docs/audit/2026-07-15-1.7.0-fable.md`. Also reconciled the ROADMAP status drift: 323/324/325 flipped to
landed with delegation lines, 322 marked partial, the queue's misnumbered "325" corrected to 322.

## Queue (ROADMAP)
- **321** feedback-collector sub-skill — on strong user emotion, OFFER (consent first) to send a distilled
  digest upstream; inbox destination, per-machine opt-out, distinct from feedback-intake. Open design Qs at
  build (Alexander 2026-07-15, "как дойдём добавим").
- **322** Give the forward-binding law a dedicated invariant and repoint every cite (the real unification;
  this item was misnumbered 325 before). The property — a duty binds forward from the first landing after
  its clause exists, never retroactively — is stated loosely across INV-15/41/74/75/127, T-16, A-3, INV-21,
  and line 626, and no anchor's text STATES it. Mint the invariant, repoint the cites. Prover F1/F5, record
  `docs/prover/2026-07-15-322-forward-binding-and-323-review-record-class.md`. Stopgap: INV-41 deflated to a
  precedent cite.
- **326** Bump the CI actions off the deprecated Node-20 runner (a cosmetic warning).
- **328** Declare the test-infrastructure invariant family a same-kind class with net-parity (design-review rec).
- **329** Reconcile INV-158's one-home with E-26's per-project removal scanner (design-review rec).
- **330** Ship the consumer's by-deed orphan-check helper in the harness's canonical home (Fable F7).
- **331** Harness sweep + signal edge hardening — cross-workspace sweep, respect a host's SIG_IGN (Fable F5/F8).

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
- Next free codes: INV-159, M-306 (INV-157/158 + M-304/305 used by 327).

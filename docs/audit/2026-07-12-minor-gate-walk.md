<!-- Promoted from .live-spec/checkpoints/pending-audit-minor-gate.md (source, 2026-07-12) -->

# 1.1.0 MINOR-gate audit — two passes, one record (2026-07-12, Opus auditor)

Context read at audit time: HEAD `93cf950`, tree clean, pack VERSION 1.0.31, SPEC v1.0.23.
Suite re-run fresh this audit: **422 passed in 36.44s** (`python3 -m pytest -q`). CI on 93cf950
(gates workflow, `gh run list`): **success**. This is a read-only audit; it writes only this file.

---

## Item 1 — the MINOR gate list (M-1)

The pack's MINOR-version gate is the milestone gate **M-1**, stated in PRODUCT_SPEC.md lines
694-706 ("Milestone (minor gate): a milestone runs the full gate"). Live-spec's own push gate
**M-6** (lines 732-736) adds a fresh whole-spec prover record before the push. Verdict vocabulary:
**MET** = satisfied now, with evidence; **OWED** = a bump-time action the gate performs, machinery
present and green, nothing blocking it; **FLAG** = a finding for the owner's eye.

| # | Gate step | Verdict | Evidence |
|---|---|---|---|
| 1 | Full spec re-prove | OWED | Machinery present: product-prover skill + M-6 record law + docs/prover/ (latest records per-row, 2026-07-12). The 1.1.0 whole-spec pass is not yet on disk. NEXT_STEPS re-arms it (a lens grew this session). Runs at the bump; its record is also the M-6 push requirement. |
| 2 | Matrix audit (E-15) | MET | tests/test_traceability.py + guardrails/check-matrix-coverage.sh, green inside the 422. |
| 3 | Surface-composition check | OWED | Machinery present (product-prover surface lens). Prior milestone walked 14 surfaces / 27 pairs. The walk runs at the bump. |
| 4 | Re-run skill evals (E-19) | MET (present) / OWED (re-run) | evals/ holds 7 scenarios, one per working skill: build-pipeline, communicator, feedback-intake, product-prover, publish, spec-author, test-author. live-spec-base is the rulebook and owes no eval. Re-run runs at the bump. |
| 5 | Skill-creator sweep | OWED | skill-creator installed. Row 219 makes it standing per skill-kind landing; the milestone sweeps all skills. Runs at the bump. |
| 6 | Doc compaction (E-24) | MET (docs) / OWED (code) | tests/test_suite_hygiene.py + INV-13 restatement prune + queue archive (INV-1), green. NEW at 1.1.0: code compaction (rows 260a/260b) runs its first pass at this audit. |
| 7 | Re-list open human gates + unharvested inbox | MET (done below) | Listed in this record. |
| 8 | Re-scan deferred queue revisit triggers | OWED | ~10 deferred rows carry triggers; the re-scan runs at the bump. |
| 9 | Re-check formal index vs prose | MET | tests/test_formal_index.py, green. |
| 10 | Re-pin derived docs' headers to spec version + prove | MET (mechanical) / FLAG | guardrails/check-pin-drift.sh + test_guardrails.py, green. FLAG: the visible header version strings read old against SPEC v1.0.23 — ARCHITECTURE.md reads v0.3.0 (2026-07-09), TEST_MATRIX.md reads v0.1 (2026-07-05, "derived from SPEC v0.7.1"). The re-pin step should reconcile the header convention or confirm the old strings are intentional. |
| 11 | Thin loader stays thin (E-16) | MET (walked) / FLAG | ~/.claude/CLAUDE.md is **24 lines**. Bootstrap lines hold the test "must this hold before any pack file loads" — the which-project disambiguation, the profile pointer, the pack pointer. FLAG: the OPUS-orchestrator model-seat detail and the three-window enumeration read as host-profile data rather than must-hold bootstrap; migration candidates, non-blocking. This is INV-108's named "1.1.0 audit's once-read walk, its first sweep." |
| M-6 | Live-spec push gate: fresh whole-spec prover record in docs/prover/ before the 1.1.0 push | OWED | Same record as step 1; must land before the push. |

### Open human gates (step 7 output)
- Row 231a — the version-alignment moments beyond MAJOR (minors? never? on his word) — waits his word.
- Row 231 / F5 — CI branch protection = his one GitHub click (also convergence lock F5, Item 2).
- Rows 191/193 picks; D-6/D-7; row 238.
- Prover-freshness midnight-rollover ledger entry — recommended AGREED NON-PROBLEM, his word owed.
- INV-24 homing observation (shopfront prose dates ride the stale-claim net) — one-sentence candidate.
- The 1.1.0 bump itself — his named gate. Standing grant (~00:35): audit clean ⇒ bump 1.1.0 and push.

### Unharvested inbox (step 7 output)
- inbox/2026-07-12-from-track-coach-derive-from-architecture-before-offering-a-fork.md — one file, unharvested.

**Item 1 — verdict.** The gate machinery is present and the tree is green (422/422, CI success on
93cf950). No step is blocked. Five steps are satisfied now (matrix audit, formal-index check,
pin-drift, the open-gate/inbox re-list, the thin-loader walk). Six are the gate's own bump-time
actions with machinery present and green (full prover pass + its M-6 record, surface composition,
eval re-run, skill-creator sweep, doc+code compaction, deferred-trigger re-scan). Two FLAGs carry
to the owner: the derived-doc header version strings read old (step 10), and one thin-loader line
is a migration candidate (step 11). Neither FLAG blocks. **CLEAN to proceed; the bump-time actions
still run at the bump.**

---

## Item 2 — the convergence pass (ROADMAP row 217)

Row 217 defines a narrower concrete pass than a free walk, and I ran that concrete pass. Its ask:
enumerate every convergence lock the pack claims, and confirm each is held by a test that proves it
cannot silently regress. Its Done-when has three clauses — the lock inventory is written; every
listed lock has its holding test (each new one red-proven); the M-1 audit's list names the
convergence pass.

The pre-1.0 milestone (docs/prover/2026-07-10-m1-audit.md, angle 4) enumerated **13 locks**: 8
already test-held, 3 fixed to test-held during that audit (M-214 norm fingerprints, M-215 lint
pattern floor, M-216 debt ratchet), 2 left attention-held (F4, F5). State now at 1.1.0:

| Convergence lock | Held by | Verdict |
|---|---|---|
| Frozen norms match a content fingerprint | test_convergence_locks.test_norm_fingerprints; scripts/norms-manifest.json (2 norms) | HELD, green |
| A norm-pointered surface owes a conformance row | test_norm_conformance_law.py (row 216) | HELD, green |
| The register lint's pattern set only grows | test_convergence_locks.test_register_lint_pattern_floor; register-lint-floor.json min_patterns 23 (above the 17 floor) | HELD, green |
| The prose-debt caps ratchet downward only | test_convergence_locks.test_debt_cap_only_downward; spec-debt-cap.json {max_waivers:0, max_redundancy_open:0} | HELD, green |
| An expired waiver reverts to a hard error | test_prose_gate.py TestWaiverMechanism.test_expired_waiver_does_not_match | HELD, green |
| Version pins (skill pins, derived-doc pins) do not drift | guardrails/check-pin-drift.sh + test_guardrails.py | HELD, green |
| Anchor + punctuation multiset survives a restructure/merge | INV-92/111/114; test_restructure_merge_gate.py, test_catchup_walk.py | HELD on invoke (see F4) |
| Traceability anchors + no-silent-drop of open legs | test_traceability.py, test_no_silent_drop.py | HELD, green |

**Two carried-forward gaps (the same two from 1.0, accepted then as post-1.0 rows):**
- **F4 — the standing anchor guard.** The anchor/punctuation multiset check fires only when a
  restructure, merge, or adopt walk invokes it (INV-92/111/114). It is not a standing guard on
  every edit. Row 231(b) holds F4 as its own future row, still unopened. No regression; the
  on-invoke check is green.
- **F5 — CI branch protection.** The guardrails live in the local pre-push hook. A push that
  bypasses the local hook is caught only when the remote gate is enforced by branch protection,
  which is the owner's one GitHub click. Row 231(b) holds F5 as his click, still pending. The CI
  mirror (M-5) runs and is green on 93cf950; the protection that makes it unbypassable is the open
  item.

**Row 217 Done-when against the tree:**
1. "the lock inventory is written" — **PARTIAL.** The 13-lock enumeration was written into a
   transient worker scratchpad at the 1.0 audit and is gone. The durable record captured counts and
   dispositions, not a standing named list. No durable lock-inventory doc exists. GAP.
2. "every listed lock has its holding test" — **11/13.** F4 has no standing-guard test; F5 is a
   GitHub config, not a test. Both were accepted as post-1.0 deferrals.
3. "the M-1 audit's list names the convergence pass" — **UNMET.** PRODUCT_SPEC.md lines 694-706
   list eleven gate steps and none names a convergence pass. INV-98 and INV-108 reference rows
   216/217, and NEXT_STEPS folds the pass into the 1.1.0 audit, but the gate enumeration itself
   omits it. GAP.

Row 217 therefore stays "queued", consistent with its ROADMAP status. Closing it at 1.1.0 needs
three doc edits outside this audit's write scope: a durable lock-inventory doc; the two open-lock
tests, or a recorded acceptance of F4/F5 as standing deferrals; and a one-line addition to the M-1
gate list naming the convergence pass.

**Item 2 — verdict.** Every test-held lock is green; nothing that was locked has regressed. Eleven
of thirteen locks hold by test. Two remain attention/human-held (F4 standing anchor guard, F5 CI
branch protection), both carried from 1.0 as accepted deferrals. Row 217's own Done-when is unmet
on two clauses (no durable lock inventory, the gate list does not name the pass). **GAPS: F4, F5,
the durable lock inventory, and naming the pass in the M-1 gate list.**

---

## Blocking assessment for the 1.1.0 bump

Nothing in the tree blocks the bump. The suite is 422/422 green, CI is green on 93cf950, and no
locked level has regressed. Two kinds of work remain. First, the gate's own bump-time actions (full
prover pass with its M-6 record, surface composition, eval re-run, skill-creator sweep, doc+code
compaction, deferred-trigger re-scan) still run at the bump. Second, four convergence gaps stay
open (F4, F5, the durable lock inventory, naming the pass in the gate list); F5 is the owner's
GitHub click, and the four together keep row 217 from closing. None is a red suite or a regressed
lock. The owner can bump 1.1.0 on his standing grant once the bump-time actions run clean, and
decide separately whether row 217 closes at this milestone or carries forward.

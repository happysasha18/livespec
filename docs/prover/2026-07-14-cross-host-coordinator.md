# Prover record — the cross-host duplicate coordinator (INV-149, M-291)

Date: 2026-07-14. Mode: CROSS-LINK (a surface add — a new invariant against the named monitor
family INV-146/147/148 and the cross-cutting laws INV-1, INV-67, INV-117). Author's pass, then an
independent fresh-eyes audit (INV-46) whose findings and folds are the second table below.

## What was reviewed

The new INV-149 body clause and Formal-index row in PRODUCT_SPEC.md, the updated INV-147 clause
(the cross-host gap it deferred now closes), the M-291 matrix row, the M-291 tests, and the
implementation in `scripts/stranger-wish-monitor.py` (claim_body, parse_claims, claim_winner,
_claim, the run() claim parameter).

## Findings and folds

| # | Finding | Severity | Fold |
|---|---|---|---|
| 1 | A claim comment bumps the source item's activity generation (updatedAt). If a claim registered as a surfaced-generation record it would falsely advance INV-146's re-surface generation and hide genuine new activity. | must-fix | Folded: the claim marker (`CLAIM_MARKER`) is a distinct substring from the surfaced-generation marker (`SURFACED_MARKER`), so `_surfaced_gen_from_comments` never reads a claim as a confirm. Stated in the spec clause and pinned by a matrix never-side and `test_claim_marker_never_reads_as_surfaced`. |
| 2 | The spec said "host identity [INV-117]", implying an identity stable across a host's runs. The arbitration needs only that two hosts contending for one item differ within one round; the package-repo Action's hostname changes per run, which would read as an over-claim. | must-fix | Folded: the spec now states the arbitration asks only that two contending hosts carry different identities, needing none stable beyond the round; `_host_id` documents the same. |
| 3 | Liveness on a dead winner: a winner that claims then dies before recording the surfacing must not swallow the wish. | verified | Holds: `claim_winner` filters a claim older than `LOCK_STALE_SECONDS` (the same stale bound the per-host lock uses), so a surviving host wins past the abandoned claim and surfaces the wish (INV-1). Pinned by `test_stale_claim_stolen_by_age`. |
| 4 | Exactly-once rests on the comment store's ordering (read-your-writes plus a total comment order). A simultaneity finer than that ordering could let two claims each read itself as first. | bound stated | The residual is the duplicate INV-147 already bounds — a duplicate the maintainers drop while the wish stays safe (INV-1) — now the rare pathological overlap where before it was every overlap. Stated honestly in the spec clause. |
| 5 | Honest failure (INV-67): `_claim` must stand down rather than risk a duplicate or a silent drop when it cannot post the claim or read it back. | verified | `_claim` returns False (stand down, retry next run) on a failed post and on a failed read-back; `run` logs the stand-down and does not count the item surfaced. |

## Open recommendations (not blocking)

- The claim uses a post-then-read primitive (an atomic claim over a medium with no compare-and-swap),
  so a losing host leaves a claim comment on a contended round. This is the cost of atomicity over
  GitHub comments; contention is rare (two hosts, one item, one window) and self-heals to one claim
  plus one surfaced-generation record in steady state. A taste call surfaced to the human, not a defect.

## Independent audit (INV-46) — findings and folds

A fresh-context adversarial read on the primary sources, opening hypothesis "tasks completed, goal
missed." It caught one correctness bug the author's own tests missed.

| # | Finding | Severity | Fold |
|---|---|---|---|
| A1 | A losing host's claim comment bumps the source item's activity generation (updatedAt) past the winner's surfaced-generation record. Measured against the confirm alone, the next run reads the trailing claim as fresh activity and re-surfaces — a duplicate inbox file plus a re-surface loop every run in the two-host contended case, defeating exactly-once (INV-1 wish-safety still held). Untested: every test set activity_gen by hand and none simulated a claim mutating updatedAt. | must-fix | Folded: `items_to_surface` now measures activity against the newest of ANY monitor marker — a claim OR a confirm (`_marker_ceiling_from_comments`) — so a trailing claim advances the baseline in lockstep with the activity it adds and reads as no new activity, while a genuine edit, reopen, or stranger comment (which bumps updatedAt without a marker) still rises above every marker and re-surfaces. Stated in the spec clause, pinned by `test_trailing_claim_does_not_reloop_surfacing` and `test_marker_ceiling_counts_claims_and_confirms`. |
| A2 | The spec's safety argument named only "a simultaneity finer than the comment store's ordering" as the residual, leaving A1's behaviour untraced. | must-fix | Folded with A1: the spec now traces the claim's effect on activity explicitly (the post-marker reasoning extended to the claim). |
| A3 | `claim_winner` reads the live set against the stale bound with each host's own clock, so a claim aged near the bound can fall on either side for two hosts a moment apart, breaking the "identical winner" claim. | should | Folded honestly in the spec: the winner is identical among the claims both hosts read as live; the stale bound is an hour where a contended claim is seconds old, so this touches only the dead-winner edge, the same steal-by-age tolerance the per-host lock carries, and the resulting duplicate is the bounded backstop (INV-1). |
| A4 | `_claim` returned False identically for a lost race and for a failed post/read, so `run` logged "another host holds the winning claim" even when the real cause was a missing write scope — a lone host could stand down every run behind a misleading log. | should | Folded: `_claim` now logs the honest cause on a failed post or read-back, and `run`'s stand-down line states the outcome (did not hold the winning claim this round) rather than asserting another host's claim. |
| A5 | The docstring's "single-host behaviour is unchanged" was true only for the injected `claim=None` path; production `main` always coordinates, so a lone host posts a claim per surfacing. | should | Folded: the docstring now states `claim=None` is the un-coordinated path the pre-INV-149 tests exercise, and production always claims (a lone host wins its own claim, at one comment per surfacing). |
| A6 | `_iso_to_epoch` returning None silently drops a claim; a host whose own claim timestamp failed to parse would stand down forever (a latent liveness hole). | nit | Kept as defensive: GitHub createdAt is well-formed ISO-8601-Z, so this cannot fire in practice; noted here rather than adding machinery for an impossible input. |

## Cross-cutting law lines

INV-1 (no wish lost): honoured — a dead winner delays by the stale bound and the survivor surfaces;
even the residual simultaneity surfaces twice rather than zero. INV-67 (honest failure): honoured —
an unreachable item stands down and retries, dropping no wish silently. INV-117 (host identity):
reused, no second identity scheme. INV-146/147/148 (the monitor family): the claim rides the existing
Issue/Discussion write, asks no new grant, and the workflow is unchanged.

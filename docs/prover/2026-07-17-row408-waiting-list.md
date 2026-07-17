# Prover record — ROADMAP 408: everything waiting for his eyes has a home that outlives the scroll

Date: 2026-07-17 · Doc version: v2.6.3 (unchanged; the version bumps once at the movement's MINOR gate) ·
Form: SHORT (small delta — infra kind, single-module on the guardrails node, one new gate + one new board
surface, no new node) · Mode: CROSS-LINK on the changed clause against its neighbours [INV-205, INV-204,
base rule 10, ROADMAP 382], with the architecture lens on the one-line owns-list edit.

## Previous records clean

The prior record (docs/prover/2026-07-17-row417-cleanup-notice-and-inversions.md) closed with zero
unfolded rows after its adversarial-review corrections. No open finding carried into this landing.

## The delta in one line

INV-206 states the waiting list: the board `WAITING.md` at the host root holds parked questions and
unseen answers, an item clears on his acknowledgement alone (never auto-expired), the shown set is
bounded at twelve while the list and attic are unbounded, and the gate `guardrails/check-board.py` reds
a closing report omitting a still-open item, a demotion with no matching line (the silent loss his
2026-07-17 ~15:57 correction forbids), or an over-cap shown set.

## Cross-link checks

- **Consumes the frame, does not re-open it [INV-205].** The waiting-list touchpoint already declared its
  kind (asynchronous, person-opened). This landing only filled its `surface` field from null to
  `WAITING.md` — the documented lifecycle for a [target] surface once built. `check-touchpoint-kind.py`
  now scans the board and stays green: the board carries only the wait and teach markers a person-opened
  asynchronous point affords, and no interrupt. PASS.
- **Base rule 10 honoured.** Nothing on the board is silently deleted: a demoted item stays alive on the
  list, and a cleared or superseded item moves to the board's attic region with a manifest line. The
  gate's silent-loss red is the mechanical enforcement of the rule the first design broke. PASS.
- **Status habit consistent with ROADMAP 382.** The clause states his status answer prints what is in
  front of him plus one line naming the list — its count and that it opens on request — the same
  one-line-offer shape row 382 gives the far tier. No conflict; row 382 is not built here. PASS.
- **Architecture lens (six checks) on the owns-list edit.** INV-206's anchor lands on exactly one node
  (guardrails), pinned to `check-board.py:1` and `WAITING.md:1` (traceability suite green). No new node,
  no new seam (the board is a file read by the gate, an internal read, not a cross-node payload). No new
  quality budget (the gate is a boolean-presence check read by the suite). The teardown/report flows are
  unchanged; placement is a build-time check on the author's machine plus a rendered file the person
  opens. PASS.

## Red-first proof

Captured in docs/prover/red-proof-2026-07-17-row408.txt: the gate reds all three fixture violations
(demoted-absent, over-cap, omitting closing note), and the test file reds 5 against the pre-delta tree
(pre-push unwired; spec/index/architecture/matrix carry no INV-206). After the delta all 15 board tests
go green.

## Verdict

HOLDS. Zero must-fix. The clause composes with INV-205 and base rule 10; the gate has teeth (it reds a
real violation, not a check that looks at nothing); the frame is consumed rather than re-opened. Open
⟨DECIDE⟩ touched by the change: none.

# Prover record — the monitor's scheduled action (INV-148), 2026-07-14

**Wish:** the FIRST-ON-RESUME beat from NEXT_STEPS — the stranger door is open (templates live, monitor
written) but unwatched: no schedule runs the monitor, and INV-147 requires a schedule where the door is
open. This delta gives the package repo its concrete schedule: a scheduled GitHub Action that runs
`scripts/stranger-wish-monitor.py`, commits any bridged inbox file, and pushes it. This is the act that
truly opens the door.

**Door / kind / footprint:** feature (a new autonomous writer to main) · infra (CI tooling, no visible
surface — facets N/A) · single-module (the stranger-monitor arm; the `inbox` node).

**Pass:** CROSS-LINK prove of INV-148 against the surfaces it seams, in the author's context, followed by a
required independent adversarial audit in a fresh context (INV-46 — a new invariant plus an autonomous
writer to main). This record carries the CROSS-LINK verdict; the audit's findings and their folds are
appended below.

## Seams checked

| seam | claim | verdict |
|---|---|---|
| INV-148 ↔ INV-147 | the action's `concurrency` group (a second run waits, `cancel-in-progress: false`) is the CI form of the per-host single instance the monitor's lock keeps | HOLDS — the lock guards a host running the script repeatedly in one checkout; a CI run is a fresh VM each time, so the lock cannot span two runs and `concurrency` is the right serializer. The two do not conflict; they cover different hosts |
| INV-148 ↔ INV-146 | the token needs issues + discussions write to record the surfaced-generation marker comment | HOLDS — `_deposit` posts the marker via `gh issue comment` (issues:write) and `gh api graphql addDiscussionComment` (discussions:write); both scopes granted |
| INV-148 ↔ INV-112 / M-6 | the push carries inbox commits only, so it rides the inbox-only push-gate carve-out | HOLDS with a note — the monitor commits touching inbox/ only, so the DELTA the push adds to origin is exactly the inbox file. A GITHUB_TOKEN push does not re-trigger gates.yml (GitHub's recursion guard), so the carve-out is not even exercised on this push; correct for an inbox deposit awaiting the next session's sweep |
| INV-148 ↔ INV-82 | the schedule is "recorded like the push grant" | HOLDS — for the package repo the record IS the committed workflow file; the schedule lives in the repo the door guards |
| INV-148 ↔ INV-1 / INV-67 | a run that cannot reach fails the job honestly, dropping no wish | HOLDS — the monitor returns exit 1 when unreachable (`return 0 if result["reachable"] else 1`), failing the "run the monitor" step before the push step runs |
| INV-148 liveness ↔ INV-147 | INV-147 requires a schedule where the door is open; INV-148 supplies it | HOLDS — this closes the liveness obligation INV-147 states; before this delta the door was open with no schedule, the exact gap NEXT_STEPS named |

## Where it held / open items

Branch protection on `main` was read live: no required PR reviews, no required status checks, no push
restrictions — a `contents:write` token push lands directly, so the workflow's push is not blocked. The
end-to-end verify (a real dispatched run proving a clean no-op) runs after the push, since a scheduled/
dispatch workflow is only triggerable once it is on the default branch — the same post-push verify the CI
gate itself takes (INV-106).

**CROSS-LINK verdict:** no defect in the seams. Findings from the independent audit and their folds follow.

## Independent audit (INV-46) — findings and folds

A fresh-context adversarial pass read every primary source, ran the tests, checked the live GitHub config,
and ran the register lint. **Verdict: GOAL MISSED — a real must-fix hole.** All findings folded before the
landing commits.

| # | severity | kind | finding | fold |
|---|---|---|---|---|
| F1 | must-fix | defect | **the monitor's own marker comment re-triggers it forever.** The monitor recorded, as the surfaced generation, the item's `updatedAt` captured BEFORE it posted its marker. Posting the marker bumps the item's `updatedAt`, so on the next run `activity_gen` (post-marker) is strictly newer than `surfaced_gen` (pre-marker) and the item re-surfaces — a second inbox file plus a new marker comment — every run, never converging. The bug lived in the monitor (INV-146/147); INV-148's DAILY cron is the amplifier that turns it from a harmless hand-run into daily duplicate spam on every open stranger item | **fold:** the recorded generation is now the newest marker comment's own `createdAt` (the post-marker generation), read via `_surfaced_gen_from_comments`; the skip test is `activity_gen <= surfaced_gen`. Next run the item's `updatedAt` equals the marker's `createdAt`, so it reads as no new activity; only another actor's edit or comment advances past it. Spec INV-146 re-surface clause + index row clarified; matrix M-289 grew the never-side; `test_monitor_does_not_retrigger_on_own_marker` encodes the exact scenario (red on the pre-fix logic) |
| F2 | should-clarify | defect | **a repo with Discussions disabled fells the whole run.** `_fetch_open_items` = issues + discussions; the discussions GraphQL errors on a repo without Discussions, propagating through `run()` to a red job every day AND dropping the Issue arm too (issues fetched but the concatenation raises before returning). Latent on this repo (`hasDiscussionsEnabled: true` confirmed live), live on any Issues-only repo INV-146 promises to serve | **fold:** `_fetch_discussions` checks `hasDiscussionsEnabled` first and returns `[]` when off, so the absent channel degrades to none rather than felling the run; a genuinely unreachable repo still raises and fails honestly [INV-67]. Spec INV-146 channel clause + index row updated; `test_fetch_discussions_degrades_when_disabled` covers it |
| F3 | nit | recommendation | the M-290 tests are string greps that under-constrain (a commented-out `cancel-in-progress: false` would pass) | accepted at the declared level (string) — they DO catch the two regressions the matrix names (flipping `cancel-in-progress` to true, dropping the `discussions` scope); the ceiling is noted, no change |

**Where the design held (audit-confirmed):** concurrency = single instance; the push is FF-scoped to the one
inbox commit and cannot clobber human work or smuggle other edits; the token scopes are exactly right; git
identity is set before the commit; honest failure is not masked by the push step; INV-148's prose is faithful
to INV-147/INV-146 and register-clean; traceability holds structurally.

**Post-fold:** full suite 698 green; the two folds each carry a red-proven test; register lint clean on the
changed sentences.

**Post-push reconciliation.** The push's CI (pytest) went red on `test_minor_versions_on_the_1_4_0_line`:
the 1.4.2 PATCH bump updated VERSION and plugin.json but not the two literals that travel with them [INV-104]
— the spec title stamp and that reconciliation test. Fixed both. This also surfaced a gate hole worth its own
row: the local push gate's `check-tests.sh` runs `python3 -m unittest discover`, which cannot collect the
plain-function pytest-style tests (fixtures like `monkeypatch`/`tmp_path`), so it false-greened while CI's
`pytest` caught the failure — the local net must run the same runner CI runs. Queued in NEXT_STEPS.

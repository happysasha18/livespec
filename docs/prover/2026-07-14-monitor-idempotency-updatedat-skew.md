# Prover record — the monitor's activity signal excludes its own writes (M-295), 2026-07-14 22:40 IDT

**Bug (found by a live round-trip on the package repo's Discussion #1, then cleaned up):** the monitor
was not idempotent on either channel. Run it twice against one open discussion with no outside activity
between runs and the same discussion surfaced into two inbox files. A single host running twice must
deposit exactly once.

**Root cause (confirmed in the code, not corrected):** the monitor fed the item's raw GitHub `updatedAt`
into the surfacing decision as `activity_gen`, and decided new activity by comparing it against the newest
of its own marker comments (`_marker_ceiling_from_comments`, added by INV-149). GitHub advances an item's
`updatedAt` to a moment strictly later than the `createdAt` of the comment that caused the bump. So when
the monitor posts its own claim (`<!-- live-spec claim-gen ... -->`) and confirm (`<!-- live-spec
surfaced-gen ... -->`) comments, the item's `updatedAt` lands a hair past the newest marker's `createdAt`.
The next run read `updatedAt` (19:20:53Z in the live evidence) as newer than the newest marker's
`createdAt` (the confirm at 19:20:52Z), cleared the ceiling, re-surfaced, and wrote a second inbox file
plus a second claim/confirm pair. The monitor's own writes advanced the very signal it used to detect
outside activity — a self-triggered loop firing every run on any open item, amplified daily by INV-148's
cron.

This is the residual of the earlier INV-148 audit fold (F1, `docs/prover/2026-07-14-monitor-schedule.md`).
That fold moved the recorded generation to the marker's own `createdAt` on the premise that "next run the
item's `updatedAt` equals the marker's `createdAt`, so it reads as no new activity." The premise was
wrong: `updatedAt` does not equal the marker `createdAt`, it lands strictly later. The marker-ceiling
comparison narrowed the gap but never closed it, because both channels still fed the raw `updatedAt`.

**Both channels shared the defect.** `_fetch_issues` and `_fetch_discussions` both set
`activity_gen = updatedAt`. The Issue channel was not safe under the same `updatedAt`-vs-marker-`createdAt`
timing — the red-first test deposits a second file on the Issue arm too. Both are fixed by one helper.

**Fix.** The activity generation is now read from activity that is not the monitor's own writes:
`_activity_gen_from_comments` returns the newest `createdAt` among the item's comments that are not one of
its markers (empty when there is no third-party comment). Both fetchers set `activity_gen` from it. The
monitor's own claim and confirm add no non-marker comment, so they never advance the generation and a
second run settles at exactly-once; a genuine third-party comment is a non-marker comment, so it advances
the generation and re-surfaces the item once, as INV-146 intends. The `marker_ceiling` reading stays in
the pure core as a belt-and-suspenders baseline (it still holds a losing host's trailing claim below the
line for INV-149), now redundant-but-consistent with the stronger non-marker signal.

**File:line of the change.** `scripts/stranger-wish-monitor.py`:
- new `_activity_gen_from_comments(comments)` (and `_is_monitor_marker`) below `_marker_ceiling_from_comments`.
- `_fetch_issues` and `_fetch_discussions` set `"activity_gen": _activity_gen_from_comments(comments)`
  in place of `iss.get("updatedAt", "")` / `d.get("updatedAt", "")`.
- docstrings corrected: the module header, the `items_to_surface` comment block, and
  `_surfaced_gen_from_comments` no longer assert the false "updatedAt after the marker equals the recorded
  value" premise.

## Spec sentences touched — prover pass

| sentence | change | verdict |
|---|---|---|
| INV-146 body re-surface clause (PRODUCT_SPEC.md ~1667) | replaced "records the item's generation as it stands after its own marker comment … the item's generation after the marker equals the recorded value" with the corrected mechanism: the activity generation is read from non-marker comments, the raw update time cannot serve (GitHub bumps it strictly past the marker createdAt), so only another actor's comment advances it | HOLDS — the sentence now states a mechanism the implementation actually realizes; the false equality premise is gone |
| INV-146 index row (PRODUCT_SPEC.md ~1835) | "records the item's POST-MARKER generation (the marker comment's own createdAt)" → "reads the item's activity generation from its non-marker comments (never the raw update time GitHub bumps strictly past the monitor's own marker createdAt)" | HOLDS |
| INV-149 body claim clause (PRODUCT_SPEC.md ~1677) | "measures new activity against the newest of its own markers, the claim among them" → the activity generation is read from non-marker comments (a claim is a marker, so it never advances it), with the newest-of-any-marker ceiling standing beside as a belt-and-suspenders baseline | HOLDS — the trailing-claim outcome is unchanged; the mechanism now matches the code, and the claim is excluded from the activity signal directly rather than only capped by the ceiling |
| matrix M-288 / M-289 / M-291 re-surface clauses (TEST_MATRIX.md) | reworded off the raw-updatedAt premise onto the non-marker-comment reading; each cites M-295 | HOLDS |

**Was the spec right and only the code wrong?** No — the spec's re-surface mechanism carried a false
premise (updatedAt after the marker equals the recorded value). The intent (record the item's post-marker
generation; only another actor advances it) was right; the stated mechanism for reaching it was wrong and
is corrected. The invariants INV-146/147/149 themselves stand; their wording was sharpened.

## Known narrowing (data-safe)

A bare edit or reopen with no accompanying comment no longer re-surfaces on the edit/reopen alone; it is
surfaced on its next comment. This is narrower than the pre-fix behaviour, which read the raw `updatedAt`
and therefore looped on every run in a stable state (the bug), so it never delivered a clean edit/reopen
re-surface anyway. No wish is lost: a reopened item stays visible on GitHub and its next comment surfaces
it. `gh issue list` exposes no `lastEditedAt`, so a body-edit signal is not cleanly available on the Issue
channel; reading the non-marker comment keeps both channels on one consistent signal. Recorded here rather
than expanded, per scope.

## Red-first proof

`tests/test_stranger_door.py` (M-295):
- `test_own_marker_updatedat_bump_does_not_reloop_discussion` — drives the real `_fetch_discussions` with
  a monkeypatched `gh` returning the second-run state (claim + confirm markers, `updatedAt` bumped to
  19:20:53Z past the confirm at 19:20:52Z); asserts `items_to_surface(...) == []`.
- `test_own_marker_updatedat_bump_does_not_reloop_issue` — the same through `_fetch_issues`.
- `test_activity_gen_excludes_the_monitors_own_markers` — `_activity_gen_from_comments` does not advance on
  the monitor's own markers and does advance on a genuine non-marker comment.

**Red on the pre-fix tree:** both channel tests deposited a second item
(`activity_gen '2026-07-14T19:20:53Z'` > `marker_ceiling '2026-07-14T19:20:52Z'`); the helper test errored
(function absent). **Green after the fix.**

**Suite:** `guardrails/check-tests.sh` — 724 passed, 6 skipped. `guardrails/check-shipped-language.sh` —
clean (0 offences). No new error-level spec-style offences introduced (the pre-existing scissors on
M-288/M-275 predate this delta).

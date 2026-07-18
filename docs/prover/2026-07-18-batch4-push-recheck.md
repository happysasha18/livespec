# Prover record — 2026-07-18 — batch 4 push re-check

A pre-push re-check of the unpushed batch sitting on top of origin/main (`fe6ef60`), run
independently of the sessions that built it, before the orchestrator pushes.

## The batch

Seven commits, HEAD `d997111`:

- `0f9c881` — Row 420 candidate 4: a finished worker leaves no runaway child (INV-213)
- `afe1b5b` — Rows 386/412/414: the lane-open act, the serial-work discipline, the cap
  re-homed (INV-214)
- `4c34958` — Row 420 runaway-child: state the provenance impersonally (INV-120)
- `f2f01e5` — Row 379: enumerable facts earn bullet structure (INV-215, M-396)
- `cfc996e` — row 406: config-health reds a dead permission rule (INV-216 / M-397)
- `06efdc1` — ROADMAP 407: state the release-tier rule (minor/major/patch by host cost)
  [INV-217, M-398]
- `d997111` — Integrate the 2026-07-18 three-lane run: batch JOURNAL + NEXT_STEPS +
  row-379 delegation line

## What was checked

The full test suite ran clean: 1366 passed, no failures, no skips beyond the pinned set.

Every pre-push gate ran individually, a through w (23 gates in total): all green. Gate k (the
compaction freeze) matched its frozen baseline on the first check, so no re-freeze was needed.
Gate g reported one pre-existing pin-drift note (`templates/skill-review.template.md`) under its
non-strict mode; that note predates this batch and does not fail the gate.

The Formal index in PRODUCT_SPEC.md carries INV-210 through INV-217 each exactly once, in
sequence, with no gap.

Every landed row carries its prover record dated 2026-07-18: rows 386/412/414
(`docs/prover/2026-07-18-rows386-412-414-lane-open-act.md`), row 420's runaway-child candidate
(`docs/prover/2026-07-18-row420-runaway-child.md`), row 379
(`docs/prover/2026-07-18-row379-enumeration-reads-as-list.md`), row 406
(`docs/prover/2026-07-18-row406-dead-permission-rule.md`), and row 407
(`docs/prover/2026-07-18-row407-release-tier-rule.md`).

## What this batch encodes

Two of the seven commits build a mechanism; the rest are the mechanism proving itself in the
field the same day.

The lane-open act (rows 386/412/414, INV-214) turns opening a lane from something a session
decides into something it performs: `scripts/open-lane.sh` commits the row-to-in-work claim to
main, cuts a `lane/<row>-<slug>` branch into its own worktree, and hands the lane to a worker
naming that branch. Row 412 asked whether serial work should be checked by a gate; the answer
landed as a discipline instead, because independence between rows is a senior read no diff can
settle, and lane branches are torn down at each landing so no push-time signal would survive to
key a gate on. Row 414 moves the lane cap out of hardcoded values and into the settings ladder.

The same day, that mechanism ran for real: three lanes opened in parallel isolated worktrees and
built rows 379, 406, and 407 concurrently, each landing its own commit and prover record, then
integrating in order. The integration commit (`d997111`) reconciles what the lanes could not each
carry alone — one shared JOURNAL entry for the run, the NEXT_STEPS queue update marking all three
rows landed, and a delegation-accounting line for row 379 the lane commit had omitted. This run
also surfaced that `isolation:worktree` cuts a lane from pushed origin/main rather than local
HEAD, a stale-base finding now on record for the next lane run.

Row 420 candidate 4 (INV-213) closes a separate gap the same movement hit: a finished worker can
leave behind a runaway child process burning a core unnoticed after the worker itself reports
done. The mechanism owns what it spawns (process group or its own tree) and reports what it holds
and why at a stopping point, notice-first and ending no process itself. The follow-up commit
(`4c34958`) restates that mechanism's own provenance line impersonally, closing an INV-120 shipped-
language finding on the row's own record.

## Verdict

PUSH-READY. Suite green (1366 passed), all 23 pre-push gates green, the Formal index contiguous
INV-210 through INV-217, every prover record present and dated. No blocker found.

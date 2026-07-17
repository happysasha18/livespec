# Prover record — 2026-07-18 — ROADMAP 420 candidate 4: a finished worker leaves no runaway child (INV-213)

Footprint: single-module. The mechanism adds one Stop-time notice check
(`guardrails/check-runaway-child.py`) plus one function on the shared cleanup-notice module, and it
reasons over a process table rather than over the gate chain. Its stakes are high — it runs in
process space, where a coarse scope closed the owner's real browser once — so the walk ran carefully
even though the delta is one module.

## Previous records clean

The prior record `docs/prover/2026-07-18-row420-every-gate-can-fail.md` (candidate 3, INV-212) carries
no unfolded rows and no open ⟨DECIDE⟩. Nothing outstanding is inherited.

## The delta in one line

At a stopping point the run reports a runaway descendant it provably owns — what it is, how much CPU
it holds, and why the run owns it — the notice word the owner gave (2026-07-17 ~16:58, the same word
that ordered row 417's cleanup notice). The mechanism `guardrails/check-runaway-child.py` reports a
descendant that is owned (its own process group, or its own temp tree), orphaned (its owning parent no
longer alive), and burning (CPU share at or above a host-settable threshold), reading no command or
name field so a bare-name match never fires (INV-162). It reports through the shared
`guardrails/cleanup_notice.py` and ends no process.

## The footprint verdict

Single-module. The notice does not own a new product surface and does not reason over other gates. Its
home is the guardrails node, beside the Stop-surface judges; its subject is the live process table.

## Verdict

- **Every spec fact has an owning node.** INV-213 is owned by the guardrails node in ARCHITECTURE.md,
  with a pin for `check-runaway-child.py`. The `runaway_notice` addition rides the existing
  `guardrails/cleanup_notice.py` pin on the test-author node, where the cleanup-notice shape (INV-204)
  and the owned-identity discipline (INV-162) already live. No unowned fact, no new node.

- **No node stands without spec backing.** No new node was carved; the fitness test does not fire.

- **The ownership discipline is the whole design, and it is mechanical.** The core `find_runaways`
  reads only process group, parent liveness, and CPU share. It reads no command or name field for its
  verdict, so the class of mistake INV-162 forbids — telling this run's copy of a program from the
  human's by NAME — cannot happen: a process whose command matches a known burner while sitting in a
  foreign process group and under no owned tree is refused because the run cannot prove it owns it.
  This is asserted directly by `test_bare_name_match_never_fires`, which supplies a burning,
  orphaned foreign process whose command reads `python difflib` and asserts an empty result.

- **A live worker at work is never a runaway.** Orphaned means the owning parent is no longer alive
  (reparented to init, or a ppid absent from the live table). A child in the owned group whose parent
  is alive is a live worker mid-computation and is never reported — `test_live_owned_working_child_is_not_reported`.
  This is the safety edge the audit flagged: the check must not endanger legitimate live background
  work. Because the distinction is mechanical (is the parent still in the table?), the mechanism ships
  as a real check rather than report-only-because-undecidable.

- **Notice-first, and it can never become the footgun it guards.** The mechanism ends no process: the
  source carries no process-ending verb, asserted by `test_the_check_source_ends_no_process`, so it
  passes the broad-kill gate (j) and the cleanup-notice gate (o) by construction — it ends nothing, so
  neither gate has anything to judge. A reap gated on the same strict ownership proof is named as a
  later, optional step and is not built here; the first version reports.

- **It is a Stop-time notice, not a push gate — so it takes no push-gate letter.** A push gate runs
  long after the runaway would have burned its cores, so wiring this into `pre-push` would report the
  burn too late to matter. It therefore adds no gate letter, is absent from `pre-push` and from
  `gates.yml` (`test_not_wired_as_a_prepush_gate`, `test_not_a_ci_step`), and is not enumerated by the
  meta-gate (gate w reads only `pre-push` gate letters), so gates u and w stay green with no change.

- **Live wiring is deferred to the owner, by name.** The check ships as pack source. Its live wiring —
  an entry in `~/.claude/settings.json`'s Stop array — is a documented owner-run step in
  `guardrails/README.md`, not an auto-wire. Wiring a process scanner into the running session's Stop
  hook mid-movement is exactly the risk the audit named: it could report against this very session's
  own live background workers. Because the check lives in `guardrails/` and not under `hooks/`, it does
  not trip config-health (gate m) or judge-listed (gate v), which require every `hooks/` file to be
  installed and wired live.

- **Testable without ever spawning a runaway.** Every test drives a SIMULATED process table — a list
  of dicts, or an injected JSON table through `LIVE_SPEC_RUNAWAY_PROCS_JSON` for the subprocess path.
  No test ends a process, spawns a CPU burner, or reads the real machine's process list, so the suite
  leaves the machine as it found it (INV-100) and can never leak a runaway.

- **Cross-section.** The notice composes with the cleanup-notice family (INV-204/INV-162, test-author
  node): it applies the same owned-via proof discipline through the same shared module, adding a
  report variant (`runaway_notice`) for a process still alive rather than one just ended. It composes
  with the meta-gate and CI-mirror gates by staying OUT of the push chain, which both of those read.

- **Red-first proven.** 18 of the 20 tests failed against the pre-delta tree (mechanism and
  `runaway_notice` absent; spec/index/architecture/matrix carried no INV-213), then green after the
  delta. The 2 that passed throughout are the two absence assertions — `test_not_wired_as_a_prepush_gate`
  and `test_not_a_ci_step` — which correctly hold before the mechanism exists. Capture:
  `docs/prover/red-proof-2026-07-18-row420-runaway-child.txt`.

## Open ⟨DECIDE⟩

None touched by this surface.

## Must-fix

0.

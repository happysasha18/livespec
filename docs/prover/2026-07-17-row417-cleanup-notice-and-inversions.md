# Prover record — ROADMAP 417: a cleanup says what it ended, and four name-list guards invert

Date: 2026-07-17 · Doc version: v2.6.3 · Form: FULL (surface delta across four gates + one new net) ·
Mode: FULL prover walk of the changed clauses beside the whole-spec composition, plus the architecture
lens on the ARCHITECTURE.md edit.

## Footprint classification

Cross-cutting on the guardrail surface, single-module on each gate's own body: the change moves one
shared law (a cleanup ends only what it owns, stated positively as an owned-identity check) across four
mechanical gates and adds a new observability net beside them. No product-facing surface, no new
persistent state, no new node — INV-204 lands on the existing test-author node beside its cleanup-safety
siblings INV-157/INV-162. Full prover walk, not the short form, because four gates' meaning changed and
a new invariant was declared.

## What changed, and the law under each

- **INV-162 inverted** (`guardrails/check-broad-kill.sh`): the guard denied a kill that named one of
  four browser words; it now denies every ending that names a NAME (a `pkill`/`killall` pattern, or a
  `kill` fed by a `pgrep`/`pidof` lookup) and accepts one that proves what it owns (a recorded PID, a
  process group, an install path under the run's tree). The browser words are the error's explanation.
  The class narrows to his 2026-07-17 ~15:56 correction: every process the pack runs a copy of (chrome
  proven; python/Demucs, node, ffmpeg live siblings), never a program the pack never launches.
- **INV-204 new** (`guardrails/cleanup_notice.py` + `guardrails/check-cleanup-notice.sh` +
  `templates/headless_harness.py`): a cleanup says what it ended. The notice ships ahead of the stricter
  INV-162 form on his 2026-07-17 ~16:58 word and makes it safe to land.
- **INV-120 inverted** (`scripts/check-shipped-language.py` + allowlist): the owner-name arm reads a
  declared alphabet held as allowlist data, so the detector's own code names no person.
- **INV-175 inverted** (`guardrails/check-config-health.sh`): the session-hook arm diffs the whole hook
  source directory against the installed set, covering every hook automatically.
- **INV-152 inverted** (`guardrails/check-deferral-marker.py`): the net reads the grammatical shape of a
  deferral, so the `⟨DECIDE⟩` marker itself is caught.

## Architecture lens — the six checks on the ARCHITECTURE.md edit

1. **Every spec fact has an owning node.** INV-204's anchor lands on the test-author node's owns-list,
   exactly one owner (traceability suite green). PASS.
2. **No node stands without spec backing.** No node added; the test-author node's description grows one
   clause backed by INV-204. PASS.
3. **Every seam names what crosses it.** No new seam; the notice is emitted on stderr within the
   harness, an internal side-effect, not a cross-node payload. PASS.
4. **Quality budgets with instrumentation homes.** No new budget; the notice is a boolean-presence gate,
   read by the suite. N/A.
5. **Runtime view walks every promised flow.** The teardown flow already walked; the reap step now emits
   a notice, a within-step side-effect that changes no flow edge. PASS.
6. **Placement view.** The gate and shape are build-time checks on the author's machine; the emitter runs
   client-side inside the harness process. Unchanged placement. PASS.

## Spec-lens findings

- **F1 (folded).** INV-204 had to name its net to satisfy the number-names-its-watcher parity and the
  suite-honesty kinship it cites [INV-157, INV-162]. The clause names both arms (the shared shape and the
  gate) and the harness as the emitting path. Folded in the clause and the Formal-index row.
- **F2 (folded).** The INV-120 restatement is the session's sharpening of the row's word (an alphabet
  rather than four spellings, minimal shape left to the seat); marked as the session's own interpretation
  in the clause per INV-114. Folded.
- **F3 (recommendation, folded).** INV-204's ownership could sit on the guardrails node (the scripts live
  there) or test-author (the emitting harness + the cleanup-safety siblings INV-157/162). Chose
  test-author for sibling-consistency; the scripts are pinned there. Recorded.

## Pre-existing findings folded (equivalence-gate, INV-114)

Two reds inherited from the register-judge landing (ebe591d), both unrelated to row 417's substance,
folded here so the suite lands green rather than routed to a queue row that would leave the suite red:

- **P1.** `hooks/register_judge_core.py:50` carries the Russian banned-frame «X, а не Y» un-spared, which
  the shipped-language gate (gate i) reds on. It is a deliberate program string — the universal chat law
  naming the frame it forbids, the detector-vocabulary self-exclusion class. Added a dated
  `cyrillic_waiver`.
- **P2.** Rows 416 and 418 landed-forward cells omitted their INV-103 delegation line; the journal
  chapter header records the work as single senior seat. Added `delegation: none — single senior seat`
  to both cells.

## Verdict

HOLDS. Zero must-fix. Every changed clause composes with its neighbours; the four inversions each keep
their gate's prior catch (red-proven) while widening it to the class; INV-204 names its net and its
emitting path. Open ⟨DECIDE⟩ touched by the change: none.

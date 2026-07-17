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

## Corrections after adversarial review 2026-07-17

The verdict's claim that "the four inversions each keep their gate's prior catch (red-proven) while
widening it to the class" was too strong, and an adversarial review of the four guards falsified it. The
broad-kill rewrite from the browser-word list to an owned-identity read did NOT keep every prior catch:
the old name-list guard reddened any line carrying a browser word beside a kill, so it caught a
`ps ... | grep chrome ... | xargs kill` pipeline and a `/usr/bin/pkill chrome` on the browser word
alone, and the rewrite lost both because its resolver regex knew only `pgrep`/`pidof` and its NAMEKILL
class excluded a leading `/`. The review found four confirmed defects; each is corrected below, red-proven
against the committed tree first, then fixed and greened. The corpus fixture — whose whole purpose is
that a later change cannot silently narrow what the guard catches — had itself failed that job, so every
newly-caught form is now pinned in it.

- **D1 — broad-kill resolver blind spots (`guardrails/check-broad-kill.sh`).** The rewrite passed three
  browser-killing forms the old guard caught. RED-proven passing against the committed tree:
  `ps aux | grep -i chrome | awk '{print $2}' | xargs kill -9`, `/usr/bin/pkill chrome`, and a two-line
  `PIDS=$(pgrep -f "Google Chrome")` then `kill $PIDS`. Fix: added a `ps`-piped-to-`grep` resolver form
  to the name-kill detection; dropped the leading-`/` exclusion from NAMEKILL so a full-path
  `pkill`/`killall` reds; added cross-line taint tracking so a variable assigned from a resolver and
  killed later reds; and extended the repo scan to the extensionless tracked executables (`guardrails/*`,
  `hooks/*`) it had skipped, e.g. `guardrails/pre-push`. The three named forms plus `pkill -f node`,
  `killall Safari` etc. are pinned RED in the corpus and now red. Safety direction: catches strictly
  more.
- **D2 — the shared-install-path exemption contradicted the spec (`guardrails/check-broad-kill.sh`,
  `tests/fixtures/kill_probes.txt`).** The guard exempted any line containing `.cache/puppeteer` or
  `user-data-dir`, and the corpus pinned `pkill -9 -f "$HOME/.cache/puppeteer/..."` as PASS, which
  re-blessed a cross-run kill the INV-162 spec text at PRODUCT_SPEC.md forbids: a shared install path
  reaches other sessions' live browsers, so only the recorded process group is safe. Verified the only
  shipped killer is `templates/headless_harness.py`, which uses `os.killpg` on its own process group and
  relies on no path exemption. RED-proven the two shared-path forms passed against the committed tree;
  fix: removed the exemption entirely (there is no safe path-scoped `pkill` to preserve), flipped the
  corpus probe from PASS to RED, added `pkill -f user-data-dir` as RED. Both now red.
- **D3 — cleanup-notice blind to the Python endings (`guardrails/check-cleanup-notice.sh`).** A file
  whose only ending was `proc.terminate()` or `proc.kill()` passed with no notice. RED-proven against the
  committed tree; fix: added `proc.terminate()` / `proc.kill()` on a `subprocess`/`Popen` handle to the
  ends-a-process detection. The real cleanup path (`templates/headless_harness.py`) still passes because
  it emits the notice beside its reap.
- **D4 — deferral marker cleared by a coincidental reason word (`guardrails/check-deferral-marker.py`).**
  `⟨DECIDE⟩ which sound file the build should bundle` passed because `sound` sits in the reason list — the
  noun, not the feel-call. RED-proven against the committed tree; fix: an open-decision marker
  (`⟨DECIDE⟩`, `TBD`, "to be decided") now requires a CORE human-only fact (taste / policy / irreversible
  / device-feel) to stand, and a soft craft noun (`sound`, `voice`, `tone`, `crop`) no longer clears it,
  while a deferral predicate already pointed at the human still accepts any reason. `⟨DECIDE⟩ ... a taste
  call` still passes; the config-choice case now reds. Residual: fully separating a craft noun's
  feel-call sense from its config sense would need a judge, so an open marker parking a genuine audio
  taste call named only by a soft word (`⟨DECIDE⟩ which reverb sounds right`) would over-red; the clear
  leaking case the review named is closed and the soft/core split is the minimal fix that does not
  over-red the legitimate cases the suite covers.

All four fixes carry a RED-first test in `tests/`; the full suite is green after the corrections (count
recorded in the landing report). The M-311 matrix row and the guards' header comments were realigned to
the corrected law (a shared install path is not a safe target; the safe targets are a recorded PID or a
process group the run holds).

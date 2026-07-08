# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**NIGHT DONE (2026-07-08→09, autonomous loop) — DURABLE PROSE-QUALITY GATE built, and SPEC + ARCHITECTURE rewritten through it. NOTHING PUSHED.**

Why: the same prose defects (scissors, redundancy, second person) kept recurring because the old gate was
holed — caps + second-person were non-blocking warnings that piled up, there was no redundancy check, and
"parked" sections kept their tells. Fix = a machine gate, not more attention. Memory
[[prose-quality-gate-must-block-not-park]]. Research (107-agent deep-research) + a clean-context design →
`docs/prose-quality-gate-design.md`.

BUILT (all code mine; the mechanism):
- `scripts/spec-style-lint.py --gate` — promotes caps-shout + second-person to blocking, adds reassurance +
  future-narration rules, exempts marked informative regions (user-story line, blockquote, NOTE), allowlists
  defined terms, waiver-aware. Default mode unchanged.
- `scripts/spec-redundancy-precheck.py` — mechanical near-duplicate catch (lexical).
- `scripts/spec-judge.py` + `judge-rubric.md` — a fresh-LLM whole-doc redundancy/register judge with a
  hash-pinned rubric, verbatim-quote evidence, and a seeded self-test canary (a green is trusted only when
  the canary fired). This is the semantic layer a regex cannot do.
- `scripts/spec-waivers.json` + `spec-debt-cap.json` — a dated, tracked waiver replaces silent parking.
- `scripts/spec-done-gate.py` — the single definition of done. `scripts/gate_common.py` shared lib.
- Tests: `tests/test_prose_gate.py` (20) incl. TestNeedleRegisterClean + TestAnchorInBlockquoteGuard.

RESULT (proof, in the repo, commits `3665f7b`..HEAD, all LOCAL):
- SPEC.md: lint gate-errors 320 → 45, and all 45 are the Formal index TABLE (left as structure by your word).
  Every body section is 0 gate-errors. Anchor multiset IDENTICAL to baseline `b05e199` (nothing lost). A fresh
  clean-context whole-doc judge (self-test passed) finds 0 surviving redundancy/register findings.
- ARCHITECTURE.md: prose converted (tables untouched); judge-clean; anchors identical; 3 emphasis caps remain
  inside table cells (parked with the tables).
- Suite 203 green; the only red is `TestGateA_ProverRecord` — the expected pre-push prover-record reminder.
- Method sealed into `skills/spec-author` (pointer to the design doc, one home).
- Every re-styled section: fresh writer (pack not loaded) + machine gate + fresh checker; every broken
  traceability needle re-pointed by narrowing, logged in `docs/restyle-repoint-log.md`.

WAITS ON YOUR WORD (then prover pass + commit its record, then push — SPEC M-6):
1. The Formal index table — convert it to register too, or keep it as a terse structured reference? (its 45
   lint errors are the only ones left).
2. The redundancy pre-check flags 9 pairs that are all legitimate cross-section references to the same law
   (the judge confirms not redundant) — teach the pre-check to skip same-law cross-refs (both cite one anchor)?
3. Seal into the playbook too — it is a separate repo, so I left it (one-window rule); your call / your window.
4. Read the rewritten SPEC and say whether the voice is right. The gate holds the floor (no defect class);
   your eye is still the ceiling.
Deferred features you asked for tonight (captured, memory): spawn parallelism + liveness watchdog; artifact
registry (pointers, not secrets).

## LIVE STATE (2026-07-08, session 26) — humanize + 0.9.0 milestone + three new laws LANDED AND PUSHED.
Versions: pack 0.9.0 (pushed) · base 0.1.24 · communicator 0.1.39 · build-pipeline 0.2.40 · SPEC v0.15.61;
suite 180 green; main = origin/main (HEAD 1cff42b). The writing register (14 rules + 8-item self-check) lives
in communicator; spec-author points to it; deployed==repo. Reporting persona = PROJECT MANAGER, plain product
words (memory [[report-as-project-manager]] + [[plain-language-communication]] + [[parametrize-defaults-and-push-when-ok]]).
Jargon guard is now mechanical (`scripts/preshow-lint.py`, the INV-28 arm). The live board = a chat NOW/NEXT
status + heartbeat (INV-71); the HTML board sketch is dropped by his word. Runs on Opus (Fable pulled 2026-07-07).

## Forward queue (mirrors ROADMAP.md)

1. **DONE and PUSHED:** humanize movement · 0.9.0 milestone · three laws — INV-70 (agent sets tunable
   parameters and tells) · INV-28 pre-show jargon guard · INV-71 (live NOW/NEXT status in any seat, resolves
   the live-board ask row 166). No autonomous rows remain that don't need his word.
2. **Needs HIS word or a real window:** remote-seat session — this evening/tomorrow (also proves INV-67/71 in
   a real cloud seat) · make live-spec work with NO hooks / NO GitHub (row 171, large) · rewrite the spec as
   an even plainer document (row 148, large) · thin-loader tidy in his personal `~/.claude/CLAUDE.md` (move
   the window-list + stale "Fable only" note to his profile — his file, offered) · pack orchestration
   (2026-07-08, his ask): take independent work while a spawn runs (no idle-block) + spawn-liveness watchdog
   (hung / silent-too-long / alive) — [[pack-orchestration-parallelism-and-spawn-liveness]], ROADMAP rows ·
   artifact registry (2026-07-08, his ask): a per-project index of handed-in artifacts surviving /clear,
   recording WHERE each lives (Keychain name / path), never the secret value — [[artifact-registry-pointers-not-secrets]].
3. Field legs riding real windows with him: 47/96 feedback loop · 54 first-run · 165 first-struggle · 168
   remote seat (this evening) · 134/141 zero-drift · 143 · 144 · 140 · 117 · 129 · 133.
4. Standing habits: `date` before ANY stamp · NOW/NEXT current + heartbeat past ~10 min (INV-71) · plain
   product words, never a code leading a line (INV-28), say "live-spec" not "пакет" · inbox EMPTY.

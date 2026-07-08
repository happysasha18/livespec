# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

**ACTIVE MOVEMENT (2026-07-08 night, autonomous loop, NO memory wipe) — DURABLE PROSE-QUALITY GATE.**
Alexander reopened the night: the SAME prose defects (scissors, redundancy, second person) recurred after a
full restyle round because the gate is holed — `caps-shout` (246) + `second-person` (71) are non-blocking
WARNINGS that just accumulate, there is NO redundancy/verbosity check at all, and "parked" sections keep their
known tells (he hit the parked preamble). His mandate: stop patching, build the mechanism so no defect class
can recur. Memory [[prose-quality-gate-must-block-not-park]]. PIPELINE (do not stop until all done or blocked):
1. RESEARCH — DONE (wf_d5338e62-3bd, 107 agents): layered gate; promote-all-to-blocking; no-park dated waiver;
   redundancy = LLM-judge with verbatim quotes + self-test canary; broken-windows (parking breeds recurrence).
2. DESIGN — DONE (fresh clean-context agent): full mechanism in docs/prose-quality-gate-design.md.
3. IMPLEMENT — DONE (all code mine, suite 201 green): scripts/gate_common.py, spec-style-lint.py `--gate`
   (promote caps+2nd-person, exemptions for user-story/blockquote/NOTE, new reassurance+future-narration,
   waiver-aware), spec-redundancy-precheck.py, spec-judge.py + judge-rubric.md (hash-pinned + self-test),
   spec-done-gate.py, spec-waivers.json + spec-debt-cap.json, tests/test_prose_gate.py (18 tests). The judge
   (stage 4 VALIDATE) is now built INTO the gate — a fresh Opus agent judges the whole doc, --verify checks it.
   STAGE 5 IN PROGRESS: anchor-multiset baseline = commit `b05e199` (552 anchor tokens). Chunks DONE:
   9 done (…, Breakpoints, Parallel lanes). Gate-errors 320 → 203. Giants left: Specifying 42, Delegation 31 (56 are the Formal index,
   parked by his word → ~242 actionable, ~33 sections). Per chunk: fresh Opus writer (pack not loaded) →
   gate (anchor multiset identical + --gate 0 on region + suite green + re-point broken needles by
   narrowing, logged) → commit only on green. Hotspots ahead (needle-heavy): "Specifying and building a
   feature" (42), "Delegation and workers" (31), "Parallel lanes" (25). Then ONE whole-doc judge pass +
   TestNeedleRegisterClean + TestAnchorInBlockquoteGuard, then ARCHITECTURE.md, then seal the method.
5. APPLY — his steer: prefer ONE whole-document clean rewrite by a fresh max-reasoning agent (Opus max, clean
   context; Fable pulled 2026-07-07) using the design stage's "right prompt", over section-by-section patching
   — one mind over the whole doc kills cross-section redundancy + register drift. Gate HARD after with the NEW
   done-gate: spec-done-gate.py GREEN (style-lint --gate 0 err + redundancy open 0 + judge selftest-passed & 0
   surviving + anchor multiset identical vs baseline), every needle survives (add TestNeedleRegisterClean +
   TestAnchorInBlockquoteGuard now), suite green; any gap → re-feed, never accept a lost anchor. Covers SPEC
   (incl. preamble convert) and ARCHITECTURE.md. Prior art in the design doc: Kiro EARS + BMAD checklists,
   ours adds the machine gate they lack. Then seal the gate into spec-author + playbook (after his sign-off).
DECIDED BY HIM: preamble → CONVERT; Formal index → LEAVE as structure (its 2 errors stay, by his word).
Prior restyle work is LOCAL commits 3665f7b..(88f228c bookkeeping); SPEC lint 4 errors / 317 warns; suite 183
green (only red = TestGateA_ProverRecord). NOTHING pushed. Before any push: prover pass + commit its record.

**LATEST (2026-07-08, session 28) — SPEC re-style: the drift is SOLVED by a mechanism; grind in progress.**
Root cause of the ornate spec prose, proven with Alexander: the author is marinated in the pack's own
register (doors/kinds/stations/coined metaphor), not the content and not text length. A fresh agent with the
pack NOT loaded writes plain product-spec English from the same facts, consistently, at length. So the fix is
mechanical + a division of labor — and it is SEALED in `docs/spec-style.md`:

THE METHOD (run every section this way; it generalizes to all projects):
- A **fresh spawned agent, pack NOT loaded**, writes the prose from the section's source/facts. Tell it: keep
  every [anchor] verbatim, keep ALL info, keep headings + bold titles, use bullet/numbered lists for any
  sequence, plain present-tense, no second person, no metaphor, do not open by saying what a thing is NOT,
  no ALL-CAPS. Do NOT let the marinated session write the prose — even its chat drifts (his catch this session).
- The marinated session does the mechanical half: gate with `scripts/spec-style-lint.py` to ZERO errors,
  verify the anchor multiset is unchanged (grep `\[...\]` old vs new), splice, run suite, and re-point any
  brittle traceability needle from the old exact phrase to an anchor + a register-invariant term.

CONVERTED so far (register-clean, gated, suite green): "What live-spec is", "Throwing a wish", "Intake",
Naming's first three rules (echo / status board / feature-map placement), "Showing work and asking for
decisions", "Doors, kinds, and craft", "Asking what the product does" (committed 3665f7b, night pass). Gold
exemplars = the decision-page list + intake.

NOTE: the earlier section-by-section "park the needle-colliding sections" plan is SUPERSEDED by stage 5's
whole-doc rewrite — one clean pass converts every section at once, and the new done-gate (with anchor-multiset
+ needle-register-clean checks) proves nothing was lost. His two goals stand: (1) human-clear, easy to read,
all info present; (2) it also helps the agent build next steps. SPEC prior state: lint 4 errors / 317 warns,
all defects to be removed by the rewrite except the 2 Formal-index errors he chose to leave. Before ANY push:
prover pass + commit its record (SPEC M-6); TestGateA_ProverRecord stays red until then (not a regression).
Baseline (pushed, clean): pack 0.9.0, main = origin/main HEAD `1cff42b`. All session-28 + gate work is LOCAL.
Memory: [[spec-prose-clean-agent-plus-linter]], [[prose-quality-gate-must-block-not-park]].

SAFE TO WIPE MEMORY here (resume cold from this block + docs/prose-quality-gate-design.md + docs/spec-style.md).

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

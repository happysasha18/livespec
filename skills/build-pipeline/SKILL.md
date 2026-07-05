---
name: build-pipeline
description: >
  Run a non-trivial change by the book — the spec → prove → reconcile → matrix → test → code → verify → commit
  pipeline, orchestrating the spec-author and product-prover skills. Use this whenever starting a new
  feature, a new stateful surface, or a behaviour change that deserves more than a one-line edit:
  "build X properly", "do this by the method", "spec and ship Y", "new surface for Z". It is the
  executable projection of the method (PLAYBOOK.md holds the principle) so the method survives memory
  wipes. NOT for tiny reversible edits (those shortcut straight to code + a test) or pure research/fact-gathering.
version: 0.1.0
---

# build-pipeline — ship a change by the method

> Part of the **livespec pack** — the shared working rules (ask-never-guess · plain words, anchors trail ·
> one surface = one name · one home per fact · junior/senior split · checkpoints · the concurrent-edit
> fence · freshness · journal discipline · attic-never-delete · verify by deed · the human's gates) live
> ONCE in the pack's base skill, `livespec-base` (v0.1.0), together with the settings ladder — this skill
> references them and elaborates only its own domain. Used standalone, this note is plain advice.

One pipeline, each step has a tool. The order is **spec → prove → reconcile → matrix → test → code → verify
→ commit**. A bug shortcuts to **bug → matrix → test → code**. **Skip the pipeline only if ALL hold:** single
file · no new state / element / user-visible behaviour · an existing test level already covers the touched
fact (still ship a test). Anything touching visibility / layout / colour enters at the matrix step minimum.
Otherwise don't skip a step — the bugs that pass every test hide in the steps you skipped. (PLAYBOOK.md holds
the principle behind each step; this skill is its executable projection — keep the two in sync.)

## When to run it — and where each kind of change enters
- **New feature / new stateful surface / behaviour change:** the full pipeline from step 1.
- **Bug:** enter at the matrix step with a red-on-bug test (`bug → matrix → test → code`); if the fixed fact
  also lives in SPEC prose, update the spec sentence in the same change.
- **Removal of a shipped feature is a change too:** spec section → dated REMOVED tombstone · matrix rows
  retired (not left "BUILT") · owning tests deleted · SKILL.md / README swept — all the same session. (This
  is the step that actually got skipped once: an excision cleaned code + tests but left four doc surfaces dangling.)
- **Refactor (behaviour-neutral):** no spec/matrix delta, but enter at step 7 with the FULL suite + the
  visual sample set + a matrix audit of the touched sections (a monolith refactor re-risks everything).
- **Docs-only change:** re-read the changed section rendered + one grep that no stale claim contradicts the
  code; no spec/matrix step.
- **Skip entirely** only under the single boundary above (pure research, fact-gathering, a one-file
  no-new-behaviour edit already covered by a test level).

## The steps

1. **Spec — invoke `spec-author`.** Write or grow the project `SPEC.md`: entities, states, transitions,
   actors, invariants, and the cross-section composition between surfaces. One surface = one name. Compose
   every stateful surface across **every** view/mode axis it lives under, not just its own. Real gaps are
   marked `⟨DECIDE⟩` and asked, never guessed. Human-first language; codes at line ends.

2. **Prove — invoke `product-prover`.** The prover only catches a cross-section hole when both sides are
   present and named the same at prove-time — so a surface absent or unlinked then is invisible to it. Two
   modes (see product-prover): **FULL** (all phases, the WHOLE spec — required at MINOR gates and structural
   rewrites) and **CROSS-LINK** (the new surface's seams against the named existing surfaces — on every
   surface add). **Write the findings to the project's `docs/prover/YYYY-MM-DD.md` (in the repo under review, not in this
   skill's) with a per-finding folded / rejected(+why) column** so "fold every must-fix" is verifiable after a wipe; the next prover run opens by checking the
   previous file's unfolded rows. Fold every must-fix by the book; record should-clarify. Resolve every
   `⟨DECIDE⟩` that the surfaces under change TOUCH (ask the human when it's genuinely their call) and list the
   remaining open ones in the reply so the count is visible — don't gate on resolving all of them.

3. **Reconcile spec with reality.** Before deriving tests, verify the spec's claims about how the code
   actually behaves (each surface → owning `file:line` from a command you ran). Specs drift from code; fix
   the spec to the shipped truth, not the other way. (This is where "the prover assumed X, the code does Y"
   gets caught.) Running the greps/commands is junior work; judging what a mismatch MEANS is the senior's.

4. **Matrix — derive `TEST_MATRIX.md` from the proven spec.** It opens with an **artifact inventory** —
   every file the user receives (widget, catalog, README render) — and every inventory entry owns at least
   one rendered-level row. One row per invariant / state / transition, and **every row pins a test LEVEL**
   (string / DOM-text / browser-computed / pixel); any fact about visibility / layout / colour / interaction
   gets level ≥ browser-computed. The matrix is the bridge: tests come from the matrix, not from the code.
   (The mechanical projection is junior work; choosing each row's level + assertion is the senior's.)

5. **Test — write tests that assert the REAL shipped artifact.** Render the widget / produce the file /
   call the function and inspect the output — never a source-string match. Watch the new test FAIL first
   (red-on-bug), then implement. Never edit a test just to make a change pass.

6. **Code — implement until green.** Delegate well-scoped, mechanical implementation to a junior worker
   with a precise brief + a persistent checkpoint file (so a cut-off resumes, not restarts). Keep the hard
   parts (ambiguous specs, design, tricky debugging) on the senior model. Verify the junior's result by deed.

7. **Verify by deed.** Run it and see the result with your own eyes. Only call it done/working after that;
   otherwise label it an assumption. Run the whole suite before any push. **Green = zero failures AND the
   skip-set is exactly the expected pinned list** — an unexpected skip (Chrome absent, a real-data fixture
   missing) is a FAILURE, not a pass. **If red at a pause / session end: never commit; write the failing test
   name + hypothesis as the top `NEXT_STEPS.md` item** — the checkpoint IS the red test.

8. **Commit & show.** Commit when green with no regression (unasked). Bump the version (PATCH by default).
   Docs travel with the change — README + CHANGELOG + the skill's own `SKILL.md`, same session; diary the
   WHY in `JOURNAL.md`. Show the human the REAL render in a new window; push/deposit only after they've
   reviewed it. A push re-renders all deposited artifacts.

## Guardrails — the pipeline's TEETH (mechanical, every project inherits them)
The eight steps are guidance, and an agent DRIFTS from guidance — that is the failure that stops a project
converging (a whole panel ships empty; a behaviour nobody asked for gets buried; a change lands with no test).
So the pipeline is not trusted, it is ENFORCED: a `guardrails` check the project wires to a **git pre-push
hook** (+ the suite), so a change that fails ANY of these is RED and CANNOT be pushed. `test_traceability`
(below) is the first of these — generalise it to the full set. **Each project INSTANTIATES the checks for its
own surfaces; the pipeline REQUIRES the check exists and is green.** This is a first-class step, not a per-project
patch. The four mechanical guardrails:
- **Completeness** — a SURFACE REGISTRY + a render-scan test that fails if any user-facing surface is empty OR
  is rendered but not in the registry (so a new surface goes red until registered + asserted). No partial/
  stripped artifact can ship or be shown. Self-closing: the DOM is the source of truth, not a hand-list.
- **Tests-present** — a diff that touches a user-facing module MUST touch `tests/`. No change without a test.
- **Bounds (behaviour ↔ spec)** — every user-facing behaviour traces to a SPEC clause; a behaviour with no
  spec backing (a silent micro-decision — a default, an auto-mute, a sort order) is RED. This is what catches
  freelancing mechanically: you cannot ship an unasked, unrecorded behaviour.
- **Conflicts** — id duplicates, a spec invariant with no matrix row, a ⟨DECIDE⟩ marked RESOLVED but still
  live, a surface named two ways. (This is today's `test_traceability`, widened.)
**Honest boundary:** guardrails catch STRUCTURAL defects (empty surface, missing test, untraced behaviour,
partial artifact, id/naming conflict). They do NOT catch a subtle SEMANTIC bug (is the number right?) — that
still needs `product-prover` + a human's eyes. Enforce structure mechanically; reason about meaning with the
prover. Verify-by-deed (step 7) and push (step 8) both run the guardrails first; guidance and teeth agree.

## Gates worth remembering
- **Before a MINOR (0.x.0) bump:** the 3-pass preventive audit — product-prover on the whole spec + a matrix
  audit + a surface-composition check. Fix holes by the book; record the rest.
- **Order is law:** `spec → prove → matrix → test → code`; `bug → matrix → test → code`. Never code first and
  back-fill a spec.
- **Junior delegation (decided from the request, BEFORE the first tool call):** delegate when ≥1 holds —
  >3 files touched/read for facts · a known script/suite runs >~30s · the output is a report/list/dump · the
  edit strings or command are known verbatim. Tier: no-decision one-shot → haiku; multi-step mechanical →
  Sonnet; judgment/design → senior. The junior pastes RAW output (command + exit + failing lines) into a
  persistent checkpoint file as it goes — that raw output is evidence, its prose is only a lead. See PLAYBOOK.
- **Traceability is a test, not a vow.** A standing `test_traceability.py` fails the suite on a matrix row
  citing a missing test, a duplicate invariant id, a spec invariant with no matrix row, or a ⟨DECIDE⟩ marked
  RESOLVED that still carries the live marker — so drift is caught every commit, not once per MINOR.

## How it relates to the other skills
- `spec-author` — writes/grows the spec (step 1). Public.
- `product-prover` — reviews the whole spec with formal-verification thinking (step 2). Public.
- `build-pipeline` (this) — the orchestrator that sequences them through to a shipped, verified, committed
  change.

> The method, made durable: spec-author and product-prover each own one step; build-pipeline is the spine that
> runs the whole arc from a spec to a shipped, tested, committed change.

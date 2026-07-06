---
name: build-pipeline
description: >
  Run a non-trivial change by the book — the spec → prove → architecture → prove architecture → matrix →
  test → code → verify → commit & show pipeline, orchestrating the spec-author and product-prover skills. Use this whenever starting a new
  feature, a new stateful surface, or a behaviour change that deserves more than a one-line edit:
  "build X properly", "do this by the method", "spec and ship Y", "new surface for Z". It is the
  executable projection of the method (PLAYBOOK.md — in the private playbook repo, not this one — holds the principle) so the method survives memory
  wipes. NOT for tiny reversible edits (those shortcut straight to code + a test) or pure research/fact-gathering.
metadata:
  version: 0.2.26
---

# build-pipeline — ship a change by the method

> Part of the **live-spec pack** — the shared working rules (ask-never-guess · plain words, anchors trail ·
> one surface = one name · one home per fact · junior/senior split · checkpoints · the concurrent-edit
> fence · freshness · journal discipline · attic-never-delete · verify by deed · the human's gates · claims
> need primary sources · fix the class, sweep look-alikes · the door before code · prototype ≠ product) live ONCE in the pack's base skill, `live-spec-base` (v0.1.16), together with the
> settings ladder — this skill references them and elaborates only its own domain. Used standalone, this
> note is plain advice.

One pipeline, each step has a tool. The order is **spec → prove → architecture → prove architecture →
matrix → test → code → verify → commit & show**. A bug shortcuts to **bug → matrix → test → code** (citing the
existing architecture node it lands in). **Skip the pipeline only if ALL hold:** single
file · no new state / element / user-visible behaviour · an existing test level already covers the touched
fact (still ship a test). Anything touching visibility / layout / colour enters at the matrix step minimum.
Otherwise don't skip a step — the bugs that pass every test hide in the steps you skipped. (The private playbook repo's PLAYBOOK.md holds
the principle behind each step; this skill is its executable projection — keep the two in sync.)

**The craft ladder — whose head you wear at each step (SPEC INV-33).** Each artifact is judged by its
craft's standards, not a generalist's: **spec** — a strong product manager (the user's journey, the
product's words) · **prove / prove architecture** — the prover's formal-methods reviewer ·
**architecture** — a software architect (nodes, seams, one responsibility each) · **matrix** — a QA
automation lead deriving coverage · **test** — the same QA engineer writing it · **code** — a senior
developer · **verify** — the visitor's own eyes, not the builder's · **commit & show** — a careful
release hand whose reader is the human. The landing report's step accounting speaks in these standards,
and the hat each artifact was made under is namable on ask. The craft wears the work-KIND's face
(SPEC INV-22, INV-33): on a prose product the code step is worked as a strong writer, on infra as a
toolsmith — the ladder names the archetypes, the kind says what their standards look like in its medium.

## When to run it — and where each kind of change enters
- **Step zero, before ANY tool call: name the door aloud (SPEC T-12, INV-16; base rule 15) — and the human hears the intake line back as the capture echo: heard · door · name · row · place on the map (communicator rule 12; SPEC INV-27, INV-37).**
  - The intake line states size (a wish too big for its worth is negotiated in SCOPE — cut surfaces or
    split into stages, never a time budget or estimate; proposals proceed on the recommended option and
    are surfaced, SPEC T-15) · priority · door: feature · bug · refactor · docs-only · skip · work-kind: product · infra · skill ·
    prose — what the wish BUILDS, one kind per wish, scaling the FORM of every step it walks (the
    work-kind table below; SPEC T-16, INV-22). The same line PLACES the wish on the product's feature
    map — **changes feature X · a new feature · restructure** — spoken in the echo and written in the
    row's `map:` note; the map is the spec's scenario sections plus the architecture's nodes, never a
    third document, and a restructure verdict queues its OWN row (refactor door if only structure
    moves, feature door if behaviour moves too) — the re-carve happens only through the architecture
    step and its re-prove (SPEC INV-37).
  - Tripwires decide, not judgment — a new user-visible surface · new persistent state · a new interaction on an existing surface
    · the spec marks the touched surface [target] · behaviour no spec clause backs ⇒ FEATURE, however
    casually asked. The tripwire verdict outranks a casual "bugfix" label, and queue-cutting belongs to the
    bug door alone — a re-doored wish takes no preemption.
  - Re-fire the door mid-work the moment the work is
    about to create a surface or state its door doesn't grant: STOP, reclassify, continue by the right
    door.
  - **One wish = one user story (SPEC T-17):** a wish carrying several distinct things a person will DO and SEE splits at intake — each story its own row through the full pipeline (stages slice ONE story's depth, T-15's knife; separate stories never fuse into one row); sub-behaviours (a hover face, a phone face, a backpointer) are the story's ACCEPTANCE, not new stories; unclear whether it is one story or two ⇒ ask at intake, and every row born of a split cites the one spoken wish it came from. A request to merely SEE/TRY with no commitment goes to a labelled prototype home instead (base
    rule 16) — never into prod, never shown as product.
- **New feature / new stateful surface / behaviour change:** the full pipeline from step 1.
- **Bug:** enter at the matrix step with a red-on-bug test (`bug → matrix → test → code`); if the fixed fact
  also lives in SPEC prose, update the spec sentence in the same change. **The reported defect is a sample
  of its class (base rule 14):** before calling it done, name the pattern, grep the repo for it, check the
  visible text of every user-facing surface, and fix all siblings in the same change — the matrix row and
  the red-on-bug test cover the CLASS, not the single instance. **A RECURRING bug re-doors to feature:**
  a second bug in the same area within ~30 days is not another patch — the area is missing an INVARIANT,
  so it escalates to the full pipeline from step 1 (spec the invariant, re-prove, then fix under it).
  The journal is how you notice: before taking any bug, grep JOURNAL.md for the area's name and check
  the dates.
- **Removal of a shipped feature is a change too:** spec section → dated REMOVED tombstone · matrix rows
  retired (not left "BUILT") · owning tests deleted · SKILL.md / README swept — all the same session. (This
  is the step that actually got skipped once: an excision cleaned code + tests but left four doc surfaces dangling.)
- **Refactor (behaviour-neutral):** no spec/matrix delta, but enter at step 8 with the FULL suite + the
  visual sample set + a matrix audit of the touched sections (a monolith refactor re-risks everything);
  if the refactor moves node boundaries, ARCHITECTURE.md's pins update in the same change.
- **Docs-only change:** re-read the changed section rendered + one grep that no stale claim contradicts the
  code; no spec/matrix step.
- **Skip entirely** only under the single boundary above (pure research, fact-gathering, a one-file
  no-new-behaviour edit already covered by a test level).

## When NOT to run it

Not for the skip-boundary edit (single file · no new state, element, or visible behaviour · an existing
test level already covers the touched fact — it still ships a test, just no pipeline); not for pure
research or fact-gathering (no artifact changes); not for a SEE/TRY ask (that goes to the labelled
prototype home, base rule 16 — and comes BACK through this pipeline only at promotion).

## The work-kind table — WHAT the wish builds scales HOW each step runs (SPEC T-16, INV-22)

The door picks WHICH steps run; the kind picks the FORM each running step takes. The work-kind table
below is the per-kind meanings' ONE normative home (the spec binds the contract around it). The
contract, before the table: at landing, every door-granted step has either **APPLIED in its kind's form
or STOOD DOWN by name** in the landing report ("design-sync — text product, stands down") — a silently
skipped step is a defect. **An unresolved kind scales nothing down** — standing a step down requires a
NAMED kind (the ask rides the row, SPEC INV-12). And no kind ever touches the safety net: the door law
and its tripwires, the delta's mandatory sentences (fences · facets · non-goals · success measure),
ask-at-intake — the same law a scope cut obeys (SPEC T-15).

| Step | product (a user faces it) | infra (tooling for the project) | skill (an agent works by it) | prose (a human reads it) |
|---|---|---|---|---|
| 1 spec | full delta: fences, axes, facet sweep over visible surfaces | the tool's contract: inputs → outputs, failure behaviour, where it runs; usually "no visible surface — facets N/A" | the behaviour it must produce: trigger, the correction it makes, when NOT to fire | the reader, the claims, the reading path; visual facets only if it renders |
| 2 prove | as written | as written | as written | as written — the prover reads documents natively |
| 3 architecture | nodes + `file:line` pins | one node owns the tool, pinned to its entry point | the skill IS a node; pin its SKILL.md | owned by a docs node; new node only if structure grows |
| 4 prove architecture | when structure changed | same | same | usually stands down — assignment, no structure change |
| 5 matrix | rendered-level rows (E-15) | function-level rows: run the tool, assert real output | string rows on the SHIPPED SKILL.md; behaviour eval when the eval machinery lands (row 94) | render-level: file shipped, sections present, links resolve |
| 6 test | assert the real render | run on a fixture, assert output | string assertions against the installed artifact | assert the shipped file's content |
| 7 code | as written | as written | as written | the writing IS the step |
| 8 verify by deed | open the real artifact, eyes on it — then the VISITOR WALK (first visit · return · cross-entry · from-any-point navigation · exits) and the FEEL pass (motion quality, affordance craft) against the approved prototype's bar; findings become rows or red (SPEC INV-30) | one real run, eyes on the output | re-read the INSTALLED copy; fire the trigger once where cheap | render it by the show rule and READ it |
| 9 commit & show | show the render | show the run's output | version bump + installed-copy sync, same session | open the rendered page for the human |
| design-sync / snapshot | product with visuals: declared scope syncs (human-gated) | stands down | stands down | stands down |

## The steps

1. **Spec — invoke `spec-author`.** Write or grow the project `SPEC.md`: entities, states, transitions,
   actors, invariants, and the cross-section composition between surfaces. One surface = one name. Compose
   every stateful surface across **every** view/mode axis it lives under, not just its own. Real gaps are
   marked `⟨DECIDE⟩` and asked, never guessed. Human-first language; codes at line ends. A feature-doored
   wish also walks the **fit walk** — the kind-scaled product-fit interrogation (journey · flows ·
   trigger lenses; lens lists live in spec-author; prover mode FEATURE-FIT; SPEC INV-29) — and the
   **standard-facet sweep** (the canonical list lives in spec-author): phone/narrow
   layout · touch-vs-hover · empty/error/loading · accessibility · performance — every facet ends as a
   spec sentence, decided or `[default]`-tagged and TOLD at landing as a plain-words tradeoff, never a
   confirmation request (SPEC INV-31); a
   mid-work re-door walks the sweep before work resumes (SPEC T-13, INV-18). And when the wish touches a
   surface that already lives, the delta opens with **regression fences** BEFORE that sweep — neighbouring
   promises that must stay true, each citing the clause it guards, named by anchor in the wish's row; a
   fence discharges through the cited clause's existing never-side row, never a new row (SPEC T-14, INV-19).
   The delta CLOSES with its two sentences — non-goals ("nothing left out" is valid, a narrowing one is
   surfaced) and one success measure, decided or `[default]`-tagged (SPEC INV-20, INV-21).

2. **Prove — invoke `product-prover`.** The prover only catches a cross-section hole when both sides are
   present and named the same at prove-time — so a surface absent or unlinked then is invisible to it. Two
   modes (see product-prover): **FULL** (all phases, the WHOLE spec — required at MINOR gates and structural
   rewrites) and **CROSS-LINK** (the new surface's seams against the named existing surfaces — on every
   surface add). **Write the findings to the project's `docs/prover/YYYY-MM-DD.md` (in the repo under review, not in this
   skill's) with a per-finding folded / rejected(+why) column** so "fold every must-fix" is verifiable after a wipe; the next prover run opens by checking the
   previous file's unfolded rows. Fold every must-fix by the book; record should-clarify. Resolve every
   `⟨DECIDE⟩` that the surfaces under change TOUCH (ask the human when it's genuinely their call) and list the
   remaining open ones in the reply so the count is visible — don't gate on resolving all of them.

3. **Architecture — write or update `ARCHITECTURE.md` from the proven spec** (template:
   `ARCHITECTURE.template.md` — template paths here and in step 5 resolve from the PACK repo,
   github.com/happysasha18/live-spec; a standalone install fetches them there, never from the skill
   dir: the pack is the source, a copy would fork the truth). Named nodes, one responsibility and one name each; every spec fact OWNED
   by exactly one node; named seams between nodes. In a live codebase every node pins to its owning
   `file:line` — **this step is where the spec is reconciled with reality**: each pin comes from a command
   you ran, never from the doc's own prose, your memory, or a worker's summary — those are leads to verify
   (base rule 13). Specs drift from code; fix the spec to the shipped truth, not the other way. A large or
   surface-class change updates the doc; a bug or small change just cites its existing node and skips to
   the matrix. (Running the pin-greps is junior work; judging what a mismatch MEANS is the senior's.)
   **The doc is ITERATIVE — never written milestones ahead:** it maps the product as it stands plus the
   landing in flight. A node exists for what ships today, or for what the spec already promises under an
   owned queue row (marked [target], pin empty). A future feature earns its node when its landing arrives;
   a speculative node is unbacked structure — the prover flags it, and "should I architect the next few
   milestones now?" is answered NO by the method, not by taste. Re-carving the whole node map IS
   legal — it arrives as a restructure placement's own queue row (SPEC INV-37), walks this step, and
   is re-proven like any structure change; a placement may SAY the shape no longer fits, only a
   landing changes the shape.

4. **Prove the architecture — invoke `product-prover` with the architecture lens** whenever the doc
   changed in step 3: every spec fact has an owning node · no node stands without spec backing · every
   seam names what crosses it and who owns the format. Findings land in the same `docs/prover/` record
   discipline as step 2.

5. **Test spec — DERIVE `TEST_MATRIX.md` from the proven spec through the proven architecture.** The
   matrix is derived, never just filled: rows organized **architecture node × spec fact** (one block per
   node), every fact gets ≥ 1 row, **every row states BOTH sides — what the fact DOES and what it must
   NEVER do** (the never side IS the regression fence, SPEC INV-6; a row without it is a derivation
   defect), and **every row pins a test LEVEL** (string / DOM-text /
   browser-computed / pixel); any fact about visibility / layout / colour / interaction gets level ≥
   browser-computed. It opens with an **artifact inventory** — every file the user receives — and every
   inventory entry owns at least one rendered-level row. Derivation CLOSES with the template's **coverage
   validation checklist, actually walked** (every anchor ≥ 1 row · every node's negative-side rows exist ·
   no stale refs); a fact with no row or at a too-weak level is a derivation defect, fixed here. The
   matrix is the bridge: tests come from the matrix, not from the code. (The mechanical projection is
   junior work; choosing each row's level + assertion is the senior's.)

6. **Test — write tests that assert the REAL shipped artifact.** Render the widget / produce the file /
   call the function and inspect the output — never a source-string match. Watch the new test FAIL first
   (red-on-bug), then implement. Never edit a test just to make a change pass.

7. **Code — implement until green.** Delegate well-scoped, mechanical implementation to a junior worker
   with a precise brief + a persistent checkpoint file (so a cut-off resumes, not restarts). Keep the hard
   parts (ambiguous specs, design, tricky debugging) on the senior model. Verify the junior's result by deed.

8. **Verify by deed.** Run it and see the result with your own eyes. Only call it done/working after that;
   otherwise label it an assumption. Run the whole suite before any push. **Green = zero failures AND the
   skip-set is exactly the expected pinned list** — an unexpected skip (Chrome absent, a real-data fixture
   missing) is a FAILURE, not a pass. **If red at a pause / session end: never commit; write the failing test
   name + hypothesis as the top `NEXT_STEPS.md` item** — the checkpoint IS the red test.

9. **Commit & show.** Commit when green with no regression (unasked). Bump the version (PATCH by default).
   Docs travel with the change — README + CHANGELOG + the skill's own `SKILL.md`, same session; diary the
   WHY in `JOURNAL.md`. **The CHANGELOG speaks to the USER, the journal to the builder:** each entry says
   what changed for the person using the product, with one concrete example from real output — never
   function names, internal ids, or row numbers (those live in the journal). And no doc pins a drifting
   version number in prose — "current version: vX.Y" always goes stale; point at the version's one home
   (the VERSION file, the frontmatter) or omit it. The landing report TELLS the taste choices made
   without asking — the open `[default]`s — each in plain words with an example and a tweakable mark;
   no confirmation requested, silence is consent, never re-asked (SPEC INV-31). Show the human the REAL render in a new window; push/deposit only
   after they've reviewed it. A push re-renders all deposited artifacts. Where the host's design-sync is ON (base
   defaults; SPEC E-18), the landing's DECLARED components also sync to the team's design project — after
   the human's gate, never instead of the in-session show.

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
prover. Verify-by-deed (step 8) and commit/push (step 9) both run the guardrails first; guidance and teeth agree.

## The excuses table — read it the moment one of these crosses your mind

The shortcuts that kill the method never announce themselves; they arrive as one of these thoughts.
Each is a tripwire: thinking it means STOP and take the pipeline door you were about to skip.

| The thought | Why it is a trap |
|---|---|
| "it's a one-liner / just a prototype" | The Room was "just to see" — it shipped hover-only with no phone layout and no spec. Size never picks the door; the tripwires do (base rule 15). |
| "I'll write the spec after it works" | Spec-after-code documents what you built, not what was asked; the prover can no longer catch the difference (spec-author anti-pattern). |
| "the human is in a hurry" | Urgency moves PRIORITY, never the door — a critical feature heads the queue, it still enters at the spec step (SPEC T-12). |
| "the suite is green, ship it" | Green proves the facts the matrix knows; an unspecced surface has no rows, so green says nothing about it (SPEC INV-15). |
| "asking would bother them" | Batched questions exist exactly for this; a silent guess costs a re-build, the batch costs one read (SPEC INV-4, INV-5). |
| "долго объяснять — сам быстрее сделаю" | That is delegation dying, and the senior drowning in junior work; write the self-contained brief (the delegation rule above). |

## Gates worth remembering
- **Before a MINOR (0.x.0) bump:** the 3-pass preventive audit — product-prover on the whole spec + a matrix
  audit + a surface-composition check. Fix holes by the book; record the rest.
- **Order is law:** `spec → prove → architecture → prove architecture → matrix → test → code`;
  `bug → matrix → test → code`. Never code first and back-fill a spec — and never jump from spec straight
  to tests: the two layers between them (architecture, test-spec derivation) are where whole classes of
  holes get caught (SPEC E-14/E-15/INV-15).
- **A row closes only whole (SPEC INV-26):** where a row carries several legs, its Done-when enumerates each, and the landing report may close the row only with EVERY leg met — half-done is a status, never a landing; an open leg keeps the row in-work, and the resume file's LIVE-STATE restates it at every supersession, never compresses it away (still open at compaction ⇒ restated, not summarized out).
- **Two trains, one pen (SPEC T-18, INV-39):** one session may roll at most two INDEPENDENT build lanes —
  no shared surface, no shared spec section; opening the second is narrated and both trains ride the
  departures board, the waiting lane naming whom it waits behind. Only penless stages overlap: the second
  train's code and tests in an isolated tree (its delta integrates only under the pen; the disjoint-file
  road stays within one lane), read-only analysis free. Every shared-doc edit, the integration, and the
  closing of a row take the pen one lane at a time — a pen-stage is never cut mid-edit — and a landing
  commit carries exactly one row's delta, its gate run on a tree clean of the other lane's unfinished
  work; after a landing, the waiting lane re-fences and re-runs its gate on the new truth. Never across
  sessions, never mid-milestone; a bug takes the pen at the end of the current pen-stage and parks every
  rolling lane, each at its own checkpoint, resuming in landing order.
- **Junior delegation (decided from the request, BEFORE the first tool call):** delegate when ≥1 holds —
  >3 files touched/read for facts · a known script/suite runs >~30s · the output is a report/list/dump · the
  edit strings or command are known verbatim. Tier: no-decision one-shot → haiku; multi-step mechanical →
  Sonnet; judgment/design → senior. The junior pastes RAW output (command + exit + failing lines) into a
  persistent checkpoint file as it goes — that raw output is evidence, its prose is only a lead. **The
  brief is self-contained (the BMAD story-file lesson):** delegated work ships as one document embedding
  the EXACT spec sentences it serves, the exact edit strings or commands, the checks to run, and the
  checkpoint path — the worker never hunts context, never interprets the spec, never decides. If writing
  the brief means deciding something first, that decision is the senior's and happens BEFORE delegation
  — "долго объяснять" is how delegation silently dies. See the private playbook repo's PLAYBOOK.md. **The worker contract (SPEC
  ACT-3):** the brief NAMES the files the worker may write — its session's write-ownership narrowed to
  exactly those, reads free, writes fenced; same-session sibling-worker files are fence-benign (the
  concurrent-edit fence alarms on foreign sessions, not on your own briefed hands — the senior who
  briefed both owns the seams between briefs); the session's live setting lines ride into the brief
  verbatim — a worker never resolves the settings ladder itself, it cannot hear the human's spoken
  word; the brief ARMS the worker for the workshop — it carries the host's problem-ledger path
  (`.live-spec/PROBLEMS.md`) with the WATCHED-line duty: workshop noise the worker hits (a flaky
  harness, a missing dependency, a tool misbehaving) goes into its checkpoint as a ledger line —
  signature, date, one line of context — never a silent retry, and the senior carries the lines into
  the ledger at verify (SPEC INV-23); and it carries the CLOCK — the date and time read at briefing —
  so the worker stamps its checkpoint and any dated output from the brief's clock, never an invented
  hour (SPEC INV-24; a worker WITH a shell re-reads the machine clock itself — the brief's line is the
  floor for one without, and elapsed time is never guessed); and a result failing its brief's acceptance escalates ONE tier with a logged
  line — never a silent retry on the same tier, never a skipped rung. **Every delegation reports its saving:** the
  landing report carries one line — what went to the worker and roughly how much senior work it saved.
  The line is what keeps the habit alive; a session that never writes it is a session that quietly
  stopped delegating.
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

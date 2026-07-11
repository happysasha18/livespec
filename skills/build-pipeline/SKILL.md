---
name: build-pipeline
description: >
  Run a non-trivial change by the book — the spec → prove → architecture → prove architecture → matrix →
  test → code → verify → commit & show pipeline, orchestrating the pack's working skills (spec-author,
  product-prover, test-author). Use this whenever starting a new
  feature, a new stateful surface, or a behaviour change that deserves more than a one-line edit:
  "build X properly", "do this by the method", "spec and ship Y", "new surface for Z". It is also the
  entry point for bugs, refactors, docs-only changes, and feature removals — a bug enters at the matrix
  step with a red-on-bug test. NOT for tiny reversible edits (those shortcut straight to code + a test) or pure research/fact-gathering.
metadata:
  version: 1.0.6
---

# build-pipeline — ship a change by the method

> Part of the **live-spec pack** — the shared working rules (ask-never-guess · plain words, anchors trail ·
> one surface = one name · one home per fact · junior/senior split · checkpoints · the concurrent-edit
> fence · freshness · journal discipline · attic-never-delete · verify by deed · the human's gates · claims
> need primary sources · fix the class, sweep look-alikes · the door before code · prototype ≠ product) live ONCE in the pack's base skill, `live-spec-base` (v1.0.5), together with the
> settings ladder — this skill references them and elaborates only its own domain. Used standalone, this
> note is plain advice.

One pipeline, each step has a tool. The order is **spec → prove → architecture → prove architecture →
matrix → test → code → verify → commit & show**. A bug shortcuts to **bug → matrix → test → code** (citing the
existing architecture node it lands in). **Skip the pipeline only if ALL hold:** single
file · no new state / element / user-visible behaviour · an existing test level already covers the touched
fact (still ship a test; the order of test and fix follows test-author's small-fix path — red first by
default, and a one-batch fix owes the mechanical red proof). A skip still owes the door step's spec-backed-literal tripwire: does this edit touch a spec-backed literal or clause? A yes routes the docs and the test into the same session as the fix (SPEC INV-104). Anything touching visibility / layout / colour enters at the matrix step minimum.
Otherwise don't skip a step — the bugs that pass every test hide in the steps you skipped. (The private playbook repo's PLAYBOOK.md holds
the principle behind each step. This skill is its executable projection; keep the two in sync.)

**The craft ladder — whose head you wear at each step (SPEC INV-33).** Each artifact is judged by its
own craft's standards: **spec** — a strong product manager (the user's journey, the
product's words) · **prove / prove architecture** — the prover's formal-methods reviewer ·
**architecture** — a software architect (nodes, seams, one responsibility each) · **matrix** — a QA
automation lead deriving coverage · **test** — the same QA engineer writing it · **code** — a senior
developer · **verify** — the visitor's own fresh eyes, the builder's own view set aside · **commit & show** — a careful
release hand whose reader is the human.

The landing report's step accounting speaks in these standards. The hat each artifact was made under is
namable on ask.

The craft wears the work-KIND's face (SPEC INV-22, INV-33): on a prose product the code step is worked as
a strong writer, on infra as a toolsmith. The ladder names the archetypes, and the kind says what their
standards look like in its medium.

## When to run it — and where each kind of change enters
- **Step zero, before ANY tool call: name the door aloud (SPEC T-12, INV-16; base rule 15) — and the human hears the intake line back as the capture echo: heard · door · name · row · place on the map (communicator rule 12; SPEC INV-27, INV-37).**
  - The intake line states size (a wish too big for its worth is negotiated in SCOPE — cut surfaces or
    split into stages, never a time budget or estimate; proposals proceed on the recommended option and
    are surfaced, SPEC T-15) · priority · door: feature · bug · refactor · docs-only · skip · work-kind: product · infra · skill ·
    prose — what the wish BUILDS, one kind per wish, scaling the FORM of every step it walks (the
    work-kind table below; SPEC T-16, INV-22).

    The same line PLACES the wish on the product's feature map — **changes feature X · a new feature ·
    restructure** — spoken in the echo and written in the row's `map:` note. The map is the spec's scenario
    sections plus the architecture's nodes, never a third document. A restructure verdict queues its OWN row
    (refactor door if only structure moves, feature door if behaviour moves too); the re-carve happens only
    through the architecture step and its re-prove (SPEC INV-37).
  - Tripwires decide by rule, ahead of judgment — a new user-visible surface · new persistent state · a new interaction on an existing surface
    · the spec marks the touched surface [target] · behaviour no spec clause backs ⇒ FEATURE, however
    casually asked. The tripwire verdict outranks a casual "bugfix" label, and queue-cutting belongs to the
    bug door alone — a re-doored wish takes no preemption.
  - Re-fire the door mid-work the moment the work is
    about to create a surface or state its door doesn't grant: STOP, reclassify, continue by the right
    door.
  - **A declared mockup-first entry condition is honoured from the row, cancelled only by name (SPEC
    INV-43).** A story whose intake said "show me first, then build" carries the condition WRITTEN in
    its queue row ("entry: mockup-first"); a later general "go build" moves priority, never the
    condition — only by the human naming it does the condition fall. A condition living only in chat
    memory is the defect this line kills (the tlvphoto door was built past its voiced mockup-first word).
  - **One wish = one user story (SPEC T-17):** a wish carrying several distinct things a person will DO and
    SEE splits at intake — each story its own row through the full pipeline (stages slice ONE story's depth,
    T-15's knife; separate stories never fuse into one row). Sub-behaviours (a hover face, a phone face, a
    backpointer) are the story's ACCEPTANCE, folded into the one story. Unclear whether it is one story or
    two ⇒ ask at intake, and every row born of a split cites the one spoken wish it came from. A request to
    merely SEE/TRY with no commitment goes to a labelled prototype home instead (base rule 16) — it stays a
    prototype, outside prod and unshown as product.
- **New feature / new stateful surface / behaviour change:** the full pipeline from step 1.
- **Bug:** enter at the matrix step with a red-on-bug test (`bug → matrix → test → code`); if the fixed fact
  also lives in SPEC prose, update the spec sentence in the same change. **The door step adds one tripwire at the bug door:** does this edit touch a spec-backed literal or clause (a version string, a pinned count, a named vocabulary, a promised wording)? A yes binds the docs-travel-with-the-change rule and the red-first small-fix path into one duty — the docs and the test land in the same session as the fix; the tripwire reads the edit's content, so a one-word change to a spec-cited literal owes the same duty as a full feature (born of the row 220 audit: one-line fixes touching spec-backed literals shipped without same-session doc sync, 2026-07-10; SPEC INV-104). **The reported defect is a sample
  of its class (base rule 14):** before calling it done, name the pattern, grep the repo for it, check the
  visible text of every user-facing surface, and fix all siblings in the same change — the matrix row and
  the red-on-bug test cover the CLASS, beyond the single instance. **A RECURRING bug re-doors to feature:**
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
- **A rewrite or restyle accounts for every removal of substance (SPEC INV-109):** A rewrite or restyle that removes substance — a section, an argument, a rationale, a worked example — lists every removal in its landing report, one line of judgment each: the fact was kept and where, the owner killed it by name, or the rewriter proposes dropping and asks. A removal the rewriter cannot justify becomes a question before the report closes. Never a silent cut of substance. The rule scopes to substance and leaves line-level wording free, so a tightened sentence or a reordered clause needs no accounting. The accounting rides the landing report the communicator builds; the docs-only door above and the restyle loop both carry it. (Born of a compressed README section restored the same session, 2026-07-10.)
- **Skip entirely** only under the single boundary above (pure research, fact-gathering, a one-file
  no-new-behaviour edit already covered by a test level).

## When NOT to run it

Skip it for the skip-boundary edit (single file · no new state, element, or visible behaviour · an existing
test level already covers the touched fact — it still ships a test, just no pipeline); not for pure
research or fact-gathering (no artifact changes); not for a SEE/TRY ask (that goes to the labelled
prototype home, base rule 16 — and comes BACK through this pipeline only at promotion).

## The work-kind table — WHAT the wish builds scales HOW each step runs (SPEC T-16, INV-22)

The door picks WHICH steps run. The kind picks the FORM each running step takes. The work-kind table
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
| 8 verify by deed | open the real artifact, eyes on it — then the VISITOR WALK (first visit · return · cross-entry · from-any-point navigation · exits) and the FEEL pass (motion quality, affordance craft) against the approved prototype's bar; findings become rows or red (SPEC INV-30) | one real run, eyes on the output | re-read the INSTALLED copy; fire the trigger once where cheap; walk the installed skill-creator's review of the touched skill — format, frontmatter, description-triggering (does the skill load when it should), evals where applicable — findings folded or rejected by name in the landing record (SPEC INV-99) | render it by the show rule and READ it |
| 9 commit & show | show the render | show the run's output | version bump + installed-copy sync, same session | open the rendered page for the human |
| design-sync / snapshot | product with visuals: declared scope syncs (human-gated) | stands down | stands down | stands down |

## The steps

1. **Spec — invoke `spec-author`.** Write or grow the project `PRODUCT_SPEC.md`: entities, states, transitions,
   actors, invariants, and the cross-section composition between surfaces. One surface = one name. Compose
   every stateful surface across **every** view/mode axis it lives under, not just its own. Real gaps are
   marked `⟨DECIDE⟩` and asked, never guessed. Use human-first language, with codes at line ends.

   A feature-doored wish also walks the **fit walk** — the kind-scaled product-fit interrogation (journey ·
   flows · trigger lenses; lens lists live in spec-author; prover mode FEATURE-FIT; SPEC INV-29) — and the
   **standard-facet sweep** (the canonical list lives in spec-author): phone/narrow layout · touch-vs-hover ·
   empty/error/loading · accessibility · performance. Every facet ends as a spec sentence, decided or
   `[default]`-tagged and TOLD at landing as a plain-words tradeoff, never a confirmation request (SPEC
   INV-31). A mid-work re-door walks the sweep before work resumes (SPEC T-13, INV-18).

   And when the wish touches a surface that already lives, the delta opens with **regression fences** BEFORE
   that sweep — neighbouring promises that must stay true, each citing the clause it guards, named by anchor
   in the wish's row. A fence discharges through the cited clause's existing never-side row, never a new row
   (SPEC T-14, INV-19).

   The delta CLOSES with its two sentences — non-goals ("nothing left out" is valid, a narrowing one is
   surfaced) and one success measure, decided or `[default]`-tagged (SPEC INV-20, INV-21).

2. **Prove — invoke `product-prover`.** The prover only catches a cross-section hole when both sides are
   present and named the same at prove-time — so a surface absent or unlinked then is invisible to it. Two
   modes (see product-prover): **FULL** (all phases, the WHOLE spec — required at MINOR gates and structural
   rewrites) and **CROSS-LINK** (the new surface's seams against the named existing surfaces — on every
   surface add). **Write the findings to the project's `docs/prover/YYYY-MM-DD.md` (in the repo under review, separate from this
   skill's) with a per-finding folded / rejected(+why) column** so "fold every must-fix" is verifiable after
   a wipe. The next prover run opens by checking the previous file's unfolded rows. Fold every must-fix by
   the book, and record should-clarify. Resolve every `⟨DECIDE⟩` that the surfaces under change TOUCH (ask
   the human when it's genuinely their call), and list the remaining open ones in the reply so the count is
   visible — don't gate on resolving all of them.

3. **Architecture — write or update `ARCHITECTURE.md` from the proven spec** (template:
   `ARCHITECTURE.template.md` — template paths here and in step 5 resolve from the PACK repo,
   github.com/happysasha18/live-spec; a standalone install fetches them there, never from the skill
   dir: the pack is the source, a copy would fork the truth). Named nodes, one responsibility and one name
   each. Every spec fact is OWNED by exactly one node. Named seams run between the nodes. The project's kind
   (`project.kind`, SPEC INV-36) PROPOSES the starting node structure — a fullstack app splits frontend /
   backend / template / store, a CLI one node per command, a skill pack one node per skill — and the
   template's "Node structure by project.kind" table carries the per-kind scaffold; the spec's facts then
   decide the final nodes, a speculative node still being unbacked structure the prover flags.

   In a live codebase every node pins to its owning `file:line`. **This step is where the spec is reconciled
   with reality:** each pin comes from a command you ran, never from the doc's own prose, your memory, or a
   worker's summary — those are leads to verify (base rule 13). Specs drift from code, so fix the spec to the
   shipped truth, always in that one direction.

   A large or surface-class change updates the doc. A bug or small change just cites its existing node and
   skips to the matrix. (Running the pin-greps is junior work; judging what a mismatch MEANS is the senior's.)
   **The architecture owes NUMBERS, not only names (SPEC INV-41):** measurable quality budgets plus
   each budget's instrumentation home — where the real numbers are measured and where a human can
   read them (an export, a debug view, a report).

   WHAT is measurable comes from the project's KIND (SPEC INV-36): ask "what does quality MEAN here, in
   numbers?" before writing any. A user-facing product measures paint/interaction times ("first image
   within 2 s on a cold visit"); a backend service latency, throughput, error rate; a CLI or pipeline run
   time on a typical input and per-unit cost; a skill pack its evals' pass rate and suite wall-time; prose
   what honestly HAS a number. A quality with no honest number is SAID by name, never given a vanity metric.

   Each budget is asserted by a matrix-row acceptance, never a hope in prose. A surface with no budget line
   and no instrumentation home is a derivation defect, exactly like an unowned fact. The numbers are the
   host's taste: propose with a recommendation, set on the human's word at the surface's first budget
   landing.

   **The doc owes two more views beside the node map (SPEC INV-74, INV-75), scaled by kind:** the
   **runtime view** walks every flow the spec promises through the nodes — which node serves each step,
   what crosses each hop (citing the seam by name; the payload and format stay the seam table's fact),
   where the flow can fail; a flow the doc cannot walk end to end is a finding. The **placement view**
   states every node's place — build-time on the author's machine · CDN static · client browser · edge
   worker · external service — plus the load-bearing technology choice where one exists, first-class (a
   node-table column or its own small table), so the reader answers "where does this run" at a glance.
   The per-kind flow unit and both section shapes live in the template; a book satisfies each view with
   one sentence.
   **The doc is ITERATIVE, current only to what's shipped or in flight:** it maps the product as it stands
   plus the landing in flight. A node exists for what ships today, or for what the spec already promises
   under an owned queue row (marked [target], pin empty).

   A future feature earns its node when its landing arrives. A speculative node is unbacked structure — the
   prover flags it. "Should I architect the next few milestones now?" is answered NO strictly by the method,
   taste playing no part.

   Re-carving the whole node map IS legal: it arrives as a restructure placement's own queue row (SPEC
   INV-37), walks this step, and is re-proven like any structure change. A placement may SAY the shape no
   longer fits; only a landing changes the shape.

4. **Prove the architecture — invoke `product-prover` with the architecture lens** whenever the doc
   changed in step 3 — six checks, each at the project's kind scale: every spec fact has an owning node ·
   no node stands without spec backing · every seam names what crosses it and who owns the format · the
   quality budgets are stated with their instrumentation homes (INV-41) · the runtime view walks every
   promised flow (INV-74) · the placement view says where every node runs (INV-75). Findings land in the
   same `docs/prover/` record discipline as step 2.

5. **Test spec — invoke `test-author` to DERIVE `TEST_MATRIX.md` from the proven spec through the proven architecture (the method's one home, SPEC E-27).** The
   matrix is derived, never just filled: rows organized **architecture node × spec fact** (one block per
   node), every fact gets ≥ 1 row, **every row states BOTH sides — what the fact DOES and what it must
   NEVER do** (the never side IS the regression fence, SPEC INV-6; a row without it is a derivation
   defect), and **every row pins a test LEVEL** (string / DOM-text / browser-computed / pixel). Any fact
   about visibility / layout / colour / interaction gets level ≥ browser-computed.

   It opens with an **artifact inventory** — every file the user receives — and every inventory entry owns at
   least one rendered-level row. Derivation CLOSES with the template's **coverage validation checklist,
   actually walked** (every anchor ≥ 1 row · every node's negative-side rows exist · no stale refs). A fact
   with no row or at a too-weak level is a derivation defect, fixed here.

   The matrix is the bridge: tests come from the matrix, upstream of the code. (The mechanical projection is
   junior work; choosing each row's level + assertion is the senior's.)

6. **Test — with `test-author`, write tests that assert the REAL shipped artifact.** Render the widget / produce the file /
   call the function and inspect the output as real behavior, apart from any source-string match. Watch the new test FAIL first
   (red-on-bug), then implement. Never edit a test just to make a change pass.

7. **Code — implement until green.** Delegate well-scoped, mechanical implementation to a junior worker
   with a precise brief + a persistent checkpoint file (so a cut-off resumes rather than restarts). Keep the hard
   parts (ambiguous specs, design, tricky debugging) on the senior model. Verify the junior's result by deed.

   **A norm-pointered surface builds with the artifact open (SPEC INV-43):** when the surface's spec clauses
   carry a `norm: <path>` pointer, OPEN the artifact before building — the frozen prototype is the norm for
   look and feel, the clause text only its laws — and record a one-line plan-vs-prototype diff in the
   landing's accounting. A missing diff line is a defect at review. The verify step's feel bar (step 8) reads
   the same pointer.

   **Taste-heavy deliverables build smallest-first (SPEC INV-62):** when taste rules the deliverable — voice,
   copy, visual style, spec prose — STOP at the cheapest judgeable sample (one paragraph, one card, two
   sections) and take the human's word on it before the full build spends anything. Five full packs once died
   on a failure a one-paragraph sample would have caught.

   **And a rejected artifact reopens its SOURCE (SPEC INV-63):** the fix starts at the spec clause / card /
   brief that produced it — correct the source, then rebuild from it. Line-patching the rejected output
   against an unchanged source is the five-round trap, banned.

8. **Verify by deed.** Run it and see the result with your own eyes. Only call it done/working after that;
   otherwise label it an assumption.

   Run every check the diff can reach before any push — the reach map's law (SPEC INV-45): a prose-only diff
   runs the doc gates whole and says so. Any code, spec, matrix, skill, or test file in the diff means the
   whole suite.

   **Green = zero failures AND the skip-set is exactly the expected pinned list** — an unexpected skip
   (Chrome absent, a real-data fixture missing) is a FAILURE outright. **If red at a pause / session end:
   never commit; write the failing test name + hypothesis as the top `NEXT_STEPS.md` item** — the checkpoint
   IS the red test.

   **The adversarial option — a second pair of FRESH eyes (SPEC INV-46).** When the code step was
   delegated AND the delta is surface-sized (a new surface or a multi-file behaviour change), verify
   also runs a fresh-context checker: brief it with the SPEC sentences the landing claims (the anchors) and
   the artifact paths — primary sources only, apart from the worker's summary or your own plan. Its opening
   hypothesis is "tasks completed, goal missed". It walks each claimed fact up the ladder exists →
   substantive → wired → flows, and greps for stubs: TODO · FIXME · placeholder · lorem · hardcoded sample ·
   empty function body.

   Findings become rows or red, never a nod. The checker is a worker under the full contract (checkpoint,
   ledger, clock), and its verdict rides the landing report. Anywhere else the checker is the senior's
   option. A skill or prose landing walks the ladder in its kind's form: the checker re-reads the SHIPPED
   text against the spec sentences.

9. **Commit & show.** Commit when green with no regression (unasked) — same or better is enough, never wait for perfect. Where the host has a remote, PUSH accepted work there by rule (SPEC INV-82): every gate the diff reaches ran and passed (the verdict read from the suite log's own line), plus the host's own push lines; the remote is discovered from the tree, and only a host with no remote gets one contextual question at the first push moment (create one — GitHub, GitLab, whatever the human names — or stay local, recorded in the host profile). Every push re-walks the README against the pushed truth — crisp and current, a stale claim fixed before the push (the shopfront law at every-push cadence). After the push the push step reads the remote gate's own verdict (the CI run the push triggered, one `gh run` read), and a red verdict is the pushing session's own immediate bug: fixed and re-pushed the same session before anything else, so the human never meets the red first in a GitHub email; a slow gate is watched to its verdict on the detached-work cadence (SPEC INV-106, INV-35). The human's personally named gates still wait for his word. Bump the version (PATCH by default).
   Docs travel with the change — README + CHANGELOG + the skill's own `SKILL.md`, same session. Diary the WHY
   in `JOURNAL.md`.

   **The CHANGELOG speaks to the USER, the journal to the builder:** each entry says what changed for the
   person using the product, with one concrete example from real output, in outcome terms only. Function
   names, internal ids, and row numbers live in the journal instead. And no doc pins a drifting version
   number in prose — "current version: vX.Y" always goes stale. Point at the version's one home (the VERSION
   file, the frontmatter) or omit it.

   The landing report TELLS the taste choices made without asking — the open `[default]`s — each in plain
   words with an example and a tweakable mark. No confirmation is requested; silence is consent, never
   re-asked (SPEC INV-31). The same TELL covers a tunable parameter you set to a sensible default — a
   resolution, a batch size, a timeout, a sampling rate — named with what it trades, tuned together later at
   most, never a stall on a knob you can reasonably pick (SPEC INV-70).

   Show the human the REAL render in a new window; push or deposit only after they've reviewed it. A push
   re-renders all deposited artifacts, and a push shipping a new version walks the publish skill's shopfront
   check — README claims + kind-owed visuals fresh, the outcome line riding the landing report (SPEC INV-44).
   Where the host's design-sync is ON (base defaults; SPEC E-18), the landing's DECLARED components also sync
   to the team's design project — after the human's gate, never instead of the in-session show.

## Guardrails — the pipeline's TEETH (mechanical, every project inherits them)
The eight steps are guidance, and an agent DRIFTS from guidance — that is the failure that stops a project
converging (a whole panel ships empty; a behaviour nobody asked for gets buried; a change lands with no test).
So the pipeline is not trusted, it is ENFORCED: a `guardrails` check the project wires to a **git pre-push
hook** (+ the suite), so a change that fails ANY of these is RED and CANNOT be pushed. `test_traceability`
(below) is the first of these — generalise it to the full set. **Each project INSTANTIATES the checks for its
own surfaces; the pipeline REQUIRES the check exists and is green.** This is a first-class step, applied project-wide
rather than as a per-project patch. The four mechanical guardrails:
- **Completeness** — a SURFACE REGISTRY + a render-scan test that fails if any user-facing surface is empty OR
  is rendered but not in the registry (so a new surface goes red until registered + asserted). No partial/
  stripped artifact can ship or be shown. Self-closing: the DOM is the source of truth, checked directly instead of a hand-list.
- **Tests-present** — a diff that touches a user-facing module MUST touch `tests/`. No change without a test.
- **Behaviour-traces-to-spec (bounds)** — every user-facing behaviour traces to a SPEC clause; a behaviour with no
  spec backing (a silent micro-decision — a default, an auto-mute, a sort order) is RED. This is what catches
  freelancing mechanically: you cannot ship an unasked, unrecorded behaviour.
- **Conflicts** — id duplicates, a spec invariant with no matrix row, a ⟨DECIDE⟩ marked RESOLVED but still
  live, a surface named two ways. (This is today's `test_traceability`, widened.)
**Honest boundary:** guardrails catch STRUCTURAL defects (empty surface, missing test, untraced behaviour,
partial artifact, id/naming conflict). They do NOT catch a subtle SEMANTIC bug (is the number right?) — that
still needs `product-prover` + a human's eyes. Enforce structure mechanically, and reason about meaning with
the prover. Verify-by-deed (step 8) and commit/push (step 9) both run the guardrails first, so guidance and
teeth agree.

## The excuses table — read it the moment one of these crosses your mind

The shortcuts that kill the method never announce themselves; they arrive as one of these thoughts.
Each is a tripwire: thinking it means STOP and take the pipeline door you were about to skip.

| The thought | Why it is a trap |
|---|---|
| "it's a one-liner / just a prototype" | The Room was "just to see" — it shipped hover-only with no phone layout and no spec. Size never picks the door; the tripwires do (base rule 15). |
| "I'll write the spec after it works" | Spec-after-code documents what you built, apart from what was asked; the prover can no longer catch the difference (spec-author anti-pattern). |
| "the human is in a hurry" | Urgency moves PRIORITY, never the door — a critical feature heads the queue, it still enters at the spec step (SPEC T-12). |
| "the suite is green, ship it" | Green proves the facts the matrix knows; an unspecced surface has no rows, so green says nothing about it (SPEC INV-15). |
| "asking would bother them" | Batched questions exist exactly for this; a silent guess costs a re-build, the batch costs one read (SPEC INV-4, INV-5). |
| "explaining it would take longer than just doing it myself" | That is delegation dying, and the senior drowning in junior work; write the self-contained brief (the delegation rule above). |

## Gates worth remembering
- **Before a MINOR (0.x.0) bump:** the 3-pass preventive audit — product-prover on the whole spec + a matrix
  audit + a surface-composition check. Fix holes by the book; record the rest.
- **Process bookkeeping scales to the delta (SPEC INV-61):** the pre-push re-check keeps its rigor and
  scales its FORM — a small delta (skill/prose/infra kind, no new surface, no structure change) ships a
  three-line SHORT-FORM record (previous records clean · the delta in one line · the verdict). A
  surface-sized or structural delta keeps the full walk. Claims batch per declared lane, and the journal
  chapter and the resume rewrite come once per landing batch. Never scaled: the law's own text, the
  red-first test, the delta's prove, the gates.
- **Order is law:** `spec → prove → architecture → prove architecture → matrix → test → code`;
  `bug → matrix → test → code`. Never code first and back-fill a spec — and never jump from spec straight
  to tests: the two layers between them (architecture, test-spec derivation) are where whole classes of
  holes get caught (SPEC E-14/E-15/INV-15).
- **A row closes only whole (SPEC INV-26):** where a row carries several legs, its Done-when enumerates
  each, and the landing report may close the row only with EVERY leg met —
  half-done is a status, never a landing. An open leg keeps the row in-work, and the resume file's LIVE-STATE restates it at every
  supersession, never compresses it away (still open at compaction ⇒ restated in full).
- **Trains, one pen (SPEC T-18, INV-39):** one session may roll up to three INDEPENDENT build lanes
  without asking (his 2026-07-06 word; a fourth opens only on the human's asked word, never silently) —
  pairwise independent: no shared surface, no shared spec section. Opening each lane is narrated, and
  every train rides the departures board, a waiting lane naming whom it waits behind. Only penless
  stages overlap: a later train's code and tests in its own isolated tree (its delta integrates only
  under the pen; the disjoint-file road stays within one lane), read-only analysis free.

  Every shared-doc edit, the integration, and the closing of a row take the pen one lane at a time — a
  pen-stage is never cut mid-edit — and a landing commit carries exactly one row's delta, its gate run
  on a tree clean of the other lanes' unfinished work. After a landing, waiting lanes re-fence and
  re-run their gates on the new truth. Never across sessions, never mid-milestone. A bug takes the pen
  at the end of the current pen-stage and parks every rolling lane, each at its own checkpoint,
  resuming in landing order.
  **Lanes are picked by a graph, never by mood (SPEC INV-49):** at queue-take read the runnable head
  and build the mini dependency graph — an edge wherever two rows share a surface, a spec section, a
  skill file, or a doc region. Open lanes on a pairwise-independent set up to the cap. Rows that
  collide only at integration pre-roll isolated build stages with the landing order DECLARED at claim
  (first-declared lands first, the later re-fences). Tiny rows ride serial — parallel pays only when
  build stages dominate the pen work — and the chosen set, the order, and a said-aloud "serial by the
  graph" are board lines.

  **The drafter-applier pipeline is the standard colliding-rows form (SPEC INV-49):** on colliding rows
  the penless DRAFT stage overlaps the current landing: a drafter worker at the judgment tier prepares the
  next row's exact edit strings with self-verified needles while the applier lands the current row under
  the pen. The landing order stays declared and the numbers follow it. This form ran live 2026-07-12, the
  night the law batch serialized on the spec/matrix/version chain and still moved at two rows an hour
  [T-18, INV-39, INV-49].
- **Junior delegation (decided from the request, BEFORE the first tool call):** delegate when ≥1 holds —
  >3 files touched/read for facts · a known script/suite runs >~30s · the output is a report/list/dump · the
  edit strings or command are known verbatim. The tier ladder and the raw-output law live in the base
  skill's rule 5 (live-spec-base).

  **The routing rule (SPEC INV-69) picks the tier — propose the cheapest tier that can pass the brief, the
  senior may overrule it aloud:** the proposal reads the STEP and kind of the work, beyond the row's size
  alone — a judgment step (spec, prove, architecture, matrix-level calls, findings triage, any taste call)
  proposes the senior and is never routed down, a mechanical step proposes a worker at the tier above. The
  economy rung moves the threshold (at `lean` an airtight brief rides one tier cheaper, at `tight` the
  cheapest sufficient tier is always the proposal). And the proposal is ADVISORY — the senior may override
  per wish, the override logged as one line on the checkpoint and the landing report, proposed tier → chosen
  tier → why.

  **The brief is self-contained (the BMAD story-file lesson):** delegated work ships as one document
  embedding the EXACT spec sentences it serves, the exact edit strings or commands, the checks to run, and
  the checkpoint path — the worker never hunts context, never interprets the spec, never decides. If writing
  the brief means deciding something first, that decision is the senior's and happens BEFORE delegation —
  "explaining it would take longer than doing it" is how delegation silently dies.

  **The brief's birth has three laws (SPEC INV-53/54/55):** a brief that edits existing files is born from
  READING them in full — three recorded lines per file (current state · what changes · what must survive),
  every step back-referencing its spec sentence, every technical claim citing a source (a file:line, a
  command's output), never memory of a file. The brief carries the closed HALT list — ambiguous requirement
  · two consecutive unexplained failures of one command · missing config/dependency · acceptance impossible
  as briefed — stop WITH evidence, otherwise run to completion (the senior's escalation ladder is a separate
  move, after a failed acceptance). And the brief is SIZED — its text within ~300 lines, at most ~8 files to
  edit [default], the work splitting above either — passing PATHS, never inlined file bodies. See the private
  playbook repo's PLAYBOOK.md.

  **The worker contract (SPEC ACT-3):** the brief NAMES the files the worker may write — its session's
  write-ownership narrowed to exactly those, reads free, writes fenced. Same-session sibling-worker files
  are fence-benign (the concurrent-edit fence alarms on foreign sessions, staying quiet on your own briefed
  hands — the senior who briefed both owns the seams between briefs). The session's live setting lines ride
  into the brief verbatim — a worker never resolves the settings ladder itself, it cannot hear the human's
  spoken word.

  The brief ARMS the worker for the workshop — it carries the host's problem-ledger path
  (`.live-spec/PROBLEMS.md`) with the WATCHED-line duty: workshop noise the worker hits (a flaky harness, a
  missing dependency, a tool misbehaving) goes into its checkpoint as a ledger line — signature, date, one
  line of context, logged every time — and the senior carries the lines into the ledger at verify (SPEC
  INV-23). And it carries the CLOCK — the date and time read at briefing — so the worker stamps its
  checkpoint and any dated output from the brief's clock, never an invented hour (SPEC INV-24; a worker WITH
  a shell re-reads the machine clock itself — the brief's line is the floor for one without, and elapsed
  time is never guessed). And a result failing its brief's acceptance escalates exactly ONE tier every time,
  with a logged line covering the move — one rung up, in order, always logged.

  **Every delegation reports its saving:** the
  landing report carries one line — what went to the worker and roughly how much senior work it saved.
  The line is what keeps the habit alive; a session that never writes it is a session that quietly
  stopped delegating. The line lives in the landed row's status cell, and a suite check reads it: a
  landed row without the line goes red (SPEC INV-103, forward from 2026-07-12). The duty binds the
  orchestrator seat regardless of model, whatever tier leads the seat.
- **Traceability is a test, enforced automatically.** A standing `test_traceability.py` fails the suite on a matrix row
  citing a missing test, a duplicate invariant id, a spec invariant with no matrix row, or a ⟨DECIDE⟩ marked
  RESOLVED that still carries the live marker — so drift is caught every commit, continuously rather than once per MINOR.

## How it relates to the other skills
- `spec-author` — writes/grows the spec (step 1). Public.
- `product-prover` — reviews the whole spec with formal-verification thinking (step 2). Public.
- `test-author` — derives the matrix and writes the tests (steps 5–6). Public.
- `build-pipeline` (this) — the orchestrator that sequences them through to a shipped, verified, committed
  change.

> The method, made durable: spec-author and product-prover each own one step; build-pipeline is the spine that
> runs the whole arc from a spec to a shipped, tested, committed change.

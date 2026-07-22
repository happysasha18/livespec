# Decision: a new genre for the spec

This page asks for one decision: should the spec move to the requirements genre shown below?
The material is one area of the spec — request intake — written both ways.
Exhibit A is today's spec: a prose paragraph plus the index row that carries the full rule.
Exhibit B is the new genre: a glossary, then numbered requirements a stranger can read on first pass.
Five rounds of cold reading shaped Exhibit B; the numbers and findings are below.
The two holes the rewrite found in the spec itself close this page as queue candidates.

---

## Exhibit A — today's spec

Today one rule lives in two places: a short prose paragraph a person reads, and one index row that carries every condition of the rule in a single sentence. Here is the index row behind the three-source impact read (INV-128), verbatim, 1,655 bytes in one line:

> every request enters through a three-source impact read beside the door [T-12] and work-kind [T-16]: the footprint is read from the spec (what behaviour changes), the architecture (which module owns it), and the code (what gets touched) at one intake moment, producing one named footprint — presentation-only · single-module · cross-cutting — spoken in the capture echo and written in the row's `footprint:` note beside door/kind/map [INV-43, INV-108]; the footprint decides the route (presentation → light road; single-module → the matrix step against the module's interface; cross-cutting → the full pipeline), weight matched to reach, the footprint not the size picking the road; the read names any source disagreement as a finding routed to its owner (bug row / spec fix / restructure row [INV-37]) rather than silently trusting one source — pulling the architecture step's spec-to-code reconciliation forward to entry; the three-source read is the verdict derive-before-fork [INV-121] rests on (only the genuinely-open fork reaches the human); the footprint re-classifies mid-work when an edit reaches past its layer (mirroring the door re-fire), the landing report recording held-or-reclassified; the station carries the boundary-health law — a right boundary keeps a typical request in one module, repeated cross-cuts on the same module pair being the signal to move a boundary (only through the architecture step's re-prove [INV-37], on the recorded-footprint evidence not a hunch); recorded live 2026-07-12, the entry station (P1-P6) of the fourteen-principle architect draft, deeper mechanical enforcement on the follow-on rows

And here is a slice of today's body prose for the same area:

> **A wish is classified by size, priority, and work-kind.** Size uses one four-word vocabulary everywhere: bug, small, surface, large. The queue's class column uses the same four words and no second size scale. The door is a separate axis — where the wish enters the pipeline. Size is a separate question.
>
> Priority is normal unless the row states otherwise, with two marks:
> - **Critical** — the shipped product is broken for its user: an unusable surface, lost data, or a violated safety gate.
> - **Quick win** — low effort, immediate value, no design decision inside.
>
> When the classifier cannot call a size, a priority, or a work-kind [T-16], it asks the human at intake and does not guess. Until the human answers, the wish carries normal priority; its kind is the host's recorded default, or none; a kind not yet named scales nothing down [INV-22]. The open question stays in the row while the lane keeps moving [INV-4]. [INV-12]
>
> **A large wish negotiates scope, never time.** The walk does not ask how long a wish will take, and does not accept an estimate in hours or days as an input. When a wish is larger than its worth, the walk answers in scope terms and proposes one of two moves:
> - **cut the scope** — fewer surfaces in, plainer defaults on what stays;
> - **split into stages** — each stage lands through the full pipeline on its own (the large size decomposes this way [INV-12]).

A reader meets coined words (wish, door, walk, lane) with no definitions, and the full rule sits in the index row above, one sentence long.

---

## Exhibit B — the new genre

The document opens with a closed glossary. Every domain noun used anywhere in the text is defined at the top, one sentence each. The first eight entries:

- **request** — one thing a person asks the pipeline to build, change, or fix.
- **inbox** — a folder in the project where a request can arrive as a dropped file.
- **intake** — the first step, where the pipeline reads a new request and records what it is before any work starts.
- **intake classifier** — the part of intake that reads a new request and states its size, its priority, its entry route, and its work type.
- **backlog item** — one row that tracks a single request from intake to its close.
- **queue** — the ordered list of backlog items waiting for work. The pipeline runs the item at the head first.
- **pipeline** — the fixed sequence of steps a request passes through, from intake to delivery: spec, architecture, test matrix, tests, code, and a final check.
- **spec** — the document that states what the product does for its user.

Each rule then becomes a requirement block: a short context, a user story, and numbered criteria — one trigger and one response each, grouped into named cases, the keywords set in lowercase italics. Here is Requirement 3 in full:

### Requirement 3: The intake classifier states a request's size, priority, and work type

**Context:** A request arrives from the person. Before any work starts, the intake classifier reads the request and records what it is. It states the request's size, its priority, and its work type. The person sees these on the backlog item.

**User Story:** As a person handing in a request, I want the intake classifier to state its size, priority, and work type at intake, so that a small request gets a small process and a large one gets the full pipeline, and I can see how the request was read.

#### Acceptance Criteria

**Case: size**

1. *when* a request arrives, the system *shall* classify it by size, priority, and work type.
2. The system *shall* name a request's size with one four-word vocabulary: bug, small, surface, or large.
3. The system *shall* use those same four words in the queue's class column, and *shall* keep to one size scale.
4. The system *shall* treat the entry route as a separate axis from size, with one stated tie: a request sized bug enters by the bug entry route, one call stated once, and the route axis adds the other four values. [T-12]

**Case: priority — critical**

5. The system *shall* set a request's priority to normal unless its backlog item states another value.
6. *when* the intake classifier judges the shipped product broken for its user, the system *shall* mark the request critical. The intake classifier judges the product broken by three tests: a surface the user cannot use, lost data, or a violated guardrail. [T-11]
7. *when* a request on a non-bug entry route is marked critical, the system *shall* move it to the head of the queue while the running work keeps going. [INV-133]
8. *when* a request on a non-bug entry route is marked critical, the system *shall* keep the running work running. [INV-133]
9. *when* a request is marked critical, the system *shall* state at intake that the mark heads the queue and keeps the running work running, so the person can reclassify it as a bug if the person meant a live break that must stop the work now. [INV-133]
10. The system *shall* set priority on the person's word, and the critical mark *shall* stand once the person gives it. [INV-133]

**Case: priority — quick win**

11. *when* the intake classifier judges a request low in effort, immediate in value, and free of any design decision, the system *shall* mark the request a quick win. [T-11]
    [GAP: the spec does not define how the intake classifier measures a request's effort or a request's value for the quick-win mark.]
12. *when* the queue frees and a quick win is waiting, the system *shall* be free to take the quick win ahead of larger queued items, and *shall* mark the promotion in the backlog item. [T-11]
13. *when* a promoted quick win is delivered, the system *shall* run the queue head next, so a run of quick wins does not starve a larger request. [T-11]

**Case: work type**

14. *when* a request arrives, the system *shall* tag it with one work type from the curated vocabulary: product, infra, skill, or prose. [T-16]
15. The system *shall* keep the project's default work type in its profile. [T-16]
16. *while* a pipeline step runs, the system *shall* scale its effort by the request's work type, and *shall* report whether it applied or stood down, naming the step. [INV-22]
17. The system *shall* run the guardrails whatever the work type. [INV-22]

**Case: the classifier is unsure**

18. *if* the intake classifier cannot call a request's size, priority, or work type, *then* the system *shall* ask the person at intake and *shall* refrain from guessing. [INV-12]
19. *while* the person has not answered, the system *shall* carry the request at normal priority. [INV-12]
20. *while* the work type is unnamed, the system *shall* use the project's recorded default, or none. [INV-22]
21. *if* a work type is not yet named, *then* the system *shall* scale nothing down. [INV-22]
22. *while* a classification decision is open, the system *shall* keep it in the backlog item and keep the queue moving. [INV-4]

**Case: the bug route**

23. *when* a request enters by the bug entry route, the system *shall* admit it at the test-matrix step and *shall* reproduce the break as a failing test before fixing it. [T-12]
24. The bug entry route is the one route allowed to interrupt running work: the running work parks at a stopping point from which it can resume with nothing lost, the bug is fixed, and the parked work resumes in its original order. [T-9]


Where the spec itself holds no answer, the genre says so on the spot instead of writing around it. The three such lines in the document:

> [GAP: the spec does not define how the intake classifier measures a request's effort or a request's value for the quick-win mark.]

> [GAP: the spec does not define who weighs a request's effort against its benefit, or by what measure, at scope negotiation.]

> [GAP: the spec does not name the entry routes for the spec-fix and restructure backlog items; of the three disagreement outcomes, only the bug item's route is stated.]

---

## Numbers

| Piece | Bytes |
|---|---|
| Source slice (intake prose + its cited index rows) | 17,297 |
| genre2 sample (first attempt at this genre) | 12,000 |
| genre3 sample (this genre, after six rounds of cold reading and the owner's format pass) | 26,977 |

What each round of cold reading found:

| Round | Result |
|---|---|
| 1 | 6 findings, among them 2 real holes in the spec itself (the two GAP lines above) |
| 2 | comprehension correct; 12 term stumbles (undefined words, an unnamed channel, an unnamed owner) |
| 3 | comprehension correct; 10 precision stumbles (pronouns, glosses, one unstated mechanism) |
| 4 | 1 blocking finding (the entry-route set was never named) + 6 notes |
| 5 | 3 blocking terms from a different fresh reader (session, aspect, richness) |
| 6 | final two-reader panel: 7 blocking items (double names, unstated effects, one word on two independent-looking axes) |
| 7 | verification panel, reader C: 3 blocking (the "unread" trigger for a lost decision is ambiguous; "taste call" carries the ask-versus-decide split with no definition; "depth" in stage-splitting is a bare metaphor) |
| 7 | verification panel, reader D: 5 blocking (the system and the pipeline read as two unequated actors; the pipeline's step list and the document chain's step list differ; "spec pin" undefined; the restructure-versus-refactor relation unstated; the rule-10 pointer leads outside the document) |
| Verdict | every fresh reader finds new blocking terms; fixed items stay fixed; the union across 8 readers is about 35 items on a 25 KB sample. The permanent gate is therefore a panel of fresh readers until two consecutive clean reads, applied per changed section — cheap on small deltas. |

The honest projection: on rule-dense material like this slice, the readable genre costs about 1.56 times the source bytes. The whole-file win has to come from what the rewrite deletes: the triple statement of each rule (prose + index row + skill restatement), the 270 KB manual index, and the history inlined into rules. A full-section pilot is the next measurement.

---

## Five spec holes found — queue candidates

The rewrite and the reader panel surfaced five places where the source spec leaves a judgment, a route, a category, or a sequence undefined:

1. The quick-win mark rests on "low effort, immediate value", and the spec holds no measure of a request's effort or value.
2. Scope negotiation triggers on "a request larger than its worth", and the spec never says who weighs effort against benefit, or by what measure.
3. A three-source disagreement opens one of three backlog items, and the spec names an entry route only for the bug item; the spec-fix and restructure items have an owner and no route.
4. The "taste" category decides what is asked and what is decided, and the spec holds no definition or measure for it.
5. The pipeline's step sequence and the document chain's sequence read as two differing lists, and the spec never states their relation.

Each is one backlog item: define the scale, the route, the category, or the relation — or state plainly whose judgment it is.

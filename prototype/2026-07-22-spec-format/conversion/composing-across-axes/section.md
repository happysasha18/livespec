# Composing across axes

This section states how a surface is reviewed against every angle its behaviour can vary along, and where the rules that hold a capability's body, its installed copy, and its version live. It is written for a reader who has never seen the pipeline before.

Bracket codes like `[INV-244]` and `[C-1]` point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `INV-` an invariant (a numbered rule that must always hold), `C-` a composition rule (a numbered rule about how surfaces compose across their axes), `E-` an entity (a numbered part of the product), `T-` a transition (a numbered change of state), `M-` a rhythm rule (a numbered recurring routine), `A-` an adoption step, and `D-` a recorded decision. The keywords *when*, *while*, *if*, *then*, and *shall* are set in italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, *if* and *then* open a condition and its result.

Terms already defined in the intake glossary and the founding, build-loop, agents-together, and bounds sections — surface registry, prover, design review, facet, standard facet, lens, project kind, project layers, design principle, proof kinds, architecture node, tier, host, pack, guardrail, suite, push gate, net, ratchet manifest, migration chapter, catch-up walk, installer, snapshot, seat, worker, milestone, attic, journal, spec, architecture, invariant — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **stateful surface** — a part of a host project that holds state: a screen, a panel, or a saved file the user can change and find again later.
- **composition axis** — one angle a stateful surface's behaviour can vary along, stated as one question about the surface. A floor axis is one of the kind-independent set every stateful surface answers; a kind-owed axis is one a project's kind adds beyond the floor.
- **input-capability axis** — the composition axis for the input a surface is used through, such as touch or a fine pointer. Its values are the input capabilities a device carries, which co-occur on one machine.
- **config-health check** — the check that diffs each installed copy of a pack artifact against its source in the pack and reds a missing or drifted copy, naming the one fix; it runs inside the suite and the push gate.
- **document provenance** — the composition axis adoption adds: where a spec claim came from. A claim is native when it was written fresh under the pack, and re-engineered when it was recovered from documents a project held before adoption.

---

## Requirement 1: Every stateful surface is reviewed against a floor of composition axes

**Context:** Some parts of a host project hold state — a screen, a panel, a saved file the user can change and find again later. Each is a stateful surface. Every stateful surface is reviewed against a set of composition axes, each axis one question about the surface's behaviour. A floor of axes holds for every stateful surface whatever its project's kind. The axis a reviewer skips most is the last one, the presence of every other live surface: a caption still naming the previous photo once the closing screen arrives is the classic stranding hole, because the caption's behaviour with the finale in view was never written as a sentence.

**User Story:** As a person composing a surface, I want a fixed floor of axes every stateful surface answers and one stated shape for the whole axis set, so that no kind-independent angle of its behaviour is left unreviewed and a reader knows when the surface's spec is complete.

### Acceptance Criteria

**Case: the kind-independent floor**

1. The system *shall* review every stateful surface against the floor axes: its behaviour in each view, in each mode, at each user tier, at each viewport size, when it is closed and reopened, and under two writers that can act on it at once. [C-1]
2. The system *shall* include in the floor the surface's behaviour alongside every other surface that can be present at the same time — a sibling sharing the screen, or a surface the flow reaches one step before or after it — whether or not that other surface holds state. [C-1]

**Case: the seam beside each other live surface**

3. The system *shall* state, for each other live surface present with this one, what this surface does while that one is present — whether it holds, clears, or hands off. [C-1, INV-72]

**Case: the axis set declares its own shape**

4. The system *shall* read the axis set as a hybrid whose shape it declares: the floor is an enumerated set every stateful surface answers, and the kind-owed tail is an open set whose members a kind names one at a time. [C-1, INV-226]
5. The system *shall* read a surface's spec as complete only once every floor axis and every axis its kind owes has an answer. [C-1, INV-244]

---

## Requirement 2: The prover hunts the situation the author never wrote

**Context:** The prover reads the whole axis list actively and derives each surface's reachable situations for itself, rather than trusting the author to have filled every one. A reachable situation the spec leaves blank is the exact hole a running product still reaches, and the prover reports it and leaves the sentence to the author.

**User Story:** As a person relying on a spec to cover what the product reaches, I want the prover to derive each surface's reachable situations and flag every blank one, so that a state the product can reach but the spec never wrote is caught before a user meets it.

### Acceptance Criteria

**Case: derive the reachable situations**

1. *when* the prover reads a stateful surface, the system *shall* walk every axis — the views, modes, and tiers; the viewport shapes and reopens it passes through while already shown; and every other surface that can be present at the same time, siblings on its screen and the surfaces one step before and after it in the flow. [INV-72, C-1]
2. *when* the prover reaches one situation, the system *shall* ask whether this surface's behaviour is stated there, and *shall* report a reachable situation with a blank answer as a finding of the same class as a fact no node owns. [INV-72, E-14]

**Case: the hunt rides both passes and leaves the sentence to the author**

3. The system *shall* run the hunt on both the whole-spec pass and the surface-add pass. [INV-72, M-6]
4. *when* the hunt reports a missing situation, the system *shall* leave the sentence to the author, who writes it as a composition invariant, decided or marked a default the way the standard-facet sweep marks its own, and *shall* invent no answer and ask the human for nothing. [INV-72, INV-18, INV-31]

---

## Requirement 3: A cross-surface policy is stated once at the class level

**Context:** When a decision governs a kind that recurs across sibling surfaces or elements — a gesture policy, an affordance, an input-to-action mapping, a repeated state transition, or a feature and its element shared across places — the spec states it once at the surface-class level, naming the class and enumerating the surfaces it governs. Consistency of this kind is itself an invariant. This is the preventive twin of the class hunt: the class hunt sweeps siblings once a bug is confirmed, and this holds the policy uniform before a bug is filed.

**User Story:** As a person keeping behaviour uniform across similar surfaces, I want a policy for a recurring kind stated once at the class level and checked across its siblings, so that a rule written for one surface while its siblings stand cannot ship non-uniform.

### Acceptance Criteria

**Case: the policy is homed on the class**

1. *when* a decision governs a kind that recurs across sibling surfaces or elements, the system *shall* state it once at the surface-class level, naming the class and enumerating the surfaces it governs. [INV-125]
2. The system *shall* read a policy written for one surface while siblings of the same kind exist as a spec defect. [INV-125, INV-124]

**Case: the prover and the guardrail hold it**

3. *when* the prover reads an interaction policy, the system *shall* enumerate the surfaces of that kind from the surface registry and flag any the clause does not cover, the same finding class as a reachable situation with a blank answer. [INV-125, E-10, INV-72]
4. *when* a product renders a page, the system *shall* assert a policy declared for one surface root across every registered sibling root and hold it red until all are covered, so the non-uniformity reds the day the single-surface fix lands. [INV-125, INV-97]
5. The system *shall* keep the spec-class rule as the root and leave the page-wide assertion to the products the pack serves, the pack shipping the rule and the prover lens as the ship-the-shape pole of the pack-to-host split. [INV-125, INV-163]

**Case: the same defect stated in prose**

6. *when* a sentence states a principle for a whole kind while it is homed on one surface and siblings of that kind exist, the system *shall* read it as the same defect in prose form, and *shall* demand the author lift the principle to a class clause naming the class and its members, or scope it to the one member by a decided sentence. [INV-125]

---

## Requirement 4: Both directions of a paired state change get the same craft

**Context:** When a surface has a pair of opposite state changes — open and close, enter and exit, expand and collapse, show and hide — a transition crafted for one direction is a decision about the pair, so the other direction is stated too. The default is symmetry: the exit mirrors the enter's feel unless a reason is written. A shorter exit or a deliberately instant one is a valid, stated, decided answer. Motion feel is the human's own gate, so where the author cannot judge the pair the question is surfaced to him.

**User Story:** As a person crafting a paired transition, I want the opposite direction stated whenever one direction is crafted, so that a crafted-in and instant-out pair cannot ship silently and a reader tells a decided asymmetry from an overlooked one.

### Acceptance Criteria

**Case: the continuity of the transition**

1. *when* a surface has a pair of opposite state changes and one direction's transition is crafted, the system *shall* state the other direction too, defaulting to symmetry unless a written reason parts them. [INV-126]
2. The system *shall* have the author write the pair's answer as a spec sentence — mirror, a named shorter exit, or deliberately instant — decided or marked a default on the standard-facet sweep. [INV-126, INV-18, INV-31]
3. *if* the author cannot judge the pair's feel, *then* the system *shall* surface the question to the human rather than ship a crafted-in and instant-out pair. [INV-126, INV-30]
4. *when* the prover reads a paired state change with one direction described and the opposite unstated, the system *shall* report it as a finding of the same blank-answer class as an unwritten situation. [INV-126, INV-72]

**Case: the reversibility of the means**

5. *when* a surface is opened by a continuous, reversible gesture — a pinch, a drag, a lift — the system *shall* have that same gesture reversed stand among its ways to close, or a decided sentence state why it is absent. [INV-126, INV-30]
6. *when* an opening gesture has a natural inverse, the surface offers no way to close by that inverse, and no deciding sentence stands, the system *shall* block it as a finding of the same blank-answer class. [INV-126, INV-72]

**Case: the magnitude of a reversible quantity**

7. *when* the paired open and close ride a continuous, reversible quantity — a pinch span, a drag distance, a wheel accumulation — the system *shall* state whether the inverse asks the same magnitude as the forward move, symmetric or a named deliberate asymmetry, decided or marked a default, and *shall* report a stated pair whose magnitude sentence is missing as the same blank-answer finding. [INV-126, INV-31, INV-72]

---

## Requirement 5: Each scenario states how it is entered and how it exits

**Context:** A person-facing scenario is a flow, and a flow has edges: it is entered from somewhere with something already true, and it exits to somewhere leaving something behind. The scenario states both, so a reader can check it against a known before and after. This lifts the per-operation precondition and postcondition lenses to the scenario level.

**User Story:** As a person reading a scenario, I want its entry and its exit stated, so that the prior state it assumes and the postcondition the next scenario inherits are both stated on the page for the reader.

### Acceptance Criteria

**Case: the scenario states both edges**

1. The system *shall* have each person-facing scenario state its entry — where the walk arrives from and what must already hold — and its exit — where the person lands and what it leaves true for the next scenario to inherit. [INV-127]
2. The system *shall* read this as the scenario-level lift of the per-operation precondition and postcondition lenses, kin of the entry-symmetry lens and the runtime view's flow walks. [INV-127, INV-50, INV-74]

**Case: the prover holds it, binding forward**

3. *when* the prover reads a flow whose entry or exit is unstated, the system *shall* report it as a finding of the same blank-answer class. [INV-127, INV-72]
4. The system *shall* have a new scenario state its edges from the first draft and *shall* flag an existing scenario's unstated edge as a finding rather than block the lane. [INV-127, INV-159]

**Case: a trivially-none edge is still stated**

5. *when* a scenario's entry or exit is trivially none — a top-level scenario entered from nowhere, a terminal scenario exiting to nowhere — the system *shall* state it as such in one short clause, so a reader tells a decided edge from an overlooked one. [INV-127]

---

## Requirement 6: A gated behaviour names both ends of its range, and a scoped guarantee answers for its whole domain

**Context:** When a transition is gated on a quantity that runs on a line — elapsed time, a count, a distance, a size — the spec states its behaviour at both ends of the live range: below the low end and above the high end. When a slot on screen is filled by asynchronously produced content, the spec names the three faces of the wait — pending, arrived, and failed — and a visible pending face stands wherever the slot holds a reserved place. A guarantee that holds over one named part of its domain owes the same completeness across the whole domain, the viewport its worked instance.

**User Story:** As a person crossing an unnamed edge — reloading before the lower bound, returning after the upper, landing on a viewport band a guarantee never named — I want every range end, wait face, and domain part decided, so that no edge of a range or a partial guarantee renders as a blank the spec never wrote.

### Acceptance Criteria

**Case: both ends of a gated range**

1. *when* a transition is gated on a quantity that runs on a line, the system *shall* state its behaviour below the low end and above the high end, and *shall* read a phrase that names one point and leaves an unbounded interval silent as incomplete until that interval is bounded on both sides. [INV-138]

**Case: the three faces of an async slot**

2. *when* a slot on screen is filled by asynchronously produced content, the system *shall* name the pending, arrived, and failed faces of the wait and stand a visible pending face wherever the slot holds a reserved place. [INV-138]
3. The system *shall* read the pending face as that slot's loading state, sharpening the standard facets' empty, error, and loading states for a reserved slot. [INV-138, INV-18]
4. *when* the prover reads a gated range or an async slot with an out-of-range or in-between state left unspecified, the system *shall* report it as the same class as an unwritten situation, and the author *shall* write each edge as a spec sentence, decided or marked a default, surfacing the timing to the human where only he can judge it. [INV-138, INV-72, INV-31, INV-30]

**Case: a scoped guarantee owes its whole domain**

5. *when* a guarantee holds over one named part of its domain — a band of a ranged quantity, a user state, a network condition, a locale — the system *shall* draw the standing question about the remainder and give each remaining part its own decided or default sentence until the domain is covered. [INV-138]
6. The system *shall* read a guarantee that speaks for one part while the remainder stays silent as the same unwritten-situation class. [INV-138, INV-72]

**Case: the viewport is the worked instance**

7. The system *shall* have every layout guarantee name its viewport quantifier — holding on every viewport or naming the band it is scoped to — and *shall* leave the other bands silent until each is stated, the short-viewport band among them. [INV-138, T-13]
8. *when* the parts are a same-kind group no clause has yet declared, the system *shall* reach them through the design review's group pass and hold them in the prover once a part-uniform guarantee is declared. [INV-138, INV-141, INV-150]
9. The system *shall* read this as the range-and-lifecycle member of the composition-lens family, its member set open-ended, naming the viewport as its worked instance and leaving the remainder to the general duty. [INV-138, INV-125, INV-126, INV-136, INV-226]

---

## Requirement 7: A general law over concrete instances declares whether it enumerates them or lets them ride

**Context:** A law that states one general duty a set of concrete instances falls under makes one choice about those instances: the clause names every member, or an instance rides the general duty with no name. The member set keys the choice. A closed set names every member; an open-ended set names only its worked instances and leaves the remainder to the general duty. A law that reaches this choice by feel is the defect this rule keys.

**User Story:** As a person writing a general law over instances, I want the member set to decide whether the law enumerates or lets instances ride, so that a closed set names every member while an open-ended set names only what a real incident earned.

### Acceptance Criteria

**Case: the member set keys the choice**

1. *when* a law states a general duty a set of concrete instances falls under, the system *shall* make one choice: name every member in the clause, or let an instance ride the general duty with no name. [INV-226]
2. *when* the member set is closed and enumerable — finite and nameable, even one that grows a member at a time by a named incident — the system *shall* name every member in the clause, as the per-kind quality budgets name each project kind and the standard-facet list names each facet. [INV-226, INV-18, INV-41]
3. *when* the member set is open-ended — any sub-case of a domain, unlistable in advance — the system *shall* name only its worked instances, each earned by a real incident, and leave the remainder to the general duty carried by the rule with no list, as the scoped-guarantee law names the viewport alone. [INV-226, INV-18, INV-138]

**Case: reaching the choice by feel is the defect**

4. The system *shall* read a general law reaching enumerate-or-ride by feel as the defect this rule keys, the member set deciding, and *shall* have a law whose set is genuinely borderline state which side it took and why. [INV-226]
5. The system *shall* read this as the declaration member of the composition-lens family. [INV-226, INV-125, INV-126, INV-136, INV-138]

---

## Requirement 8: A surface's composition axes are the set its project's kind owes

**Context:** The floor axes are the kind-independent set every stateful surface answers, and a project's kind settles which further axes a surface owes beyond it. A kind carries a standard set of composition axes the way it already carries a node-structure scaffold and a set of design principles, so the author of a surface reads its axes from the kind before composing. An axis exists because the kind renders under it, and that existence stands apart from what today's code happens to cover; the gap between an owed axis and the code's coverage is the finding.

**User Story:** As a person composing a visitor-facing surface, I want its axes read from the project's kind and every owed axis covered against each of its values, so that an axis the kind owes cannot sit uncovered until a visitor falls through it.

### Acceptance Criteria

**Case: the axis set is read from the kind**

1. The system *shall* have the author read a surface's axes from the project's kind before composing, the kind carrying its axis set the way it carries a node-structure scaffold and a set of design principles. [INV-244, INV-36, INV-135, INV-136]
2. *when* a project's kind is visual — one that renders a visitor-facing surface and declares a design-principles set, the `static site` and `fullstack` kinds among them — the system *shall* owe every visitor-facing surface an open axis set whose first named member is the input-capability axis, beyond the viewport axis the floor already carries. [INV-244, INV-36, INV-136, C-1]
3. The system *shall* have the sibling axes on that surface — browser engine, locale and text direction, connection reach, first-versus-returning visit, accessibility, and measurement reach — ride the per-kind duty and enter as their own increments, so the visual kind's owed set stays open. [INV-244, INV-226]

**Case: the axis set is a founding declaration**

4. The system *shall* have every project kind name the composition axes it owes beyond the floor as a founding declaration, the way it declares its concrete layers and proof kinds. [INV-244, INV-135]
5. *when* a kind owes no axis beyond the floor, the system *shall* accept the empty set only as an explicit stated decision, the case the per-kind design-principles set already legitimises for a kind with no visual surface. [INV-244, INV-136]
6. *when* a kind is recorded with no axis-set declaration at all, the system *shall* flag it the way a kind recorded with no layers or proofs is flagged. [INV-244, INV-135, A-10]
7. The system *shall* have a non-visual backend kind owe its own non-empty axis set — load, version, and tenant — so an axis set that stays empty for a non-visual kind is a defect the flag-if-absent check stops. [INV-244, INV-135]

**Case: the gap between owed and covered is the finding**

8. The system *shall* read the two layers at each surface — the axes the kind owes and the values the shipped code covers — and *shall* report an owed axis whose value the code leaves uncovered as a finding of the same blank-answer class as a reachable situation the spec never wrote. [INV-244, INV-72]
9. *when* the gap is found, the system *shall* have the author state it as a spec sentence, decided or marked a default. [INV-244, INV-18, INV-31]
10. The system *shall* read an owed axis as covered only once the author composes and tests the surface against each elementary value of the axis, the write-the-sentence half and the cover-the-values half splitting one dimension by time. [INV-244, C-1, INV-18]

**Case: an axis carries its own value space**

11. The system *shall* read an axis's value space as a domain the same completeness reaches, and *shall* model the input-capability values as combinable capabilities a surface answers for in combination, since touch, a fine pointer, hover, and a keyboard co-occur on one machine. [INV-244, INV-138, INV-226]
12. The system *shall* owe and answer the two elementary poles — touch and a fine pointer — up front, and *shall* carry the co-occurrence answer, hover present alongside touch, in with the later step that forces the author to answer for the in-between. [INV-244]
    [GAP: the source answers the two elementary poles up front but defers the co-occurrence value — one device carrying touch and hover at once — to a later forcing step, naming no interim answer or default; a surface's behaviour when both are present is unstated today, so a test author cannot pin the tablet-with-hover-and-touch case.]
13. The system *shall* leave the refinement values past the elementary poles — a stylus, a keyboard-only reach, a device an advanced user registers — to the human's taste, entering later, decided or marked a default when they do. [INV-244, INV-30, INV-31]

**Case: the rule binds forward**

14. The system *shall* have a surface authored after this rule read its axis set from the kind from the first draft, and a surface that predates it carry the read at the first landing that touches it, staying uncovered on the axis until that landing arrives. [INV-244, INV-159]

**Case: the value-space machinery is promised**

15. The system *shall* keep the value-space in-between forcing step and the recursive axis-registry similarity sweep promised as later increments. [INV-244]
    [target]

---

## Requirement 9: A declared axis that adds runtime code names whether its artifact divides or ships whole

**Context:** The composition law reads whether a surface's behaviour divides along a cross-cutting axis its kind owes. Its dual reads whether the artifact the visitor receives divides along that same axis or arrives as one piece. When a spec declares such an axis and covering it adds runtime code, the design owes one of two decided sentences; an axis that adds runtime code and carries neither is the finding, shipping as one artifact because the choice went unexamined.

**User Story:** As a person reviewing an artifact's delivery, I want each declared axis that adds runtime code to state whether the artifact divides along it or ships whole for a named reason, so that a monolith nobody examined is caught while a monolith with a stated reason stands.

### Acceptance Criteria

**Case: the dual of the composition law**

1. The system *shall* read whether the delivered artifact divides along a declared axis its kind owes or arrives as one piece, the dual of the composition law that reads whether behaviour divides along that axis. [INV-248, INV-244]
2. *when* a spec declares such an axis and covering it adds runtime code, the system *shall* carry one of two decided sentences. [INV-248]

**Case: the two settled answers and the finding**

3. The system *shall* accept a monolith named for a stated architectural reason — one bundle behind one page that is never torn down, a delivery that runs on no server, or a payload the design judges too small to make a split worth its cost — as a settled answer, the design the judge of whether the named reason holds. [INV-248]
   [GAP: the source names the design as the judge of a "too small to make a split worth its cost" payload but states no measure — the payload size below which a split costs more than it saves — so a maintainer cannot pin the boundary between a settled small-payload monolith and an unexamined one; the source leaves it to the design as a senior read, not a gate.]
4. The system *shall* accept an axis that names the delivery road it owes — a platform split, a lazy load, a per-value chunk — carried by its own later row. [INV-248, INV-159]
5. The system *shall* read the finding as the third case: an axis that adds runtime code and carries neither sentence, shipping as one artifact because the choice went unexamined, its byte weight the downstream symptom of the unasked separability question. [INV-248]

**Case: the lens's reach and its standing**

6. The system *shall* reach this lens past the input-capability axis to any declared axis a kind owes — an assistant capability present or absent, a rendering engine, the viewport — each reached only where covering it ships runtime code, so a viewport answered by a media query or a locale answered by a logical property draws no delivery question. [INV-248]
7. The system *shall* keep this a senior read the prover carries and not a gate, since a monolith is lawful whenever its reason is named and only the design can say whether that reason holds. [INV-248, INV-244, INV-214]
8. The system *shall* carry a prover discovery habit stated in its skill: for a lens the prover applies, it may ask whether that lens's dual applies to the document here. The system *shall* read this as a prompt that surfaces a missing lens, and not as a rule that every lens ship paired, since one dual folds into a lens already run while another is nameable yet seldom applies. [INV-248]
9. The system *shall* read this as the delivery-separability member of the composition-lens family, binding forward: a surface authored after this rule states its runtime-code axes' delivery from the first draft, and a surface that predates it carries the read at the first landing that touches it. [INV-248, INV-125, INV-126, INV-136, INV-138, INV-226, INV-159]

---

## Requirement 10: A capability the pack can ship identically lives in one pack home

**Context:** Where a capability's body lives is placed on the pack-to-host axis by one question: can the pack ship a single identical body that every host runs? The base rulebook gives every fact one home, and this rule resolves where that home sits when the pack could hold the body or each host could. A body the pack can ship identically centralizes; a host-specific body ships as a shape each host fills.

**User Story:** As a person placing a capability's body, I want the pack-to-host question to settle whether it centralizes or ships as a shape, so that shared machinery has one source that a fix reaches everywhere while a host-specific part stays home.

### Acceptance Criteria

**Case: the placing question**

1. *when* a capability's body could live in the pack or in each host, the system *shall* place it by one question — can the pack ship a single identical body that every host runs — resolving where the fact's one home sits. [INV-163]

**Case: the two poles**

2. *when* the pack can ship one identical body, the system *shall* centralize the body to a single pack home adopted by a package update, so a fix lands once and reaches every host and no divergent copy can form, the browser test harness the centralize pole. [INV-163, INV-158]
3. *when* the body is host-specific — it names a host's own surfaces, holds a host's own data, or reads a host's own artifacts — the system *shall* ship the shape, a template and the guidance around it, and have each host own the instance it fills. [INV-163]
4. The system *shall* ship the shape for the cross-surface uniformity rule as its rule and prover lens, for a project kind's design principles as the law and starter set with the pixel projection left to the adopting project, and for the removal-list scanner as host-held greps under a pack-shipped template. [INV-163, INV-125, INV-136, INV-139, E-26]

**Case: the boundary moves toward centralization, binding forward**

5. *when* a host's instance grows a generic seam, the system *shall* lift that seam to the pack and keep the host-specific remainder home, so the boundary moves toward centralization as a body proves uniform. [INV-163]
6. The system *shall* have a new host-specific capability state which pole it takes from its first landing, the bodies that predate this rule standing as they are cited. [INV-163, INV-159]

---

## Requirement 11: Adoption wires the ratchet gates in one pass, seeded at the host's current size

**Context:** The compaction and register gates a machine can run reach a host through one installable kit rather than prose the host re-implements. The pack vendors the style lint, the redundancy precheck, the freeze tool, and their shared library into the host's tree, each vendored copy carrying a source pin so a later update check can tell a current copy from a stale one. The kit seeds the host's debt caps at the host's current measured size, so the gate is green the moment it lands and every later push may only hold or shrink the debt.

**User Story:** As a person adopting the pack, I want the ratchet gates vendored, seeded, guard-tested, and wired into the push gate in one pass, so that adoption demands no re-compaction and the ratchet points down from the first landing.

### Acceptance Criteria

**Case: vendor the kit with source pins**

1. *when* adoption runs, the system *shall* vendor the style lint, the redundancy precheck, the freeze tool, and their shared library into the host's tree, each vendored copy carrying a source pin — the pack version and content hash it came from — that a later update check reads. [INV-172, A-7]
2. The system *shall* merge the ratchet manifest across installer runs, so a prior install's keys survive a later run of the other kit. [INV-172]

**Case: seed the caps and pin them**

3. *when* the installer runs the gates over the host's declared doc set, the system *shall* write the cap file at the counts it finds, so the gate is green the moment it lands and every later push may only hold or shrink the debt, demanding no re-compaction at adoption. [INV-172]
4. The system *shall* pin the seeded caps with a generated guard test, so lowering the cap file is an ordinary edit while raising it demands editing the test. [INV-172, INV-98]

**Case: wire the push gate red-first**

5. *when* the installer wires the gates into the host's push gate, the system *shall* insert the block at a safe anchor ahead of the host's terminating exit, verify the block is reachable before it reports the gate wired, follow the four project-side checks' shipping contract — config-driven, standard-library only, one JSON line per red — and prove itself red-first on a planted defect. [INV-172, INV-97]
6. *when* a re-run finds a block stranded past a terminating exit, the system *shall* repair it by moving it to the safe anchor. [INV-172]

---

## Requirement 12: The pack's hooks have one canonical home, split universal against personal

**Context:** A live-channel hook the pack relies on lives as source in the pack's `hooks/` home and reaches a machine through an installer, the same ship-and-attach contract as the gates. A hook living only in an installed location has no home to update from, and that is a defect of this law. The set splits on one question: a universal hook enforces a pack law that binds every host, and a personal hook enforces one human's own patterns.

**User Story:** As a person installing the pack's hooks, I want each hook homed as source in the pack and split into a universal set that ships and a personal set the personal layer owns, so that a fix has one home and the pack ships nobody's personal rules.

### Acceptance Criteria

**Case: the canonical home**

1. The system *shall* keep a live-channel hook the pack relies on as source in the pack's `hooks/` home reached through an installer, and *shall* read a hook living only in an installed location as a defect of this law. [INV-173, INV-108, INV-97]

**Case: universal against personal**

2. The system *shall* split the set on one question: a universal hook enforces a pack law that binds every host, such as the contrast-frame scan in the docs language, and ships with the pack; a personal hook enforces one human's own patterns, such as a chat-language rule, and lives in the personal layer. [INV-173]
3. The system *shall* have the canonical universal hook read the personal patterns as an overlay file the personal layer owns, so one installed hook serves both. [INV-173]
4. *when* adoption or the machine-setup walk runs, the system *shall* install the universal set by the agent's own hand and say it aloud in the report. [INV-173]

**Case: a scan hook skips a demonstration**

5. *when* a scan hook reads text inside quotation marks or code fences, the system *shall* skip it, since such text names a pattern rather than using it, so a demonstration is never flagged. [INV-173]

---

## Requirement 13: The installed gate is the source gate, held by a config-health check

**Context:** A gate lives twice — its source in `guardrails/` travels with the repo, its installed copy in the hooks directory runs — and the two drift the moment an install is skipped. A stale installed hook silently under-runs the source's gate list, which is how a gate believed wired stays unenforced. The config-health check reds the drift and names the one fix, and it runs inside the suite so even a stale push gate that still runs the tests surfaces the drift.

**User Story:** As a maintainer trusting a wired gate, I want a config-health check that reds a missing or drifted installed hook against its source, so that a skipped install cannot leave a gate believed wired but unenforced.

### Acceptance Criteria

**Case: the check reds the drift**

1. *when* an expected hook is missing from the hooks directory or differs from its source, the system *shall* red the config-health check and name the one fix, running it inside the suite and wiring it into the push gate itself. [INV-175, INV-164]

**Case: it reads the whole source directory**

2. The system *shall* read the whole hook source directory against the installed set, so every hook the pack ships is covered the moment it lands with no edit to the check. [INV-175]
3. *when* a file lives only in the installed set — a personal-layer overlay the pack never ships — the system *shall* leave it alone, since it has no source to drift against. [INV-175]
4. *when* a checkout carries no installed hooks by design, such as a continuous-integration runner, the system *shall* skip the check by name. [INV-175]

**Case: the commit fence's second arm**

5. *when* a file is both staged and holding unstaged modifications at commit time, the system *shall* read it as a fence stop, the signature of a second writer touching a file mid-landing. [INV-175, INV-11, INV-174]

---

## Requirement 14: The installed skill copy is the source skill

**Context:** The pack authors a skill in `skills/<skill>` and the seat installs a working copy at the agent's skills home, and the two drift the moment an install is skipped, so an out-of-date installed skill silently runs an older behaviour than the pack ships. The config-health check gains a second arm beside its hook-diff arm to catch this, holding the installed skill copy to its source.

**User Story:** As a maintainer relying on installed skills, I want the config-health check to red an installed skill that has drifted from its pack source, so that a stale installed skill cannot silently run an older behaviour than the pack ships.

### Acceptance Criteria

**Case: the skill-copy arm**

1. *when* an installed skill tree is un-synced or drifted against the pack's `skills/` source, the system *shall* red the config-health check's skill-copy arm and name the one fix, to re-run `scripts/sync-skills.sh`. [INV-243, INV-175]
2. The system *shall* read the whole skill source directory against the installed set, so every skill the pack ships is covered the moment it lands and a personal-layer skill with no pack source is left alone. [INV-243, INV-175]

**Case: a shipped skill is held byte-pristine**

3. The system *shall* hold a shipped skill's installed copy byte-pristine, the recursive tree diff counting even an extra file dropped inside a shipped skill's directory as drift. [INV-243]
4. *when* a checkout carries no installed skills, such as a continuous-integration runner, the system *shall* stand the whole check down through its single top-of-file carve-out, so the skill-copy arm needs no skip of its own. [INV-243, INV-175]

---

## Requirement 15: A law that earns a gate gets a retroactive gate over the whole tree

**Context:** When a request or a stated law is extracted into a mechanical gate, the gate's scan is retroactive by construction: it reads the entire tracked tree, or the whole gated artifact set, rather than the changed lines alone. So the debt that predates the gate is found the day the gate lands, never the day each old file happens to be touched next.

**User Story:** As a person landing a new gate, I want its scan to read the whole tree from the first landing, so that debt older than the gate is found at once, in a single sweep of the tree.

### Acceptance Criteria

**Case: the scan is retroactive by construction**

1. *when* a law is extracted into a mechanical gate, the system *shall* scan the entire tracked tree or the whole gated artifact set, reaching beyond the changed lines, so debt that predates the gate is found the day the gate lands, as the browser-mute gate reds an old script the same as a new one. [INV-176, INV-164, INV-157]

**Case: an over-big backlog and the catch-up run**

2. *when* the found backlog is too big to fold at once, the system *shall* absorb it by the seeding law, seeding the cap at the current size so it ratchets down. [INV-176, INV-172]
3. *when* adoption or a catch-up walk runs, the system *shall* run the pack's current gate set backward over the host's existing tree the same way. [INV-176, A-11]

---

## Requirement 16: The pack's version is one fact, stamped outward from one home

**Context:** The product's version lives in one place, the root VERSION file. Every skill's frontmatter version line and every in-text base-version reference is a stamped copy written by the sync script at every bump and held by a guard test, so a copy that drifts reds the guard test instead of quietly disagreeing. A per-skill number hand-rolled at edit time drifts the moment attention does.

**User Story:** As a maintainer reading a version anywhere in the pack, I want every shown version to be a stamped copy of one root home, so that no two copies can disagree and a record's version line names the pack version.

### Acceptance Criteria

**Case: one home, stamped copies**

1. The system *shall* keep the root VERSION file as the one home and *shall* write every skill's frontmatter version line and in-text base-version reference as a stamped copy, refreshed by the sync script at every bump and held by a guard test that reds a drifted copy. [INV-178, INV-14]
2. The system *shall* have a record's version line name the pack version from this law on. [INV-178]

---

## Requirement 17: A release's number reports what taking it costs a host

**Context:** A release picks a version number, and the number answers one question for a host that vendored the previous version: what taking it costs the host, in the host's own action. A patch costs nothing, a minor costs a re-run of the catch-up walk, and a major costs a change to what the host already carries. The default is a patch, raised only where the release earns the higher tier.

**User Story:** As a host reading a release's number, I want it to tell me what taking the release costs me in my own action, so that I know whether to do nothing, re-run my catch-up walk, or follow a migration.

### Acceptance Criteria

**Case: the three tiers answer one question**

1. The system *shall* have a release's number answer one question for a host that vendored the previous version: what taking it costs the host in the host's own action. [INV-217]
2. *when* a release fixes a machine to hold a law already stated, with no new capability and no changed contract, the system *shall* number it a patch, which the host takes by doing nothing. [INV-217]
3. *when* a release grows what a host may adopt — a new capability, a new law, a new gate — in a backward-compatible way, the system *shall* number it a minor, which the host takes by re-running its catch-up walk with nothing it already carries rewritten. [INV-217, INV-91]
4. *when* a release cannot be taken without the host changing what it already carries — a reworded vendored rule, a renamed or removed surface a host depends on, a changed adoption or catch-up step, a moved law that forces host action — the system *shall* number it a major and ship its dated migration chapter. [INV-217, INV-91]

**Case: the tier call is a stated judgment**

5. The system *shall* default to a patch and raise to a minor or major only where the release earns the higher tier. [INV-217]
6. The system *shall* keep the minor-versus-major call a stated guidance the releasing session applies and names, held by no gate, the same standing as a design-review finding that never blocks a lane, since the call reads meaning a machine cannot. [INV-217, INV-141]
7. The system *shall* home this rule in the base rulebook, in build-pipeline's commit-and-show step, and here, beside the version-is-one-fact home. [INV-217, INV-178]

---

## Requirement 18: The pack's authored artifacts and their installed copies are one class

**Context:** A capability the pack authors lives twice — its source in the pack, a running copy on the host — and the two drift the moment an install or a stamp is skipped. The class carries one parity: each member names the mechanical net that tells its running copy stale. The installed skills were the class's weakest member, held by discipline where its siblings held by a machine, until the config-health skill-copy arm gave them a net too.

**User Story:** As a person trusting the pack's installed copies, I want every installable artifact to name the net that catches its running copy going stale, so that no installed copy can fall silently behind the pack it came from.

### Acceptance Criteria

**Case: the class and its parity**

1. The system *shall* read the pack's authored artifacts and their installed copies as one class, each member naming the mechanical net that tells its running copy stale. [INV-180]

**Case: each member names its net**

2. The system *shall* have the vendored kit scripts name the ratchet manifest's source pin, the pack version and content hash the update check reads against the pack's current copy. [INV-180, INV-172, INV-177]
3. The system *shall* have the installed hooks and gates name the config-health check that reds a hook missing from the hooks directory or drifted from its source. [INV-180, INV-173, INV-175]
4. The system *shall* have the stamped version copies name the stamp script and the guard test that reds a copy diverged from the one home. [INV-180, INV-178]
5. The system *shall* have the installed skills name the config-health skill-copy arm, backed by the session-run version compare at the freshness points, the same-session sync through the named tool, and the daily update proposal. [INV-180, INV-243, A-7, M-7, E-23, E-25, D-4]

**Case: the class binds forward**

6. The system *shall* have a new installable artifact state its own staleness net against this parity, the members named before the class standing as they are cited. [INV-180, INV-159]

---

## Requirement 19: Adoption adds the document-provenance axis

**Context:** Adoption adds one composition axis beyond the floor: document provenance, where a spec claim came from. A claim written fresh under the pack is native and trusted from the start. A claim recovered from documents a project held before adoption is re-engineered and starts unverified, staying unverified until it is reconciled against real code or removed.

**User Story:** As a person adopting an existing project, I want each spec claim marked by where it came from, so that a claim recovered from pre-adoption documents is checked against real code before it is trusted as truth.

### Acceptance Criteria

**Case: the provenance axis and its two values**

1. *when* a project is adopted, the system *shall* add document provenance as a composition axis, marking each spec claim by where it came from. [A-3, C-1]
2. The system *shall* read a claim written fresh under the pack as native and trust it from the start. [C-1]
3. The system *shall* read a claim recovered from a project's pre-adoption documents as re-engineered, holding it unverified until it is reconciled against real code or removed. [A-3]

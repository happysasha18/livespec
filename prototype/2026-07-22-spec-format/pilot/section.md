# Starting and adopting a project

This section continues the document whose format the intake page defines. The keywords *when*, *while*, *if*, *then*, and *shall* read as they do there. The bracket codes trail each criterion and point to the rule's home in the project spec; a reader can ignore them. Terms already defined in the intake glossary — request, inbox, pipeline, spec, architecture, invariant, proven document, skill, entry route, work type, session, backlog item, queue, journal, footprint, scope, stage, regression check, delivery, delivery report, default mark, guardrail, suite, compaction, movement, resume file, profile — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **pack** — the shipped live-spec method: its skills, its document and suite templates, and its guardrail scripts. It carries a version.
- **host** — one project the pack attaches to. Each host holds its own spec, queue, journal, and `.live-spec/` folder.
- **founding** — the start of a fresh host, where the shaping questions are answered in the new spec's opening and the templates are copied in.
- **adoption** — attaching the pack to a project already running, run as an ordered set of phases.
- **catch-up** — the sequence that brings an already-adopted host onto the pack's current version.
- **version-control gate** — the check that a host has git and a settled or explicitly declined remote before its first delivery.
- **scaffold** — the runnable suite the templates ship with. It defines what a green suite means for the first delivery.
- **personal profile** — the human's own settings file on the machine, holding their languages, how to address them, what they do, and their own vocabulary. The intake glossary's *profile* is the host's own project settings; this is the machine-wide file the person owns.
- **settings ladder** — the four nested scopes that resolve any setting: the session's live word, then the host profile, then the personal profile, then the pack default. A nearer scope overrides a farther one.
- **settings card** — the rendered page that lists every setting the pack knows, its current value where one is recorded, and one plain-speech line saying how to change it.
- **project kind** — what a host's product is, named from a curated vocabulary: book, backend service, static site, fullstack app, CLI, or skill pack. It is recorded in the host profile and seeds the host's defaults.
- **project layers** — the concrete parts a project kind decomposes into. They are the host's own footprint categories.
- **proof kinds** — the concrete checks a project kind proves its work with. They are the host's own test-ladder rungs.
- **design principle** — a checkable design rule that a project kind's products must hold, run by the verify pass in the medium's own form.
- **engine** — in an engine-and-instance pair, the generic reusable mechanism. It ships as its own host, public by default, tested on its own generic fixtures.
- **instance** — in an engine-and-instance pair, the concrete product a real person uses today. It holds the content and plugs into the engine.
- **content contract** — the engine's public list naming every place a concrete instance plugs in. Each entry has a handle and a test proving the engine works without that instance's value.
- **attic** — the host's append-only archive folder (`attic/`). A superseded file moves here with one manifest line and is kept rather than deleted.
- **migration chapter** — one dated, versioned entry in the migration guide (MIGRATION.md) stating the host-side steps a pack release requires.
- **installer** — the pack's one install script (`install.sh`). It copies the pack's skills onto a machine and backs up any existing copy first.
- **freshness check** — the check that compares each installed skill's version against the pack's and re-reads any skill whose version moved.
- **update check** — the once-a-day check that asks the public repo whether the pack has moved past what this machine runs.
- **ratchet manifest** — the host record that pins the pack version each vendored gate script came from.
- **agent card** — a host's self-describing file (`.live-spec/agent.md`) stating its name, mission, zones, published contracts, and inbox address.
- **founding-question set** — the versioned set of questions founding asks a host. It grows as the pack learns what a founding host owes; a host records which version it answered.

---

## Requirement 1: The version-control gate runs before the first delivery

**Context:** Every host reaches its first delivery through the same gate, and both a fresh start and an attach run it in the same order. A gate cannot protect files older than itself, so the gate runs before anything is created or moved. The gate settles two things: that git exists, and that a remote either exists or is declined on the record.

**User Story:** As a person starting or attaching a host, I want the version-control gate settled before the first delivery, so that no work is committed somewhere it cannot be recovered or tracked.

### Acceptance Criteria

**Case: git exists first**

1. *when* founding or adoption begins, the system *shall* run the version-control gate before it creates or moves any file. [INV-8, A-0, A-5]
2. *if* the host has no git, *then* the system *shall* initialize git and make a pristine baseline commit that doubles as the diff baseline. [A-5]

**Case: the remote is settled on the record**

3. Before the first delivery, the system *shall* settle the remote as a named deliverable: a remote exists, or the human has declined one, and the host's journal records which. [INV-8]
4. A recommendation of a remote *shall* not close the gate; the gate closes only on an existing remote or the human's recorded decline. [INV-8]

**Case: never deliver into an unversioned host**

5. The system *shall* refuse to deliver into a host that lacks version control. [INV-8]

---

## Requirement 2: Bootstrapping a fresh host

**Context:** A fresh host starts from the templates the pack ships. The system copies the document set and the suite scaffold, then the first request enters the queue and runs through the ordinary pipeline. The scaffold's green is the starting floor the first delivery builds on.

**User Story:** As a person starting a fresh host, I want the templates and a runnable scaffold in place, so that the first request runs through the ordinary pipeline against a known starting floor. [F-bootstrap, B-1]

### Acceptance Criteria

**Case: the templates land**

1. *when* the version-control gate has closed, the system *shall* copy the document templates — spec, architecture, test matrix, roadmap, journal, and the resume file — and copy the suite scaffold (`test_scaffold.py`) into `tests/`. [B-1]
2. *when* the templates are in place, the system *shall* offer hooks in plain words, and *shall* impose none. [E-6]
3. *when* the templates are in place, the system *shall* let the first request enter the queue and run from intake through the ordinary pipeline. [B-1]

**Case: the scaffold defines the first green**

4. The scaffold suite *shall* judge the first delivery green by four checks: the document set exists; every header is filled with content; the coverage checklist is present; and one live-state block is present. [B-1]
5. *when* a header holds a leftover template placeholder, the scaffold suite *shall* count that header as red. [B-1]
6. The scaffold green *shall* stand as the starting floor; the first delivery *shall* ship its own first real test beside the scaffold. [B-1]
   [GAP: the spec does not state what content a live-state block must carry for the scaffold suite to count it present.]

---

## Requirement 3: Founding asks its shaping questions and never infers them

**Context:** Before the first request is worked, founding answers the questions that shape everything downstream, in the new spec's opening. The first of them is whether the product is a personal tool or a reusable product. Every later sentence leans on this answer, so an inferred answer is the most expensive silent choice.

**User Story:** As a person founding a host, I want the founding questions asked outright at setup, so that the answers every later decision leans on come from my word rather than a guess. [B-2]

### Acceptance Criteria

**Case: the founding questions block the first request**

1. *when* founding begins, the system *shall* answer the founding questions in the new spec's opening before it works the first request. [B-2]
2. The system *shall* ask the personal-tool-or-reusable-product question first among them. [B-2]
3. This question *shall* block the first request until the system asks it or reads its answer from the profile; an ordinary open question rides along without stopping work, and this one *shall* not. [INV-4, INV-12, B-2]

**Case: the answer comes from the human or the profile**

4. *when* the personal-scope standing preference in the personal profile covers the answer, the system *shall* seed this host's default from it and *shall* say so aloud. [E-13, B-2]
5. *if* no standing preference covers the answer, *then* the system *shall* ask the human. [B-2]
6. The system *shall* derive no founding answer from example artifacts; naming three of the human's own artifacts *shall* not decide the product is those artifacts, since an inferred founding answer is a silent micro-decision at its most expensive. [B-2, INV-5]

**Case: adoption owes the same questions**

7. *when* adoption reaches its orient phase, the system *shall* put the founding questions again, personal-versus-reusable first. [A-1, B-2]

---

## Requirement 4: Founding learns who the human is

**Context:** Before any founding question resolves, the system learns who it is working with. It looks for the personal profile at its one home, at founding, at adoption's orient, and at the first session on a new machine or with a new human. The human tells the system about themselves, or names sources for it to read, and every line lands on the human's word.

**User Story:** As a person the system is about to work for, I want it to load or found my personal profile at setup, so that it works from what I told it and never from a silent assumption about me. [B-3]

### Acceptance Criteria

**Case: find the profile first**

1. *when* founding starts, adoption reaches orient, or a session opens on a new machine or with a new human, the system *shall* look for the personal profile at its one home first. [E-13, B-3]
2. *if* the personal profile exists, *then* the system *shall* load it, name the file, and read any unrecognized line aloud instead of skipping it silently. [E-13]
3. *if* the personal profile is absent, *then* the system *shall* offer to create it from `templates/profile.template.md`. [B-3]

**Case: every line lands on the human's word**

4. *when* the human tells the system a line about themselves, the system *shall* write that line faithfully. [INV-9, B-3]
5. *when* the human names a source — their repos, their docs, a public page — the system *shall* read it and propose lines, and *shall* accept or drop each proposed line one at a time on the human's word. A dropped proposal *shall* stay dropped. [INV-9, B-3]
6. The template *shall* mark every placeholder as a placeholder, so nothing in it can pass for the human's word. [B-3]

**Case: the human can decline, and a worker never onboards**

7. *if* the human declines the whole step, *then* the system *shall* run the session on pack defaults, say so, and raise the offer again at the next project setup rather than mid-work. [B-3]
8. *when* the personal profile already exists, the system *shall* skip the founding step and load the profile. [B-3]
9. A worker session *shall* onboard no one; its brief already carries the setting lines it needs. [ACT-3]

---

## Requirement 5: Founding proposes the engine-and-instance split

**Context:** A reusable product can still ship as one concrete thing a real person uses today — a gallery that hangs these photos, a coach that reads these tracks. The moment the reusable answer lands on a product that carries content of its own, founding asks one more shaping question: is the generic mechanism worth its own home, apart from the content it serves now. The system proposes; the human's word decides; both outcomes are recorded.

**User Story:** As a person founding a reusable, content-carrying product, I want the engine-and-instance split proposed rather than imposed, so that I decide whether the generic mechanism gets its own home. [INV-85]

### Acceptance Criteria

**Case: the split is proposed, and the human decides**

1. *when* the reusable answer lands on a product that carries content of its own, the system *shall* ask whether the generic mechanism is worth its own home. The human's word *shall* decide, and the system *shall* record both outcomes. [INV-85, B-2]
2. *when* the system proposes the split, the system *shall* name two homes and what each owns: an engine repo, public by default and tested on its own generic fixtures, carrying a content contract; and an instance home, holding the content, its corrections, and the private fragments. [INV-85, INV-79]
3. *when* the split proposal places binary content such as images or audio, the system *shall* place it by the architecture's placement prompt. [INV-75]

**Case: a declined split, and a taken split**

4. *if* the human declines the split, *then* the system *shall* record a one-line reuse note in the host profile under the key `reuse.split-declined: <date>`, and *shall* treat a single-repo host as a complete outcome. [INV-85]
5. *when* the human takes the split, the system *shall* bind the pair-leadership rules from that moment. [INV-85]
6. *when* a donor-specific constant is found while carving the engine, the system *shall* record it as a named content-contract entry with a test that proves the engine works without it. [INV-79]

**Case: the offer returns only when one home no longer holds**

7. *if* a declined product later outgrows one home — a second instance appears, or the content and the mechanism can no longer share one file — *then* the system *shall* raise the split offer again. [INV-85]
   [GAP: the spec does not name who judges that the content and the mechanism can no longer share one file, or by what measure.]
8. *when* adoption reaches orient, the system *shall* put the same split proposal alongside the other founding questions. [A-1, B-2]

---

## Requirement 6: Founding names the project kind, and the kind can change

**Context:** Beside personal-versus-reusable, founding asks what the project is — a book, a backend service, a static site, a fullstack app, a CLI, or a skill pack. The answer is recorded in one line in the host profile and seeds the host's defaults. The line stays alive: when work notices the project has outgrown its kind, the line updates on the human's word.

**User Story:** As a person founding or adopting a host, I want its project kind asked outright and recorded in one home, so that the host's defaults are seeded from a stated kind rather than a guessed one. [INV-36]

### Acceptance Criteria

**Case: the kind is asked and recorded**

1. *when* founding runs, the system *shall* ask the project kind and record it in the host profile on a `project.kind` line. [INV-36, E-13]
2. *when* adoption reaches orient, the system *shall* ask the project kind again with the rest of the founding set. [A-1, INV-36]
3. The system *shall* ask the project kind of the human every time; no personal-profile line can state what a host is. [B-2, INV-36]

**Case: three intake verdicts stay separate**

4. The system *shall* keep three verdicts separate and *shall* let none collapse into another: the project kind, which says what the product is and seeds project-wide defaults; the request's work type, which says what this request builds; and the placement, which says where the request lands on the feature map. [T-16, T-13, INV-30, INV-37]
5. *if* the host profile already records a `work-kind.host-default` line, *then* the system *shall* keep it, and the project kind *shall* not silently override that explicit line. [T-16, E-13]

**Case: the kind vocabulary and its growth**

6. The system *shall* name the project kind from the curated vocabulary, and *shall* add a custom kind through the queue when a named project the list did not serve well appears. [T-16]

**Case: the line stays alive**

7. *when* work notices the project has outgrown its kind, the system *shall* update the `project.kind` line on the human's word and journal it at that moment rather than parking it for an audit. [INV-36]

---

## Requirement 7: Founding declares the project's concrete layers and proof kinds

**Context:** The impact read, the footprint categories, and the test ladder are stated once by the pack in kind-abstract terms, and each project kind fills them with its own concrete parts. So the founding line that records the kind carries two more: the concrete layers this project splits into, and the concrete checks it proves with. The per-kind fill is the project's own ratchet from there.

**User Story:** As a person founding a host of a given kind, I want its concrete layers and proof kinds declared beside its kind, so that the footprint read and the test levels run against this project's real parts rather than a hardcoded list. [INV-135]

### Acceptance Criteria

**Case: two more lines beside the kind**

1. *when* the system records `project.kind`, the system *shall* also record a `project.layers` line naming the project's concrete footprint categories and a `project.proofs` line naming its concrete proof kinds. [INV-135, INV-36]
2. The three footprint categories *shall* hold across every kind — a presentation-only change touches what the audience meets and nothing behind it, a single-module change stays inside one owned layer, and a cross-cutting change moves a shared law or crosses more than one layer — while the layers themselves are the project's own. [INV-128, INV-135]

**Case: an incomplete founding line is flagged**

3. *when* adoption reads a host profile that records `project.kind` with no declared layers and no declared proofs, a founding check *shall* flag the line as incomplete, the way an unbacked surface is flagged. [INV-135, A-10]
   [GAP: the spec flags the missing layers and proofs at adoption; it does not state whether a bootstrap founding that omits them is flagged.]

**Case: the checks read the declared categories**

4. The footprint check and the test-level rule *shall* read the project's declared categories rather than a hardcoded code list. [INV-134, INV-135]
5. The architecture document *shall* carry the per-kind footprint-and-proof table beside the node-structure-by-kind scaffold, and the spec and test roles *shall* read the declared layers and proofs rather than assuming code. [INV-135]
6. *when* live-spec itself carries no product surface, the system *shall* ship the abstract law and leave the concrete assertion to the products it serves. [INV-163]

---

## Requirement 8: A project kind's design principles and the interactive-overlap rule

**Context:** Beside its layers and proof kinds, a project kind names a set of design principles: checkable design rules its products must hold. The pack ships a starter set per kind, and a founding that records a visual kind declares them in the host profile. The verify pass runs each principle in the medium's own form.

**User Story:** As a person founding a visual host, I want its design principles declared and run at verify, so that a design rule its products must hold is checked in the medium's own form. [INV-136]

### Acceptance Criteria

**Case: the principles are declared and run**

1. *when* founding records a visual kind, the system *shall* declare its design principles in the host profile on a `project.design-principles` line — the pack's starter set plus any the project adds. [INV-136]
2. *when* a visual kind is recorded with no design principles, a founding check *shall* flag it, the way a kind recorded with no layers or proofs is flagged. [INV-136, INV-135]
3. *when* the verify pass runs, the system *shall* read the declared design principles and run each in the medium's own form, beside walking each surface as a visitor and the feel pass. [INV-136, INV-30]
4. *if* a design principle is one the suite cannot make green — motion feel, a real-device gesture — *then* the system *shall* have the human check it by eye; *if* the suite can hold it, *then* the system *shall* make it a matrix row in the adopting project's suite. [INV-30, INV-77, INV-136]

**Case: the frontend starter set and the interactive-overlap rule**

5. The frontend kind's starter set *shall* gather the pack's frontend guidance — walking each surface as a visitor, the feel pass scaled to a whole site, and motion and scroll feel as the human's own check — and *shall* add the interactive-overlap rule. [INV-30, INV-136]
6. Two interactive controls from different visual layers — a player, a close button, a zoom handle — *shall* hold separate clickable regions, so every press lands on one control alone. A non-interactive element — a plaque, a picture, a caption — may overlap anything. [INV-136]

**Case: the prover catches the blind spot on the spec**

7. *when* two interactive controls from different layers are reachable on one screen while the covering surface leaves the lower control pressable, the prover *shall* report it as a finding, the same blank-answer class as an unwritten seam. [INV-136, INV-125, INV-126, INV-72]
8. For each covering overlay a project defines, the adopting project's suite *shall* open the overlay and assert every other interactive control is either not rendered or not pressable — computed `pointer-events:none`, `opacity:0`, or off-screen — while the overlay stands. [INV-136, INV-163]

---

## Requirement 9: The frontend kind's legibility floor

**Context:** Beside the interactive-overlap rule, the frontend kind carries a legibility floor: text meets a minimum contrast ratio against its background and a minimum size, so a human can read what a surface shows. The floor is read at two moments — the verify feel pass and the pre-show gate — the same two the register lint guards.

**User Story:** As a person shown a surface's text, I want it to meet a stated contrast and size floor, so that what a surface shows can be read. [INV-139]

### Acceptance Criteria

**Case: the floor's numbers**

1. The legibility floor *shall* require normal text at a contrast ratio of at least 4.5 to 1; large text — font size at least 24 pixels, or 18.66 pixels when bold — at a contrast ratio of at least 3 to 1; and body and caption text at a font size of at least 12 pixels. A host may set its own numbers on its word. [INV-139]

**Case: the two reading moments**

2. *when* the verify feel pass runs, the system *shall* read a product surface's computed colours and sizes against the floor. [INV-139, INV-30]
3. *when* a styled file is about to be shown to a human, the pre-show legibility lint (`scripts/preshow-legibility-lint.py`) *shall* read the declared colours and sizes against the floor, beside the register lint. [INV-139, INV-83]
4. *if* the pre-show legibility lint reads a result below the floor, *then* the system *shall* block the showing until the text is lifted to the floor. [INV-139, INV-83]

**Case: the pack ships the law, the product ships the assertion**

5. The pack *shall* ship the law, the floor's default numbers, and the script; the browser-computed assertion for a product surface *shall* live in the adopting product's suite. [INV-139, INV-163]

---

## Requirement 10: Adoption runs as an ordered set of phases

**Context:** Adoption attaches the pack to a project already under way. It runs as a sequence where each phase finishes before the next starts, and it assumes no blank slate. The version-control gate runs first so the whole run stays reversible.

**User Story:** As a person attaching the pack to a running project, I want adoption to read everything first and re-engineer it into the pack's shapes without trusting or losing anything, so that the existing work is preserved and checked before it is trusted. [F-adoption]

### Acceptance Criteria

**Case: orient and inventory**

1. *when* adoption begins, the system *shall* read every existing document — README, roadmap, spec, test suite, journals, TODO files, and repo wikis — before touching anything, and *shall* answer the founding questions about what was found. [A-1]
2. *when* orient completes, the system *shall* list the code, the user-facing surfaces, and the document set, each entry named with its owner, and surfaces named to file and line. [A-2]
3. Listing the surfaces *shall* seed the host's surface registry. [E-10]
4. The system *shall* keep adoption's working artifacts — the orient digest, the inventory, the reconcile notes — in the host's `.live-spec/adopt/`, tracked in git, and *shall* keep them out of the host's own folders. [A-8]

**Case: re-engineer the documents**

5. *when* the system re-engineers an existing spec, the system *shall* keep its claims as spec sections and mark them unverified. [A-3]
6. The system *shall* seed the architecture document's nodes from the inventory's file-and-line entries, turn existing tests into matrix rows cited at their real level, and turn an existing roadmap or TODO into queue rows. [E-14, E-15]
7. The system *shall* reconcile every unverified claim — pin it to file and line, or remove it — at the first delivery that touches its surface, or by the first milestone, whichever comes first. [A-3]

**Case: version-control gate, baseline, and incremental**

8. The system *shall* run the version-control gate before touching or moving anything. [A-5]
9. The system *shall* save a first baseline snapshot of the host's artifacts as found, git-tracked, as the diff baseline the snapshot machinery guards. [A-6, E-7]
10. *when* the earlier phases are done, the system *shall* run the host on the same request lifecycle as a bootstrapped host, and *shall* record the installed skill versions in `.live-spec/` at attach time. [A-7]
11. *when* the pack's version or an installed skill's version changes, the freshness check *shall* re-read the changed skill before continuing and write a one-line journal note naming old and new. [A-7, M-7]
12. *when* a safe breakpoint is reached, the freshness check *shall* re-stat the installed skills and the pack on disk and re-read whatever changed, and *shall* ask the public repo once a day whether the pack has moved. [A-7, M-2, E-25]

---

## Requirement 11: Every unbacked live surface gets one verdict

**Context:** An adopted product often carries a surface that reaches the user but has no spec backing — a de-facto prototype, the most common residue in an adopted host. Adoption flags each one at orient. The human then decides, per surface, what becomes of it.

**User Story:** As a person adopting a running product, I want every unbacked live surface flagged and settled per surface, so that nothing keeps running unexplained. [A-10]

### Acceptance Criteria

**Case: flag every unbacked surface**

1. *when* an inventoried surface reaches the user but carries no spec backing, the system *shall* flag it at orient for the human's verdict. [A-10]

**Case: the three verdicts**

2. *if* the human chooses promote, *then* the system *shall* enter the surface at the spec step as a feature. [INV-16]
3. *if* the human chooses quarantine, *then* the system *shall* move the surface into a prototype home, label it, and leave a dated one-line record at the prototype home stating what, why, and the date. This *shall* be treated as a production change, since the user loses the surface or sees it relabelled. [E-17]
4. *if* the human chooses attic, *then* the system *shall* archive the surface. [A-4]

---

## Requirement 12: Attic over deletion

**Context:** No adopt or rework run deletes a host file. A superseded file moves to the attic with a manifest line, so nothing removed from active use is lost. One exception passes only through the human's explicit gate.

**User Story:** As a person whose project is being adopted or reworked, I want every superseded file kept in the attic rather than deleted, so that nothing I authored is ever lost. [INV-7]

### Acceptance Criteria

**Case: the attic keeps what is superseded**

1. *when* an adopt or rework run supersedes a host file, the system *shall* move it to `attic/` with one manifest line stating what it was, why it moved, and the date, and *shall* delete nothing. [INV-7, A-4]
2. The attic *shall* be append-only, one manifest line per file. [A-4]
3. *when* two files collide on a basename in the attic, the system *shall* prefix the name with its source directory, and *if* the name is still taken, *then* append a numeric ordinal. [E-9]

**Case: the cruft-sweep gate**

4. *when* adoption offers a cruft sweep, the system *shall* list the file counts and sizes of regenerable junk — caches, build leftovers, already-gitignored files — and *shall* delete only on the human's explicit approval. [A-9]
5. The system *shall* route authored content through the attic and *shall* never let it qualify for the cruft sweep. [A-9]
   [GAP: the layout of the adoption attic — a flat folder with a manifest against dated subfolders — is an open decision. D-1]

---

## Requirement 13: The catch-up sequence brings an adopted host onto the current pack

**Context:** An already-adopted host falls behind the pack as the pack moves. The catch-up sequence brings the host's documents and records onto the current pack. The owner asks in any wording; the version delta decides that catch-up fires, whatever words the ask used. The sequence runs four phases in fixed order.

**User Story:** As the owner of an already-adopted host that has fallen behind, I want catch-up to bring it onto the current pack in fixed phases behind my gate, so that the host is brought current with nothing lost. [F-catchup, A-11]

### Acceptance Criteria

**Case: a release that owes host actions ships a chapter**

1. *when* a pack release changes something a host must act on, that release *shall* land one dated, versioned migration chapter stating the host-side steps; a release owing nothing *shall* add no chapter and *shall* say so in its changelog. [INV-91]
2. The system *shall* build the work list as the ordered chain of migration chapters from the host's recorded pack version to the current one, oldest first. [INV-91]
3. *if* the host's record carries no readable pack version, *then* the system *shall* start the chain at the earliest chapter. [INV-91, INV-89]

**Case: the four phases in order**

4. The system *shall* run catch-up in four phases in fixed order: orient on the delta, plan behind the owner's gate, execute while preserving facts, then verify and re-record. [A-11]
5. *when* orient runs, the system *shall* read the host's installed-set record and tree, read the pack's current version and journal, and build the work list as the difference; *when* preconditions in the guide disagree with the tree, the system *shall* take the tree as the truth. [A-11]
6. *when* the delta includes founding questions the host has never answered, orient *shall* read the host's recorded `founding.set-version` against the current set and name each question added since. [INV-227]
7. *when* the plan is written, the system *shall* write it into the host's `.live-spec/adopt/`, list every file that moves, merges, or retires and every open conflict, and *shall* move no file before the owner's word on the plan. A plan that finds nothing to do *shall* report that and end. [A-11, A-8]
8. *when* execute runs, the system *shall* open with a clean-tree baseline commit, run under the checkpoint discipline, and resume an interrupted run from the checkpoint under the already-given gate. [A-11, A-5]
9. *when* verify runs, the system *shall* run the host's own gates including the suite, keep the sequence open until the gates read green, re-record the installed-set record in the current format, and land one journal chapter. [A-11, M-7]

**Case: machine-level steps run once**

10. *when* a step touches the machine's shared homes — the installed-skills folder or the personal profile — the system *shall* run it once per machine and *shall* report it done and skip it when its already-done check passes. [A-11]

---

## Requirement 14: Every catch-up step is safe on a half-done state

**Context:** A catch-up sequence can stop partway and be resumed or re-run. Every step reads its precondition from the tree so that a step already done is skipped and a step that finds both the old and new form present merges them. The sequence preserves the host's recorded facts, and a fact leaves its home only to move to one that holds it without loss.

**User Story:** As the owner of a host mid-catch-up, I want every step safe to resume or re-run and every recorded fact preserved, so that an interrupted sequence applies nothing twice and loses nothing. [INV-89, INV-90]

### Acceptance Criteria

**Case: read the precondition, then act**

1. *when* a catch-up step opens, the system *shall* read its precondition from the tree. [INV-89]
2. *if* a step's end state already holds, *then* the system *shall* report it done and skip it. [INV-89]
3. *if* a step finds both the old and the new form present, *then* the system *shall* merge them file by file. [INV-89]
4. *if* two files hold identical content, *then* the system *shall* drop the old copy to the attic. [INV-89]

**Case: reconcile a differing profile by the ladder**

5. *if* a profile file differs between old and new, *then* the system *shall* reconcile it by where each line's home sits under the settings ladder: a host-profile line whose home is the personal profile moves up, and a host-scoped line stays. [INV-89, E-16]
6. *when* a line moves up into a machine-shared file, the system *shall* follow the promotion law and re-read that file immediately before appending. [E-16]
7. *if* any other differing file or remaining conflict is found, *then* the system *shall* ride it on the plan to the owner's gate; the system *shall* never nest a directory inside its replacement and *shall* never overwrite the new form with the old. [INV-89]

**Case: preserve facts and re-home them**

8. The system *shall* rewrite settled prose only where the owner rejected it or the new shape cannot hold it as written, and *shall* carry each proposed rewrite on the plan for the owner's decision. [INV-90]
9. *when* a host adopted under its own document names, the system *shall* keep those names, record each as a host-profile line (`spec.file: SPEC.md`), and *shall* read the pack's canonical name as the host's file under its recorded name. [INV-90]
10. *when* an installed-set record is kept in an outdated format such as commit pins, the system *shall* retire it to the attic and read the new record from the version lines of the skills installed on disk and the pack version. The skills on disk *shall* be the authoritative set. [INV-90, M-7]
11. *when* a stray state file is found — a checkpoint at the repo root, a closed checkpoint, a look-alike state directory — the system *shall* re-home it: a root checkpoint to `.live-spec/checkpoints/`, a closed one to the attic, and a look-alike directory merged under the half-done-state rule. [INV-90, INV-89]

---

## Requirement 15: Catch-up proves itself and stays restorable

**Context:** The catch-up sequence proves that content survived by comparing the host before and after. It records a pre-sequence inventory beside the plan, records the same inventory after execute, and accounts for every difference by a plan item. The pre-sequence state stays restorable from the baseline commit.

**User Story:** As the owner of a caught-up host, I want the sequence to account for every difference against the plan and keep a one-command restore point, so that no file changes outside the plan and the pre-sequence state can be recovered. [INV-92]

### Acceptance Criteria

**Case: the before-and-after comparison**

1. *when* the sequence starts, the system *shall* record a pre-sequence inventory beside the plan: every document with a content fingerprint, the host spec's anchor multiset, and the suite's verdict and count as found. [INV-92]
2. *when* execute completes, the system *shall* record the same inventory again and compare the two. [INV-92]
3. Every difference *shall* be accounted for by a plan item — a file unchanged, re-homed to a named path, merged from named sources, or resting in the attic under its manifest line; an anchor delta *shall* match a change the plan names; and the suite *shall* read at least as green as before. [INV-92]
4. *if* a difference falls outside the plan, *then* the system *shall* block the verify phase until the owner accepts it as a plan amendment or the step is reverted. [INV-92]

**Case: the restore point**

5. The plan document *shall* name the baseline commit and state the one command that returns the host to the pre-sequence state. [INV-92, A-5]
6. The attic *shall* keep every superseded file readable without any restore. [INV-92]

**Case: the sequence's own show**

7. *when* the sequence changes only documents and records and creates no product surface, the system *shall* skip the facet sweep and open the plan document by the ordinary show rule. [INV-92]

---

## Requirement 16: A same-version docs-layout pass rides one named vehicle

**Context:** An adopted host may want its own documents restructured with no pack-version delta. That ask routes to the host's own queue, and the pass runs one named vehicle rather than ad-hoc edits. The vehicle proves content survived and reads the suite green before it lands.

**User Story:** As the owner of a host restructuring its own documents with no version delta, I want the pass to ride one named vehicle with a proven restore path, so that the layout changes safely and content survives. [INV-111]

### Acceptance Criteria

**Case: the vehicle's steps**

1. *when* an ask restructures a host's own documents with no pack-version delta, the system *shall* route it to the host's queue and run one named vehicle. [INV-111, INV-110]
2. The system *shall* lock the owner's decisions in a checkpoint before any file moves, and *shall* build on a clean pushed base so one command restores the pre-pass tree. [INV-111, INV-107]
3. The system *shall* prove content survived by a word-token multiset check and a punctuation multiset check, since word-token identity alone passes a reflow that dropped or moved punctuation. [INV-111]
4. The system *shall* read the full suite green on the restructured tree from the suite log's own line, since a reflow can break a suite-owned doc check no multiset reads. [INV-111, INV-39]
5. The system *shall* land one journal chapter naming what moved and why. [INV-111]

**Case: closing the pass**

6. *if* the pass rides a branch back to main, *then* the system *shall* close it through the restructure merge gate, where the multiset proof serves as the gate's first part; *if* the pass lands directly on main, *then* the system *shall* stand it on its own green suite. [INV-111, INV-114]
7. A host *shall* cite this vehicle and *shall* never improvise a layout pass. [INV-111]

---

## Requirement 17: A restructure or migration merge gate judges the delta

**Context:** When a restructure or a migration is gated for merging back into main, the gate judges the delta rather than re-proving the untouched whole. It has three parts and routes pre-existing findings to the queue instead of blocking on them.

**User Story:** As a person merging a restructure or migration, I want the gate to judge only the delta, so that a large reorganization is verified without re-proving what it did not touch. [INV-114]

### Acceptance Criteria

**Case: the three parts**

1. *when* a restructure or migration is gated for merge, the system *shall* judge the delta in three parts: load-bearing token identity old-versus-new except the per-chunk named deltas plus the punctuation-multiset check; the full suite green on the merged tree; and a prover pass on both sides whose blocking set is scoped to the delta. [INV-114, INV-111, INV-39]
2. The system *shall* block on an unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change. [INV-114]
3. *when* a finding is present and equal on both sides, the system *shall* route it to a queue row in the same delivery and *shall* not block on it. [INV-114]

**Case: a deliberate redesign**

4. *if* a change is a deliberate redesign that changes content by intent, *then* the system *shall* route it by the architecture-redesign rule and stand its merge on the green suite and the delta-scoped prover pass, with no token-identity demand over text the redesign meant to change. [INV-114, INV-113]

**Case: a sharpened bar is said back**

5. *when* a session sharpens the human's spoken bar beyond the human's words, the system *shall* say the sharpened form back and mark it as its own interpretation. [INV-114]

---

## Requirement 18: The catch-up routing and its non-goals

**Context:** The catch-up sequence fires on one test: the host's recorded pack version is behind the current pack version. The owner's wording is an example, never the decider. A docs restructure with no version delta is the host's own queue row.

**User Story:** As the owner asking to bring a host up to date, I want the version delta alone to decide the routing, so that a same-version restructure is never misrouted into a migration sequence. [INV-110]

### Acceptance Criteria

**Case: the version delta decides**

1. *when* the host's recorded pack version is behind the current pack version, the system *shall* fire the catch-up sequence, whatever wording the ask used. [INV-110]
2. *if* an ask carries no version delta, *then* the system *shall* route it as the host's own queue row through its pipeline, whatever wording it used. [INV-110]
3. The system *shall* not fire catch-up on a first adoption, on a single-document edit, or on a restructure of the host's own product. [INV-110]

**Case: the non-goals**

4. The system *shall* execute catch-up as a procedure with no script automating it, *shall* force no rename, and *shall* keep no pack-side registry of hosts' catch-up states, since each host's own records carry its state. [INV-110]

---

## Requirement 19: The settings card shows at setup and answers the standing question

**Context:** At the end of founding, and again at the end of adoption's orient, the system renders the settings card. The human reaches it twice — here at setup without asking, and any later time by asking. The card shows what the pack has set up and what is the human's to change, and asks nothing.

**User Story:** As a person new to the pack, I want the settings card shown at setup and re-rendered whenever I ask what I can customize, so that I see every setting and change any of them by speaking its change-line. [F-onboarding, INV-87]

### Acceptance Criteria

**Case: the card shows at setup's end**

1. *when* founding ends, or adoption's orient ends and the project kind and the economy setting have settled, the system *shall* render the settings card. [INV-87, INV-36]
2. The card *shall* list every setting the pack knows, each row giving the setting's plain-words name, its current value for this host where one is recorded, and one line saying how to change it in plain speech. A recorded default *shall* be shown as told, and the card *shall* ask nothing. [INV-87, INV-31]
3. The system *shall* read each value from the settings ladder — the reader's own profiles and this host's recorded lines. [E-13, INV-87]
4. *when* the card opens, the system *shall* open it by the show rule — a new browser window on a local seat, its own channel on a remote seat — and *shall* pass the pre-show register lint on the fixed copy and the rendered values before it opens. [INV-67, INV-83]

**Case: the same card answers the standing question**

5. *when* the person later asks what they can customize, in any wording, the system *shall* answer with the same card re-rendered from the current truth, and *shall* let no hand-kept copy answer. [INV-87]

**Case: one catalog home**

6. The card and the standing answer *shall* derive from one source: the pack-defaults table joined with the reader's profile files and the host's recorded lines. No second hand-kept settings list *shall* exist. [INV-87]
7. Every card-visible table row *shall* appear on the card, every recorded profile line *shall* appear in the card's project-rules part, and every card row *shall* trace to a marked table row or a recorded profile line; a missing card-visible row and a card row with no source *shall* each be a defect. [INV-87]

**Case: the copy states rules, values stay the reader's own**

8. The card's fixed copy *shall* state each setting as a rule anyone can read, and *shall* show a personal value — a language, a name — only as the reader's current value, labelled as theirs to change. [INV-88]
9. The fixed copy *shall* never present one person's value as the product's prescription. [INV-88]

**Case: the render and its states**

10. A build-time script (`scripts/onboarding-card.py`) *shall* render the card from the pack-defaults table and the profile files, and *shall* fail the render loudly on a malformed table row. [INV-87]
11. *if* the personal profile is missing, *then* the script *shall* render the card on pack defaults, say plainly that no profile exists yet, and name how the founding offer creates one. [INV-87]
12. *when* the pack-defaults table grows a row, the system *shall* draft that row's card rule-copy on the clean-writer road before it first renders. [INV-84]

**Case: the card's facets**

13. *when* the viewport is a phone, or a window too narrow to hold multiple columns, the card *shall* read as one column top to bottom; on a window wide enough to hold them it *shall* keep its multi-column arrangement. [default] [INV-87]
14. The card *shall* be a static rendered page, plain structured HTML with headings and keyboard scrolling, and *shall* depend on no hover. [default] [INV-87]
15. The card's empty state *shall* be a missing personal profile — pack defaults shown, the absence said plainly, the founding offer named; its error state *shall* be a malformed catalog row — the render fails loudly; its blocked state *shall* be flagged text at the register lint — the showing stops until the text is fixed and the block names what it flagged. [INV-87, INV-83]
16. Rendering the card *shall* be read-only, so two sessions can render it at the same time; an open card *shall* show the truth of its render moment, and a later change *shall* not update the open page. [default] [INV-87]

---

## Requirement 20: Running an engine and its instance as a pair

**Context:** When founding takes the engine-and-instance split, the two repos run as a pair. Each repo is a full host with its own spec, queue, journal, and settings folder. No third document spans the pair. A lesson crosses between the two only through the inbox.

**User Story:** As the owner of an engine-and-instance pair, I want each repo to run as its own full host with the inbox as the only cross-seam channel, so that one window serves one repo and neither half writes the other's tree. [F-pair, INV-86]

### Acceptance Criteria

**Case: each repo is a full host**

1. Each repo of the pair *shall* carry its own spec, queue, journal, and `.live-spec/` folder, and no third document *shall* span the pair. [INV-86, E-1, E-14]
2. The engine's spec *shall* state what the mechanism does for any instance and *shall* cite no instance's content; the instance's spec *shall* state what the product is for its real user and *shall* cite the engine only by its content-contract handles. [INV-79, INV-86, D-7]

**Case: wishes and lessons cross the seam**

3. *when* a request is shaped for both engine and instance, the system *shall* split it at intake into one queue row in each repo, each citing the one spoken request. [T-17, INV-1, INV-37]
4. The system *shall* keep each repo's own inbox as the place outside items arrive; the instance's inbox is where the human hands in requests. [E-11, INV-37]
5. *when* a lesson travels between the two, the system *shall* carry it only through the inbox under write-ownership: the learning window files one new inbox file in the other repo and journals the hand-off in its own tree, writing no foreign tree beyond that one file. [E-11, INV-10, T-10]
6. One window *shall* serve one repo of the pair, *shall* stay read-only on the other half save for that one inbox file, and *shall* keep the concurrent-edit fence binding inside each repo. [INV-10, INV-11, INV-86]

**Case: the load-bearing crossing**

7. *when* the human throws a request at the instance window and intake finds a generic part and this instance's own part, the system *shall* file the engine-shaped part as one engine inbox request and park its own half as a dated blocked-on-engine debt line, so the lane keeps moving. [INV-37, T-17, E-11, INV-10, INV-56]
8. The dated debt line *shall* appear in the instance's every status report until the engine ships the request. [INV-27]
9. *when* the engine's session sweeps its inbox, the system *shall* land the request through the full pipeline on the engine's generic fixtures, make each new plug-in point a named content-contract entry with a works-without-it test, and ship and version on the engine's own rhythm. [T-10, INV-79, E-3]
10. *when* the engine ships, the system *shall* update the instance to that engine version, plug the real content into the new entry, verify on the real product, un-park the parked row, and close it whole. [INV-56, T-17]

**Case: the engine's spec carries its own provenance**

11. The engine's spec *shall* cite only the engine's own public commits for provenance and *shall* give each mechanism a neutral name in the engine's own vocabulary. [INV-119]
12. *where* a running instance shows a locale-specific label for a mechanism, the engine's spec *shall* note that string as instance-supplied copy and *shall* keep the neutral term as the mechanism's one name. [INV-79, E-4]
13. The publish gate *shall* check a generalized pack for two leaks: a private-instance provenance hash, and an instance's locale label standing as a mechanism name. [E-20, INV-119]

---

## Requirement 21: How the skills arrive and how a machine learns a newer pack exists

**Context:** The pack ships one installer that copies its skills onto a machine and backs up any existing copy first. A separate daily check tells a machine when the public repo has moved past what it runs. The check proposes; the human's word installs.

**User Story:** As a person running the pack on a machine, I want the installer to add skills without losing an existing setup and the daily check to tell me when a newer pack ships, so that updating stays my own step. [E-21, E-25]

### Acceptance Criteria

**Case: the installer**

1. *when* the installer runs, the system *shall* copy every pack skill into the agent's skills home (`~/.claude/skills/`). [E-21]
2. The installer *shall* be idempotent: it *shall* back up an existing copy with a timestamp before overwriting and *shall* delete nothing. [E-21]
3. The installer *shall* place the backup in an attic folder beside the skills home rather than inside it, so the agent never scans a stale copy as a live skill. [E-21]
4. The installer *shall* write to `.live-spec/` exactly what adoption's record clause writes. [E-21, A-7]

**Case: the daily update check**

5. *when* the day's first freshness point is reached, the update check *shall* run once, throttled by a dated stamp in the machine's pack home, and *shall* ask the public repo's VERSION file on main whether the pack has moved past the installed version. The update check *shall* be the outward twin of the dev-machine skill sync, which keeps the machine's copies true to the local repo. [E-25, M-7, E-23]
6. *if* the remote is newer, *then* the update check *shall* propose in the session's chat, naming both versions, pointing to what changed, and naming the install road; it *shall* install nothing. [E-25, ACT-1]
7. *if* there is no network or the answer is unreadable, *then* the update check *shall* report one honest skip line naming the address it tried, *shall* leave the stamp unwritten so the next session retries, and *shall* neither block nor guess. [E-25]
8. *if* the machine is ahead of the public repo, *then* the update check *shall* read as up to date and *shall* propose no downgrade. [E-25]
9. The update check's only surface *shall* be the proposal line, governed by the plain-language register. [INV-28]

**Case: the check reads vendored pins and never-answered questions**

10. *when* the update check sees the pack moved past the pin in the ratchet manifest, the system *shall* propose the re-install and name the vendored files whose content differs from the local pack's current copies, naming each stale key's own re-install road. [INV-177, INV-172]
11. *when* a host carries no ratchet manifest, the system *shall* give it the plain version proposal unchanged. [INV-177]
12. *when* the update check runs, its founding arm *shall* read the host's recorded `founding.set-version` against the current set and name each founding question the host has never answered, beside the vendored-file report. [INV-227]
13. *if* a host has no readable `founding.set-version`, *then* the founding arm *shall* name every founding question as potentially owed. [INV-227, INV-91]
14. The system *shall* surface a never-answered founding question for the owner to answer at catch-up, *shall* answer none on the host's behalf, since the duty binds forward, and *shall* home the recorded set version in the host profile and the agent card among the questions. [INV-227, INV-159, E-16, E-32, INV-184]

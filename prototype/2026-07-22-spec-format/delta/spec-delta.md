# Spec-delta: the spec format mechanism

This document states the requirements the format migration adds to `PRODUCT_SPEC.md`. It is a delta: it holds only the new requirements, written in the format they define, so a stranger can read them on first pass.

Bracket codes like `[INV-250]` point to the rule's home in the project spec. They are reference anchors for the maintainer; a reader can ignore them. The letter before the number names the rule's kind: `INV-` an invariant, a numbered rule of behaviour tests enforce. The codes minted here run from `INV-250`; a code below `INV-250` points to a rule that already stands in the project spec. Each criterion states the code it carries.

The keywords *when*, *while*, *if*, *then*, and *shall* are set in lowercase italics and carry their standard requirements meaning. *Shall* states a duty. *When* and *while* open a situation. *If* and *then* open a condition and its result.

A source hole — a place where a behaviour is stated but its judge, measure, or scope is not — is recorded as a `[GAP: ...]` line under the criterion it touches. Dates, provenance, and the reasons behind these requirements live in `JOURNAL.md`, not here.

---

## Glossary additions

Every domain noun this delta introduces is defined here, one sentence each. A noun already defined in the base spec glossary — *spec*, *journal*, *queue*, *backlog item*, *guardrail*, *suite*, *session*, *compaction*, *delivery* — carries its existing entry and is not restated.

- **requirements format** — the genre a spec document is written in: a preamble, a glossary, then a body of requirements.
- **requirement** — one unit of the body, made of a Context block, a User Story line, and acceptance criteria grouped into named cases.
- **named case** — one bold line naming a situation, followed by the two to six criteria that hold in it.
- **criterion** — one numbered line stating one trigger and one response, with its code anchor trailing at the line's end.
- **trigger** — the situation or condition a criterion opens with: a *when*, a *while*, or an *if* clause.
- **response** — the single duty a criterion states after its trigger: the *shall* clause.
- **glossary** — the block at the head of a spec document that defines every domain noun once.
- **closed vocabulary** — the rule that every domain noun in the document holds exactly one glossary entry.
- **domain noun** — a noun naming a thing the product deals in, as against a word of ordinary English.
- **source hole** — a place where the spec states a behaviour and leaves its judge, its measure, or its scope unstated.
- **GAP line** — the line that records a source hole under the criterion it touches, in the form `[GAP: ...]`.
- **weak word** — a relational word — proportional, larger, sufficient, fast, and their kind — that opens a slot for a reference point, a measure, or a reason.
- **slot** — the reference point, the measure, or the reason a weak word opens and its criterion must fill.
- **judge** — the named actor a criterion states as deciding one of its evaluative phrases.
- **generated index** — the code-to-location table a script builds from the body criteria at freeze; it is output only.
- **freeze** — the moment the spec is fixed for a release and its generated index is rebuilt from the body.
- **spec-touching delivery** — a delivery whose change set includes the spec document.
- **delta record** — the per-code declaration a spec-touching delivery carries, naming each touched code as new, sharpen, retire, or scenario-only.
- **delta kind** — one of the four words a delta record assigns to a touched code: *new* (a code the body did not carry before), *sharpen* (a code whose criterion text changed), *retire* (a code the body no longer carries), or *scenario-only* (a code whose criterion text is unchanged and only its named cases or examples moved).
- **criteria set** — the set of criteria a spec document holds at one moment, each keyed by its code and its criterion text.
- **delta classifier** — the pre-push gate that reads the delta record and diffs the old criteria set against the new one.
- **new-criteria budget** — the byte sum a spec-touching delivery declares for the criteria it adds under the *new* kind, each within the per-criterion byte cap.
- **size ratchet** — the recorded bytes-per-criterion bound of the spec document, which a delivery may not raise and may only lower.
- **bytes-per-criterion** — the byte count of a document's criterion lines alone, glossary and preamble bytes excluded, divided by the count of criteria in its body.
- **comprehension gate** — the two-layer check a changed section passes: the mechanical layer, then the cold-reader panel.
- **mechanical lint** — a free script check the comprehension gate runs before any reader: the vocabulary check, the one-name check, the weak-word check, or the style lint (INV-251).
- **cold reader** — a fresh reader who reads a changed section with zero project context.
- **cold-reader panel** — the set of cold readers a changed section is read by in one round.
- **finding** — one recorded item a cold reader returns on a section; a note-level finding is recorded and does not stop the section.
- **blocking finding** — a finding that a criterion cannot be understood or acted on as written; it stops the section from passing.
- **green line** — the single line a gate prints when it passes.
- **reach** — what a gate read to reach its verdict: the files it opened and the rows it matched of the rows it scanned.

---

## Requirement 1: The spec is a glossary and requirements a stranger can read

**Context:** The spec is the document that states what the product does for its user. Before this migration it was long-form prose with codes woven through it. After it, the spec opens with a glossary and states its behaviour as requirements: each requirement a Context block, a User Story, and acceptance criteria in named cases. A stranger opens the document and follows one requirement without asking what a word means or where a rule lives.

**User Story:** As a person reading the spec for the first time, I want it written as a glossary plus named-case requirements in plain words, so that I can follow any one requirement on first pass without project context.

### Acceptance Criteria

**Case: the document shape**

1. The spec *shall* open with a preamble, then a glossary, then a body of requirements, in that order. [INV-250]
2. Each requirement *shall* carry three parts in order: a Context block of two to four sentences, a one-sentence User Story, and acceptance criteria grouped into named cases. [INV-250]
3. *when* a criterion is written, the system *shall* place it in exactly one named case, and *shall* number the criteria continuously through the requirement. [INV-250]

**Case: the criterion form**

4. Each criterion *shall* state one trigger and one response, and *shall* trail its code anchor at the line's end. [INV-251]
5. The keywords *when*, *while*, *if*, *then*, and *shall* *shall* be set in lowercase italics, and no word in the document *shall* be written in all capitals outside a code anchor or a filename. [INV-251]

**Case: a source hole is recorded, never filled by invention**

6. *when* a criterion names a behaviour whose judge, measure, or scope the source spec does not state, the system *shall* name the plainest honest actor and *shall* write a `[GAP: ...]` line under the criterion. [INV-252]
7. *if* the source does not answer a behaviour, *then* the system *shall* write the gap line and *shall* invent no answer. [INV-252]

**Case: history lives in the journal**

8. The spec *shall* state today's behaviour only; dates, provenance, and the reasons behind past choices *shall* live in `JOURNAL.md`. [INV-253]
9. *if* a dated note or a provenance sentence appears in the spec body, *then* the system *shall* count it a defect and move it to `JOURNAL.md`. [INV-253]

**Case: closed vocabulary**

10. Every domain noun used anywhere in the document *shall* hold exactly one glossary entry; a word of ordinary English *shall* hold none. [INV-254]
11. *if* a domain noun appears in the body with no glossary entry, *then* the vocabulary check *shall* red. [INV-254]

**Case: one name per thing**

12. One thing *shall* carry one name everywhere in the document. [INV-255]
13. *if* one thing is referenced under two names, *then* the one-name check *shall* red. [INV-255]

**Case: every relational word fills its slots**

14. *when* a criterion uses a weak word — proportional, larger, sufficient, fast, and their kind — the sentence *shall* fill every slot the word opens: the reference point, the measure, or the reason, stated where the word stands. [INV-256]
15. *if* a weak word stands with an unfilled slot and no `[GAP]` line, *then* the weak-word check *shall* red. [INV-256]

**Case: every judgment names its judge and inputs**

16. *when* a criterion carries an evaluative phrase — broken, larger than, worth — the criterion *shall* name the actor that judges it and the inputs the actor judges by. [INV-257]
17. *if* an evaluative phrase names no judge and no inputs and carries no `[GAP]` line, *then* the comprehension gate *shall* treat it as a blocking finding. [INV-257]

**Case: when the gates arm**

18. *when* the migration converts the spec to this format, the system *shall* convert the whole document in one delivery. [INV-270]
19. Every gate this delta names *shall* arm in that same conversion delivery, and no gate *shall* arm before it. [INV-270]

---

## Requirement 2: The lookup index is generated from the criteria, never hand-written

**Context:** A maintainer follows a code from a criterion to its home and back. The map from a code to its location is a table. Before this migration the table was kept by hand and drifted from the body. After it, a script builds the table from the body criteria at freeze, so the table is output the build owns and no one edits. A code the body carries and the build misses, or the build carries and the body misses, stops the index gate — the gate that checks the body and the build agree.

**User Story:** As a maintainer following codes through the spec, I want the code-to-location table built from the criteria at freeze, so that the table never drifts from the body it describes.

### Acceptance Criteria

**Case: the index is generated output**

1. *when* the spec is frozen, the system *shall* build the code-to-location table from the criteria in the body. [INV-258]
2. The generated index *shall* be output only; *if* the generated index is edited by hand, *then* the system *shall* count the edit a defect. [INV-258]

**Case: the body and the build must agree**

3. *if* a code appears on a criterion in the body and not in the generated index, *then* the index gate *shall* red. [INV-259]
4. *if* a code appears in the generated index and not on any criterion in the body, *then* the index gate *shall* red. [INV-259]

**Case: the authored home of a rule's statement**

5. After the migration, the criteria and the glossary *shall* be the authored home of every code's plain statement: a criterion carries its code's rule, and an entity code's definition lives in the glossary. [INV-271]
6. The generated index *shall* carry locations only. [INV-271]
7. *when* the migration-end delivery lands, the description-field gate — `check-description-field.py`, the check behind INV-239 — *shall* retire, with the criteria and the glossary as its stated successor. [INV-271]

---

## Requirement 3: Every spec-touching delivery declares its delta per code

**Context:** A delivery that changes the spec adds, sharpens, or retires rules. Left undeclared, a rule can vanish or change wording without notice. So every spec-touching delivery carries a delta record: for each touched code it states one of four kinds — new, sharpen, retire, or scenario-only. Before the push, the delta classifier diffs the old criteria set against the new one and reds where the record and the diff disagree.

**User Story:** As a person reviewing a delivery that changes the spec, I want each touched code declared as new, sharpen, retire, or scenario-only and checked against the diff, so that no rule appears, changes, or disappears unannounced.

### Acceptance Criteria

**Case: the delivery declares a delta record**

1. *when* a delivery changes the spec, the system *shall* carry a delta record that names each touched code with one delta kind: new, sharpen, retire, or scenario-only. [INV-260]

**Case: the diff must match the record**

2. The delta classifier *shall* diff criterion text under normalization: whitespace collapsed, italic markers stripped, and letters case-folded outside code anchors. A difference that survives normalization is a text change; any other difference is none. [INV-261]
3. *if* a code is present in the old criteria set and absent from the new one with no *retire* declared for it, *then* the delta classifier *shall* red. [INV-261]
4. *if* a code is present in the new criteria set and absent from the old one with no *new* declared for it, *then* the delta classifier *shall* red. [INV-261]
5. *if* a code's criterion text differs under normalization between the old and the new criteria set with no *sharpen* declared for it, *then* the delta classifier *shall* red. [INV-261]

**Case: a sharpen replaces its old sentence**

6. *when* a code is declared *sharpen*, the delta classifier *shall* check survival by a normalized full-sentence match, and *shall* verify that the sharpened code's own criterion line no longer equals its old text. [INV-262]
7. *if* a *sharpen* code's old sentence survives that match anywhere in the document, *then* the delta classifier *shall* red. [INV-262]

**Case: growth stays inside the declared budget**

8. *when* a delivery declares its *new* criteria, the system *shall* sum their bytes into the delivery's new-criteria budget. [INV-263]
9. Each declared new criterion *shall* fit within a 500-byte cap; the cap's seed value is the pilot rewrite's measured average bytes per criterion, stated in the pilot's `NUMBERS.md`. [INV-263]
10. *when* the delta classifier measures the document's byte growth over the delivery, the delta classifier *shall* exclude declared sharpen bytes and glossary-addition bytes from the growth. [INV-263]
11. *if* the measured growth exceeds the declared new-criteria budget, *then* the delta classifier *shall* red. [INV-263]

**Case: one pen on the shared document**

12. The delta record *shall* ride the existing single-pen serialization for the shared spec document. [INV-198]
13. *when* a delivery merges after another delivery has frozen the spec, the delta classifier *shall* re-diff against the post-merge freeze baseline. [INV-261]

---

## Requirement 4: A document's bytes-per-criterion may only fall

**Context:** The spec grows one delivery at a time, and prose can bloat while the rule count holds. To hold the density, the spec document records a bytes-per-criterion bound — its size ratchet. The ratchet gate is the gate that holds this bound. A delivery may push the bound down or leave it, and may not push it up. Raising the bound is itself a change to this requirement and takes the same route: it goes through this pipeline as a spec change. The ratchet governs the spec document alone; the other documents keep their flat byte bound.

**User Story:** As a person who owns the spec's readability over time, I want the spec document's bytes-per-criterion bound to move only down, so that no single delivery is free to bloat the prose.

### Acceptance Criteria

**Case: the recorded bound**

1. The spec document `PRODUCT_SPEC.md` *shall* record a bytes-per-criterion bound, measured as the byte count of its criterion lines alone — glossary and preamble bytes excluded — divided by the count of criteria in its body. [INV-264]
2. The recorded bound *shall* live in the file `guardrails/spec-ratchet.json`. [INV-264]
3. The initial bound *shall* be the value measured at the migration-end freeze, recorded by the freeze actor. [INV-264]
4. The ratchet *shall* govern `PRODUCT_SPEC.md` only; `ROADMAP.md`, `TEST_MATRIX.md`, and `JOURNAL.md` *shall* keep their flat document byte bound. [INV-264]

**Case: the ratchet moves only down**

5. *when* a delivery freezes the spec document, the system *shall* compute the new bytes-per-criterion and *shall* require it to be at or below the recorded bound. [INV-264]
6. *if* a delivery's new bytes-per-criterion is above the recorded bound, *then* the ratchet gate *shall* red. [INV-264]
7. *when* a delivery's new bytes-per-criterion is below the recorded bound, the system *shall* lower the recorded bound to the new value. [INV-264]

**Case: raising the bound is a spec change**

8. The system *shall* raise the recorded bytes-per-criterion bound only through a change to this requirement, run through this same pipeline; no delivery *shall* raise the bound on its own. [INV-265]

---

## Requirement 5: A changed section passes the mechanical lints, then the cold readers

**Context:** A section is not shipped because its author finds it clear. It ships when it survives two layers. First the mechanical lints run — free scripts a machine runs on every push. Then a panel of cold readers, each reading with zero project context, reads the changed section; a blocking finding is fixed as it is found, and the section passes only after two reads in a row return zero blocking findings. A reader finding that names a source hole becomes a queue row, so the hole is tracked and not lost.

**User Story:** As a person shipping a changed section, I want it to clear the mechanical lints and then a cold-reader panel, so that a stranger can read it and every source hole a reader names is tracked.

### Acceptance Criteria

**Case: the mechanical layer runs first and free**

1. *when* a section changes, the system *shall* run the mechanical lints — the vocabulary check, the one-name check, the weak-word check, and the style lint — before any reader, on every push. [INV-266]
2. *if* any mechanical lint reds, *then* the system *shall* stop the section at the mechanical layer and *shall* send no reader. [INV-266]

**Case: the cold-reader panel**

3. *when* the mechanical layer passes, the system *shall* give the changed section to a cold-reader panel, each reader reading with zero project context. [INV-267]
   [GAP: this delta does not state how many cold readers form one panel, nor the actor that supplies them.]
4. *when* a cold reader returns a blocking finding, the system *shall* fix the finding before the next read. [INV-267]
5. The system *shall* pass a changed section only *when* two consecutive reads return zero blocking findings. [INV-267]

**Case: a section that will not converge**

6. *when* four rounds of reads have run on one section and new blocking findings still arrive, the system *shall* escalate to the human as a named question stating which terms keep failing, and *shall* pause the panel until the human answers. [INV-267]

**Case: a source hole a reader names becomes a queue row**

7. *when* a cold reader's finding names a source hole, the system *shall* open a queue row for the hole and *shall* record the criterion it sits under. [INV-268]

---

## Requirement 6: Every gate in this family states its reach on the green line

**Context:** A gate that prints green proves nothing until a reader knows how much it read. The gates in this family — the index gate, the delta classifier, the ratchet gate, and the mechanical lints — each read files and match rows. So each states its reach on the line it prints when it passes: the files it opened, and the rows it matched of the rows it scanned. A reader of the green line knows the verdict and its reach together.

**User Story:** As a person reading a gate's green line, I want it to state what the gate read, so that I can tell a real pass from a pass that read nothing.

### Acceptance Criteria

**Case: the green line carries the reach**

1. *when* a gate in this family passes, the system *shall* print a green line that names the files it opened and the count of rows it matched of the rows it scanned. [INV-269]
2. *if* a gate passes while its scanned-row count is zero, *then* the system *shall* mark the pass as reading nothing rather than printing a bare green line. [INV-269]

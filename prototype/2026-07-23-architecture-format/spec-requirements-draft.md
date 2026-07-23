# PRODUCT_SPEC requirements — the architecture format member (draft)

These are the draft requirements that carry the architecture format's definition into PRODUCT_SPEC.md,
written in the requirements genre the existing family members use (Requirement 283 for the matrix,
Requirement 286 for the queue). They add three requirements — Requirement 289, Requirement 290, and
Requirement 291 — under the next free invariant codes INV-278, INV-279, and INV-280. The member's own
definition lives at `docs/architecture-format.md`; these requirements bind that definition under the
gates that hold the family. The proposed new glossary entries the requirements lean on are listed at
the end.

---

## Requirement 289: The architecture is a family member written as node sections

**Context:** ARCHITECTURE.md is the format family's fourth member, joining the spec, the matrix, and the queue. The page `docs/architecture-format.md` defines the member — the laws it inherits from the family and the parts particular to the architecture — and this requirement binds that definition, putting the architecture's shape under the gates that hold the family. The architecture's reading job is a component inventory: a reader opens it to learn what parts exist, what each is for, which spec facts each owns, and where the part sits on disk. Each part is one node, and each node is one section headed `### [node: <name>]`, carrying its responsibility, the spec anchors it owns, the file-and-line pins where it lives, and a short notes line for what the other fields cannot hold.

**User Story:** As a maintainer reading the architecture, I want its format governed by the family's laws and gates, so that reading and holding it costs what the other family documents cost.

### Acceptance Criteria

**Case: the member definition and its inheritance**

1. The architecture *shall* follow the family genre by reference to `docs/spec-format.md` — closed vocabulary, keyword form, trailing anchors, no-history, generated-section gating, the comprehension gate — and *shall* restate none of them, its own definition living at `docs/architecture-format.md`. [INV-278]
2. The architecture *shall* open with a preamble, then its body of node sections, then the generated tables the member-definition page fixes in order. [INV-278]

**Case: a node is a section with four fields**

3. Each node *shall* stand as one section headed `### [node: <name>]`, and a node promised under an open queue row with its machinery still ahead *shall* carry the target tag in that heading, the matrix's block heading for the node reading the same. [INV-278]
4. A node section *shall* carry four fields — the responsibility, one sentence naming what the node is for; the owns list of spec anchors; the pins list of file-and-line places its responsibility is carried on disk; and a notes line, present only *when* the other three cannot hold something. [INV-278]

**Case: every anchor lives under exactly one node**

5. Every spec anchor *shall* be owned by exactly one node, and the suite *shall* hold that bond both ways — each anchor to its node and each node to its anchors. [INV-278]

**Case: when the gates arm**

6. The architecture's conversion *shall* follow the family's one-delivery arming rule: the whole document moves at once, every consumer of the old shape is repointed in that delivery, and this member's gates arm inside it. [INV-278] [INV-270]

---

## Requirement 290: An owns anchor cites its rule and carries no history

**Context:** A node's owns list points at the spec anchors the node implements, and the rule each anchor names lives once at the spec. So an owns entry cites that home and adds at most one parenthetical sentence saying where the anchor sits or why the node keeps it; a law copied back into the owns cell is a second home and a defect. *when* the spec turns out to lack a sentence the owns cell was carrying, that sentence moves into the spec clause in the same delivery, so the words survive at their one home. The architecture states today's structure alone: the dated prover-record table leaves for its own dated home under the prover records, and a pin carries no date and no provenance, the journal already telling when and why the node landed.

**User Story:** As a maintainer following an owns anchor, I want it to cite one home and carry no history, so that the rule lives once and the architecture reads as today's map.

### Acceptance Criteria

**Case: the owns anchor cites, and a restated law is a defect**

1. An owns entry *shall* cite the rule's home at the spec by its anchor and *shall* trail at most one parenthetical sentence saying where the anchor sits or why the node keeps it. [INV-279]
2. *if* an owns cell restates the rule its anchor names, *then* the suite *shall* red, the restated law standing as a second home. [INV-279]

**Case: content the spec lacks moves to the spec**

3. *when* an owns cell carries a sentence the cited spec clause lacks, the system *shall* move that sentence into the spec clause in the same delivery, so the content lives once at the spec. [INV-279]

**Case: the architecture carries no history**

4. The dated prover-record table *shall* relocate verbatim to its own dated home under the prover records, and the family's no-history law *shall* thereafter reach this document. [INV-279]
5. A pin *shall* carry no date and no provenance, the journal holding when and why the node landed. [INV-279]

---

## Requirement 291: One node reader serves every consumer of the node shape

**Context:** The node sections are read by many checks — the traceability suite's tests, the node-growth counter, the pin-drift check, and every test asking which node owns an anchor. One reader reads the node shape for all of them: the node names, each node's owned-anchor set, and each node's pins. It is the sibling of `guardrails/specformat.py`, the spec format's one reader. A consumer that reads the raw node shape on its own reads a shape that can drift under it, so such a consumer is a defect the conversion retires. The node-growth counter's hardcoded node-name list retires the same way — it re-derives the list from the reader, so a renamed node stays in step across every consumer.

**User Story:** As a maintainer changing a node, I want every check to read the node shape through one reader, so that a rename or a moved anchor reaches every consumer at once and none reads a stale shape.

### Acceptance Criteria

**Case: one reader, every consumer through it**

1. One reader — the node reader — *shall* read the node shape, the node names, each node's owned-anchor set, and each node's pins, and every consumer *shall* read through it: the traceability tests, the node-growth counter, the pin-drift check, and every test asking which node owns an anchor. [INV-280]
2. *if* a consumer reads the raw node shape on its own, *then* the suite *shall* red, that consumer standing as a defect the conversion retires. [INV-280]

**Case: the hardcoded node list re-derives**

3. The node-growth counter's node-name list *shall* re-derive from the node reader, so a renamed node *shall* stay in step across every consumer. [INV-280]

---

## Proposed new glossary entries

These domain nouns appear in the requirements above and are absent from the current PRODUCT_SPEC.md
glossary. Each is drafted to match the shape of its sibling entries (compare **roadmap format** and
**test-matrix format** for the member entry, and **node block** for the section entry).

- **architecture format** — the format-family member the architecture document is written in: a preamble, then a body of node sections, then the architecture's generated tables; it inherits the family's shared laws from the spec format and adds only the architecture-particular rules, its definition at `docs/architecture-format.md`.
- **node section** — the section one architecture node stands as, headed `### [node: <name>]` and carrying four fields: the responsibility, the owns list of spec anchors, the pins list of file-and-line places, and a notes line for what the other fields cannot hold.
- **node reader** — the one reader that reads the node shape — the node names, each node's owned-anchor set, and each node's pins — read through by every consumer of the architecture; the sibling of `guardrails/specformat.py`, the spec format's one reader.

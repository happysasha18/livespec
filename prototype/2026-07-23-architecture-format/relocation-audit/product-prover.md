# Relocation audit — node `product-prover`, **owns** field

Source: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, `### [node: product-prover]`, line 61.

The field opens with the owned anchor codes (M-6, INV-61, INV-72, INV-114, INV-125, INV-140, INV-170, INV-171 — codes, not prose), then a framing clause ("also carries lenses it does not own, each named beside its actual owner:") introducing a chain of twelve lens-ownership notes. Each lens note is one fragment below. A bare `lens-name (owner X)` is a wiring note that stays (KEEP); a note whose gloss restates a design fact or rule the spec already carries under the lens's clause is DUPLICATE. Anchor = the spec code the named lens maps to (the prose carries no trailing code of its own).

| fragment (quoted) | anchor | class | evidence |
|---|---|---|---|
| "the entry-symmetry lens (owner spec-author)" | INV-50/INV-29 | KEEP | Bare wiring note — lens named, owner (spec-author) stated, no rule restated. |
| "the entry-state lens (owner spec-author — the state a re-entry opens in, the complement of entry-symmetry's path-existence check)" | INV-167 | DUPLICATE | Spec Req 64 line 1508: "The entry-symmetry lens tests that a re-entry path exists; this lens tests the state that re-entry opens in." |
| "the transition-payload lens (owner spec-author — the parent of the motion and entry-state lenses)" | INV-168 | DUPLICATE | Spec Req 65 line 1540: "…read the motion-parity lens as this lens on the exit's animation and the entry-state lens as this lens on a re-entry's internal state, both instances this parent generalizes." |
| "the declared-laws station including its per-law net-check (owner spec-author — a declared law with no named net is a broken invariant, backstopped by the every-fact-owned-once check below)" | INV-101/INV-150 | DUPLICATE | Spec line 1326: "*when* a declared law names no net, the system *shall* rank the missing net a broken invariant…"; backstop at line 1346: "…keeping the architecture's one-owner check as the backstop." |
| "the paired-transition-symmetry lens with its reversibility-of-means half (owner spec-author)" | INV-126 | DUPLICATE | Spec Req 261 states both halves as the lens's own Cases — line 5915 "**Case: the reversibility of the means**" under the paired-transition-symmetry requirement (INV-126). The two-halves structure is the spec's. |
| "the scenario-level entry/exit lens (owner spec-author)" | INV-127 | KEEP | Bare wiring note — lens named, owner stated, no gloss. |
| "the edge-condition-completeness lens (owner spec-author)" | INV-138 | KEEP | Bare wiring note — lens named, owner stated, no gloss. |
| "the interactive-overlap lens (owner base-rulebook)" | INV-136/INV-30 | KEEP | Bare wiring note — lens named, owner (base-rulebook) stated, no gloss. |
| "the cross-source-disagreement lens (owner build-pipeline; a product-vs-spec divergence it names routes by the spec-is-the-definition-of-correct reconciliation law, owned by build-pipeline)" | INV-144 | DUPLICATE | Spec Req 46 title line 1153: "When the product and the spec diverge, the spec is the definition of correct"; line 1163: "…route the divergence to the home that owns it." |
| "the prototype-norm lens (owner build-pipeline; a prototype-born clause with no pointer, or text contradicting its own artifact, is a finding)" | INV-43 | DUPLICATE | Spec line 2312: "…the system *shall* flag a prototype-born clause carrying no pointer, and *shall* flag a clause whose text contradicts its own artifact." |
| "the delivery-separability lens (owner spec-author — the dual of the composition-axes law: a declared axis adding runtime code that ships as one artifact with no named reason and no owed delivery road is a finding … dual-discovery habit)" | INV-248 | PARTIAL | Finding rule is in spec — line 6057 "the dual of the composition law", line 6065 "an axis that adds runtime code and carries neither sentence, shipping as one artifact because the choice went unexamined…", line 6064 (the owed delivery road). Spec lacks the trailing fact, quoted verbatim: "the lens carries the prover's dual-discovery habit". |
| "and the discovery-side sibling of the declared-class uniformity lens is the design review (owner design-reviewer), which reaches the undeclared same-kind groupings the uniformity lens cannot" | INV-141 | DUPLICATE | Spec Req 61 line 1454: design review "…build its own transient inventory of every element a person acts on…"; line 1455: "…propose elements whose sentences match as a same-kind group…" — the design review reaching the undeclared groupings is its spec-stated role. |

## Pins-provenance list

The **pins** field (line 63) holds four pins:
- `skills/product-prover/SKILL.md:158` (review modes)
- `skills/product-prover/SKILL.md:312` (unwritten-seam hunt — the stress-lens family, INV-72)
- `.live-spec/profile.md:6` (gate cadence instance)
- `skills/product-prover/SKILL.md:170` (restructure-merge gate — INV-114 delta-judging)

None of the four labels carries a date, a session number, or a landed-row (ROADMAP row) provenance note. The parentheticals are pure descriptors or bare INV cross-references (INV-72, INV-114). **Pins with provenance: 0.**

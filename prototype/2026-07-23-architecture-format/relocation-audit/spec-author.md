# owns-field prose audit — [node: spec-author]

Source: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, section `### [node: spec-author]`, **owns** field (line 53). Spec cross-check: `PRODUCT_SPEC.md`.

The owns list carries anchor codes plus four prose fragments. The INV-248 parenthetical splits into a law-statement clause and a wiring clause; the rest are one fragment each.

| fragment (quoted; shortened past 40 words) | anchor | class | evidence |
|---|---|---|---|
| the delivery-separability law — the dual of INV-244's composition-axes law: a declared axis adding runtime code states whether the delivered artifact splits along it or ships whole for a named reason | INV-248 | DUPLICATE | Spec R266.1 (line 6057): "The system *shall* read whether the delivered artifact divides along a declared axis its kind owes or arrives as one piece, the dual of the composition law that reads whether behaviour divides along that axis." (R266.2/R266.3 add the runtime-code + named-reason halves; R266.9 names it "the delivery-separability member of the composition-lens family.") |
| the lens carried by product-prover | INV-248 | KEEP | Cross-node wiring note — product-prover carries the lens, ownership stays at spec-author (reciprocal of the product-prover node's "delivery-separability lens (owner spec-author…)"). |
| the enumeration-threshold structure rule: a prose paragraph packing an enumeration of three or more distinct parallel facts reads as a bulleted or numbered list … read by eye and by the prover's cognitive-load lens | INV-215 | DUPLICATE | Spec R134.1 (line 2902): "*when* a paragraph carries three or more distinct, parallel facts, the system *shall* render the enumeration as a bulleted or numbered list…"; R134.2 (line 2903): "…leave the rule read by eye and by the prover's cognitive-load lens, earning no mechanical lint of its own…" |
| also carries the prototype-norm pointer's format sentence (`norm: <path>`, frozen copy in `docs/norms/`) — wiring, the invariant's owner is build-pipeline | (prototype-norm) | KEEP | Wiring note — the invariant's owner is build-pipeline; spec-author only carries the format sentence. Explicitly self-labelled "wiring". |
| also carries the pole-declaration duty for a new host-specific capability (the pack-to-host split, owner base-rulebook) | (pole-declaration) | KEEP | Wiring/ownership note — owner base-rulebook; carried here, ownership stays elsewhere. |

## pins provenance (line 55)

Pins field: `skills/spec-author/SKILL.md:135` (spine), `:160` ([target] tag tripwire), `:181` (axes composition), `:243` (fences), `:263` (facet sweep — the canonical facet list), `:83` (the enumeration-threshold structure rule, INV-215).

Pin labels carrying a date, a session number, or a landed-row provenance note: **none**. No spec-author pin label carries any such provenance marker.

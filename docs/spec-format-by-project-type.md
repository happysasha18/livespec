# Spec format by project type — design note (decided 2026-07-09, Alexander)

Working capture of a decided direction. The polished authoring of this into the pack
(spec-author + architecture instructions) is a later step, best done from a clean agent.

## The decision

Borrow Kiro's traceability mechanic; make the primary spec UNIT a parameter of project
type, the way BMAD swaps templates by domain. Keep our single-document shape — no
per-feature file sprawl.

### The mechanic (one, for every type)
- Each primary unit carries a stable inline ID (a bracket code, same family as `[T-x]`,
  `[M-x]`): e.g. `[feature: F-wish]` on the scenario heading.
- Downstream artifacts back-reference the ID: an ARCHITECTURE coverage row names the
  implementer(s) and the test for each unit; a test's matrix row already names its unit.
- The suite checks BOTH directions: every unit ID has an implementer + a test; every
  implementer traces to at least one unit. Missing either side goes red. This is the same
  shape as the existing `[target]`↔queue-row and `M-x`↔test checks — an extension that reuses the
  existing machinery.

### The unit is per project type
| project type | primary unit | coverage check validates |
|---|---|---|
| web / app | feature / user story (a visible flow) | every feature → architecture node(s) + test |
| CLI / library / API | command / function / endpoint | every surface → contract + owning module + test |
| methodology package (live-spec itself) | rule / guarantee the pack promises | every guarantee → an enforcing mechanism (script, gate, template) |
| content / book / article | argument / chapter / section | every promised argument → a home in the outline (structure check; no technical architecture) |

A project declares its type once; the type sets the unit name, the acceptance-criterion
style, and what the coverage check means. For a book the check degrades gracefully to an
outline/structure check.

### No file explosion
One PRODUCT_SPEC.md, one ARCHITECTURE.md, one TEST_MATRIX.md. Feature IDs live inline in the
scenario. Shard into per-feature files only for a genuinely huge project, by explicit call.

### Hypertext references in Markdown
Source stays plain, standard MD: a bracket code `[F-wish]` plus one index table
(ID → section → implementer → test). When a doc is rendered, `render-doc.py` resolves a
`.md` cross-link to its rendered `.html` neighbour and lands its `#anchor` on the target
heading (ROADMAP row 195, shipped 2026-07-10); resolving a bracket code to its index row
stays an optional later leg.

### On our live spec
live-spec is a methodology package, but its SPEC scenarios are the product's features:
```
## Throwing a wish        [feature: F-wish]
As a producer, I throw a wish and the workshop turns it into shipped, tested work.
flows: intake [T-x] → name → show → build → land

ARCHITECTURE.md coverage row:
| feature | implemented by                               | test  |
| F-wish  | feedback-intake, build-pipeline, spec-author | M-0xx |
```

## Grounding (research 2026-07-09)
- Kiro: requirements.md (user story + EARS criteria, numbered 1 / 1.1 / 1.2) · design.md ·
  tasks.md; each task back-references requirement numbers (`_Requirements: 1.1, 2.3_`).
- BMAD: PRD → architecture → epics → stories; adapts to non-software domains via expansion
  packs (the document unit itself is swapped per domain).
- Requirements-engineering standard: ISO/IEC/IEEE 29148 (unique, verifiable, traceable
  requirements + a traceability matrix); architecture views from arc42 / C4.

## Sequencing
English + one-thought-per-paragraph sweep → product-prover pass → build this feature/flow
format → authoring-terminology corpus. This format sits on a clean, proven spec and is a
pre-migration foundation.

## Standard vocabulary — the field's names for our parts
The pack's method is its own, but its concepts are the field's, and naming the lineage lets a reader who
knows requirements engineering recognize what a live-spec document is doing.

| our house term | the standard it maps to |
|---|---|
| a use-case-first scenario | a use case / user story (ISO 29148 §9.4; Kiro's requirements.md) |
| entities · states · transitions · invariants | a state model + the "shall" requirements of ISO 29148 |
| composition across axes | cross-cutting concerns (arc42 §8) / the relationships of a C4 model |
| the Formal index + traceability check-phrases | a requirements traceability matrix (ISO 29148 §5.2.8) |
| the primary unit + feature coverage | the traceable unit and its coverage (Kiro's `_Requirements:` back-reference) |
| the facet sweep | non-functional requirements / quality attributes (ISO/IEC 25010; arc42 §10) |
| a quality budget + its instrumentation home | an arc42 quality scenario (§10) with a measurable fit criterion |
| the `[target]` tag | a backlog / roadmap item named but not yet specified for build |
| architecture nodes + seams | C4 containers/components + their relationships; arc42 building-block view (§5) |
| the runtime view (a flow's walk through the nodes) | arc42 runtime view (§6); a C4 dynamic diagram |
| the placement view (what runs where, with its technology) | arc42 deployment view (§7); a C4 deployment diagram |
| the shape at a glance (tiers-first reading order) | BMAD architecture's high-level overview; Kiro design.md's Overview section |
| the runtime view's if-it-fails fallbacks | BMAD's error-handling strategy section; Kiro design.md's error handling |

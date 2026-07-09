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
  shape as the existing `[target]`↔queue-row and `M-x`↔test checks — an extension, not new
  machinery.

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
(ID → section → implementer → test). Rendered pages do not yet resolve a bracket code or a
`.md` cross-link to its section anchor (`render-doc.py` renders `[text](href)` verbatim);
that resolution is queued (ROADMAP row 195).

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

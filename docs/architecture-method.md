# The architecture method

Every project in this method keeps one ARCHITECTURE.md. The doc names the parts the product is
built from, assigns every spec fact to exactly one part, and shows how the promised behaviour runs
through them. It is written from the proven PRODUCT_SPEC.md, and it is itself proven before the
test matrix is derived from it. The normative shape lives in the template
([templates/ARCHITECTURE.template.md](../templates/ARCHITECTURE.template.md)); the pack's own doc
([ARCHITECTURE.md](../ARCHITECTURE.md)) is the worked example this page links throughout.

Two words carry the whole doc. A **node** is a named part with one responsibility; one node carries
one name (the one-surface-one-name rule, applied to structure). A **seam** is a place where two
nodes meet and data crosses.

## Tiers first

The doc reads tiers-first. A **tier** is a place where things run: build-time on the author's
machine, a static file on a content delivery network, the client browser, an edge worker, an
external service. The doc
opens with the shape at a glance — the tiers in a few plain lines — then the nodes, then the flows
that walk those tiers, then the budgets. A reader lands oriented before any table detail. The
placement table below is the full tiers-and-technology statement; the opening lines only sketch it
(spec: "The doc reads tiers-first", [PRODUCT_SPEC.md](../PRODUCT_SPEC.md)).

## The template's sections

The template carries ten sections, in this order. Each line below says the section's job; the
template's own text is the normative wording.

- **The shape at a glance** — the tiers in two to five lines, so the reader knows what runs where
  before any table. The pack's own version:
  [the shape at a glance](../ARCHITECTURE.md#the-shape-at-a-glance).
- **Node structure by project.kind** — a starting node split proposed by the project's kind
  (fullstack app, backend service, CLI, skill pack, book), with the seam each kind's composition
  bugs hide in. The kind proposes the shape; the spec's facts decide the final nodes (INV-36).
- **Nodes** — the table that owns the doc: each node's one-line responsibility, the spec facts it
  owns, and its pin. A **pin** is a `file:line` pointing at where the responsibility is carried in
  code, produced by a command actually run. Worked example: [Nodes](../ARCHITECTURE.md#nodes).
- **Seams** — each seam names what crosses it and which side owns the format. Where a real schema
  crosses (a JSON contract, an API shape), the row names the schema's one home. Worked example:
  [Seams](../ARCHITECTURE.md#seams).
- **Runtime view** — one short walk per promised flow: which node serves each step, where the flow
  can fail, what happens then (INV-74). Detailed below.
- **Placement view** — the tiers-and-technology table: where every node runs, plus secrets and
  heavy content (INV-75). Detailed below.
- **Quality budgets** — measurable numbers with their instrumentation homes (INV-41). Detailed
  below.
- **Feature coverage** — the map from each spec feature to its implementing nodes and a test
  (E-29). Detailed below.
- **Decisions — where they live** — one pointer table to the decisions' real homes. Detailed below.
- **Prover record** — one dated line per prove pass, pointing at the record file. Worked example:
  [Prover record](../ARCHITECTURE.md#prover-record).

A coverage rule closes the template: every spec anchor appears in some node's "owns" column. An
orphan fact means a missing node or a missing assignment; a node that owns nothing has no spec
backing, and that is itself a finding.

## The runtime view — flows and fallbacks

A **flow** is one promised behaviour running end to end; the flow unit comes from the project's
kind. A web product walks its visitor scenarios, a CLI walks one invocation per command, a skill
pack walks a wish through the skills, and a book crosses no machines — one sentence saying so
satisfies the duty. For every flow the spec promises, the doc walks the running product: which node
serves each step, and where the flow can fail (INV-74).

Every named failure point carries its fallback — a degrade, a retry, a guard — so "if X fails, Y
happens" is readable per flow. A failure point without a fallback sentence is an unfinished walk. A
flow the doc cannot walk end to end is a finding: a node is missing or a seam is unnamed.

Each hop cites its seam by name; the payload and format stay the seam table's fact, stated once
there. The pack's own flows: [Runtime view](../ARCHITECTURE.md#runtime-view).

## The placement view — where everything runs

Every node states its tier, plus the load-bearing technology choice where one exists — the
embedding model, the render harness, the store (INV-75). The table is first-class, so a reader
answers "where does this run" for any node at a glance. A single-place project (a book, a local
CLI) satisfies the duty with one sentence. The pack's own table:
[Placement view](../ARCHITECTURE.md#placement-view).

Two placements belong here by law:

- **Secrets.** The table says where each secret lives (a keychain, a platform binding, an env
  store) and which tier holds each verdict that must never be decided on the client. A secret's
  place is architecture; an implementation footnote is the wrong home for it.
- **Heavy binaries.** An image archive, audio, video, or model weights name their home here:
  object storage, or the machine's archive plus a named backup. A git repository is the wrong home
  for large binaries — hosting caps bind per file and per repo — and a derivation that finds one
  raises it as a finding.

## Quality budgets

A **budget** is a measurable number the architecture commits to, paired with its instrumentation
home — where the number is measured and where a human reads it (INV-41). The project's kind
proposes the dimensions: paint and interaction times for a product, latency and error rate for a
backend, run time and per-unit cost for a CLI, eval pass rate and suite time for a skill pack. A
quality with no honest number is said by name; a vanity metric is banned. The numbers are the
host's taste: the doc proposes them, and the human's word sets them at the surface's first budget
landing. The pack's own budgets: [Quality budgets](../ARCHITECTURE.md#quality-budgets).

## Feature coverage

The feature layer sits above the fact-to-node matrix (E-29). Each primary unit of the project — a
feature, a command, a guarantee, named by the kind — carries an inline `[feature: F-x]` tag on its
spec heading, and the coverage table maps every unit to the nodes that implement it and a test that
exercises it. The check runs both ways: every tag has a row, every row traces to a tagged unit, and
every named node and test is real. Worked example:
[Feature coverage](../ARCHITECTURE.md#feature-coverage).

## Decision records

The doc keeps one pointer table to decisions; the decisions themselves stay where they were made —
the queue's dated rows, the journal's chapters, and the spec's open decision marks. The table is
the doc's single entry point to them, an architecture-decision log held as an index. A
structure-changing decision
also leaves a line in the prover record. Worked example:
[Decisions — where they live](../ARCHITECTURE.md#decisions--where-they-live).

## The prover's architecture lens

Like the spec, the doc is proven before anything derives from it: a product-prover pass with the
architecture lens. The lens checks six things, each judged at the project's kind scale (normative
home: [skills/product-prover/SKILL.md](../skills/product-prover/SKILL.md)):

1. every spec fact has an owning node;
2. no node stands without spec backing;
3. every seam names what crosses it and which side owns the format;
4. the quality budgets are stated with their instrumentation homes (INV-41);
5. the runtime view walks every flow the spec promises (INV-74);
6. the placement view says where every node runs, with its load-bearing technology (INV-75).

Every pin must be a real `file:line` citation; a prose description fails the check. The paired
PRODUCT_SPEC.md must be in view, since ownership is only checkable against the fact list it owns.
The lens grew from three checks to six on observed evidence: a real derivation passed the
three-check lens and shipped with no budgets and no views, because a mandate the lens never asks
about gets skipped. The validation record is
[docs/prover/2026-07-09-row180.md](prover/2026-07-09-row180.md).

The doc stays iterative. It maps the product as it stands plus the landing in flight; a future
feature earns its node when its landing arrives, and a speculative node is unbacked structure the
prover flags. Re-proving happens exactly when the structure changes — a new node or a new seam. A
plain fact assignment triggers no re-prove.

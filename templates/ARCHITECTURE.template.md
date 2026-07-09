# [Project Name] — Architecture

How the product is BUILT: the named nodes the spec's facts live in. Written from the proven PRODUCT_SPEC.md,
proven itself (product-prover, architecture lens) before the test matrix is derived from it. One node =
one name = one responsibility — the one-surface-one-name rule, applied to structure.

**When this doc changes:** a large or surface-class wish updates it BEFORE the matrix is touched; a bug or
small wish only cites the existing node it lands in. Re-proven only when it changes.

**This doc is ITERATIVE. Never written milestones ahead.** It maps the product as it stands plus the
landing in flight. A node exists for what ships today, or for what the spec already promises under an
owned queue row (marked [target], pin empty until code lands). A future feature earns its node when its
landing arrives; a speculative node is unbacked structure — the prover flags it as a node without spec
backing.

---

## Node structure by project.kind

The project's kind (`project.kind`, SPEC INV-36 — set once at founding/adoption) PROPOSES the starting
node structure; the spec's facts then decide the final nodes. The proposal is a scaffold to fit, never a
frame to force — a node still earns its place by owning a spec fact, and a speculative node is unbacked
structure the prover flags. Pick the row for your kind, then adjust.

| project.kind | the nodes it usually splits into | the seam composition bugs hide in |
|---|---|---|
| fullstack app / static site | a frontend (views / components / client state) · a backend (services, API, data) · a template or renderer that turns data into markup · a store | the browser↔server contract, and template↔data (a value rendered stale) |
| backend service | an entry / handler layer · the domain core it calls · a data store · each external integration | the API contract and the store boundary (a partial write, a schema drift) |
| CLI / library / API | a command / entry surface · the core modules behind it · an I/O boundary — one node per public surface | entry↔core (argument parsing) and core↔I/O (a missing or malformed input) |
| skill pack (live-spec's own kind) | one node per skill · the shared rulebook · the templates · the guardrails — the skill IS a node | skill↔skill (the handoff) and base↔working-skill (the inherited rule) |
| book / content | usually ONE docs node owns the whole outline; a new node only when the structure genuinely grows | section↔section (the narrative flow / a forward reference) |
| a custom kind | derive the split from the spec's own surfaces; name the seams where two of them meet | wherever two surfaces share state or a format |

The kind sets the SHAPE; the facts fill it. Two projects of the same kind can end with different node maps
because their specs differ — the table saves a blank-page start, and the coverage rule below is what
actually proves the map complete.

**Two shapes the plain rows miss (learned by deriving a real project's map, 2026-07-09):**
- **A derive-pipeline tier.** A data-heavy or ML project's "build" is not templating — it is a multi-stage
  DERIVE: several nodes chained by intermediate data contracts (`raw → catalog.json → vector.json →
  render-data.json`), each contract with its own format owner, often with a human-overlay seam where a
  person's correction must win over the machine's guess. When the build is more than one hop from data to
  output, give each stage its own node and name the contract between them; do not collapse six derive steps
  into one "build" node.
- **Kinds blend — static-first + a narrow edge backend.** A static site and a fullstack app are not
  exclusive. A project can be static-first (the front is a deterministic bake on a CDN, crawlable without JS)
  yet still carry ONE narrow server surface — an edge worker holding secrets, cache/state, and any verdict
  that must not be decided on the client. Name that worker its own backend node and its private-data seam
  (what the bake injects that never ships as a static asset); the kind is then "fullstack, static-first",
  not "static site".

## Nodes

Every spec fact is OWNED by exactly one node. In a live codebase every node pins to its owning
`file:line` (each pin from a command actually run — an unverified pin is merely a claim). In a
new project the pin column starts empty and fills as code lands.

| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |
|---|---|---|---|
| [e.g. renderer] | [builds the HTML widget from analysis JSON] | INV-1, T-3, E-2 | `build_widget.py:120` |
| [e.g. player] | [multi-stem playback, seek, mute/solo] | INV-4..6 | `player.js:1` |

## Seams

The places two nodes meet — named, because that is where composition bugs live. Each seam states what
crosses it and which side owns the format.

| Seam | Between | What crosses | Format owner |
|---|---|---|---|
| [analysis → render] | [analyzer · renderer] | [analysis JSON] | [analyzer] |

## Runtime view

How each promised flow runs through the nodes (SPEC INV-74). The flow unit comes from the project's
kind: a web or app product walks its visitor scenarios; a CLI walks one invocation per command; a skill
pack walks a wish through the skills; a book crosses no machines and says so in one sentence, which
satisfies the duty. One short walk per flow: which node serves each step, what crosses each hop, where
the flow can fail. Each hop cites the seam it crosses by name — the payload and format stay the seam
table's fact, stated once there. A flow the doc cannot walk end to end is a finding: a node is missing
or a seam is unnamed.

| Flow | The walk through the nodes | Where it can fail |
|---|---|---|
| [e.g. visitor plays a track] | [player loads analysis JSON (seam: analysis → render) → renderer draws the charts → player syncs the playhead] | [a stale analysis JSON; a chart drawn before data arrives] |

## Placement view

Where every node runs (SPEC INV-75): build-time on the author's machine · static file on a CDN · client
browser · edge worker · external service — plus the load-bearing technology choice where one exists (the
embedding model, the render harness, the store). First-class, so the reader answers "where does this
run" for any node at a glance: keep this table, or fold a "runs at" column into the Nodes table when the
map is small. A single-place project (a book, a local CLI) satisfies the duty with one sentence.

| Node | Runs at | Load-bearing technology |
|---|---|---|
| [e.g. renderer] | [build-time, author's machine] | [python3 + jinja] |
| [e.g. story API] | [edge worker] | [Cloudflare Worker + KV] |

## Quality budgets

Measurable numbers plus each budget's instrumentation home — where the number is measured and where a
human reads it (SPEC INV-41). The project's kind proposes the dimensions (product: paint/interaction
times; backend: latency/throughput/errors; CLI/pipeline: run time, per-unit cost; skill pack: eval pass
rate, suite time; prose: what honestly has a number). A quality with no honest number is said by name,
never given a vanity metric. Numbers are the host's taste: propose with a recommendation, set on the
human's word at the surface's first budget landing.

| Budget | Number | Instrumentation home |
|---|---|---|
| [e.g. first image on a cold visit] | [≤ 2 s] | [the perf line in the deploy check's output] |

## Feature coverage

The feature layer above the anchor matrix (SPEC E-29): the project's primary unit (a feature, command,
guarantee, or argument — named by `project.kind`) carries an inline `[feature: F-x]` tag on its spec
heading, and this table maps every unit to the node(s) that implement it and a test that exercises it.
The check runs both ways: every tag is a row here, every row is a tagged unit, every named node and test
is real.

| Feature | Implemented by | Test |
|---|---|---|
| [F-example] | [node name(s)] | [test name] |

## Prover record

| Date | Doc version proven | Record |
|---|---|---|
| [YYYY-MM-DD] | [v0.1] | `docs/prover/YYYY-MM-DD-architecture.md` |

---

*Coverage rule (walked at matrix derivation): every spec anchor appears in some node's "owns" column —
an orphan fact means a missing node or a missing assignment; a node owning nothing traces to no spec
backing and is itself a finding.*

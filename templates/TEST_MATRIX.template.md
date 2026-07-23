# [Project Name] — Test Matrix

Derived from the proven PRODUCT_SPEC.md **through the proven ARCHITECTURE.md** — the matrix is derived,
never just filled, and it is the test-matrix member of the format family (`docs/test-matrix-format.md`).
Rows are organized **architecture node × spec fact**: every fact gets at least one row under its owning
node, every row pins a test level, and each row is one criterion carrying both sides — what the fact does
and what it must never do — with its spec anchor trailing the sentence. The derivation closes against the
mechanical gates below, not a hand-walked checklist. Tests come from the matrix; the matrix comes from the
spec and the architecture, never from the code.

**Test levels:**
- `string` — assert against raw source text / Python output (fast, no render)
- `DOM-text` — parse the rendered HTML and assert on element content
- `browser-computed` — headless browser, assert on computed style / layout / interaction
- `pixel` — screenshot comparison (use sparingly; fragile)

Any fact about visibility, layout, colour, or interaction gets level ≥ `browser-computed`.

---

## Artifact inventory

Every file the user receives. Each inventory entry owns at least one rendered-level test row.

| Artifact | Path | Type | Owning test |
|---|---|---|---|
| [e.g. Widget HTML] | `output/widget.html` | rendered | `test_widget_renders` |

---

## Matrix rows — grouped by architecture node

One `###` block per node from ARCHITECTURE.md, so "is this node covered?" is answerable by looking at one
block. Every row states the positive and the negative side — what the fact does and what it must never do —
its status one of *built*, *todo*, or *retired* in lowercase italic, and its spec anchor trailing the fact
sentence in brackets.

### [node: renderer]

| ID | Fact (from spec) | Test level | Owning test | Status |
|---|---|---|---|---|
| M-001 | [Plain-language fact, e.g. "Stem player shows all four stems on load"; never a blank shell] [INV-1] | browser-computed | `test_stem_player_loads` | *built* |
| M-002 | [Fact; never its regression] [CR-2] | string | `test_...` | *todo* |

---

## How coverage is held

The coverage checklist the matrix once walked by hand retires; two mechanical checks hold its facts at
every run.

- The **row lint** (`test_matrix_rows_have_level_and_negative_side`) reds a row that pins no level from
  the ladder or states no never side, naming the offending row.
- The **generated Reference gate** (`guardrails/check-matrix-reference.py`) maps every spec anchor a body
  row carries to its rows and reds a stale anchor no row carries, so anchor coverage and stale-reference
  catching are the gate's, not a checkbox's.

The standing suite holds the derivation's other facts: every module block owns at least one
**interface-level row** asserting the module's declared interface (P9); every row's level follows its
footprint **layer** — a presentation fact at `browser-computed` or above, a single-module fact at its
module's interface, a cross-cutting law by a string test across the surfaces it governs (P8); every
declared cross-cutting law owns a test per surface it governs (INV-101); every artifact-inventory entry
owns at least one rendered-level row; and every test removes what it creates in a temp home the suite's
leak check diffs. A fact with no row, or a row at a too-weak level, is a derivation defect — fix it here,
before it is a production bug.

---

## Reference

The anchor-to-row table below is generated output, built from the body rows by
`scripts/build-matrix-reference.py`; no one edits it by hand. It is spliced in at freeze and maps each spec
anchor to the matrix rows that cover it, ranges and compound anchors expanded.

| Anchor | Rows |
|---|---|
| INV-1 | M-001 |

---

*Add rows as the spec grows. Retire rows (mark *retired*, never delete) when a feature is removed — so the
removal is auditable.*

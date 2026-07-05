# [Project Name] — Test Matrix

Derived from the proven SPEC.md **through the proven ARCHITECTURE.md** — the matrix is DERIVED, never just
filled. Rows are organized **architecture node × spec fact**: every fact gets at least one row under its
owning node, every row pins a test level, and the derivation closes with the coverage validation at the
bottom of this file — a checklist actually walked, not decoration. Tests come from the matrix; the matrix
comes from the spec and the architecture — never from the code.

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
block. Every row states the positive AND the negative side — what the fact does and what it must never do.

### [node: renderer]

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-001 | [Plain-language fact, e.g. "Stem player shows all four stems on load"] | INV-1 | browser-computed | `test_stem_player_loads` | BUILT / TODO / SKIP (reason) |
| M-002 | [Fact] | CR-2 | string | `test_...` | TODO |

---

## Coverage validation — walked at every derivation, re-walked at milestones

Derivation is not done until every line below is checked against the CURRENT spec + architecture:

- [ ] Every spec anchor (invariant / state / transition) appears in ≥ 1 row.
- [ ] Every architecture node has ≥ 1 block, and its negative-side rows exist (the regression fence).
- [ ] Every artifact-inventory entry owns ≥ 1 rendered-level row.
- [ ] Every visibility / layout / colour / interaction fact sits at level ≥ `browser-computed`.
- [ ] No row cites a spec anchor or node that no longer exists (stale rows are RETIRED, not deleted).

A fact with no row, or a row at a too-weak level, is a **derivation defect** — fix it here, before it is
a production bug.

---

*Add rows as the spec grows. Retire rows (mark RETIRED, do not delete) when a feature is removed — so the removal is auditable.*

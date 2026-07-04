# [Project Name] — Test Matrix

Derived from the proven SPEC.md. Every row comes from a spec invariant, state, or transition — not from the code. Tests come from the matrix; the matrix comes from the spec.

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

## Matrix rows

| ID | Fact (from spec) | Spec ref | Test level | Owning test | Status |
|---|---|---|---|---|---|
| M-001 | [Plain-language fact, e.g. "Stem player shows all four stems on load"] | INV-1 | browser-computed | `test_stem_player_loads` | BUILT / TODO / SKIP (reason) |
| M-002 | [Fact] | CR-2 | string | `test_...` | TODO |

---

*Add rows as the spec grows. Retire rows (mark RETIRED, do not delete) when a feature is removed — so the removal is auditable.*

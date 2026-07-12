# PENDING DRAFT — row 257 (INV-113/M-252), drafted 2026-07-12 by an Opus drafter, NOT yet applied
# Next session: brief a sonnet applier from these blocks (the row-225/row-233 applier briefs are the shape);
# versions: read live values, +0.0.1 each; the index anchor note inside applies.
# LANDING ORDER for tonight's batch: 257 → 258 → (260 STOPPED, see its file). This row lands FIRST.

Row 257 is draftable. Here is the delta.

---

# DELTA — Row 257 (INV-113 / M-252) — DRAFTABLE

Row 257 is a single behavioural law (size `small` in the queue). It needs a genuinely new invariant:
the pack today states two narrower things — build-pipeline step 3 "write or update ARCHITECTURE.md
from the proven spec", and the refactor line "if the refactor moves node boundaries, ARCHITECTURE.md's
pins update in the same change" — and neither forces a real redesign to re-shape the document. No
existing anchor covers "a deliberate redesign re-shapes AND re-proves the architecture document in the
same movement" (INV-37/E-14 own the re-carve ROUTING — a restructure opens its own row and re-proves —
but not the document-rework OBLIGATION, and the refactor line's pins-only path is under-scoped). Owner
node = **build-pipeline** (it owns the architecture step and the refactor door), so the matrix row sits
in the `[node: build-pipeline]` block. Row 257 does **not** touch `live-spec-base`, so the seven
working-skill `` `live-spec-base` (v1.0.5) `` header pins do **not** move.

The law lives in three homes (spec clause + build-pipeline architecture step + build-pipeline refactor
line), so a single **canonical block** is embedded verbatim so the needles match after whitespace-collapse:

> CANONICAL BLOCK (identical in the spec clause + the build-pipeline re-carve paragraph; the refactor
> line carries the two needles inline):
> `When structure is deliberately redesigned — layers restacked, a surface's ownership moved, nodes merged or split — the architecture document is re-shaped to the new form and re-proven with the architecture lens in the same movement. Updating the pins alone is scoped to a boundary shift that leaves the document's shape standing; after a real redesign the old shape itself lies, so fresh pins on a stale shape are a defect.`

## 257.1 — NEW TEST FILE (full content) — `tests/test_architecture_redesign_owes_rework.py`

```python
"""A deliberate architecture redesign re-shapes and re-proves ARCHITECTURE.md in the same movement — M-252 (SPEC INV-113, row 257).

The tlvphotos window's word, 2026-07-11 ~23:11: a second-finger bug (a moving finger dragged the
underlying room layer into view in the polaroid side room, the resting-finger fix having opened the
window for it) led Alexander to order a rethink of the UI-layer architecture plus a spec update, and he
asked whether the pack already forces the document rework in that case. The honest answer was only
partly: build-pipeline step 3 updates the doc from the spec and the refactor line updates its pins, but
after a real restacking the old document's own shape lies even with fresh pins. The law: when structure
is deliberately redesigned (layers restacked, a surface's ownership moved, nodes merged or split) the
architecture document is re-shaped to the new form and re-proven with the architecture lens in the same
movement; the pins-only path is scoped to a boundary shift that leaves the shape standing. String rows
on the law's two prose homes plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestRedesignOwesReworkLaw(unittest.TestCase):
    HOMES = (
        "PRODUCT_SPEC.md",
        "skills/build-pipeline/SKILL.md",
    )

    def test_redesign_owes_rework_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "re-shaped to the new form and re-proven with the architecture lens in the same movement",
                body,
                home,
            )

    def test_pins_only_scoped_to_boundary_shift_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "a boundary shift that leaves the document's shape standing", body, home
            )

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-113]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-113 |"):
                    self.assertIn("redesign", line)
                    return
        self.fail("INV-113 index row missing")


if __name__ == "__main__":
    unittest.main()
```

Needles (verbatim, whitespace-collapsed) in BOTH prose homes: `re-shaped to the new form and re-proven
with the architecture lens in the same movement`, `a boundary shift that leaves the document's shape
standing`. Spec-only: `[INV-113]`, index row `| INV-113 |` contains `redesign`.

## 257.2 — SPEC CLAUSE (PRODUCT_SPEC.md) — new paragraph in the architecture-doc "Keeping the doc up to date" section, after the re-carve bullet (live line 634)

**old_string** (exact anchor from the live tree — the re-carve bullet's tail plus the next heading):
```
walks this step, and gets re-proven [E-14].

**The architecture owes numbers, not just names.**
```

**new_string**:
```
walks this step, and gets re-proven [E-14].

**A deliberate redesign re-shapes the document, not only its pins.** When structure is deliberately redesigned — layers restacked, a surface's ownership moved, nodes merged or split — the architecture document is re-shaped to the new form and re-proven with the architecture lens in the same movement. Updating the pins alone is scoped to a boundary shift that leaves the document's shape standing; after a real redesign the old shape itself lies, so fresh pins on a stale shape are a defect. The re-carve routing [INV-37] carries such a redesign as its own row [E-14]; this states what that row owes the document. (Born of the tlvphotos second-finger redesign, 2026-07-11: a UI-layer rethink was ordered and the pack forced only a pins update, not a re-shaping.) [INV-113]

**The architecture owes numbers, not just names.**
```

## 257.3 — BUILD-PIPELINE HOME A (skills/build-pipeline/SKILL.md) — extend the re-carve paragraph in the architecture step (live lines 215-217)

**old_string**:
```
   Re-carving the whole node map IS legal: it arrives as a restructure placement's own queue row (SPEC
   INV-37), walks this step, and is re-proven like any structure change. A placement may SAY the shape no
   longer fits; only a landing changes the shape.
```

**new_string**:
```
   Re-carving the whole node map IS legal: it arrives as a restructure placement's own queue row (SPEC
   INV-37), walks this step, and is re-proven like any structure change. A placement may SAY the shape no
   longer fits; only a landing changes the shape. **When structure is deliberately redesigned — layers
   restacked, a surface's ownership moved, nodes merged or split — the architecture document is re-shaped
   to the new form and re-proven with the architecture lens in the same movement (SPEC INV-113). Updating
   the pins alone is scoped to a boundary shift that leaves the document's shape standing; after a real
   redesign the old shape itself lies, so fresh pins on a stale shape are a defect.**
```

## 257.4 — BUILD-PIPELINE HOME B (skills/build-pipeline/SKILL.md) — scope the refactor line's pins-only path (live line 95)

**old_string**:
```
  if the refactor moves node boundaries, ARCHITECTURE.md's pins update in the same change.
```

**new_string**:
```
  if the refactor moves node boundaries but leaves the document's shape standing, ARCHITECTURE.md's pins
  update in the same change — the pins-only path is scoped to a boundary shift that leaves the document's
  shape standing. A deliberate redesign (layers restacked, a surface's ownership moved, nodes merged or
  split) is not a pins-only change: the architecture document is re-shaped to the new form and re-proven
  with the architecture lens in the same movement (SPEC INV-113).
```

## 257.5 — FORMAL-INDEX ROW (PRODUCT_SPEC.md) — insert after the INV-109 index row (live line 1848), section column `From the spec to the tests` (matching INV-74/INV-75, the architecture-doc laws)

**old_string** (the INV-109 index row — the last INV row physically before INV-78; unique):
```
| INV-109 | a rewrite or restyle that removes substance (a section, an argument, a rationale, a worked example) lists every removal in its landing report, one line of judgment each — the fact kept and where, the owner killed it by name, or the rewriter proposes dropping and asks; a removal the rewriter cannot justify becomes a question before the report closes; never a silent cut of substance; scopes to substance and leaves line-level wording free; homes: communicator's pre-report walk + build-pipeline's docs-only door; born of a compressed README section restored the same session (2026-07-10) | Throwing a wish |
```

**new_string** (appends the INV-113 row after INV-109):
```
| INV-109 | a rewrite or restyle that removes substance (a section, an argument, a rationale, a worked example) lists every removal in its landing report, one line of judgment each — the fact kept and where, the owner killed it by name, or the rewriter proposes dropping and asks; a removal the rewriter cannot justify becomes a question before the report closes; never a silent cut of substance; scopes to substance and leaves line-level wording free; homes: communicator's pre-report walk + build-pipeline's docs-only door; born of a compressed README section restored the same session (2026-07-10) | Throwing a wish |
| INV-113 | a deliberate architecture redesign re-shapes and re-proves the document in the same movement: when structure is redesigned (layers restacked, a surface's ownership moved, nodes merged or split) ARCHITECTURE.md is re-shaped to the new form and re-proven with the architecture lens in that movement, not only re-pinned; the pins-only path is scoped to a boundary shift that leaves the document's shape standing, since after a real redesign the old shape itself lies and fresh pins on a stale shape are a defect; the re-carve routing [INV-37, E-14] carries the row, this states what the row owes the document; homes: the architecture-doc clause + build-pipeline's architecture step + the refactor line; born of the tlvphotos second-finger redesign (2026-07-11) | From the spec to the tests |
```

APPLIER NOTE: the index is grouped loosely by the section column, not strictly by INV number, and the
tail appends by landing. Insert this INV-113 row immediately after the INV-109 index row (its unique
anchor above). Row 258 (INV-114) inserts NEXT, after this INV-113 row — its draft quotes this row as
its post-257 anchor.

## 257.6 — MATRIX ROW (TEST_MATRIX.md) — in the `[node: build-pipeline]` block, after M-245 (live line 234, the block's last row)

**old_string** (tail of M-245, the anchor):
```
| M-245 | The push walk reads the remote gate's verdict and a red CI is the session's own immediate bug (INV-106, row 228): a push does not end at the push, and the push step reads the remote gate's own verdict (the CI run the push triggered, one `gh run` read, minutes, no human wait); a red verdict is the pushing session's own immediate bug, preempting by the bug lane (INV-2), fixed and re-pushed the same session before anything else, so the human never meets the red first in a GitHub email; a slow gate is watched to its verdict on the detached-work cadence (INV-35); the law lives in two homes: the spec's push clause and build-pipeline step 9; born of Alexander's word (2026-07-10 ~11:00: why does a mail tell him a deploy failed the session should have caught itself); never a push left standing on an unread verdict, never a red run the human meets first in his mailbox | INV-106 | string | `test_verdict_read_in_both_homes` + `test_red_is_immediate_bug_in_both_homes` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```

**new_string**:
```
| M-245 | The push walk reads the remote gate's verdict and a red CI is the session's own immediate bug (INV-106, row 228): a push does not end at the push, and the push step reads the remote gate's own verdict (the CI run the push triggered, one `gh run` read, minutes, no human wait); a red verdict is the pushing session's own immediate bug, preempting by the bug lane (INV-2), fixed and re-pushed the same session before anything else, so the human never meets the red first in a GitHub email; a slow gate is watched to its verdict on the detached-work cadence (INV-35); the law lives in two homes: the spec's push clause and build-pipeline step 9; born of Alexander's word (2026-07-10 ~11:00: why does a mail tell him a deploy failed the session should have caught itself); never a push left standing on an unread verdict, never a red run the human meets first in his mailbox | INV-106 | string | `test_verdict_read_in_both_homes` + `test_red_is_immediate_bug_in_both_homes` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
| M-252 | A deliberate architecture redesign re-shapes and re-proves ARCHITECTURE.md in the same movement (INV-113, row 257): when structure is deliberately redesigned — layers restacked, a surface's ownership moved, nodes merged or split — the architecture document is re-shaped to the new form and re-proven with the architecture lens in that movement, not only re-pinned; the pins-only path is scoped to a boundary shift that leaves the document's shape standing, since after a real redesign the old shape itself lies and fresh pins on a stale shape are a defect; the re-carve routing (INV-37, E-14) carries the row and this states what the row owes the document; the law lives in three homes — the spec's architecture-doc clause, build-pipeline's architecture step, and the refactor line; born of the tlvphotos second-finger redesign, a UI-layer rethink the pack forced only a pins update on (2026-07-11); never a real redesign shipped with only its pins updated, never a boundary shift dragged into a full re-shape it did not need | INV-113 | string | `test_redesign_owes_rework_in_both_homes` + `test_pins_only_scoped_to_boundary_shift_in_both_homes` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```

## 257.7 — APPLIER VERSION REMINDERS (live values move tonight — apply +0.0.1 over whatever each reads at apply time; never hardcode a target)

- `skills/build-pipeline/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.7 now; row 258 bumps it AGAIN after this — sequential).
- `VERSION` (pack) — +0.0.1 (reads 1.0.29 now; row 258 bumps it AGAIN after this — sequential).
- Base rulebook NOT touched: do **not** move the seven `` `live-spec-base` (v1.0.5) `` header pins for this row.
- No spec-internal version field exists to bump (the spec rides the pack VERSION).
- ARCHITECTURE.md is NOT edited by this row (the row's map names no ARCHITECTURE.md home; the law lives
  in the spec clause + the two build-pipeline spots). The row STATES the doc-rework obligation; it does
  not itself re-shape any document.
- Red-proof order per house rule: run `tests/test_architecture_redesign_owes_rework.py` against the
  pre-delta tree first (all three asserts must fail — the homes lack the needles), then apply the four
  edits, then green.

---

## Self-verify

- Both prose needles (`re-shaped to the new form and re-proven with the architecture lens in the same
  movement`, `a boundary shift that leaves the document's shape standing`) appear verbatim in the spec
  clause (257.2) AND both build-pipeline edits (257.3 re-carve paragraph, 257.4 refactor line).
- `[INV-113]` closes the spec clause; the `| INV-113 |` index row contains `redesign`.
- All prose anchors quoted from the live tree: spec re-carve bullet tail (line 634) + numbers heading
  (636); build-pipeline re-carve paragraph (215-217) and refactor line (95); index INV-109 row (1848);
  matrix M-245 (234).
- No banned contrast frame: the prohibitions are plain sentences (`fresh pins on a stale shape are a
  defect`); em-dashes wrap appositive enumerations (the redesign kinds), not denied neighbours.
- Dates only from the row's own record (2026-07-11) or the landing date (2026-07-12).
- INV-113 verified free (grep clean; ROADMAP row 242's landing note reserves it); M-252 verified free.

---

## Inter-draft note (257 → 258)

Row 258 lands after this one and shares two surfaces: (a) `skills/build-pipeline/SKILL.md` — 258 adds a
bullet after the INV-109 docs-only bullet (live line 98), which THIS row does not touch (257 edits line
95 and lines 215-217), so 258's anchor stays byte-identical post-257; only line numbers shift. (b) The
Formal index — 258 inserts its INV-114 row after the INV-113 row THIS draft adds; 258's index anchor
quotes this INV-113 row. Both rows bump `build-pipeline` `version:` and the pack `VERSION` by +0.0.1
each, sequentially (257 first, then 258).

---

APPLIED + CLOSED at landing 2026-07-12 (rows257-258-worker.md). All six drafted edits (257.2-257.6 +
version bumps) landed exactly as drafted, zero content deviation. One applier-side STOP: the draft's
257.7 note "ARCHITECTURE.md is NOT edited by this row" proved wrong — the traceability suite requires
every Formal-index anchor owned by exactly one ARCHITECTURE.md node, and INV-113 had none. The applier
caught this as unpredicted red and stopped per house rule; the orchestrator's call at continuation
added `INV-113` to ARCHITECTURE.md:43's build-pipeline Owns column (the row's own map already names
build-pipeline as owner) plus a `:215` pin. Suite green after: 418 passed. Prover short form
docs/prover/2026-07-12-row257-architecture-rework.md — 0 must-fix.

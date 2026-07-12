# PENDING DRAFT — row 258 (INV-114/M-253), drafted 2026-07-12 by an Opus drafter, NOT yet applied
# Next session: brief a sonnet applier from these blocks (the row-225/row-233 applier briefs are the shape);
# versions: read live values, +0.0.1 each; the index anchor note inside applies.
# LANDING ORDER: 257 → 258 → (260 STOPPED). This row lands SECOND. Every anchor below is quoted as it
# reads AFTER row 257's edits are in the tree; the two 257-adjacent anchors are flagged in §258.8.

Row 258 is draftable. Here is the delta.

---

# DELTA — Row 258 (INV-114 / M-253) — DRAFTABLE

Row 258 is a single behavioural law (size `small` in the queue): a restructure/migration merge gate that
judges the DELTA, in three parts, plus the honesty rider that a session sharpening a human's spoken bar
says the sharpened form back and marks it as interpretation. It needs a new invariant: the pack states no
law today for what a restructure merge's equivalence proof consists of or how prover findings route, so
each session invents its own bar — the exact gap that tonight produced a wrong bar (the orchestrator
over-sharpened «prover finds nothing both sides» into «any finding parks the merge» and parked a
strictly-improving merge on the OLD side's pre-existing debts, corrected live). The law BUILDS ON kin,
never restating them: INV-111 owns the word-token + punctuation multiset check (row 240), INV-39 owns the
landing gate (full suite green), and product-prover owns the pass — this row states how those compose into
a merge gate and how findings route. The say-the-bar-back rider is folded into the same law (same
incident, same moment): it homes in the spec clause and the prover mode, not a separate invariant.

Owner node = **product-prover** (it owns the pass whose findings the gate routes), so the matrix row sits
in the `[node: product-prover]` block. Row 258 does **not** touch `live-spec-base`, so the seven
working-skill `` `live-spec-base` (v1.0.5) `` header pins do **not** move.

The law lives in three homes (spec clause + product-prover mode + build-pipeline restructure door), so a
single **canonical block** is embedded verbatim so the needles match after whitespace-collapse:

> CANONICAL BLOCK (identical in the spec clause + the product-prover restructure-merge paragraph + the
> build-pipeline restructure-door bullet):
> `A restructure or migration merge gate judges the delta. It has three parts: load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111]; the full suite green on the merged tree [INV-39]; and a full prover pass on both sides whose blocking set is delta-scoped — an unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change. Pre-existing findings equal on both sides route to queue rows in the same landing and never block. And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation.`

## 258.1 — NEW TEST FILE (full content) — `tests/test_restructure_merge_gate.py`

```python
"""A restructure/migration merge gate judges the delta, in three parts — M-253 (SPEC INV-114, row 258).

The tlvphotos window's word, 2026-07-12 ~01:28 («надо переписать правила … пойми откуда пришло»): the pack
states no law for what a restructure merge's equivalence proof consists of or how prover findings route,
so each session invents its own bar. Tonight that produced a wrong one — the orchestrator over-sharpened
his spoken «prover finds nothing both sides» into «any finding parks the merge» and parked a
strictly-improving merge on the OLD side's pre-existing clarity debts, which he corrected live: the gate
judges the DELTA. The law in three parts: (1) load-bearing token identity old-versus-new modulo the
per-chunk named deltas plus the punctuation-multiset check (INV-111); (2) the full suite green on the
merged tree (INV-39); (3) a full prover pass on both sides whose blocking set is delta-scoped — an
unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change.
Pre-existing findings equal on both sides route to queue rows in the same landing and never block. And a
session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as
its own interpretation. String rows on the law's three homes plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestRestructureMergeGateLaw(unittest.TestCase):
    HOMES = (
        "PRODUCT_SPEC.md",
        "skills/product-prover/SKILL.md",
        "skills/build-pipeline/SKILL.md",
    )

    def test_merge_gate_judges_the_delta_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("merge gate judges the delta", body, home)
            self.assertIn("blocking set is delta-scoped", body, home)

    def test_preexisting_findings_route_not_block_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "route to queue rows in the same landing and never block", body, home
            )

    def test_say_the_bar_back_duty_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "says the sharpened form back and marks it as its own interpretation",
                body,
                home,
            )

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-114]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-114 |"):
                    self.assertIn("delta", line)
                    return
        self.fail("INV-114 index row missing")


if __name__ == "__main__":
    unittest.main()
```

Needles (verbatim, whitespace-collapsed) in ALL THREE homes: `merge gate judges the delta`, `blocking set
is delta-scoped`, `route to queue rows in the same landing and never block`, `says the sharpened form back
and marks it as its own interpretation`. Spec-only: `[INV-114]`, index row `| INV-114 |` contains `delta`.

## 258.2 — SPEC CLAUSE (PRODUCT_SPEC.md) — new paragraph after the INV-111 layout-vehicle clause (live line 1196, UNCHANGED by row 257)

**old_string** (the INV-111 clause tail plus the next heading — unique, not touched by 257):
```
A host never improvises a layout pass; it cites this vehicle. [INV-111]

**Non-goals.** No script automates the walk;
```

**new_string**:
```
A host never improvises a layout pass; it cites this vehicle. [INV-111]

**A restructure or migration merge gate judges the delta.** When a restructure or a migration is gated for merging back into main, the gate judges the delta. It has three parts: load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111]; the full suite green on the merged tree [INV-39]; and a full prover pass on both sides whose blocking set is delta-scoped — an unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change. Pre-existing findings equal on both sides route to queue rows in the same landing and never block. And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation. (Born of a strictly-improving restructure merge parked on the old side's pre-existing clarity debts because a spoken «prover finds nothing both sides» was over-sharpened into «any finding parks the merge», corrected live 2026-07-12.) [INV-114]

**Non-goals.** No script automates the walk;
```

## 258.3 — PRODUCT-PROVER HOME (skills/product-prover/SKILL.md) — new paragraph after the "All three modes…" paragraph, before "## Phase 0 — Triage" (live lines 167-169)

**old_string**:
```
All three modes keep the whole document in view — a cross-section hole is only findable when both sides of the seam are present and named the same at prove-time. CROSS-LINK narrows the FINDINGS to the new surface's seams, and FEATURE-FIT to the feature's fit; the reading still covers the whole document.

## Phase 0 — Triage
```

**new_string**:
```
All three modes keep the whole document in view — a cross-section hole is only findable when both sides of the seam are present and named the same at prove-time. CROSS-LINK narrows the FINDINGS to the new surface's seams, and FEATURE-FIT to the feature's fit; the reading still covers the whole document.

**The restructure-merge gate: judge the delta.** When a restructure or a migration is gated for merging back into main, a restructure or migration merge gate judges the delta. It has three parts: load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check (SPEC INV-111); the full suite green on the merged tree (SPEC INV-39); and a full prover pass on both sides whose blocking set is delta-scoped — an unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change. Pre-existing findings equal on both sides route to queue rows in the same landing and never block; the merge is not held on debts it did not create. And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation, so a bar the human never spoke is never applied as his (SPEC INV-114). The pass reads both the old tree and the merged tree; a finding present on both is pre-existing, a finding new to the merged side is delta-scoped and blocks.

## Phase 0 — Triage
```

## 258.4 — BUILD-PIPELINE HOME (skills/build-pipeline/SKILL.md) — new bullet after the INV-109 restyle bullet (live ~line 98, UNCHANGED by row 257 — see §258.8)

**old_string** (the INV-109 bullet tail plus the skip-entirely bullet — quoted as it reads POST-257; row 257 does not touch these lines):
```
The accounting rides the landing report the communicator builds; the docs-only door above and the restyle loop both carry it. (Born of a compressed README section restored the same session, 2026-07-10.)
- **Skip entirely** only under the single boundary above (pure research, fact-gathering, a one-file
```

**new_string**:
```
The accounting rides the landing report the communicator builds; the docs-only door above and the restyle loop both carry it. (Born of a compressed README section restored the same session, 2026-07-10.)
- **A restructure or migration merged back to main is gated on the delta (SPEC INV-114):** A restructure or migration merge gate judges the delta. It has three parts: load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check (SPEC INV-111); the full suite green on the merged tree (SPEC INV-39); and a full prover pass on both sides whose blocking set is delta-scoped — an unmatched token, a red suite, a new-side finding absent on the old side, or an unnamed meaning change. Pre-existing findings equal on both sides route to queue rows in the same landing and never block. And a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation. (Born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live 2026-07-12.)
- **Skip entirely** only under the single boundary above (pure research, fact-gathering, a one-file
```

## 258.5 — FORMAL-INDEX ROW (PRODUCT_SPEC.md) — insert after the INV-113 index row THAT ROW 257 ADDED, section column `The machines that hold the bounds` (matching INV-47/INV-98/INV-108, the gate/lock laws)

**old_string** (the INV-113 row row 257 inserts — quoted from row 257's draft §257.5; this is the POST-257 anchor):
```
| INV-113 | a deliberate architecture redesign re-shapes and re-proves the document in the same movement: when structure is redesigned (layers restacked, a surface's ownership moved, nodes merged or split) ARCHITECTURE.md is re-shaped to the new form and re-proven with the architecture lens in that movement, not only re-pinned; the pins-only path is scoped to a boundary shift that leaves the document's shape standing, since after a real redesign the old shape itself lies and fresh pins on a stale shape are a defect; the re-carve routing [INV-37, E-14] carries the row, this states what the row owes the document; homes: the architecture-doc clause + build-pipeline's architecture step + the refactor line; born of the tlvphotos second-finger redesign (2026-07-11) | From the spec to the tests |
```

**new_string** (appends the INV-114 row after INV-113):
```
| INV-113 | a deliberate architecture redesign re-shapes and re-proves the document in the same movement: when structure is redesigned (layers restacked, a surface's ownership moved, nodes merged or split) ARCHITECTURE.md is re-shaped to the new form and re-proven with the architecture lens in that movement, not only re-pinned; the pins-only path is scoped to a boundary shift that leaves the document's shape standing, since after a real redesign the old shape itself lies and fresh pins on a stale shape are a defect; the re-carve routing [INV-37, E-14] carries the row, this states what the row owes the document; homes: the architecture-doc clause + build-pipeline's architecture step + the refactor line; born of the tlvphotos second-finger redesign (2026-07-11) | From the spec to the tests |
| INV-114 | a restructure or migration merge gate judges the delta: three parts — load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check [INV-111], the full suite green on the merged tree [INV-39], and a full prover pass on both sides whose blocking set is delta-scoped (an unmatched token, a red suite, a new-side finding absent on the old side, an unnamed meaning change); pre-existing findings equal on both sides route to queue rows in the same landing and never block; and a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation; homes: the spec clause + product-prover's restructure-merge gate + build-pipeline's restructure door; born of a strictly-improving merge parked on the old side's pre-existing debts, corrected live (2026-07-12) | The machines that hold the bounds |
```

APPLIER NOTE (fallback): if row 257 is NOT yet applied at 258's landing (order was declared 257 → 258, so
this should not happen), anchor the INV-114 row on the INV-109 index row instead and place it after
INV-109. The intended tree has INV-113 already present.

## 258.6 — MATRIX ROW (TEST_MATRIX.md) — in the `[node: product-prover]` block, after M-190 (live line 173, the block's last row; UNCHANGED by row 257)

**old_string** (tail of M-190, the anchor):
```
| M-190 | The re-prove exemption is lens-aware: a prover record opens naming the prover version that ran, and adoption's skip-the-re-prove exemption holds only when that version matches the installed prover — a prover that grew a lens re-arms the full pass; never a stale green surviving a lens the spec was never held to (the 2026-07-09 composition-slip mechanism, pinned) | M-6 | string | `test_prove_exemption_is_lens_aware` (red proven against HEAD — no version condition there) | BUILT |
```

**new_string**:
```
| M-190 | The re-prove exemption is lens-aware: a prover record opens naming the prover version that ran, and adoption's skip-the-re-prove exemption holds only when that version matches the installed prover — a prover that grew a lens re-arms the full pass; never a stale green surviving a lens the spec was never held to (the 2026-07-09 composition-slip mechanism, pinned) | M-6 | string | `test_prove_exemption_is_lens_aware` (red proven against HEAD — no version condition there) | BUILT |
| M-253 | A restructure/migration merge gate judges the delta (INV-114, row 258): three parts — load-bearing token identity old-versus-new modulo the per-chunk named deltas plus the punctuation-multiset check (INV-111), the full suite green on the merged tree (INV-39), and a full prover pass on both sides whose blocking set is delta-scoped (an unmatched token, a red suite, a new-side finding absent on the old side, an unnamed meaning change); pre-existing findings equal on both sides route to queue rows in the same landing and never block; and a session that sharpens a human's spoken bar beyond his words says the sharpened form back and marks it as its own interpretation; the law lives in three homes — the spec clause, product-prover's restructure-merge gate, and build-pipeline's restructure door; born of the tlvphotos correction (2026-07-12 ~01:28), a strictly-improving merge parked on the old side's pre-existing clarity debts because a spoken «prover finds nothing both sides» was over-sharpened into «any finding parks the merge»; never a merge held on debts it did not create, never a sharpened bar applied as the human's own | INV-114 | string | `test_merge_gate_judges_the_delta_in_all_homes` + `test_preexisting_findings_route_not_block_in_all_homes` + `test_say_the_bar_back_duty_in_all_homes` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```

## 258.7 — APPLIER VERSION REMINDERS (live values move tonight — apply +0.0.1 over whatever each reads at apply time; never hardcode a target)

- `skills/product-prover/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.1 now; row 257 does not touch it).
- `skills/build-pipeline/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.7 now, but row 257 lands FIRST and bumps it to 1.0.8, so this row reads 1.0.8 and lands 1.0.9 — read live, do not hardcode).
- `VERSION` (pack) — +0.0.1 (reads 1.0.29 now, but row 257 lands first and bumps it, so read the live value at apply time and +0.0.1).
- Base rulebook NOT touched: do **not** move the seven `` `live-spec-base` (v1.0.5) `` header pins for this row.
- No spec-internal version field exists to bump (the spec rides the pack VERSION).
- Red-proof order per house rule: run `tests/test_restructure_merge_gate.py` against the tree BEFORE this
  row's edits (all four asserts fail — the homes lack the needles), then apply the five edits, then green.

## 258.8 — POST-257 ANCHOR FLAGS (read before applying)

- **§258.4 (build-pipeline restructure door):** the anchor sits at the INV-109 restyle bullet's tail
  (live line 98) and the skip-entirely bullet (line 99). Row 257 edits the refactor line ABOVE this (line
  95) and the re-carve paragraph BELOW this (lines 215-217); it does NOT touch lines 98-99, so this
  anchor is byte-identical whether 257 landed or not. Only line numbers shift down by 257's inserted
  lines. Safe.
- **§258.5 (Formal index):** anchors on the INV-113 row row 257 adds. This is the one genuine cross-draft
  dependency: 258's index anchor does not exist until 257 lands. The fallback note in §258.5 covers the
  out-of-order case.
- **§258.2 (spec INV-111 clause) and §258.3 (prover modes) and §258.6 (matrix M-190):** all at lines row
  257 does not touch; anchors byte-identical pre- or post-257.

---

## Self-verify

- All four needles (`merge gate judges the delta`, `blocking set is delta-scoped`, `route to queue rows in
  the same landing and never block`, `says the sharpened form back and marks it as its own interpretation`)
  appear verbatim in all three drafted home texts (258.2 spec, 258.3 prover, 258.4 build-pipeline).
- `[INV-114]` closes the spec clause; the `| INV-114 |` index row contains `delta`.
- Kin cited, never restated: INV-111 (token+punctuation multiset), INV-39 (landing gate). This row states
  the composition and the routing; it does not re-author those laws.
- No banned contrast frame: the three-part list uses em-dashes for the blocking enumeration, not a denied
  neighbour; every prohibition is a plain clause.
- Dates only from the row's own record (2026-07-12 ~01:28) or the landing date (2026-07-12).
- INV-114 verified free; M-253 verified free.
- STOP-rule check: the say-the-bar-back rider was weighed as a possible second story. It is folded, not
  split, because it is the same incident's lesson about how the SAME gate's bar is set honestly — one
  subject, one law, one code. (Contrast row 260, which bundles two genuinely independent stories and is
  STOPPED — see its file.)

---

APPLIED + CLOSED at landing 2026-07-12 (rows257-258-worker.md). All five drafted edits (258.2-258.6 +
version bumps) landed exactly as drafted, zero content deviation. Same-shape gap as row 257: the draft
named product-prover as INV-114's owner node but no block edited ARCHITECTURE.md. Unlike row 257, the
owner was unambiguous from the draft's own text, so per the orchestrator's instruction the fix (INV-114
added to ARCHITECTURE.md:42's product-prover Owns column, plus a `:168` pin) was applied proactively
before the first full-suite run — no unpredicted red this lane. Suite green: 422 passed. Prover short
form docs/prover/2026-07-12-row258-restructure-merge-gate.md — 0 must-fix.

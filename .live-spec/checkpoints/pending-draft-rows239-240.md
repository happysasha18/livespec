RENUMBERED 2026-07-12 by the orchestrator's call: reservation of INV-109/M-247 lifted, codes consume in landing order; row 239 = INV-110/M-248, row 240 = INV-111/M-249.

# PENDING DRAFTS — rows 239 (INV-110/M-248) and 240 (INV-111/M-249), drafted 2026-07-12, NOT yet applied
# Landing order is law: 239 before 240 (240's anchors sit on 239's text).
# Next session: brief a sonnet applier per delta (the row-225 applier brief is the shape);
# versions: read live values, +0.0.1 per landing; delegation line duty per INV-103 applies.

I have everything needed. Both rows are draftable (neither hits the STOP rule: each is a single coherent rule, no new surface, no bundle, and both trace to an audited APPROVE, not a pending human word). Both need a new invariant. Here are the two deltas.

---

# ROW 239 → INV-110, M-248 — the catch-up routing's version-delta discriminator

**Homes:** the spec's F-catchup *Skill behaviour* paragraph (PRODUCT_SPEC.md) + MIGRATION.md *When to run this*. Owner node: `attach`. Verified free: `INV-110`, `M-248` absent from the whole tree.

## 239.1 — NEW test file `tests/test_catchup_discriminator.py` (full content)

```python
"""The catch-up routing carries its version-delta discriminator — M-248 (SPEC INV-110, row 239).

The track-coach audit (2026-07-10 ~14:19) found the trigger wordings would justify the heavy
catch-up walk where a host queue row is the truth: a pure docs-layout pass with no pack-version
delta fell into the gap. The routing states the discriminator in one sentence — the walk fires
only when the host's recorded package version is behind the current package VERSION — carried in
both homes: the spec's skill-behaviour paragraph and the guide's "When to run this".
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestCatchupDiscriminator(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "MIGRATION.md")

    def test_discriminator_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "fires only when the host's recorded package version is behind the current package VERSION",
                body,
                home,
            )
            self.assertIn(
                "no version delta is the host's own queue row through its pipeline",
                body,
                home,
            )

    def test_trigger_wordings_read_as_examples(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("The trigger wordings are examples under this test", body, home)
            self.assertIn("A wording never decides the routing", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-110]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-110 |"):
                    self.assertIn("version", line)
                    return
        self.fail("INV-110 index row missing")


if __name__ == "__main__":
    unittest.main()
```

## 239.2 — spec clause (PRODUCT_SPEC.md, F-catchup *Skill behaviour*, line 1192)

Append the discriminator to the paragraph's tail.

OLD:
```
which is the host's own queue row and pipeline.
```
NEW:
```
which is the host's own queue row and pipeline. The catch-up walk fires only when the host's recorded package version is behind the current package VERSION. A docs restructure that carries no version delta is the host's own queue row through its pipeline, whatever wording the ask used. The trigger wordings are examples under this test. A wording never decides the routing; the version delta decides. [INV-110]
```
(Anchor is unique — the string `which is the host's own queue row and pipeline.` occurs once, at the close of the F-catchup Skill-behaviour paragraph.)

## 239.3 — MIGRATION.md home (*When to run this*, line 11)

OLD:
```
This walk fires only to move an adopted host's own live-spec documents and records onto a newer package version.
```
NEW:
```
This walk fires only to move an adopted host's own live-spec documents and records onto a newer package version. The catch-up walk fires only when the host's recorded package version is behind the current package VERSION. A docs restructure that carries no version delta is the host's own queue row through its pipeline, whatever wording the ask used. The trigger wordings are examples under this test. A wording never decides the routing; the version delta decides. (INV-110)
```

## 239.4 — formal-index row (PRODUCT_SPEC.md, Catch-up section, after INV-92 at line 1753)

Anchor on the INV-92 index row; append INV-110 immediately after it (section column `Catch-up`, matching INV-89…INV-92).

OLD (end of the INV-92 row):
```
the attic readable without any restore | Catch-up |
```
NEW:
```
the attic readable without any restore | Catch-up |
| INV-110 | the catch-up routing's discriminator: the walk fires only when the host's recorded package version is behind the current package VERSION; a docs restructure carrying no version delta is the host's own queue row through its pipeline, whatever wording the ask used; the trigger wordings (re-layout the documentation, catch up to the current pack) are examples under the version test, and a wording never decides the routing; homes: the F-catchup skill-behaviour paragraph + MIGRATION's When-to-run section; born of the track-coach audit (2026-07-10) | Catch-up |
```

## 239.5 — matrix row M-248 (TEST_MATRIX.md, catch-up block, after M-221 at line 338)

Anchor on the M-221 row (INV-92's owner block); append M-248.

OLD (end of the M-221 row):
```
(red proven against the pre-rewrite MIGRATION.md, 2026-07-10) | BUILT |
```
NEW:
```
(red proven against the pre-rewrite MIGRATION.md, 2026-07-10) | BUILT |
| M-248 | The catch-up routing carries its version-delta discriminator (INV-110, row 239): the walk fires only when the host's recorded package version is behind the current package VERSION; a docs restructure carrying no version delta is the host's own queue row through its pipeline, whatever wording the ask used; the trigger wordings are examples under the version test and a wording never decides the routing; the law lives in two homes — the spec's F-catchup skill-behaviour paragraph and MIGRATION's When-to-run section; born of the track-coach audit (2026-07-10 ~14:19); never the heavy catch-up walk fired on a same-version docs-layout ask, never a trigger wording routing the ask on its own | INV-110 | string | `test_discriminator_in_both_homes` + `test_trigger_wordings_read_as_examples` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```
Note: the M-221 tail `(red proven against the pre-rewrite MIGRATION.md, 2026-07-10) | BUILT |` also appears on M-218/M-219; the applier should target the M-221 line specifically (match the fuller line `| M-221 | The walk's self-test:` … then append). If a unique tail is needed, anchor on `never a walk with no named restore point | INV-92 | string |` … which is M-221-only.

## 239.6 — ARCHITECTURE.md owned-anchors (`attach` node, line 46)

OLD:
```
INV-89, INV-90, INV-91, INV-92, E-21, E-25, INV-85, INV-86 |
```
NEW:
```
INV-89, INV-90, INV-91, INV-92, INV-110, E-21, E-25, INV-85, INV-86 |
```

---

# ROW 240 → INV-111, M-249 — the sanctioned light vehicle for an owner-scoped docs-layout pass

**Homes:** the spec's F-catchup vehicle clause (new paragraph, PRODUCT_SPEC.md) + build-pipeline's docs-only/restructure door (skills/build-pipeline/SKILL.md). Owner node: `attach` (host-side document movement, sibling of catch-up; the build-pipeline door is the vehicle it rides). Verified free: `INV-111`, `M-249` absent.

**Landing dependency:** 240 lands AFTER 239. Three of its anchors sit on text 239 wrote (the INV-110 index row, the M-248 matrix row, and `INV-110` already in the attach owns-list). Apply 239 first.

## 240.1 — NEW test file `tests/test_docs_layout_vehicle.py` (full content)

```python
"""The light vehicle for an owner-scoped docs-layout pass is sanctioned — M-249 (SPEC INV-111, row 240).

The track-coach audit (2026-07-10 ~14:23) found track-coach s63, lacking a named vehicle, correctly
improvised one for a pure docs-layout pass: a checkpoint carrying the owner's locked decisions, work
on a clean pushed base so restore is one command, and a multiset proof that content survived. The
pack now names that shape so hosts neither skip discipline nor over-apply the catch-up machinery.
Two homes: the spec's F-catchup vehicle clause and build-pipeline's docs-only/restructure door.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestDocsLayoutVehicle(unittest.TestCase):
    HOMES = ("PRODUCT_SPEC.md", "skills/build-pipeline/SKILL.md")

    def test_vehicle_in_both_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn(
                "A same-version docs-layout pass rides one sanctioned light vehicle",
                body,
                home,
            )
            self.assertIn(
                "a word-token multiset check AND a punctuation multiset check",
                body,
                home,
            )

    def test_vehicle_owes_the_full_shape(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("The owner's decisions are locked in a checkpoint before any file moves", spec)
        self.assertIn("builds on a clean pushed base", spec)
        self.assertIn("lands one journal chapter", spec)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-111]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-111 |"):
                    self.assertIn("vehicle", line)
                    return
        self.fail("INV-111 index row missing")


if __name__ == "__main__":
    unittest.main()
```

## 240.2 — spec clause (PRODUCT_SPEC.md, insert new paragraph before *Non-goals* at line 1194)

OLD:
```
**Non-goals.** No script automates the walk; the session executes it as a procedure.
```
NEW:
```
**A same-version docs-layout pass rides one sanctioned light vehicle.** The routing sends an adopted host's ask to its own queue when the ask restructures the host's own documents with no package-version delta [INV-110]. That pass runs one named shape. The owner's decisions are locked in a checkpoint before any file moves [INV-107]. The work builds on a clean pushed base, so one command restores the pre-pass tree. The pass proves content survived by a word-token multiset check AND a punctuation multiset check, since word-token identity alone passes a reflow that dropped or moved punctuation. The pass lands one journal chapter naming what moved and why. A host never improvises a layout pass; it cites this vehicle. [INV-111]

**Non-goals.** No script automates the walk; the session executes it as a procedure.
```

## 240.3 — build-pipeline home (skills/build-pipeline/SKILL.md, docs-only/restructure door, ~line 58)

OLD:
```
the re-carve happens only through the architecture step and its re-prove (SPEC INV-37).
```
NEW:
```
the re-carve happens only through the architecture step and its re-prove (SPEC INV-37). A same-version docs-layout pass rides one sanctioned light vehicle: the pass builds on a clean pushed base, locks the owner's decisions in a checkpoint first, and proves content survived by a word-token multiset check AND a punctuation multiset check (SPEC INV-111).
```

## 240.4 — formal-index row (PRODUCT_SPEC.md, Catch-up section, after the INV-110 row 239.4 added)

Anchor on the tail of the INV-110 index row (written by 239); append INV-111.

OLD:
```
born of the track-coach audit (2026-07-10) | Catch-up |
```
NEW:
```
born of the track-coach audit (2026-07-10) | Catch-up |
| INV-111 | a same-version docs-layout pass rides one sanctioned light vehicle: a host restructuring its own documents with no package-version delta [INV-110] runs one named shape; the owner's decisions are locked in a checkpoint before any file moves [INV-107], the work builds on a clean pushed base with a one-command restore, content is proven by a word-token multiset check AND a punctuation multiset check (word-token identity alone passes a reflow that moved punctuation), and one journal chapter lands; a host never improvises a layout pass and cites this vehicle; born of the track-coach s63 audited pass (2026-07-10) | Catch-up |
```
(The string `born of the track-coach audit (2026-07-10) | Catch-up |` is unique to the INV-110 row 239 wrote — no collision with pre-existing rows.)

## 240.5 — matrix row M-249 (TEST_MATRIX.md, catch-up block, after the M-248 row 239.5 added)

Anchor on the tail of the M-248 row (written by 239); append M-249.

OLD:
```
(red proven against the pre-delta tree, 2026-07-12) | BUILT |
```
NEW:
```
(red proven against the pre-delta tree, 2026-07-12) | BUILT |
| M-249 | The light vehicle for an owner-scoped docs-layout pass is sanctioned (INV-111, row 240): a host restructuring its own live-spec documents with no package-version delta (INV-110) runs one named shape — the owner's decisions locked in a checkpoint before any file moves (INV-107), the work built on a clean pushed base with a one-command restore, content proven by a word-token multiset check AND a punctuation multiset check, one journal chapter landed; the law lives in two homes — the spec's F-catchup vehicle clause and build-pipeline's docs-only/restructure door; born of the track-coach s63 improvised pass, audited APPROVE (2026-07-10 ~14:23); never a host layout pass improvised without the vehicle, never content proven by a word-token check alone | INV-111 | string | `test_vehicle_in_both_homes` + `test_vehicle_owes_the_full_shape` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```
WARNING for the applier: the phrase `(red proven against the pre-delta tree, 2026-07-12) | BUILT |` will also be the tail of M-248 once 239 lands — target the M-248 line specifically. Unique anchor: match `never a trigger wording routing the ask on its own | INV-110 | string |` … through to that row's end, then append M-249.

## 240.6 — ARCHITECTURE.md owned-anchors (`attach` node, line 46 — post-239 state)

OLD (after 239 applied):
```
INV-89, INV-90, INV-91, INV-92, INV-110, E-21, E-25, INV-85, INV-86 |
```
NEW:
```
INV-89, INV-90, INV-91, INV-92, INV-110, INV-111, E-21, E-25, INV-85, INV-86 |
```

---

# Applier reminders (version + order + gates)

1. **Landing order is law: 239 before 240.** 240's index/matrix/architecture anchors sit on text 239 writes.
2. **Neither delta touches the base rulebook** (`skills/live-spec-base/SKILL.md`). The SEVEN working-skill header pins `` `live-spec-base` (vX.Y.Z) `` lockstep does NOT fire for either row. Live repo pin value is currently `v1.0.4` (it moves tonight) — leave it untouched. 240 edits `skills/build-pipeline/SKILL.md` *body*; if the pack bumps that skill's own version header that is build-pipeline's own concern, unrelated to the base-pin lockstep.
3. **VERSION bump:** live `VERSION` is `1.0.23` (moves tonight). Each row lands as its own patch step, `+0.0.1` per landing — do not hardcode; read the live value at apply time and increment.
4. **Red-first:** run each new test against the pre-delta tree and confirm red BEFORE applying the home edits, to honour the matrix cells' "red proven against the pre-delta tree, 2026-07-12".
5. **Skip-set + traceability:** add neither test to the pinned skip-set; run `test_traceability.py` after apply — both new invariants are owned by the `attach` node (239.6 / 240.6) with matrix rows, so coverage should close.
6. **Delegation accounting (INV-103 / M-241):** both rows land on 2026-07-12, so each ROADMAP status cell must carry its delegation-accounting line at landing (the drafting/apply split rode an Opus drafter + applier); the queue-scan check goes red on a forward-landed row without it.

# Self-verify

- Every test needle appears verbatim (whitespace-collapsed) in its drafted home text: 239 needles in both PRODUCT_SPEC.md (239.2) and MIGRATION.md (239.3); 240 both-homes needles in PRODUCT_SPEC.md (240.2) and build-pipeline (240.3); 240 spec-only needles all in 240.2; `[INV-110]`/`[INV-111]` and the index-row keyword (`version`/`vehicle`) present in 239.4/240.4.
- Anchors quoted from the LIVE tree (239 and the 240 edits that don't depend on 239); the three 240 anchors on 239-written text are flagged with the order dependency.
- No banned contrast frame in any drafted prose: prohibitions are plain `never` sentences ("A wording never decides the routing", "A host never improvises a layout pass"); matrix "never …, never …" is the standard regression-fence list, not a scissors.
- Dates only from the rows' own record (2026-07-10 audit timestamps ~14:19 / ~14:23) or 2026-07-12 (the red-proof date).
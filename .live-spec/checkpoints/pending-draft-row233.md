# PENDING DRAFT — row 233 (INV-110/M-248), drafted 2026-07-12 by an Opus drafter, NOT yet applied
# Next session: brief a sonnet applier from these blocks (the row-225 applier brief is the shape);
# versions: read live values, +0.0.1 each; the index anchor note inside applies.

I have everything needed. Row 233 is draftable; row 234 hits the STOP rule. Here are the two deltas.

---

# DELTA — Row 233 (INV-110 / M-248) — DRAFTABLE

Row 233 is a single behavioural rule (size `small` in the queue), needs a genuinely new invariant (no existing anchor covers "list every removal of substance in the landing report" — INV-34 is register, INV-93 is time-estimates, INV-94 is self-certification), and lands before 234. Owner node = **communicator** (it owns the report-walk family INV-34/93/94/95 per ARCHITECTURE.md:44), so its matrix row sits in the `[node: communicator]` block. Row 233 does **not** touch `live-spec-base`, so the seven working-skill `` `live-spec-base` (v1.0.3) `` header pins do **not** move.

A single **canonical block** (below) is embedded verbatim in all three homes so the string needles match after whitespace-collapse:

> CANONICAL BLOCK (identical in spec + communicator + build-pipeline):
> `A rewrite or restyle that removes substance — a section, an argument, a rationale, a worked example — lists every removal in its landing report, one line of judgment each: the fact was kept and where, the owner killed it by name, or the rewriter proposes dropping and asks. A removal the rewriter cannot justify becomes a question before the report closes. Never a silent cut of substance. The rule scopes to substance and leaves line-level wording free, so a tightened sentence or a reordered clause needs no accounting.`

## 233.1 — NEW TEST FILE (full content) — `tests/test_no_silent_drop.py`

```python
"""A rewrite that removes substance names every removal in its landing report — M-248 (SPEC INV-110, row 233).

His 2026-07-10 ~12:10 word, after a night docs pass compressed the README's account of why live-spec
stands beside BMAD, Kiro, and spec-kit to one pointer line: a sound thought is never silently dropped —
a removal of substance is at least questioned, of himself or of the owner, in case it is needed later,
with no per-line paralysis. A restyle that removes a section, an argument, a rationale, or a worked
example lists every removal in its landing report with one line of judgment each; a removal the rewriter
cannot justify becomes a question. The rule scopes to substance and leaves line-level wording free.
String rows on the law's three homes plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestNoSilentDropLaw(unittest.TestCase):
    HOMES = (
        "PRODUCT_SPEC.md",
        "skills/communicator/SKILL.md",
        "skills/build-pipeline/SKILL.md",
    )

    def test_removal_rule_in_all_three_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("lists every removal in its landing report", body, home)
            self.assertIn("one line of judgment each", body, home)
            self.assertIn(
                "A removal the rewriter cannot justify becomes a question", body, home
            )
            self.assertIn("Never a silent cut of substance", body, home)

    def test_scope_carveout_in_all_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("line-level wording", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-110]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-110 |"):
                    self.assertIn("removal", line)
                    return
        self.fail("INV-110 index row missing")


if __name__ == "__main__":
    unittest.main()
```

Needles (all verbatim, whitespace-collapsed) in every home: `lists every removal in its landing report`, `one line of judgment each`, `A removal the rewriter cannot justify becomes a question`, `Never a silent cut of substance`, `line-level wording`. Spec-only: `[INV-110]`, index row `| INV-110 |` contains `removal`.

## 233.2 — SPEC CLAUSE (PRODUCT_SPEC.md) — insert new paragraph after the INV-93 clause (line 203)

**old_string** (exact anchor from live tree, boundary between the INV-93 and INV-95 paragraphs):
```
ran loose on it.) [INV-93]

**One spoken leave-word winds the session down to a shutdown-safe stop.**
```

**new_string**:
```
ran loose on it.) [INV-93]

**A rewrite that removes substance accounts for it in the landing report.** A restyle or a restructure drops content as it tightens, and some of what it drops carries weight. A rewrite or restyle that removes substance — a section, an argument, a rationale, a worked example — lists every removal in its landing report, one line of judgment each: the fact was kept and where, the owner killed it by name, or the rewriter proposes dropping and asks. A removal the rewriter cannot justify becomes a question before the report closes. Never a silent cut of substance. The rule scopes to substance and leaves line-level wording free, so a tightened sentence or a reordered clause needs no accounting. The law's homes are the communicator's pre-report walk and build-pipeline's docs-only door. (Born of the night docs pass that compressed the README's account of why live-spec stands beside BMAD, Kiro, and spec-kit to a single pointer line; the section was restored the same session on the owner's word, 2026-07-10.) [INV-110]

**One spoken leave-word winds the session down to a shutdown-safe stop.**
```

## 233.3 — FORMAL-INDEX ROW (PRODUCT_SPEC.md) — anchor on the last INV index row (INV-103, line 1832), section column `Throwing a wish` (matching INV-34/81/83/93/94)

**old_string**:
```
| INV-103 | every landed queue row carries its delegation accounting in the landed row's status cell — what went to a worker with a rough saving, or a stood-down line naming why the senior kept the work; a suite check reads the queue (ROADMAP.md) and a landed row without the line goes red; binds forward from its landing date (a row landed 2026-07-12 or later carries the line, earlier rows stay stock); the duty binds the orchestrator seat regardless of model; born the night prose alone did not hold the routing rule (2026-07-12) | Who decides what |
```

**new_string** (appends the INV-110 row after INV-103):
```
| INV-103 | every landed queue row carries its delegation accounting in the landed row's status cell — what went to a worker with a rough saving, or a stood-down line naming why the senior kept the work; a suite check reads the queue (ROADMAP.md) and a landed row without the line goes red; binds forward from its landing date (a row landed 2026-07-12 or later carries the line, earlier rows stay stock); the duty binds the orchestrator seat regardless of model; born the night prose alone did not hold the routing rule (2026-07-12) | Who decides what |
| INV-110 | a rewrite or restyle that removes substance (a section, an argument, a rationale, a worked example) lists every removal in its landing report, one line of judgment each — the fact kept and where, the owner killed it by name, or the rewriter proposes dropping and asks; a removal the rewriter cannot justify becomes a question before the report closes; never a silent cut of substance; scopes to substance and leaves line-level wording free; homes: communicator's pre-report walk + build-pipeline's docs-only door; born of a compressed README section restored the same session (2026-07-10) | Throwing a wish |
```

APPLIER NOTE: the index tail grows tonight (INV-107/108, INV-109 reserved). If any INV-1xx index row already sits below INV-103 at apply time, move this INV-110 row to sit after the last INV-numbered index row instead — it stays the last INV row, matching the tail's append-by-landing habit.

## 233.4 — COMMUNICATOR HOME (skills/communicator/SKILL.md) — new step 5 in the pre-report walk (after step 4, before the "A pattern lint catches…" paragraph)

**old_string**:
```
becomes a pattern the same day (the set grows by one per caught leak).

A pattern lint catches known coinages, known calques, and named term classes
```

**new_string**:
```
becomes a pattern the same day (the set grows by one per caught leak).
5. **Account for every removal of substance (SPEC INV-110).** When the movement being reported rewrote or restyled existing text, the removal accounting runs before the report closes. A rewrite or restyle that removes substance — a section, an argument, a rationale, a worked example — lists every removal in its landing report, one line of judgment each: the fact was kept and where, the owner killed it by name, or the rewriter proposes dropping and asks. A removal the rewriter cannot justify becomes a question before the report closes. Never a silent cut of substance. The rule scopes to substance and leaves line-level wording free, so a tightened sentence or a reordered clause needs no accounting. (Born of a compressed README section restored the same session, 2026-07-10.)

A pattern lint catches known coinages, known calques, and named term classes
```

## 233.5 — BUILD-PIPELINE HOME (skills/build-pipeline/SKILL.md) — new bullet after the docs-only door (line 96-97)

**old_string**:
```
- **Docs-only change:** re-read the changed section rendered + one grep that no stale claim contradicts the
  code; no spec/matrix step.
```

**new_string**:
```
- **Docs-only change:** re-read the changed section rendered + one grep that no stale claim contradicts the
  code; no spec/matrix step.
- **A rewrite or restyle accounts for every removal of substance (SPEC INV-110):** A rewrite or restyle that removes substance — a section, an argument, a rationale, a worked example — lists every removal in its landing report, one line of judgment each: the fact was kept and where, the owner killed it by name, or the rewriter proposes dropping and asks. A removal the rewriter cannot justify becomes a question before the report closes. Never a silent cut of substance. The rule scopes to substance and leaves line-level wording free, so a tightened sentence or a reordered clause needs no accounting. The accounting rides the landing report the communicator builds; the docs-only door above and the restyle loop both carry it. (Born of a compressed README section restored the same session, 2026-07-10.)
```

## 233.6 — MATRIX ROW (TEST_MATRIX.md) — in the `[node: communicator]` block, after M-224 (line 291, the block's last row)

**old_string** (tail of M-224, the anchor):
```
| M-224 | One spoken leave-word winds the session down to a shutdown-safe stop: workers halted or run to their landing (an unhaltable one recorded, its death-with-sleep said aloud), every lane at its checkpoint, red never committed (failing test tops the resume file), green committed under standing gates, resume file says what resumes where; first beat gives minutes-to-safe, last is ONE closing line — safe to power off + what resumes where — said only when every point above holds, in all three homes (spec clause + communicator leave-word rule + base checkpoint rule 6); never the closing line before the walk holds, never a leave guessed from silence | INV-95 | string | `test_leave_word_reaches_a_safe_stop` + `test_closing_line_says_safe_and_what_resumes` + `test_never_said_early` (red proven against the pre-law homes, 2026-07-10) | BUILT |
```

**new_string**:
```
| M-224 | One spoken leave-word winds the session down to a shutdown-safe stop: workers halted or run to their landing (an unhaltable one recorded, its death-with-sleep said aloud), every lane at its checkpoint, red never committed (failing test tops the resume file), green committed under standing gates, resume file says what resumes where; first beat gives minutes-to-safe, last is ONE closing line — safe to power off + what resumes where — said only when every point above holds, in all three homes (spec clause + communicator leave-word rule + base checkpoint rule 6); never the closing line before the walk holds, never a leave guessed from silence | INV-95 | string | `test_leave_word_reaches_a_safe_stop` + `test_closing_line_says_safe_and_what_resumes` + `test_never_said_early` (red proven against the pre-law homes, 2026-07-10) | BUILT |
| M-248 | A rewrite or restyle that removes substance names every removal in its landing report (INV-110, row 233): a rewrite or restyle that removes a section, an argument, a rationale, or a worked example lists every removal in its landing report, one line of judgment each — the fact kept and where, the owner killed it by name, or the rewriter proposes dropping and asks; a removal the rewriter cannot justify becomes a question before the report closes; never a silent cut of substance; the rule scopes to substance and leaves line-level wording free; the law lives in three homes: the spec clause, the communicator's pre-report walk, and build-pipeline's docs-only door; born of a night docs pass that compressed the README's account of why live-spec stands beside BMAD, Kiro, and spec-kit to one pointer line, restored the same session (2026-07-10); never a silent cut of substance, never a line-level tightening dragged into the accounting | INV-110 | string | `test_removal_rule_in_all_three_homes` + `test_scope_carveout_in_all_homes` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```

## 233.7 — ARCHITECTURE.md OWNED-ANCHORS (line 44, communicator node's "Owns" column)

**old_string**:
```
INV-94, INV-95, INV-42
```

**new_string**:
```
INV-94, INV-95, INV-110, INV-42
```

## 233.8 — APPLIER VERSION REMINDERS (live values move tonight — apply +0.0.1 over whatever each reads at apply time; never hardcode a target)

- `skills/communicator/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.3 now).
- `skills/build-pipeline/SKILL.md` frontmatter `version:` — +0.0.1 (reads 1.0.5 now).
- `VERSION` (pack) — +0.0.1 (reads 1.0.22 now).
- Base rulebook NOT touched: do **not** move the seven `` `live-spec-base` (v1.0.3) `` header pins for this row.
- No spec-internal version field exists to bump (the spec rides the pack VERSION).
- Red-proof order per house rule: run `tests/test_no_silent_drop.py` against the pre-delta tree first (all four asserts must fail — homes lack the needles), then apply the six edits, then green.

---

# DELTA — Row 234 — STOP (routing, not drafted)

Row 234 ("Managing one project's independent parallel lanes") trips the STOP rule on three counts, so I did not draft it:

1. **Surface-sized.** Its own size column reads `surface` (the queue's larger classification, same as rows 230/236), and its Done-when is a whole feature landing across four homes plus a first real multi-lane session citing it — not a string-level law edit.
2. **A structure change.** One of its mechanisms is a new *per-lane state line in the resume file* — a structural change to the NEXT_STEPS template (each lane naming its station and next step), which is a template/surface redesign, not a prose clause.
3. **A bundle of separable stories.** It packs at least five independently-shippable behaviours, each with its own home and its own likely invariant:
   - per-lane state line in the resume file → NEXT_STEPS template + spec clause;
   - a heartbeat that names every live lane → communicator, extends INV-35/INV-71;
   - lane-scoped workers with non-overlapping write-sets, worktree-default on overlap → **already largely covered** by INV-105 / INV-11 / T-18 / INV-39 (row 227); this half needs a de-dup check before it earns any new anchor;
   - one report that walks the lanes one by one → communicator report shape (kin to INV-34/the departures board INV-27);
   - the cross-lane commit law (one lane, one commit; never a sweep carrying a second lane's files) → build-pipeline commit law.

**Routing it needs:** enter through build-pipeline as a `surface` (spec → prove → architecture → matrix → tests), and at the spec step split into the separable stories above under the one-feature-one-story law — with the worktree/write-set half reconciled against INV-105/INV-11/T-18 first (it may fold in rather than mint a new invariant). It also self-declares dependence on rows 215 (parallel buildability) and 206 (pack orchestration), which the three cite each other — sequence it with those.

**Numbering consequence:** because 234 stops, the reserved **INV-111 / M-249 are not consumed**. To keep the INV index dense, the **next draftable row should take INV-111 and M-249** (INV-109/M-247 remain reserved for row 231's alignment half, blocked on the human's word). Row 233 consumes **INV-110 / M-248** as assigned.

---

## Self-verify

- Every test needle (`lists every removal in its landing report`, `one line of judgment each`, `A removal the rewriter cannot justify becomes a question`, `Never a silent cut of substance`, `line-level wording`) appears verbatim in all three drafted home texts (233.2 / 233.4 / 233.5); `[INV-110]` in the spec clause; `| INV-110 |` index row contains `removal`.
- All prose anchors quoted from the live tree (spec 203/1832, communicator 620, build-pipeline 96, ARCHITECTURE 44, matrix 291).
- No banned contrast frame: every prohibition is its own plain `Never a silent cut of substance.` sentence; the em-dashes wrap appositive enumerations, not denied neighbours.
- Dates only from the row's own record (2026-07-10) or the landing date (2026-07-12).
- M-248 / M-249 verified free; INV-110/INV-111 verified free.

---

RENUMBERED 2026-07-12 by the orchestrator's call: reservation of INV-109/M-247 lifted, codes consume in landing order; row 239 = INV-110/M-248, row 240 = INV-111/M-249. This row (233) itself landed as INV-109/M-247, one step down from the INV-110/M-248 this draft was written under (see row233-worker.md for the applier's renumber walk) — the "Numbering consequence" paragraph above, which reserved INV-109/M-247 for row 231, is superseded by this call; row 231 now takes the next free code at its own landing.

APPLIED + CLOSED at landing 2026-07-12 (row233-worker.md).
# Source coverage audit — docs/attic/2026-07-22-pre-format/PRODUCT_SPEC.md

Read-only audit. Source file: 2459 lines. Method: built the source's heading line map, matched
each conversion unit's `mapping.md` (and `assembly/assemble.py`'s `UNITS` list) to a source line
range, computed the gaps between assigned ranges, and read every gap to classify it.

## Coverage table

| Range (lines) | Lines | Owner unit / classification |
|---|---:|---|
| 1–47 | 47 | `conversion/what-live-spec-is` (header + `## What live-spec is`) |
| 48–276 | 229 | `conversion/build-loop-a-intake` (`## The build loop` intro + first half of `### Throwing a wish`) |
| 277–620 | 344 | `conversion/build-loop-b-doors-spec-lanes` (second half of `### Throwing a wish`: Doors/kinds/craft, Specifying and building, Parallel lanes) |
| 621–927 | 307 | `conversion/build-loop-c-prototype-tests-rhythm-publish` (prototype, spec-to-tests, rhythm, publishing) |
| 928–1055 | 128 | `conversion/what-the-human-sends-back` |
| 1056–1162 | 107 | `conversion/when-something-breaks` |
| 1163–1439 | 277 | `pilot/` (`## Starting and adopting a project`) |
| 1440–1616 | 177 | `conversion/agents-together` (`## When agents work together`) |
| 1617–1842 | 226 | `conversion/rules-and-who-applies` (`## The rules and who applies them`) |
| 1843–2026 | 184 | `conversion/bounds` (`## What holds the bounds`) |
| 2027–2030 | 4 | (b) navigation — `## Reference` intro paragraph, pure TOC ("supporting material: how the axes compose, the open questions, the index") |
| 2031–2092 | 62 | `### Composing across axes` (incl. `#### Document provenance`) — a converter is in progress on this range per brief; treated as covered |
| 2093–2116 | 24 | **(c) PROSE/RULES CONTENT — `### Open decisions` — no owner unit found. See UNCOVERED CONTENT below.** |
| 2117–2459 | 343 | (a) retired by design — `### Formal index`, the manual code table; `assembly/assemble.py` replaces it with a generated code-to-location table built by `scripts/build-index.py`, confirmed in the assembler source (`Reference` section = "generated output... no one edits it by hand") |

**Totals:** 2459 source lines. Owned by a conversion unit: 2026 (82.4%). Owned + in-progress
(Composing across axes) + retired-by-design (Formal index): 2431 (98.9%). The one range with no
owner and no by-design retirement is `### Open decisions` (24 lines, 1.0% of the file).

## UNCOVERED CONTENT

### Finding 1 — `### Open decisions` (source lines 2093–2116) has no assigned conversion unit

First line: `### Open decisions  [not a scenario]`

Bracket codes in the range: `D-1`, `D-6`, `D-7` (open decisions), `D-2`, `D-3`, `D-4`, `D-5`
(resolved decisions kept as one-line pointers), plus cross-cites `INV-69`, `E-7`, `E-13`, `E-16`.

This range is not in `assemble.py`'s `UNITS` list, not claimed as a "Source:" range by any
`conversion/*/mapping.md`, and the assembled `Reference` section (per `assemble.py`) is defined to
hold only the generated code table — nothing else. So nothing carries this section forward by
design; unlike the Formal index, this section is not superseded by an equivalent generated
mechanism.

Splitting by what each entry actually is:

- **Resolved decisions (D-2, D-3, D-4, D-5)** — each is a one-line pointer to a decision whose
  "full dated rationale moved to JOURNAL.md" (source's own words, line 2103), and whose *content*
  already has a real home elsewhere. Checked against the assembled document: D-2's content (tier
  routing proposed-not-fixed) is at `rules-and-who-applies` R11 [D-2, INV-69]; D-4's content
  (package-is-source) is at `rules-and-who-applies` R1 [D-4] and `bounds` R31 [D-4]; D-5's content
  (all-into-profile / thin loader) is at `rules-and-who-applies`'s "one home and a thin loader"
  case [E-16, INV-13]. D-3's content (snapshot retention: last-only in the working tree, git
  history as archive) is substantially present at `bounds` section.md line 633 ("keep only the
  last baseline in the working tree... git-tracked... any older baseline can be checked out"
  [E-7]), though the specific clause "a heavy surface keeps only its hash" was not found restated
  in any converted unit (its source home, line 1923, sits inside `bounds`' already-claimed range,
  so this is a unit-internal completeness question, not a range-coverage gap, and is flagged only
  as a side note — not one of this audit's findings). These four pointer lines are the kind of
  provenance/history content the new format's own rule sends to `JOURNAL.md`, so their absence as
  literal lines is consistent with the migration's design, not a silent drop.

- **Open decisions (D-1, D-6, D-7)** — live product decisions, not yet resolved, that a reader of
  the new spec would need to see. These are NOT history and have no "elsewhere" home:
  - **D-1** (attic layout: flat-with-manifest vs. dated subfolders) survives, but only as a side
    effect of the pilot unit's own cross-reference to the code, compressed into a `[GAP: ...]`
    line in the assembled document (`assembly/PRODUCT_SPEC.md` line 3824): "the layout of the
    adoption attic — a flat folder with a manifest against dated subfolders — is an open decision.
    D-1". The decision's substance is kept, though its declared "not yet forced, revisit at next
    real adopt run" framing is not.
  - **D-6** (pair queues: one stitched reading view across the pair's two queues, vs. strictly two
    — recommended two plain queues until real friction earns a stitched view) — grepped for
    "pair queues", "stitched", and the code `D-6` across every `conversion/*/section.md` and
    `pilot/section.md`: zero matches anywhere. `agents-together`'s R20 ("Running an engine and its
    instance as a pair") states each repo keeps its own queue (R20.1) but never raises or answers
    the stitched-vs-two question. **This decision's content is completely dropped** — it appears
    nowhere in the assembled document.
  - **D-7** (pair specs: may the instance's spec cite engine facts, or only the content contract —
    recommended: contract-handles only, since "an entry is the engine's versioned public promise,
    an internal rots at the engine's next refactor") — the operative clause survives, folded into
    `pilot/section.md` R20.2 as a hard `shall`: "the instance's spec *shall* state what the product
    is for its real user and *shall* cite the engine only by its content-contract handles.
    [INV-79, INV-86, D-7]". But the decision's **open/recommended status and its stated reasoning**
    (the promise-vs-internal-rot rationale) are gone — the new text asserts the recommendation as
    settled law with no trace that the source called it an open, merely-recommended question.

## Summary

- Total source lines: 2459
- Covered (assigned unit, or in-progress per brief, or retired-by-design): 2431 (98.9%)
- Class-(c) findings: 2
  1. `### Open decisions` has no owner unit; its two still-open, un-homed decisions are D-6 (pair
     queues stitched-vs-two) and D-1 (attic layout) — D-1 survives only as an incidental GAP line.
  2. Within that same gap, D-6 (pair queues) is a total silent drop — zero trace in the assembled
     document — and D-7 (pair specs) has its operative rule kept but its open/recommended status
     and stated rationale silently dropped, now read as settled law.

## Resolution (row 445)

Both findings are resolved. The new format sends provenance and decision history out of the spec body,
so the three open decisions move to the root `DECISIONS.md`, and each is pointed to from the
requirement it touches by a gap line carrying its code — the mechanism the format already owns (the
same shape the pilot's D-1 gap line already used).

**Finding 1 — the three open decisions.** `DECISIONS.md` gains an **Open — recorded, not yet decided**
section holding D-1, D-6, and D-7 with their full source content: the question, today's practice, the
recommendation, and its reason. These are open questions the pack carries, not decisions attributed to
the person, so they name no exchange and carry no date, and the section says so; the authority-anchor
gate passes them because they are pack-voice prose carrying no dated authority-claim. In `pilot/section.md`:

- **D-1** (attic layout): the existing gap line under R12.5 now also names `DECISIONS.md` as the home.
- **D-6** (pair queues, stitched-versus-two): previously dropped everywhere, now added as a gap line
  under R20.1 — the criterion that already states each repo keeps its own queue — carrying today's
  practice (two plain queues) and pointing to `DECISIONS.md`. It becomes no `shall` criterion, since
  the recommendation is an open decision rather than an enforced duty.
- **D-7** (pair specs): R20.2's `shall` stays as today's enforced practice (the instance cites the
  engine only by content-contract handles); a gap line added beneath it records that the underlying
  policy is an open decision recorded in `DECISIONS.md`, restoring the open/recommended status the
  source carried. `pilot/mapping.md` records all three as declared sharpens (Part 1, Part 2, Part 3).

**Finding 2 — the too-heavy-surface snapshot rule (source line 1923), verified real.** The claim "a
too-heavy surface keeps only its manifest line and hash" sits in the bounds unit's range but was
absent from `bounds/section.md` (its `mapping.md` Part 3 mapped source lines 1922 at claims 126–127
but never line 1923). It is restored as `bounds/section.md` R27 criterion 4 (`*if* a surface's
rendered bytes are too heavy to hold in git, *then* … keep only its manifest line and content hash …
diff … on the hash alone`), the adoption criterion renumbering to R27.5; `bounds/mapping.md` adds it as
claim 126a and bumps the total to 177.

All five format lints (vocabulary, weak-words, requirement-shape, no-history, one-name) pass on both
changed `section.md` files, and the authority-anchor gate passes on `DECISIONS.md`.

# Gates plan: the format mechanism's guardrails

This plan lists, for each of the six requirement areas in `spec-delta.md`, the scripts that enforce it, the red case each one fires on, its test file, and how it stands against the 32 existing shape-readers — replace or coexist. History and rationale live in `JOURNAL.md`; this plan states the target state.

Paths: enforcing gates live under `guardrails/`; builders and shared helpers live under `scripts/`.

**Arming (INV-270):** the whole spec converts in one delivery, and every gate this plan names arms in that same conversion delivery — none arms before it. Precedent: the description gate armed in the delivery that back-described.

---

## Area 1 — the document format (INV-250..257)

The format's laws are enforced by the mechanical-lint set. Each is one script, run free on every push, and each is also a member the comprehension gate (Area 5) calls in its mechanical layer.

| Script | Red case | Test file | Against the 32 |
|---|---|---|---|
| `guardrails/check-requirement-shape.py` (INV-250, INV-251) | a requirement missing its Context, User Story, or named cases; a criterion sitting outside a case; discontinuous criterion numbering; a criterion carrying more than one trigger or more than one response; a trailing anchor missing | `test_requirement_shape.py` | **replaces** `test_scenario_heading_tag.py` and `test_description_field.py` — the heading/tag/description-field parsers read the old prose shape this script supersedes |
| `guardrails/check-vocabulary.py` (INV-254) | a domain noun used in the body with no glossary entry; a glossary entry no body line uses | `test_vocabulary_check.py` | **new**; coexists with `check-index-prose.py` |
| `guardrails/check-one-name.py` (INV-255) | one thing referenced under two names anywhere in the document | `test_one_name_check.py` | **new**; coexists with all shape-readers |
| `guardrails/check-weak-words.py` (INV-256) | a weak word from the seeded list standing with an unfilled slot and no nearby reference point and no `[GAP]` line | `test_weak_words.py` | **new**; no existing reader covered vague terms |
| `guardrails/check-style.py` (INV-251) | an all-capital word outside a code anchor or filename; a keyword not set lowercase italic; a sentence over the length bound; a contrast-by-denial frame; a grading adjective | `test_style_lint.py` | **coexists** with `stamp-versions.py`; partially **replaces** the tag-format assertions inside `test_scenario_heading_tag.py` |
| `guardrails/check-gap-lines.py` (INV-252) | a `[GAP: ...]` line whose form is malformed, or a gap line that carries an invented answer rather than naming the hole; an evaluative phrase with no judge and no inputs and no gap line (INV-257) | `test_gap_lines.py` | **new**; coexists |
| `guardrails/check-no-history.py` (INV-253) | a dated note, a provenance sentence, or a past-choice reason appearing in the spec body rather than in `JOURNAL.md` | `test_no_history.py` | **new**; coexists |

---

## Area 2 — the generated index (INV-258, 259)

| Script | Red case | Test file | Against the 32 |
|---|---|---|---|
| `scripts/build-index.py` (builder, not a gate) | — builds the code-to-location table from the body criteria at freeze | `test_build_index.py` | **supersedes** `needle-extract.py` as the code-to-home extractor; reuses its matching logic |
| `guardrails/check-index-generated.py` (INV-258, INV-259) | the committed index differs from a fresh build (a hand edit); a code on a body criterion missing from the index; a code in the index carried by no body criterion; an expected-non-empty input arriving empty or missing — the `require_nonempty` guard, INV-218 | `test_index_generated.py` | **replaces** `test_formal_index.py`, `check-index-prose.py`, and the index half of `check-freeze.sh` / `spec-freeze.py`; `test_traceability.py` is **rebuilt** — its row source repoints to the generated index |

After the migration the criteria and the glossary are the authored home of every code's plain statement, and the generated index carries locations only (INV-271). On the migration-end delivery, the description-field gate — `check-description-field.py`, the check behind INV-239 — **retires** with that stated successor.

---

## Area 3 — the delta classifier (INV-260..263)

| Script | Red case | Test file | Against the 32 |
|---|---|---|---|
| `guardrails/check-delta-record.py` (INV-260..263) | a code in the old criteria set absent from the new with no *retire* declared; a code in the new set absent from the old with no *new* declared; a code whose criterion text changed under normalization with no *sharpen* declared; a *sharpen* code whose old sentence survives a normalized full-sentence match anywhere, or whose own criterion line still equals its old text; a declared new criterion over the 500-byte cap; document byte growth over the delivery — sharpen bytes and glossary-addition bytes excluded — exceeding the declared new-criteria budget | `test_delta_classifier.py` | **replaces** `check-pin-drift.sh` — pin-drift detected a moved anchor; the sharpen/appearance/disappearance diff generalises it; **coexists** with `check-freeze.sh` / `spec-freeze.py`, which supplies the old criteria set from the last freeze |

The old and new criteria sets come from `build-index.py` output at the last freeze versus the working tree; the classifier keys each criterion by its code and its text, diffed under normalization — whitespace collapsed, italic markers stripped, letters case-folded outside code anchors. The delta record rides the existing single-pen serialization for the shared spec document (INV-198), and a delivery that merges after another has frozen the spec re-diffs against the post-merge freeze baseline.

---

## Area 4 — the size ratchet (INV-264, 265)

| Script | Red case | Test file | Against the 32 |
|---|---|---|---|
| `guardrails/check-size-ratchet.py` (INV-264, INV-265) | a delivery's new bytes-per-criterion — criterion-line bytes only, glossary and preamble excluded, divided by criteria count — above the recorded bound in `guardrails/spec-ratchet.json`; a delivery raising the recorded bound outside a change to Requirement 4 | `test_size_ratchet.py` | **coexists** with `check-doc-bound.py`, split by document: the ratchet governs `PRODUCT_SPEC.md` alone, and `check-doc-bound.py` stays in force for `ROADMAP.md`, `TEST_MATRIX.md`, and `JOURNAL.md`; **coexists** with `check-doc-rotation.py` / `rotate-doc.py`, which handle rotation, a separate axis |

On a delivery whose new bytes-per-criterion is below the bound, the script lowers the recorded bound in `guardrails/spec-ratchet.json` to the new value; it never raises it. The initial bound is the value measured at the migration-end freeze, recorded by the freeze actor.

---

## Area 5 — the comprehension gate (INV-266..268)

| Script | Red case | Test file | Against the 32 |
|---|---|---|---|
| `guardrails/comprehension-gate.py` (INV-266..268) | a section shipped while any mechanical lint reds; a reader sent while the mechanical layer is red; a section shipped before two consecutive reads returned zero blocking findings; a fifth round of reads started on one section with new blocking findings still arriving and no escalation raised; a cold reader's finding naming a source hole with no queue row opened | `test_comprehension_gate.py` | **new** — the old suite had no comprehension layer; **coexists** with and orchestrates every Area 1 mechanical-lint script |

The gate runs the Area 1 lints first and stops the section if any reds. The cold-reader panel is an agent-or-human step; the script reads the panel's per-read blocking-finding log, holds the section until two consecutive reads log zero, and opens a queue row for each reader-named source hole. After four rounds on one section with new blocking findings still arriving, the gate escalates to the human as a named question — which terms keep failing — and pauses the panel (INV-267). `[GAP]` in the delta: the panel size is unstated, so the script takes the read count from a configured value and does not hard-code a panel size.

---

## Area 6 — gate reach (INV-269)

| Script | Red case | Test file | Against the 32 |
|---|---|---|---|
| `scripts/gatelib.py` (shared helper, not a gate) | — every family gate calls it to print its green line with the files opened and the rows matched of rows scanned | `test_gatelib.py` | **new**; coexists with `stamp-versions.py`, which stamps the version onto the same output line |
| `guardrails/check-gate-reach.py` (INV-269) | a family gate's green line missing the files-opened or rows-matched-of-scanned fields; a gate reporting a pass while its scanned-row count is zero, printing a bare green line | `test_gate_reach.py` | **new** — the meta-gate wraps the Area 2–5 gates and folds ROADMAP row 446's reach principle into this family |

Row 446's principle folds in naturally: the Area 2–5 gates each open files and match rows, so `gatelib.py` gives them one way to state that reach and `check-gate-reach.py` proves they do. The principle applies to this family's gates only, as the delta's Requirement 6 scopes it.

---

## Shape-reader disposition summary

Of the 32 existing shape-readers, this plan touches these by name:

- **Replaced** (the new format removes the shape they parsed): `test_description_field.py`, `test_scenario_heading_tag.py`, `test_formal_index.py`, `check-index-prose.py`, `check-pin-drift.sh`, and the index half of `check-freeze.sh` / `spec-freeze.py`.
- **Retired with a stated successor**: `check-description-field.py` (INV-239) retires on the migration-end delivery; its successor is the authored home stated in Requirement 2 (INV-271) — the criteria carry each code's rule, the glossary carries each entity code's definition, and the generated index carries locations only.
- **Rebuilt**: `test_traceability.py` — its row source repoints to the generated index; the code-to-test links it checks stay.
- **Superseded but reused**: `needle-extract.py` (its matching feeds `build-index.py`).
- **Coexisting unchanged**: `check-doc-bound.py` (stays in force for `ROADMAP.md`, `TEST_MATRIX.md`, and `JOURNAL.md`; the ratchet takes `PRODUCT_SPEC.md`), `check-matrix-coverage.sh`, `check-doc-rotation.py` / `rotate-doc.py`, `stamp-versions.py`, and the remaining pytest shape-readers whose subjects — matrix coverage, rotation, version stamps — this migration does not touch.

The 17 pytest shape-readers split the same way: those parsing the old heading, tag, or description-field shape (test_scenario_heading_tag, test_description_field, test_formal_index and their kin) are replaced by the Area 1 and Area 2 gates; test_traceability is rebuilt onto the generated index; those parsing coverage or rotation coexist.

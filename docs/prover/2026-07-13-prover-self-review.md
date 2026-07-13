# Prover record — 2026-07-13 — the prover run on the prover skill itself

**Prover skill version at this pass:** 1.0.10 (bumped this landing; see finding 2).
**Change under review:** the product-prover skill itself (`skills/product-prover/SKILL.md`), reviewed to
confirm it is internally sound after the interactive-overlap lens landed (row 299). Owner's ask: "run the
prover on the prover, just to see it's all in order."

**Review mode:** adversarial fresh-context audit (SPEC INV-46), run on Fable at the owner's word, opening
hypothesis "tasks completed, goal missed". Verdict: **in good order** — the method is internally sound and
the three composition lenses (INV-125/126/136) are a coherent family with the new one framing its finding as
the spec's text, not rendered geometry. Six findings, all folded this landing.

| # | Finding | Severity | Disposition |
|---|---|---|---|
| 1 | The stress-lens intro said "nine families of questions" while the list holds eighteen bullets — the count drifted 9→18 as lenses were appended (INV-72/125/126/136/127/128 among them). A guardrail test pinned the literal "nine families", so it guarded the word without verifying the count. | MUST-FIX | **FOLDED** — the number dropped for a self-maintaining phrasing ("the families of questions below"); the test needle changed to "families of questions" so it can no longer go stale (kin of the no-drifting-number-in-prose rule). |
| 2 | The lens landed at row 299 without bumping the prover skill's own frontmatter version (stuck at 1.0.9 since row 294), yet the record-opens-by-naming-the-version rule stakes the full-pass re-arm on that line. | MUST-FIX | **FOLDED** — bumped to 1.0.10 and named at the head of this record; the re-arm mechanism reads a moved version again. |
| 3 | The entry-symmetry lens named its finding "A get with no set", a coined getter/setter metaphor absent from SPEC INV-50 and murky — a violation of the no-coined-names law. A guardrail test pinned the coined phrase. | SHOULD-CLARIFY | **FOLDED** — restated in plain words ("A conditionally-entered face with no deliberate re-entry path is a finding"); the test needle updated in lockstep. |
| 4 | The interactive-overlap lens named one referent two ways — "the lower layer's control's fate" then "retract the lower layer's chrome". | SHOULD-CLARIFY | **FOLDED** — "chrome" → "controls" (one name); its test needle updated. |
| 5 | The FULL-mode line wrote the MINOR pattern as `0.x.0`; the pack versions at 1.1.x, where a MINOR bump is `1.2.0`. | SHOULD-CLARIFY | **FOLDED** — rewritten `x.Y.0`. |
| 6 | Two comma-led contrast frames ("is a decided answer, not a gap"; "a named plan or a fold, not auto-rejection") — the no-contrast-frame law. | SHOULD-CLARIFY | **FOLDED** — each restated as its own positive sentence, the denied neighbour dropped. |

**Deferred (out of this file's scope, noted for a future harmonizer):** INV-125 and INV-126 carry their
born-of stories in the spec body while INV-136's lives in JOURNAL; the JOURNAL placement matches the
history-goes-to-JOURNAL rule, so the two older clauses are the outliers if anyone ever harmonizes.

**Cross-references:** all 28 tags in the file resolve against the Formal index (verified in the audit).
**Suite:** 609 green after the folds.

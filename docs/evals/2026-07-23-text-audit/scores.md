# Scores — text-audit eval, first real run (2026-07-23)

Trigger: the text-audit eval carried a predicted red only; this run proves it against real
transcripts. Arms: one Sonnet worker each, bare vs with-skill (repo skill version: text-audit
3.6.0). Bare arm used zero tool calls (verified); with-skill arm read the repo's own
`skills/text-audit/SKILL.md` and used 15 tool calls (real lint scripts + one fresh cold-reader
agent under the verbatim reader-prompt). Honest boundary (evals/README.md) applies: bare is
bare-of-the-SKILL, loader-fed — the machine-global loader already teaches plain-words and
ground-every-term, and it shows in the bare transcript.

## text-audit

| Criterion | bare | with-skill |
|---|---|---|
| Flags the undefined coined term "Relay Gate" | MET BARE — "coined name with no definition", first use pinned | **PARTIAL (regression vs the eval's expectation)** — the step-1 lint fix reworded the denial frame to "is a coordinator: it clears panels to refresh…", part-defining the term; the cold reader then returned it only NON-blocking ("restates rather than adds content"), never blocking with first use pinned |
| Flags the unfilled "depends on the upstream state" | MET BARE — "upstream of what… a term the paragraph never grounds" (the eval predicted RED; the loader-fed bare arm caught it) | GREEN — blocking, both empty slots named (what the upstream state is, what fires the refresh) |
| Flags the contrast-by-denial "a coordinator — not a queue" | MET BARE — read as define-by-what-it-isn't plus a non-sequitur (the eval predicted RED) | GREEN — `spec-style-lint.py` hit, fixed before the reader with a positive sentence stating what the coordinator does |
| Every finding classified blocking or non-blocking | RED — flowing prose, no per-finding verdict | GREEN — 6 blocking, 4 non-blocking, loop keyed to zero blocking |
| Mechanical lints run before the reader | RED — no lints, one prose pass | GREEN — five lints named and run first (two fell to their grep fallbacks on a glossary-less paragraph, per the skill); the one hit fixed before the reader |
| Fixes drawn from the source, never invented | RED — no fix pass at all: nothing invented (unlike the eval's predicted red), but no fix and no question recorded either | GREEN — four `[GAP]` marks + four owner questions, no invented definition; the one rewording drew only on the paragraph's own sentences |
| The loop's close stated: two consecutive clean reads | RED — one pass, no termination rule | GREEN — close stated, loop honestly reported open pending the owner's answers |
| The reader runs with zero context on the text's history | RED — the same session that got the audit framing did the reading | GREEN — fresh agent spawned under the verbatim reader-prompt, given only the corrected text |

**Skill's proven value (RED→GREEN rows):** classification, lints-first, fixes-from-source
discipline, the stated close, and the zero-context reader — the METHOD rows. All three planted
DEFECTS were substance the loader-fed bare arm already caught, so the eval's predicted reds on
rows 1–3 downgraded to MET BARE on this real run.

**Regression flag (with-skill arm):** fixing the contrast-by-denial frame at the lint step
inserted a partial definition of "Relay Gate", which muted the cold reader's coined-term finding
to non-blocking. The skill's lint-fix rule and its vocabulary rule interact here: a step-1
rewording can pre-answer a term the reader was supposed to flag blocking. Worth a queue row —
either the lint fix at step 1 may not introduce defining content for an audited term, or the
vocabulary fallback must flag the coined term itself before any rewording.

**Extra find (with-skill arm):** the cold reader surfaced a defect the eval never planted — the
apparent contradiction between "depends on the upstream state" and "panels never wait on one
another" — reported per the reader-prompt's new-find instruction.

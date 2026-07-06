# Kill-list — <artifact or project name>

> The human's review-round cuts, made mechanical (live-spec pack: SPEC INV-42 + E-26). One line per
> killed literal: the exact phrase, the date, one line of context. A line is APPENDED the moment a
> cut happens and NEVER removed — a wipe must not resurrect a cut. A scanner test reads this table
> and greps the artifact's surfaces for every literal below; a reappearance turns the suite RED
> (see the guardrails README's kill-list scanner note).

| Killed literal (exact) | Date | Context (one line) |
|---|---|---|
| "<example — not X, it's Y>" | YYYY-MM-DD | the negation frame, killed in review round N |

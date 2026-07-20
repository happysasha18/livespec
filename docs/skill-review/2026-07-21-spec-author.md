# Skill review — spec-author (whole-file prose-quality sweep to the style-lint floor)

`SKILL-REVIEW`

Skill: spec-author
Date: 2026-07-21
Reviewer: skill-creator (Anthropic) — review method applied against the diff from a fresh read;
this is the highest-risk of the four (large prose churn), so the sweep was checked line-by-line for
any weakened rule and for a moved trigger.

Verdict: passes — the sweep changed register and wording only. Every instruction's meaning is
preserved, no rule was weakened, the anchor set is byte-for-byte identical (the skill's own
restructure-safety guard), and the two reworded scissors constructions were reworded without
dropping their force. The `description:` frontmatter was touched — shouted capitals lowercased — but
every trigger phrase and keyword is preserved, so no routing regression is expected. Body reviewed;
description reviewed.

## What changed

A whole-file prose-quality sweep of `skills/spec-author/SKILL.md` to the style-lint floor: shouted
capitals lowercased (IS, DOES, NEVER, EVER, MANDATORY, PRIMARY, WHOLE, LEAD, START, ADD, WRITES,
REVIEWS, NOT, FIRST, FREEZES, and others), second person removed (`you`/`your` → `spec-author` / `the
author` / `the author months later` / `the reply`), two scissors ("X — not Y") constructions
reworded, and a handful of jargon tokens backticked (`LLM`, `TBD`, `ISO`). The change spans the
frontmatter description and roughly forty body lines.

## How this review was run

Because prose churn this wide is where a rule quietly loses its force, the diff was read as 1:1
line replacements and each changed line classified: pure caps-lowering, pure second-person removal,
or a genuine reword. The genuine rewords were then checked one by one against the meaning of the
line they replaced. Separately: (1) the anchor set was compared before/after — the skill preaches an
anchor-set guard for any restructure and must pass its own; (2) the description was diffed for any
dropped trigger phrase; (3) the diff was checked for any wholly-deleted rule (an unbalanced
insertion/removal), since a sweep can smuggle a cut under cover of a reword.

## Findings

- **Anchor set identical — the skill's own restructure guard holds (clean).** No SPEC/INV/T/E/CR/S
  code was added, dropped, or altered across the whole diff (INV-127, INV-215, INV-118, INV-163,
  T-15, T-14, INV-19, T-13, INV-18, INV-29, INV-50, INV-20, INV-21, E-29, INV-73, INV-79, INV-101,
  INV-150, INV-31, INV-138, INV-41, S-0, INV-16, E-17, INV-37 all preserved in place). By the skill's
  own anchor-set guard, an identical anchor set proves the shape changed and no rule was lost.

- **No rule weakened by lowering its capitals (clean).** The normative force of each rule is carried
  by the word, not its case: "must NEVER happen" → "must never happen", "must EVENTUALLY happen" →
  "must eventually happen", "MANDATORY for a feature and no scope cut may trim it" → "mandatory for a
  feature and no scope cut may trim it", "silence is not an option / not a legal state" preserved.
  Every "must/never/mandatory/always" survives as a word; only the shouted emphasis is gone — which is
  precisely what the style-lint floor requires, and the doc now practises the "shouted capitals" rule
  it names in the style-lint list.

- **The two reworded scissors kept their force (checked, clean).** (1) "the publish floor is the
  backstop, not the author." → "Write the shipped clause impersonally from the first draft rather than
  scrubbing names at publish time, with the publish floor standing only as the backstop." The
  author-owns-it force that "not the author" carried is preserved by the imperative "Write ... from
  the first draft rather than scrubbing at publish time" plus "standing only as the backstop." Meaning
  intact, arguably clearer. (2) Edge-completeness: "below the low end and above the high end — not only
  at the one point the wish named" → "... below the low end and above the high end, beyond the one
  point the wish named." "not only ... but also both ends" becomes "both ends beyond the one point" —
  same requirement (write both bounds, not just the named point). Neither reword dropped a rule.

- **Genuine rewords preserve meaning (checked, clean).** "Without it, you get the classic stranding
  bug" → "Without it, the classic stranding bug follows" (causal force intact); "close the holes
  yourself AND WRITE HOW each was closed" → "close the holes and write how each was closed" (the
  write-how obligation intact); "Run the completeness pass on what you wrote" → "on the section just
  written"; "Hand off on the WHOLE spec — your delta included" → "on the whole spec — the delta
  included"; "You also surface, in your reply, the ⟨DECIDE⟩ points you couldn't resolve" → "The reply
  also surfaces the ⟨DECIDE⟩ points that could not be resolved and the leading questions behind them."
  Each preserves the instruction; none narrows it.

- **No rule deleted (clean).** The diff is line-for-line replacement throughout — no hunk removes a
  rule without replacing it. The spine checklist (items 1–7), the facet list, the fit-walk lens
  lists, the completeness-pass questions, and the anti-patterns are all present with the same content,
  only de-shouted and depersonalised.

- **Description triggering preserved despite the frontmatter touch (checked — highest-risk item).**
  The `description:` change lowercases shouted capitals only (LEAD, START, ADD, WRITES, REVIEWS, NOT).
  Every trigger phrase is byte-identical after the caps change — "spec this out", "write the spec for
  X", "start a spec", "add a feature/surface", "keep a spec in sync", "how to structure a spec", and
  the "NOT for reviewing ... product-prover's half" negative-boundary. No keyword was added or removed,
  so the routing surface is unchanged in substance and no eval drift is expected. (The caps were
  emphasis, not trigger tokens; skill-creator treats the description as the primary triggering
  mechanism, and here its content is preserved.)

- **Register fit — the sweep is internally consistent (clean).** The doc removed its own shouted
  capitals and second person, which are exactly two of the tells its style-lint clause lists as
  blocked ("shouted capitals, second person"). The skill now conforms to the floor it authors, so the
  sweep also removed a latent self-inconsistency rather than merely restyling.

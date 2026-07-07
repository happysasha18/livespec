# Prover cross-link — SPEC humanize: "Throwing a wish" CHUNK 1 of ~5 (2026-07-07, session 25)

The giant wish-walk section (595 lines, 157 tested phrases, 86 code groups / 165 occurrences) is rewritten
in the register in contiguous chunks, one per loop tick, each gated against the WHOLE-section baseline so
nothing is lost across chunk seams.

CHUNK 1 = the intro (wish → queue row → the one-path walk) + the bold-leads: How batched questions reach
you · A decision card asks in consequences, not mechanisms · How a wish is classified · A big wish
negotiates scope, never time · One wish = one user story.

Gates (whole section, after this chunk's splice): 157/157 tested phrases preserved section-scoped;
code multiset identical to baseline (165 occurrences / 86 groups, zero diffs); full suite 175 green.
Chunk 1 carries 15 of the tested phrases and ~30 code occurrences, all preserved.

## Facts carried in chunk 1 (all KEPT)
- Wish = one plain request, any size, any moment [E-2]; becomes a queue (ROADMAP.md) row same minute, fields
  pulled into a list (your words / class / status / acceptance) [E-3]; spoken means the row exists; rows
  never deleted, terminal exits archived, deferred rows stay active; no wish is ever lost [INV-1].
- The one-path walk pulled into a list (classify + INTAKE line / draft spec-delta / validate whole spec,
  only human questions batched / queue + in-work / land / LANDING line) [T-1..T-7].
- How batched questions reach you: ONE interactive decision page, lane keeps moving [INV-4]; archived in
  `docs/decisions/`, harvested same session, an answer left un-harvested is a decision lost; an answer is
  his word (withdrawn-answer law, 2026-07-05 shell-separator, Russian quote paraphrased) [INV-9]; mechanics
  in communicator rule 10 [INV-13] [E-22].
- A decision card asks in consequences, not mechanisms: opens with what the choice CHANGES for the person;
  labelled by consequence; 2026-07-06 origin paraphrased [INV-28 kin] [INV-32].
- How a wish is classified: four size words (bug/small/surface/large), priority normal / critical / quick
  win, classifier asks and never guesses [T-16], a kind not yet named scales nothing down [INV-22], lane
  keeps moving [INV-4] [INV-12].
- A big wish negotiates scope, never time: no time estimates (not an input the walk accepts), Alexander's
  scope-not-timelines word paraphrased; cut the scope / split into stages list; bends scope only, never
  order [T-11]; no cut touches the fences [T-14] / facets [INV-18] / non-goals + success measure
  [INV-20, INV-21]; Scope dials richness; it never touches the safety net [T-15]; [INV-4], [INV-5], [INV-12].
- One wish = one user story; a row closes only whole: door-and-gallery fusion origin; split at intake, each
  story its own row; stages slice one story's depth [T-15]; sub-behaviours are acceptance; a split cites the
  spoken wish [INV-1]; per-leg Done-when, half-done is a status, never a landing; LIVE-STATE never compresses
  an open leg [M-2] [INV-26] [T-17] [INV-12].

## Wording changes worth naming (meaning intact)
- Three Russian quotes rendered as plain-English paraphrases with their dates; no new quotation introduced.
- The queue-row fields, the walk stages, and the two scope moves pulled into lists.
- Long compound sentences split throughout; no new scissors added (required "never"/"not" phrases kept).

Verdict for chunk 1: **CLEAN.** Whole-section gates green after the splice; the remaining chunks follow.

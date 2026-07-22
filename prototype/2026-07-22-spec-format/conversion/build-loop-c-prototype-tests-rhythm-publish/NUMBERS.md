# NUMBERS — the size effect of the rewrite

All figures are bytes (UTF-8), measured with a command, not estimated.

## The measured inputs

| Item | Bytes | How measured |
|---|---:|---|
| (a) Source section body | 74,560 | `PRODUCT_SPEC.md` lines 621–927, the four subsections `### A prototype stays a sketch`, `### From the spec to the tests`, `### The rhythm: breakpoints, milestones, pushes`, and `### Publishing`, from the first heading to the line before `## What the human sends back`. |
| (b) Consumed Formal-index rows | 75,623 | The Formal-index rows for the 110 codes the section cites. Every cited code carries an exact index row (this stretch names no inline-only feature code), so all 110 rows are counted. |
| (a+b) Combined source basis | 150,183 | (a) + (b). |

## The produced output

| Item | Bytes |
|---|---:|
| (c) `section.md` total | 88,844 |
| — preamble (title + code legend + carried-terms note) | 2,116 |
| — glossary additions (20 new domain nouns) | 2,986 |
| — requirements (54 requirements, 102 named cases, 187 criteria, 2 GAP lines) | 83,742 |

## The two ratios

**Whole-basis: (c) / (a+b) = 88,844 / 150,183 = 0.592.**

**Prose-to-prose: requirements bytes / source body = 83,742 / 74,560 = 1.123.**

## What the ratios actually measure

The (a+b) denominator folds in 75,623 bytes of Formal-index rows. The new format does **not** rewrite those rows — it keeps pointing at the same index through the trailing code anchors (`[INV-157]`, `[E-14]`, …), exactly as the source prose already did. So the index is shared infrastructure, unchanged on both sides and counted once in each. Putting it in the denominator makes the whole-basis ratio (0.592) look like the format shrinks the document, when what it really does is fold prose into structured prose and leave the index alone. The 0.592 figure is honest arithmetic but is an artifact of counting the unchanged index inside the source basis; it is reported because the task defines the ratio that way.

The prose-to-prose replacement is the honest measure of the format's own weight:

- **Requirements bytes / source body = 83,742 / 74,560 = 1.123.**

The structured requirements come out at about 112% of the source prose they replace — a slight growth. This stretch behaves differently from the provenance-heavy bounds machinery section (which shrank to 0.683). The cause is the character of these four subsections: they are less dense in the datable, named-incident narrative the no-history law strips, and heavier in structural material that the format expands. The spec-to-tests and milestone subsections carry long enumerations — the architecture lens's six checks, the coverage-validation list, the milestone gate's dozen stations, the per-kind budget dimensions — which the format lifts into named cases and one-criterion-per-line bullets, and that scaffolding (Context blocks, User Story lines, case headers) is added mass the modest history-stripping here does not fully repay. The two GAP lines and the twenty glossary entries add a little more. The result sits close to the founding-section pilot's flat 1.003, above it rather than below.

## The finding, in one line

Converting these four build-loop subsections to the requirements format leaves the prose weight roughly flat — a **1.12× prose-to-prose ratio**, a slight growth driven by the format's scaffolding over structural, enumeration-heavy material that carries less strippable history than the bounds section did; the lower 0.592 whole-basis ratio is an artifact of counting the unchanged Formal index inside the source basis, and the prose-to-prose figure is the one that answers "does this format grow the spec here": it grows it a little, and the growth buys a stranger-readable structure with explicit cases, filled slots, and two recorded holes.

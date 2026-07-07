# live-spec — spec-style round 3 (2026-07-07 morning, session 23)

**One decision: does the use-case genre fit (row 148).** His morning verdict (~07:59) killed round 2:
the rule-book genre itself is out; the bar = the language of use cases and feature descriptions,
BMAD-METHOD and Kiro studied for the shape. This page shows round 3 — the same two sections in the
new genre. The interactive twin is the .html beside this file; this .md is the repo record.

Kill-list (cumulative, INV-42):
- Round 1 (~23:38 the night before): the first before/after sample — KILLED («непонятно ни до ни
  после»).
- Round 1b (~23:40): pack coinages as reader-facing words — KILLED; filler openers — KILLED.
- Round 2 (2026-07-07 ~07:59): **the rule-book genre itself — KILLED** («это все равно плохо»).
  Numbered laws in an owner's voice still read as regulation. New bar: use-case / feature-description
  language — user story, short narrative, testable acceptance criteria (BMAD + Kiro shapes).
- Round 3 (2026-07-07 ~08:11): **the STRUCTURE APPROVED** («структура правильная»); three language
  kills: the scissors frame "X — not Y" — BANNED FOREVER in all texts of all projects, law written to
  his profile (`language.no-scissors`) and to memory; the overcompressed narrative («the sketch itself
  carries the look» — «непонятно вообще») — KILLED; the non-native English (he read it as Hinglish) —
  KILLED, bar = short plain native sentences (`language.native-english` profile line). Round 4 = the
  same page rewritten to this bar; the page file is refreshed in place.

## The round-3 shape (what the samples demonstrate)

Each feature carries four parts: **User Story** (as a…, I want…, so that…) · a **short narrative
walk** — the person doing the thing, 2–4 sentences · **Acceptance Criteria** — a numbered list, one
testable behavior per item (samples use Kiro's strict WHEN … THEN … SHALL form) · **Why this
exists** — the incident that birthed the rule, two sentences at the end. Codes stay as trailing
anchors. Rule content held identical to the current spec — only the genre changed.

Sample A: "An approved prototype is the design reference" (the prototype-norm law, INV-43).
Sample B: "A bug takes the lane; parked work returns first" (T-9, T-11, T-18).
Full sample text: the .html twin.

## Questions on the page

1. **Genre verdict:** (a) fits — run the whole-doc pass (recommended) · (b) closer, adjust — name
   what · (c) still wrong — name what.
2. **Criteria voice:** (a) plain sentences, one behavior per item (recommended — same testability,
   easier read) · (b) strict WHEN/THEN/SHALL as sampled.

Answer file watched for: `live-spec-decisions-2026-07-07-round3.json` (Downloads → read back →
archived here → harvested into row 148 the same session).

## Research inputs (session 23, two parallel readers)

- **Kiro** (kiro.dev docs, spec-agent prompt, example repos): requirements.md = numbered Requirements,
  each = one user story + 3–5 EARS criteria (WHEN/IF/WHILE/WHERE … THE SYSTEM SHALL …); criterion
  address N.M is the traceability unit; tasks reference criteria (`_Requirements: 1.3_`); user-visible
  messages quoted literally inside criteria; requirements avoid implementation details.
- **BMAD-METHOD** (bmad-code-org/BMAD-METHOD, v4 templates + v6 spine): feature = one narrative
  description paragraph + nested FRs with testable consequences (declarative, no SHALL); stories =
  the three-line "As a / I want / So that"; Gherkin Given/When/Then in the epics doc; user journeys
  as short named narratives about a concrete person; stable global IDs (FR-1, UJ-3) never renumbered;
  non-goals and counter-metrics are load-bearing sections; glossary discipline — a synonym is a
  violation.

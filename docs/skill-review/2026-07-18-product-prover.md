# Skill review — product-prover (the 2.7.1 readability patch)

SKILL-REVIEW

Skill: product-prover

Date: 2026-07-18
Reviewer: skill-creator (Anthropic)

Verdict: changes folded: the split preserved every invariant citation and named concept, the two
count-fixes are genuine improvements, and the two folds below closed the one artifact the split left
(an orphaned mechanically-cut fragment) and one dropped README summary bullet. Description frontmatter
unchanged, so no triggering surface moved. Passes; description and body reviewed.

## What changed

The 2.7.1 patch (commits c59ed46 + d4adb20) is a prose/readability restructure of SKILL.md and
README.md with no behaviour change. Four dense one-paragraph lenses were split into nested sub-bullets
(the architecture lens, the declared-cross-cutting-laws sweep, the edge-condition sweep, the
paired-transition-symmetry lens); the bar-interpretation rule (INV-114) was extracted out of the
restructure-merge paragraph into its own named rule; the README was de-jargoned and gained an install
note plus ARCHITECTURE.md as a listed input; a follow-up commit re-inserted content-pinning phrases the
first split had dropped. Two count corrections rode along: the Phase 5 header (Four → Five, matching the
five numbered blocks the body already had) and the README example tag (`unresolved-failure-state` →
`stuck-state`, which now matches a real category row — a reference fix, not a regression).

## How this review was run

Run from a CLEAN context — a fresh reviewer that had not seen the change discussed, forming its own
independent read of the diff and both files, and instructed to adversarially BREAK the split (hunt for
a dropped clause, a broken reference, a drifted description). This dogfoods the clean-context review
rule this movement lands (INV-237). Meaning preservation was checked anchor-by-anchor across every
split: the architecture lens carries INV-122 (×2), INV-41, INV-74, INV-75, INV-233, INV-37 across its
seven sub-bullets; the cross-cutting-laws sweep carries INV-101, INV-150, P9, `tests/test_interface_coverage.py`,
`docs/lenses.md`; the edge-condition sweep carries INV-72, INV-30, INV-31, INV-141, INV-150, INV-138;
the paired-transition lens carries INV-126, INV-72, INV-4, INV-30, INV-31, INV-165. `docs/lenses.md`
resolves; SKILL.md sits under the 500-line ideal; the `description` frontmatter is unchanged.

## Findings

- **Orphaned mechanically-cut fragment (defect · folded).** `SKILL.md` paired-transition symmetry, the
  *inverse's magnitude* sub-bullet read `— And the half's magnitude question: where the pair rides a
  continuous quantity…`. The leading "And the half's magnitude question:" was a sentence cut from its
  original paragraph and pasted whole under a label that already names it — a dangling clause, the one
  readability artifact the split left. FOLDED: dropped the fragment so the sub-bullet reads
  `*the inverse's magnitude* — where the pair rides a continuous quantity…`. No meaning lost; the
  magnitude read survives.

- **README completeness list dropped the lifecycle sweep (recommendation · folded).** The old README
  prose named five things the sweeps check, including "a surface's full lifecycle from entry to return
  holds up"; the new five-bullet list re-split range/async into two and omitted the lifecycle sweep (the
  SKILL still carries all five sweeps). FOLDED: added the bullet "whether a screen's whole lifecycle
  holds from entry back to return" so the README summary shows the major sweep again.

- **Architecture-lens growth history dropped (recommendation · accepted).** The old lens carried its
  growth provenance (three → six → seven checks, ROADMAP 390, the tlvphoto validation 2026-07-09). The
  paragraph is gone. No anchor or behavioural clause was lost — the "seven checks" count and every INV
  reference survive — and de-historying SKILL prose is consistent with the pack's history→JOURNAL habit.
  Accepted; the history lives in JOURNAL and `docs/lenses.md`.

- **Paired-transition rationale trimmed (recommendation · accepted).** The "…reads to the human as a
  crafted-in and hard-out asymmetry" motivation and the "continuity half above shares the transition's
  craft" cross-note were dropped in the split. Explanatory, not load-bearing. Accepted.

- **Description and triggering (none).** The diff touches only body prose; the `description` frontmatter
  is unchanged. The trigger surface is untouched and no eval drift is expected.

- **Version stamp.** This record ships in the same push range as the reviewed edit and the two folds
  above; the 2.7.1 stamp is applied by `scripts/stamp-versions.py` and is exempt from this gate by
  construction.

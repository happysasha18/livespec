# Model comparison — pass 1 run twice, independently (Fable vs Opus), 2026-07-05

Same brief, same input (SPEC v0.8.1 at 15369ba), no cross-reads before both records existed.
Records: `pass1-prover-fable.md` (9 findings: 1 must-fix · 5 should · 3 worth) and
`pass1-prover-opus.md` (13 findings: 4 must-fix · 8 should · 2 worth, per its corrected tally).

## Where they agreed

- The single biggest defect, found by both as their top structural finding: the serial-lane rule's
  unstated scope (SPEC INV-2). Different attack angles — Opus reached it through the two-parallel-sessions
  lens and proposed the better FIX (the in-work row as the lane token); Fable reached it through the
  sharper EVIDENCE (the flagship's own journal records blessed parallel workers, so the spec forbade its
  authors' own practice). The fold used both halves.
- The stale derivation headers (matrix/architecture citing SPEC v0.7.x under v0.8 content) — found by
  Fable, by Opus, and by the matrix pass independently; a three-way consensus, folded with a standing
  re-pin rule in M-1.
- The worker seam as a weak area (Fable: ownership/fence inheritance; Opus: no escalation path;
  composition pass: session-scope invisible to workers) — three adjacent holes in one cluster, now one
  owned queue row.

## Where they differed

- Opus found three real holes Fable missed or under-called: the parked-resume vs quick-win-bubble race
  (two rules claiming the same freed lane), the INV-1 "never deleted" vs M-1 "queue pruning" direct
  contradiction (Fable likely suppressed it by KNOWING row 30 already queued the archive rule — knowledge
  of the debt masked the doc-level contradiction), and harvest atomicity (Fable saw it and wrongly waved
  it through as "reasonably atomic"; Opus showed the duplicate/lost-wish crash window). All three folded.
- Fable found four Opus missed: the E-16 "outside any project repo" sentence that the imminent row-52
  flip would land against (the most time-critical catch of the night — it gates the very next landing),
  the loader-thinness liveness gap (nothing keeps the loader thin AFTER the flip), the absorbed-wish
  dead path (superseded-into-a-wish that is later declined), and the attic second-collision (Opus caught
  the inbox sibling of the same class; together they made the class finding).
- Severity calibration: Opus ran hotter (4 must-fix vs 1); at triage each of its four was a one-sentence
  fold, so the heat cost nothing here, but on a noisier doc it would inflate the gate. Fable's counts were
  the more conservative read of the same material.

## What this says for the budget split (the question the sample was run for)

On a document-review pass carried by a strong skill scaffold, Opus was fully sufficient — denser output,
sound must-fix judgment, and the best single fix proposal of the night. Fable's distinct edge showed
exactly where the budget plan predicted: cross-document, cross-time judgment (connecting a spec sentence
to a flip that hasn't happened yet) and severity restraint. Recommendation: keep audits/reviews of this
class on Opus; spend Fable on fold triage, spec wording, and the seams between documents and plans —
which is the split already written in the roadmap.

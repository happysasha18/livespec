# Prover cross-link — SPEC humanize batch: "When the workshop itself misbehaves (the problem ledger)" (2026-07-07, session 25)

Register rewrite of one scenario section. Fact table built from `git diff SPEC.md`, not the new prose
alone. Mechanical gates green before this record: every tested phrase re-matched section-scoped (14/14,
`needle-extract.py --verify`); bracket-code multiset identical to the captured baseline (16 codes incl.
[B-2, B-3] which wraps across a line — captured on the whitespace-flattened section, none added/dropped,
all trailing); full suite 175 green.

## Fact table (old claim → new carrier → verdict)

| # | Old fact / code | New carrier | Verdict |
|---|---|---|---|
| 1 | Workshop noise ≠ product bug (flaky harness, missing dep, shell eats command, tool times out); retry-and-move eats the same minutes repeatedly | opening list of four noise kinds + the repeat-cost sentence | KEPT |
| 2 | Problem ledger = host's dynamic list; one git-tracked file `.live-spec/PROBLEMS.md`; only checkpoints stay ignored in `.live-spec/` [E-8]; born on first entry | "**The problem ledger** … `.live-spec/PROBLEMS.md` … only the checkpoints stay ignored [E-8] … born on its first entry" | KEPT |
| 3 | Entry = signature (short greppable phrase, two examples) + dated occurrences + status; four statuses WATCHED/OWNED/AGREED NON-PROBLEM/SOLVED with their meanings [E-24] | **signature** defined, both examples kept, four statuses as a list, [E-24] trailing | KEPT |
| 4 | The walk: grep for signature; not-listed → WATCHED line replaces silent retry, never takes the lane, product defect → bug lane [T-9] | three-item list, item 1; "silent retry" and "bug lane" verbatim; [T-9] trailing | KEPT |
| 5 | Listed → second occurrence gets owner THAT MOMENT: queue row or human's dated agreed non-problem; verdict human's alone [INV-9]; agent recommends+writes owner, ask rides batched report [INV-4, E-22], lane never stalls | item 2; "second occurrence", "queue row", "agreed non-problem" verbatim; [INV-9], [INV-4, E-22] trailing | KEPT |
| 6 | Third recurrence no owner = method defect; leaves host as wish to pack queue, one inbox file [E-11, INV-10], citing signature+dates [INV-23] | item 3; codes trailing | KEPT |
| 7 | After owner: entry only collects dates; recurrence on OWNED/AGREED appends its date, changes nothing else; re-raising an agreed non-problem is human's move; closing landing flips to SOLVED same session, no wait for audit | dedicated paragraph; "appends its date" verbatim | KEPT |
| 8 | A limping thing never dams the flow: known owned problem PARKED not orbited; ledger line/row/expected-red note holds it; unrelated lanes keep rolling; human's 2026-07-07 principle | "**A limping thing never dams the flow.**" verbatim; principle rendered in plain English + date (Russian quote dropped per English-gate); no new quote added | KEPT (quote→paraphrase, intended) |
| 9 | Two teeth: (a) hand-fix loops cap at two-strikes, second occurrence buys owner never another hand-pass; (b) owned defect serviced in BATCH, silent fence-fix, one append at session end, never a per-instance ceremony; clock-drift-10× story | two-item list + the story trimmed to one sentence; "serviced in BATCH", "never a per-instance ceremony" verbatim | KEPT |
| 10 | Real NEW bug still preempts [T-9]; law governs KNOWN limp [INV-56] | kept, both codes trailing | KEPT |
| 11 | Seams: write-ownership (sessions write; worker via checkpoint unless brief names ledger [ACT-3]); concurrent-edit fence [INV-11]; same-problem by grep+eyes, short signatures, merge at compaction; SOLVED/agreed → ARCHIVED tail at compaction [M-1], one home, bounded; product-vs-workshop seam (product bug re-doors to feature) | six labelled paragraphs; every code trailing | KEPT |
| 12 | No visible surface → facets N/A | "**Facets.** … facets are N/A." | KEPT |
| 13 | Non-goals: no mechanical guardrail yet (pre-push cross-milestone-unowned check earns row after usage); no automated signature matching; foreign-host ledgers open from own windows, this landing opens pack's own | three-item non-goals list | KEPT |
| 14 | Success measure: next hiccup lands as ledger line not silent retry, checked at milestone audit [default] | "**Success measure.** … instead of a silent retry, checked at the milestone audit [default]." | KEPT |
| 15 | Skill-search: two triggers. SETUP (founding/adoption orient, beside founding questions [B-2, B-3]) → scan installed skills + reachable catalogs for kind+crafts match, propose fit list + recommendation, human picks | dedicated paragraph, [B-2, B-3] trailing | KEPT |
| 16 | STRUGGLE (ledger second occurrence [INV-23], taste artifact rejected twice [INV-62 kin], returning failure family) → next attempt waits one search; found skill adopted or rejected BY NAME, verdict recorded where struggle lives | paragraph; "adopted or rejected BY NAME" verbatim; codes trailing | KEPT |
| 17 | The five-review-rounds origin story (public checklist carried it for months; search cost a minute) (promoter, stop-slop, 2026-07-07) | one-sentence paragraph, attribution kept | KEPT |
| 18 | Borrowing practice: invoke found skill as it ships; paraphrase folded lessons + credit source; verbatim text travels only under its license, notice kept, never republish unlicensed [INV-65] | list of three; "verbatim text travels only under its license" verbatim; [INV-65] trailing | KEPT |

## Anchor→sentence pairing spot-check
- [T-9] both occurrences still trail (a) the not-listed / bug-lane clause and (b) the "real NEW bug still preempts" clause.
- [INV-56] still trails the KNOWN-limp governance clause.
- [B-2, B-3] still trails the SETUP founding-questions clause.
- [default] still trails the success-measure sentence.

## Wording changes worth naming (meaning intact)
- The human's principle, previously a Russian quote, is now plain English with its date. This obeys the
  English-only / paraphrase-quotes doc rule; no fact lost, no new quotation introduced.
- Passive→active and one-idea-per-sentence throughout. The single dense "seams" paragraph became six
  labelled paragraphs; the non-goals became a list. No fact added or dropped.

Verdict: **CLEAN.** Every fact, status, rule, seam, non-goal and the success measure carried; 14/14
tested phrases section-scoped; 16-code multiset identical; suite 175 green. No must-fix.

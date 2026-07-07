# Prover cross-link — SPEC humanize batch: "One rulebook behind the skills" (2026-07-07, session 25)

Register rewrite of one scenario section. This section carries NO tested-literal phrases (needle-extract
`--list` returns 0), so the safety rests on the bracket-code multiset + the fact table below, built from
`git diff SPEC.md`. Codes: 6 distinct ([D-4], [E-12], [E-13], [INV-13], [M-1], [INV-66]), identical to
baseline, none added/dropped, all trailing. Full suite 175 green.

## Fact table (old claim → new carrier → verdict)

| # | Old fact / code | New carrier | Verdict |
|---|---|---|---|
| 1 | Same working rules greet you in every skill: ask-never-guess; plain words + code trailing; one surface one name; one canonical home per fact; junior resumes from a checkpoint after cut-off | five-item bulleted list, all five rules recognizable | KEPT |
| 2 | Each skill used to carry its own near-copy; copies drift; two proofs: anchor convention told two ways; concurrent-edit fence only in adoption text though every shared-file writer needs it | opening paragraph keeps both proofs, one clause each | KEPT |
| 3 | Shared rules live once in the base skill; folder `live-spec-base`; package-is-source, standalone repos read-only mirrors [D-4]; base states rules next to package default settings [E-13] | "**So the shared rules live once, in the base skill.**" + `live-spec-base` + [D-4] + [E-13] trailing | KEPT |
| 4 | Each working skill opens with one line naming base skill + base version written against; pin swept same session that bumps base, never stale; references not restates | dedicated paragraph, all four facts | KEPT |
| 5 | Skill elaborates only own domain (communicator teaches HOW to speak plainly; THAT we speak plainly is base's); standalone skill still stands, pointer reads as plain advice, no dependency [E-12] | paragraph; split of duties stated as two plain sentences (no scissors); [E-12] trailing | KEPT |
| 6 | One normative home per shared rule; a second full statement is drift to fold; restatements older than base pruned at milestones via compaction pass [M-1] skill by skill, never one risky rewrite [INV-13] | "**A shared rule has exactly one normative home…**"; [M-1] and [INV-13] both trailing | KEPT |
| 7 | List-parity: every place listing skills names the same complete set; list lives in working-skills sentence, closing lists, README table; drifts (communicator closing list named four after pack passed six, 2026-07-07, worker's halt surfaced it, two missing since birth); checked mechanically every commit, short list red [INV-66] | final paragraph keeps every fact incl. the four-after-six story and the date; [INV-66] trailing | KEPT |

## Wording changes worth naming (meaning intact)
- The duties split ("communicator teaches HOW … THAT we speak plainly is the base's sentence") is now two
  plain sentences describing who owns which rule, with no dash-contrast.
- Passive→active; the five rules pulled out into a list. No fact added or dropped.

Verdict: **CLEAN.** Every fact carried; 6-code multiset identical; no tested phrase to break; suite 175 green.

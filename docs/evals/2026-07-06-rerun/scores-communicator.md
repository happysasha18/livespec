# Scores — communicator re-run (2026-07-06)

Two isolated Sonnet workers, one per arm (bare: zero tools before the write; with-skill: read
`skills/communicator/SKILL.md` in full first). Verbatim outputs in `bare-communicator.md` and
`with-skill-communicator.md` in this directory.

| # | Criterion (the skill's promise) | Bare | With-skill |
|---|---|---|---|
| 1 | Plain product words, no dev jargon walls | MET BARE — plain throughout | MET — plain throughout |
| 2 | The map as a map: status icons (✅/🙋/⬜), one substance clause per line | RED — plain bullet list, no icons, no explicit map | MET — ✅✅✅🙋 icons, each line carries its own substance clause |
| 3 | The one decision asked cleanly, recommendation marked | MET BARE — "I'd lean toward urgency" reads as a clear pick, asked as one question | MET — "My pick: by urgency (recommended)" explicitly marked |
| 4 | No internal bookkeeping as message content (version numbers, "64 green" as content) | RED — "64/64 tests passing" and "version 0.9.16" both stated as content | MET — "saved on my end... sitting on your green light" — no version number, no test count |
| 5 | Row numbers trail, never lead | MET BARE — row numbers never appear at all, so none lead | MET — every row number trails in parentheses after its clause |
| 6 | NEW — row 16 (evidence panel) named with its pipeline STATION (spec → prove → architecture → matrix → tests → code → verify → landed) | RED — "basically done," no station named at all | RED — "built out through the spec, paused there" gestures at a station word but doesn't read as a station marker; a producer can't tell this names a step in a sequence rather than an offhand phrase, and it isn't put in the plain-words-lead / station-trails-in-parens shape rule 6 asks for elsewhere |

## The honest read

Criteria 1, 3, 5 land for both arms this round — the bare arm's plain language and clean single-question
ask were already solid, so the skill's edge here is real but narrower than the icon-map and
bookkeeping criteria suggest. Criteria 2 and 4 replicate the prior run's finding cleanly: bare ships an
undifferentiated bullet list and lets "64/64 tests passing" / "version 0.9.16" do the talking; with-skill
produces an icon map and keeps bookkeeping out of the message entirely.

Criterion 6 is the new one this round, and neither arm actually meets it. The bare arm doesn't attempt a
station at all. The with-skill arm attempts one ("built out through the spec, paused there") but the
phrasing doesn't do what rule 9's "departures board" language promises — a producer reading "built out
through the spec" has no way to know that's a pipeline stage rather than a stray word, and the skill's own
rule 6 (plain sentence carries the meaning, the code only trails as a quiet anchor) wasn't applied to the
station name the way it's applied to row numbers two lines above it in the same message. This is a real
gap worth fixing at the skill level, not a scenario-wording issue this time: rule 9 names the station
vocabulary but doesn't give a worked example of how to say "held at station X" in plain words the way it
does for other rules (see the "Live examples" section) — the next skill revision should add one.

## Run 2 (after the rule-9 example fix)

Fresh isolated Sonnet worker, with-skill arm only, re-reading the amended `skills/communicator/SKILL.md`
(rule 9 now carries the worked example: "🙋 evidence panel — the spec sentence is written, your sort
answer decides how it moves on (station: spec done, prove next)"). Verbatim output in
`with-skill-communicator-2.md` in this directory.

**Criterion 6 — GREEN.** The row-16 line reads: "Evidence panel — the design is written; your
sort-order answer decides if it moves on to review (station: spec done, prove next)." This now matches
the shape rule 9's fix asks for: a plain-words sentence carries the meaning on its own ("the design is
written; your sort-order answer decides if it moves on to review" — a non-technical reader can place
this as "drafted, waiting on you before the next check happens"), and the pipeline vocabulary
("spec done, prove next") only trails in parentheses as a quiet anchor, exactly like the row number two
words later. This is the fix working: last run's "built out through the spec, paused there" gestured at
a station without landing it; this run's line does the same job the worked example does — plain
sentence leads, station name trails — so the map line actually informs a phone-reading producer instead
of reading as an offhand phrase.

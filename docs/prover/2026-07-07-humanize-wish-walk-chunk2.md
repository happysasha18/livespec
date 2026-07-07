# Prover cross-link — SPEC humanize: "Throwing a wish" CHUNK 2 (2026-07-07, session 25)

CHUNK 2 = three bold-leads: A wish hears itself land (the departures board) · Every wish is also PLACED
on the product's map · The outcome does the talking (names chosen plain). Lines 83–142 of the section.

Gates (whole section, after splice): 157/157 tested phrases preserved section-scoped; code multiset
identical to baseline (165 occurrences / 86 groups, zero diffs); full suite 175 green. Chunk 2 carries 21
tested phrases and ~10 code occurrences, all preserved (incl. the verbatim pipeline-station chain
"spec → prove → architecture → prove architecture → matrix → test → code → verify → commit & show" +
"plus the terminal landed").

## A splice error the gate caught (worth recording)
The first splice used the wrong end-anchor (the passport bold-lead two paragraphs further down) and so
DELETED the "report law is walked" and "work is narrated" paragraphs. The whole-section verify flagged it
at once — 5 dropped phrases, code total 165 → 155, suite red. Reverted with `git checkout SPEC.md` and
re-spliced with the correct end-anchor ("The report law is walked, not remembered."). Nothing bad was
committed. This is exactly what gating every chunk against the whole-section baseline is for.

## Facts carried in chunk 2 (all KEPT)
- Departures board [INV-27]: intake line spoken back (heard · door · name · row number); silent wishes
  echo in the next report; every in-flight feature named with its pipeline STATION (the nine-step chain +
  plus the terminal landed); landed is a state not a step; his 2026-07-05 word paraphrased; the echo also
  carries the map place [INV-37].
- PLACED on the product's map [INV-37]: spec sections + architecture nodes ARE the feature map [E-14];
  three verdicts pulled into a list (changes an existing feature / a new feature / restructure — the
  modular-architecture moment paraphrased); A restructure verdict never re-carves in passing, queues its
  own row, re-carve walks the architecture step [E-14]; bug placement = the feature it repairs; uncallable
  feature asked [INV-12]; `map:` note greppable [T-14 kin]; his 2026-07-06 out-of-the-box word paraphrased.
- The outcome does the talking [INV-28]: the reader-failed board (bad coined titles translated to English
  as the negative example); NAMING (descriptive, never a private metaphor); LINES (open with what changed,
  narration lines [INV-35], internal handles trail, one fact = one standalone sentence); Bookkeeping
  numbers are handles too, the never-list (test count / suite size / version string / check tally never
  message content; tested clean / saved / the method held), the asked-substance carve-out pins method
  version [INV-25]; the chat-law hook `scripts/chat-law-hook.sh` reminds, never legislates.

## Wording changes worth naming (meaning intact)
- The three map verdicts and the naming/lines/never-list pulled into lists/labelled sentences.
- Four Russian/mixed quotes rendered as plain-English paraphrases with dates; the two bad example titles
  translated to English and kept as the negative example; no new quotation introduced.
- Long compound sentences split; required "never"/"not" tested phrases kept verbatim.

Verdict for chunk 2: **CLEAN** (after the caught-and-fixed boundary slip). Whole-section gates green.

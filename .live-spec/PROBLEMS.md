# live-spec — Problem ledger (`.live-spec/PROBLEMS.md`; SPEC E-24, INV-23)

The pack's own workshop ledger (dogfood; opened at the row-100 landing, 2026-07-05). The walk: grep for
the signature; not listed → one WATCHED line, keep working — never a silent retry. Listed → the second
occurrence gets an owner that moment (a queue row, or the human's dated AGREED NON-PROBLEM). A third
unowned recurrence goes to the queue as a METHOD defect. Owned entries only append dates; the landing
that closes the row flips them to SOLVED; the milestone compaction archives below.

| Signature | Occurrences (dates) | Status | Notes |
|---|---|---|---|
| zsh eats a bare `===` echo separator | 2026-07-05 (session 7), 2026-07-05 (session 9), 2026-07-05 ~23:55 (session 11, fired once more before the verdict was read) | AGREED NON-PROBLEM [recommended 2026-07-05, still awaiting his INFORMED word: his 23:49 page-3 pick "non-problem" was withdrawn ~23:58 by his own "я не понял… потом разберемся" — an uninformed pick is not a verdict; plain-words explanation owed in the morning report] | shell glob behaviour, not ours to fix; standing workaround: separators are `---`, never bare `===` |
| invented-time stamps: files/entries dated tomorrow | 2026-07-05 (rows 95–97 intake), 2026-07-05 (session 8 re-sweep), 2026-07-05 ~23:15 (inbox file + tlvphoto prover record both dated 07-06) | SOLVED 2026-07-05 (row 103 landed: `test_no_future_dated_stamps`, red proven on a synthetic future file) | hand-swept twice, recurred anyway → mechanical owner landed the same night |

| invented-time stamps, TIME variant: same-day stamps written ahead of the wall clock | 2026-07-05 (session 8: "~23:55"/"00:05" written at 22:40 — JOURNAL:853), 2026-07-05 23:43 (session 10: "~23:50"/"~23:58"/"00:02" written at ~23:35–23:43; caught in-session, corrected against git), 2026-07-06 ~00:11 (session 11: queue/landing stamps "00:15"/"00:30"/"00:40" written at ~00:05–00:11 — elapsed time GUESSED again; caught at the journal step's `date` call, corrected; third occurrence on the owned entry — row 104 should bubble as a quick win) | OWNED row 104 | the date fence (row 103) can't see same-day times; owner: pre-commit check — an ADDED line stamping today with a time later than the commit clock goes red (not racy at commit time) |
| invented-time stamps, CHAT variant: a reply's leading [HH:MM] typed from feel, not the clock | 2026-07-05 23:47 (session 11 opener stamped [01:47]; caught at the first `date` call, corrected aloud) | WATCHED | rows 103/104 fence files and commits — neither sees chat; watch: read `date` before the first stamped reply of a session |

## ARCHIVED (moved here at each milestone compaction, dated)

| Signature | Occurrences (dates) | Status | Notes |
|---|---|---|---|

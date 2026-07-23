# feedback-intake — register rewrite notes (2026-07-22)

Register-only rewrite of `skills/feedback-intake/SKILL.md` (and a scan of `README.md`, which was
already clean and needed no change). Every rule, route, scope, force, and code anchor (INV-x, T-x,
E-x, S-x) is preserved; only the register changed.

## Counts

- **Scissors (contrast-by-denial) fixed: 1.** The only definitional contrast in SKILL.md was the
  "feedback *rather than* a wish" filter at the "When it fires" section; rewritten as a positive
  sentence plus a plain boundary sentence. README carried no definitional contrast — its only
  negatives ("Do not use it on…") are lawful directives, left as-is.
- **Lint findings fixed: 2.** Baseline `preshow-register-lint.py` on SKILL.md reported two
  `en-wish-door` hits (line 3 description, line 35 body). Both cleared. Final lint on both files:
  OK / exit 0.
- **Coined metaphor / poetic-compression / inflation fixes: 14 sites.**
  1. "the wish door" → "wish intake" (description, line 3)
  2. "the wish door owns that verdict" → "wish intake makes that verdict" (When NOT to fire)
  3. "walk wish intake: door, echo, row" → "walk wish intake: arrival, echo, row" (routing table)
  4. "travel the same road" → "follow the same route"
  5. "The seam between the two ledgers" → "What separates the two ledgers"
  6. "the SUBJECT" → "the subject" (drama caps)
  7. "wordless drops awaiting their question" → "wordless files still waiting for their question"
  8. "born on its first line, with a two-line header" → "begins with a two-line header"
  9. "appends take the pen" → "an append follows the concurrent-edit fence"
  10. "rides the measurement family" → "belongs to the measurement family — the pack's measurement
      skills" (grounded at first use)
  11. "the reading machinery" → "that reading work"
  12. "is reaped the way a harvested file is" → "is removed the same way a harvested file is"
  13. "CLOSES it forever" → "CLOSES it" (inflation)
  14. "wish route" → "wish intake" (one-name fix; see cold-read below — "wish route" was a second
      name I introduced in the scissors rewrite, corrected to the canonical term)
- **Long sentences split into short SVO:** the "When it fires" sentence (1 → 4), the "When NOT to
  fire" nominalization ("unsure whether a remark was handed in is answered by one plain question" →
  "When it is unclear whether a remark was handed in, one plain question settles it"), the `.draft`
  sweep sentence (1 → 3), the echo bullet (1 → 2).

## Cold-read rounds

- **Round 1 (fresh zero-context subagent).** Listed blocking + non-blocking stops. Nearly all
  BLOCKING findings were ungrounded *pack-vocabulary nouns* (wish intake, the queue / queue row, the
  inbox door + sweeping, decision/review pages, the archive / harvested row, host / assigned vs
  unassigned session). These have their defining homes in other pack skills and `live-spec-base`; a
  pack skill references them by design (one-home-per-fact), and the doc states it is "plain advice"
  only when used standalone. Grounding them here would duplicate other skills' definitions and
  expand scope — left as deliberate references. **One finding was in-scope and self-inflicted:** my
  scissors rewrite had introduced "wish route" as a second name for "wish intake" (a one-name
  violation). Fixed (item 14 above).
- **Round 2 (confirming read).** Re-read the full body; re-ran the register lint (OK on both files)
  and the tests that read the file (all green). No new blocking stop.

## Pins (tests/ and guardrails/ that pin fragments of SKILL.md)

Every pinned substring was **preserved verbatim** — no pinning file needed an OLD→NEW swap, and no
pinning file was edited. Where a *changed sentence* contained a pinned fragment, the fragment itself
survived intact:

| Pinning file | Pinned substring (kept) | Changed sentence around it? |
|---|---|---|
| tests/test_traceability.py (TestFeedbackIntake) | `WISH` `FIXED` `CLOSES` `FIELD EVIDENCE`; homes `queue row` `journal` `archive` `ledger` `problem ledger` | routing rows reworded (e.g. "CLOSES it forever" → "CLOSES it"); every pinned token kept |
| tests/test_traceability.py | `workshop noise` | row unchanged; kept |
| tests/test_traceability.py | `inbox sweep` | "When it fires" reworded; phrase kept |
| tests/test_traceability.py | `never on the agent's own output` (lowercased match) | kept |
| tests/test_traceability.py | `never opens a queue row on its own judgment` | NOT-fire reworded; phrase kept |
| tests/test_traceability.py | `one echo per item` `appends its date` `only the assigned session` | echo/ledger lines reworded; phrases kept |
| tests/test_traceability.py | channel headings, `FEEDBACK.md`, ledger-line parts (`when it arrived`, `who handed it in`, `which channel`, `what it concerns`, `where it went`) | unchanged; kept |
| tests/test_inbox_deposit_protocol.py | `INV-249` `.draft` | `.draft` sweep sentence split into 3; both tokens kept |

Not a pin on this file (verified): the two lint/judge tests that mention "wish door"
(`test_preshow_register_lint.py`, `test_register_judge.py`) pin their own fixture strings, not this
skill's prose — so removing "wish door" from SKILL.md does not touch them (both still green). The
`the home its route owns` pin (test_traceability line 993) is on `inbox/README.md`, not this file.
The `measurement family` pin (test_feedback_collector.py) is on the collector skill, not this file.

## Sentences left unchanged because rewriting risked meaning/scope

- The opening and closing **pack blockquotes** (the shared "Part of the live-spec pack …" boilerplate
  and the "The pack, whole:" footer): identical across every pack skill, carry base-rule references;
  reword would desync the pack and is out of register scope.
- The **pack-vocabulary nouns** the cold-reader flagged (wish intake, the queue / queue row, the
  inbox door, decision/review pages, the archive / harvested row, host / session, tripwire verdict,
  the feature map): defined in other pack skills / base; grounding here duplicates and breaks
  one-home-per-fact.
- **Force-caps** (ANY, ONE, IS, NEW) and **route-name caps** (WISH, FIXED, CLOSES, FIELD EVIDENCE):
  caps carry rule force; the route words are test-pinned. Lowercasing risks force/scope.
- "**the home its law owns**" / "**the home its route owns**" (intro): kept — plain enough, echoes
  the pinned inbox-README phrasing, and rewriting risked the one-home meaning.

## Verify verdict

- `preshow-register-lint.py` on SKILL.md and README.md: OK, exit 0 (both).
- Contrast grep (` — not `, `, not `, `rather than`, `instead of`) on both files: SKILL clean;
  README's only hits are lawful directive negatives ("Do not use it …").
- Tests reading this file — TestFeedbackIntake, test_inbox_deposit_protocol,
  test_preshow_register_lint, test_register_judge: all green.
- Three unrelated failures in test_traceability (TestSkillEvals, TestPackListParity,
  TestWorkerContract) target `text-audit` evals, build-pipeline's craft ladder, and pack-list
  parity — none read feedback-intake's prose; pre-existing to the in-progress spec-format migration.

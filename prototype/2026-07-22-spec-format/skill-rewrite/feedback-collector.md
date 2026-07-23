# Register rewrite — feedback-collector skill (2026-07-22)

Scope: register only. Every rule keeps its meaning, scope, and force. Code anchors, the
frontmatter description's trigger semantics, and base-rule number references were left intact.

Files changed:
- `skills/feedback-collector/SKILL.md`
- `skills/feedback-collector/README.md`

## Counts

- Contrast-by-denial (scissors) fixed: 7
- Metaphor / poetic-compression fixed: 3
- Ungrounded-term fixed (from cold-read, blocking): 1
- Register-lint findings fixed: 0 (file passed `preshow-register-lint.py` at baseline and after;
  the pattern list flagged nothing in either file, before or after)

## Scissors fixed (contrast-by-denial → positive statement)

1. SKILL "When NOT to fire" bullet
   OLD: `a moment the human hands in as ordinary feedback (that is feedback-intake's, not this arm's).`
   NEW: `a moment the human hands in as ordinary feedback (feedback-intake owns that route).`

2. SKILL disjoint-work paragraph (also split one tangled sentence into three)
   OLD: `The one moment the human HANDS the reaction in (a comment on shown work), feedback-intake logs its field-evidence ledger line and this arm, if the moment reads as strong, offers the upstream note — the two do disjoint work, they do not compete (\`PRODUCT_SPEC.md\` E-30, T-20 route 4).`
   NEW: `When the human HANDS the reaction in — a comment on shown work — the two skills do separate parts of the work. feedback-intake logs its field-evidence ledger line. This arm, if the moment reads as strong, offers the upstream note (\`PRODUCT_SPEC.md\` E-30, T-20 route 4).`

3. SKILL consent paragraph (positive definition first; boundary to INV-31 in its own sentence)
   OLD: `Consent here is **positive word, asked every time** — the deliberate opposite of the pack's silence-is-consent default (\`INV-31\`), because this is an outbound move about a real person.`
   NEW: `Consent here is a **positive word, asked every time**: the note is written only on an explicit yes. The pack's usual silence-is-consent default (\`INV-31\`) does not apply here, because this is an outbound move about a real person.`

4. SKILL "distilled" bullet
   OLD: `**distilled** — the point of what happened, not the raw material; never the transcript, ...`
   NEW: `**distilled** — the point of what happened, and only the point; never the transcript, ...`

5. SKILL "courteous private request" bullet
   OLD: `**a courteous private request** — shaped for the authors, never for a public audience;`
   NEW: `**a courteous private request** — shaped for the authors who will read it, and meant to stay private;`

6. SKILL "anonymized" bullet — `a law rather than taste` removed; em-dash runs split into
   sentences with colon-lists (see pins section for the pinned substrings preserved inside).
   OLD tail: `... An enterprise host is the reason this is a law rather than taste: a note that leaks an internal name is unsendable there, and a note masked after the yes is a different note from the one approved.`
   NEW tail: `... An enterprise host makes this a hard law: a note that leaks an internal name cannot be sent there, and a note masked after the yes is a different note from the one approved.`

7. SKILL outbox "cleared" bullet
   OLD: `**cleared once the human has delivered it** — the human's own step, not the pack's.`
   NEW: `**cleared once the human has delivered it** — a step the human owns.`

## Metaphor / poetic-compression fixed

1. SKILL intro: `The pack has three arrows.` → `The pack moves feedback in three directions.`
2. SKILL "What it is not": `Opposite arrows.` → `Opposite directions.`
3. README: `It is the third arrow of the pack's exchange.` → `It is the third of the pack's feedback directions.`

## Ungrounded-term fixed (cold-read blocking finding)

SKILL "When it fires": the referent "the lead" was never introduced anywhere in either file.
   OLD: `It fires at the tempo of the lead's own occasional surfacing: rare by design, on a clear signal, and silent on a mild or routine reaction.`
   NEW: `It fires rarely by design: on a clear signal, and silent on a mild or routine reaction.`
Meaning preserved: the firing tempo (rare, clear-signal-only, silent on mild) is stated directly.

## Pins recorded

Grepped `tests/` and `guardrails/` for distinctive fragments of every changed sentence.
Findings:

- **test_collector_anonymization.py — REAL assertions (pinning substrings inside the "anonymized"
  bullet).** The bullet was rewritten around them; the pinned substrings were preserved exactly, so
  no break. Do not edit the test.
  - asserts substring `masked before the note leaves the draft` — preserved verbatim in NEW text
    (`the host's real entities are masked before the note leaves the draft (SPEC INV-179).`).
  - asserts substring `part of the draft the user reads at consent` — preserved verbatim in NEW text
    (`The masking is part of the draft the user reads at consent, so ...`).
  - asserts substring `anonymized` — preserved.
  - Full OLD bullet:
    `- **anonymized** — the host's real entities are masked before the note leaves the draft (SPEC INV-179): a person's name, the company or client, an internal product or repo name, a file path, a customer's data — each becomes a neutral role word ("the owner", "a client project", "an internal repo"), and the masking is part of the draft the user reads at consent, so what they approve is exactly what would travel. The pack's own public names (skill names, invariant codes) stay. An enterprise host is the reason this is a law rather than taste: a note that leaks an internal name is unsendable there, and a note masked after the yes is a different note from the one approved.`
  - Full NEW bullet:
    `- **anonymized** — the host's real entities are masked before the note leaves the draft (SPEC INV-179). A person's name, the company or client, an internal product or repo name, a file path, a customer's data: each becomes a neutral role word ("the owner", "a client project", "an internal repo"). The masking is part of the draft the user reads at consent, so what they approve is exactly what would travel. The pack's own public names (skill names, invariant codes) stay. An enterprise host makes this a hard law: a note that leaks an internal name cannot be sent there, and a note masked after the yes is a different note from the one approved.`

- **Non-breaking echoes (test COMMENTS / DOCSTRINGS only, not assertions — no edit needed, none broke):**
  - `test_collector_anonymization.py:6` docstring: `are why this is law rather than taste.` — mirrors the
    phrase I removed from SKILL. It is a docstring, not an assertion; the real assertions are the three
    substrings above. Left untouched (it is the pinning file's own prose, and it is not an assertion).
  - `test_feedback_collector.py:33-34` + `:39` comments reference `the deliberate opposite of
    silence-is-consent [INV-31]`. These are comments; the real assertion is `assert "inv-31" in s`.
    The `INV-31` anchor is preserved in the rewritten consent paragraph, so the assertion still passes.

No fragment of any changed sentence appeared in `guardrails/`.

## Cold-read rounds

- Round 1: fresh zero-context cold-reader over both files. One BLOCKING finding: `the lead` (ungrounded
  referent) — fixed (see above). All other stops were pack-internal vocabulary the file's real readers
  (pack agents) know: trailing codes (E-30/T-21/INV-*), sibling-skill names, "host", "measurement
  family" — non-blocking, and outside a register rewrite's remit.
- Round 2: confirming read of the fixed region — reads clean, meaning preserved.

## Left unchanged because rewriting risked meaning or force

- **Frontmatter `description` (SKILL line 3)** — left entirely unchanged per the task (trigger semantics
  must stay). It carries the standard skill-description negative-trigger idiom (`NOT feedback-intake —
  that RECEIVES ..., this NOTICES ...`; `NOT a measurement machine — ... never scores or aggregates`),
  which is trigger-critical and is the lawful boundary form for a description.
- **The "What it is not" section (SKILL) and README's "What it is not" section** — the `Not X` bullets
  are the lawful boundary-naming form (each boundary in its own labelled bullet, each opening with a
  positive statement of what the skill does). Kept as boundary statements; only `Opposite arrows` →
  `Opposite directions` changed within.
- **`outbox/ never rides a push; a private note must not travel with the repo` (SKILL gitignored
  bullet)** — a plain rule/boundary (states the gitignore consequence), not a definitional contrast.
- **The threshold adjectives** (`genuinely strong`, `unmistakable`, `real delight`, `real hurt`,
  `conservative floor`) — meaning-bearing calibration of the firing bar, not decoration; left as-is.

## Verification

- `preshow-register-lint.py SKILL.md README.md` → OK (clean), both files.
- Scissors re-grep (`— not` / `, not` / `rather than` / `instead of` / `opposite`): remaining hits are
  the exempt frontmatter description and the lawful "What it is not" boundary sections only.
- `pytest tests/test_feedback_collector.py tests/test_collector_anonymization.py` → 9 passed.

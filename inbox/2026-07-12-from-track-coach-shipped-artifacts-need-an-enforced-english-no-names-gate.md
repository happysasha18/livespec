# Wish: shipped artifacts need an ENFORCED English + no-personal-names gate, because the rule rotted

**The item.** The rule already exists — chat speaks the user's language, but the spec, README, skill card,
and code that ship are English, and they carry no personal names. Nothing ENFORCED it on the way out, so it
rotted silently. Across track-coach's whole build (2026-07-12 audit) the shipped repo had accumulated ~138
personal attributions in the spec, ~23 in the matrix, and ~82 lines of Russian or a personal name inside
code comments and docstrings, plus two Russian section headings — none caught until a human read it months
later. A stated rule with no gate is a rule that decays one un-reviewed commit at a time.

**Why it matters.** Shipped artifacts are the product's face to everyone — contributors, auditors, users. A
language or a name that reads as "one person's private project" narrows a thing meant to be everyone's. The
existing "docs are English / impersonal" guidance lives as prose a session may or may not honour; it needs
to be a check that a change cannot pass without meeting.

**The gate proposed.** The publish gate (and ideally a fast pre-commit lint) refuses a shipped artifact that
carries: any Cyrillic outside a user-language string the program deliberately emits; any owner/personal name
("Alexander", "Sasha", …) in spec / README / skill / code comments; a coined non-English metaphor where a
plain English term belongs. It reports each offending file:line so the fix is mechanical. Attribution and
candid Russian process-notes stay in the local-only diaries (JOURNAL / NEXT_STEPS), never in the shipped
tree. This composes with the impersonal-spec wish already filed (2026-07-12): that one states the voice,
this one makes a machine hold the line.

**Who throws it.** The track-coach Mac window, 2026-07-12 ~09:54, on Alexander's word
(«вроде бы мы просили не оставлять русского»).

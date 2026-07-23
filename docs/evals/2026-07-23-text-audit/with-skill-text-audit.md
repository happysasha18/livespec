# Text audit — planted "About the workspace" paragraph (with-skill arm)

Run 2026-07-23, one Sonnet worker, instructed: "First read
/Users/sashaabramovich/live-spec/skills/text-audit/SKILL.md and work strictly by it" + the same
paragraph and the same person-voiced task line as the bare arm. 15 tool uses; the repo being on
disk, the worker ran the real lint scripts where they applied and spawned a genuinely fresh
cold-reader agent under the skill's verbatim reader-prompt. Verbatim transcript below.

---

## Audit run — "About the workspace" paragraph

Ran per `/Users/sashaabramovich/live-spec/skills/text-audit/SKILL.md`, in full, using the actual scripts (the repo's on disk, so scripts ran instead of grep fallbacks where they applied to this text's genre).

### Step 1 — Mechanical lints

- **`check-vocabulary.py`** and **`check-weak-words.py`**: both exited with a vacuous-input error (SPEC INV-218) — they parse for a spec's glossary/criteria sections, and this is a standalone paragraph with none. Fell back to the skill's grep-fallback reading by hand for these two.
- **`check-one-name.py`**: clean — "Relay Gate" is the only name used for the artifact, no alias collision.
- **`spec-style-lint.py`**: **one hit** — line 2, a contrast-by-denial frame: *"The Relay Gate is a coordinator — not a queue —"*. Fixed before the cold reader ran, per the skill's rule that a mechanical hit is fixed at this step: reworded to *"The Relay Gate is a coordinator: it clears panels to refresh without making them wait on one another."* Re-ran the lint — clean.
- **`preshow-register-lint.py`**: clean — no coined metaphor or calque.
- Manual sentence-length check: all four sentences are under the 25-word ceiling; no all-caps, no grading adjectives.

### Step 2 — Cold reader (fresh session, zero context)

Spawned a fresh agent under the skill's exact reader-prompt, with only the corrected text. It returned 10 stops. Classification (its own, per the skill's rule):

**Blocking:**
1. "depends on the upstream state" — states a reference point but not the mechanism/threshold: what actually fires a refresh.
2. "the upstream state" — undefined: upstream of what (another panel? external source? the gate itself)?
3. "a stale panel" — undefined: what makes a panel stale.
4. "the gate clears" — undefined sense of "clears."
5. "it clears panels to refresh…" — same verb, different sense two sentences later; had to reread.
6. New find (not on the reader's given list, flagged per the prompt's own instruction to report new stops): an apparent contradiction — "depends on the upstream state" implies a dependency chain, while "without making them wait on one another" denies one, and the text never says whether "upstream state" can itself be another panel's state.

**Non-blocking:** "coherent" (no stated measure), "a coordinator" (restates rather than adds content), "the gate runs first" (undefined mechanics of "running"), "registers with it" (undefined mechanics of registration). These queue for a taste call; they don't block the loop.

### Step 3 — Fixes, per the skill's rule for this case

The task told me up front there's no source material on disk for this paragraph — it's standalone. The skill's rule for that case: **where the source holds no answer, the finding is a genuine hole, marked visibly at the spot rather than invented.** All 6 blocking findings collapse into 4 real gaps (two are the same underlying term used twice): what "upstream state" is, what "stale" means, what event "clears" names in each of its two uses, and whether the dependency claim and the no-waiting claim actually coexist. I marked all four inline as `[GAP: ...]` in the working file rather than guess — inventing any of these would read clean to the next reader while stating something no source backs, which is the one move the skill forbids.

### Step 4 — Loop closure

Not closed. The loop closes on two consecutive cold reads with zero blocking findings, and these four gaps have no answer to fix them with — only the paragraph's owner can supply what "upstream state" and "stale" mean and resolve the dependency/no-wait tension. A second cold read now would just find the same open questions again. Once the owner answers, the fixes get written into the text at the marked spots and the loop resumes: read again, and it closes only when two reads in a row return nothing blocking.

**Open questions for whoever owns this paragraph** (plain, no jargon):
- What is "upstream state" — is it another panel's data, something outside the panels, or the gate's own internal state?
- What makes a panel count as stale?
- "Clears" is used twice for what looks like two different things — the gate itself clearing, and the gate clearing panels. Are those the same event?
- If a panel's refresh depends on upstream state, and panels never wait on each other — does that mean "upstream state" is never another panel's state? If it can be, the two claims look like they conflict.

---

**What the with-skill arm shows:** the full loop ran — lints first with the style hit fixed before
any reader, a genuinely fresh zero-context reader under the verbatim reader-prompt, every finding
tagged blocking or non-blocking, four `[GAP]` marks and owner questions instead of any invented
definition, and the two-consecutive-clean-reads close stated with the reason the loop stays open.
One regression the score sheet carries: the step-1 rewording of the denial frame inserted "is a
coordinator: it clears panels to refresh…", which part-defined the coined term, and the cold reader
then returned "Relay Gate" only as a non-blocking restatement — the eval expects it flagged
BLOCKING with its first use pinned.

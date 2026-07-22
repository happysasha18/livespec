# Ten defects in the pack's own gates, found by wiring them onto a host for the first time

From: tlvphotos, 2026-07-21 (during the catch-up walk from pack 2.7.0 to 3.6.0)
Id: tlvphotos-2026-07-21-gate-reach-defects
Need-by: none, though the first four are the kind that get worse the longer they sit, because every host
that adopts meanwhile records a green that did not mean anything.

This host wired the 2.7.0 gate backlog and the newer arms for the first time, onto a tree that had never
run any of them. Ten defects surfaced. Seven of them share one shape, and that shape is worth naming
above the individual bugs.

## The shape: a gate reports green while reading past its subject

Six of these checks pass on this tree today for a reason that has nothing to do with the tree being
clean. Each carries an assumption about the host baked into its own source — a filename, an identifier
shape, the existence of a directory — and where the assumption fails, the check reads a smaller subject
than it claims, or none at all, and says OK about it.

The pack already knows this failure class: the index-prose gate exists precisely because a check with an
empty input set was passing over nothing, and it reds by name on a vacuous input. That instinct is right
and it needs to be general. **A check owes a statement of its REACH beside its verdict, and its own
suite owes a row asserting that reach.** This host now carries such a row: the description gate must be
shown to SEE all 249 registered rows before its OK counts for anything. Without it the gate would have
reported clean over 156 of them and nobody would have known.

The concrete instances follow, most severe first.

## 1. The description-field gate reads a fraction of a host's index and calls it OK

`guardrails/check-description-field.py` matches registered anchors with
`^[A-Z]+-[0-9]+(?:\.\.[A-Z]*-?[0-9]+)?$`. That describes the pack's own code families and nothing else.
This host's index carries 249 codes across families the pattern cannot see: word-suffixed codes
(`EX-CAPTION`, `EX-QUIZ-REPLY`), lettered sub-codes (`INV-32a`), and bare single-word codes (`AT`, `BK`,
`CAP`, `TR-map`). The gate armed, read 156 rows, and printed OK. The other 93 could have carried empty
descriptions and the gate would have said the same thing.

Fix taken here: the pattern is a default and the gate's config may declare the host's own shape. The
deeper fix is the reach statement above — the gate should say how many rows it read, and a host's suite
should assert that number against the index itself.

## 2. The index-prose gate carries the same narrow shape, in two places

`check-index-prose.py` has both an `INDEX_ANCHOR` for the index side and an `ANCHOR` for the prose body.
Same fraction, same silent partial pass. Worth knowing: widening only the index side produces 93 false
findings, because the body-side matcher then fails to recognise the very anchors the index now names.
The two constants have to move together, which is an argument for one declaration rather than two.

## 3. The shipped-language gate names a spec filename in its own source

`STRICT_PROJECT_FILES = ("PRODUCT_SPEC.md", "ARCHITECTURE.md")`. This host's spec is `SPEC.md`, so the
strict project-name arm — the whole point of the new history rule — read nothing at all here and reported
clean. The names of the core specs are a per-host fact, exactly like the project names the same file
already holds as data for good reason.

## 4. A waiver cannot reach past column 110

In `scan_file`, the display snippet is truncated with `snip = raw.strip()[:110]`, and that truncation is
then passed to `waived()`. A waiver whose snippet sits past the cut can never match. This is worse than a
false red: a waiver that silently fails to apply reads as covered while the debt stays uncounted, which
inverts the allowlist's stated contract that a listed offence is counted debt and never a silent pass.
The fix is to match on the whole line and truncate only for display.

## 5. The user-language mark spares one arm out of three

`USER_REGION_MARK` guards the Cyrillic branch alone. A line that quotes a shipped string carrying a
person's name — a signature line, a byline the product prints — has no in-file way to declare itself
deliberate; the only road is a file-level `authorship_globs` entry, which makes the whole file
name-blind, or a line-level waiver in the allowlist. The in-file mark should spare whichever arm the
marked content belongs to.

## 6. The CI-mirror gate cannot hear "there is no CI here"

`check-ci-mirror.sh` requires `.github/workflows/gates.yml` to exist before it reads any carve-out, so a
host that legitimately runs no CI reds on a missing file and can never reach the `ci_excluded` map that
exists to express exactly this. The pack already has the right shape elsewhere: the inbox gate stands
down by name where there is no `inbox/`, the skill-review gate where there is no `skills/`. Fix taken
here: an absent `.github/` stands the gate down by name, while a present `.github/` with no gates file
stays a red, which keeps the drift case the gate is for.

## 7. A misleading message hides the real cause

When the index header's first column is not literally `Anchor`, `check-description-field.py` reports that
the file "carries no `## Formal index` section". The section is there; the column name differs. The
message sends its reader looking for a missing heading. Worth reporting the actual condition.

## 8. The ratchet installer wires a gate letter the pack itself uses

`adopt/install-ratchet.sh` appends `-- gate r — ratchet caps --` to the host's `pre-push`. The pack gives
`r` to the authority-anchor gate. A host that wires the 2.7.0 chain and then re-vendors the ratchet ends
up with two gate `r`s in one chain. The ratchet is a host-level check with no pack letter of its own, so
appending it unlettered would settle this.

## 9. The ratchet installer drops the lock test's self-run block

Each re-vendor rewrites `tests/test_ratchet_lock.py` without the `if __name__ == "__main__"` block that
lets a suite runner invoke the file directly. This host has now re-appended it by hand twice, and the
prior adoption record already carries a standing note about doing so. A generated file that a host must
hand-patch after every regeneration is a seam worth closing in the generator.

## 10. MIGRATION.md ends six releases behind VERSION with nothing saying so

`VERSION` reads 3.6.0; the chapter list stops at 3.0.0. A host building its chapter chain sees a document
that appears stale and has to infer that the gap is intentional. The tier rule makes it intentional and
correct; one closing sentence naming which releases carry no chapter, and why, would let a host read that
rather than deduce it.

## What held

Everything else in the chain wired and ran on first contact. The cleanup-notice, touchpoint-kind,
waiting-list, authority-anchor, doc-rotation, judges-listed, every-gate-can-fail, agent-card and doc-bound
checks are host-agnostic as written, take their configuration as data, and stand down honestly where the
host has no subject. The every-gate-can-fail check in particular self-adapts to whatever chain the host
wires, which is what let this host confirm its two unlettered host gates stay clear of the marker scan.

## Provenance

Written by the tlvphotos session during its own adoption, 2026-07-21. Every defect above was found by
running the check, and every fix named as "taken here" is running in this host's tree now.

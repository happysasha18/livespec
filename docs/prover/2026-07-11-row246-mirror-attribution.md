# Prover — row 246, mirror attribution stamp (2026-07-11)

Ran under **product-prover v1.0.0**, CROSS-LINK mode — the seams of the row-246 change
(the sync script now stamps the "made with live-spec" line onto the standalone mirrors),
read against the whole spec. Not a full whole-spec re-prove.

## Opening

The change is sound and does what INV-96 wants for the mirror case: the line is built once
from the live `VERSION` file and stamped on the two files a skill owes, README.md and SKILL.md,
rather than hand-written where it would go stale. The mechanism is idempotent, guards a missing
file, sits in the right place in the loop, and touches only the isolated scratch clone — no pack
tree contamination. The two new tests are real string pins and pass green (7/7 in the file). The
README bullet fixes match SKILL.md's actual content exactly. Nothing here blocks the change.

The two findings below are spec-text polish, not code defects: the INV-96 prose is written for a
FOREIGN built-with project, and the pack's own mirrors — which the script serves — satisfy the
intent while matching none of the clause's literal read-source / offer-mechanism phrases. Verdict:
**ready to ship; two should-clarify sentences would close the seam between the code and the clause.**

## Findings

| ID | Severity · label (formal) | Finding | Folded / rejected (+why) |
|---|---|---|---|
| F1 | should-clarify · boundary-issue (composition) | INV-96's mechanism phrases are all written for a foreign built-with project and none names the pack-self-mirror case the script implements. Sweep (base rule 14) found the class in three phrases: **(a)** the version is "read from the host's attach record at write time" (`PRODUCT_SPEC.md:776`, INV-index `:1730`) — the script instead reads the pack's own `VERSION` file (`scripts/sync-mirrors.sh:42`), correct because here the pack IS the project and it does not attach to itself; **(b)** "each built-with project applies the line through its own queue, the pack never writing foreign trees" (`:776`) — the mirrors are the owner's OWN repos rebuilt from the pack, written by the owner's own sync tool, so this is not a foreign-tree write, but the clause never says so; **(c)** "the walk says once when absent and proposes, the owner's word decides" (`:776`) — the script stamps unconditionally, correct because the OFFER is settled once at pack level by the owner who owns both pack and mirrors, but no sentence records that settlement. The spec text SUPPORTS the reading (intent = "the version the project runs", on the landing surface, owner-consented) but does not COVER the self-mirror mechanism. **Action:** add one sentence to INV-96 — the pack's own standalone mirrors carry the line stamped by the sync script from the live `VERSION` file, the offer settled once at the pack by the owner of both trees, distinct from a foreign project that offers through its queue. | **folded** — the sentence added to INV-96's prose (`PRODUCT_SPEC.md:776`) and a matching phrase to the index row (`:1730`), same session |
| F2 | should-clarify · internal-conflict (consistency) | The exact wording has one normative home — the publish floor (`skills/publish/SKILL.md:51`, canonical markdown `made with [live-spec](...) v<pack-version>`). The script now constructs the same string (`scripts/sync-mirrors.sh:56`). **Verdict: this is a mechanism APPLYING the wording, not a second normative home** — same status as the test's own hardcoded copy (`tests/test_made_with_attribution.py`), so it is NOT a one-home defect. BUT the reproduction is unguarded: nothing asserts the script's line EQUALS the floor's canonical form, so a future edit to the floor wording drifts the script silently, and the mirrors would then advertise a stale wording that the next rsync re-stamps. `test_sync_script_builds_the_line_from_the_live_version` pins the string literally in the script but not against the floor. **Action (either):** a test asserting the script's `ATTRIBUTION_LINE` matches the publish floor's canonical wording, or a `# wording home: skills/publish/SKILL.md` comment on `ATTRIBUTION_LINE` declaring it a reproduction. | **folded** — both: `test_script_wording_locksteps_with_the_publish_floor` added (M-225's owning cell updated) AND the wording-home comment on `ATTRIBUTION_LINE`, same session |
| F3 | worth-considering · hard-to-operate (ops-ux) | The `stamp_attribution` refresh branch (grep-found → `sed` replace, `scripts/sync-mirrors.sh:60-66`) is unreachable in normal operation: `rsync -a --delete` (`:114`) rebuilds every mirror file from the pack folder each sync, and no pack source file carries the line, so the `^made with \[live-spec\]` grep never matches and the append branch always runs. The branch is harmless and defensive for a future where a pack file ships the line, but is dead today — a later reader should not assume it is exercised. **Action:** none required; optionally a one-line comment that it guards a future pack-carried line. | **folded** — the one-line comment added on the refresh branch, same session; the defensive branch itself kept |

## What holds (checked, no finding)

- **Idempotence.** rsync rebuild + deterministic stamp reconstructs each file byte-identically when
  pack content and version are unchanged, so `git diff --cached --quiet` (`:156`) is true → "up to
  date", no empty commit. A version bump changes the stamped line → exactly one clean commit. Correct.
- **Missing SKILL.md.** `[ -f "$file" ] || return 0` (`:59`) skips a mirror with no SKILL.md silently;
  README always exists before the stamp (the banner block always writes one). Handled.
- **Ordering.** Both stamps run AFTER the banner block (`:150-151`), so the README footer sits below
  the banner and body; SKILL.md's appended `---` is an end-of-file horizontal rule, not frontmatter. Correct.
- **No pack contamination.** `git add -A` (`:155`) runs inside the isolated scratch clone `$mirror_dir`,
  never the pack tree; the script only pushes to mirror repos (`:20-21`). Clean.
- **M-225 row (`TEST_MATRIX.md:232`) internally consistent.** Fact cell now states the sync-script stamp
  on README.md + SKILL.md from the live VERSION; owning-test cell lists all five tests (3 prior + the 2
  new), all present and green (7/7 in the file); status BUILT is accurate.
- **README bullet fixes (`skills/product-prover/README.md:35-36`).** "Three review modes" and its
  full/cross-link/feature-fit descriptions match SKILL.md's Review-modes section (`SKILL.md:161-165`);
  "folded/rejected column" matches the persist-findings rule (`SKILL.md:358`). Sweep of the README found
  no lingering "two depths" or "resolved" wording.

## Readiness

Ready to build. No must-fix. Two should-clarify sentences (F1 self-mirror case in INV-96; F2 lockstep
guard on the reproduced wording) would close the seam between the shipped mechanism and the clause.

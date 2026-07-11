# PENDING ANALYSIS + APPLIER-READY DRAFT — row 247 (INV-112 / M-251)

Written 2026-07-12 by an Opus analyst preparing row 247's pipeline run. Not yet applied.
Next session: brief a Sonnet applier from the lettered blocks below (the row-233 draft is the shape).
Read live values before applying; the code-allocation and grant-URL notes inside are load-bearing.

---

## Verdict

Row 247 is **applier-ready as a small single-story law** for two of its three Done-when clauses.
The law is one new invariant (INV-112), one matrix row (M-251), three short prose homes, one
architecture edit, one profile grant line, and one scripted grant-ask. The delta is small and
draftable now. Two honest caveats ride it, stated under Done-when below: the exact grant URL is a
read-at-draft-time fill-in the drafter must copy from the live GitHub App settings page (never
guessed), and Done-when clause (c) — one real remote deposit landed — is a field-acceptance beat
the owner closes from his browser, which a local pipeline run structurally cannot produce.

The row's fourth point (GitHub Issues as a public repo's stranger door) is a separable story about a
different actor; the recommendation is to split it into its own follow-up row, not fold it here.

## The law in one sentence

The inbox door has a remote arm: a seat that reaches a repo only through git deposits one new file
in `inbox/`, commits it touching `inbox/` only with the source named, and pushes it under a per-repo
grant recorded in the host profile; a seat with no grant fails honestly, names the grant it lacks,
and hands the owner the one action that supplies it.

## Homes touched

- **PRODUCT_SPEC.md** — new remote-arm paragraph inside the inbox-law section (after line 1592), plus
  the INV-112 clause and its Formal-index row (Package repo section).
- **inbox/README.md** — one sentence after the commit rule (line 15), the door's own mechanics home.
- **adopt/ADOPT.md** — the grant model in the "Settle the remote" step (line 51), the adopt/cloud home.
- **.live-spec/profile.md** — a `trust.github-grant` line, kin to `trust.push-grant`.
- **ARCHITECTURE.md** — the `inbox` node's Owns column (line 47) gains INV-112.
- **TEST_MATRIX.md** — M-251 in the `[node: inbox]` block (line 345).
- **tests/test_inbox_remote_arm.py** — new string test, red-proven against the pre-delta tree.
- **VERSION** — pack +0.0.1 (reads 1.0.28 now; the spec rides the pack VERSION, no separate field).

## Done-when, clause by clause

Row 247 (ROADMAP.md line 145) Done-when: "the remote arm stands in the inbox law red-proven, the
grant ask is scripted with its exact path, and one real remote deposit landed."

1. **The remote arm stands in the inbox law, red-proven.** MET by this draft. Blocks A–D land the
   canonical clause in three homes plus the spec anchor and index row; block F is the red-first test.

2. **The grant ask is scripted with its exact path.** MET by block E, with one fill-in. The ask
   template is drafted; the exact repository-access URL for the Claude GitHub App must be READ from
   the live settings page at draft time and pasted in — the analyst does not fabricate it. The
   template marks the fill-in `<APP-REPO-ACCESS-URL>` so the applier cannot miss it.

3. **One real remote deposit landed.** FIELD-GATED — a local run cannot self-certify it. A local
   session's remote-agent request falls back to a local worktree; a real cloud session fires only
   from the owner's browser at claude.ai/code (the settled facts, 2026-07-10). So the run lands the
   law and scripts the ask, and this clause stays open as a dated field-acceptance line the owner
   closes with one real browser deposit. No-self-certification [INV-94] forbids claiming it met on a
   local or synthetic deposit. The row therefore LANDS the law but stays open on (c) until the owner's
   real deposit — this is an applier-ready law with a human-gated acceptance tail, not a surface split.

## Grounding — what the law extends, and where it is genuinely new

- **The inbox door as it stands** (PRODUCT_SPEC.md:1584–1604, inbox/README.md): the outsider creates
  one new file, commits it touching `inbox/` only with the source named, and that commit is inside the
  read-only exception [INV-10, E-11]. Today's law assumes a shared filesystem; it never states the
  PUSH or the grant that a git-only seat needs. That gap is exactly what row 247 fills.
- **The push grant** (PRODUCT_SPEC.md:726 [INV-82], profile:24–28): INV-82 governs a host pushing its
  OWN accepted work to its OWN remote, under a grant recorded in the host profile. Row 247 is a
  different actor — an outside seat depositing into a foreign repo's inbox — so it earns its own
  invariant, kin to INV-82's grant-recorded-in-profile pattern but not covered by it.
- **The honest-failure kin** (PRODUCT_SPEC.md:223 [INV-67]): a seat that cannot reach its reader fails
  the same way a window that never opened fails. The no-grant failure is the same shape: name what is
  missing, hand over the one action, never fail silently.
- **The seat law** (INV-67 kin, settled facts): a local sub-agent never appears in the owner's browser
  session list; real cloud seats fire only from claude.ai/code. This is why clause (c) is field-gated.

## Recommendation on the DECIDE (GitHub Issues as a public repo's stranger door)

**Split it into its own small follow-up row; do not fold it into 247.** Reasons: it serves a
different actor (a stranger with no push rights, not a granted seat), it needs its own mechanic (a
sweep of Issues beside `inbox/`), and its facts wait on a real public-repo contribution case to
ground them — the same "waits on a first real run" posture that gates 247's own clause (c). Folding
it would bundle two stories under the one-feature-one-story law. The orchestrator makes the final
call at landing; if the call is to answer it here instead, it becomes a second invariant, not a
clause on INV-112.

---

## CANONICAL BLOCK (embedded verbatim in all three prose homes so the string needles match)

> A remote seat reaches a repo only through git. Its deposit stays one new file in `inbox/`, committed
> touching `inbox/` only with the source named in the message, and then pushed. The push runs under a
> per-repo grant: the owner links the Claude environment to the GitHub account once, and grants each
> repo to the app once, and the grant is recorded in the host profile like the push grant. A seat with
> no grant fails honestly. It names the grant it lacks and hands the owner the one action that supplies
> it. It never fails silently and never guesses a workaround.

Needles (verbatim, whitespace-collapsed) in every prose home: `A remote seat reaches a repo only
through git`, `committed touching`, `under a per-repo grant`, `recorded in the host profile like the
push grant`, `A seat with no grant fails honestly`, `hands the owner the one action`.

---

## BLOCK A — SPEC CLAUSE (PRODUCT_SPEC.md) — insert after line 1592

**old_string**:
```
The outsider commits its one new file — a commit touching inbox/ only, its message naming the source. That commit is inside the read-only exception.
```

**new_string**:
```
The outsider commits its one new file — a commit touching inbox/ only, its message naming the source. That commit is inside the read-only exception.

**The inbox has a remote arm.** A shared filesystem is not the only way in. A remote seat — a cloud session, a scheduled routine, another machine — reaches a repo only through git. A remote seat reaches a repo only through git. Its deposit stays one new file in inbox/, committed touching inbox/ only with the source named in the message, and then pushed. The push runs under a per-repo grant: the owner links the Claude environment to the GitHub account once, and grants each repo to the app once, and the grant is recorded in the host profile like the push grant [INV-82]. A seat with no grant fails honestly. It names the grant it lacks and hands the owner the one action that supplies it, the same honest failure as a window that never opened [INV-67]; it never fails silently and never guesses a workaround. (Born of the owner thinking the cloud seat through mid-session, 2026-07-10: today's inbox law assumed a shared filesystem, and a live routine alert was the first seat to hit the gap.) [INV-112]
```

## BLOCK B — INBOX MECHANICS HOME (inbox/README.md) — append after line 15's commit rule

**old_string**:
```
Commit your one new file (a commit touching inbox/ only, message naming the source) — that commit is part
of the exception. A live-spec session sweeps this folder as its first act, harvests each file into the home
its route owns (a wish into a ROADMAP row, feedback by the routing law — SPEC T-20), and removes the file
in the harvest commit (git history keeps it).
```

**new_string**:
```
Commit your one new file (a commit touching inbox/ only, message naming the source) — that commit is part
of the exception. A live-spec session sweeps this folder as its first act, harvests each file into the home
its route owns (a wish into a ROADMAP row, feedback by the routing law — SPEC T-20), and removes the file
in the harvest commit (git history keeps it).

**From a remote seat, over git.** A remote seat reaches a repo only through git, so it also pushes.
The deposit stays one new file here, committed touching inbox/ only with the source named, and then pushed
under a per-repo grant recorded in the host profile like the push grant. A seat with no grant fails honestly:
it names the grant it lacks and hands the owner the one action that supplies it (SPEC INV-112).
```

## BLOCK C — ADOPT / CLOUD HOME (adopt/ADOPT.md) — extend the "Settle the remote" step (line 51)

**old_string**:
```
4. **Settle the remote — a named deliverable (SPEC A-5).** By the first landing a
   remote (GitHub) either EXISTS or the human has EXPLICITLY DECLINED one; record the outcome in the run's
   journal entry. Creating/pushing the remote is the human's gate — offer and follow through, don't do it
   silently and don't let "recommended" quietly become "never happened" (the pilot ended local-only that way).
```

**new_string**:
```
4. **Settle the remote — a named deliverable (SPEC A-5).** By the first landing a
   remote (GitHub) either EXISTS or the human has EXPLICITLY DECLINED one; record the outcome in the run's
   journal entry. Creating/pushing the remote is the human's gate — offer and follow through, don't do it
   silently and don't let "recommended" quietly become "never happened" (the pilot ended local-only that way).
   Where a remote seat will reach this repo — a cloud session, a scheduled routine, another machine — the
   remote arm of the inbox door applies (SPEC INV-112). A remote seat reaches a repo only through git, so
   its deposit stays one new file in inbox/, committed touching inbox/ only with the source named, and then
   pushed under a per-repo grant: the owner links the Claude environment to the GitHub account once, and
   grants each repo to the app once, and the grant is recorded in the host profile like the push grant. A
   seat with no grant fails honestly — it names the grant it lacks and hands the owner the one action that
   supplies it. Script that ask with its exact settings path (see the grant-ask template, block E).
```

## BLOCK D — FORMAL-INDEX ROW (PRODUCT_SPEC.md) — Package repo section, after INV-11 (line 1723)

**old_string**:
```
| INV-11 | concurrent-edit fence before write/commit | Package repo |
```

**new_string**:
```
| INV-11 | concurrent-edit fence before write/commit | Package repo |
| INV-112 | the inbox door's remote arm: a seat that reaches a repo only through git deposits one new file in inbox/, commits it touching inbox/ only with the source named, and pushes it, under a per-repo grant recorded in the host profile like the push grant [INV-82] (the owner links the Claude environment to GitHub once, grants each repo once); a seat with no grant fails honestly — it names the grant it lacks and hands the owner the one action, the honest failure of a window that never opened [INV-67], never silent, never a guessed workaround; born of the owner thinking the cloud seat through (2026-07-10) | Package repo |
```

APPLIER NOTE (index placement): the INV index is grouped by the section column, not strictly by
number, and the tail appends by landing. Place this row in the **Package repo** group, directly under
INV-11 as shown. If the tree at apply time has moved to a strict tail-append habit (an INV-1xx row
already sits at the very end regardless of section), follow whatever the two nearest landed rows did —
match the local habit, keep the section column `Package repo`.

## BLOCK E — SCRIPTED GRANT-ASK (the exact-path deliverable, Done-when b)

The ask is a fixed template the session prints when a remote seat is being set up for a repo with no
recorded `trust.github-grant`. It carries the exact settings path. **The applier reads the live URL
from the GitHub App settings page and replaces `<APP-REPO-ACCESS-URL>` before landing — do not guess
it.** Home it as a short block in adopt/ADOPT.md beside step 4, or as `scripts/grant-ask.md` if the
orchestrator prefers a standalone artifact (kin to `scripts/judge-rubric.md`). Recommended: the
standalone `scripts/grant-ask.md`, so the exact URL has one home and the prose homes point to it.

```
GRANT ASK — a remote seat needs this repo granted to the Claude GitHub app

One action, yours:
1. Open the app's repository-access settings: <APP-REPO-ACCESS-URL>
   (read once from github.com/settings/installations → the Claude app → Configure → Repository access)
2. Add this repo (<owner>/<repo>) to the app's granted repositories, and Save.
3. Tell me it is done. I record it in the host profile as trust.github-grant with today's date,
   like the push grant, and the remote arm is live for this repo.

Until then, the remote seat cannot push its inbox deposit. It has named exactly this grant as the
one thing it lacks; nothing else is blocked.
```

## BLOCK F — NEW TEST FILE (full content) — tests/test_inbox_remote_arm.py

```python
"""The inbox door has a remote arm — M-251 (SPEC INV-112, row 247).

The owner thought the cloud seat through mid-session on 2026-07-10: today's inbox law assumes a shared
filesystem, and a cloud session, a scheduled routine, or another machine reaches a repo only through git.
The remote arm states the deposit — one new file in inbox/, committed touching inbox/ only with the source
named, then pushed — under a per-repo grant recorded in the host profile like the push grant. A seat with no
grant fails honestly: it names the grant it lacks and hands the owner the one action that supplies it. String
rows on the law's three prose homes plus the spec anchor and its index row.
"""

import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_flat(rel):
    """The file's text with whitespace collapsed, so wrapped lines match needles."""
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return " ".join(f.read().split())


class TestInboxRemoteArm(unittest.TestCase):
    HOMES = (
        "PRODUCT_SPEC.md",
        "inbox/README.md",
        "adopt/ADOPT.md",
    )

    def test_remote_arm_in_all_prose_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("A remote seat reaches a repo only through git", body, home)
            self.assertIn("under a per-repo grant", body, home)
            self.assertIn("recorded in the host profile like the push grant", body, home)

    def test_honest_failure_in_all_prose_homes(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("fails honestly", body, home)
            self.assertIn("hands the owner the one action", body, home)

    def test_deposit_stays_inbox_only(self):
        for home in self.HOMES:
            body = read_flat(home)
            self.assertIn("committed touching inbox/ only", body, home)

    def test_spec_anchor_and_index(self):
        spec = read_flat("PRODUCT_SPEC.md")
        self.assertIn("[INV-112]", spec)
        with open(os.path.join(ROOT, "PRODUCT_SPEC.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("| INV-112 |"):
                    self.assertIn("remote arm", line)
                    self.assertIn("grant", line)
                    return
        self.fail("INV-112 index row missing")


if __name__ == "__main__":
    unittest.main()
```

Red-proof order: run `tests/test_inbox_remote_arm.py` against the pre-delta tree first (all four
asserts fail — no home carries the needles, no INV-112 anchor), then apply blocks A–D, then green.

## BLOCK G — ARCHITECTURE OWNED-ANCHORS (ARCHITECTURE.md line 47, inbox node's Owns column)

**old_string**:
```
| inbox | parallel-safe intake door for wishes born outside a live-spec session | E-11, T-10, INV-10 | `inbox/README.md:3` (one door, one NEW file), `:9` (file format), `:14` (commit rule) |
```

**new_string**:
```
| inbox | parallel-safe intake door for wishes born outside a live-spec session | E-11, T-10, INV-10, INV-112 | `inbox/README.md:3` (one door, one NEW file), `:9` (file format), `:14` (commit rule), `:19` (remote arm) |
```

## BLOCK H — MATRIX ROW (TEST_MATRIX.md) — [node: inbox] block, after M-050 (line 351)

**old_string**:
```
| M-050 | Only a session assigned to live-spec writes this repo; an outsider never writes spec/queue/journal/skills — the inbox file is the whole exception | INV-10 | string | `test_inbox_states_write_rule` | BUILT |
```

**new_string**:
```
| M-050 | Only a session assigned to live-spec writes this repo; an outsider never writes spec/queue/journal/skills — the inbox file is the whole exception | INV-10 | string | `test_inbox_states_write_rule` | BUILT |
| M-251 | The inbox door has a remote arm (INV-112, row 247): a seat that reaches a repo only through git deposits one new file in inbox/, committed touching inbox/ only with the source named, then pushed, under a per-repo grant recorded in the host profile like the push grant [INV-82] (the owner links the Claude environment to GitHub once, grants each repo once); a seat with no grant fails honestly — it names the grant it lacks and hands the owner the one action, the honest failure of a window that never opened [INV-67], never silent; the law lives in three prose homes — the spec inbox-law clause, inbox/README.md, and adopt/ADOPT.md's remote-settle step; born of the owner thinking the cloud seat through mid-session (2026-07-10); the field beat — one real remote deposit — waits on a real browser cloud session and is not self-certified on a local run [INV-94] | INV-112 | string | `test_remote_arm_in_all_prose_homes` + `test_honest_failure_in_all_prose_homes` + `test_deposit_stays_inbox_only` + `test_spec_anchor_and_index` (red proven against the pre-delta tree, 2026-07-12) | BUILT |
```

## BLOCK I — HOST PROFILE GRANT LINE (.live-spec/profile.md) — after the push-grant block (line 28)

Records live-spec's own already-done link + repo grant (his click 2026-07-10), kin to `trust.push-grant`.

**old_string**:
```
  («сам пуши! не надо меня ждать»); this answers the push-law grant question (SPEC INV-82) for this host.
```

**new_string**:
```
  («сам пуши! не надо меня ждать»); this answers the push-law grant question (SPEC INV-82) for this host.

- `trust.github-grant: standing — the Claude environment is linked to Alexander's GitHub account (his
  one-time click), and this repo is granted to the app, so a remote seat's inbox deposit may push here
  under the remote arm (SPEC INV-112)` — recorded 2026-07-10, the account link and repo grant done that
  day; a seat that ever finds this line absent for a repo runs the grant ask (scripts/grant-ask.md) rather
  than failing silently.
```

## BLOCK J — VERSION

- `VERSION` (pack) — +0.0.1 (reads 1.0.28 now). The spec rides the pack VERSION; no separate spec field.
- No skill frontmatter moves: `inbox/` and `adopt/ADOPT.md` carry no version field, and feedback-intake
  is untouched (the door mechanics home is inbox/README.md + the spec, not the intake skill).

---

## Code allocation note

INV-112 and M-251 are verified free across PRODUCT_SPEC.md, ROADMAP.md, and TEST_MATRIX.md at this
writing (grep clean; row 250's own analysis names INV-112 as the next free slot and mints nothing).
But other lanes run tonight (rows 248, 249, 253–256 carry worker checkpoints). Per the row-231
reservation-lift call, codes consume in **landing order**, not by reservation. So the applier must
**re-verify INV-112 / M-251 are still free at the moment of landing**; if another lane landed first
and took them, this row takes the next free INV / M pair, and blocks A, D, F, G, H, I update in
lockstep to the new numbers.

## Self-verify

- Every needle (`A remote seat reaches a repo only through git`, `committed touching inbox/ only`,
  `under a per-repo grant`, `recorded in the host profile like the push grant`, `fails honestly`,
  `hands the owner the one action`) appears verbatim in all three prose homes (blocks A, B, C);
  `[INV-112]` in the spec clause; the `| INV-112 |` index row contains `remote arm` and `grant`.
- All anchors quoted from the live tree: spec 1592 / 1723, inbox/README.md 15, ADOPT.md 51,
  ARCHITECTURE 47, matrix 351, profile 28.
- Owner node = inbox (ARCHITECTURE:47); the matrix row sits in `[node: inbox]`.
- Register: plain SVO, no "X — not Y" contrast frame (each prohibition is its own plain sentence —
  "It never fails silently and never guesses a workaround."), no coined metaphor; "remote arm" is a
  plain ordinary phrase for the door's git-reaching half, not an invented mechanism name.
- Dates only from the row's own record (2026-07-10) or the landing date (2026-07-12).
- Field-gate honesty: Done-when (c) is carried as an open field-acceptance beat, not claimed met;
  the exact grant URL is a marked fill-in, not fabricated.

---

APPLIED + CLOSED at landing 2026-07-12 (row247-worker.md; field leg open). The block-E grant-URL
fill-in could not be read mechanically (no authenticated github.com session, `gh api
/user/installations` 403'd); the orchestrator's call substituted the stable settings path
`https://github.com/settings/installations` plus the named click path in place of the
per-installation numeric URL, recorded in the checkpoint. All other blocks (A-D, F-J) landed
exactly as drafted. Done-when (a) and (b) MET; (c) stays OPEN, closable only by the owner's real
browser cloud deposit.

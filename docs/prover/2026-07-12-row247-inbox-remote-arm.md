# Prover — row 247, the inbox door's remote arm (2026-07-12, short form per INV-61)

Small delta (kind: skill; architecture = anchor assignment INV-112 → inbox).

- **Previous records:** 2026-07-12-row239-catchup-discriminator, 2026-07-12-row240-layout-pass-vehicle,
  2026-07-12-row233-no-silent-drop all clean (0 must-fix); no unfolded rows.
- **The delta in one line:** a remote seat — a cloud session, a scheduled routine, another machine —
  reaches a repo only through git, so its inbox deposit stays one new file in inbox/, committed
  touching inbox/ only with the source named, then pushed, under a per-repo grant recorded in the
  host profile like the push grant [INV-82]; a seat with no grant fails honestly, naming the grant it
  lacks and handing the owner the one action that supplies it, the same honest-failure shape as a
  window that never opened [INV-67]; spec clause (INV-112 + index), inbox/README.md, adopt/ADOPT.md's
  remote-settle step, ARCHITECTURE.md's inbox owns-list, M-251, four string tests red-proven against
  the pre-delta tree. Composition read: no clash with the push-grant law (INV-82, a host pushing its
  own accepted work) — a different actor, an outside seat depositing into a foreign repo's inbox,
  earning its own invariant kin to INV-82's grant-recorded-in-profile pattern; no clash with
  no-self-certification (INV-94) — Done-when clause (c), one real remote deposit, stays open on that
  law rather than being claimed on a local run. Born of the owner thinking the cloud seat through
  mid-session on 2026-07-10: today's inbox law assumed a shared filesystem, and a live routine alert
  was the first seat to hit the gap.
- **Fill-in note:** block E's grant-ask template carried a marked placeholder
  (`<APP-REPO-ACCESS-URL>`) for the exact GitHub App repository-access URL, explicitly not to be
  guessed. The applier could not read it mechanically (no authenticated github.com session available;
  `gh api /user/installations` returned 403). The orchestrator's landing-time call substituted the
  STABLE settings path (`https://github.com/settings/installations`) plus the named click path
  ("Claude App → Configure → Repository access → add the target repository") in place of the
  per-installation numeric URL — reasoned as exact and durable where the numeric URL is visible only
  inside the owner's authenticated session and changes on reinstall. This satisfies Done-when clause
  (b), the grant ask scripted with its exact path, at `scripts/grant-ask.md`.
- **Open field leg:** Done-when clause (c), one real remote deposit landed, stays OPEN — a local
  session's remote-agent request falls back to a local worktree, and a real cloud session fires only
  from the owner's browser at claude.ai/code, so this clause closes only by his real deposit, never a
  local or synthetic one [INV-94].
- **DECIDE resolved:** GitHub Issues as a public repo's stranger door is split into its own follow-up
  queue row per the draft's recommendation, not folded into this law — a different actor (a stranger
  with no push rights) needing its own mechanic and its own field grounding.
- **Verdict:** ready to ship — 0 must-fix, 0 should-clarify; field leg (c) named open, not claimed.

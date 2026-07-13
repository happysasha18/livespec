# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-12 ~21:31, session 41 — the free-work queue closed autonomously under /loop)
**s41: the whole free queue landed — twelve rows. VERSION 1.1.16, suite 590 green, CI green on every push,
tree clean, everything pushed.** Read this section then wipe memory; the detail lives in JOURNAL + ROADMAP.

**Follow-ups 2026-07-13:** the rewritten READMEs landed (live-spec + the product-prover mirror synced) and the
marketplace owner placeholder became the real owner (name + GitHub profile); all pushed, CI green. The same
placeholder in the sibling promoter repo was routed to its inbox.

- **Five prover findings F3-F7 → rows 282-286 (INV-129..133):** deferred rows are re-scanned for a fired
  revisit trigger at every queue-take; a withdrawn decision converges to a surfaced default after the second
  withdrawal; a mid-work re-door rebuilds the parallel-lanes independence graph and serialises a new collision;
  every person-facing heading carries its tag or an explicit marker (untagged is red); a critical non-bug heads
  the queue yet never preempts a rolling lane (only the bug door preempts), echoed at intake.
- **Delegation consolidated → row 262 (anchored INV-69):** base rule 5 is the single statement; the personal
  playbook collapsed to a pointer plus its own "why #2" note; the three superseded bars (numeric file/time
  triggers, default-not-propose, once-per-session spot-check) removed. A guard test greps the whole pack so a
  size/time numeric trigger can never regress. Row 295 removed the one the audit caught surviving in build-pipeline.
- **The four architect-draft mechanical halves → rows 291-294:** the footprint-note suite check (INV-134);
  per-kind concrete layers + proofs declared at founding (INV-135); the cross-cut counter (an advisory signal to
  the next MINOR audit); the interface-test machinery (layer→level rule + a per-block interface row).
- **Communicator body thinned 578→499 lines with no rule cut → row 280;** worked examples spilled to
  references/field-examples.md, all 22 rules and every test-pinned phrase kept in the body.
- **Impersonal voice ADOPTED in the pack's own docs → row 279:** 46 owner-name attributions rewritten in place
  (date + reason kept, the who/when moved to JOURNAL); the shipped-language gate now runs in pre-push AND CI with
  zero active offences. Six authorship bylines kept under a dated carve-out. The former self-exemption is retired.
- **An independent adversarial audit (INV-46) ran over the seven new laws:** one must-fix (found and fixed as
  row 295), two latent hardenings folded (rows 296/297 — numeric/multi-feature heading ids; the footprint
  cutoff-day missing-time escape). Four string-only process-laws (129/130/131/133) sit at the accepted prose floor.

## LANDED 2026-07-13 (after the s41 close)
- **Per-kind design principles — row 298, INV-136 (v1.1.17), CI green.** The tlvphotos deposit landed and a
  background worker shipped it: a project.kind now declares checkable design principles the verify/feel pass
  runs; the frontend kind's starter set names the interactive-overlap rule (interactive controls of different
  layers hold separate clickable regions; a passive element may overlap freely). Homed in the spec founding
  clause + ARCHITECTURE + spec-author/build-pipeline wiring, NOT in base rule 24 (avoids a base-version pin sweep).
- **Mirror auto-sync — v1.1.19, both arms LIVE.** The standalone mirror (product-prover) now syncs on its own from
  two homes: the local pre-push green-gate tail (proven live on the push) and a CI `sync-mirrors` job. The CI arm's
  credential is a per-repo SSH deploy key (secret `MIRROR_SYNC_DEPLOY_KEY` on live-spec, read-write deploy key on
  product-prover) — set up entirely from the CLI, no owner action, no broad token. Fixes the drift found 2026-07-13.
  The prover stays ONE copy in the pack; the mirror is showcase-only — extracting it would break install/manifest/Prove.

- **Interactive-overlap prover lens — row 299, v1.1.20, Fable-audited.** The open decision closed: the overlap rule
  now also has a spec-time lens in product-prover, sibling to INV-125/126, as another home of INV-136 (no new code).
  The finding is stated as the spec's silence (the INV-72 blank-answer class), not rendered geometry — a Fable
  adversarial audit (INV-46) caught that must-fix and two clarity folds before commit. The verify-time principle
  stays the render-time floor; the lens catches the blind spot earlier on the spec.
- **Prover self-review — row 300, v1.1.21, Fable.** Pointed the prover at the product-prover skill itself: verdict
  in good order, six folds — a "nine families" count that had drifted to 18 (pinned by a test that guarded the word),
  a missed prover-skill version bump from row 299 (1.0.9→1.0.10), a coined "get/set" metaphor (also test-pinned),
  and three smaller register/notation fixes. Two of the six were enshrined by guardrail tests; prose and pin fixed
  together. No lens meaning changed.

## OWNER-HELD / OPEN (each needs the owner's word — no autonomous move taken)
- **Future mirror repos need their own deploy key.** The CI mirror-sync auth is a deploy key scoped to
  product-prover alone. If another skill (e.g. spec-author) later gets a standalone mirror repo, add a read-write
  deploy key on it and either reuse one key across mirrors or store a second secret — a one-command CLI step, no owner action.
- **Row 261** — GitHub Issues as the strangers' wish door for public repos: still a DECIDE. Recommendation: defer.
- **Install the pack globally** — the installed copies at ~/.claude/skills/ drifted from the repo this session
  (communicator, build-pipeline, spec-author, test-author, live-spec-base, product-prover all changed). Running
  `bash install.sh` makes 1.1.16 live for the other windows; held for the owner's word, since it changes every window.
- **One real remote deposit** — the local cross-project inbox works; the browser arm (claude.ai/code) still owes
  one live deposit to close its field leg (never self-certified, INV-94). The owner's optional action.
- **tlvphotos** — an impersonal-voice wish sits in its inbox (591 attributions in shipped docs); it runs in the
  tlvphotos window. track-coach is already clean.

## Non-blocking debt (recorded, not urgent)
- The ARCHITECTURE pin note "check-shipped-language.py (its engine)" drifts — the label word is absent from the
  file head; present at baseline bbf7790, not this session's delta.
- The sibling INV-73 coverage-mapping regex still reads `F-[a-z-]`; no live heading uses a numeric or multi id, so
  there is no active divergence (row 296 widened the INV-132 side).
- Next free codes at s41 close: INV-136, M-278 — read the live Formal index before minting; codes consume in
  landing order, reservations are dead.

## CLOUD FACTS (settled 2026-07-10; row 247 law live, its field leg open)
A remote-agent request from a local session falls back to a local worktree; real cloud sessions fire only from
the browser (claude.ai/code). The remote inbox arm: one new inbox/ file per deposit, a per-repo grant in the host
profile, honest failure that names the missing grant (INV-112; grant-ask template at scripts/grant-ask.md).

## Standing habits (always-on)
- `date` before any stamp; chat leads use the prompt hook's wall clock, never extrapolation.
- Shipped docs stay impersonal — the language gate runs in pre-push + CI (INV-118/INV-120); provenance lives in
  JOURNAL. Delegation runs by base rule 5 → INV-69: one home, guarded by a whole-pack test.
- No self-certification (INV-94) · no calques · plain words, codes trail (INV-28) · the say-what-it-is rule with
  no contrast frames · inbox swept first · one lane one commit · a delegated run's verdict is the suite log's tail
  (INV-80) · the push walk reads the CI verdict itself (INV-106) · a high-stakes change whose only review is its
  author's gets an independent fresh-context checker (INV-46) · a landed row carries its footprint note (INV-134)
  and its delegation line (INV-103) · landings close their checkpoints and list every substance move (INV-107/109).
- Machine: re-arm caffeinate at the next night batch if a long run is queued.

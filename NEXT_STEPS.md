# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-15 14:35 — 1.6.1 READY (committed, not pushed — the harness push gate needs an explicit push signal or the git-push allow rule); the deferral rule gained its mechanical net + delivery arm, and build-pipeline's SKILL body was thinned under 500; suite 755; pack v1.6.1)
**PACK v1.6.1** (1.6.0 at CI green; 1.6.1 hardens INV-152 and thins build-pipeline, suite 755). A PATCH:
it strengthens the enforcement of an existing rule and refactors a doc, adding no new rule or capability.
Two things landed, from Alexander's words on the recurring "handed me what was never mine" leak; the change
was reviewed by an independent adversarial prover pass (record `docs/prover/2026-07-15-deferral-guard.md`,
HOLDS-WITH-FIXES) whose six defects were all folded before commit:

- **The deferral rule (INV-152 / base rule 29) got its two enforcement arms.** A mechanical net,
  `guardrails/check-deferral-marker.py`, reds a commit when an item in NEXT_STEPS or a decision page parks
  for the human's word and names no reason category (taste · policy · irreversible · device-feel); it reads
  the file as folded work items, so a signal or its reason wrapped across lines is handled. A delivery arm,
  a fifth chat-law hook line, re-fires the derivability re-test at the moment a marker is written or an
  AskUserQuestion is opened. Matrix rows M-297 (extended) + M-302 (the hook), a CI backstop on the repo's
  own files. (The prose rule alone kept leaking — three instances on 2026-07-15 across tlvphotos,
  track-coach, and this window.)
- **324 done — build-pipeline SKILL.md 601 → 499 lines.** Set-piece tables moved to
  `skills/build-pipeline/references/*.md` with pointers; conftest's `read_all` lets content-presence tests
  read the whole skill surface, so traceability follows relocated text (size tests still read SKILL.md alone).

## Queue (ROADMAP)
- **321** feedback-collector sub-skill — on strong user emotion, OFFER (consent first) to send a distilled
  digest upstream; inbox destination, per-machine opt-out, distinct from feedback-intake. Open design Qs at
  build (Alexander 2026-07-15, "как дойдём добавим").
- **325** Give the forward-binding law a dedicated invariant and repoint every cite to it — the real
  unification 322 named. The property (a duty binds forward from the first landing after its clause exists,
  never retroactively) is stated loosely across INV-15 / 41 / 74 / 75 / 127, T-16, A-3, INV-21, and line 626,
  and no anchor's text actually STATES the law (INV-15's own text is the node+matrix rule). Mint the
  invariant, repoint the cites, one root. Prover finding F1/F5, record
  `docs/prover/2026-07-15-322-forward-binding-and-323-review-record-class.md`. 322's stopgap: INV-41's
  forward-binding was deflated from a false "the one law [INV-15]" claim to a precedent cite.
- _(323 done — the review-record class declared once, INV-156; prover HOLDS-WITH-FIXES, six findings folded.)_

## Standing habits / OWNER-HELD
- **Memory can be wiped** — the whole story is in JOURNAL + the prover/design-review records + ROADMAP.
- Version bumps are NOT owner-reserved (Alexander confirmed 2026-07-15): cut them on green; standing push
  authorization holds. The deep independent audit runs by default as quality, not on his word.
- On a failure: the root/infrastructure fix first, never a blind retry or a pointwise patch [INV-155 kin].
- **Pushing depends on the session's permission mode.** Under the global `bypassPermissions` a plain
  `git push` to an existing repo runs free (v1.6.1 pushed with no block, 2026-07-15). Only the narrow set of
  truly-dangerous outward acts stays hard-blocked above bypass — `gh repo create`, force-push of rewritten
  history, self-editing settings.json (the agent's one hard boundary). A session launched in a stricter mode
  than the global default may still hold an ordinary push for an explicit go.
- Next free codes: INV-157, M-304 (INV-156 + M-303 used by 323).

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
- **322** the forward-binding law is cited to two roots — unify to one.
- **323** declare the review-record class once (prover / design-review / skill-creator / verify records).

## Standing habits / OWNER-HELD
- **Memory can be wiped** — the whole story is in JOURNAL + the prover/design-review records + ROADMAP.
- Version bumps are NOT owner-reserved (Alexander confirmed 2026-07-15): cut them on green; standing push
  authorization holds. The deep independent audit runs by default as quality, not on his word.
- On a failure: the root/infrastructure fix first, never a blind retry or a pointwise patch [INV-155 kin].
- **Push runs through the harness gate.** Every outward push is held by the harness above the model until an
  explicit push signal; the fix that ends the friction is Alexander running the `!` one-liner that adds
  `Bash(git push)` / `Bash(git push *)` / `Bash(gh repo create *)` to `~/.claude/settings.json` (the agent
  cannot self-edit settings — the one hard harness boundary). Until then a push owes an explicit go.
- Next free codes: INV-156, M-303.

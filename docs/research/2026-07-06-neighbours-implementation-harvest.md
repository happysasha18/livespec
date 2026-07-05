# How the neighbours actually built it — implementation-level harvest (row 107)

*2026-07-06, night session 11. Three clean-context workers cloned and read the code (not the READMEs):
GitHub Spec Kit, OpenSpec, Open GSD, and BMAD's story-file mechanism. Each mechanism below says where
it lives in their source, whether it is script-enforced or prompt-enforced, and the verdict for us.
Candidates worth taking are filed as their own queue rows (each one wish = one story, T-17).*

## The headline finding

**Spec Kit's celebrated "cross-artifact consistency checks" are prompt text, not code.** Its analyze
and converge commands — the centerpiece — are LLM instructions; the only mechanical checks in the
whole repo are shell tests that a file EXISTS (`[[ -f "$IMPL_PLAN" ]]`). No script anywhere greps a
requirement id against a task id. OpenSpec is the honest opposite: its delta-spec grammar, merge, and
archive are real, tested TypeScript — but its "verify" and review steps are prompt-only and never
block. GSD's strength is orchestration discipline (fresh contexts, contracts between phases) with one
real schema validator; BMAD's story files are heavily proceduralized prompts. Net: **executable
enforcement of spec↔test↔code traceability is genuinely rare** — our suite + pre-push walk is not a
me-too; the research doc's claim holds at the code level too.

## Worth stealing (filed as rows 110–115)

1. **The adversarial fresh-context verifier** (GSD `agents/gsd-verifier.md`): opens with the
   hypothesis "tasks completed, goal missed"; re-derives what must be true from the ORIGINAL spec,
   never from the worker's summary; checks each claim at four levels (exists → substantive → wired →
   data actually flows); carries literal stub-detection greps (`return <div>Placeholder</div>`, static
   `[]` returns). Their stated reason matches our law: workers "reliably report Self-Check: PASSED"
   even when wrong. → row 110.
2. **The brief is born from read code** (BMAD `bmad-create-story/SKILL.md` step 3, marked critical):
   before writing a story/brief, READ IN FULL every file the work will modify and record
   current-state / what-changes / what-must-survive; every task carries an `(AC: #)` back-reference
   to its acceptance criterion; every technical claim a `[Source: file#section]` citation. Their words:
   skipping the read is "the primary cause of implementation failures". → row 111.
3. **Named HALT list + restricted edit zones for workers** (BMAD `bmad-dev-story/SKILL.md`): the
   worker may edit only named zones of its artifacts, and may stop early ONLY on a named condition
   (ambiguous requirement, 3 consecutive failures, missing config, new dependency) — sharper than a
   general "ask if unsure". We have write-fencing; the enumerated HALT list is the delta. → row 112.
4. **Quantified brief sizing** (GSD `references/context-budget.md` + planner degradation curve):
   quality degrades past ~30% context; a delegated task targets 2-3 tasks / bounded share of the
   window; pass PATHS to a worker, never inlined file bodies. Our delegation gate states the principle
   — theirs quantifies it. → row 113.
5. **Gate-script conventions** (OpenSpec `archive.ts`, `cli/index.ts`): all-or-nothing batched writes
   (validate every rebuilt file BEFORE writing any); every blocked gate emits a typed
   `{severity, code, message, fix}` — one JSON document for agents, the same `fix` line for humans;
   an explicit advisory-vs-blocking taxonomy per check. Our guardrails work; these are their next
   hygiene rungs. → row 114.
6. **Digest, not archive — with a size cap** (GSD `templates/state.md`, hard <100 lines): the resume
   digest is bounded; growth is a design failure, detail flows to the journal it points at. Our
   NEXT_STEPS drifts long; a cap with an owning check is the concrete fix. → row 115.

## Considered, not taken (and why)

- **Spec Kit's constitution file**: a second governance home beside the spec, synced only by prompt
  trust — our single living SPEC.md with one-home-per-fact is the stronger form of the same idea.
- **OpenSpec's change-folders + delta grammar + block merge**: solves "many pending mutations of one
  doc" — a problem a single living spec edited in place does not have; the name-keyed string surgery
  is fragile on header drift.
- **OpenSpec's SHALL/MUST + ≥1 scenario lint**: attractive, but it enforces EARS-style phrasing our
  use-case-first prose deliberately avoids; our traceability test (every anchor ≥1 matrix row ≥1
  test) already guards the same failure at the artifact level, not the wording level.
- **GSD's 35 named agent roles, wave/worktree machinery**: parallel-fan-out infrastructure for a
  problem we don't have while one junior works at a time; revisit only if parallel workers on one
  repo become real (their one-line rule — no two concurrent briefs may declare overlapping files —
  is already our worker contract's fence).
- **Completion markers regex-routing** (GSD): our task-notification harness already owns this seam;
  the valuable half — never trust the return value, spot-check disk/git — is base rule 13 already.
- **Spec Kit's converge scan** ("what's specified but not built, appended as tasks"): this is our
  reverse-verify / milestone audit under another name; periodic rows exist.
- **BMAD's sprint-status.yaml**: a shared status file with NO schema validator — noted as a warning,
  not a model; if we ever share a status file across workers, it gets a validator (see row 114).

## Sources

Cloned at study time into the session scratchpad: `github/spec-kit` · `Fission-AI/OpenSpec` ·
`gsd-build/get-shit-done` · `bmad-code-org/BMAD-METHOD`. File paths cited inline are theirs; the three
workers' full reports (with per-file quotes) live in the session transcript, the load-bearing facts
restated here.

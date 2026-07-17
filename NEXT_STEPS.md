# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-17 ~13:28 — the agent-communication layer BUILT, UNCOMMITTED, one worker still live)

**Nothing in this repo is committed.** The whole delta sits in the working tree. Memory stays until it pushes.
The playbook repo IS committed and pushed (71fec48: the owner's 2026-07-15 settings landed after two days
uncommitted; `language.no-inflation` grown to both poles with its machine; `language.no-validation` added;
the loader's skill count corrected to nine).

**What is built (uncommitted):** the agent-communication stage, ROADMAP rows 371-378, re-stated as landed.
PRODUCT_SPEC gained `## When agents work together` (~lines 1393-1545) with four scenarios — F-roster,
F-contract, F-agent-ask, F-agent-birth — and 19 anchors (E-31..E-33, INV-182..INV-196, T-22), all indexed,
owned in ARCHITECTURE, and covered by TEST_MATRIX rows M-352..M-370. Base rule 31 carries the always-on
laws. INV-153 grew from three controls to four (the earned message joins the routing principle).
New files: `guardrails/check-earned-message.py`, `.live-spec/agent.md` (the pack's own card),
`templates/agent.template.md`, `tests/test_agent_channels.py`, `docs/design/2026-07-17-node-growth-law.md`.

**LIVE WORKER — check before touching its files.** A gate-fix worker was briefed ~15:00 and has not landed
its edits. Write-set: `guardrails/check-earned-message.py` · `inbox/README.md` · `tests/test_agent_channels.py`
(gate tests only). Liveness per INV-76: read those three files' mtimes, then decide. If they are untouched
since ~15:00 the worker is gone and its brief is unclaimed — do the work directly (the brief's content is
below). Do not spawn a sibling on those files without that check.

**Suite:** 1041 green at ~14:00, BEFORE the audit fold. The fold since then touched PRODUCT_SPEC,
ARCHITECTURE, TEST_MATRIX, ROADMAP, base rule 31, and test_request_classifier.py. **Re-run the full suite
first thing.** Two known reds to expect and close:
- `test_base_description_counts_the_rule` — rewritten to DERIVE the count. The base description now says
  "thirty-one rules" and the disk holds 31, so it should pass; verify.
- INV-195/INV-196 have matrix rows (M-369, M-370) naming `test_agent_recognises_a_neighbours_zone_itself`
  and `test_one_question_crosses_twice_then_goes_to_the_owner`. **Those two tests are NOT written yet** —
  they belong in `tests/test_agent_channels.py`, which the live worker owns. Write them once it releases.

## ON RESUME — in order

1. **Finish the gate.** The 2026-07-17 audit proved it inert: it keys on a body `From: <name> (agent)` line
   that no shipped convention prescribes, while `inbox/README.md:10` puts the source in the FILENAME. It
   passed the one real agent deposit on the machine (`inbox/2026-07-17-from-track-coach-*.md`, exit 0) and
   passed ten hostile fixtures. It also reds a spec-legal reply, which INV-192 says owes no blocked work.
   The design call is made: **the filename is the source's one home**, `inbox/README.md` prescribes what the
   gate reads, and the two never disagree again. INV-189 was corrected at ~15:30 — a message names its
   BIRTH (blocked work, or a lived fault with its evidence), so the gate demands the birth rather than
   blocked work from everything. The track-coach deposit is the regression fixture: it is a fault message,
   it names no blocked work, and it is CORRECT.
2. **Write M-369/M-370's two tests**, then run the full suite to green.
3. **Commit + push** (VERSION → 2.6.0; the owner's word 2026-07-17: this is an ordinary release, and the
   major waits until the projects have run the layer in the field). Re-walk the README before the push.
   Journal the chapter. Then memory may be wiped.
4. **Re-audit is owed.** The first audit's fold is unverified by a second fresh pass. The folded findings:
   INV-184 and INV-185's false present-tense gate claims now carry [target] + rows 387/385; the INV-41,
   INV-86, INV-117 widenings corrected; rows 371-378 re-stated as landed; the template joined the artifact
   inventory; the base description's count corrected; the vacuous count-check rewritten to derive.
   Still standing (queued, not folded): rows 388 (zone uniqueness, wrong referral), 389 (the remote read
   grant), 387 (the card's gate + adoption's line).

## Standing word / OWNER-HELD
- The whole movement solo, push on green; plain English in docs, plain Russian in chat. Gates mandatory.
- **The roster needs his ratification and nothing else does — the human-only fact is POLICY: who counts as a standing agent on his machine is his act, and a tree's presence on a filesystem grants nothing [INV-152].** INV-184: a roster row is written by the
  session holding the ratification conversation, never by an agent unbidden; pre-law agents take their rows
  at their own catch-up [A-11]. The machine's real trees, swept 2026-07-17 (facts, not a proposal):
  tlvphotos (instance of exhibition-engine, live) · exhibition-engine (engine, live) · promoter (engine,
  live) · promoter-alexander (instance, hub of five campaign spokes, quiet since 07-11) · the REAL
  track-coach is `~/.claude/skills/track-coach` (the most active tree on the machine; `~/track-coach` is an
  inbox-only stub with no git) · tc-cloud-validate is a frozen 11-minute clone of track-coach carrying an
  unmerged branch. Ambiguous by their own records and his to settle: exhibition-engine's `project.kind`
  (its profile marks it owner-gated), whether `~/track-coach` is a deliberate inbox mount, whether
  tc-cloud-validate is disposable.
- CONCURRENCY: multiple windows share ~/live-spec. Commit narrowly by explicit path, never `git add -A`;
  re-check HEAD before writing (fence). A co-located deposit is the FILE ALONE (INV-174, INV-175).
- Next free codes: INV-197, E-34, T-23, M-371, next ROADMAP row 393.

## The queue's near head (his ranking)
- **386 — parallel lanes get branches and worktrees.** HIS WORD: this matters more than the communication
  layer, and it waits until the communication layer has run in the field. Verified for it: `isolation:
  worktree` on a subagent and `EnterWorktree`/`ExitWorktree` on a session both exist; INV-105 already calls
  worktree isolation the default when write-sets overlap, while the tool's own contract says to use it only
  on his explicit word — the law and the tool contradict, so neither fires. His word lifts it. The method
  has no branch and no merge road at all; the three-lane cap is his 2026-07-06 word and he is questioning it.
- **390 — the node-growth law** (Fable's consult, `docs/design/2026-07-17-node-growth-law.md`): nodes-per-file
  read from the architecture's pin column, a ratcheted every-push counter, a prover re-ask, a design-review
  split proposal. Born of exhibition-engine, whose own doc declares five nodes all pinning into one
  4017-line file. He asked for the root fix and ruled the particular case out.
- **383/384/391 — the three machine-holds-the-rule rows**: dramatization (docs arm), the vacuous-pass class,
  every net keeps its own runs/fires numbers. 391's personal arm is armed already (`~/.claude/hooks/hook-meter.py`,
  wrapping the scan; `--report` prints runs/fires).
- **387, 388, 389, 385** — the layer's own owed arms, in that order.
- **379 (bullets), 380 (reach classes to host config), 370, 381 [far]** — smaller, unblocked.
- **There is also a far tier** (row 382 gives it its law; row 381 is its first member). The what's-left
  answer leaves it out and offers it on request.

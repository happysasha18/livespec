# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-12 ~13:49, session 39 close — resume COLD from here)
**s39 CLEARED the buildable smalls backlog: ELEVEN rows landed (263, 273, 269, 264, 265, 266, 267,
268, 270, 260a, 260b) + a delta-scoped prover record, suite 490 GREEN, all COMMITTED locally —
NOT YET PUSHED (awaiting his OK; push grant is standing but the batch is large, so a nod first).**
Every row red-first proven, one lane one commit, every landed status cell carries its delegation
line. New invariants: INV-121 (derive-before-fork), INV-122 (node fitness test), INV-123 (code
compaction). Skills bumped: live-spec-base 1.0.6 (all seven working skills re-pinned), build-pipeline
1.0.14, product-prover 1.0.3, communicator 1.0.5, spec-author 1.0.3. Last commit 035c914 + the prover
record commit. Next free codes: INV-124, M-265 (read the live index before minting).

**THREE landed rows carry honestly-flagged forward legs (resume owes them, INV-26):**
- **Row 266** — the register extracted to `references/writing-register.md` (679→565 lines), but the
  Done-when's "under ~500" is arithmetically unreachable by this extraction alone (the 22-rules core is
  ~423 lines). **OWNER-CALL owed:** accept ~565, OR a follow-up row splits the 22-rules core. Recommend accept.
- **Row 270** — the derive-before-fork law is live; leg 3 ("row 259's station cites INV-121") is
  WIRED INTO row 259's Done-when and closes when 259 lands.
- **Row 260b** — the code-compaction law is live; its first real pass fires at the NEXT milestone audit
  (the 1.1.0 audit already ran at s37, before the law existed).

**Carried from s38 (still true):** branch protection set by API on the public repos; prover findings
F3-F7 still open (not yet rows); the earlier morning asks (below) stand unless answered elsewhere.
- **Branch protection** set by API on the PUBLIC repos (live-spec, track-coach, product-prover):
  force-push + deletion blocked, direct pushes allowed, admins not enforced. Closes the F5 half of
  row 231 without his click. Private repos (tlvphotos, exhibition-engine) need a paid plan — his call.
  (s38 landed rows 271/272/274/275/276/277/278 — detail in JOURNAL; all prover-confirmed, 0 must-fix.)
- **GitHub Issues stranger-door (row 261)** — recommendation recorded to DEFER; his word still closes it.

**OPEN / next:**
- **Row 279 — OWNER-DECIDES**: does live-spec's OWN tree adopt the impersonal voice (drop ~138 owner
  attributions into JOURNAL) + wire the shipped-language gate into its own pre-push/CI, OR keep
  attribution as the pack's provenance (the standing dated exemption)? Recommended default: keep the
  exemption. Also the 274-fork A/B is this row.
- **Prover findings F3-F7** (`.live-spec/checkpoints/2026-07-12-prover-spec-findings.md`) still open,
  NOT yet rows: trigger cadence, tag-symmetry, critical-on-any-door, withdrawn-decision loop, mid-work
  re-door independence. (Row 273 LANDED s39: the seam row + record-table catch-up.)
Morning s37 asks below stand unless his answers came in another window — sweep by name.

1. **Waiting HIS word (the morning asks; relay on resume if unanswered)**:
   - the ARCHITECT PRINCIPLES draft (fourteen principles, P0-P12) — rendered page opened in his
     browser; his comments route into row 259's pipeline run;
   - row 262: delegation de-dup, two OWNER-DECIDES (does the playbook keep any parallel copy;
     where the concrete task-list lives); the three divergences are listed in
     docs/audit/2026-07-12-delegation-dedup.md;
   - row 261: GitHub Issues as the strangers' wish door — DECIDE, no build yet;
   - row 247's open field leg: one REAL remote deposit from his browser (claude.ai/code) closes
     it; never self-certified (INV-94);
   - row 231's two halves: F5 branch protection (his one GitHub click) and the skill/pin
     version-alignment moments beyond MAJOR (the 1.1.0 bump left skill versions unaligned
     deliberately; INV-115 next free if it mints);
   - row 217's two human-held gaps (F4 standing anchor guard policy; F5 as above);
   - carried from before: rows 191/193 picks · D-6/D-7 · row 238 · the prover-freshness
     midnight-rollover ledger entry (recommended AGREED NON-PROBLEM, his word owed) · the INV-24
     homing observation (row-223 record).
2. **Next build work (new session, cold)**: the eleven smalls (263, 264, 265, 266, 267, 268, 269,
   270, 273, 260a, 260b) are DONE (s39). Remaining: row 259 (SURFACE, full pipeline with story
   split) — the entry impact-analysis station, BLOCKED on his design-principles comments; working
   material: .live-spec/checkpoints/pending-design-principles-architect-draft.md + the archived
   wish's two addenda + his comments. When 259 lands it MUST cite INV-121 (row 270's leg 3, now in
   259's Done-when). Then row 192 (activated 2026-07-12: scenario entry/exit contracts — its own
   movement).
3. **Blocked/waiting on others**: row 243 (README ↔ articles) waits the campaign; row 241 open
   leg runs in track-coach's window. Field legs with him: 47/96 · 54 · 165 · 168 · 134/141 ·
   143 · 144 · 140 · 117 · 129 · 133.
4. Next free codes: INV-124, M-265 at s39 close — read the live Formal index before minting;
   codes consume in landing order — reservations are dead (s37, row 233's lesson).

## CLOUD FACTS (settled 2026-07-10; row 247 landed the law, its field leg open)
A remote-agent request from a local session FALLS BACK to a local worktree; real cloud sessions
fire only from HIS browser (claude.ai/code). Bridge = brief-in-repo or brief-in-prompt; the
branch returns through git; integrated only when its FILE is on main and read to the end.
Local sub-agents never appear in his browser list (INV-67). The remote inbox arm: one new
inbox/ file per deposit, per-repo grant in the host profile, honest failure names the missing
grant (INV-112; grant-ask template at scripts/grant-ask.md).

## Standing habits (always-on)
- `date` before ANY stamp; chat leads use the prompt hook's wall clock, never extrapolation.
- No self-certification (INV-94) · no calques · plain words, codes trail (INV-28) · every ask
  hears its time range, landings settle estimate vs actual (INV-93) · a delegated run's verdict
  is the suite log's tail (INV-80) · push walk reads the CI verdict itself (INV-106) · inbox
  swept · one lane one commit · README paragraphs via clean writer (INV-84) · the leave-walk
  before any machine sleep (INV-95) · every landed row's status cell carries its delegation
  line (INV-103, suite-checked) · landings close their checkpoints (INV-107) · a rewrite that
  removes substance lists every removal (INV-109) · drafter briefs get the self-verify trio
  until row 263 lands it durably (index density · owning node · matrix-under-owner).
- Machine: caffeinate KILLED at s37 close (~04:27); re-arm it at the next night batch.

# live-spec — NEXT_STEPS (resume file: LIVE STATE + queue only; history → JOURNAL.md; ≤100 lines, INV-48)

## LIVE STATE (2026-07-12 ~11:05, session 38 close — resume COLD from here)
**1.1.0 shipped (s37); s38 landed SEVEN rows + a fresh prover record, suite 428 green, all
PUSHED to main, CI read green.** Everything through the drafter-applier pipeline (opus drafts /
sonnet applies / Opus orchestrator briefs+accepts); every landed row's status cell carries its
delegation line. Last pushed commit 739214d.
- **Branch protection** set by API on the PUBLIC repos (live-spec, track-coach, product-prover):
  force-push + deletion blocked, direct pushes allowed, admins not enforced. Closes the F5 half of
  row 231 without his click. Private repos (tlvphotos, exhibition-engine) need a paid plan — his call.
- **Row 272 (INV-115)** — the full-pass doc-compaction step states his compaction rule verbatim
  (a fact lives once, in one home; remove only redundancy; keep anything whose removal changes
  meaning; per-item judgment). **Row 271 (INV-116)** — the prover runs over ARCHITECTURE.md at the
  M-1 and M-6 gates; check-prover-record.sh gained an ARCHITECTURE.md freshness block; matrix M-255.
- **Inbox swept** — three wishes (from track-coach x2, tlvphotos x1) harvested into rows 274-276,
  files removed. Then all three BUILT this session:
- **Row 277 / F1 (INV-117)** — every session mints a stable identity at its start; the parallel-lanes
  pen tie-break orders on it; the inbox source-mark is its projection. Fixes a silent-corruption seam.
  **Row 278 / F2 (INV-76 amended)** — the worker-death verdict needs a stale heartbeat as a third
  signal (worker touches its checkpoint ~60s); a busy compute-bound worker is never declared dead.
  Both F1/F2 came from the s38 for-fun prover pass; both now FIXED and prover-confirmed non-colliding.
- **Row 274 (INV-118)** — shipped docs state requirements impersonally (rule + role-actor + reason;
  dated decision keeps the date, drops the name); the pack's own attribution-heavy spec kept under a
  dated exemption. **Row 275 (INV-120)** — a lint (scripts/check-shipped-language.py) holds the
  English + no-personal-names line on shipped artifacts, proven on FIXTURES only, NOT wired to
  live-spec's own tree (measured 126 own offences: 39 owner-name = provenance debt, 87 Cyrillic =
  mostly a prototype sketch + fixtures). **Row 276 (INV-119)** — provenance + naming convention at
  the instance→engine boundary (reconciliation-log framing, engine's own public-commit provenance,
  neutral mechanism names).
- **Two prover records** committed (5349964 for rows 271/272; 739214d for the F1/F2/274/275/276
  batch): both Ready, 0 must-fix; architecture proved each pass (discharging INV-116).
- **GitHub Issues stranger-door (row 261)** — recommendation recorded to DEFER; his word still closes it.

**OPEN / next:**
- **Row 279 — OWNER-DECIDES**: does live-spec's OWN tree adopt the impersonal voice (drop ~138 owner
  attributions into JOURNAL) + wire the shipped-language gate into its own pre-push/CI, OR keep
  attribution as the pack's provenance (the standing dated exemption)? Recommended default: keep the
  exemption. Also the 274-fork A/B is this row.
- **Prover findings F3-F7** (`.live-spec/checkpoints/2026-07-12-prover-spec-findings.md`) still open,
  NOT yet rows: trigger cadence, tag-symmetry, critical-on-any-door, withdrawn-decision loop, mid-work
  re-door independence. **Row 273** (F-arch-1 seam row, F-arch-2 record-table drift) still queued.
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
2. **Next build work (new session, cold)**: row 259 (SURFACE, full pipeline with story split) —
   the entry impact-analysis station; working material: .live-spec/checkpoints/
   pending-design-principles-architect-draft.md + the archived wish's two addenda + his
   comments; then row 192 (activated 2026-07-12: scenario entry/exit contracts — its own
   movement); then the smalls 260a, 260b, 263, 264, 265, 266, 267, 268, 269, 270 (270 = derive a
   requirement from a proven artifact before offering the human a fork — track-coach's morning
   deposit through the inbox door, swept ~08:35; the ask-never-guess twin) (opus-draft →
   sonnet-apply; row 263 FIRST is cheap and protects every later draft: the drafter self-verify
   list — index density, owning node, matrix-under-owner).
3. **Blocked/waiting on others**: row 243 (README ↔ articles) waits the campaign; row 241 open
   leg runs in track-coach's window. Field legs with him: 47/96 · 54 · 165 · 168 · 134/141 ·
   143 · 144 · 140 · 117 · 129 · 133.
4. Next free codes: read the live Formal index before minting (INV-115/M-254 were free at s37
   close); codes consume in landing order — reservations are dead (s37, row 233's lesson).

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

# Prover record — the lane branch road + self-declaring agents (CROSS-LINK ×2 + architecture lens)

**Ran under:** product-prover v2.5.0 — the *installed* copy at `~/.claude/skills/product-prover`. Diffed
against the tree's own copy (`skills/product-prover/SKILL.md`, v2.6.0): the two differ in the version
string alone, so **the lens set that ran is current**. The installed pack copy trailing the tree by one
version is a catch-up gap [A-11] outside this delta and is not filed as a finding.

**Mode:** CROSS-LINK on two new surfaces, plus the **architecture lens** (six checks), since ARCHITECTURE.md
carves a new node in the same delta and a node is a structure change that owes a re-prove.

- Surface A — the lane branch road: PRODUCT_SPEC.md ~571-596, anchors E-34, T-23, INV-198..INV-201, the
  T-18/INV-105 index rows; TEST_MATRIX.md M-372..M-382; `tests/test_lane_branch_road.py` (25 tests);
  ARCHITECTURE.md's new `parallel-lanes` node and its five seams.
- Surface B — self-declaring agents: PRODUCT_SPEC.md ~1420-1573, anchors E-31, E-32, INV-184, T-22;
  `skills/live-spec-base/SKILL.md` rule 31; `templates/agent.template.md`; `.live-spec/agent.md`;
  `tests/test_agent_channels.py`.

Whole document in view; findings scoped to the two newcomers' seams. The mandatory whole-document step for
this mode — the quantifier re-verify [INV-170] — ran and its verdicts are recorded below.

**Previous record checked (opening duty):** `docs/prover/2026-07-17-agent-communication.md`. Its 12 defects
and 3 recommendations were raised against the roster design that surface B now removes. F2 (agent-hood
constituted two ways) and F3 (the empty state misreads the machine) are **dissolved by this delta** — the
card constitutes agent-hood in one home, and the third empty state is now named. R2 (the roster's place has
no named heading) is **moot** — the roster is gone. The rest are outside these two surfaces and are not
re-litigated here.

**Primary sources.** Every machine claim below was checked by running it, never read off the prose:
the full suite (`1093 passed, 2 skipped`), the new file alone (`25 passed`), `git worktree list`,
the card and host census under `~`, the greps for the vendored line, `EnterWorktree`'s own published
contract, and `guardrails/check-config-health.sh`.

**Known context honoured.** The three design notes were read first. A hole an author already named is
ranked below one nobody saw, and the finding says which. The notes are unusually honest: `design-branch-merge-road.md`
lists six holes and eight unswept downstreams, and `design-self-declaring-agents.md` lists seven. Most of
what follows is either a named hole *verified and ranked*, or the half of a named hole the author did not
reach.

---

## Verdict

**It does not hold as written.** Six defects block. The road's two central claims — that git itself
enforces the pen's new clause, and that the branch is born from the claim commit — are both wider than the
machines that would perform them, and in each case **the delta's own suite or the tool's own contract
proves it**. The scan's flag clause cannot fire from the globs the scan states. Three findings are the
day's own lesson landing inside the paragraph written to answer it.

The craft underneath is strong, and two things are worth saying plainly. The deed-proofs are the best work
here: 25 tests driving real git hermetically, with the guarantee's **boundary pinned beside the guarantee**
and each boundary test written so that going red is good news. And `design-branch-merge-road.md` §3 refused
to carry "he is questioning the cap" into the spec because row 386's verbatim words do not say it — that
refusal is exactly the discipline the day's second lesson demands, and it caught a live fabrication before
it shipped. F4 below is that same discipline applied one section further than its author took it.

---

## Findings

| # | Finding | What the doc claims | What actually holds | Severity | Folded / rejected |
|---|---|---|---|---|---|
| F1 | **INV-198's central guarantee is wider than git gives, and the delta's own suite proves it** | "while one tree holds main checked out, every other worktree's attempt to check it out, force it, or push to it is refused by name… **the tool refuses the violation ahead of any gate the pack writes**. That guarantee rests on the primary tree holding main, which is the condition the config-health check asserts [target]." | The enumeration of three is true; the conclusion drawn from it is false, and the stated condition is insufficient. `test_update_ref_walks_past_every_refusal` (green today) moves a checked-out main from a lane worktree with `rc=0` **while the primary tree holds main** — the guarantee's own condition holding — and `test_update_ref_leaves_the_primary_tree_inconsistent` asserts the damage lands. `--ignore-other-worktrees` and `receive.denyCurrentBranch=ignore` open two more doors, both pinned green. The spec names none of the three: `grep -n "update-ref\|plumbing\|porcelain\|ignore-other-worktrees\|denyCurrentBranch" PRODUCT_SPEC.md` returns only INV-80's unrelated suite-plumbing law. The test file's own docstring says it — "a suite that pinned only the happy three would certify a guarantee wider than the one git actually gives" — and TEST_MATRIX M-375 says it, so **the suite and the matrix are honest and the law they test is not**. Consequence: a lane agent or a script reaching for `git update-ref refs/heads/main <sha>` (the test's own docstring: "plumbing is what a script reaches for") moves main while another lane holds the pen; INV-198 says no gate is needed, so none is written; the config-health check [target] asserts only that the primary tree holds main, which is TRUE in that scenario and passes green. The pen's central clause — "holding the pen is the sole right to move main" — is unheld, and the day's lesson lands exactly here: the law delegated its machine to git, and git looks at three porcelain roads. **Nobody named this**; the design note named only the narrower "no tree holds main" lapse. Fix: INV-198 names the guarantee's real scope (git refuses the three porcelain roads and leaves `update-ref`, `--ignore-other-worktrees`, and `receive.denyCurrentBranch` open), then either (a) routes the residual to a gate row — config-health reads main's reflog for a move made from a lane worktree — or (b) states by a decided sentence that the open doors sit outside an agent's habit and accepts the risk by name. Prefer (a). | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F2 | **T-23's branch birth contradicts both tools that would perform it** | T-23: "A lane branch is born from the claim commit, on main… the branch is cut from that commit." E-34: a worker lane takes its worktree through `isolation: "worktree"`, "and the worker's brief names the branch its work rides." | `EnterWorktree`'s published contract: "The base ref is governed by the `worktree.baseRef` setting: **`fresh` (default) branches from origin/<default-branch>**; `head` branches from your current local HEAD." No `worktree.baseRef` is set in `live-spec/.claude/settings.json` or `~/.claude/settings.json` (verified), so the default rules. The claim commit is a **local** commit on main under the pen; the spec's own non-goals say "no lane branch pushed anywhere", and nothing states the claim is pushed. So a session lane entered by the tool is cut from `origin/main` — a commit predating its own claim — and T-23's first step is false as performed. The subagent road is worse: the Agent tool's `isolation` option takes **no branch and no base parameter at all**, so E-34's "the worker's brief names the branch its work rides" is a duty with no mechanism — a brief cannot name what the tool does not accept. Consequence: the lane's own claim is absent from its branch; the rebase at integration re-applies it so the tree self-heals, and the stated birth was never performed — which leaves `git branch --list 'lane/*'` reading names the tool chose and the merge-base check's semantics derived from a birth that did not happen. **Half-named**: the design note named the subagent branch behaviour as unverified ("What branch it lands on by default… I did not verify"); nobody named the `baseRef` half, which is stated in the tool's contract and needed no probe. Fix: state the birth as an act the lane performs with plain git — `git worktree add -b lane/<row>-<slug> <path> <claim-sha>`, the exact shape `tests/test_lane_branch_road.py:68` already proves — and name `worktree.baseRef: head` as a setting a host taking the tool road vendors beside INV-201's line. The suite proves the plain-git road; nothing proves the tool road. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F3 | **The scan's flag clause cannot fire from the globs the scan states** | INV-184: "The scan reads **two globs** under each of its roots — `<root>/*/.live-spec/agent.md` and `<root>/*/*/.live-spec/agent.md`." The flag clause: "the scan's report names each live-spec host it found carrying no card, **which the same globs already listed**." | The globs match `agent.md`. A host carrying no card matches neither, so the globs list no such host and the flag has nothing to name. Verified on this machine: `ls -d ~/*/.live-spec/agent.md` returns **one** path (live-spec); finding the six hosts needed a third pattern, `ls -d ~/*/.live-spec` — `exhibition-engine`, `live-spec`, `promoter-alexander`, `promoter`, `tc-cloud-validate`, `tlvphotos`. So five of six standing hosts are invisible to the stated scan, and the clause written to make that gap visible reads a set that does not contain them. Consequence, today: an agent on `~/live-spec` meeting something in tlvphotos' zone scans, finds one card (its own), lands on the facets block's first empty state — "a scan finding only the reader's own card answers that the reader is the only declared agent, **which is a true answer under this scenario's own law**" — and concludes it is alone on a machine running six, two of which already exchange inbox files. It then takes its concern to the pack as default owner [INV-197], which is itself; the routing law's answer is self-addressed and no clause reds. **Half-named**: the design note named the under-report's magnitude squarely ("the single biggest practical hole"). Nobody named that the flag's own mechanism cannot see it — the day's lesson again, a machine looking in the wrong place. Fix: state the host globs (`<root>/*/.live-spec`, `<root>/*/*/.live-spec`) beside the two card globs, and correct the budget's "two globs" to four; the report then names cards found AND live-spec hosts carrying none, which is what the flag clause already promises. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F4 | **INV-201's live-spec line is attributed to a word the owner never spoke** | INV-201: "Each host's line **records that host owner's word** for that host's tree, and **live-spec's own line rides the owner's 2026-07-17 request**." | Row 386 records his verbatim words: *can we not run different agents in different branches in parallel? why do we wait? why is this written nowhere?* and *there are commands in Claude Code for each agent to work on its own tree isolated, verify.* Neither authorizes a vendored project-instructions line. The chain runs: INV-201 → row 386(a)'s "his word today lifts it, recorded as a standing profile line" → verbatim words carrying no lift. The profile line does not exist (verified: no such line in `~/.claude/playbook/personal/profile.md`), and `design-branch-merge-road.md` §7.6 confirms it was never written. The weight is what makes this block rather than queue: `EnterWorktree` treats a project instruction as authorization **equal to the user's word**, so the vendored line does not merely record his word — it **stands in for it**, at every future worktree entry, unattended. A line whose authority is a reading of "why do we wait?" becomes a standing permission the tool honours. This is row 415's own class, minted today at his own catch, landing in the delta written the same afternoon. The design note refused exactly this class for the cap and did not sweep its own section for the same shape. Fix: rewrite the live-spec sentence in the pack's voice — the line records the pack's judgment that the road he asked about needs the tool's authorization, and his word **on the line itself** is owed the way T-18's cap re-read already marks its own recommendation [INV-4]. | **defect** · false claim (consistency) | OPEN — for the landing session |
| F5 | **Three of the four [target] machines are netted by a station structurally unable to read them** | "The other four are this road's build half and stand [target] until row 386's build lands, **with the prover's station as their net meanwhile** [INV-150, INV-101]." INV-199 repeats it: "the prover's station being their net meanwhile". | The prover reads **documents** — the skill's own boundary says so twice ("it reads documents", "NOT for code or diffs"). Three of the four machines have facts about the **machine at a moment** as their subject: a lane worktree with no open queue row, a primary tree that does not hold main, a fourth open lane. No document carries any of them, so no prover pass can see one. This pass could only check them by running shell commands, which is not the station's job and is not repeatable as one. Verified that the machines are absent: `guardrails/check-config-health.sh` contains **zero** occurrences of "worktree"; the merge-base check exists only as `merge_base_equals_main_tip`, a helper method inside the test class (`tests/test_lane_branch_road.py:187`) that no gate calls. Consequence: the road ships with the honest-sounding label "netted by the prover" over three laws no reader of any document will ever enforce, and a stale lane worktree sits on the machine until a human notices. The fourth (the adoption gate for the vendored line) genuinely is document-readable and the station does hold it. **The predicates-not-gates half was named** in the brief and the design note; **the mis-assignment of the prover as their net is unnamed**. Fix: INV-198's and INV-199's [target] clauses name their net as **none until row 386's build lands** — an accepted, dated gap — rather than naming a station that cannot reach them. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F6 | **T-23's code is already claimed by ROADMAP row 398** | The delta mints T-23 = the lane's branch walk. `design-self-declaring-agents.md`: "INV-198 / E-34 / T-23 **stay free**." | ROADMAP row 398's Done-when: "red-proven on a fixture prompt naming a foreign zone (**T-23**: the fixture deposit lands in the fixture tree with the one-line notice)". Row 401's INV-198 collision was caught by `design-branch-merge-road.md` §0 and has since been re-minted (verified: row 401 now reads INV-202). The T-23 collision was not caught, and one design note affirmatively records the code as free. Consequence: row 398 lands and either takes an anchor the spec already owns — `test_spec_index_unique_anchors` reds — or a session silently re-points it, which is the collision class row 384 exists to catch. Cheap to fix and cheap to miss. **Unnamed, and asserted false.** Fix: re-mint row 398's T-23 to a free code in this landing, the way row 401's INV-198 became INV-202, since this delta is the one taking the code. (E-34 is claimed by the PLAN for row 396's coordination board, but the PLAN is a scratchpad rather than a tree artifact, and ROADMAP carries no E-34 — no fix owed, worth one line to the next hand.) | **defect** · internal-conflict (consistency) | OPEN — for the landing session |
| R1 | **E-34's subagent grant is untested, and its one claim rests on a reading nothing re-reads** | E-34: "A lane delegated to a worker takes one today with no permission of any kind, because the Agent tool's `isolation: "worktree"` option **carries no gate**." | The claim is **true today** — I read the tool's published contract: `isolation: "worktree"` gives the agent its own git worktree, with no permission language anywhere. So nothing is false and this queues rather than blocks. The gap is durability: nothing in the 25-test file drives the Agent tool, and nothing can, since pytest has no harness for it. When the harness adds a gate to that option, every test stays green and the law goes silently false — the exact structure INV-198's deed-proofs exist to prevent, in the one place a deed-proof is impossible. And by INV-201's own admission the session road is shut until the vendored line exists, so this untested road is **the only usable road today**. **Named**: `design-branch-merge-road.md` §8 named it squarely and recommended the fix. Fix: take the design note's own recommendation — a live two-lane run is row 386's first build act, and its report is the deed. Until then E-34's clause carries a dated verification stamp naming the tool contract read, the way INV-198's clause carries "(verified 2026-07-17 on a probe repo)". | recommendation · now · hard-to-monitor (observability) | OPEN — for the landing session |
| R2 | **INV-200 never says how a lane notices a semantic conflict** | INV-200: "a semantic conflict surviving a green suite on the rebased tree is a fact no test covers, which is a matrix gap and routes to the matrix's own home rather than earning a net invented here [INV-73, E-15]." | The routing is right and the honesty is real — the law claims no net it does not hold, and says so. The missing half is that **no lane has an occasion to look**: two lanes land code that passes the suite on each rebased tree and composes wrong, and nothing reds, nothing reports, nobody reads. "Routes to the matrix" answers who owns the coverage gap; it does not answer who notices the instance. **Named**: the design note named it in these words — "it does not say how a lane *notices* it has one." Nothing stated is false, so it queues. Fix: name the residual's one available signal — the landing report names what this lane's delta touched that another lane also touched in this movement, which the dependency graph already computes [INV-49] — or state plainly that no detection exists and the risk is accepted at the cap of three. | recommendation · now · hard-to-monitor (observability) | OPEN — for the landing session |
| R3 | **TEST_MATRIX's "Owed" note went stale during this pass** | TEST_MATRIX.md:30 — "**Owed:** `.live-spec/profile.md`'s `project.proofs` line still reads that no fact needs a browser-computed rung, which this road makes stale. That line's home is the host profile, so its correction belongs to the hand that holds it." | The hand that holds it wrote it **while this pass ran**: `.live-spec/profile.md` was absent from `git status` at my first call and present at my second, and now carries "**Grown 2026-07-17, the lanes landing:** the engine rung is occupied", naming the deed rung and the three git facts. So the matrix's note now claims a debt already paid — the brief's "stale profile line" is fixed and the note about it is what is stale. Trivial, and reported because a live tree makes it easy to leave behind. Fix: drop the Owed sentence, or repoint it at what remains owed. | recommendation · now · consistency | OPEN — for the landing session |
| R4 | **A new law cites a row carrying a known fabrication** | E-34: "That is the road the owner asked for by name on 2026-07-17, and it is open now (**ROADMAP row 386 records his words**)." | Row 386 does record his verbatim words, so the citation is sound and E-34's own sentence is fair — he did name branches and parallelism. But the same row also carries "he is questioning it now" and "**His ranking, kept: this matters more than the communication layer, and it waits until the communication layer has run in the field**" — which ROADMAP row 415, queued today at his own catch, documents as invented: "no message of his, on any day, ranks parallel lanes above the communication layer or makes them wait for a field run". Row 386 is pre-existing (line 291, untouched by this delta), so by the delta-scoped gate [INV-114] it queues under row 415's sweep and never blocks the landing it did not create. Worth one line because this delta points two new anchors at that row as their authority, and the next hand reading row 386 for "his words" meets both the real ones and the invented ones in one cell. Fix: none owed here — row 415 owns the sweep and names the tree's existing attributions as its first act. | recommendation · later · consistency | OPEN — rides row 415 |

**Counts:** 6 defects · 4 recommendations · 0 open ⟨DECIDE⟩. Every defect carries a derived fix with a
stated preference; none rests on a fact only the owner holds. F4's fix hands him a question (his word on
the vendored line) without holding the landing on it, by INV-4's proceed-on-recommended arm.

---

## The quantifier re-verify [INV-170] — the mandatory whole-document step for this mode

Every enumeration and universal in the two newcomers' reach, re-read against the surface set including them.

| Sentence | Home | Verdict |
|---|---|---|
| "every other worktree's attempt to check it out, force it, or push to it is refused by name" | INV-198 | **clean as enumerated** — all three verified green by deed. The *conclusion* drawn past the enumeration is F1. |
| "the tool refuses the violation ahead of any gate the pack writes" | INV-198 | **hit** — F1. "The violation" ranges wider than the three roads git guards. |
| "The scan reads **two globs** under each of its roots" | INV-184 | **hit** — F3. Two globs find cards; the flag clause needs two more to find card-less hosts. |
| "which the same globs already listed" | INV-184 flag clause | **hit** — F3. The globs listed one card and zero hosts. |
| "no permission of any kind" / "carries no gate" | E-34 | **clean as written** — verified against the Agent tool's published contract. Durability is R1. |
| "The other four are this road's build half… with the prover's station as their net" | INV-198/199 machines para | **hit** — F5. Three of the four are not document-readable. |
| "Exactly two channels carry everything that passes between two agents" | INV-183 | **clean** — untouched by both newcomers; the scan reads, and reading is not a channel. |
| "No file outside any tree describes any agent" | INV-184 | **clean** — verified: the roster is gone from the profile's reach, and the scan writes nothing. The delta's strongest sentence, and it holds. |
| "durable state, a standing mission, and a zone of its own make a capability an agent" | INV-182 | **clean now** — the previous record's F2 (two constitutive tests) is dissolved: T-22 no longer says ratification creates the agent, and the card declares it. |
| "a tree's presence on a filesystem grants nothing" | INV-152 / INV-184 | **clean** — and consistently applied: the five card-less hosts are correctly *not* agents by this law. F3 is about the flag rather than this rule. |
| "the cap holds at three… [default]" | T-18 | **clean** — stated as the pack's re-read and recommendation, his word owed, work proceeding [INV-4]. Correctly attributed; see Phase 3.5. |
| "a lane's branch is born from the claim commit" | T-23 | **hit** — F2. Neither tool that opens a lane performs it. |
| "every document on the pen's list stays under the pen" | INV-198 | **clean** — the pen's list is unchanged and the argument for keeping it ("no suite reads a proof") is sound and load-bearing. |
| Formal index completeness | PRODUCT_SPEC.md index | **clean** — `test_every_new_anchor_carries_an_index_row` pins all six; verified green. T-23's *uniqueness across the roadmap* is F6. |

---

## Mandatory sweep verdicts — surface × sweep

All three CRUD / invariants-per-state / authorization tables go N/A for this delta: live-spec is a
single-human local text product with no user-mutated persistent entities and no roles. The surface × sweep
table stands in their place [INV-171].

| Sweep | Surface A — the lane branch road | Surface B — self-declaring agents |
|---|---|---|
| Declared cross-cutting laws [INV-101] | **hit** — F5. The three declared laws (register, clock-honest stamps, no self-certification) are each met; the *net-per-law* arm is where it breaks: three machines name a net that cannot read them. | **clean** — the register governs the card and the chat answer; the scan's dated lines carry stamps; T-22 closes self-certification by naming the missing ratification gate as owed rather than claiming one. |
| Edge-condition completeness [INV-138] | **hit** — F1 (the guarantee's range at its open end: what holds when the road is plumbing rather than porcelain). The named-part ask is answered for the porcelain three and silent for the remainder. | **clean** — the two-level bound names both ends and ships with its escape hatch (a deeper nester names the deeper directory as a root). |
| Cross-surface policy uniformity [INV-125] | **clean** — the pen's policy is stated for the class (every shared document) rather than for one member, and the branch grain is derived from the existing clause rather than written beside it. | **clean** — the card law is stated for every tree, and the delta swept every home (spec, base rule 31, template, the pack's own card, tests). Zero "roster" left in the spec body, verified. |
| Lifecycle [INV-168] — payload, entry symmetry, entry state, paired transitions, persistence, scenario edges | **hit** — R2 (the paired transition open↔land is stated in both directions; the *conflict* branch of the return path names its nets and leaves detection blank). Teardown's inverse is stated and deed-proven; the parked-lane fork is named. Persistence: a lane branch is short-lived by non-goal, so no version-skew case exists. | **clean** — entry (a tree writes its card) and exit (a declined proposal leaves no tree and no card) are both stated; the three empty states are each named with their own answer; re-entry is a fresh scan by construction, since no index caches state to resume. |
| Unwritten seams [INV-72] | **hit** — F2 (the seam between the law's stated birth and the two tools that perform it was never written); F5 (the seam between a [target] machine and its interim net). | **hit** — F3 (the seam between the scan's globs and the flag's promised report). |

---

## Phase 3.5 — Acknowledged gaps

Gaps the delta itself flags. These carry no kind and are not new discoveries.

**A1 — INV-105 is one anchor carrying two unrelated facts.** ARCHITECTURE.md names it in its own words:
"the state-directory anchor is one anchor carrying two unrelated facts, the canonical `.live-spec`
directory and the worktree-isolation default… so it sits here with its leading fact and its stated category
while the lanes node owns the mechanism that default fires." The author saw it, decided to keep it, and
stated the reason — a split would move a shipped anchor every host has vendored, and the architecture's
seam row (`fence + identity → the pen`) carries the ownership honestly. My read: the decision is right for
now and the note is the right size. The day it costs something is the day INV-105's isolation half is
reworded and the `.live-spec` half moves with it; a split then is a rename with a migration, which is
row-shaped work rather than a fold here.
`acknowledged · boundary-issue (composition)`

**A2 — the cap holds at three with no measurement behind it.** T-18: "The artifact that would move it is a
measurement the pack has never taken — pen-wait time per lane and re-fences per landing… This paragraph is
the pack's re-read and its recommendation; the owner's word on the recommendation is owed, and the work
proceeds on it meanwhile [INV-4]." This is the correct road and the correct voice, and it is the one place
in the delta where an attribution was actively refused rather than inherited. The cost model it argues
(worktrees remove the tree's cost; pen-wait, rebase-and-re-gate, and dividing attention survive) is sound
and I have no counterexample. The residual the section names itself — no session can see another session's
pen-wait, so a repo with several live windows is pen-bound in a way no lane count reads — is real and live
today: several windows share this repo right now.
`acknowledged · missing-outcome-check (postcondition)`

**A3 — no gate reds on a card whose founding carries no ratification.** T-22 names it: "No gate reds today
on a card whose founding carries no ratification, and this sentence owes one [INV-150]." The design note
declined to invent one, correctly — a gate here needs a ratification record to check against, and nothing
today defines one. The detection road the spec does state ("a card the owner never authorized appears in
the same scan that finds every other") is honest and is genuinely better than a list would offer. My read:
this is a row rather than a fold, and it is smaller than F3 — a false card is a hypothetical, while the
under-report is the machine's state today.
`acknowledged · missing-rule (invariant)`

**A4 — a card's authenticity rests on the tree it sits in.** Named in the design note rather than the spec:
no signature, no identity proof; out of scope for one machine with one human, a real gap the day a tree
arrives from somewhere else. Agreed on both halves. Worth a spec non-goal line so the boundary is in the
shipped text rather than only in a scratchpad the next session will not read.
`acknowledged · boundary-issue (composition)`

---

## Closing

**Top 6 to fix before this lands.** F1 (INV-198 claims a guarantee git does not give, and the suite proves
it) · F2 (T-23's branch birth is performed by neither tool) · F3 (the scan's flag cannot fire from the
scan's globs) · F4 (INV-201 attributes a vendored line to a word he never spoke) · F5 (three machines named
a net that cannot read them) · F6 (T-23 collides with row 398).

**Properties to state explicitly**, ready to paste:

- "Git refuses the three porcelain roads — `checkout`, `branch -f`, `push` — to a branch another tree holds
  checked out, and leaves `update-ref`, `--ignore-other-worktrees`, and `receive.denyCurrentBranch=ignore`
  open; the pen's clause rests on the three and names the rest as an accepted, dated gap [INV-198]."
- "A lane's branch is cut by `git worktree add -b lane/<row>-<slug> <path> <claim-sha>`, naming the claim
  commit as the base explicitly, because every tool default bases a new worktree elsewhere [T-23]."
- "The scan reads four globs under each root — two for cards and two for live-spec hosts — so its report
  names both the agents it found and the hosts that have not declared themselves [INV-184]."
- "A [target] machine whose subject is the machine's own state carries no interim net, and the gap is dated
  rather than assigned to a station that reads documents [INV-150]."

**Open questions only the owner can answer.** One, and it does not hold the landing: does his 2026-07-17
word authorize live-spec's vendored worktree line, or is the line the pack's own judgment awaiting his word
(F4)? The pack should proceed on the recommended arm [INV-4] and record the line in its own voice until he
speaks.

**Queued for a taste call.** R1 (E-34's untested grant — take the design note's live two-lane run as row
386's first build act) · R2 (INV-200's undetected residual) · R3 (the stale Owed note) · R4 (rides row 415).

**[default]-tagged count.** This is a CROSS-LINK pass, so the whole-document `[default]` sweep is not owed.
Within the delta: 4 new `[default]` tags — the cap at three (T-18), the branch road's success measure
(T-23), and the two scenarios' success measures and facets (F-roster, F-agent-birth). Each is
correctly tagged and none is stale.

**Readiness: needs another iteration.** Six defects, all with derived fixes and none needing the owner's
word to fold. The road's shape is right, its argument for keeping documents under the pen is the delta's
best thinking, and its deed-proofs set a bar the rest of the pack should meet. What blocks is that three of
its laws describe machines that do not do what the laws say — which is the day's own lesson, arriving in the
paragraphs written to answer it.

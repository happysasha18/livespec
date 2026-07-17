# Prover record — the agent-communication layer (CROSS-LINK + architecture lens)

**Ran under:** product-prover v2.6.0 (pack VERSION 2.6.0, base `live-spec-base` v2.6.0). Lens set current.

**Mode:** CROSS-LINK — the new surface `## When agents work together` (PRODUCT_SPEC.md ~1393-1541; features
F-roster, F-contract, F-agent-ask, F-agent-birth; anchors E-31, E-32, E-33, INV-182..INV-197, T-22) proved
against the named existing surfaces it composes with. Plus the **architecture lens** (six checks), since
ARCHITECTURE.md changed in the same delta. Whole document in view; findings scoped to the newcomer's seams.
The mandatory whole-document step for this mode — the quantifier re-verify [INV-170] — ran and its verdicts
are recorded below.

**Previous record checked (opening duty):** `docs/prover/2026-07-17-2.5.0-minor-gate.md`. One unfolded row
rides forward: R1 (INV-138's bold lead header under-describes its broadened clause; `recommendation · later`,
non-blocking, queues). Nothing in this delta touches it and it is not re-litigated here.

**The design's purpose, judged against:** keep the channel quiet — stop agents manufacturing traffic — while
letting the necessary thing across. Bogus agent-to-agent communication is the owner's named main problem.

**Known context honoured:** the 2026-07-17 adversarial audit's 13 findings were read first. Its folded items
(the [target] tags on INV-184/INV-185 with rows 387/385, the INV-41/INV-86/INV-117 citation corrections, the
ROADMAP 371-378 re-statement, the template's inventory row, the derived rule count, the rewritten
count-checks) are not re-litigated. F7 and F9 below report where two of those folds landed in one home and
left an identical claim standing in another — the fold is right and its sweep is short. Its queued items
(rows 385, 387, 388, 389) are queued correctly and are not re-filed.

---

## Findings

| # | Finding | What the doc claims | What actually holds | Severity | Folded / rejected |
|---|---|---|---|---|---|
| F1 | The concern message has no birth, and the shipped gate reds it | INV-197: a concern no zone owns goes to the pack's inbox, and the work never stalls. INV-189: "A message has exactly two births, and the set is closed" — blocked by the receiver's zone as it stands, or a fault lived in the receiver's zone. | Neither birth covers the concern. Birth one needs the sender's work standing still, and INV-197 orders the opposite ("does the reasonable thing now… marks that work provisional"). Birth two needs a fault lived *in the receiver's zone*, and the concern's defining property is that no zone — the pack's included — owns it. `guardrails/check-earned-message.py` (wired into `guardrails/pre-push:108`) accepts `Blocked:`, `Lived:`/`Fault:`, `Re:` and nothing else. A track-coach session filing a cross-project-measurement concern into `~/live-spec/inbox/` either writes a `Blocked:` line its own law says is false, or the pack's pre-push reds and the concern never lands. | **defect** · direct-contradiction (contradiction) | OPEN — for the landing session |
| F2 | Agent-hood is constituted two ways | INV-182: "durable state, a standing mission, and a zone of its own make a capability an agent". F-roster's fence bullet + T-22: each half of a pair becomes an agent "when the owner ratifies its roster row"; "The owner's ratification is the act that creates the agent". | Two constitutive tests for one kind, in two homes, disagreeing on every unratified tree. ~/track-coach carries durable state, a standing mission and a zone: an agent by INV-182, not an agent by T-22, and INV-184 says a lookup against it "reports the absence". The laws that bind only "between two agents" (INV-183, INV-194) therefore bind nothing on this machine today, while `check-earned-message.py` binds every `from-<agent>` deposit regardless of any row — the gate and the law range over different sets. Preferred fix: INV-182's properties constitute agent-hood, the ratification authorizes the ROW and the roster RECORDS it; T-22's "the act that creates the agent" becomes "the act that seats it". | **defect** · internal-conflict (consistency) | OPEN — for the landing session |
| F3 | The empty state misreads the machine it lands on | F-roster facets: "a profile with no roster reads as a single-agent machine and the lookup says so". | Primary-source check: `~/.claude/live-spec/profile.md` has no roster; `~/live-spec`, `~/track-coach`, `~/tlvphotos`, `~/promoter` all exist, and two of them already exchange inbox files. On landing day every lookup on this machine answers "single-agent machine" — false, and the answer INV-184 makes each agent read first. The migration clause creates this state by design (rows come at each catch-up), so the third case — agents exist, rows not yet ratified — is the normal state for the layer's whole first period, and no clause names it. Fix: name the third case (an unrostered machine reads as unknown, not as single-agent) and state the read's answer there. | **defect** · missing-scenario (state-space) | OPEN — for the landing session |
| F4 | The message identifier is per-session, so the two-crossing bound cannot count | INV-192: "A message carries a stable identifier its reply can name. The identifier is a projection of the sender's session identity [INV-117]". INV-196: the bound is two, "counted by the identifier the exchange carries [INV-192]". | INV-117's identity is minted per SESSION and "a projection" is defined at that home as its leading characters. So one session's two messages to one receiver carry one identifier and count as one exchange — the second question's first crossing reads as the exchange's second, and its reply escalates to the owner as a question the agents "could not settle". And a re-send from a fresh session mints a new identity, so the count resets with no rewording at all, which is the one evasion INV-196 explicitly forecloses. The identifier must be per-message (session identity + a per-message discriminator) with the exchange keyed to the first message's id, which the reply already names. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F5 | The gate's trigger has no spec home, and the spec's own naming law admits a bypass | INV-189's net is a mechanical gate (base rule 31 names `check-earned-message.py`; ARCHITECTURE's F-agent-ask flow: "the receiving sweep's gate reds while an unearned file sits in the inbox"). The message is "named and shaped as every inbox item is [E-11]". | The gate fires on the `from-` prefix alone (`check-earned-message.py:202`), and that prefix's only home is `inbox/README.md:15-17`; PRODUCT_SPEC.md contains zero occurrences of `from-<agent>` / `from-owner`. E-11's stated form is `YYYY-MM-DD-<source>-<slug>.md`, which permits `2026-07-17-track-coach-orphan-child.md` — a spec-conformant agent deposit that the gate, by `inbox/README.md:34`, reads as outside agent traffic and never checks. The declared mechanical net is bypassed by a filename the spec itself allows. Fix: E-11's naming clause states the `from-<agent>` source form and the two reserved words, so the gate's trigger is spec-backed. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F6 | "The only data path" forbids the evidence the fault message owes | INV-185: "the published artifact is the only data path that exists between two agents [INV-183]". INV-189: a fault message "names the fault and the evidence the sender lived: what it ran, what happened, and how the fault showed itself". | The two rules cannot both hold. Read as written, the layer's own worked example — the track-coach deposit of 2026-07-17 carrying its orphaned-child evidence — is illegal, and INV-189's second birth can never produce a legal file. The sentence's intent is the producer's product data; its range is every byte crossing. Fix: scope it — the published artifact is the only road for a producer's product data — leaving a sender's own lived evidence outside its range. | **defect** · direct-contradiction (contradiction) | OPEN — for the landing session |
| F7 | The [target] fold swept the bodies and left the same present-tense claim in two other homes | Formal index, INV-185 row: a permission-less field "stays home, **held by a mechanical gate on the producer's suite**". Formal index, INV-184 row: "a tree with no card **is flagged** at founding and at adoption's orient". ARCHITECTURE's F-contract fallback column: "the producer's suite reds on a permitted-less field… the cadence's watcher reds… the consumer's freshness check reds… the compatibility test reds". | The bodies of INV-184 and INV-185 carry [target] against rows 387 and 385, correctly (the audit's fold). None of these gates exist: `grep -rln "agent\.md\|roster" guardrails/ adopt/ scripts/ hooks/` returns `tests/test_agent_channels.py` alone, and row 385 states the contract's three arms are unbuilt on purpose. The identical false present tense stands in three places the fold did not sweep — a session reading the index or the architecture's fallback column learns the gate ships today. Class fix: sweep every home of a [target]-tagged claim, index rows and ARCHITECTURE's fallback column included. | **defect** · false claim (consistency) | OPEN — for the landing session |
| F8 | The architecture excludes host-contract from the feature layer and then names it twice | ARCHITECTURE.md:108 — "The infra machines (guardrails, host-contract, package-docs) implement guarantees rather than user features, and **sit outside this layer** by the project type's own definition." | The two new rows F-roster (`host-contract, base-rulebook`) and F-agent-birth (`build-pipeline, host-contract`) place host-contract inside the layer the sentence excludes it from. `tests/test_traceability.py` checks only that a named node is real, so it stays green while the doc's own paragraph and its own table disagree. Before this delta no feature row named host-contract, so the divergence is delta-scoped and blocks. Fix: the sentence narrows to guardrails and package-docs, or names host-contract's feature-implementing arm as its exception. | **defect** · internal-conflict (consistency) | OPEN — for the landing session |
| F9 | Base rule 31 counts four laws and lists six | `skills/live-spec-base/SKILL.md:340` — "Four laws hold the quiet, and each is a way of routing a thing to the home that governs it [INV-153]." | Six bullets follow: the earned message [INV-189]; the referral and the drop [INV-190, INV-191]; data-never-travels with default-deny [INV-188, INV-185]; the agent's own recognition [INV-195]; the two-crossing bound [INV-196]; non-duplication with the proposal law [INV-194, INV-193]. No test asserts the number, and this is the file every agent loads to learn the layer. The same class the audit folded ("the base description's rule count derived rather than pinned"), one file over. Fix: derive the count or drop the number. | **defect** · false claim (consistency) | OPEN — for the landing session |
| F10 | INV-197's owning node never states it | ARCHITECTURE.md:43 lists INV-197 among base-rulebook's owned facts, pinned to `skills/live-spec-base/SKILL.md`. The architecture lens's first check: every spec fact is owned by exactly one node. | `grep -rn "INV-197" skills/` returns nothing; so does a search for the law's words ("no agent's zone owns", "default owner") across `skills/`. Eleven of the twelve base-owned new anchors are written into rule 31; INV-197 alone is absent, so the pack-as-default-owner road and the never-stall clause exist only in PRODUCT_SPEC.md, which a working session does not load. `tests/test_agent_channels.py:1069` passes because `assert_index_and_ownership` (`:78-83`) checks the index row and the count of claiming nodes — never that the owning node's file carries the fact. This is the audit's finding-5 shape (a test asserting the spec sentence alone) surviving in one more place. | **defect** · boundary-issue (composition) | OPEN — for the landing session |
| F11 | F-contract is the runtime flow that cannot be walked | ARCHITECTURE.md:151 walks F-contract; INV-74 demands the doc walk the running product, naming which node serves each step, and give every named failure point its fallback. | Four of the seven hops name no node: the owner's per-field permission record, the producer's clock regenerating at cadence, the freshness check, and the analysis. They name none because they belong to a producer and a consumer that do not exist — row 385 says so plainly ("this pack contains no data producer"). The other three new flows walk end to end through real nodes; this one describes a host's future product in the present tense, and its fallback column (F7) states four gates that ship with row 385. Fix: mark the F-contract flow [target] against row 385 and state the walk in the conditional until a real producer exists, the way the guardrails and snapshot nodes carry their [target]. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| F12 | The cadence watcher cannot fire in the failure it watches | INV-186: "The cadence is a budget, so it names its watcher: the producer's own check reds when its scheduled regeneration did not run [INV-41]." INV-41's home: the watcher is "the mechanical check that reads the real number and reds past the stated one, so the budget cannot silently rot". | The spec never says where the producer's check runs. The failure it targets is the producer's own machinery having stopped — a dormant window, a dead cron — and a check hanging off the producer's own suite or session runs exactly when that failure is absent. The consumer's staleness bound (INV-187) is the only thing that actually reds, and by INV-186's own two-numbers clause it measures a different thing and answers to a different owner. Fix: state where the cadence check runs (the producer's session-start sweep, beside the update check [E-25]), or take INV-41's other arm — a decided sentence naming the consumer's staleness red as the cadence's real net. The instrumentation home INV-41 also demands is unstated for both budgets; the artifact's generation stamp and the consumer's freshness report are the honest candidates already in the text. | **defect** · unenforceable-promise (discharge) | OPEN — for the landing session |
| R1 | The routing principle's homeless-outcome list does not name the newcomer's arm | INV-153 (line 411): "a thing that pins to no home is itself the finding, so nothing is homeless by silence", then four outcomes — one plain question, a broken invariant, the seat, the drop. | INV-197 adds a fifth outcome (a homeless concern takes the pack as default owner) and INV-153's list does not carry it, so the principle's own home teaches four of five. Nothing stated is false — the list does not claim exhaustiveness — so it queues. The growth from three controls to four is otherwise sound: the four are named, each with its own verifier, and the earned message genuinely is the same principle across a window's edge. | recommendation · now · consistency | OPEN — for the landing session |
| R2 | The roster's place inside the profile has no named heading | INV-184: "The roster lives in the human's personal profile, one line per agent — a name and a tree path", read by every agent before it acts. | The file is ~200 lines and the roster has no stated heading or key, so a reader cannot distinguish "no roster" from "a roster under a heading I did not look for" — which is F3's empty state resolved by guesswork. Two ratification sessions can also write two roster blocks in one file, each legal, and the concurrent-edit fence [INV-11] guards the write rather than the location. Fix: name the block the way `project.kind` names a key, and state it at E-32 where the line format already lives. | recommendation · now · hard-to-operate (ops-ux) | OPEN — for the landing session |
| R3 | Write-ownership's one exception is worded for wishes, and the reply is neither a wish nor feedback | INV-10's home (line 1855): "It has exactly one exception: creating a new wish file in the inbox." The new fences claim "write-ownership grants the one new file and nothing beyond it [INV-10]". | E-11 already carries wishes AND feedback, so the wording is stretched before this delta and the finding is largely pre-existing — it queues by the delta-scoped gate [INV-114] rather than blocking. The newcomer widens it: a reply carrying a terminal state is a third kind, neither a wish nor feedback, written into a foreign tree. Fix: the exception names "one new inbox file", which covers every kind the door already admits. | recommendation · later · over-specific (abstraction) | OPEN — for the landing session |

**Counts:** 12 defects · 3 recommendations · 0 open ⟨DECIDE⟩. Every defect carries a derived fix with a
stated preference; none rests on a fact only the owner holds.

---

## The quantifier re-verify [INV-170] — the mandatory whole-document step for this mode

Every enumeration and universal in view, re-read against the surface set including the newcomer.

| Sentence | Home | Verdict |
|---|---|---|
| "Exactly two channels carry everything that passes between two agents" | INV-183 | **clean** — the reply rides the inbox in the other direction; the count is of channel kinds, not directions, and INV-192 adds no transport (the arms are E-11 / INV-10 / INV-174 / INV-112, unchanged). No third channel is introduced. |
| "A message has exactly two births, and the set is closed" | INV-189 | **hit** — F1. The reply is carved legally (INV-192 states it inherits the birth of the message it discharges and names its identifier); the concern is not carved at all. |
| "the published artifact is the only data path that exists between two agents" | INV-185 | **hit** — F6. |
| "The infra machines (guardrails, host-contract, package-docs) … sit outside this layer" | ARCHITECTURE.md:108 | **hit** — F8. |
| "Four laws hold the quiet" | base rule 31 | **hit** — F9 (six bullets). |
| "the declared laws are three" + the two dated exemptions | INV-101 | **clean** — the layer states its line against all three (register: text files and one chat answer, INV-28; clock-honest stamps on every dated line, INV-24; no self-certification, closed by the ratification law INV-94/INV-193). The exemptions still hold: no live audience, and no rendered surface here. |
| "one principle stated four times" | INV-153 | **clean on the count** (classifier · net · deferral · message, each with its own verifier); **R1** on the outcome list. |
| "durable state, a standing mission, and a zone of its own make a capability an agent" | INV-182 | **hit** — F2 (T-22 states a second constitutive test). |
| "a profile with no roster reads as a single-agent machine" | F-roster facets | **hit** — F3. |
| "the roster names the agents whose rows the owner has ratified" | INV-184 migration clause | **clean as written** — the clause is honest and binds forward the way INV-159 binds every architecture duty; its cost is F3's unnamed third state, filed there. |
| "the pack's three laws each name a mechanical gate" | INV-101 | **clean** — unchanged by the delta; the three gates exist and are wired. |
| Formal index completeness | PRODUCT_SPEC.md:2234-2253 | **clean on coverage** — all 21 new anchors carry a row and a home column; **F7** on two rows' tense. |

## The architecture lens — six checks at this pack's scale

| Check | Verdict |
|---|---|
| Every spec fact has an owning node | **hit — F10.** All 21 new anchors are claimed exactly once (base-rulebook ×12, spec-author ×4, host-contract ×2, inbox ×1, build-pipeline ×1) and the placement is coherent: rules to the rulebook, the contract surface's shape to spec-author, the settings records to host-contract, the message's lifecycle to the inbox, the birth walk to build-pipeline. INV-197's claim is nominal only — its owner's file never states it. |
| No node stands without spec backing | **clean.** No node was added; every node carrying new anchors already stood with its own backing. See the no-new-node judgment below. |
| Every seam names what crosses it and who owns the format | **clean, with R2.** The three new seams each name their payload and a format owner: `roster + card → any agent` (host-contract owns both line formats), `agent → neighbour's inbox` (inbox owns the naming and deposit law; base-rulebook the earned-message law the gate reads), `producer → consumer (the contract)` (spec-author owns the artifact's shape). The roster line's format owner is named while the line's location is not — R2. The contract seam's two sides are both spec-author, which reads oddly for a seam between two hosts and is honest at this pack's scale: the format lives in the producer's own spec. |
| Quality budgets state their instrumentation homes and name their watchers | **hit — F12.** Two budgets, two named watchers, no instrumentation home for either, and the cadence's watcher cannot fire in its own failure mode. |
| The runtime view walks every promised flow | **hit — F11.** F-roster, F-agent-ask and F-agent-birth walk end to end through real nodes. F-contract does not. |
| The placement view says where every node runs | **clean.** The new anchors added no node and moved no node's place; the roster's place (the personal profile, `~/.claude/live-spec/profile.md`, symlinked to the playbook repo) and the card's place (each agent's own tree at `.live-spec/agent.md`) are both stated at host-contract's row. |

## The no-new-node judgment [INV-122]

**The reading holds. No node is owed.**

The three-question fitness test, applied to a hypothetical agent-communication node: testable alone — yes
(`tests/test_agent_channels.py` is already one file). Needed by a real second place — no; one place needs it,
the promoter↔site pair, and no second is promised. Workable in parallel — yes. That is the one-no case, and
the lens gives it two legal answers: a named plan that turns it to a yes, or a fold back into its caller. The
delta took the second, and INV-122's own bar (two or more no fold the carve back) never forced it either way,
so the fold is a choice the lens permits rather than one it compelled — which is the right call at one caller.

The fold's placement is coherent on inspection, node by node, and each receiving node's domain genuinely owns
what it took. The counter-evidence I looked for — facts landing in a node whose domain does not cover them,
or one node swelling into a second responsibility — is absent. F10 is a fold-quality defect (a fact assigned
to base-rulebook and never written there), not evidence that a node is owed: writing INV-197's sentence into
rule 31 costs one paragraph and needs no carve.

The re-visit trigger is already named where it belongs: row 385's revisit is the first host declaring a
contract, and the promoter↔site pair is the expected first. If a second and third pair arrive and the
contract's machinery grows past the four anchors spec-author now holds, the second-place question answers yes
and the carve earns a fresh read.

## What I assumed

- **The delta's boundary.** I read the surface at PRODUCT_SPEC.md 1393-1541, INV-153's growth at 411, the
  three seams and four flows and four coverage rows in ARCHITECTURE.md, base rule 31, and `.live-spec/agent.md`
  as the delta. Anything else on both sides is pre-existing and queues rather than blocks [INV-114]. R3 is
  filed that way.
- **F3's consequence rests on primary sources**, not on the doc's prose: the four trees and the profile's
  missing roster were read off the filesystem, and `.live-spec/agent.md` is the only card on the machine.
- **The gates' existence was read from the tree, never from the spec.** `check-earned-message.py` exists and
  is wired at `guardrails/pre-push:108`; the card gate, the permission gate, the freshness check and the
  compatibility test do not exist, which rows 387 and 385 state and F7 measures the docs against.
- **The onboarding-card seam I expected to break does not.** The roster lands in the personal profile, which
  `scripts/onboarding-card.py` parses; I read the renderer to check whether a roster line would surface as a
  setting on the card shown to the human. It would not — the project-rules section renders host entries only
  (`inject_project_rules(doc, host_entries)`), and personal entries reach the page only through the norm's
  known-row map. Clean, recorded so the next pass need not re-walk it.
- **The installed-copy version skew is out of scope.** The session's loaded prover copy opens at base v2.5.0
  while every skill in the repo pins v2.6.0; that is the installed-vs-source gap INV-175 owns, not a delta
  finding.

## What is working

- The two births are correctly split, and the reasoning is carried by a real case rather than a hypothetical:
  demanding blocked work of the fault message would have refused the track-coach deposit, which is the message
  a neighbour most wants. The law names that and carries the date.
- The write-ownership argument for splitting the roster from the card is the strongest structural move here.
  A single shared description file would have been the one mutable file every window races; each agent owning
  its own card and the human owning the roster line dissolves the race rather than guarding it.
- INV-188 (data never travels as a message) is the layer's sharpest quiet-keeping law: it names the exact
  traffic that costs a neighbour a session and points at the road that already exists.

## Readiness

Needs another iteration. The design's shape is sound and its purpose is served by laws that bite; twelve
defects stand between it and a landing, and eight of them (F1, F2, F3, F5, F6, F7, F9, F10) are sentences to
fix rather than mechanisms to build. F11 and F12 want a [target] tag and a decided sentence. F4 wants one
discriminator on the identifier. No finding asks the owner for anything.

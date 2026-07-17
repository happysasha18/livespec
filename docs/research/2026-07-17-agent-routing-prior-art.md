# Prior art: request routing and ownership negotiation between autonomous agents

**Date:** 2026-07-17 · **Asked by:** the owner ("let's research it, so we do not reinvent the wheel") ·
**Run:** the deep-research harness, 105 agents, adversarially verified · **Queue rows:** 395, 396 ·
**Status:** the summary below is the harness's own returned verdict; the full per-claim record with its
vote counts lives in the run's journal (`subagents/workflows/wf_84ff0284-3ab/journal.jsonl`).

**Read this with row 396's correction in hand.** The question was posed with git named as the universal
transport, on this pack's own reasoning at the time. The owner refused that premise the same day: agents
on one machine should talk through a direct channel, and git carries what needs no timely answer. So the
closing line below — that no prior art fits a repo-as-unit, git-as-transport setting — answers a question
that has since changed shape, and the direct-protocol sweep it implies has not been run.

## The verdict

The design question has one load-bearing precedent and it is 46 years old.

**Contract Net Protocol** (Smith, *IEEE Transactions on Computers* C-29(12), December 1980) already ships
two of the three requirements this pack was designing for.

- **The router lives in every node.** Each node runs its own contract processor; the routing decision is
  local. Verbatim from the paper: "there is neither global control nor global data storage".
- **Ownership settles by two-way mutual selection, with no central allocator.** Verbatim: "negotiation
  has four important components: 1) it is a local process that does not involve centralized control, 2)
  there is a two-way exchange of information, 3) each party to the negotiation evaluates the information
  from its own perspective, and 4) final agreement is achieved by mutual selection."
- **Manager and contractor are dynamic roles, never a priori assignments.** Verbatim: "Individual nodes
  are not designated a priori as managers or contractors; these are only roles, and any node can take on
  either role dynamically... nodes are not statically tied to a control hierarchy."

The refutation attempts that failed, recorded because they are the ones worth having: *the manager is a
central allocator per task* — rejected, since the role is dynamic per task, an award requires a voluntary
bid, and the paper denies centralized control outright. *It is outdated* — rejected, since a 1980
precedent cannot expire, and CNP was standardized as FIPA's `fipa-contract-net` and implemented in JADE,
so it is a shipped standard with adopters rather than an orphaned paper.

## The anti-noise vocabulary already exists there

The pack spent 2026-07-17 inventing terms CNP already carries: eligibility specification, bid
specification, focused addressing, and above all the **directed contract** — when the owner is known, the
award goes straight to it, with no announcement and no bids. That is this pack's referral law under
another name, arrived at independently.

A 1996 ICMAS extension measured the shape: **2 messages after learning, against a ~20-message broadcast
baseline**, with a graded fallback ladder — directed award, then reasoned announcement, then broadcast.

## Non-blocking is not free, and the fix is architectural

Requirement three — no stall while ownership settles — is delivered by no negotiation protocol. The
canonical market-based survey (Dias, Zlot, Kalra, Stentz) states that bid valuation can tax a bidder's
processor "to the point of not being able to do any other useful work", and that bid-valuation overflow is
"largely unaddressed".

The transferable fix from the same literature: make negotiation **purely opportunistic** — an optimization
layer over a baseline where every agent can already act alone. Then communication loss degrades quality
and never blocks.

**This is the owner's own constraint, stated independently the same day**: work must keep moving, an agent
meeting an unowned concern does the reasonable thing now in whatever tree can hold it, marks it
provisional, and the re-home lands later. He derived it from the work; the literature says it is the only
known working form. It landed as INV-197.

## The modern frameworks contribute nothing reusable

- **OpenAI Agents SDK handoffs** — a single in-process tool-choice that transfers the one thread of
  control; the handing-off agent stops. The neighbour set is fixed at construction. No discovery, no
  file- or git-native representation.
- **AutoGen GroupChat** — broadcasts every turn to every participant over one shared thread, which is the
  exact anti-noise failure mode this layer exists to prevent. AutoGen itself later routed around it with
  GraphFlow and MessageFilterAgent.

The shape of the miss is worth naming: these solve orchestration inside one process passing one thread of
control between functions. This pack's problem is several independent long-lived projects, each with its
own tree, queue, and gates, settling who owns a concern. It looks similar from outside and is a different
problem.

**Not verified in this round:** the summary names OpenAI's SDK and AutoGen by name and does not report a
per-claim finding on Google's Agent2Agent protocol, which the question asked about. Read the run's journal
before citing anything about A2A.

## The recommendation, as returned

- **Adapt** CNP's decision structure: directed contract first; announcement only when ownership is
  genuinely open; machine-checkable eligibility on every announcement; explicit no-bid handling. And the
  opportunistic-optimization architecture for non-blocking.
- **Reject** CNP's broadcast transport and its rich agent-communication-language semantics.
- **Ignore** the framework handoff designs.
- **Build ourselves** the ownership representation and the bid/award transport — no prior art verified in
  this round fits, though row 396 says the transport half of that question needs re-asking without the git
  premise.

## What this changes for the pack

Nothing that landed on 2026-07-17 is refuted. The referral law is CNP's directed contract; INV-197's
never-stall clause is the opportunistic-optimization architecture; the two-crossing bound [INV-196] is the
graded ladder's spirit at a smaller scale. What the research adds is a vocabulary with 46 years of use
behind it, a measured number for what the quiet channel is worth (2 against 20), and one name for a road
the pack has not built: the announcement, for a concern whose owner is genuinely open. Today that concern
goes to the pack as default owner [INV-197], which is the centralized answer CNP's whole point was to
avoid. Whether the pack keeps the default-owner road or grows the announcement is a design question for
the field run, and row 395's expensive-decision class is where it should be decided.

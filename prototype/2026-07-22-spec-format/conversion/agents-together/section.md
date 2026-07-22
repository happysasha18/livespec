# When agents work together

This section continues the document whose format the intake page defines and the starting-and-adopting section extends. The keywords *when*, *while*, *if*, *then*, and *shall* read as they do there. The bracket codes trail each criterion and point to the rule's home in the project spec; a reader can ignore them. Terms already defined in the earlier glossaries — request, inbox, pipeline, spec, invariant, session, journal, queue, backlog item, delivery, delivery report, guardrail, suite, profile, personal profile, settings ladder, host, pack, engine, instance, content contract, agent card, founding, adoption, catch-up, entry route, and the reviewer role — carry their meanings unchanged. The block below adds only the new nouns this section needs.

## Glossary additions

- **agent** — one project window that carries its own tree, queue, gates, published contracts, a standing mission, and an agent card, each of which outlives any single conversation.
- **capability** — one thing a window can do; a capability holding durable state, a standing mission, and a zone of its own is an agent, and a capability living wholly inside one session is a skill.
- **zone** — the area of ownership an agent claims, declared on its own card.
- **card scan** — the live scan that reads the agent-card files under each of its roots and treats every card it finds as an agent.
- **published contract** — a surface in a producer agent's own spec, paired with a machine-readable artifact at the path the producer's card names, stating the version it was generated under and the moment it was generated, that another agent reads on its own clock.
- **generation stamp** — the moment a published artifact records as the time it was generated.
- **cadence** — the one number a producer owns, stating how often it regenerates its published artifact.
- **staleness bound** — the one number a consumer owns, stating how old a published artifact may be and still carry that consumer's analysis.
- **grant** — a recorded permission one session holds for one repo: a push grant to deposit and push into it, a read grant to clone and pull a private producer's repo.
- **named reference** — an internal item's stable code paired with a plain one-sentence description of what the item does and the problem it solves.
- **description field** — the one home, a field the Formal index carries, where each code's plain one-sentence description lives.
- **earned message** — one file a sender agent deposits in a receiver agent's inbox, naming the sender's own work that earned it.
- **ground** — the reason a message earns sending, drawn from a closed set of three.
- **referral** — the answer that a question belongs to another agent's zone, returned to whoever asked it.
- **need-by** — the moment a message states as the time by which it needs its terminal state.
- **transport** — the road a message between two agents travels: the store, where the sender deposits one file the receiver sweeps later, or the direct channel, a live back-and-forth between two running sessions.
- **harness** — the runtime that runs a session and its tools, the environment the agent executes in; it owns the machinery between sessions, among it the socket plumbing whose listener the direct channel waits on.
- **stranger** — a contributor with no push rights and no per-repo grant for a repo; a stranger's message enters through an issue opened on the repo's public tracker, which the monitor bridges into the inbox.
- **monitor** — the scheduled script that bridges each open issue a stranger filed into one committed inbox file under the reserved stranger source word, naming its source.
- **status report** — the running account a session gives its user of the work in hand and the messages its agent channel has sent.
- **adversarial read** — a fresh-context audit set on breaking a decision's case, run before the decision lands, that closes by bringing the decision to the owner with its findings and a recommendation.
- **expensive decision** — a decision that would cost more to unwind than to make.

---

## Requirement 1: An agent and a skill are told apart by what outlives a conversation

**Context:** Several agents work on one person's projects, and the moment they can talk to each other they can generate noise. The layer that governs them opens by telling an agent from a skill, since only an agent holds standing work of its own that another agent can address. An agent is a project window with a tree, a queue, gates, contracts, a standing mission, and a card; a skill is a capability a window loads for one conversation.

**User Story:** As a person running several agents on one machine, I want an agent and a skill told apart by what outlives a conversation, so that only the trees holding standing work are addressed as agents.

### Acceptance Criteria

**Case: what an agent carries**

1. *when* a tree carries its own spec, queue, gates, published contracts, standing mission, and agent card, the system *shall* treat that tree as an agent, each of those outliving any one conversation. [E-31]
2. one window *shall* serve one agent, the same rule the engine-and-instance pair already holds for its two repos. [E-31, INV-86]

**Case: what a skill carries**

3. *when* a capability loads into a window, holds no tree, no standing mission, and no queue, and leaves nothing standing once the conversation closes, the system *shall* treat that capability as a skill. [E-31]

**Case: the line between the two**

4. the system *shall* count a capability as an agent *when* it holds durable state, a standing mission, and a zone of its own, and *shall* count a capability that lives wholly inside one session as a skill. [INV-182]
5. *when* a real capability sits on the line between the two, the owner's word *shall* place it. [INV-182, T-22]

---

## Requirement 2: Two channels carry everything between agents, and the traffic's kind picks the transport

**Context:** A message between two agents travels two roads and no more. One is the receiver's inbox, which carries a one-shot request to change something; the other is a published contract, a versioned read the reader takes on its own clock. Which road a given message takes is decided by whether it needs a timely answer, while who may talk and when stays the same on either road.

**User Story:** As a person whose agents pass work between them, I want exactly two channels to carry everything between two agents, so that no third improvised road grows to carry the traffic the two were meant to hold.

### Acceptance Criteria

**Case: the two channels**

1. the receiver's inbox *shall* carry a one-shot request to change something, one new file per item. [INV-183, E-11]
2. a published contract *shall* carry a recurring read, versioned, taken on the reader's own clock. [INV-183, E-33]
3. a reply *shall* ride the inbox in the other direction, so the count of channels between two agents stays at two. [INV-183, INV-192]

**Case: the traffic's kind picks the transport**

4. *when* a message needs no answer within a deadline — a durable record read on the neighbour's own clock, or a notification — the system *shall* send it by the store, the sender depositing one new file and the receiver sweeping it later, reachable while the receiver is not running and committed and pushed *when* the sender is remote. [INV-236, E-11, T-10, INV-112]
5. *when* a message is a back-and-forth needing a live peer that answers in turn, the router (`guardrails/route_agent_transport.py`) *shall* route it to the direct channel. [INV-236]
6. *while* the harness has shipped no listener, the direct channel *shall* stand unavailable, and the router *shall* name the listener it waits on. [INV-236, INV-231]

**Case: the store road's watcher**

7. *when* a receiver arms a one-shot check that reads a deposit on the receiver's own rhythm, whenever it next runs, the system *shall* treat that check as the store road's watcher. [INV-236, INV-231, INV-129]

**Case: the contract holds across transports**

8. whichever transport carries a message, the system *shall* leave the two-channel contract untouched, so who talks and when stays as it stands. [INV-236, INV-183]

---

## Requirement 3: Every reference to an internal item carries its code and a plain description

**Context:** The method names its internal items with short codes, and a code alone tells a person nothing. So every reference to a named item carries a pair — the item's stable code beside a plain one-sentence description of what it does and the problem it solves. The pair travels in a cross-agent message and in a report a human reads alike, and each description lives in one home the Formal index carries.

**User Story:** As a reader of a report or a cross-agent message, I want every internal code carried beside a plain one-sentence description, so that a bare code never stands alone before me and a second agent reasons in the same terms.

### Acceptance Criteria

**Case: the pair travels together**

1. *when* a reference names an internal item the method carries a code for, the system *shall* carry the item's stable code beside a plain one-sentence description pinned to the item at its owning surface. [E-35, INV-239, E-4]
2. the system *shall* carry that pair in a message across the agent channel and in a human-facing report alike. [INV-239, INV-183]
3. within one report, the system *shall* carry the full pair on a code's first mention and the code alone on each later mention of that code. [INV-239, INV-28, INV-31]

**Case: one home for the description**

4. the system *shall* keep each code's description in one dedicated description field the Formal index carries, written once there and read by every reference. [INV-239]
5. the system *shall* back-describe the whole existing code set in one pass at a major release carrying one MIGRATION.md chapter. [INV-239, INV-217]
6. *when* the project runs in another language, the system *shall* translate the English description in real time and translate it consistently, so one item reads under one translation across a session. [INV-239, INV-83]

**Case: the description's presence is checked, its quality sampled**

7. a mechanical gate *shall* check that every registered code carries a non-empty description and *shall* fail on a code whose description field is empty, judging presence alone. [INV-239]
8. for a code deposited on the agent channel with no description beside it, the reviewer's review *shall* stand as the net — the reviewer role's review is the enforcement until the named gate ships — the deposit-time lint over each `from-<agent>` inbox file being the mechanism the law declares. [INV-239, INV-189, INV-150]
9. a human *shall* sample descriptions against the quality bar at the migration's authoring and again on the periodic audit's own count — every ten deliveries by default, the host setting its own count in its profile — and *shall* accept each that reads as clear, and a description that reads below the bar *shall* become a queue row. [INV-239, INV-41, INV-145]

**Case: the quality bar a description is written to**

10. a description *shall* say what the item does and the problem it solves, *shall* show the whole class *when* the rule governs a class, *shall* name its key term in plain words, and *shall* use the accurate actor and object. [INV-239, INV-153, INV-83]

---

## Requirement 4: A description a reader could not follow is rewritten by the agent that owns the item

**Context:** A description can be clear to its author and still leave a reader asking what one of its terms means. That re-asked question is the signal the description did not land. The agent that owns the item rewrites the description, and it does so on its next turn writing that item's home document rather than in the middle of another turn.

**User Story:** As a reader who re-asks what a term means, I want the description rewritten by the agent that owns the item, so that each description earns its clarity from real use rather than a one-time guess.

### Acceptance Criteria

**Case: the re-asked question is the signal**

1. *when* a human re-asks what a term a reference carries means, the system *shall* read that question as a signal the description did not land. [INV-240, INV-83]

**Case: the owning agent writes the rewrite**

2. the system *shall* let only the window that owns the item write that item's description, its one home being the item's owning surface. [INV-240, INV-10]
3. *when* the confusion lands in the owning window, the owning agent *shall* reformulate the description to answer the question just asked and overwrite it in its one home on its next turn writing that document. [INV-240]
4. *when* the confusion lands at a window that does not own the item, that window *shall* carry the confusion to the owning agent as a lived-fault earned message, and the owning agent *shall* rewrite the description on its next turn writing that document. [INV-240, INV-189]

**Case: the rewrite waits for a written turn**

5. whichever window the confusion arrived at, the system *shall* record the re-question and defer the rewrite to the owning agent's next turn writing the document, holding clear of a rewrite in the middle of another turn. [INV-240, INV-39]
6. the deferred rewrite *shall* take the description's home document under its own pen and *shall* ride as a named intended change to the identity check the restructure procedure runs — word-token and punctuation multisets unchanged except the named changes — which expects it as a matched token. [INV-240, INV-198, INV-111]

**Case: the rewrite meets the same bar**

7. the rewrite *shall* obey the quality bar every description obeys, sampled against a real reference by the human sampling net, with the presence gate beneath it. [INV-240, INV-41]

---

## Requirement 5: An agent is found by the card it writes and a live scan

**Context:** An agent reaches this point the moment it meets something that might belong to another agent — a capability it lacks, data another project holds, a question about a neighbour's zone. It answers by scanning for cards, since a card is what makes a tree an agent. It comes away holding the owning agent's name, mission, zones, contracts, and inbox address, or it learns no agent owns the thing, which opens the birth scenario.

**User Story:** As an agent meeting something outside its own zone, I want to find the owning agent from a card it wrote and a live scan, so that who owns what is a lookup rather than a guess.

### Acceptance Criteria

**Case: the card is the declaration**

1. the agent card *shall* live in the agent's own tree at `.live-spec/agent.md` and *shall* name the agent's name, its standing mission, the zones it owns, each contract it publishes with the path its artifact lives at, and its inbox address. [E-32]
2. the system *shall* treat a tree that carries a card as an agent, and writing the card *shall* be the one act that seats it. [E-32, INV-184]
3. *when* an agent finds no card on a thing that might not be its own, the system *shall* ask one plain question rather than guess. [INV-184, INV-4]

**Case: discovery is a live scan**

4. the system *shall* discover agents by reading two globs under each root — `<root>/*/.live-spec/agent.md` and `<root>/*/*/.live-spec/agent.md` — and *shall* treat every card it finds as an agent. [INV-184, E-32]
5. the scan's roots *shall* be the parent directory of the reader's own tree together with any root the personal profile names. [INV-184, E-16]
6. the scan *shall* descend no branch, so its whole cost is two directory listings per root and one stat per candidate. [INV-184]
7. the system *shall* run the scan live on every lookup and *shall* keep no cached index of who exists, since a scan reads the machine as it stands *while* a cached list answers from a past moment and is the shared file two windows race to edit. [INV-184, INV-10, INV-11]

**Case: no shared file describes an agent**

8. the system *shall* let no file outside any tree describe any agent, each agent owning its own description the way it owns its own tree. [INV-184, INV-10]
9. the system *shall* read the owning card before acting on anything that might not be its own, the reviewer's review standing as the net for that discipline. [INV-184, INV-150]

**Case: the card needs no permission, and its bounds**

10. the system *shall* grant the card by write-ownership, so writing it needs no permission act. [INV-184, INV-10]
11. the card *shall* hold the agent's own identity and addresses, and product data placed in a card *shall* be a contract field taking the contract's permission road. [INV-184, INV-185]

**Case: a tree with no card is flagged**

12. *when* an inventoried live-spec host tree carries no `.live-spec/agent.md`, the system *shall* flag it as an incomplete record, the rank a project kind recorded with no declared layers carries, and *shall* have the host write its card at its catch-up walk, the duty binding forward. [INV-184, A-10, A-11, INV-159, INV-36, INV-135]
13. the gate `guardrails/check-agent-card.py` *shall* read a host tree's root and fail by name *when* the root carries no `.live-spec/agent.md`, and the pack carries its own card so the gate reads the pack's tree and passes. [INV-219, INV-97]

---

## Requirement 6: A published contract is read on the reader's own clock

**Context:** A consumer agent arrives here from the scan holding a producer's card and the path its artifact lives at. A published contract is a surface in the producer's own spec, paired with a machine-readable artifact carrying its own version and generation stamp. The consumer reads it read-only on its own clock, and data past its staleness bound stops the analysis.

**User Story:** As a consumer agent needing another agent's numbers, I want to read its published contract on my own clock rather than ask it, so that I depend on a stated, versioned interface instead of an unstamped snapshot.

### Acceptance Criteria

**Case: the contract and its artifact**

1. a published contract *shall* be a surface in the producer's own spec, written, proven, and tested where the producer's other surfaces are and earning its feature coverage there. [E-33, INV-73]
2. each contract field *shall* name what the field means, the window it is measured over, how it is aggregated, and the source it derives from, and the reviewer *shall* read a field missing any of the four as an incomplete surface. [E-33, INV-101]
3. the published artifact *shall* live at the path the producer's card names and *shall* state the contract version it was generated under and the moment it was generated, so a reader tells its shape and its age from the artifact itself. [E-33, E-32, E-14, INV-24]

**Case: nothing publishes by default**

4. a contract *shall* publish no field until the owner records an explicit permission for it in the producer's tree with its date and author. [INV-185, INV-24]
5. a field with no recorded permission *shall* stay in the producer's tree, the way a neighbour's product is built granting no permission, and the reviewer's review *shall* read a declared contract's fields against their permission records. [INV-185, INV-150]
6. credentials *shall* cross no channel under any permission, the published artifact being the one road a producer's product data takes between two agents. [INV-185, INV-183]

**Case: the producer's cadence**

7. the producer *shall* declare one cadence — how often it regenerates the artifact — and *shall* hold to it whatever its consumers do, a deploy refreshing the artifact as a bonus and never triggering it. [INV-186]
8. the producer's own session-start check *shall* fail *when* its scheduled regeneration did not run, beside the pack-update check that runs there, and the consumer's staleness bound *shall* stand as the second, independent watcher that catches a producer gone quiet. [INV-186, INV-187, E-25]

**Case: the consumer's read**

9. the consumer *shall* declare one staleness bound — how old the artifact may be for its analysis — and its freshness check *shall* fail past that bound before any analysis runs. [INV-187, INV-41]
10. the consumer *shall* pin the contract version it was written against and *shall* carry a compatibility test that fails *when* its pinned version and the artifact's version diverge. [INV-187]
11. the consumer *shall* read the artifact read-only — over the filesystem when co-located, over git when remote under its recorded read grant — and *when* the generation stamp reads past its staleness bound it *shall* name the stale data aloud and stop. [INV-187, INV-112, INV-232, INV-67]

**Case: two numbers, set apart**

12. the cadence and the staleness bound *shall* be two numbers set independently, and neither side *shall* read the other's. [INV-186, INV-187]

**Case: data reads, it never asks**

13. a consumer wanting a producer's data *shall* read the contract rather than send a message asking for it. [INV-188]
14. *when* a consumer wants a field the contract lacks, the system *shall* treat it as a request about the contract's shape, which the earned message governs. [INV-188, INV-189]

---

## Requirement 7: An agent earns a message before it deposits one

**Context:** A sender agent reaches this point holding the receiver's card and inbox address and a piece of its own work the receiver's zone blocks. A message is one new file in the receiver's inbox, and every message names the work of the sender's own that earned it. The agent recognizes the neighbour's zone on its own and deposits the message in the course of its work, telling its user each time.

**User Story:** As an agent blocked by a neighbour's zone, I want to deposit a message only when my own work earns it, so that curiosity and tidiness generate no traffic on the channel.

### Acceptance Criteria

**Case: the transport**

1. a message *shall* be one new file in the receiver's inbox, named and shaped as every inbox item, naming its source with the `from-<agent>` form the inbox uses, two source words being reserved and owing no ground — `from-owner`, the owner's own message, and `stranger-`, a stranger's bridged item, the inbox file the monitor commits from a stranger's issue. [INV-189, E-11, INV-193, INV-146]
2. the system *shall* deposit that one file by the standing arms — a co-located sender writes it and stops, a remote sender commits and pushes it under its per-repo grant, and the receiver's sweep carries it into the receiver's queue. [E-11, INV-10, INV-174, INV-112, T-10]

**Case: a message names the work that earned it**

3. a message *shall* name the sender's own work that earned it, and a message that can name no such work *shall* stay unsent. [INV-189]
4. a blocked message *shall* name the blocked work — a real row, a real failing step, a real thing the sender cannot finish *while* the receiver's zone stands as it does. [INV-189]
5. a lived-fault message *shall* name the fault and the evidence the sender lived — what it ran, what happened, and how the fault showed itself. [INV-189]

**Case: three grounds, and the set is closed**

6. the system *shall* recognize exactly three grounds for a message — the sender blocked by the receiver's zone as it stands; the sender having lived a fault in that zone and carrying the evidence; or the sender holding a concern no agent's zone owns, carried to the pack as its default owner. [INV-189, INV-197]
7. a candidate message matching no ground *shall* stay unsent, and the third ground *shall* carry only to the pack and only *while* no zone owns the thing. [INV-189, INV-197]

**Case: the owner's zone is presumed informed**

8. the system *shall* report to a zone's owner nothing that owner's own instruments already see, so a fault the owner's instruments cannot see, carried with the evidence the sender lived, is the case that earns the file. [INV-189]

**Case: the agent recognizes the zone and deposits on its own**

9. *when* an agent's own work meets a fault or a lack in something another agent's zone owns, the system *shall* scan for cards, find the owning agent, and take the channel that fits, on its own recognition. [INV-195, E-32, INV-183]
10. *when* the agent's work earns a message under a ground, the agent *shall* write the file to the neighbour's inbox in the course of its own work, the trigger being any earned ground rather than a fixed list of occasions, the pack stating the form of a message and the host's work stating its content. [T-24, INV-189, INV-153, INV-163]
11. the deposited message *shall* name its references by the pair, so the neighbour reads a self-explaining file. [T-24, E-35]

**Case: the user is told**

12. *when* the agent deposits a message, the system *shall* tell its own user in the status report, naming the message's subject by its pair and the neighbour it reached, in a plain notice. [T-24, INV-27, INV-28, INV-31]
13. *when* the earned-message law declines a message the agent had drafted, the system *shall* tell the user in the status report with the reason it was withheld, and *shall* raise no tell for an impulse the discipline turned away before it became a draft. [T-24, INV-190, INV-191]

**Case: a capability is used, not copied**

14. an agent needing a capability another agent's zone owns *shall* send a message or read a contract rather than keep a local copy of it. [INV-194, INV-183]

**Case: a deposit is written whole**

15. the system *shall* write a deposit into another window's inbox under a `.draft` name and make it final by an atomic rename once the content is complete. [INV-249]
16. the receiving sweep *shall* act only on a finished deposit and *shall* pass over any name still carrying the `.draft` suffix, leaving a routed deposit earned in place rather than removing it under a live writer. [INV-249, INV-247]

---

## Requirement 8: A misdirected question is referred back, and no refer-and-resend loop runs on

**Context:** A question can land on an agent that does not own it. The answer is a referral: the question lives in another agent's zone, so it goes back to whoever asked. Every message carries an identifier and a stated need-by and reaches a terminal state, and one question crosses between the same two agents at most twice before the third crossing goes to the owner.

**User Story:** As an agent handed a question from another agent's zone, I want to refer it back to whoever asked and let no refer-and-resend loop run on, so that a misdirected question reaches its owner without manufacturing traffic.

### Acceptance Criteria

**Case: a referral returns to whoever asked**

1. *when* a question belongs to another agent's zone, the system *shall* refer it back to whoever asked, and the zone's owner *shall* receive nothing from a referral. [INV-190]
2. *when* a human asks, the system *shall* answer in chat that the answer is the other agent's and to ask that agent, sending nothing. [INV-190]
3. *when* an agent asks, the system *shall* answer along the reply road as the message's terminal state, declined and naming the zone that owns the question. [INV-190, INV-192]

**Case: a question dropped for want of a home**

4. *when* a question pins to no artifact and no work of the sender's stands on it, the system *shall* drop it, the holding of it being the finding. [INV-191, INV-153]

**Case: a concern no zone owns**

5. *when* a concern is real work whose owning zone does not exist yet, the system *shall* carry it to the pack's inbox, and the pack repo's own assigned session, sweeping that inbox, *shall* answer who owns it — an existing agent, a new agent the owner ratifies, or a skill. [INV-197, T-22, INV-182, INV-97, T-10]
6. *while* ownership is being settled, the agent *shall* do the work it can do now in whatever tree can hold it and mark that work provisional, the re-home landing later as ordinary pipeline work. [INV-197]

**Case: the crossing bound**

7. the system *shall* let one question cross between the same two agents at most twice, counted by the message identifier, and *shall* send the third crossing to the owner, named in the sender's status report as a zone question the two could not settle, the shape the human-decision withdrawal loop already takes. [INV-196, INV-192, INV-27, INV-130]
8. neither agent *shall* reopen the count by rewording the question. [INV-196]

**Case: a wrong referral is named**

9. *when* an exchange reaches the crossing bound through a referral met by a counter-referral between the same two agents, the system *shall* name the wrong referral in the sender's status report — a referral that pointed at a zone which, by its own referring-back, does not own the target. [INV-225, INV-196, INV-27]
10. *when* a referral is answered by an acceptance, or an onward referral to a third zone answers it, the system *shall* reach no bound and name nothing. [INV-225]
11. the checker `guardrails/check-wrong-referral.py` *shall* read the shape of the exchange and ride the suite rather than the push chain — the sequence of checks a push runs — *while* whether the target falls inside a zone's claim stays the receiving sweep's and the reviewer's judgment. [INV-225, INV-150, INV-222]

**Case: the message identifier**

12. the system *shall* mint a stable identifier per message from the sender's session identity — the harness session id where the context carries one, else the session's start time joined with its worktree path and a nonce, recorded in the session checkpoint — plus a discriminator the sender mints for that message, so one session's two messages carry two identifiers, and an exchange *shall* be keyed to its first message's identifier, which every reply names, so the crossing bound counts questions rather than sessions and outlives the sender's own session. [INV-192, INV-117]
13. a reply *shall* name the message by that identifier after the file has left the inbox and become a row in the receiver's queue. [INV-192, E-11]

**Case: the reply and the terminal state**

14. a reply *shall* travel back to the sender as one new file in the sender's inbox, owing no blocked work of its own since the message it discharges already named the work. [INV-192, E-11]
15. every message *shall* state its need-by and *shall* reach one terminal state — delivered, declined, or escalated past its stated need-by. [INV-192, INV-1]
    [GAP: the spec does not name what checks that a message has passed its stated need-by, nor who sets the need-by value, so the move to the escalated state has no named watcher.]
16. *when* a message escalates, the system *shall* surface it in the sender's status report as blocked work aged past its need-by, and *shall* wake a dormant window on no occasion. [INV-192, INV-27]

**Case: authority does not travel by relay**

17. an agent-initiated message *shall* stand as a proposal in the receiver's queue until the owner ratifies it, *while* an owner-initiated message carries the owner's authority. [INV-193, INV-94]
18. relaying a message *shall* change only its carrier and leave its authority where it started. [INV-193, INV-94]

---

## Requirement 9: A new agent is created only on the owner's word

**Context:** An agent reaches this point when a capability pins to no agent's zone, or when a capability has outgrown the agent hosting it. Any agent may propose a new agent, and the owner alone brings a new tree into being. The founded agent then declares itself by writing its own card, so every scan finds it from that moment.

**User Story:** As the owner of the machine, I want a new agent created only on my own word and declared by its own hand, so that a new tree and its standing cost never come into being without me and every scan still finds what is really there.

### Acceptance Criteria

**Case: any agent may propose**

1. *when* a capability pins to no agent's zone, or a capability has outgrown its host, the system *shall* let any agent propose a new agent, naming the capability, the zone the new agent would own, and the contracts it would publish. [T-22]
   [GAP: the spec does not name who judges that a capability has outgrown its host, or by what measure.]
2. the proposal *shall* carry the adversarial read an expensive decision earns and *shall* stand as a proposal until the owner ratifies the creation. [T-22, INV-235, INV-193]

**Case: the owner ratifies, the agent declares itself**

3. the owner's word *shall* authorize the creation, since a new agent is a new tree, a new queue, a new set of gates, and a standing cost the owner carries. [T-22, INV-10]
4. the owner *shall* ratify on the adversarial read the proposal carries, the read reaching the owner with its findings and a recommendation and the taste call staying the owner's. [T-22, INV-235, INV-143]
5. the founded agent *shall* declare itself by writing its own card, and every scan *shall* find it from that moment, no third party seating it. [T-22, E-32]
6. creating an agent *shall* be a delivery, so the new tree's journal *shall* record it with its date and the request row it cites. [T-22, INV-3, INV-24]

**Case: a false declaration travels the same scan**

7. *when* a tree declares itself with a card the owner never authorized, the system *shall* show that card in the same scan that finds every other, so the owner reading it sees what stands on the machine. [T-22, E-32]
   [GAP: no gate today catches a card whose creation carries no ratification, and the spec records that this behaviour owes one.]

**Case: the contract survives the migration**

8. *when* a capability moves from its old host to a new agent, the system *shall* let the consumer keep reading its pinned version until it chooses to move, the new owner publishing at the address its own card names. [T-22, INV-187, E-32]

**Case: the kind is the owner's call**

9. *when* a capability sits on the line between a skill and an agent, the owner's word *shall* settle which it is, the call recorded with its date in the proposing agent's journal. [T-22, INV-182, INV-152, INV-24]

# New source holes found — "When agents work together"

Holes surfaced while converting the section: places where the source states an evaluative or relational term and never answers its judge, its measure, or its enforcing net. Each is recorded as a `[GAP: ...]` line under its criterion in `section.md`; no behaviour was invented to paper over one.

## G1 — "outgrown its host" names no judge or measure

**Where:** R9.1 (source `T-22` / `INV-182`, line 1600 and the birth-scenario entry, line 1598).

**The hole:** The birth walk fires when "a capability has outgrown the agent hosting it," but the spec never names who judges that a capability has outgrown its host, or by what measure. This is the direct sibling of the pilot section's open question about when "the content and the mechanism can no longer share one file" — the reuse-split offer's return trigger. The grain call once a capability *is* on the line is explicitly the owner's (R9.9); the *outgrown* trigger that reaches that call is unquantified.

**Plainest honest actor named in the text:** the proposing agent raises the proposal, but nothing tells it the threshold. Recorded as the gap.

## G2 — a message's need-by has no named watcher

**Where:** R8.15 (source `INV-192`, line 1581).

**The hole:** "Every message states its need-by and reaches a terminal state … delivered, declined, or escalated past its stated need-by." The escalation surfaces in the sender's status report — but the spec names nothing that *checks* a message has passed its need-by, so the move into the escalated state has no watcher, and it does not say who sets the need-by value or by what measure. A message on a dormant sender's clock could sit past its need-by with no session running to notice. (The producer's cadence and the consumer's staleness bound each name their watcher explicitly, per `INV-186`/`INV-187`; the message need-by does not.)

## G3 — no gate enforces that a card's creation was ratified

**Where:** R9.7 (source `T-22` / `INV-150`, line 1604).

**The hole:** A false self-declaration — a tree writing a card the owner never authorized — travels to the human through the ordinary scan, which is the whole of the stated safety here. The source states plainly that "no gate reds today on a card whose founding carries no ratification, and this sentence owes one." So the ratification-presence net is an acknowledged, unfilled hole rather than a design decision that no net is wanted. Recorded so the owed net is not lost.

## G4 — "the pack answers who owns it" names no acting session (source finding, resolved by derivation)

**Where:** R8.5 (source `INV-197`, line 1575).

**The finding:** The source says "the pack answers who owns it," and the pack as a bundle of skills and templates cannot answer anything. The concrete actor is derivable from the source rather than a hole: the pack is a host, its own first host (`INV-97`), with its own inbox swept by its assigned session (`T-10`, write-ownership `INV-10`). R8.5 therefore names "the pack repo's own assigned session, sweeping that inbox" as the answering actor. Recorded here because the source sentence itself is actorless and should name the session when it is next touched; no `[GAP]` line stands in the section since the derivation closes the hole.

---

Non-holes deliberately **not** marked as gaps (the spec answers them, so a `[GAP]` would be wrong):

- The agent-channel description lint and the contract-permission gate are unbuilt today, but the spec answers each with a present net — the reviewer's review (`INV-150`) — so R3.8 and R6.5 state that present behaviour rather than a gap.
- "Reads below the bar", "reads as clear" (R3.9): the human sampling net (`INV-41`) is the named judge, and the sample's period is stated by the source's own citation — the periodic audit's cadence (`INV-145`), every ten deliveries by default with the host setting its own count.
- The message identifier's stability across a session wipe (R8.12): the source states it — the exchange is keyed to its first message's identifier, which every reply names, "so the bound counts questions rather than sessions" (`INV-192`) — so no gap stands.
- The wrong-referral zone-claim judgment (R8.11): the receiving sweep and the reviewer are the named judges.
- The cadence and staleness-bound numbers (R6.7, R6.9): the producer/consumer propose, the owner sets on his word — actor named.

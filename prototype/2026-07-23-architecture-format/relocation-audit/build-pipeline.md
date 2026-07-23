# owns-field prose audit — node `build-pipeline`

Source: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, `### [node: build-pipeline]`, **owns** field (line 69).
Spec checked: `PRODUCT_SPEC.md`.

| fragment (quoted; … past 40 words) | anchor | class | evidence |
| --- | --- | --- | --- |
| "a deferred item's own state is re-derived from the code before its work resumes" | INV-247 | DUPLICATE | R93.1 (2102): "the system *shall* read the code the item touches … and re-derive the item's real current state before it designs anything on the item." |
| "the resume-side twin of the primary-source rule and the architecture step's pin-from-a-command" | INV-247 | KEEP | ownership note — why the anchor sits here (kinship to primary-source rule / pin-from-a-command). |
| "standing beside the queue-take trigger re-scan [INV-129] — that reads whether the row returns while this reads whether its described internals still hold" | INV-247 | KEEP | cross-anchor wiring note distinguishing INV-247 from INV-129; the distinction is not itself a spec rule. |
| "a discipline the seat holds at the queue-take walk with no mechanical gate" | INV-247 | DUPLICATE | R93.3 (2107): "*shall* keep this a discipline the seat holds, since a resume is an in-session act at chat cadence with no committed artifact for a gate to scan". |
| "homing the spec clause and base rule 34" | INV-247 | KEEP | home/ownership pointer. |
| "ROADMAP 430" | INV-247 | KEEP | ROADMAP-row pointer. |
| "grading the size of a change is the reader's act in either direction, both poles one bias" | INV-221 | DUPLICATE | R135.1 (2917): "*shall* leave grading that size — to the plus or to the minus — to the reader." |
| "the pack owes the general law the profile holds as a personal value" | INV-221 | KEEP | provenance/ownership note — pack generalizes a personal-profile value. |
| "binding every text and carried into the worker brief beside the no-scissors law so a worker's report and agent-to-agent message obey it" | INV-221 | DUPLICATE | R135.2 (2918): "*shall* bind this law across every text — chat, docs, worker reports, and agent-to-agent messages"; R135.3 (2922): "*shall* carry the law in the worker brief for the surface the judge does not read". |
| "no new machine, since the register judge already holds the class on the chat and document surfaces" | INV-221 | DUPLICATE | R135.3 (2922): "*shall* have the register judge read this class on the chat and document surfaces". |
| "a `far`-status row carries no revisit trigger and no plan to run" | INV-222 | DUPLICATE | R5.4 (350): "keep a far row in the queue's body with no revisit trigger and no plan to run". |
| "a queue-status sibling of `deferred` [INV-129] told apart by the trigger" | INV-222 | DUPLICATE | R94.1 (2121): "distinct from a deferred row whose revisit trigger the queue-take re-scans"; R94.2 (2122). |
| "the runnable what's-left report stands it down by name and offers it on request" | INV-222 | DUPLICATE | R5.5 (351) / R94.3 (2126): "*shall* stand the far tier down by name … and *shall* show it only on the person's request." |
| "the report-shape home is communicator, carried there as wiring" | INV-222 | KEEP | wiring note — communicator owns the report shape, ownership stays here. |
| "the fixture check `guardrails/check-far-tier.py` reds a far row named among runnable work, riding the suite and not the push chain since a chat report is no committed file to gate" | INV-222 | DUPLICATE | R94.4 (2127): "*shall* red the report-shape check, which rides the suite and not the push chain since the status report is a chat surface with no committed file to gate." (filename is the only non-spec token) |
| "a node's fitness is re-answered as it grows" | INV-233 | DUPLICATE | R244.2 (5513): "*when* an architecture is re-proven … *shall* have each node re-answer the three fitness questions on its pins". |
| "node co-residence in one file is the counted signal … the measured thing is nodes-per-file read from this doc's own pin column as the count of distinct nodes naming a file" | INV-233 | DUPLICATE | R244.1 (5512): "*shall* count nodes-per-file from the architecture's own pin column as the number of distinct nodes whose pins name a file". |
| "kin of the three-question fitness test [INV-122] and the boundary-health law [INV-128]" | INV-233 | KEEP | cross-anchor wiring/kinship note. |
| "raw size rejected as INV-41's vanity metric" | INV-233 | DUPLICATE | R244.1 (5512): "*shall* reject raw size as the signal." |
| "the ratcheted counter `guardrails/node_growth_counter.py` with its cap `guardrails/node-file-cap.json` seeded at the current count so the tree lands green while any increase reds and the cap ratchets down only [INV-164]" | INV-233 | DUPLICATE | R244.3 (5517): "*shall* hold a ratcheted per-file node cap seeded at the tree's current count, and *shall* red any increase while the cap ratchets down only." (filenames are pins) |
| "riding the suite `tests/test_node_growth.py` and taking no push-gate letter the way the far-tier check takes none" | INV-233 | ABSENT | R244.1–R244.6 carry no clause on this check riding the suite or taking no push-gate letter; spec is silent on the node-growth check's push status. |
| "the prover's seventh architecture lens (the growth re-ask, carried by product-prover as wiring)" | INV-233 | KEEP | wiring note — product-prover carries the growth re-ask as a lens; R244.2 names no prover or lens count. |
| "the design review's split proposal in its two-objects finding shape, carried by design-reviewer as wiring" | INV-233 | DUPLICATE | R244.4 (5518): "the design review *shall* carry the split proposal in its two-objects shape". (only "carried by design-reviewer" is a wiring tag) |
| "a split is a structure change carved by the architecture step alone and re-proven there [INV-37, INV-113]" | INV-233 | DUPLICATE | R244.5 (5522): "*shall* carve it by the architecture step alone and re-prove it there." |
| "the proposed number two nodes per code file set on the host's word [INV-41]" | INV-233 | KEEP | target/proposal pointer — the proposed cap number (spec seeds at current count, states no target of two). |
| "the declared-layers rule saying what counts as a code file" | INV-233 | DUPLICATE | R244.6 (5523): "*shall* read what counts as a code file from the project's declared layers." |
| "ROADMAP 390" | INV-233 | KEEP | ROADMAP-row pointer. |
| "a decision whose reversal costs more than making it did" | INV-235 | DUPLICATE | Glossary (88): "**expensive decision** — a decision that would cost more to unwind than to make." |
| "a new agent's birth, a node carve or merge, a contract's shape once a consumer pinned it, a project's kind, an engine/instance split, a repository going public" | INV-235 | DUPLICATE | R214.1 (4871): "an agent's birth, a node carved or merged, a contract's shape once a consumer pinned it, a project's kind, an engine-and-instance split, and a repository going public". |
| "earns a fresh-context best-tier audit" | INV-235 | DUPLICATE | R214.3 (4876): "*shall* run a fresh-context independent audit at the best tier the pack's quality habit sets". |
| "where a kind is in question, the design review's two-objects read before it lands" | INV-235 | DUPLICATE | R214.4 (4878): "*where* the decision turns on whether members are one kind, the design review *shall* read the grouping with the two compared objects in hand." |
| "brought to the human with findings and a recommendation, the taste call his" | INV-235 | DUPLICATE | R214.5 (4879): "close by bringing the decision to the human with its findings and a recommendation, the taste call staying the human's". |
| "the members are a closed enumerable set named in full on the enumerate-versus-ride keying" | INV-235 | DUPLICATE | R214.1 (4871): "treat the expensive-decision set as closed and enumerable … naming every member as either enumerated on its own row or riding inside another row's work." |
| "agent birth is the first member wired to carry it, T-22's ratification naming the read the owner ratifies on, the rest riding the class-level statement until each is wired member by member" | INV-235 | DUPLICATE | R214.2 (4872): "have each member carry it at its own decision point, a traceability test holding that this clause names the read and that agent birth carries it"; T-22 R197.4 (4503): "the owner *shall* ratify on the adversarial read the proposal carries". |
| "a stated duty at the enumerated decision points with a traceability test `tests/test_expensive_decision_read.py`" | INV-235 | DUPLICATE | R214.2 (4872): "a traceability test holding that this clause names the read and that agent birth carries it." (filename is a pin) |
| "no new push-gate letter since no gate reads a reversal cost — the far-tier and node-growth checks the precedent" | INV-235 | ABSENT | R214.1–R214.5 carry no clause on push-gate letters or a reversal-cost gate; spec is silent on this check's push status. |
| "the spec the law's one home, with no skill-prose fork" | INV-235 | KEEP | ownership note — one home for the law. |
| "the full anchor citations live in the spec clause and Formal-index row" | INV-235 | KEEP | pointer to the spec clause / index. |
| "ROADMAP 395" | INV-235 | KEEP | ROADMAP-row pointer. |
| "the authoring seat does not adversarially certify its own work" | INV-237 | DUPLICATE | R215.1 (4893): "*shall* never let it provide the change's own adversarial certification." |
| "the release's adversarial pass is authored by a fresh differently-contexted seat" | INV-237 | DUPLICATE | R215.2 (4894): "author a release's adversarial pass … with a fresh, differently-contexted seat". |
| "a newly added lens is self-applied to its own introducing document before release" | INV-237 | DUPLICATE | R215.3 (4898): "apply a newly added lens or rule to the document that introduces it and *shall* name the result in the release record." |
| "generalizing verify's fresh-eyes freshness [INV-46] and the periodic audit's adversarial stance to the release pass the 2.7.0 release ran in-context" | INV-237 | KEEP | provenance/ownership note — cites the landed 2.7.0 in-context release the rule generalizes from. |
| "carried into this node's verify station and product-prover as wiring" | INV-237 | KEEP | wiring note — verify station / product-prover carry it, ownership stays here. |
| "a release gate optionally requiring a dated clean-context review record naming a different seat" | INV-237 | DUPLICATE | R215.4 (4899): "The release gate *shall* be able to require a dated review record that exists, is dated to the release, and names a seat other than the release's." |
| "the rest a discipline the seat holds" | INV-237 | KEEP | enforcement/ownership note — not a stated spec rule. |
| "ROADMAP 422" | INV-237 | KEEP | ROADMAP-row pointer. |
| "also carries three steps whose governing law is the parallel-lanes node's … the steps staying here as wiring while the lane set, the claim's atomicity, and the landing commit's one-row shape are owned there and cited rather than restated" | (three steps) | KEEP | wiring/ownership note — steps sit here, law owned by the parallel-lanes node. |
| "the mid-work re-door is this node's step, the independence re-check it fires being the lanes node's law" | (mid-work re-door) | KEEP | wiring/ownership note — step here, re-check law owned by the lanes node. |

## pins-provenance list

Pins field (line 71). Every pin carrying a date, a session number, or a landed-row (ROADMAP-row) provenance note:

- none.

All ten pin labels carry only a step/section gloss and, on three, an anchor code (INV-113, INV-221, INV-233). No pin label carries a date, a session number, or a landed-row / ROADMAP-row provenance note. Provenance count: 0.

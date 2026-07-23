# owns-field relocation audit — node: communicator

Source: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, `### [node: communicator]`, **owns** field.
Spec checked: `PRODUCT_SPEC.md`.

| fragment (quoted; shortened with … past 40 words) | anchor | class | evidence |
| --- | --- | --- | --- |
| "the report step; the walk before it is build-pipeline's" | T-7 | KEEP | Ownership/placement note: identifies T-7 as the landing-report transition (R6.5, "*when* the wish lands, the system *shall* report to the person in one plain-language line…") and draws the ownership boundary — the pre-report walk belongs to the build-pipeline node, not here. States node placement, not a spec rule. |
| "the showing channel matches the session's seat" | INV-67 | DUPLICATE | Restates INV-67's rule. Spec R28.2: "The system *shall* show a local session's artifact as a local page in a browser window, and *shall* show a remote session's artifact through its own channel … carrying the same identifier and the same round-trip. [INV-67, INV-51]" (also R28.1: "*shall* read where the session runs … and *shall* name the channel it picked. [INV-67]"). |
| "the far backlog surfaces itself rarely and unasked: the status report carries a rare line that a far backlog is kept, at a settings-ladder cadence default recorded against a dated marker, an instance of the touchpoint-kind frame riding the status report the agent pushes" | INV-223 | DUPLICATE | Each clause restates a spec rule under INV-223. R239.1: "above that floor *shall* carry a rare status-report line naming that a far backlog is kept. [INV-222, INV-223]"; R239.2: "*shall* propose at most one such offer per 14 days as a settings-ladder default … and *shall* record the last self-surfacing in a dated marker. [INV-223, E-13]"; R239.3: "*shall* treat it as an asynchronous touchpoint that may only wait, holding the entry `far-tier-surfacing` in the manifest. [INV-223, INV-205]". |
| "the fixture check `guardrails/check-far-tier.py --window` reds a second offer inside the window, riding the suite and not the push chain" | INV-223 | PARTIAL | Spec covers the rule: R239.4 "*when* a second offer would fall inside the last surfacing's window, the system *shall* red the report-shape check…" and R94.3 "…*shall* red the report-shape check, which rides the suite and not the push chain since the status report is a chat surface with no committed file to gate." Spec lacks the concrete fixture path — no occurrence of `guardrails/check-far-tier.py --window` anywhere in PRODUCT_SPEC.md (it calls it only "the report-shape check"). That fixture-file pointer is the fact the spec does not carry. |
| "also carries the clock law's chat-arm sentence as a wiring pin — that clock invariant's owner is the guardrails node" | (wiring) | KEEP | Explicit wiring note: text carried here for reference, ownership assigned to the guardrails node. Cross-node wiring belongs in the architecture. |
| "also carries the two earned-message tells — the deposit-tell and the decline-tell — as status-report wiring, a plain notice register, owned by the base-rulebook" | (wiring) | KEEP | Explicit wiring note: status-report wiring whose owner is the base-rulebook. Cross-node wiring belongs in the architecture. |

## pins-provenance list

The **pins** field:
`skills/communicator/SKILL.md:35` (the rules), `:295` (rule 10 — the decision page), `:348` (rule 11 — the evidence walk), `:228` (rule 9 — the outcome-leads line shape), `:436` (the pre-report walk), `:282` (rule 7 — the chat-arm clock sentence)

Pin labels carrying a date, a session number, or a landed-row provenance note: **none.** Every label is a rule/step gloss; no label carries a date, a session number, or a landed-row (row NNN) note.

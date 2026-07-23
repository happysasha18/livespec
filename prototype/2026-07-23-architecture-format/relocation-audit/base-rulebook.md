# owns-field prose audit — node `base-rulebook`

Source: `prototype/2026-07-23-architecture-format/out/ARCHITECTURE.converted.md`, section `### [node: base-rulebook]`, **owns** field.
Duplication checked against `/Users/sashaabramovich/live-spec/PRODUCT_SPEC.md`.

| fragment (quoted; shortened past 40 words with …) | anchor | class | evidence |
| --- | --- | --- | --- |
| "a wrong referral is named as the finding where the exchange loops back over the same pair, rather than absorbed by the two-crossing cap" | INV-225 | DUPLICATE | Spec R196.9 line 4458: "*when* an exchange reaches the crossing bound through a referral met by a counter-referral between the same two agents, the system *shall* name the wrong referral in the sender's status report". Same rule: the loop-back over one pair earns the wrong-referral name at the bound. |
| "the checker `guardrails/check-wrong-referral.py` rides the suite not the push chain, the sibling of the far-tier report-shape check" | INV-225 | PARTIAL | Spec R196.11 line 4461 covers rides-suite/clear-of-push-chain: "the checker `guardrails/check-wrong-referral.py` *shall* read the shape of the exchange and ride the suite, staying clear of the push chain". Spec lacks the sibling relationship — the exact fact absent: "the sibling of the far-tier report-shape check". |
| "ROADMAP 388" | INV-225 | KEEP | ROADMAP-row pointer; stays in the architecture. |
| "three of these are read by the parallel-lanes node and stay here, each for a stated reason" | INV-9/INV-11 · session-identity · state-directory | KEEP | Wiring note — another node (parallel-lanes) reads these anchors, ownership stays here. |
| "the fence fires before every write and every commit in every writing skill with no lane rolling at all" | fence (INV-9/INV-11) | KEEP | Ownership rationale for keeping the fence anchor here (base rule, not lane-specific) rather than at the lanes node. |
| "the session identity is minted by every session at its start and feeds both the pen tie-break and the inbox source-mark's projection" | session-identity | KEEP | Wiring/ownership note — why the session-identity anchor stays here though the lanes node reads it (feeds the pen tie-break). |
| "the state-directory anchor is one anchor carrying two unrelated facts, the canonical `.live-spec` directory and the worktree-isolation default … so it sits here with its leading fact and its stated category while the lanes node owns the mechanism that default fires" | state-directory (E-31) | KEEP | Ownership/wiring note — states the split: leading fact stays here, the lanes node owns the mechanism the default fires. |
| "the brief's isolated-tree clause likewise stays with the delegation law that states it" | brief isolated-tree | KEEP | Wiring note — the text lives with the delegation law; ownership stays here. |
| "the named-reference pair — a code travels beside a one-sentence description pinned to the item's owning surface, so a bare code never stands alone before a reader" | E-35 | DUPLICATE | Spec R191.1 line 4242: "*when* a reference names an internal item the method carries a code for, the system *shall* carry the item's stable code beside a plain one-sentence description pinned to the item at its owning surface." |
| "the living description — a description that leaves a reader asking what a term means is rewritten on the owning agent's next penned run, taking the pen, deferred rather than reactive" | INV-240 | DUPLICATE | Spec R192.5 line 4285: "the system *shall* record the re-question and defer the rewrite to the owning agent's next turn writing the document, holding clear of a rewrite in the middle of another turn" (with R192.6 line 4286 "take the description's home document under its own pen"). |
| "earned auto-deposit and its two status-report tells — the deposit-tell and the decline-tell" | T-24 | DUPLICATE | Spec R195.12 line 4414 (deposit-tell): "*when* the agent deposits a message, the system *shall* tell its own user in the status report"; R195.13 line 4415 (decline-tell): "*when* the earned-message law declines a message the agent had drafted, the system *shall* tell the user in the status report with the reason it was withheld". |

## pins-provenance list

Every pin label in the **pins** field of `base-rulebook` was scanned for a date, a session number, or a landed-row provenance note. **None carry any.** The labels are anchor/rule descriptions and pointers only (e.g. `ROADMAP 424 [target]`, which is a roadmap target, not a landed-row provenance note). Dated/landed-row provenance notes (e.g. "row 52 landed 2026-07-05") appear in *other* nodes' pins, not in `base-rulebook`.

- (empty — no pin label carries a date, session number, or landed-row provenance note)

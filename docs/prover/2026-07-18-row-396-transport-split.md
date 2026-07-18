# Prover record — 2026-07-18 — row 396 — INV-236, the traffic-kind transport split (INV-183 corrected)

CROSS-LINK pass over the one delta plus the architecture lens on the new node-owned invariant.
Previous record (docs/prover/2026-07-18-rows-393-405-389.md) carried no unfolded rows into this one.

## Scope

One small row: a correction to INV-183's transport sentence plus a new law INV-236 (the traffic-kind
split) and its guardrails router. Shared docs (PRODUCT_SPEC.md, ARCHITECTURE.md, TEST_MATRIX.md,
ROADMAP.md) edited under one pen. No new pre-push gate — the router rides the suite the way the listener
tripwire does, so the gate chain (gates.yml, gate-red-proofs.json, pre-push letters a–z) is untouched.
VERSION held at 2.6.3.

## The machine-fact, verified before building (the premise blocker)

The distillation raised one premise blocker: the direct-channel fact must be verified on the real
machine, never derived. Read against INV-231 (row 405, landed): the harness's socket plumbing —
`messagingSocketPath`, the uds client, the local-session recipient kind — is built and switched OFF, and
no harness listener has shipped, so there is no live direct channel between two local sessions today.
INV-231's own text and its check (`guardrails/check-listener-tripwire.py`, field-gated, quiet on a
listenerless harness) carry this as an established fact, not a derivation. VERDICT: the machine-fact is
established by landed work; the landing proceeds and derives nothing that needs a real-machine probe.

## The correction — INV-183's transport sentence

- **The refused premise.** INV-183's old transport sentence ("two agents sharing one machine changes the
  transport's speed and leaves the contract itself untouched; a remote agent reaches the other through
  git alone") reasoned from the worst case (a remote seat reaches a repo through git alone [INV-112]) to
  the universal rule that git is every message's transport and co-location only a fast path. The owner
  refused that premise 2026-07-17.
- **The corrected sentence** states that which transport carries a message is decided by the traffic's
  kind and that the two-channel contract stays untouched whichever transport it takes, handing the detail
  to INV-236. Red-proven: `test_spec_corrects_inv183_transport_sentence` asserts the old sentence is gone
  and the traffic-kind cut is present.
- **The channel law survives untouched.** INV-183's subject is WHO talks and WHEN (the inbox channel and
  the published contract, count of two). INV-236 changes only which transport carries each traffic kind,
  so the channel count, the reply-rides-the-inbox arm [INV-192], and the no-third-channel rule are
  unweakened. Seam verified by reading INV-183 whole after the edit.

## INV-236 — the traffic-kind split

- **Cross-link.** INV-236 cuts inter-agent traffic by kind. A no-answer message (a durable record read on
  the neighbour's own clock, or a notification) takes the store road — one inbox file the sender deposits
  and the receiver sweeps later [E-11, T-10], reachable while the receiver is not running, committed and
  pushed when remote [INV-112]; this road works today, the remote-deposit arm having landed [ROADMAP 247].
  A conversation (a back-and-forth needing a live peer) takes the direct channel, which the harness has
  not shipped and which waits on the listener tripwire [INV-231]. Seams to INV-112 (the store/git road),
  INV-231 (the direct channel's availability), INV-129 (the receiver-armed watcher road), E-11/T-10 (the
  deposit and sweep) are by reference, not re-mint.
- **The machine-driven read (the router's honesty).** The conversation road's availability is not
  hardcoded to False — it is read from the session records through the listener tripwire's own
  socket-field truth [INV-231, reused, not copied — INV-194]. Verified: a fixture session record carrying
  a socket field flips the road to available and drops the `waits_on` marker
  (`test_conversation_available_when_a_listener_ships`), while an empty record set leaves it unavailable
  and naming the listener (`test_conversation_road_is_unavailable_today`,
  `test_conversation_road_names_the_listener`). So the day a listener ships, the router reports the road
  available on its own — the field-gating is real, never simulated.
- **The red proof.** `route` sends a no-answer message to the store road (available) and a conversation to
  the direct channel (unavailable, naming the listener); an unclassified message raises rather than
  guessing a route [INV-4]. 14 red against HEAD 50b9f2f (module + spec/index/architecture/matrix/roadmap
  absent), then green; the two not-wired absence assertions green throughout.
- **Architecture lens.** INV-236 owned by exactly one node (guardrails), pinned to
  `guardrails/route_agent_transport.py`, matching sibling INV-231's placement (the check lives in
  guardrails though the law sits beside INV-183 in the base-rulebook's inter-agent layer). The owns-cell
  note cites only guardrails-owned anchors, so no anchor is owned twice
  (`test_architecture_owns_every_anchor_once` green). No orphan node, no unowned fact. No new node — the
  router joins the guardrails node's existing suite-riding checks.
- **The wiring decision.** No new pre-push gate. A router is a stated routing rule a test exercises, not
  a committed file a push gate scans [INV-83]. It rides the suite the way the listener tripwire and the
  far-tier report-shape check do. `test_not_wired_as_a_prepush_gate` and `test_not_a_ci_step` hold the
  boundary.

## The field leg that stays open

The conversation channel's real first use is field-gated on the harness shipping a listener [INV-231,
row 405] — closable only when a listener ships, never self-certified on a local run [INV-94]. Row 396's
second paragraph (the direct-protocol prior-art sweep) is answered for co-located agents by the
machine-fact itself — the harness's dormant unix-domain-socket plumbing IS the local direct channel,
switched off — so the git-premise-free re-read is settled for this machine; a broader cost-and-portability
sweep across other shapes stays available as a research row, off this law's critical path.

## Open ⟨DECIDE⟩ touched

None. The delta touches no open decision marker.

## Verdict

0 must-fix. The correction removes the refused premise, INV-236 states the traffic-kind split, the road
each kind takes is red-proven, and the machine-fact is read (INV-231) rather than derived. The landing
stands; the conversation channel's real use stays field-gated on the listener.

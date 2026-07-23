# Relocation audit — node: inbox, owns field

The owns field carries two parentheticals of prose: one attached to `INV-249`
(the atomic-write deposit protocol) and one attached to `INV-232` (the remote
seat's read arm). Fragments below are split at clause level.

| fragment (quoted) | anchor | class | evidence |
|---|---|---|---|
| "the atomic-write deposit protocol — a deposit is written under a `.draft` name and made final by an atomic rename, the receiving sweep reading only a complete deposit and never a mid-write file" | INV-249 | DUPLICATE | R195.15 [INV-249]: "the system *shall* write a deposit into another window's inbox under a `.draft` name and make it final by an atomic rename once the content is complete." + R195.16 [INV-249]: "the receiving sweep *shall* act only on a finished deposit and *shall* pass over any name still carrying the `.draft` suffix". |
| "the concurrency half of E-11's one-file law" | INV-249 | KEEP | Ownership/wiring note — ties INV-249 to E-11's one-file law, explaining why the anchor sits at this node. Not a rule the spec restates. |
| "a consumer reading a private contract over git … needs a read grant the push grant does not supply" | INV-232 | DUPLICATE | R253.6 [INV-232]: "*when* a remote consumer reads a private producer repository, the system *shall* require a read grant recorded beside the push grant". Also R194.11 [INV-232]: "over git when remote under its recorded read grant". |
| "the consumer's read the spec-author node owns" | INV-232 | KEEP | Wiring note — the consumer-read text lives at the spec-author node; ownership of the read arm stays here. |
| "the producer repo readable by the consumer's seat" | INV-232 | DUPLICATE | Glossary, `grant`: "a read grant to clone and pull a private producer's repository." (states the read grant makes the private producer repo readable to the consumer). |
| "recorded in the host profile beside the push grant the push-law owns as `trust.read-grant`" | INV-232 | PARTIAL | Spec covers the placement — R253.6 [INV-232]: "a read grant recorded beside the push grant"; push grant home per INV-112 R253.1: "a per-repository grant recorded in the host profile". Spec lacks the literal field key: "as `trust.read-grant`". |
| "a grantless seat fails honestly naming the grant it lacks by the honest-failure rule" | INV-232 | DUPLICATE | R253.6 [INV-232]: "*shall* fail honestly naming the read grant it lacks rather than guess." |
| "the read-direction sibling of the remote arm's push grant this node owns" | INV-232 | KEEP | Ownership note — places the read grant as the read-direction sibling of the push grant the inbox node owns; explains why the anchor sits here. |
| "the honest-failure check `scripts/read-grant.py`" | INV-232 | KEEP | Pointer to the implementing artifact (also carried as a pin). |
| "the real cross-machine read field-gated on a private producer-and-consumer pair over a private repo, rows 385 and 247, this landing the law arm alone" | INV-232 | KEEP | ROADMAP/landed-row provenance pointer (rows 385 and 247) plus a field-gate note; stays in the architecture. |

## Pins provenance

Pins carrying a date, a session number, or a landed-row provenance note:

- none. Every pin label in the inbox node is a file/location pointer with at
  most a bare INV code (e.g. `scripts/stranger-wish-monitor.py:1` — "the monitor
  bridge, INV-147"). No pin carries a date, a session number, or a landed-row
  provenance note.

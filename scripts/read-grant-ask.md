READ-GRANT ASK — a remote consumer needs read access to this private contract's repo

A consumer reads a published contract over git when it runs on another machine [SPEC INV-187, INV-112].
On a PRIVATE producer repo (tlvphotos is one), that read needs its own grant: the repo readable —
clonable and pullable — by the consumer's seat. This is the read-direction sibling of the push grant
ask (scripts/grant-ask.md), and it is recorded the same way.

One action, yours:
1. Give the consumer's seat read access to the producer repo — grant the repo to the app the seat runs
   under, or add the seat's deploy key / token with read (clone + pull) scope.
   For a Claude GitHub app seat: https://github.com/settings/installations (logged in as the repo
   owner) → Claude App → Configure → Repository access → add the producer repository.
2. Tell me it is done. I record it in the host profile as trust.read-grant with today's date, beside
   the push grant (trust.push-grant, trust.github-grant), and the remote consumer's read is live for
   this repo.

Until then, the remote consumer cannot read the contract. It has named exactly this read grant as the
one thing it lacks; nothing else is blocked, and it reads nothing rather than guessing a workaround
[SPEC INV-67].

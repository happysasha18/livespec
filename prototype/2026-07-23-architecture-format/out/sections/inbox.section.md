### [node: inbox]

**responsibility** — parallel-safe intake door for wishes born outside a live-spec session; its remote arm for granted seats and its stranger arm (a monitor bridges Issues/Discussions into inbox files), two hosts on one repo converging on a single surfacing by a claim on the shared item

**owns** — E-11, T-10, INV-10, INV-112, INV-146, INV-147, INV-148, INV-149, INV-174, INV-192, INV-232 (the read-direction sibling of the remote arm's push grant this node owns), INV-249 (the concurrency half of E-11's one-file law)

**pins** — `inbox/README.md:3` (one door, one new file), `:10` (file format), `:15` (commit rule), `:23` (remote arm), `:28` (stranger arm), `scripts/stranger-wish-monitor.py:1` (the monitor bridge, INV-147), `scripts/stranger-wish-monitor.py:103` (the cross-host claim + arbitration, INV-149), `.github/ISSUE_TEMPLATE/wish.yml:1` (the wish template requesting a source, INV-146), `.github/workflows/stranger-monitor.yml:1` (the package repo's scheduled monitor, INV-148), `scripts/read-grant.py:1` (the read-grant honest-failure check, INV-232), `scripts/read-grant-ask.md:1` (the read grant ask, beside grant-ask.md, INV-232)

**notes** — INV-232: the consumer's read the spec-author node owns. INV-232: the honest-failure check `scripts/read-grant.py`. INV-232: the real cross-machine read field-gated on a private producer-and-consumer pair over a private repo, rows 385 and 247, this landing the law arm alone.
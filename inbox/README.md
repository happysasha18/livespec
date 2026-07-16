# inbox — parallel-safe intake for wishes and feedback

The one door into this repo for a session NOT assigned to live-spec itself (a host's adopt run, any passing
conversation). Such a session may do exactly one thing here: **create one NEW file per item** — a wish or a
piece of feedback. It never edits
the spec, the queue, the journal, the skills — and never an existing inbox file (SPEC INV-10).

Why a folder of files: creating a fresh file cannot collide with anyone; editing a shared file can.

**Format:** `YYYY-MM-DD-<source>-<slug>.md` (name taken? append `-2`, `-3`, … — the pack's one collision law, base rule 18; two sessions racing one slug: add a short session token to the source mark) — a few plain lines:
- the item, in plain words (a wish, a reaction, an answer, a report)
- why (what broke / what was missing, with the primary source if there is one)
- who threw it (which host / which conversation)

**From the same filesystem (a co-located window), the deposit is the file alone (SPEC INV-174).** You
share the assigned session's working tree and git index, so stop after writing the file: no staging, no
commit, no push — the assigned session's sweep commits the harvest itself, and your item is durable on
disk from the moment it is written. **From a separate clone,** commit your one new file (a commit touching
inbox/ only, message naming the source) — that commit is part of the exception. A live-spec session sweeps this folder as its first act, harvests each file into the home
its route owns (a wish into a ROADMAP row, feedback by the routing law — SPEC T-20), and removes the file
in the harvest commit (git history keeps it).

**From a remote seat, over git.** A remote seat reaches a repo only through git, so it also pushes.
The deposit stays one new file here, committed touching inbox/ only with the source named, and then pushed
under a per-repo grant recorded in the host profile like the push grant. A seat with no grant fails honestly:
it names the grant it lacks and hands the owner the one action that supplies it (SPEC INV-112).

**From a stranger, through GitHub.** A stranger is a contributor with no push rights and no per-repo grant —
a read-only collaborator on a private repo, or anyone at all on a public one. The git deposit is closed to
them, so their door is a GitHub Issue or Discussion opened by the wish template
(`.github/ISSUE_TEMPLATE/wish.yml`, `.github/DISCUSSION_TEMPLATE/wish.yml`), which requests a source. A stranger
never writes the queue or the repo. The **monitor** bridges the gap: `scripts/stranger-wish-monitor.py` runs on
a schedule, converts each open un-surfaced Issue or Discussion into one new inbox file here (naming the source
and its origin) and commits it, then records the item's update generation on a marker comment — from that
committed file on it is an ordinary inbox wish under the sweep above. The monitor holds no verdict; whether an
item is a wish, feedback, or neither stays the inbox sweep's call (SPEC T-20). A missing source is asked for in a
comment before routing, and newer activity on a surfaced item re-surfaces it, so nothing pressed onto a closed
wish is lost (SPEC INV-146, INV-147).

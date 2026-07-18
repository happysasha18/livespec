#!/usr/bin/env python3
"""read-grant.py — a remote consumer's read grant, and its honest grantless failure (SPEC INV-232, ROADMAP 389).

The defect (the 2026-07-17 audit's finding 8): INV-187 sends a remote consumer to read a private
contract "over git when remote" and cites [INV-112], whose home records only a PUSH grant on the deposit
path. No READ grant is defined anywhere, yet tlvphotos is a private repo and the promoter↔site pair is
the expected first real consumer [row 385]; the first contract read across machines has no stated road.

This is the LAW arm's honest-failure mechanism. The remote-seat law's read arm: a consumer reading a
private repo over git needs that repo readable — clonable, pullable — by the consumer's seat, and the
grant is recorded in the host profile beside the push grant [INV-82] as `trust.read-grant`. A seat with
no read grant fails honestly, naming the grant it lacks and handing the one action that supplies it
[INV-67] — the read-direction sibling of the push grant ask (scripts/grant-ask.md), whose ask lives in
scripts/read-grant-ask.md. The real cross-machine read is field-gated (tied to rows 385/247) and is not
attempted here; this module states the read-grant check and its honest failure alone.
"""
import sys

READ_GRANT_KEY = "trust.read-grant"


class ReadGrantMissing(Exception):
    """A grantless consumer's honest failure: it names the read grant it lacks and the one action."""

    def __init__(self, repo):
        self.repo = repo
        super().__init__(
            "read grant absent for %s: this consumer reads a private contract over git [INV-187, "
            "INV-112] and has no read grant for that repo. It names exactly this grant as the one thing "
            "it lacks and reads nothing (SPEC INV-67, INV-232). The one action, yours: grant the "
            "consumer's seat read access to %s (so it can clone and pull), then record %s for it in the "
            "host profile beside the push grant [INV-82]. See scripts/read-grant-ask.md."
            % (repo, repo, READ_GRANT_KEY))


def _kinds_of(record):
    """The grant kinds a record carries, as a list of lowercased strings."""
    if record is True:
        return ["all"]
    if isinstance(record, (list, tuple, set)):
        kinds = list(record)
    elif isinstance(record, dict):
        kinds = record.get("kind") or record.get("kinds") or record.get("grants") or []
    else:
        kinds = []
    if isinstance(kinds, str):
        kinds = [kinds]
    return [str(k).lower() for k in kinds]


def has_read_grant(repo, grant_records):
    """True when a read grant covering `repo` is recorded.

    `grant_records` is the host's recorded grants — a dict {repo: record} or a list of records each
    naming its `repo`. A record grants read when its kinds include read (a read-and-write app grant
    reads too), or an `all`/`full` grant. A record for another repo never satisfies this repo.
    """
    if isinstance(grant_records, dict):
        rec = grant_records.get(repo)
        records = [rec] if rec is not None else []
    else:
        records = [r for r in (grant_records or []) if isinstance(r, dict) and r.get("repo") == repo]
    for rec in records:
        for k in _kinds_of(rec):
            if "read" in k or "write" in k or k in ("all", "full"):
                return True
    return False


def check_read_grant(repo, grant_records):
    """Proceed when the read grant is recorded; else fail honestly naming the grant.

    Returns a plain-words ok line when a read grant for `repo` is on record. Raises ReadGrantMissing —
    which names the grant and the one action — on a grantless seat.
    """
    if has_read_grant(repo, grant_records):
        return ("read grant present for %s (%s recorded in the host profile) — the remote consumer may "
                "read the contract over git [INV-112, INV-187, INV-232]" % (repo, READ_GRANT_KEY))
    raise ReadGrantMissing(repo)


if __name__ == "__main__":
    # A tiny self-check: `read-grant.py <repo>` reports the grantless honest failure for that repo
    # against an empty grant set, so the failure's wording is exercisable on demand.
    repo = sys.argv[1] if len(sys.argv) > 1 else "owner/private-repo"
    try:
        print(check_read_grant(repo, {}))
    except ReadGrantMissing as e:
        print(e)
        sys.exit(1)

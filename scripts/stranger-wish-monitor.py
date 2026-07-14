#!/usr/bin/env python3
"""The stranger-door monitor (INV-147, ROADMAP row 261).

A stranger — a contributor with no push rights and no per-repo grant who can still open a
GitHub Issue — has no git path into the repo. This monitor is the bridge: it lists the open
stranger Issues, and for each that has not yet been surfaced at its current activity generation
it writes ONE new inbox/ file naming the source Issue and its source field, COMMITS that file
(touching inbox/ only, the source in the message — the same committed-file law the local and
remote arms obey [E-11, INV-112]), and records the surfaced generation on the Issue. From that
committed file on, the item is an ordinary inbox wish swept by the inbox law under its
git-atomic harvest [T-10, INV-11]. The monitor holds NO verdict: whether an item is a wish,
feedback, or neither stays the inbox sweep's call [T-20].

New stranger activity has an actor: the monitor records, at surfacing time, the Issue's update
generation, and on each run re-surfaces an Issue whose current generation is newer than the one
it last recorded — so a reopened, edited, or commented swept Issue is seen again rather than
sitting durably-recorded but operationally invisible [INV-138].

The surfacing decision is a PURE function of (open items, the generation each was last surfaced
at, existing inbox files), so a crash between depositing and recording still surfaces an item
exactly once. The process is single-instance by a lock (stale locks are stolen by age), and a
run that cannot reach the repo fails honestly [INV-67] — it names the reach it lacks, logs, and
retries on its next scheduled run, dropping no wish silently.

The bridge serves both Issues and Discussions: Issues over the `gh issue` commands, Discussions
over the GraphQL path (`gh api graphql`). Both are recorded by a hidden marker comment carrying
the surfaced generation, so neither needs a label.

The core (items_to_surface / surface_key / single_instance / run) carries no I/O and is unit
-tested in tests/test_stranger_door.py. main() wires the `gh` CLI and the inbox/ directory.
"""
from __future__ import annotations

import contextlib
import os
import subprocess
import sys
import time
from pathlib import Path

SURFACED_MARKER = "<!-- live-spec surfaced-gen:"  # a hidden marker comment records the generation
REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX = REPO_ROOT / "inbox"
LOCK_STALE_SECONDS = 3600  # a lock older than this is stolen (a hard-killed run left it behind)


# ---- the pure core -------------------------------------------------------------------------

def surface_key(item: dict) -> str:
    """The identity of one surfacing event: an item plus its activity generation."""
    return f"{item['kind']}-{item['number']}-gen{item.get('activity_gen', 0)}"


def items_to_surface(open_items: list[dict], existing_inbox_sources: set[str]) -> list[dict]:
    """The items that owe a fresh inbox file this run — the monitor's whole decision.

    An item is surfaced unless it was already surfaced at its current generation (no new
    activity since), or an inbox file for this exact generation already exists (the crash
    -safety check: a monitor that died after depositing but before recording still surfaces
    the item exactly once). `surfaced_gen` is the generation last recorded on the Issue, or
    None if it was never surfaced.
    """
    out = []
    for it in open_items:
        if it.get("surfaced_gen") == it.get("activity_gen"):
            continue
        if surface_key(it) in existing_inbox_sources:
            continue
        out.append(it)
    return out


@contextlib.contextmanager
def single_instance(lock_path, stale_seconds: float = LOCK_STALE_SECONDS):
    """Hold the monitor to one running instance; a second live acquisition stands down (False).

    A lock older than stale_seconds is stolen — a hard-killed run leaves its lock behind, and a
    permanent stand-down would blind the door against INV-147's required liveness.
    """
    acquired = False
    fd = None
    try:
        try:
            fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            acquired = True
        except FileExistsError:
            try:
                age = time.time() - os.stat(str(lock_path)).st_mtime
            except FileNotFoundError:
                age = None
            if age is not None and age > stale_seconds:
                try:
                    os.remove(str(lock_path))
                    fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                    acquired = True
                except (FileExistsError, FileNotFoundError):
                    acquired = False
            else:
                acquired = False
        yield acquired
    finally:
        if acquired:
            if fd is not None:
                os.close(fd)
            try:
                os.remove(str(lock_path))
            except FileNotFoundError:
                pass


def run(fetch_open_items, list_inbox_sources, deposit, log) -> dict:
    """One monitor pass over injected I/O — honest on an unreachable repo, silent-drop never.

    `deposit` returns True when the item was durably surfaced (file committed AND generation
    recorded); an item whose deposit fails is logged and NOT counted surfaced, so the next run
    retries it rather than leaving a half-done deposit to masquerade as done [INV-67].
    """
    try:
        open_items = fetch_open_items()
    except Exception as exc:  # any reach failure — network, auth, gh missing
        log(f"stranger-wish-monitor: cannot reach the repo ({exc}); dropping nothing, "
            f"retrying on the next scheduled run")
        return {"reachable": False, "surfaced": []}
    existing = list_inbox_sources()
    surfaced = []
    for item in items_to_surface(open_items, existing):
        if deposit(item):
            surfaced.append(item)
        else:
            log(f"stranger-wish-monitor: deposit of {surface_key(item)} did not complete; "
                f"not counted surfaced, will retry next run")
    log(f"stranger-wish-monitor: {len(surfaced)} item(s) surfaced into inbox files")
    return {"reachable": True, "surfaced": surfaced}


# ---- the gh / filesystem shell (not unit-tested; the core above is) ------------------------

def _gh_json(args: list[str]):
    import json
    out = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
    return json.loads(out.stdout or "[]")


def _gh_graphql(query: str, **variables):
    import json
    args = ["gh", "api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        args += ["-F", f"{k}={v}"]
    out = subprocess.run(args, capture_output=True, text=True, check=True)
    return json.loads(out.stdout or "{}")


def _gen_from_comments(comment_bodies: list[str]) -> str | None:
    """The generation last recorded, read from the newest marker comment (or None)."""
    gen = None
    for body in comment_bodies:
        if SURFACED_MARKER in body:
            gen = body.split(SURFACED_MARKER, 1)[1].split("-->", 1)[0].strip()
    return gen


def _owner_repo() -> tuple[str, str]:
    nwo = _gh_json(["repo", "view", "--json", "nameWithOwner"])["nameWithOwner"]
    owner, repo = nwo.split("/", 1)
    return owner, repo


def _fetch_issues():
    items = []
    issues = _gh_json(["issue", "list", "--state", "open", "--limit", "200",
                       "--json", "number,title,updatedAt,body"])
    for iss in issues:
        comments = _gh_json(["issue", "view", str(iss["number"]), "--json", "comments"]).get("comments", [])
        items.append({
            "kind": "issue",
            "number": iss["number"],
            "title": iss.get("title", ""),
            "body": iss.get("body", ""),
            "activity_gen": iss.get("updatedAt", ""),
            "surfaced_gen": _gen_from_comments([c.get("body", "") for c in comments]),
        })
    return items


def _fetch_discussions():
    owner, repo = _owner_repo()
    q = ("query($owner:String!,$repo:String!){repository(owner:$owner,name:$repo){"
         "discussions(first:100,states:OPEN){nodes{number id title body updatedAt "
         "comments(first:100){nodes{body}}}}}}")
    data = _gh_graphql(q, owner=owner, repo=repo)
    nodes = (data.get("data", {}).get("repository", {}) or {}).get("discussions", {}).get("nodes", [])
    items = []
    for d in nodes:
        bodies = [c.get("body", "") for c in d.get("comments", {}).get("nodes", [])]
        items.append({
            "kind": "discussion",
            "number": d["number"],
            "id": d["id"],  # the node id, needed to post a comment
            "title": d.get("title", ""),
            "body": d.get("body", ""),
            "activity_gen": d.get("updatedAt", ""),
            "surfaced_gen": _gen_from_comments(bodies),
        })
    return items


def _fetch_open_items():
    """List open Issues AND Discussions as monitor items, each carrying its activity generation."""
    return _fetch_issues() + _fetch_discussions()


def _list_inbox_sources() -> set[str]:
    keys = set()
    if not INBOX.exists():
        return keys
    for f in INBOX.glob("*.md"):
        for line in f.read_text(errors="ignore").splitlines():
            if line.startswith("surface-key:"):
                keys.add(line.split(":", 1)[1].strip())
    return keys


def _deposit(item: dict) -> bool:
    """Write, COMMIT, and record one surfaced item. Returns True only when all three held."""
    key = surface_key(item)
    slug = "".join(c if c.isalnum() else "-" for c in item.get("title", "wish"))[:40].strip("-")
    name = f"stranger-{item['kind']}-{item['number']}-{slug}.md"
    path = INBOX / name
    n = 2
    while path.exists():
        path = INBOX / f"stranger-{item['kind']}-{item['number']}-{slug}-{n}.md"
        n += 1
    path.write_text(
        f"surface-key: {key}\n"
        f"source: GitHub {item['kind']} #{item['number']}\n\n"
        f"# {item.get('title', '(no title)')}\n\n"
        f"{item.get('body', '')}\n\n"
        f"_Bridged from the stranger door by scripts/stranger-wish-monitor.py. "
        f"Route this by the inbox sweep; the wish-vs-not verdict is the sweep's [T-20]._\n"
    )
    # commit the file touching inbox/ only, the source in the message (E-11's committed-file law)
    rel = str(path.relative_to(REPO_ROOT))
    add = subprocess.run(["git", "-C", str(REPO_ROOT), "add", rel], capture_output=True, text=True)
    if add.returncode != 0:
        return False
    commit = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "commit", "-m",
         f"inbox: stranger {item['kind']} #{item['number']} ({item.get('title','')[:50]})", "--", rel],
        capture_output=True, text=True)
    if commit.returncode != 0:
        return False
    # record the surfaced generation on the item; a failed record is honest, not silent
    note = (f"Surfaced into the maintainers' inbox for review. Thank you — a live session will "
            f"route this wish.\n\n{SURFACED_MARKER} {item['activity_gen']} -->")
    if item["kind"] == "discussion":
        mut = ("mutation($discussionId:ID!,$body:String!){addDiscussionComment("
               "input:{discussionId:$discussionId,body:$body}){comment{id}}}")
        rec = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={mut}",
             "-F", f"discussionId={item['id']}", "-F", f"body={note}"],
            capture_output=True, text=True)
    else:
        rec = subprocess.run(
            ["gh", "issue", "comment", str(item["number"]), "--body", note],
            capture_output=True, text=True)
    return rec.returncode == 0


def main() -> int:
    lock = REPO_ROOT / ".live-spec" / "stranger-monitor.lock"
    lock.parent.mkdir(exist_ok=True)
    with single_instance(lock) as acquired:
        if not acquired:
            print("stranger-wish-monitor: another instance holds the lock; standing down")
            return 0
        result = run(_fetch_open_items, _list_inbox_sources, _deposit, print)
        return 0 if result["reachable"] else 1


if __name__ == "__main__":
    sys.exit(main())

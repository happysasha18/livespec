"""The stranger door (INV-146) and its monitor (INV-147) — ROADMAP row 261.

M-288 asserts the stranger-arm law lives in its prose homes and the templated door ships.
M-289 asserts the monitor's surfacing logic is a pure, idempotent, crash-safe function,
single-instance by a lock, and honest on an unreachable repo.
"""
import importlib.util
import os
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _load_monitor():
    path = REPO / "scripts" / "stranger-wish-monitor.py"
    spec = importlib.util.spec_from_file_location("stranger_wish_monitor", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---- M-288: the stranger arm lives in its prose homes + the templated door ships ----

def test_stranger_arm_in_prose_homes():
    spec = (REPO / "PRODUCT_SPEC.md").read_text()
    readme = (REPO / "inbox" / "README.md").read_text()
    # the spec inbox-law clause carries the stranger arm and the monitor bridge
    assert "stranger arm" in spec
    assert "monitor bridges" in spec or "monitor" in spec.lower()
    # inbox/README.md documents the stranger arm for a contributor without push/grant
    assert "stranger" in readme.lower()
    assert "monitor" in readme.lower()


def test_wish_issue_template_requests_source():
    tmpl = REPO / ".github" / "ISSUE_TEMPLATE" / "wish.yml"
    assert tmpl.exists(), "the templated stranger door must ship"
    text = tmpl.read_text().lower()
    # a source field is requested (the same source the inbox deposit names)
    assert "source" in text
    # the template is a GitHub Issue Form (has a body of form elements)
    assert "body:" in text or "- type:" in text


def test_stranger_arm_spec_anchor_and_index():
    spec = (REPO / "PRODUCT_SPEC.md").read_text()
    # each invariant carries a body clause (the bracketed anchor) AND a Formal-index row
    for code in ("INV-146", "INV-147"):
        assert f"[{code}]" in spec, f"{code} needs a body clause anchor"
        assert f"| {code} |" in spec, f"{code} needs a Formal-index row"


# ---- M-289: the monitor's surfacing logic ----

def test_monitor_surfaces_each_item_once():
    m = _load_monitor()
    # two open, never-surfaced items (no recorded generation)
    items = [
        {"kind": "issue", "number": 1, "activity_gen": "t0"},
        {"kind": "issue", "number": 2, "activity_gen": "t0"},
    ]
    first = m.items_to_surface(items, existing_inbox_sources=set())
    assert len(first) == 2
    # after depositing, their keys are recorded — a second run surfaces nothing
    keys = {m.surface_key(it) for it in first}
    second = m.items_to_surface(items, existing_inbox_sources=keys)
    assert second == []


def test_monitor_idempotent_on_already_surfaced():
    m = _load_monitor()
    # an item already surfaced at its current generation is never re-surfaced
    surfaced = [{"kind": "issue", "number": 1, "surfaced_gen": "t0", "activity_gen": "t0"}]
    assert m.items_to_surface(surfaced, existing_inbox_sources=set()) == []
    # crash-safety: never recorded but its inbox file already exists → not surfaced twice
    unrecorded = [{"kind": "issue", "number": 1, "activity_gen": "t0"}]
    key = m.surface_key(unrecorded[0])
    assert m.items_to_surface(unrecorded, existing_inbox_sources={key}) == []
    # new stranger activity (a newer generation than the one recorded) re-surfaces once —
    # the monitor is the actor: it compares generations, no label-dropping by a third party
    reactivated = [{"kind": "issue", "number": 1, "surfaced_gen": "t0", "activity_gen": "t1"}]
    assert len(m.items_to_surface(reactivated, existing_inbox_sources={key})) == 1


def test_monitor_deposit_failure_is_not_counted_surfaced():
    m = _load_monitor()
    logged = []
    result = m.run(
        fetch_open_items=lambda: [{"kind": "issue", "number": 1, "activity_gen": "t0"}],
        list_inbox_sources=lambda: set(),
        deposit=lambda item: False,  # deposit did not complete (commit or record failed)
        log=lambda msg: logged.append(msg),
    )
    # a half-done deposit is logged honestly and NOT counted surfaced, so next run retries it
    assert result["reachable"] is True
    assert result["surfaced"] == []
    assert any("did not complete" in msg for msg in logged)


def test_monitor_single_instance_lock(tmp_path):
    m = _load_monitor()
    lock = tmp_path / "monitor.lock"
    with m.single_instance(lock) as got_first:
        assert got_first is True
        # a second acquisition while the first is held stands down
        with m.single_instance(lock) as got_second:
            assert got_second is False
    # released after the first exits → acquirable again
    with m.single_instance(lock) as got_third:
        assert got_third is True


def test_monitor_honest_failure_on_unreachable():
    m = _load_monitor()

    def unreachable_fetch():
        raise ConnectionError("github unreachable")

    logged = []
    result = m.run(
        fetch_open_items=unreachable_fetch,
        list_inbox_sources=lambda: set(),
        deposit=lambda item: logged.append(("deposit", item)),
        log=lambda msg: logged.append(("log", msg)),
    )
    # honest failure: it names the reach it lacks, logs, drops nothing, deposits nothing
    assert result["reachable"] is False
    assert result["surfaced"] == []
    assert any(kind == "log" for kind, _ in logged)
    assert not any(kind == "deposit" for kind, _ in logged)


def test_monitor_does_not_retrigger_on_own_marker():
    # The monitor's own marker comment bumps the item's updatedAt. The recorded generation is that
    # marker's createdAt (the post-marker generation), so on the next run the item's updatedAt equals
    # the recorded generation and it reads as NO new activity — no re-surface loop. A daily cron would
    # otherwise manufacture one duplicate inbox file and one comment per open item every run.
    m = _load_monitor()
    marker = m.SURFACED_MARKER
    tm = "2026-07-14T10:00:00Z"
    comments = [{"body": f"Surfaced for review.\n\n{marker} 2026-07-14T09:00:00Z -->", "createdAt": tm}]
    # the recorded generation is the marker's own createdAt, not the pre-comment value in its body
    assert m._surfaced_gen_from_comments(comments) == tm
    # the item's updatedAt was bumped to the marker's time by the marker itself → not re-surfaced
    same = [{"kind": "issue", "number": 1, "activity_gen": tm, "surfaced_gen": tm}]
    assert m.items_to_surface(same, existing_inbox_sources=set()) == []
    # a genuine actor comment AFTER the marker advances updatedAt past it → re-surfaced once
    newer = [{"kind": "issue", "number": 1, "activity_gen": "2026-07-14T11:00:00Z", "surfaced_gen": tm}]
    assert len(m.items_to_surface(newer, existing_inbox_sources=set())) == 1


def test_fetch_discussions_degrades_when_disabled(monkeypatch):
    # A repo with Discussions turned off offers no discussion channel; _fetch_discussions returns []
    # rather than letting a GraphQL error fell the whole run (which would also drop the Issue arm).
    m = _load_monitor()

    def fake_gh_json(args):
        if "nameWithOwner" in args:
            return {"nameWithOwner": "owner/repo"}
        if "hasDiscussionsEnabled" in args:
            return {"hasDiscussionsEnabled": False}
        raise AssertionError("no further gh call expected once discussions are off: %r" % args)

    def fake_graphql(*a, **k):
        raise AssertionError("GraphQL must not run when discussions are disabled")

    monkeypatch.setattr(m, "_gh_json", fake_gh_json)
    monkeypatch.setattr(m, "_gh_graphql", fake_graphql)
    assert m._fetch_discussions() == []


# ---- M-290: the package repo's scheduled monitor action (INV-148) ----

WORKFLOW = REPO / ".github" / "workflows" / "stranger-monitor.yml"


def _workflow_text():
    assert WORKFLOW.exists(), "the scheduled monitor action must ship (INV-148)"
    return WORKFLOW.read_text()


def test_monitor_schedule_workflow_ships():
    text = _workflow_text()
    # it wakes on a daily cron AND on a manual dispatch (the verify hand-run)
    assert "schedule:" in text
    assert "cron:" in text
    assert "workflow_dispatch:" in text


def test_monitor_schedule_is_single_instance():
    text = _workflow_text()
    # a concurrency group serializes runs; an in-progress run is never cancelled,
    # so a second scheduled run waits rather than racing the first's push (the CI
    # form of the per-host lock, INV-147)
    assert "concurrency:" in text
    assert re.search(r"cancel-in-progress:\s*false", text), \
        "the concurrency group must not cancel a mid-flight run"


def test_monitor_schedule_grants_write_scopes():
    text = _workflow_text()
    # the token needs contents (push the inbox commit) + issues + discussions
    # (record the surfaced-generation marker comment, INV-146)
    for scope in ("contents", "issues", "discussions"):
        assert re.search(rf"{scope}:\s*write", text), f"missing {scope}: write grant"


def test_monitor_schedule_runs_and_pushes():
    text = _workflow_text()
    # it runs the monitor script and pushes whatever inbox commit it made
    assert "stranger-wish-monitor.py" in text
    assert "git push" in text

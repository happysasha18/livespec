"""INV-157, INV-158 — the browser test harness launches muted, reaps the whole
process group of the browser it spawned, and bounds each command with a real
per-command deadline; and it has one canonical home, shipped once by the pack as
a template (templates/headless_harness.py) rather than a copy each project
maintains alone. This guard asserts on the SHIPPED files at the string level: the
template is the generic core (no project-specific methods), it carries the mute
flag, the process-group reap, and the per-command deadline; test-author states
the rule; the spec states the two invariants.

The token assertions run against a STRIPPED view of the template — the module
docstring and every comment removed (``_stripped_code`` / ``_func_code``) — so a
token that lives only in prose can no longer satisfy the net: removing the real
construct turns the guard RED even while the docstring still mentions it. Landed
2026-07-15."""
import ast
import py_compile
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "headless_harness.py"


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _template():
    return TEMPLATE.read_text(encoding="utf-8")


def _strip_comments(text):
    """Drop full-line comments and trailing ``  # ...`` comments, line by line. A trailing comment is
    only cut when a ``#`` follows whitespace, so a ``#`` inside a string literal (never preceded by
    whitespace in this template, e.g. ``.split("#", 1)``) is left intact."""
    out = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        out.append(re.sub(r"\s+#.*$", "", line))
    return "\n".join(out)


def _stripped_code():
    """The template source with the module docstring AND all comments removed — real code only."""
    src = _template()
    tree = ast.parse(src)
    if ast.get_docstring(tree, clean=False) is not None and tree.body:
        seg = ast.get_source_segment(src, tree.body[0])
        if seg:
            src = src.replace(seg, "", 1)
    return _strip_comments(src)


def _func_code(funcname, classname=None):
    """The source of the named function with its own docstring and comments stripped — so a token
    asserted against it must live in the function's real code, not its prose. ``classname`` scopes
    the lookup to a method of that class (e.g. ``Browser.__init__``, not ``_WS.__init__``)."""
    src = _template()
    tree = ast.parse(src)
    scope = tree
    if classname is not None:
        scope = next((n for n in ast.walk(tree)
                      if isinstance(n, ast.ClassDef) and n.name == classname), None)
        assert scope is not None, f"class not found in template: {classname}"
    search = ast.walk(scope) if classname is None else scope.body
    for node in search:
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            seg = ast.get_source_segment(src, node)
            if ast.get_docstring(node, clean=False) is not None and node.body:
                dseg = ast.get_source_segment(src, node.body[0])
                if dseg:
                    seg = seg.replace(dseg, "", 1)
            return _strip_comments(seg)
    raise AssertionError(f"function not found in template: {classname or ''}.{funcname}")


def test_template_exists():
    assert TEMPLATE.exists()


def test_template_compiles():
    # A syntax error must never ship green [F6].
    py_compile.compile(str(TEMPLATE), doraise=True)


def test_template_launches_muted():
    # Asserted against STRIPPED code, so removing --mute-audio from the argv turns this RED even
    # though the docstring still names the flag [F2].
    assert "--mute-audio" in _stripped_code()


def test_template_reaps_process_group():
    src = _stripped_code()
    for token in ("killpg", "SIGKILL", "start_new_session"):
        assert token in src, token


def test_template_bounds_commands_with_a_deadline():
    src = _stripped_code()
    for token in ("CMD_TIMEOUT", "_deadline", "settimeout(None)"):
        assert token in src, token


def test_mute_flag_lives_in_the_chrome_argv():
    # --mute-audio must sit in the real CHROME launch argv (Browser.__init__), not just the docstring.
    init = _func_code("__init__", "Browser")
    assert "--mute-audio" in init, "--mute-audio"
    assert "--headless=new" in init            # among the other launch flags


def test_close_reaps_the_group_unconditionally():
    # close() must SIGKILL the whole group even when the leader already exited: a wedged renderer
    # child would orphan forever otherwise, and the profile-dir marker is rmtree'd right after, so
    # the launch sweep could not find it either [F1]. os.killpg lives in close()'s real code.
    close = _func_code("close", "Browser")
    assert "os.killpg" in close, "os.killpg"
    assert "SIGKILL" in close, "SIGKILL"
    # the reap is not gated on the leader still running
    assert "poll()" not in close, "reap must not be gated on proc.poll()"


def test_sweep_reap_is_scoped_to_the_same_boot():
    # The sweep records a boot id with the pid and only killpg's a DEAD owner from the SAME boot; a
    # cross-boot dir (a reused pid could name an unrelated live group) is rmtree'd, never signalled;
    # an ownerless dir is skipped entirely [F3/F4]. All asserted against real code.
    sweep = _func_code("_sweep_stale_profiles")
    assert "os.killpg" in sweep, "os.killpg"          # the same-boot reap
    assert "_boot_id()" in sweep, "_boot_id()"        # reads the current boot
    assert "_pid_alive(owner)" in sweep, "_pid_alive(owner)"
    assert "def _boot_id" in _stripped_code()         # the boot-id helper exists in real code
    # the boot id is recorded at launch alongside the pid
    assert "_boot_id()" in _func_code("__init__", "Browser")


def test_template_sweeps_stale_profiles_at_launch():
    # A run KILLED before teardown (SIGKILL, power loss, sleep) never runs close(), so its Chrome
    # group and profile dir leak and pile up across runs [INV-157]. The launch sweep is the backstop:
    # a named sweep function, called from Browser.__init__, that reaps only THIS harness's own
    # crash leftovers — a dir whose recorded owner pid is dead — never a live concurrent run.
    src = _stripped_code()
    assert "def _sweep_stale_profiles" in src            # the sweep symbol
    assert "_sweep_stale_profiles()" in src              # invoked at launch
    assert "OWNER_PID" in src                            # each run records its Chrome pid…
    assert "def _pid_alive" in src                       # …so the sweep can skip a live owner
    # the sweep must be safe against a concurrent run: a live recorded owner is skipped, not reaped
    assert "_pid_alive(owner)" in src


def test_template_teardown_on_signal_and_atexit():
    # The catchable exits (Ctrl-C, a plain kill) must still run close() and reap the group; the
    # launch sweep is the backstop only for the uncatchable ones [INV-157].
    src = _stripped_code()
    assert "import atexit" in src
    assert "atexit.register" in src
    assert "def _install_teardown_hooks" in src
    for token in ("signal.SIGINT", "signal.SIGTERM"):
        assert token in src, token


def test_template_is_generic_core_no_project_methods():
    src = _template()
    for method in ("def block", "def net_capture", "def net_clear", "def net_log",
                   "def pretend", "def set_local_storage", "def clear_storage",
                   "def local_storage"):
        assert method not in src, method


def test_template_docstring_cites_invariants():
    src = _template()
    assert "INV-157" in src
    assert "INV-158" in src


def test_test_author_states_the_harness_rule():
    ta = _read("skills/test-author/SKILL.md")
    assert "--mute-audio" in ta
    assert "INV-157" in ta


def test_spec_states_harness_invariants():
    spec = _read("PRODUCT_SPEC.md")
    assert "[INV-157]" in spec
    assert "[INV-158]" in spec
    assert "launches muted" in spec

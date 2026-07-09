"""Rendered documentation pages resolve their cross-links (ROADMAP row 195).

String-level assertions against the real output of scripts/render-doc.py:
  (a) a relative link to a sibling .md becomes the .html neighbour name;
  (b) a link carrying an anchor keeps the anchor (pipeline.html#station-9-...);
  (c) rendered headings carry GitHub-style ids (lowercase, spaces -> hyphens,
      punctuation stripped) so those anchors land;
  (d) an external http(s)/mailto link stays untouched;
  (e) a bare in-page #anchor link stays and lands on a heading id.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "render-doc.py"


def _render(src, dst):
    subprocess.run([sys.executable, str(SCRIPT), str(src), str(dst)],
                   check=True, capture_output=True, text=True)
    return dst.read_text(encoding="utf-8")


def _fixtures(tmp_path):
    (tmp_path / "pipeline.md").write_text(
        "# Pipeline\n\n"
        "## Station 9 — verify by deed\n\n"
        "Body of the station.\n",
        encoding="utf-8",
    )
    main = (
        "# Main\n\n"
        "See [the pipeline](pipeline.md) and "
        "[station nine](pipeline.md#station-9--verify-by-deed).\n\n"
        "External [repo](https://github.com/x/y) and [mail](mailto:a@b.com).\n\n"
        "Jump to [that section](#a-later-section).\n\n"
        "## A Later Section\n\n"
        "Body of the later section.\n"
    )
    (tmp_path / "main.md").write_text(main, encoding="utf-8")


def test_relative_md_link_becomes_html_neighbour(tmp_path):
    _fixtures(tmp_path)
    html = _render(tmp_path / "main.md", tmp_path / "main.html")
    assert 'href="pipeline.html"' in html
    assert 'href="pipeline.md"' not in html


def test_link_with_anchor_keeps_the_anchor(tmp_path):
    _fixtures(tmp_path)
    html = _render(tmp_path / "main.md", tmp_path / "main.html")
    assert 'href="pipeline.html#station-9--verify-by-deed"' in html
    assert "pipeline.md#" not in html


def test_headings_carry_github_style_ids(tmp_path):
    _fixtures(tmp_path)
    html = _render(tmp_path / "pipeline.md", tmp_path / "pipeline.html")
    # "Station 9 — verify by deed": lowercase, em-dash stripped (double hyphen), spaces -> hyphens
    assert 'id="station-9--verify-by-deed"' in html
    main_html = _render(tmp_path / "main.md", tmp_path / "main.html")
    assert 'id="a-later-section"' in main_html


def test_external_links_stay_untouched(tmp_path):
    _fixtures(tmp_path)
    html = _render(tmp_path / "main.md", tmp_path / "main.html")
    assert 'href="https://github.com/x/y"' in html
    assert 'href="mailto:a@b.com"' in html


def test_bare_in_page_anchor_stays_and_lands(tmp_path):
    _fixtures(tmp_path)
    html = _render(tmp_path / "main.md", tmp_path / "main.html")
    assert 'href="#a-later-section"' in html
    assert 'id="a-later-section"' in html

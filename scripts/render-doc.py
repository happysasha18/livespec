#!/usr/bin/env python3
"""render-doc.py — render a Markdown doc into one readable, self-contained HTML page.

Why this exists: documents a human must READ deserve typography, not a code editor
(Alexander, 2026-07-06: Sublime for prose reads "как когда-то на VT220"). Zero
dependencies — a deliberately modest converter covering what our docs actually use:
headings, paragraphs, bold/italic, inline code, fenced code blocks, lists, tables,
blockquotes, links, horizontal rules.

Usage: render-doc.py IN.md [OUT.html]   (default OUT: alongside IN, .html)
"""
import html
import re
import sys
from pathlib import Path


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', s)
    return s


def render(md):
    out, i, lines = [], 0, md.split("\n")
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(html.escape(lines[i]))
                i += 1
            out.append("<pre><code>%s</code></pre>" % "\n".join(block))
            i += 1
            continue
        m = re.match(r"^(#{1,6}) (.*)$", line)
        if m:
            n = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,})\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[\s:|-]+\|?\s*$", lines[i]):
                    cells = [c.strip() for c in lines[i].strip("|").split("|")]
                    rows.append(cells)
                i += 1
            if rows:
                thead = "<tr>%s</tr>" % "".join("<th>%s</th>" % inline(c) for c in rows[0])
                tbody = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r)
                                for r in rows[1:])
                out.append("<table><thead>%s</thead><tbody>%s</tbody></table>" % (thead, tbody))
            continue
        if line.startswith(">"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip("> "))
                i += 1
            out.append("<blockquote><p>%s</p></blockquote>" % inline(" ".join(block)))
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.) (.*)$", line)
        if m:
            ordered = m.group(2)[0].isdigit()
            items = []
            while i < len(lines):
                m2 = re.match(r"^(\s*)([-*]|\d+\.) (.*)$", lines[i])
                if m2:
                    items.append(m2.group(3))
                    i += 1
                elif lines[i].startswith(("  ", "\t")) and lines[i].strip() and items:
                    items[-1] += " " + lines[i].strip()
                    i += 1
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % inline(x) for x in items), tag))
            continue
        if line.strip():
            block = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|```|\s*([-*]|\d+\.) )", lines[i]):
                block.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % inline(" ".join(block)))
            continue
        i += 1
    return "\n".join(out)


STYLE = """
:root { color-scheme: light dark; }
body { font-family: -apple-system, "Segoe UI", Georgia, serif; max-width: 46rem;
       margin: 3rem auto 6rem; padding: 0 1.5rem; line-height: 1.65; font-size: 1.06rem; }
h1 { font-size: 1.7rem; line-height: 1.25; } h2 { font-size: 1.3rem; margin-top: 2.2rem; }
h3 { font-size: 1.1rem; }
code { font-family: ui-monospace, Menlo, monospace; font-size: .9em;
       background: rgba(127,127,127,.14); padding: .1em .35em; border-radius: 4px; }
pre { background: rgba(127,127,127,.10); padding: 1rem; border-radius: 8px; overflow-x: auto; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; display: block; overflow-x: auto; }
th, td { border: 1px solid rgba(127,127,127,.35); padding: .45rem .7rem; text-align: left;
         vertical-align: top; }
th { background: rgba(127,127,127,.12); }
blockquote { border-left: 3px solid rgba(127,127,127,.4); margin: 1rem 0; padding: .1rem 1.2rem;
             opacity: .85; }
hr { border: none; border-top: 1px solid rgba(127,127,127,.35); margin: 2rem 0; }
a { color: #2f6fed; }
"""


def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".html")
    md = src.read_text(encoding="utf-8")
    title = html.escape(next((l.lstrip("# ") for l in md.split("\n") if l.startswith("# ")), src.name))
    page = ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width, initial-scale=1'>"
            "<title>%s</title><style>%s</style></head><body>%s</body></html>"
            % (title, STYLE, render(md)))
    dst.write_text(page, encoding="utf-8")
    print(dst)


if __name__ == "__main__":
    main()

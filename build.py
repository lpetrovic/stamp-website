#!/usr/bin/env python3
"""Build the STAMP website from markdown.

    python3 build.py            # build into _site/
    python3 build.py --serve    # build, then preview at http://localhost:8000

Content lives in content/*.md (YAML front matter + markdown body).
News posts are content/news/YYYY-MM-DD-slug.md and are listed automatically.
Site-wide settings (menu, links, dates, funding note) are in site.yml.
"""
import datetime as dt
import http.server
import os
import re
import shutil
import socketserver
import sys

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
OUT = os.path.join(HERE, "_site")

md = MarkdownIt("commonmark", {"html": True, "typographer": True}).enable(["table", "strikethrough", "replacements", "smartquotes"])
env = Environment(loader=FileSystemLoader(os.path.join(HERE, "templates")), autoescape=select_autoescape(["html"]))
env.filters["markdown"] = lambda text: md.render(text or "")
env.filters["date"] = lambda d, fmt="%-d %B %Y": d.strftime(fmt) if hasattr(d, "strftime") else d


def read(path):
    """Return (front matter dict, markdown body) for a content file."""
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def write(rel_dir, html):
    d = os.path.join(OUT, rel_dir)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)


def root_for(rel_dir):
    depth = 0 if rel_dir in ("", ".") else rel_dir.strip("/").count("/") + 1
    return "../" * depth or "./"


def load_news():
    posts = []
    ndir = os.path.join(CONTENT, "news")
    for name in sorted(os.listdir(ndir), reverse=True):
        if not name.endswith(".md"):
            continue
        meta, body = read(os.path.join(ndir, name))
        if meta.get("draft"):
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", name)
        if not m:
            sys.exit(f"news file {name!r} must be named YYYY-MM-DD-slug.md")
        date = meta.get("date") or dt.date.fromisoformat(m.group(1))
        posts.append(dict(meta, date=date, slug=m.group(2), body=body, url=f"news/{m.group(2)}/",
                          html=md.render(body)))
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def build():
    site = yaml.safe_load(open(os.path.join(HERE, "site.yml"), encoding="utf-8"))
    site["year"] = dt.date.today().year
    news = load_news()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(HERE, "static"), os.path.join(OUT, "static"))

    def render(template, rel_dir, page, **extra):
        html = env.get_template(template).render(site=site, page=page, news=news, root=root_for(rel_dir),
                                                 current=rel_dir, **extra)
        write(rel_dir, html)

    for name in sorted(os.listdir(CONTENT)):
        if not name.endswith(".md"):
            continue
        meta, body = read(os.path.join(CONTENT, name))
        slug = name[:-3]
        rel = "" if slug == "index" else slug
        page = dict(meta, slug=slug, html=md.render(body))
        render(meta.get("template", "page.html"), rel, page)

    render("news_list.html", "news", {"title": "News", "slug": "news"})
    for post in news:
        render("post.html", post["url"].strip("/"), dict(post, title=post["title"]))

    open(os.path.join(OUT, ".nojekyll"), "w").close()
    if site.get("cname"):
        open(os.path.join(OUT, "CNAME"), "w").write(site["cname"] + "\n")
    print(f"built {OUT}  ({len(news)} news posts)")


def serve(port=8000):
    os.chdir(OUT)
    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True  # restart without "Address already in use"
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"serving http://localhost:{port}  (Ctrl+C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()

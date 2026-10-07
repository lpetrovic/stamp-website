# STAMP website

A small static site generated from markdown. You never touch HTML to update it.

## Updating content

| What | Where |
|------|-------|
| Project text on the home page | `content/index.md` |
| Objectives table (on the Project page) | `content/index.md` (the `objectives:` list in the header) |
| Team members | `content/team.md` (`members:` list; photos go in `static/img/team/`) |
| Publications | `content/publications.md` (plain markdown list) |
| Software and dataset | `content/software-data.md` |
| Contact | `content/contact.md` |
| **News post** | add `content/news/YYYY-MM-DD-short-title.md` (see below) |
| Menu, footer, social links, funding note | `site.yml` |

A news post looks like this:

```markdown
---
title: Paper accepted at ICRA 2027
summary: One sentence shown in the news list.
image: news/icra.jpg        # optional, file in static/img/news/
---
Body text in **markdown**.
```

Add `draft: true` to the header to hide a post. A new top-level page is just a new file in
`content/`. Add it to `menu:` in `site.yml` to show it in the navigation.

Then commit and push. GitHub Actions rebuilds and publishes the site automatically.

## Preview locally

```bash
pip install -r requirements.txt
python3 build.py --serve      # http://localhost:8000
```

## First-time setup on GitHub

1. Create a repository and push this `website/` folder as its root.
2. Go to **Settings → Pages → Source** and choose **GitHub Actions**.
3. Custom domain stamp.fer.hr: see `DEPLOY.md`.

All links are relative, so the site works both at `https://<user>.github.io/<repo>/` and at a custom domain.

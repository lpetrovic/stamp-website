# Publishing the website at stamp.fer.hr

- Repository: `git@github.com:lpetrovic/stamp-website.git` (branch `main`)
- Hosting: **GitHub Pages**. `.github/workflows/pages.yml` builds and publishes the site on every push to `main`.
- Domain: `stamp.fer.hr`. The FER webmaster adds an **ANAME** record pointing to `lpetrovic.github.io`.

Checked on 7 Oct 2026: `stamp.fer.hr` does not exist yet, and fer.hr has no CAA records, so GitHub can issue the free HTTPS certificate (Let's Encrypt).

## 1. Turn on GitHub Pages (once)

1. Open https://github.com/lpetrovic/stamp-website/settings/pages
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Open the **Actions** tab and re-run the "Build and deploy website" workflow (it fails on the first push because Pages was not on yet).
4. When it is green, the site is live at https://lpetrovic.github.io/stamp-website/

## 2. Verify the domain (recommended)

1. Open https://github.com/settings/pages (your **account** settings, not the repository's).
2. Click **Add a domain**, enter `stamp.fer.hr`.
3. GitHub shows a TXT record: name `_github-pages-challenge-lpetrovic.stamp.fer.hr` and a code. Put the code in the email below.
4. Leave that page open. After the webmaster adds the record, click **Verify**.

This stops anyone else from claiming `stamp.fer.hr` for their own GitHub Pages site if the repository is ever deleted or renamed.

## 3. Email the FER webmaster

> **Predmet:** DNS zapis za stamp.fer.hr (HRZZ projekt STAMP)
>
> Poštovani,
>
> za mrežne stranice HRZZ projekta STAMP (UIP-2026-8339) molim dodavanje sljedećih DNS zapisa u zonu fer.hr:
>
> 1. **ANAME** `stamp.fer.hr` → `lpetrovic.github.io`
>    (umjesto ANAME može i **CNAME** na isti cilj, jer je riječ o poddomeni)
> 2. **TXT** `_github-pages-challenge-lpetrovic.stamp.fer.hr` → `<kod s GitHuba>`
>    (služi za potvrdu vlasništva domene na GitHubu)
>
> Stranice se poslužuju preko GitHub Pages, koji sam izdaje HTTPS certifikat (Let's Encrypt), pa s vaše strane nije potrebno ništa drugo.
>
> Hvala unaprijed!
>
> Lijep pozdrav,
> Luka Petrović

## 4. Connect the domain (after the webmaster confirms)

1. Check DNS: `dig stamp.fer.hr` should return GitHub's addresses `185.199.108–111.153`.
2. Open https://github.com/lpetrovic/stamp-website/settings/pages, enter `stamp.fer.hr` under **Custom domain** and click **Save**. With Actions-based publishing this setting is what counts; `cname:` in `site.yml` is set too, so the config stays consistent.
3. Wait for the DNS check to pass and the certificate to be issued (minutes to about an hour), then tick **Enforce HTTPS**.
4. Open https://stamp.fer.hr

## Updating the site later

Edit the markdown in `content/` (see `README.md`), then commit and push to `main`. The site rebuilds automatically within a minute or two.

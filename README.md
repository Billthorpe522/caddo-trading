# Caddo Trading Company

A lightweight website for Caddo Trading Company and Sam Johnson in Murfreesboro, Arkansas. Current sales lead to the **Caddoman eBay store**; historical catalogs remain separately labeled reference material.

## Preview and deployment

- Existing GitHub Pages preview: https://billthorpe522.github.io/caddo-trading/
- Repository: https://github.com/Billthorpe522/caddo-trading
- Production/original website: http://www.caddotc.com/
- GitHub Pages currently publishes the root of `main`. A review branch does not change that deployment.
- No custom domain is configured here. Changing the original domain, TLS configuration, or hosting is a separate deployment decision.

Run locally from this folder:

```sh
python -m http.server 8768 --bind 127.0.0.1
```

Open http://127.0.0.1:8768/. No framework, package installation, API keys, or build server is required.

## Files and maintenance

| File | Purpose |
| --- | --- |
| `index.html` | Homepage, eBay sales path, certification, visit information, FAQ, contact |
| `collection.html` | Searchable directory of 20 historical catalog categories and a small sold gallery |
| `assets/styles.css` | Responsive design and reduced-motion support |
| `assets/site.js` | Mobile menu enhancement, archive filtering, footer year |
| `assets/images/` | Original brand and catalog images, plus one original trading-post photograph |
| `catalogue-*.html` | Eight compatibility pages for formerly broken prototype links |
| `404.html` | Branded recovery page |
| `robots.txt`, `sitemap.xml` | Discovery metadata for the GitHub Pages preview |
| `scripts/build_collection.py` | Generates the archive page and compatibility pages using only Python’s standard library |
| `scripts/check_site.py` | Checks local references, fragments, image metadata, headings, IDs, and sitemap syntax |
| `docs/2026-09-29-audit.md` | Review of the original site, prototype, sales channels, preservation, and changes |

Edit category names and links in `scripts/build_collection.py`, then run:

```sh
python scripts/build_collection.py
python scripts/check_site.py
node --check assets/site.js
```

The directory generator shares the homepage’s header, footer, and metadata. Re-run it after editing those homepage areas. Format generated HTML if desired; formatting is not required to serve the site.

The last formatting pass used `npx --yes prettier@3.6.2 --write index.html collection.html 404.html 'catalogue-*.html' assets/styles.css assets/site.js`.

## Content rules

- Keep eBay as the source of current prices, availability, shipping, returns, and checkout. Do not describe archived photographs as current listings.
- The original Museum Quality catalog explicitly says its pieces have sold.
- Contact Sam before publishing current certification fees, admission prices, opening hours, payment terms, memberships, or guarantees.
- No audio tour is offered until real recordings are supplied. No guest book is offered until entries can actually be delivered and managed.
- There are no analytics, third-party embeds, tracking scripts, forms, or local-storage writes in this version. External destinations have their own policies.
- Original images are retained without AI retouching or invented reconstructions.
- Canonical and Open Graph URLs currently describe the GitHub Pages preview. Update these, the sitemap, and recovery links together if a domain move is approved.

## Verification scope

The September 29 review checked desktop and phone layouts, menu navigation, archive search and its empty state, a working eBay handoff, FAQ expansion, local links and assets. Purchases, telephone calls, email delivery, and Sam’s current service capacity were not tested.

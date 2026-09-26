# Neocloud Summit 2026

Standalone site for the inaugural Neocloud Summit — October 8, 2026 · Hotel Kabuki, San Francisco · SF Tech Week.
Produced by IgniteGTM. Static HTML/CSS/JS — no build step, no framework.

Live at **https://neocloudsummit.ai** (GitHub Pages, `main` branch root; custom domain via `CNAME`).
Extracted from `neocloud.html` in the IgniteGTM site repo (`curseyoukakarot/ignite`).

## Run locally

```bash
python3 -m http.server 4173
# then open http://localhost:4173
```

## Structure

| Path | What it is |
|---|---|
| `index.html` | The Neocloud Summit landing page (page-specific styles inline in `<head>`) |
| `css/style.css` | IgniteGTM design system (shared with the main site) |
| `css/pages.css` | Sub-page components (page hero, detail rows, timeline, media sections) |
| `js/page.js` | Page behaviors — reveals, counters, nav, cursor (needs GSAP + ScrollTrigger from CDN) |
| `tools/speakers.py` | Regenerates the speaker cards from one list (run after editing speakers or adding headshots) |
| `logos/` | Original logo files as received; `assets/logos/` holds the web-ready white versions |
| `assets/` | Logo, favicons, event photography, and partner logos (`assets/logos/`, rendered pure white on black) |

Nav/footer links to other IgniteGTM pages point at the live site, `https://www.ignitegtm.com/`.

## Content

Page copy follows the summit's program overview; sessions and speakers follow the
organizers' agenda. Speaker cards show name, title, company, and LinkedIn only.
Planning documents are kept out of this repo.

Assets in `assets/video/` are compressed web encodes; video masters stay out of git.

Style rule: "neocloud" always takes a lowercase c, including the event name.

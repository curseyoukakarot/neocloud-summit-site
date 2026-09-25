# NeoCloud Summit 2026

Standalone site for the inaugural NeoCloud Summit — October 8, 2026 · Hotel Kabuki, San Francisco · SF Tech Week.
Produced by IgniteGTM. Static HTML/CSS/JS — no build step, no framework.

Extracted from `neocloud.html` in the IgniteGTM site repo (`curseyoukakarot/ignite`).

## Run locally

```bash
python3 -m http.server 4173
# then open http://localhost:4173
```

## Structure

| Path | What it is |
|---|---|
| `index.html` | The NeoCloud Summit landing page (page-specific styles inline in `<head>`) |
| `css/style.css` | IgniteGTM design system (shared with the main site) |
| `css/pages.css` | Sub-page components (page hero, detail rows, timeline, media sections) |
| `js/page.js` | Page behaviors — reveals, counters, nav, cursor (needs GSAP + ScrollTrigger from CDN) |
| `assets/` | Logo, favicons, and event photography |

Nav/footer links to other IgniteGTM pages point at the live site, `https://www.ignitegtm.com/`.

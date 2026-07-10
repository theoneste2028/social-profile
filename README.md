# Social Profile — Linktree Page

A self-contained, dependency-free "linktree" style landing page for my investing / quant-finance personal brand. A single Python script generates a static `index.html` — no frameworks, no npm, no pip installs.

**Live site:** _add your Netlify/Vercel URL here after deploying_

## What's in this repo

| File | Purpose |
|------|---------|
| `linktree.py` | Generator script. Edit the `CONFIG` block, run it, and it writes `index.html`. |
| `index.html` | The generated static page — this is what gets deployed. |
| `README.md` | This file. |

## How it works

All content (name, handle, tagline, links, accent color) lives in the `CONFIG` dictionary at the top of `linktree.py`. The script injects that config into an inline HTML/CSS template and writes a single, fully self-contained HTML file with inline SVG icons — no external assets except Google Fonts.

## Usage

Requires Python 3 (standard library only).

```bash
# Generate index.html in the current folder
python linktree.py

# Or write to a custom path
python linktree.py --out site.html
```

Open `index.html` in a browser to preview.

## Updating the page

1. Edit the `CONFIG` block in `linktree.py` (links, tagline, colors, etc.)
2. Re-run `python linktree.py`
3. Commit and push both files:

```bash
git add linktree.py index.html
git commit -m "Update links"
git push
```

If the repo is connected to Netlify or Vercel, the site redeploys automatically on push.

## Deploying (Netlify)

1. Push this repo to GitHub (make sure `index.html` is committed).
2. In Netlify: **Add new site → Import an existing project → GitHub** and pick this repo.
3. Build settings:
   - **Build command:** leave blank
   - **Publish directory:** `.` (the repo root)
4. Deploy. Every future push updates the live site.

## Customization

- **Accent color:** change `"accent"` in `CONFIG` (e.g. `#f0a020` for amber).
- **Avatar:** paste an image URL into `"avatar_url"`, or leave blank to use the monogram.
- **Links:** add/remove entries in the `"links"` list. Available icon types: `x`, `blossom`, `linkedin`, `github`, `website`, `substack`, `stocktwits`, `email`, `link`.

## Disclaimer

Not financial advice. This site documents a personal investing journey.

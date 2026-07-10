#!/usr/bin/env python3
"""
build_linktree.py
-----------------
Generates a self-contained, dependency-free linktree page (index.html) for an
investment-journey / quant-finance personal brand.

Usage:
    python build_linktree.py                 # writes ./index.html
    python build_linktree.py --out site.html # custom output path

Edit the CONFIG block below, then re-run. No pip installs required (stdlib only).
Host the resulting index.html on GitHub Pages, Vercel, Netlify, etc.
"""

import argparse

# ----------------------------------------------------------------------------
# CONFIG — edit this block, then re-run.
# ----------------------------------------------------------------------------
CONFIG = {
    "name": "Theoneste Ndahimana",
    "tagline": "Documenting an investing journey — markets, models, and the math behind them.",
    "monogram": "TN",                          # fallback avatar if no image
    "avatar_url": "",                          # optional: paste an image URL to use instead of the monogram
    "accent": "#3fb950",                       # single accent color (terminal green). Try "#f0a020" for amber.
    # Links render top-to-bottom in this order. "type" picks the icon.
    # Available icon types: x, blossom, linkedin, github, website, substack, stocktwits, email, link
    "links": [
        {"label": "X / Twitter",        "url": "https://x.com/da_goatt263",                "type": "x",         "note": "Daily takes & trade journal"},
        {"label": "Blossom",            "url": "https://www.blossomsocial.com/users/Theoneste__IYUW3JojLLYMZUFU",   "type": "blossom",   "note": "Portfolio & investing journey"},
        {"label": "LinkedIn",           "url": "https://www.linkedin.com/in/theoneste-nd",     "type": "linkedin",  "note": "Professional background"},
        # Optional — uncomment / edit if you'll keep them active:
        # {"label": "Substack",  "url": "https://yourname.substack.com", "type": "substack",  "note": "Long-form write-ups"},
        # {"label": "StockTwits","url": "https://stocktwits.com/yourname","type": "stocktwits","note": "Market chatter"},
        {"label": "Email",              "url": "mailto:tnd@u.northwestern.edu",           "type": "email",     "note": "For recruiters/Any Contacts"},
    ],
    "footer": "Not financial advice. Built for documenting a personal investing journey.",
}

# ----------------------------------------------------------------------------
# Inline SVG icons (no external requests).
# ----------------------------------------------------------------------------
ICONS = {
    "x": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
    "blossom": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2c1.6 0 2.9 1.3 2.9 2.9 0 .5-.1.9-.3 1.3 1.3-.6 2.9-.2 3.7 1.1.8 1.3.5 3-.6 3.9.4 0 .8.1 1.2.3 1.4.6 2.1 2.2 1.5 3.6-.6 1.4-2.2 2.1-3.6 1.5.4.4.7.9.8 1.5.3 1.5-.7 3-2.2 3.3-1.5.3-3-.7-3.3-2.2-.1.6-.4 1.1-.8 1.5-1.1 1.1-2.8 1.1-3.9 0-.4-.4-.7-.9-.8-1.5-.3 1.5-1.8 2.5-3.3 2.2-1.5-.3-2.5-1.8-2.2-3.3.1-.6.4-1.1.8-1.5-1.4.6-3-.1-3.6-1.5-.6-1.4.1-3 1.5-3.6.4-.2.8-.3 1.2-.3-1.1-.9-1.4-2.6-.6-3.9.8-1.3 2.4-1.7 3.7-1.1-.2-.4-.3-.8-.3-1.3C9.1 3.3 10.4 2 12 2zm0 7a3 3 0 100 6 3 3 0 000-6z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 110-4.13 2.06 2.06 0 010 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.37.5 0 5.87 0 12.5c0 5.3 3.44 9.8 8.21 11.39.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.75.08-.73.08-.73 1.21.09 1.84 1.24 1.84 1.24 1.07 1.84 2.81 1.31 3.5 1 .11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 016 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.24 2.88.12 3.18.77.84 1.23 1.91 1.23 3.22 0 4.61-2.8 5.63-5.48 5.92.43.37.81 1.1.81 2.22v3.29c0 .32.22.7.83.58A12 12 0 0024 12.5C24 5.87 18.63.5 12 .5z"/></svg>',
    "website": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 6 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-6-3.8-9s1.3-6.5 3.8-9z"/></svg>',
    "substack": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22.539 8.242H1.46V5.406h21.08v2.836zM1.46 10.812V24L12 18.11 22.54 24V10.812H1.46zM22.54 0H1.46v2.836h21.08V0z"/></svg>',
    "stocktwits": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l5-5 4 3 7-8"/><path d="M21 7v5h-5"/></svg>',
    "email": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 6l10 7 10-7"/></svg>',
    "link": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 007 0l3-3a5 5 0 00-7-7l-1.5 1.5M14 11a5 5 0 00-7 0l-3 3a5 5 0 007 7l1.5-1.5"/></svg>',
}

# ----------------------------------------------------------------------------
# HTML / CSS template. {ACCENT} and {LINKS}/{AVATAR}/etc. are replaced below.
# CSS braces are doubled so .format() leaves them intact.
# ----------------------------------------------------------------------------
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{NAME} — Links</title>
<meta name="description" content="{TAGLINE}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {{
    --accent: {ACCENT};
    --bg: #0a0e0f;
    --panel: #11181a;
    --panel-hover: #161f22;
    --border: #1f2b2e;
    --text: #e6edec;
    --muted: #7d8d8a;
    --mono: 'IBM Plex Mono', ui-monospace, monospace;
    --sans: 'IBM Plex Sans', system-ui, sans-serif;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ height: 100%; }}
  body {{
    font-family: var(--sans);
    background:
      radial-gradient(900px 500px at 50% -10%, rgba(63,185,80,0.10), transparent 60%),
      var(--bg);
    color: var(--text);
    min-height: 100vh;
    display: flex; align-items: flex-start; justify-content: center;
    padding: 64px 20px 48px;
    -webkit-font-smoothing: antialiased;
    position: relative; overflow-x: hidden;
  }}
  /* subtle grain texture */
  body::after {{
    content: ""; position: fixed; inset: 0; pointer-events: none; opacity: 0.035;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  }}
  .wrap {{ width: 100%; max-width: 460px; position: relative; z-index: 1; }}

  .ticker {{
    font-family: var(--mono); font-size: 11px; letter-spacing: 0.18em;
    color: var(--muted); text-transform: uppercase; text-align: center;
    margin-bottom: 28px; opacity: 0; animation: rise 0.6s ease forwards;
  }}
  .ticker b {{ color: var(--accent); }}

  .head {{ text-align: center; margin-bottom: 36px; }}
  .avatar {{
    width: 84px; height: 84px; border-radius: 50%; margin: 0 auto 18px;
    display: grid; place-items: center; object-fit: cover;
    background: var(--panel); border: 1px solid var(--border);
    font-family: var(--mono); font-weight: 600; font-size: 26px; color: var(--accent);
    box-shadow: 0 0 0 4px rgba(63,185,80,0.06);
    opacity: 0; animation: rise 0.6s ease 0.05s forwards;
  }}
  .name {{
    font-family: var(--mono); font-weight: 600; font-size: 22px; letter-spacing: -0.01em;
    opacity: 0; animation: rise 0.6s ease 0.1s forwards;
  }}
  .handle {{
    font-family: var(--mono); font-size: 13px; color: var(--accent); margin-top: 4px;
    opacity: 0; animation: rise 0.6s ease 0.15s forwards;
  }}
  .tagline {{
    font-size: 14px; color: var(--muted); line-height: 1.5; margin-top: 12px;
    max-width: 340px; margin-left: auto; margin-right: auto;
    opacity: 0; animation: rise 0.6s ease 0.2s forwards;
  }}

  .links {{ display: flex; flex-direction: column; gap: 12px; }}
  .link {{
    display: flex; align-items: center; gap: 14px; text-decoration: none;
    background: var(--panel); border: 1px solid var(--border); border-radius: 12px;
    padding: 15px 16px; color: var(--text);
    transition: transform 0.16s ease, border-color 0.16s ease, background 0.16s ease;
    opacity: 0; animation: rise 0.5s ease forwards;
  }}
  .link:hover {{
    transform: translateY(-2px);
    background: var(--panel-hover);
    border-color: var(--accent);
  }}
  .ic {{
    flex: 0 0 38px; width: 38px; height: 38px; border-radius: 9px;
    display: grid; place-items: center;
    background: rgba(63,185,80,0.08); color: var(--accent);
    border: 1px solid var(--border);
  }}
  .ic svg {{ width: 19px; height: 19px; }}
  .meta {{ flex: 1; min-width: 0; }}
  .meta .label {{ font-family: var(--mono); font-weight: 500; font-size: 15px; }}
  .meta .note {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}
  .chev {{ color: var(--muted); flex: 0 0 auto; transition: transform 0.16s ease, color 0.16s ease; }}
  .link:hover .chev {{ transform: translateX(3px); color: var(--accent); }}

  .footer {{
    text-align: center; margin-top: 36px; font-family: var(--mono);
    font-size: 11px; color: var(--muted); letter-spacing: 0.03em; line-height: 1.6;
    opacity: 0; animation: rise 0.6s ease 0.5s forwards;
  }}

  @keyframes rise {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; opacity: 1 !important; }} }}
</style>
</head>
<body>
  <main class="wrap">
    <div class="ticker">// LIVE &nbsp;·&nbsp; <b>INVESTING JOURNAL</b> &nbsp;·&nbsp; FOLLOW ALONG</div>
    <header class="head">
      {AVATAR}
      <h1 class="name">{NAME}</h1>
      <div class="handle">{HANDLE}</div>
      <p class="tagline">{TAGLINE}</p>
    </header>
    <nav class="links">
      {LINKS}
    </nav>
    <p class="footer">{FOOTER}</p>
  </main>
</body>
</html>
"""

CHEVRON = '<svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg>'


def build_link(item, delay):
    icon = ICONS.get(item.get("type", "link"), ICONS["link"])
    note = item.get("note", "")
    note_html = f'<div class="note">{note}</div>' if note else ""
    return (
        f'<a class="link" href="{item["url"]}" target="_blank" rel="noopener" '
        f'style="animation-delay:{delay:.2f}s">'
        f'<span class="ic">{icon}</span>'
        f'<span class="meta"><div class="label">{item["label"]}</div>{note_html}</span>'
        f'{CHEVRON}</a>'
    )


def build_avatar(cfg):
    if cfg.get("avatar_url"):
        return f'<img class="avatar" src="{cfg["avatar_url"]}" alt="{cfg["name"]}">'
    return f'<div class="avatar">{cfg.get("monogram", "")}</div>'


def main():
    parser = argparse.ArgumentParser(description="Generate a linktree index.html")
    parser.add_argument("--out", default="index.html", help="output file path")
    args = parser.parse_args()

    links_html = "\n      ".join(
        build_link(item, 0.25 + i * 0.06) for i, item in enumerate(CONFIG["links"])
    )

    html = TEMPLATE.format(
        NAME=CONFIG["name"],
        HANDLE=CONFIG.get("handle", ""),
        TAGLINE=CONFIG["tagline"],
        ACCENT=CONFIG["accent"],
        AVATAR=build_avatar(CONFIG),
        LINKS=links_html,
        FOOTER=CONFIG.get("footer", ""),
    )

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {args.out} ({len(CONFIG['links'])} links). Open it in a browser to preview.")


if __name__ == "__main__":
    main()
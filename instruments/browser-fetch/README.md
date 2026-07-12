# browser-fetch — a browser when a plain fetch is blocked

An MCP server that gives a Claude teammate a way through when `WebFetch`/curl
get blocked (403s, anti-bot, Cloudflare Turnstile). Two tools, tried in order:

| Tool | What | When |
|---|---|---|
| `browser_fetch` | a **fresh, disposable, headless Chrome** per call (Playwright) | first resort — a real engine beats a bare HTTP client |
| `browser_fetch_persistent` | the **operator's own already-running Chrome** over the DevTools Protocol | only if `browser_fetch` is also blocked — an aged, real session with genuine cookies/history clears checks a brand-new automated browser can't |

Both return `status`/`title`/`url` + rendered text (or `raw_html=True`),
truncated to 80k chars to stay token-considerate.

## Why it's an *instrument* (and a different kind)

`tools/` enforce, the other `instruments/` **observe** — browser-fetch
**extends the teammate's reach**, a third verb (ADR 0006 addendum). It earns its
place here because its value is wholly the working-together relationship: it
exists so the teammate can get through a wall, and so the operator can help
(starting a real Chrome to clear a captcha the agent can't). Unlike the observer
instruments it is **Python, has dependencies, and acts on the world** rather than
reading logs read-only — the honest exception that widened the layer.

## Setup

```sh
./setup          # builds the venv (mcp + playwright + Chromium), prints the registration
```

The **code** lives here (versioned, public); the **venv** is a regenerable build
artifact under `~/.cache/atelier/browser-fetch/` — never committed, never in
iCloud. `setup` prints the exact `~/.claude.json` `mcpServers` snippet; Claude
Code picks it up on its next start.

**Intel macOS:** `constraints.txt` pins `cryptography<46` (newer versions dropped
prebuilt wheels for that platform). Needs a Python new enough for the `mcp` SDK
(3.11+; developed on 3.14).

### For `browser_fetch_persistent` — start a dedicated Chrome once per login

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --remote-debugging-port=9222 \
    --user-data-dir="$HOME/.chrome-claude-fetch-profile" \
    --no-first-run --no-default-browser-check
```

Use the binary path directly (`open -a` drops the flags if Chrome is already
running). **A DEDICATED profile — never your everyday Chrome** — so it never
touches personal logins/cookies. The debug port binds to localhost only and has
no auth of its own; never expose it on a network interface.

## Verification

Not unit-tested in CI: it drives a real browser, which CI can't cheaply do. The
floor scanners still cover `server.py` (leak/secret), and behaviour is verified
by a live fetch after `setup` (proven on adoption: `browser_fetch` returned a
rendered page end-to-end). Machine- and person-specific detail was scrubbed
before this entered the public repo.

# browser-fetch — a browser when a plain fetch is blocked

An MCP server that gives a Claude teammate a way through when `WebFetch`/curl
get blocked (403s, anti-bot, Cloudflare Turnstile). Two tools, tried in order:

| Tool | What | When |
|---|---|---|
| `browser_fetch` | a **fresh, disposable, headless Chrome** per call (Playwright) | first resort — a real engine beats a bare HTTP client |
| `browser_fetch_persistent` | a **real Chrome the operator started** on `:9222` over the DevTools Protocol — dedicated profile by default (rung 4), or their everyday session (rung 5) | only if `browser_fetch` is also blocked — a real, non-headless (and optionally aged) session clears checks a fresh automated browser can't |

Both return `status`/`title`/`url` + rendered text (or `raw_html=True`),
truncated to 80k chars to stay token-considerate.

## The fetch escalation ladder

browser-fetch is rungs 3–5 of how a Claude teammate fetches from the internet.
**Always start at the top and step down only when the current rung is blocked** —
each rung costs more (time, tokens, or the operator's attention).

| # | Method | What it is | Isolation | Needs the operator? |
|---|--------|-----------|-----------|---------------------|
| 1 | **WebFetch / WebSearch** | built-in; fetch a known URL (cleaned content) or search to find one | n/a | no |
| 2 | **curl / raw HTTP** | raw bytes — APIs, files, exact headers, or when #1's processing gets in the way (same anti-bot profile as #1: a bare HTTP client) | n/a | no |
| 3 | **`browser_fetch`** | a **completely standalone, disposable Chrome** the agent launches (headless) — its own process/session, **no** cookies, history, extensions, or downloads shared with the operator's browsing; can't be clicked away or broken by accident | fully isolated | no |
| 4 | **`browser_fetch_persistent` — dedicated profile** | a **standalone, non-headless** Chrome the operator started on `:9222` with a **dedicated** profile — like #3 but real/visible (some anti-bot blocks headless: #3's UA still says `HeadlessChrome`), still isolated from everyday browsing | isolated (dedicated profile) | ⚠️ operator starts it |
| 5 | **`browser_fetch_persistent` — everyday session** | the operator's **own everyday Chrome** — real history, cookies, logged-in sessions; "just another tab as if the operator opened it". Only when the operator **deliberately** exposes that profile on `:9222` | none — the operator's real browser | ⚠️ operator exposes it; may clear a challenge in-window |
| 6 | **ask the operator to paste** | full manual fallback — when even the operator's browser hits a challenge only a human clears | — | ⚠️ fully manual |

Today rungs 3–5 are **Chrome only**; other engines (Safari, Firefox) are roadmap.
The single `browser_fetch_persistent` tool serves both rung 4 and rung 5 — which
one depends on **which profile the operator exposes on `:9222`** (dedicated = 4,
everyday = 5).

### Credential boundary (non-negotiable)

Across **every** rung: the agent may **ride a session the operator has already
authenticated** (existing cookies / a logged-in tab are fair game). The agent may
**never use the browser's *saved credentials*** — password-manager entries,
autofill, stored logins — to authenticate, nor access those credentials
themselves, **without the operator's explicit permission**. Using an existing
session is fine; touching the credentials that mint one is the sensitive line.
(This is the operational statement of a rule owed to `method/` doctrine — see
ROADMAP.)

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
running). The `--user-data-dir` above is a **dedicated profile (rung 4)** —
isolated from everyday browsing, the safe default. Exposing your **everyday**
profile instead (rung 5 — omit the dedicated `--user-data-dir`) is a
*deliberate* operator choice for when only a real logged-in session gets through;
the **credential boundary above still binds** (ride the session, never the saved
credentials). The debug port binds to localhost only and has no auth of its own;
never expose it on a network interface.

## Verification

Not unit-tested in CI: it drives a real browser, which CI can't cheaply do. The
floor scanners still cover `server.py` (leak/secret), and behaviour is verified
by a live fetch after `setup` (proven on adoption: `browser_fetch` returned a
rendered page end-to-end). Machine- and person-specific detail was scrubbed
before this entered the public repo.

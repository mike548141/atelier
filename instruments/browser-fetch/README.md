# browser-fetch — a browser when a plain fetch is blocked

An MCP server that gives a Claude teammate a way through when `WebFetch`/curl
get blocked (403s, anti-bot, Cloudflare Turnstile). Two tools, tried in order:

| Tool | What | When |
|---|---|---|
| `browser_fetch` | a **fresh, disposable, headless browser** per call (Playwright) — `engine` picks Chromium (default), Firefox, or WebKit | first resort — a real engine beats a bare HTTP client; a second engine is a second way past anti-bot that keys on Chrome |
| `browser_fetch_persistent` | a **real Chrome the operator started** over the DevTools Protocol — `rung=4` (default) a dedicated profile on `:9222`, `rung=5` their everyday session on `:9223` | only if `browser_fetch` is also blocked — a real, non-headless (and optionally aged) session clears checks a fresh automated browser can't |

Both return `status`/`title`/`url` + rendered text (or `raw_html=True`),
truncated to 80k chars to stay token-considerate.

**Parameters that matter:** `browser_fetch` takes `engine` (`chromium` |
`firefox` | `webkit`, default `chromium`). `browser_fetch_persistent` takes
`rung` (`4` = dedicated profile / `5` = everyday session, default `4`). Both
also take `raw_html` and `wait_ms`.

## The fetch escalation ladder

browser-fetch is rungs 3–5 of how a Claude teammate fetches from the internet.
**Rungs 1–2 cost the same and clear the same walls — pick between them by
request shape; from rung 3 down, step down only when the current rung is
actually blocked** (`../../docs/method/REACH.md`) — each step costs more
(time, tokens, or the operator's attention).

| # | Method | What it is | Isolation | Needs the operator? |
|---|--------|-----------|-----------|---------------------|
| 1 | **WebFetch / WebSearch** | built-in; fetch a known URL (cleaned content) or search to find one | n/a | no |
| 2 | **curl / raw HTTP** | raw bytes — APIs, files, exact headers, or when #1's processing gets in the way (same anti-bot profile as #1: a bare HTTP client) | n/a | no |
| 3 | **`browser_fetch`** | a **completely standalone, disposable browser** the agent launches (headless) — its own process/session, **no** cookies, history, extensions, or downloads shared with the operator's browsing; can't be clicked away or broken by accident. `engine=chromium` (default), `firefox`, or `webkit` | fully isolated | no |
| 4 | **`browser_fetch_persistent rung=4` — dedicated profile** | a **standalone, non-headless** Chrome the operator started on `:9222` with a **dedicated** profile — like #3 but real/visible (some anti-bot blocks headless: #3's Chromium UA still says `HeadlessChrome`), still isolated from everyday browsing | isolated (dedicated profile) | ⚠️ operator starts it |
| 5 | **`browser_fetch_persistent rung=5` — everyday session** | the operator's **own everyday Chrome** — real history, cookies, logged-in sessions; "just another tab as if the operator opened it". Only when the operator **deliberately** exposes that profile on `:9223` | none — the operator's real browser | ⚠️ operator exposes it; may clear a challenge in-window |
| 6 | **ask the operator to paste** | full manual fallback — when even the operator's browser hits a challenge only a human clears | — | ⚠️ fully manual |

**Engines (rung 3 only).** `browser_fetch` runs any of Playwright's three
engines via the `engine` parameter — Chromium (default, real installed Chrome),
Firefox (Gecko), or WebKit (Safari's engine). When a site's anti-bot keys on
Chrome or headless-Chrome specifically, retrying the *same* rung with a different
engine is a cheap second way through before escalating to rung 4. **Rungs 4–5
stay Chrome-only** — see the honest limit below.

**Rung 4 vs rung 5 is now explicit.** The single `browser_fetch_persistent` tool
serves both, and the `rung` parameter makes the choice explicit two ways at once:
the caller passes `rung=4` (default, dedicated profile) or `rung=5` (everyday
session), and each rung maps to a **distinct debug port** the operator binds to
the matching profile — dedicated on `:9222`, everyday on `:9223`. The operator
can run both at once; the agent picks by rung, and an unreachable port yields a
**rung-specific** error. (The tool trusts the operator's port→profile setup — it
can't tell a dedicated from an everyday profile over CDP, so the explicitness
lives in the caller's `rung` and the operator's two-port setup, not a probe.)

**Honest limit — rungs 4/5 are Chrome-only, by protocol.** `browser_fetch_persistent`
connects over the Chrome DevTools Protocol (CDP), which is Chrome-specific;
Playwright's `connect_over_cdp` only speaks CDP. Firefox and WebKit have
different, incompatible remote-debug protocols with no Playwright connect-to-
running equivalent, so the multi-engine choice is **real for rung 3 and not
available for rungs 4/5**. This is a genuine protocol limit, not a stub.

### Credential boundary (non-negotiable)

Across **every** rung: the agent may **ride a session the operator has already
authenticated** (existing cookies / a logged-in tab are fair game). The agent may
**never use the browser's *saved credentials*** — password-manager entries,
autofill, stored logins — to authenticate, nor access those credentials
themselves, **without an explicit grant, which is the principal's alone to
make** (the agent records a grant, never originates one). Using an existing
session is fine; touching the credentials that mint one is the sensitive line.
(This is the operational statement of the credential boundary in
`../../docs/method/REACH.md` — the purpose-of-storage test, ride-not-mint —
which has survived independent review; that doc, not this README, is
canonical.)

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
./setup          # builds the venv (mcp + playwright + Chromium/Firefox/WebKit), prints the registration
```

`setup` runs `playwright install chromium firefox webkit`: Chromium serves rung
3's default and the Chrome-only persistent rungs; Firefox and WebKit are the
alternate `engine` choices for rung 3. These are **engine downloads (a setup
step), not dependency changes** — `requirements.txt`/`constraints.txt` are
unchanged (Playwright already bundles all three engines).

The **code** lives here (versioned, public); the **venv** is a regenerable build
artifact under `~/.cache/atelier/browser-fetch/` — never committed, never in
iCloud. `setup` prints the exact `~/.claude.json` `mcpServers` snippet; Claude
Code picks it up on its next start.

**Intel macOS:** `constraints.txt` pins `cryptography<46` (newer versions dropped
prebuilt wheels for that platform). Needs a Python new enough for the `mcp` SDK
(3.11+; developed on 3.14).

### For `browser_fetch_persistent` — start a real Chrome once per login

**Rung 4 (default) — a dedicated profile on `:9222`:**

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --remote-debugging-port=9222 \
    --user-data-dir="$HOME/.chrome-claude-fetch-profile" \
    --no-first-run --no-default-browser-check
```

The `--user-data-dir` makes this a **dedicated profile** — isolated from
everyday browsing, the safe default.

**Rung 5 (deliberate escalation) — the everyday profile on `:9223`:**

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --remote-debugging-port=9223 \
    --no-first-run --no-default-browser-check
```

Omit the dedicated `--user-data-dir` so Chrome uses your **everyday** profile —
for when only a real logged-in session gets through. This usually means quitting
your normal Chrome first (the debug port can't be added to an already-running
instance). It's a *deliberate* operator choice; the agent won't fall back to
rung 5 on its own, and the **credential boundary above still binds** (ride the
already-authenticated session, never the saved credentials).

Use the binary path directly (`open -a` drops the flags if Chrome is already
running). You can run both ports at once; the agent selects by `rung`. Each debug
port binds to localhost only and has no auth of its own — never expose either on
a network interface.

## Verification

The **non-browser-driving logic is unit-tested** in `test_server.py`: argument
validation (`engine`, `rung`), the rung→port map, the result formatter and
truncation, and the rung-specific "start Chrome like this" hints — 11 tests. Run
them with the venv interpreter (they need `mcp` + `playwright`, and skip cleanly
without them):

```sh
~/.cache/atelier/browser-fetch/venv/bin/python -m unittest \
    instruments/browser-fetch/test_server.py
```

**Driving a real browser is not unit-tested** (CI can't cheaply do it), so it is
verified by live fetch instead. Status for this change:

- `browser_fetch` with `engine=firefox` and `engine=webkit` — **live-verified
  2026-07-12** (session 47): each engine fetched `https://example.com` end-to-end
  through the actual `_launch_engine`/`_load_and_extract` path (200, correct
  title + body) after `playwright install firefox webkit`. (`engine=chromium`
  was proven on adoption.)
- `browser_fetch_persistent rung=4` on `:9222` — proven end-to-end on adoption;
  this change only parameterises the port, covered by the rung→port unit tests.
- `browser_fetch_persistent rung=5` on `:9223` — reachability guard and rung-5
  error path are unit-tested; a live fetch through an **everyday session** on the
  second port is **owed-to-operator** by nature (rung 5 exists only when the
  operator deliberately exposes their everyday Chrome — it can't be self-driven).

The floor scanners still cover `server.py` (leak/secret). Machine- and
person-specific detail was scrubbed before this entered the public repo.

#!/usr/bin/env python3
"""
MCP server exposing browser-based fetch tools, built on the official `mcp` SDK
(FastMCP, stdio transport). It gives a Claude teammate a way through when a
plain HTTP fetch is blocked — a real browser engine, and if needed the
operator's own aged browser session.

Runtime: a Python venv holding `mcp` + `playwright` (see requirements.txt /
constraints.txt), created by `setup`. The MCP client (Claude Code) is
registered to launch this file with that venv's interpreter — `setup` prints
the exact registration snippet.

Portability note: on Intel macOS, pin `cryptography<46` (constraints.txt) —
newer versions stopped shipping prebuilt wheels for that platform and fall back
to a Rust source build that fails without OpenSSL headers. Keep the constraint
when upgrading deps.

Tools:
- `browser_fetch` (ladder rung 3) drives a FRESH, disposable, headless browser
  via Playwright for each call. Defaults to real installed Chrome; the `engine`
  parameter can switch to Firefox (Gecko) or WebKit (Safari's engine), both
  Playwright-bundled. A second engine is a second way past anti-bot that keys on
  Chrome/headless-Chrome specifically. Fine for most sites; some anti-bot
  systems block a fresh automated browser anyway, because it has none of the
  signals — cookies, history, a settled fingerprint — a real visit accumulates.
- `browser_fetch_persistent` (ladder rungs 4 and 5) connects over the Chrome
  DevTools Protocol (CDP) to an ALREADY-RUNNING, real Chrome the operator starts
  separately — not one Playwright launched itself, so it carries none of
  Playwright's automation flags and looks, over repeated use, like an ordinary
  aged browser session. The `rung` parameter makes the dedicated-profile (rung
  4) vs everyday-session (rung 5) choice EXPLICIT — see below.
  Escalation path: try `browser_fetch` first; only reach for
  `browser_fetch_persistent` if that's blocked.

CHROME-ONLY for the persistent rungs (honest limitation). CDP is Chrome's own
protocol, and Playwright's `connect_over_cdp` only speaks it — Firefox and
WebKit have different, incompatible remote-debug protocols that Playwright does
not expose a connect-to-running equivalent for. So the multi-engine choice is
real for rung 3 (`browser_fetch`) and NOT available for rungs 4/5: those stay
Chrome-only. This is a genuine protocol limit, not a stub we can fill later
without a different mechanism.

Explicit rung 4 vs rung 5 (dedicated profile vs everyday session). These two
rungs differ only in WHICH Chrome profile is exposed, so the split is made
explicit two ways at once: the caller passes `rung=4` or `rung=5`, and each rung
maps to a DISTINCT debug port the operator binds to the matching profile:
  - rung 4 → port 9222 → a DEDICATED profile, isolated from everyday browsing
             (the safe default).
  - rung 5 → port 9223 → the operator's EVERYDAY profile — real history and
             logged-in sessions — exposed only as a deliberate operator choice.
The operator's setup binds each port to the right profile; the tool selects the
port by rung and reports a rung-specific error if nothing is listening. (The
tool trusts the operator's port→profile mapping; it cannot itself tell a
dedicated profile from an everyday one over CDP — the explicitness is in the
caller's rung choice and the operator's two-port setup, not a runtime probe.)

One-time setup for the persistent rungs (run once per login session, or make it
a login item). RUNG 4 — a DEDICATED profile on port 9222, bound to localhost:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \\
        --remote-debugging-port=9222 \\
        --user-data-dir="$HOME/.chrome-claude-fetch-profile" \\
        --no-first-run --no-default-browser-check

RUNG 5 — the EVERYDAY profile on port 9223, a deliberate choice for when only a
real logged-in session gets through (the credential boundary still binds: ride
the already-authenticated session, never reach for the browser's SAVED
credentials). Omit the dedicated `--user-data-dir` so Chrome uses the default
profile; this generally means quitting your normal Chrome first, since the debug
port can't be added to an already-running instance:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \\
        --remote-debugging-port=9223 \\
        --no-first-run --no-default-browser-check

(Use the binary path directly — `open -a "Google Chrome" --args ...` silently
ignores the flags if any Chrome is already running.) Leave the Chrome window
open; browser_fetch_persistent connects on demand and does not close it. Both
ports bind to localhost only and have no authentication of their own — never
expose either on a network interface. If nothing is listening on the port for
the requested rung, the tool returns a clear error with the command above.
"""
import asyncio
import urllib.request

from mcp.server.fastmcp import FastMCP
from playwright.async_api import async_playwright

MAX_CHARS = 80_000  # keep tool results token-considerate; truncate beyond this

# Engines available for rung 3 (browser_fetch). chromium uses the real installed
# Chrome (channel="chrome"); firefox/webkit use Playwright's bundled engines —
# install them once with `playwright install firefox webkit` (see setup).
ENGINES = ("chromium", "firefox", "webkit")

# Persistent rungs (browser_fetch_persistent) → the debug port the operator
# binds to the matching profile. localhost only — never expose these ports on a
# network interface; CDP has no authentication of its own.
CDP_HOST = "127.0.0.1"  # leakscan:allow: loopback address, not personal/estate data
CDP_PORTS = {4: 9222, 5: 9223}  # rung 4 = dedicated profile · rung 5 = everyday session

mcp = FastMCP("browser-fetch")


async def _load_and_extract(page, url: str, raw_html: bool, wait_ms: int):
    resp = await page.goto(url, timeout=30_000, wait_until="domcontentloaded")
    if wait_ms:
        await page.wait_for_timeout(wait_ms)
    status = resp.status if resp else None
    title = await page.title()
    body = await page.content() if raw_html else await page.inner_text("body")
    return status, title, body


def _format_result(status, title, url: str, body: str) -> str:
    truncated = len(body) > MAX_CHARS
    if truncated:
        body = body[:MAX_CHARS]
    header = f"status: {status}\ntitle: {title}\nurl: {url}\n"
    if truncated:
        header += f"[truncated to {MAX_CHARS} chars]\n"
    return header + "---\n" + body


async def _launch_engine(p, engine: str):
    """Launch a fresh headless browser for the requested engine (rung 3)."""
    if engine == "chromium":
        # Real installed Chrome — best fidelity, the default path.
        return await p.chromium.launch(channel="chrome", headless=True)
    if engine == "firefox":
        return await p.firefox.launch(headless=True)  # Playwright-bundled Gecko
    if engine == "webkit":
        return await p.webkit.launch(headless=True)  # Playwright-bundled WebKit (Safari's engine)
    raise ValueError(f"unknown engine {engine!r}; choose one of {', '.join(ENGINES)}")


@mcp.tool(
    description=(
        "Load a URL in a fresh, disposable, headless browser (via Playwright) "
        "and return its rendered text or HTML. Use this when a plain HTTP fetch "
        "tool gets blocked (e.g. HTTP 403 from anti-bot protection) — a real "
        "browser engine often gets through where a bare HTTP client doesn't. "
        "engine defaults to 'chromium' (real installed Chrome); pass 'firefox' "
        "(Gecko) or 'webkit' (Safari's engine) to retry with a different engine "
        "when a site's anti-bot keys on Chrome or headless-Chrome specifically. "
        "firefox/webkit must have been installed once via 'playwright install "
        "firefox webkit' (see the server's setup)."
    )
)
async def browser_fetch(
    url: str, raw_html: bool = False, wait_ms: int = 0, engine: str = "chromium"
) -> str:
    if engine not in ENGINES:
        raise ValueError(
            f"unknown engine {engine!r}; choose one of {', '.join(ENGINES)}"
        )
    async with async_playwright() as p:
        browser = await _launch_engine(p, engine)
        try:
            page = await browser.new_page()
            status, title, body = await _load_and_extract(page, url, raw_html, wait_ms)
        finally:
            await browser.close()
    return _format_result(status, title, url, body)


def _cdp_endpoint(port: int) -> str:
    return f"http://{CDP_HOST}:{port}"


def _cdp_endpoint_reachable(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"{_cdp_endpoint(port)}/json/version", timeout=3):
            return True
    except Exception:
        return False


def _persistent_setup_hint(rung: int, port: int) -> str:
    """Rung-specific 'start Chrome like this' guidance for the not-reachable case."""
    if rung == 4:
        return (
            f"No Chrome found listening on {_cdp_endpoint(port)} for rung 4 "
            "(dedicated profile). Start it with:\n"
            '  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" '
            f"--remote-debugging-port={port} "
            '--user-data-dir="$HOME/.chrome-claude-fetch-profile" '
            "--no-first-run --no-default-browser-check\n"
            "then retry. This is a DEDICATED profile — isolated from everyday "
            "browsing, the safe default."
        )
    return (
        f"No Chrome found listening on {_cdp_endpoint(port)} for rung 5 "
        "(everyday session). This rung uses the operator's EVERYDAY Chrome "
        "profile and is a deliberate operator choice — do not fall back to it "
        "on your own. If the operator wants it, they start (usually after "
        "quitting their normal Chrome):\n"
        '  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" '
        f"--remote-debugging-port={port} "
        "--no-first-run --no-default-browser-check\n"
        "The credential boundary still binds: ride the already-authenticated "
        "session, never reach for the browser's saved credentials. If rung 5 "
        "isn't exposed, fall back to asking the operator to paste the content."
    )


@mcp.tool(
    description=(
        "Like browser_fetch, but loads the URL in a real, already-running Chrome "
        "the operator started (connected to via the Chrome DevTools Protocol) "
        "instead of a fresh disposable one. Use this ONLY after browser_fetch "
        "has been tried and was blocked — a real, aged browser session gets past "
        "anti-bot checks (e.g. Cloudflare) that block a brand-new automated "
        "browser. CHROME ONLY: CDP is Chrome-specific, so unlike browser_fetch "
        "there is no engine choice here. The rung parameter makes the profile "
        "choice explicit: rung=4 (default) uses a DEDICATED profile on port 9222 "
        "— isolated from everyday browsing, the safe default; rung=5 uses the "
        "operator's EVERYDAY profile (real logins/history) on port 9223, and is "
        "a deliberate escalation to use only when rung 4 is also blocked and the "
        "operator has exposed it. Requires the operator to have started Chrome "
        "with --remote-debugging-port on the matching port (see the server's "
        "module docstring); if nothing is listening on that rung's port, the "
        "tool returns a rung-specific error telling you so. Credential boundary: "
        "ride the operator's already-authenticated session, never the browser's "
        "SAVED credentials."
    )
)
async def browser_fetch_persistent(
    url: str, raw_html: bool = False, wait_ms: int = 0, rung: int = 4
) -> str:
    if rung not in CDP_PORTS:
        raise ValueError(
            f"unknown rung {rung!r}; choose 4 (dedicated profile) or 5 "
            "(everyday session)"
        )
    port = CDP_PORTS[rung]
    endpoint = _cdp_endpoint(port)
    reachable = await asyncio.to_thread(_cdp_endpoint_reachable, port)
    if not reachable:
        raise RuntimeError(_persistent_setup_hint(rung, port))
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(endpoint)
        # Attach to the existing default context (the running Chrome's own
        # profile/cookies/history) rather than creating an isolated one —
        # that continuity across calls is the entire point of this tool.
        context = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await context.new_page()
        try:
            status, title, body = await _load_and_extract(page, url, raw_html, wait_ms)
        finally:
            # Close only the tab we opened — this is the operator's real,
            # persistent Chrome; closing the browser would kill the whole window.
            await page.close()
    return _format_result(status, title, url, body)


if __name__ == "__main__":
    mcp.run()

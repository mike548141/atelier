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
- `browser_fetch` drives a FRESH, disposable, headless Chrome via Playwright
  for each call. Fine for most sites; some anti-bot systems block it anyway,
  because a brand-new automated browser has none of the signals — cookies,
  history, a settled fingerprint — a real visit accumulates over time.
- `browser_fetch_persistent` connects over the Chrome DevTools Protocol (CDP)
  to an ALREADY-RUNNING, real Chrome that the operator starts separately — not
  one Playwright launched itself, so it carries none of Playwright's automation
  flags and looks, over repeated use, like an ordinary aged browser session.
  Escalation path: try `browser_fetch` first; only reach for
  `browser_fetch_persistent` if that's blocked.

One-time setup for browser_fetch_persistent (run once per login session, or
make it a login item): start Chrome with a DEDICATED profile (never the
operator's everyday profile — this must never carry personal logins/cookies)
and a debugging port bound to localhost only:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \\
        --remote-debugging-port=9222 \\
        --user-data-dir="$HOME/.chrome-claude-fetch-profile" \\
        --no-first-run --no-default-browser-check

(Use the binary path directly — `open -a "Google Chrome" --args ...` silently
ignores the flags if any Chrome is already running.) Leave that Chrome window
open. browser_fetch_persistent connects to it on demand and does not close it.
If nothing is listening on the port, the tool returns a clear error with the
command above.
"""
import asyncio
import urllib.request

from mcp.server.fastmcp import FastMCP
from playwright.async_api import async_playwright

MAX_CHARS = 80_000  # keep tool results token-considerate; truncate beyond this
CDP_ENDPOINT = "http://127.0.0.1:9222"  # leakscan:allow: loopback address, not personal/estate data
                                         # localhost only — never expose this port
                                         # on a network interface; the debugging
                                         # protocol has no authentication of its own

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


@mcp.tool(
    description=(
        "Load a URL in a real, installed Google Chrome browser (via Playwright) "
        "and return its rendered text or HTML. Use this when a plain HTTP fetch "
        "tool gets blocked (e.g. HTTP 403 from anti-bot protection) — a real "
        "browser engine often gets through where a bare HTTP client doesn't."
    )
)
async def browser_fetch(url: str, raw_html: bool = False, wait_ms: int = 0) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        try:
            page = await browser.new_page()
            status, title, body = await _load_and_extract(page, url, raw_html, wait_ms)
        finally:
            await browser.close()
    return _format_result(status, title, url, body)


def _cdp_endpoint_reachable() -> bool:
    try:
        with urllib.request.urlopen(f"{CDP_ENDPOINT}/json/version", timeout=3):
            return True
    except Exception:
        return False


@mcp.tool(
    description=(
        "Like browser_fetch, but loads the URL in the operator's own "
        "already-running Chrome (connected to via the Chrome DevTools Protocol) "
        "instead of a fresh disposable one. Use this ONLY after browser_fetch "
        "has been tried and was blocked — this real, aged browser session gets "
        "past anti-bot checks (e.g. Cloudflare) that block a brand-new automated "
        "browser, because it carries none of Playwright's own automation flags "
        "and has genuine cookies/history for sites visited before. Requires the "
        "operator to have started Chrome with --remote-debugging-port=9222 on a "
        "dedicated profile (see this server's module docstring) — if nothing is "
        "listening on that port, this tool returns an error telling you so; fall "
        "back to asking the operator to paste the content directly rather than "
        "any other workaround."
    )
)
async def browser_fetch_persistent(url: str, raw_html: bool = False, wait_ms: int = 0) -> str:
    reachable = await asyncio.to_thread(_cdp_endpoint_reachable)
    if not reachable:
        raise RuntimeError(
            "No Chrome found listening on "
            f"{CDP_ENDPOINT} (checked {CDP_ENDPOINT}/json/version). Start it with:\n"
            '  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" '
            "--remote-debugging-port=9222 "
            '--user-data-dir="$HOME/.chrome-claude-fetch-profile" '
            "--no-first-run --no-default-browser-check\n"
            "then retry. Use a DEDICATED profile — never the operator's everyday "
            "Chrome profile — so this never touches personal logins/cookies."
        )
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(CDP_ENDPOINT)
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

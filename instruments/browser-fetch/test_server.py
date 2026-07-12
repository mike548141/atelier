#!/usr/bin/env python3
"""Unit tests for browser-fetch's non-browser-driving logic.

These cover argument validation, the rung→port map, the result formatter, and
the rung-specific setup hints — everything that does NOT need to drive a real
browser. Driving Chromium/Firefox/WebKit end-to-end (rung 3) and connecting over
CDP to a running Chrome (rungs 4/5) is live-verification-owed and cannot run in
CI, so it is deliberately NOT tested here.

Run with the browser-fetch venv's interpreter (it holds mcp + playwright):
    ~/.cache/atelier/browser-fetch/venv/bin/python -m unittest \\
        instruments/browser-fetch/test_server.py
The whole module skips cleanly if those deps aren't importable, so it never
reds a plain `python3` run that lacks them.
"""
import asyncio
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import server  # requires mcp + playwright (the browser-fetch venv)
    _IMPORT_ERROR = None
except Exception as exc:  # pragma: no cover - environment-dependent
    server = None
    _IMPORT_ERROR = exc


def _run(coro):
    return asyncio.run(coro)


@unittest.skipUnless(server is not None, f"server import failed: {_IMPORT_ERROR}")
class FormatResultTests(unittest.TestCase):
    def test_header_and_body(self):
        out = server._format_result(200, "Title", "http://example.com", "hello")
        self.assertIn("status: 200", out)
        self.assertIn("title: Title", out)
        self.assertIn("url: http://example.com", out)
        self.assertTrue(out.endswith("hello"))
        self.assertNotIn("truncated", out)

    def test_truncation(self):
        body = "x" * (server.MAX_CHARS + 500)
        out = server._format_result(200, "T", "http://x", body)
        self.assertIn(f"[truncated to {server.MAX_CHARS} chars]", out)
        # body portion (after the '---\n' separator) is clipped to MAX_CHARS
        clipped = out.split("---\n", 1)[1]
        self.assertEqual(len(clipped), server.MAX_CHARS)


@unittest.skipUnless(server is not None, f"server import failed: {_IMPORT_ERROR}")
class EngineTests(unittest.TestCase):
    def test_engines_are_the_three_expected(self):
        self.assertEqual(server.ENGINES, ("chromium", "firefox", "webkit"))

    def test_unknown_engine_rejected_before_launch(self):
        with self.assertRaises(ValueError) as ctx:
            _run(server.browser_fetch("http://example.com", engine="opera"))
        self.assertIn("opera", str(ctx.exception))
        for eng in server.ENGINES:
            self.assertIn(eng, str(ctx.exception))

    def test_launch_engine_rejects_unknown(self):
        # _launch_engine also guards, independently of the tool wrapper.
        with self.assertRaises(ValueError):
            _run(server._launch_engine(object(), "netscape"))


@unittest.skipUnless(server is not None, f"server import failed: {_IMPORT_ERROR}")
class PersistentRungTests(unittest.TestCase):
    def test_port_map(self):
        self.assertEqual(server.CDP_PORTS, {4: 9222, 5: 9223})

    def test_endpoint_uses_loopback(self):
        self.assertEqual(server._cdp_endpoint(9222), "http://127.0.0.1:9222")  # leakscan:allow: loopback address, not personal/estate data

    def test_unknown_rung_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            _run(server.browser_fetch_persistent("http://x", rung=9))
        self.assertIn("9", str(ctx.exception))

    def test_rung4_hint_is_dedicated(self):
        hint = server._persistent_setup_hint(4, 9222)
        self.assertIn("9222", hint)
        self.assertIn("DEDICATED", hint)
        self.assertIn("--user-data-dir", hint)  # dedicated profile flag present

    def test_rung5_hint_is_everyday_and_warns(self):
        hint = server._persistent_setup_hint(5, 9223)
        self.assertIn("9223", hint)
        self.assertIn("everyday", hint.lower())
        # rung 5 is a deliberate escalation, and the credential boundary is named.
        self.assertIn("deliberate", hint.lower())
        self.assertIn("credential", hint.lower())
        # rung 5 must NOT carry the dedicated-profile flag.
        self.assertNotIn("--user-data-dir", hint)

    def test_rung5_unreachable_raises_rung5_hint(self):
        # Nothing is listening on 9223 in CI, so this exercises the real
        # not-reachable path and confirms it returns the rung-5 guidance.
        with self.assertRaises(RuntimeError) as ctx:
            _run(server.browser_fetch_persistent("http://x", rung=5))
        self.assertIn("9223", str(ctx.exception))
        self.assertIn("everyday", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()

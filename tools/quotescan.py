#!/usr/bin/env python3
"""quotescan — a commit that touches the principal's prompt carries his words.

WHY (board `160/900` finding QK1's second counsel, the sixth slice of
`320/810`; the principal, 2026-11-09: "all six, warnings at first and then move
to blocking action"). `docs/method/session-open/session-open-prompt.md` is his
text: the run prompt `/atelier:queue-run` reads. A cold pass found that
nothing mechanical read his say-so on a change to it, and that the commit body
it lives in is exactly what a cold reviewer is barred from reading until phase
2. The counsel: a floor check that every commit touching the prompt quotes him.

WHAT IT IS NOT. A check that the quotation is real, or that it is his: that is
`320/080`'s corpus problem. Like `attribscan` it reads the FORM. A double-quoted
span of two or more words in the message, straight or curly, or a `>` blockquote
line. Inline code is removed first, so a backticked example is not a quote.

THE PATHS. `GUARDED` below, a tuple in this file: there is one path today, the
only file the record calls his text. Adding one is a one-line, reviewable edit.

THE PLANES. `--message-file` is the `msg` plane: the paths this commit carries,
read through the index git has set for the hook, so a path-scoped commit sees
only what it named. `--range` is the `ci` plane, over a pushed range; a message
already pushed cannot be fixed, so it only reports. On an amend the hook sees the
index against the tip being amended, so a message-only amend carries no guarded
path, which is what it should read.

THE DATE. Before `QUOTE_WARN_UNTIL` a finding on the message plane is reported
and exits 0; on and after it, it exits 1, unless `--warn`. Compared with the UTC
clock; no flag, environment variable or config key moves it. The date is the
run's choice, not his (`320/810`).

EXEMPTION. A line `quotescan:allow: <reason>` in the message. A bare marker
exempts nothing. A mechanical edit by the tools (a renamed link, a reflow) is
what this is for: name it there.

Measured over atelier's history: 19 commits touch the prompt, 8 carry a quote
(42%) (`320/810`).

Exit codes: 0 nothing blocking · 1 a finding on the message plane on or after
the date · 2 the scan itself is broken.

Stdlib-only, like every sibling.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowmarker  # noqa: E402
import commitmsg  # noqa: E402
import report  # noqa: E402

NAME = "quotescan"
GUARDED = ("docs/method/session-open/session-open-prompt.md",)

# 320/810 slice 6: before this date a finding is reported and exits 0; on and
# after it, it exits 1 unless `--warn`. A run's choice of date, not the
# principal's: four weeks after `NAME_WARN_UNTIL`.
QUOTE_WARN_UNTIL = datetime.date(2027, 5, 31)

ALLOW_MARKER = f"{NAME}:allow"
ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER, sep=allowmarker.SEP_ANY_SPACE,
                                 named_reason=False)

_INLINE_CODE_RX = re.compile(r"`+[^`]*`+")
# Two or more words inside double quotes, straight or curly.
QUOTE_RX = re.compile(r'["“][^"“”\n]*\s[^"“”\n]*["”]')
BLOCKQUOTE_RX = re.compile(r"^\s*>\s*\S", re.MULTILINE)


class ConfigError(RuntimeError):
    """Something the scan needs is unusable; fail closed."""


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def warn_only_today(today: datetime.date | None = None) -> bool:
    """True strictly before `QUOTE_WARN_UNTIL` (UTC). Tests patch `_utc_today`."""
    return (today or _utc_today()) < QUOTE_WARN_UNTIL


def carries_quote(message: str) -> bool:
    text = _INLINE_CODE_RX.sub(" ", message)
    return bool(QUOTE_RX.search(text) or BLOCKQUOTE_RX.search(text))


def guarded_in(paths: list[str]) -> list[str]:
    return sorted(p for p in paths if p in GUARDED)


@dataclass
class Finding:
    where: str  # "this commit", or a short commit id
    paths: list[str]


def scan_message(message: str, paths: list[str]) -> list[Finding]:
    touched = guarded_in(paths)
    if not touched or carries_quote(message) or allowmarker.present(ALLOW_RX, message):
        return []
    return [Finding("this commit", touched)]


def scan_range(root: Path, spec: str) -> list[Finding]:
    findings: list[Finding] = []
    for c in commitmsg.commits(root, spec):
        for f in scan_message(c.message, commitmsg.commit_files(root, c.sha)):
            findings.append(Finding(c.sha[:12], f.paths))
    return findings


def _main(argv: list[str] | None) -> int:
    ap = argparse.ArgumentParser(
        prog=NAME,
        description="A commit touching the principal's prompt carries a "
                    "quotation of him in its message.")
    ap.add_argument("--message-file", default="", metavar="PATH",
                    help="the msg plane: this commit's message, as git hands it to commit-msg")
    ap.add_argument("--range", default="", metavar="SPEC",
                    help="the ci plane: a git log spec, or 'pushed'")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but exit 0 for them")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return report.quiet_selftest(NAME, _selftest)
    if bool(args.message_file) == bool(args.range):
        return report.broken(NAME, "give exactly one of --message-file and --range")
    root = Path(args.root).resolve()
    rc = report.refuse_missing_root(NAME, root, args.root)
    if rc is not None:
        return rc

    note = ""
    if args.message_file:
        mode = "message"
        findings = scan_message(commitmsg.read_message(Path(args.message_file), root),
                                commitmsg.staged_files(root))
    else:
        mode = "range"
        spec, note = (commitmsg.pushed_range(root) if args.range == "pushed"
                      else (args.range, ""))
        findings = scan_range(root, spec)

    gating = mode == "message"
    blocks = gating and bool(findings) and not args.warn and not warn_only_today()
    if args.json:
        print(json.dumps({"clean": not blocks, "mode": mode, "blocking": blocks,
                          "warn": args.warn, "note": note,
                          "findings": [asdict(f) for f in findings],
                          "until": QUOTE_WARN_UNTIL.isoformat()}, indent=2))
    else:
        print(render(findings, blocks, mode, note))
        print(report.advisory_count_line(NAME, 0 if blocks else len(findings)))
        if args.warn and findings and gating:
            print(report.WARN_NOTICE)
    return report.exit_code(blocks)


def render(findings: list[Finding], blocks: bool, mode: str, note: str) -> str:
    until = QUOTE_WARN_UNTIL.isoformat()
    what = "this commit" if mode == "message" else "the pushed range"
    extra = f" ({note})" if note else ""
    if not findings:
        return report.clean_head(NAME, f"no unquoted change to the principal's prompt on {what}.{extra}")
    head = (report.findings_head(NAME, len(findings), "unquoted change(s) to the principal's prompt",
                                 " — commit blocked.")
            if blocks else
            f"⚠ {NAME}: {len(findings)} unquoted change(s) to the principal's prompt on {what} "
            f"(warning; blocking from {until}).")
    lines = [head + extra]
    lines += [f"  {f.where}: {', '.join(f.paths)}" for f in findings[:40]]
    if blocks or mode == "message":
        lines.append("  Quote his words in the message (double quotes or a '>' line), or "
                     f"add a line '{ALLOW_MARKER}: <reason>'.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    return report.guarded_main(NAME, _main, argv, (ConfigError, RuntimeError))


def _selftest() -> int:
    fails: list[str] = []

    def check(name, got, want):
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    p = GUARDED[0]
    check("untouched", scan_message("x\n", ["README.md"]), [])
    check("touched, no quote", len(scan_message("area: x\n", [p])), 1)
    check("touched, double-quoted",
          scan_message('area: x\n\nHe said: "yes, add it"\n', [p]), [])
    check("touched, curly", scan_message('area: x\n\n“yes, add it”\n', [p]), [])
    check("touched, blockquote", scan_message("area: x\n\n> yes, add it\n", [p]), [])
    check("a one-word quote does not count", len(scan_message('area: "x" edit\n', [p])), 1)
    check("inline code does not count",
          len(scan_message('area: x\n\n`"not a quote here"`\n', [p])), 1)
    check("marker", scan_message("area: x\n\nquotescan:allow: a sweep\n", [p]), [])
    check("bare marker", len(scan_message("area: x\n\nquotescan:allow\n", [p])), 1)
    for f in fails:
        print(f"{NAME} selftest FAIL: {f}", file=sys.stderr)
    print(f"{NAME} selftest: {'FAILED' if fails else 'ok'} ({len(fails)} failure(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

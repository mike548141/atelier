#!/usr/bin/env python3
"""quotescan — a commit that touches the principal's prompt, or the agent's
grant of authority, carries his words.

WHY (board `160/900` finding QK1's second counsel, the sixth slice of
`320/810`; the principal, 2026-11-09: "all six, warnings at first and then move
to blocking action"). `docs/method/session-open/session-open-prompt.md` is his
text: the run prompt `/atelier:work-run` reads. A cold pass found that
nothing mechanical read his say-so on a change to it, and that the commit body
it lives in is exactly what a cold reviewer is barred from reading until phase
2. The counsel: a floor check that every commit touching the prompt quotes him.

WHAT IT IS NOT. A check that the quotation is real, or that it is his: that is
`320/080`'s corpus problem. Like `attribscan` it reads the FORM. A double-quoted
span of two or more words in the message, straight or curly, or a `>` blockquote
line. Inline code is removed first, so a backticked example is not a quote.

THE PATHS. `GUARDED` below, a tuple in this file: there is one path today, the
only file the record calls his text. Adding one is a one-line, reviewable edit.

THE AUTHORITY SURFACES (board `115/110`, ADVISORY, NEVER BLOCKING). AUTONOMY.md's
always-confirm floor forbids *widening your own authority: editing this file,
another repo's autonomy block, or a permission allowlist*, and "grants change
only on the owner's explicit, dated words". An agent widening its own grant
passed every check in the registry. The same evidence answers it: his words in
the message. So a commit that changes any of these, with no quotation and no
marker, gets one 🟡 line per surface, on every plane, on every date:

  * `docs/method/AUTONOMY.md`, any change (`AUTONOMY_PATH`);
  * the always-confirm floor itself: the text between `<!-- floor:begin -->`
    and `<!-- floor:end -->` in `docs/method/PROPAGATION.md`, and every stamped
    copy of it (`stamp:begin source=docs/method/PROPAGATION.md region=floor`)
    in a file named `CLAUDE.md`, which is where a child inlines it and where
    the template carries it. The marker grammar is `stampscan`'s, imported; an
    edit elsewhere in either file is not a finding;
  * the `permissions` key of a `.claude/settings*.json` at any depth, compared
    parsed; an edit to any other key is not a finding.

Why never blocking: the principal edits these files himself, and a commit that
records his grant is the act the doctrine wants. A gate there would teach the
marker, not the quote. Why here and not a sibling: the evidence (a quotation in
the message), the planes, the marker and the reader are this check's already;
only the surfaces and the severity differ, so they are a second path set here,
not a twenty-first scanner on every commit.

WHAT THE AUTHORITY SLICE CANNOT SEE. A floor copy with no stamp, a copy in a
file not named `CLAUDE.md`, a child's autonomy block outside the floor stamp,
a widening through any settings key other than `permissions` (a hook, an MCP
server switch), and a settings file git does not carry (`settings.local.json`
is usually ignored). It reads the form of a quote and cannot tell whose words
they are, as above.

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
The authority surfaces, over atelier's 2,465 commits on 2026-11-16: 47 change
one, 21 carry a quote or a marker (`115/110`).

Exit codes: 0 nothing blocking (an authority finding never blocks) · 1 a prompt
finding on the message plane on or after the date · 2 the scan itself is broken.

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
import stampscan  # noqa: E402

NAME = "quotescan"
GUARDED = ("docs/method/session-open/session-open-prompt.md",)

# 115/110: the authority surfaces. A finding on any of them is advisory on every
# plane and every date; `QUOTE_WARN_UNTIL` never reaches them.
AUTONOMY_PATH = "docs/method/AUTONOMY.md"
FLOOR_SOURCE = stampscan.FLOOR_SOURCE
FLOOR_REGION = stampscan.FLOOR_REGION
FLOOR_COPY_NAME = "CLAUDE.md"
SETTINGS_RX = re.compile(r"(?:^|/)\.claude/settings[^/]*\.json$")

PROMPT = "prompt"
AUTHORITY = "authority"
SURFACE_AUTONOMY = "the autonomy grant"
SURFACE_FLOOR = "the always-confirm floor"
SURFACE_PERMISSIONS = "a permission allowlist"

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


# A reader hands back one side of a path: `read(path, "old")` is the content
# before this commit, `read(path, "new")` after it, None where the path does not
# exist on that side. The two planes each build one (`_index_reader`,
# `_commit_reader`); the selftest passes a dict.


def floor_parts(path: str, text: str | None) -> tuple:
    """The always-confirm floor as `path` carries it: the canonical region in
    PROPAGATION.md, and every stamped copy of it, in order. Empty when the file
    holds neither, which is also what a missing file gives. A broken marker
    drops its block, so breaking a stamp reads as a change to the floor."""
    if text is None:
        return ()
    parts: list[tuple] = []
    if path == FLOOR_SOURCE:
        region = stampscan.extract_region(text, FLOOR_REGION)
        if region is not None:
            parts.append(("region", tuple(region)))
    blocks, _malformed = stampscan.find_stamp_blocks(path, text)
    parts += [("stamp", tuple(b.payload)) for b in blocks
              if (b.source, b.region) == (FLOOR_SOURCE, FLOOR_REGION)]
    return tuple(parts)


_UNPARSEABLE = object()


def permissions_of(text: str | None):
    """The `permissions` value of a settings file, parsed; None when the file is
    absent or has none. A file that does not parse is its own value, so a
    broken edit reads as a change rather than as nothing."""
    if text is None:
        return None
    try:
        doc = json.loads(text)
    except ValueError:
        return (_UNPARSEABLE, text)
    return doc.get("permissions") if isinstance(doc, dict) else (_UNPARSEABLE, text)


def authority_in(paths: list[str], read) -> list[tuple[str, str]]:
    """(path, surface) for each authority surface this change touches."""
    hits: list[tuple[str, str]] = []
    for p in sorted(paths):
        if p == AUTONOMY_PATH:
            hits.append((p, SURFACE_AUTONOMY))
        elif p == FLOOR_SOURCE or p.rsplit("/", 1)[-1] == FLOOR_COPY_NAME:
            old, new = floor_parts(p, read(p, "old")), floor_parts(p, read(p, "new"))
            if old != new:
                hits.append((p, SURFACE_FLOOR))
        elif SETTINGS_RX.search(p):
            if permissions_of(read(p, "old")) != permissions_of(read(p, "new")):
                hits.append((p, SURFACE_PERMISSIONS))
    return hits


@dataclass
class Finding:
    where: str  # "this commit", or a short commit id
    paths: list[str]
    kind: str = PROMPT   # PROMPT may block on its date; AUTHORITY never does
    surface: str = ""    # for AUTHORITY, which surface; "" for PROMPT


def scan_message(message: str, paths: list[str], read=None) -> list[Finding]:
    """Findings for one commit. `read` is needed for the floor and settings
    surfaces; without one only the path-level surfaces are judged."""
    if carries_quote(message) or allowmarker.present(ALLOW_RX, message):
        return []
    findings: list[Finding] = []
    touched = guarded_in(paths)
    if touched:
        findings.append(Finding("this commit", touched))
    if read is None:
        read = lambda _p, _side: None  # noqa: E731 - nothing to compare
    findings += [Finding("this commit", [p], AUTHORITY, surface)
                 for p, surface in authority_in(paths, read)]
    return findings


def _index_reader(root: Path):
    """The message plane: HEAD against the index git set for the hook."""
    def read(path: str, side: str) -> str | None:
        if side == "old":
            # An unborn branch has no HEAD, and no `HEAD:<path>` either.
            return commitmsg.show(root, f"HEAD:{path}")
        return commitmsg.show(root, f":{path}")
    return read


def _commit_reader(root: Path, sha: str):
    """The ci plane: one commit against its first parent (none for a root)."""
    def read(path: str, side: str) -> str | None:
        # Nothing is read unless a path names a surface: a root commit has no
        # `<sha>^`, so its old side is None like any missing path.
        return commitmsg.show(root, f"{sha}^:{path}" if side == "old" else f"{sha}:{path}")
    return read


def scan_range(root: Path, spec: str) -> list[Finding]:
    findings: list[Finding] = []
    for c in commitmsg.commits(root, spec):
        for f in scan_message(c.message, commitmsg.commit_files(root, c.sha),
                              _commit_reader(root, c.sha)):
            findings.append(Finding(c.sha[:12], f.paths, f.kind, f.surface))
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
                                commitmsg.staged_files(root), _index_reader(root))
    else:
        mode = "range"
        spec, note = (commitmsg.pushed_range(root) if args.range == "pushed"
                      else (args.range, ""))
        findings = scan_range(root, spec)

    gating = mode == "message"
    prompt = [f for f in findings if f.kind == PROMPT]
    blocks = gating and bool(prompt) and not args.warn and not warn_only_today()
    advisories = len(findings) - (len(prompt) if blocks else 0)
    if args.json:
        print(json.dumps({"clean": not blocks, "mode": mode, "blocking": blocks,
                          "warn": args.warn, "note": note,
                          "advisory": advisories,
                          "findings": [asdict(f) for f in findings],
                          "until": QUOTE_WARN_UNTIL.isoformat()}, indent=2))
    else:
        print(render(findings, blocks, mode, note))
        print(report.advisory_count_line(NAME, advisories))
        if args.warn and prompt and gating:
            print(report.WARN_NOTICE)
    return report.exit_code(blocks)


def render(findings: list[Finding], blocks: bool, mode: str, note: str) -> str:
    until = QUOTE_WARN_UNTIL.isoformat()
    what = "this commit" if mode == "message" else "the pushed range"
    extra = f" ({note})" if note else ""
    if not findings:
        return report.clean_head(
            NAME, f"no unquoted change to the principal's prompt or to the "
                  f"authority grant on {what}.{extra}")
    prompt = [f for f in findings if f.kind == PROMPT]
    authority = [f for f in findings if f.kind == AUTHORITY]
    lines: list[str] = []
    if prompt:
        head = (report.findings_head(NAME, len(prompt), "unquoted change(s) to the principal's prompt",
                                     " — commit blocked.")
                if blocks else
                f"⚠ {NAME}: {len(prompt)} unquoted change(s) to the principal's prompt on {what} "
                f"(warning; blocking from {until}).")
        lines.append(head + extra)
        lines += [f"  {f.where}: {', '.join(f.paths)}" for f in prompt[:40]]
        if blocks or mode == "message":
            lines.append("  Quote his words in the message (double quotes or a '>' line), or "
                         f"add a line '{ALLOW_MARKER}: <reason>'.")
    for f in authority[:40]:
        at = "" if mode == "message" else f"{f.where} "
        lines.append(f"🟡 {NAME}: {at}{', '.join(f.paths)} changes {f.surface}, and the "
                     "message quotes no one (advisory, never blocks)." + extra)
    if len(authority) > 40:
        lines.append(f"  {report.cap_part(len(authority) - 40, 40)}")
    if authority:
        lines.append(
            "  Authority widens only on the principal's explicit, dated words "
            "(AUTONOMY.md, Always confirm): quote them in the commit body "
            f"(double quotes or a '>' line), or add a line '{ALLOW_MARKER}: <reason>'."
            if mode == "message" else
            "  A pushed message cannot be changed now: a person reads these diffs "
            "against the principal's dated words.")
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

    # 115/110: the authority surfaces, judged from both sides of the change.
    def reader(sides):
        return lambda path, side: sides.get((path, side))

    def kinds(fs):
        return [(f.kind, f.surface, f.paths) for f in fs]

    a = AUTONOMY_PATH
    check("autonomy edit, no quote", kinds(scan_message("area: x\n", [a])),
          [(AUTHORITY, SURFACE_AUTONOMY, [a])])
    check("autonomy edit, quoted", scan_message('area: x\n\n"grant it now"\n', [a]), [])
    floor_old = "x\n<!-- floor:begin -->\nconfirm first\n<!-- floor:end -->\ny\n"
    floor_out = floor_old.replace("y\n", "z\n")
    floor_in = floor_old.replace("confirm first", "proceed")
    check("floor region edited",
          kinds(scan_message("area: x\n", [FLOOR_SOURCE], reader(
              {(FLOOR_SOURCE, "old"): floor_old, (FLOOR_SOURCE, "new"): floor_in}))),
          [(AUTHORITY, SURFACE_FLOOR, [FLOOR_SOURCE])])
    check("edit outside the floor region",
          scan_message("area: x\n", [FLOOR_SOURCE], reader(
              {(FLOOR_SOURCE, "old"): floor_old, (FLOOR_SOURCE, "new"): floor_out})), [])
    stamp = ("<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n"
             "confirm first\n<!-- stamp:end -->\n")
    check("stamped copy edited",
          kinds(scan_message("area: x\n", ["CLAUDE.md"], reader(
              {("CLAUDE.md", "old"): stamp,
               ("CLAUDE.md", "new"): stamp.replace("confirm first", "proceed")}))),
          [(AUTHORITY, SURFACE_FLOOR, ["CLAUDE.md"])])
    check("CLAUDE.md with no stamp",
          scan_message("area: x\n", ["CLAUDE.md"], reader(
              {("CLAUDE.md", "old"): "a\n", ("CLAUDE.md", "new"): "b\n"})), [])
    sp = ".claude/settings.json"
    check("allowlist widened",
          kinds(scan_message("area: x\n", [sp], reader(
              {(sp, "old"): '{"permissions": {"allow": []}}',
               (sp, "new"): '{"permissions": {"allow": ["Bash"]}}'}))),
          [(AUTHORITY, SURFACE_PERMISSIONS, [sp])])
    check("another settings key",
          scan_message("area: x\n", [sp], reader(
              {(sp, "old"): '{"model": "a", "permissions": {}}',
               (sp, "new"): '{"model": "b", "permissions": {}}'})), [])
    check("a missing file has no surface", authority_in(["CLAUDE.md"], reader({})), [])
    for f in fails:
        print(f"{NAME} selftest FAIL: {f}", file=sys.stderr)
    print(f"{NAME} selftest: {'FAILED' if fails else 'ok'} ({len(fails)} failure(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

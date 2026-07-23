#!/usr/bin/env python3
"""datescan — the mechanical check for absolute-UTC dating discipline in records.

The rule (2026-07-22 invariant-candidates review, seam S3): a dated record
states ISO-8601 absolute dates stamped from `date -u`; it never carries a
relative-time word ("today", "yesterday", "last week") whose meaning drifts
with the reader's "now"; and a dated maintenance edit carries its date. The
house has already paid for a real miss of this class — a standing correction
that cost a five-file sweep when a record was stamped from local NZ time
(a day ahead of UTC in the evening) instead of `date -u`. A rule enforced by
intent alone fails the next tired session the same way; this is the machine
that catches the shape of the mistake before it lands.

FIRST-OF-KIND, WIRED ADVISORY-ONLY (don't-stack). This scanner has not yet
earned an independent review, so it is wired into CI in `--warn` mode only —
it reports, it never gates — and it is deliberately NOT in the blocking
pre-commit hook. Do not add it there until it has been reviewed.

Two independent checks, both over `docs/**` Markdown by default:

  * RELATIVE-TIME-WORD DENYLIST — a fixed set of English words/phrases whose
    meaning is relative to the moment of reading, not an absolute point in
    time ("today", "yesterday", "tomorrow", "last week", "next month", …).
    Any hit outside an exemption is flagged: the fix is either an ISO-8601
    date stamped from `date -u`, or the sentence doesn't need dating at all.

  * ISO/UTC SHAPE CHECK — two sub-checks over date-*looking* text:
      - a non-ISO absolute date (`23/07/2026`, `23 July 2026`, `July 23, 2026`)
        is flagged as `non-iso-date` — the shape is unambiguous but not the
        house format (RECORD.md, CONVENTIONS.md: `YYYY-MM-DD`).
      - an ISO-*shaped* date (`\\d{4}-\\d{2}-\\d{2}`) that is not a real
        calendar date (`2026-13-40`) is flagged as `invalid-iso-date` — the
        shape is right but the value is impossible, a stronger signal than a
        typo elsewhere: something was hand-typed, not machine-stamped.

EXEMPTIONS — deliberately generous, because a false positive here costs a
comment, but a noisy scanner trains itself away (the house's own standing
preference: under-flag with clear exemptions over being noisy). Three layers,
same shape as the sibling scanners:

  * QUOTED EXTERNAL TEXT. A fenced (``` ```) code block is skipped whole,
    matching linkscan/sizescan. A blockquoted line (`>` at the start, after
    leading whitespace) is skipped whole — a quoted external source's own
    words are not this repo's dating claim. An inline `` `code span` `` is
    blanked before either check runs (linkscan's `_strip_inline_code`), so a
    literal `` `today` `` in a code example never fires.

  * PROSE *ABOUT* RELATIVE TIME — the hard exemption, because "this rule bans
    the word today" and "the meeting is today" are structurally identical to
    a regex. The only mechanically-honest signal available is USE vs MENTION
    by punctuation: a relative-time word immediately flanked by a matching
    pair of quote marks (`"today"`, `'yesterday'`, curly “last week”) is
    treated as a MENTION (the word itself is the topic) and exempted. This is
    exactly the shape the S3 rule's own worked examples use. It is a narrow,
    honest heuristic, not a parser: prose that discusses relative time WITHOUT
    quoting the word ("the meaning of yesterday drifts by design") still
    false-positives, and is meant to be closed with a `datescan:allow`.

  * THE ALLOW MARKER / IGNORE FILE. A line carrying `datescan:allow: <reason>`
    anywhere is exempt from every check on that line (mirrors leakscan/
    linkscan). A glob in `.datescanignore` at the scan root exempts a path
    wholesale (mirrors every sibling scanner's ignore file).

STATED RESIDUAL, HONESTLY (do not round this to "solved"):

  * The rule's third clause — "a dated maintenance edit carries its date" —
    is NOT mechanically checked here. Naming "this line is a maintenance
    edit that needed a date and didn't get one" requires knowing the edit's
    *intent*, which a text scanner cannot see; guessing would make this the
    kind of noisy tool the house has already rejected once (sizescan's
    prose-cold-content residual is the same shape). That clause stays
    caught at review, never measured.
  * The quote-flanked MENTION heuristic is punctuation-shaped, not
    semantic — unquoted prose *about* relative time still false-positives
    (see above), and a *use* that happens to sit inside quotation marks for
    an unrelated reason (a quoted sentence that itself says "we'll ship
    tomorrow") would wrongly exempt. Both directions are accepted trade-offs,
    not blind spots — they're the reason this scanner ships advisory-only
    until reviewed.
  * The non-ISO date patterns are common English/NZ shapes (slash-dates,
    "23 July 2026", "July 23, 2026") — not exhaustive of every locale's date
    grammar. A three-numeral slash requirement (`DD/MM/YYYY`, not `DD/MM`)
    keeps ordinary fractions ("3/4 of the work") from false-firing.
  * Only `docs/**` Markdown is scanned by default (dated records live there);
    code comments, commit messages, and non-Markdown prose are out of scope.

Exit codes (fail-safe — anything but a clean scan is non-zero, UNLESS --warn):
  0  clean; or --warn was given (advisory rollout — never blocks)
  1  findings, and --warn was NOT given
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can
run it with the system python3 and no install — and CI needs nothing but
Python.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

# A line carrying this marker is intentionally exempt from every check on that
# line. Keep the reason on the same line so the exemption is self-documenting
# and greppable, same contract as the sibling scanners.
ALLOW_MARKER = "datescan:allow"

# Only these extensions are scanned — dated records are Markdown prose, not
# code or config. Matches linkscan's MARKDOWN_SUFFIXES.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

# Paths never worth walking. Hardcode-skip ONLY names that are never
# human-authored prose — VCS, dependency, and tool-cache dirs (matches the
# sibling scanners; see linkscan.py's header for why `build`/`dist` are
# deliberately absent).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# The relative-time denylist. Deliberately a fixed, modest set of unambiguous
# relative-time words/phrases — not every possible hedge ("recently",
# "currently", "soon" are excluded: their relation to a specific moving
# anchor date is weaker, and the house explicitly prefers under-flagging with
# clear exemptions over a noisy scanner that trains itself away. Multi-word
# phrases are matched as literal word sequences; sorted longest-first so a
# longer phrase wins the alternation over a shorter prefix (not load-bearing
# here since none is a prefix of another, but keeps the invariant honest).
RELATIVE_TIME_TERMS = sorted([
    "today", "tonight", "tomorrow", "yesterday",
    "last night", "last week", "last month", "last year",
    "next week", "next month", "next year",
    "this week", "this month", "this year",
    "the other day", "a few days ago", "a few weeks ago", "a few months ago",
], key=len, reverse=True)

RELATIVE_TIME_RX = re.compile(
    r"\b(?:" + "|".join(re.escape(t) for t in RELATIVE_TIME_TERMS) + r")\b",
    re.IGNORECASE)

# Non-ISO absolute-date shapes. A three-numeral slash date requires TWO
# slashes (`DD/MM/YYYY`), so an ordinary fraction ("3/4 of the work") never
# matches — only one slash there.
_MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
          r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|"
          r"Nov(?:ember)?|Dec(?:ember)?)")

NON_ISO_PATTERNS: list[tuple[str, "re.Pattern[str]"]] = [
    ("slash-date", re.compile(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b")),
    ("month-day-year", re.compile(
        rf"\b{_MONTH}\.?\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}}\b", re.IGNORECASE)),
    ("day-month-year", re.compile(
        rf"\b\d{{1,2}}(?:st|nd|rd|th)?\s+(?:of\s+)?{_MONTH}\.?,?\s+\d{{4}}\b",
        re.IGNORECASE)),
]

# An ISO-8601-SHAPED date. Digits-only, so a template placeholder like the
# literal text `YYYY-MM-DD` never matches (no digits to capture).
ISO_DATE_RX = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")

# Quote-mark pairs used for the USE-vs-MENTION heuristic: a relative-time word
# immediately flanked by a matching pair is treated as a MENTION (prose about
# the word) and exempted — the exact shape the S3 rule's own worked examples
# use ('no relative-time words ("today", "yesterday", "last week")').
_QUOTE_PAIRS = {'"': '"', "'": "'", "“": "”", "‘": "’"}

_FENCE = re.compile(r"^(`{3,}|~{3,})")


@dataclass
class Finding:
    path: str          # the flagged Markdown file (repo-relative)
    line: int
    kind: str          # "relative-time-word" | "non-iso-date" | "invalid-iso-date"
    match: str          # the matched text, as written
    detail: str        # human hint at the fix


def _content_lines(text: str):
    """Yield (lineno, line) for lines outside fenced code blocks — quoted
    external text (a pasted log, an example doc) is not this repo's own
    dating claim. Fence pairing matches linkscan's _content_lines exactly:
    a fence closes only on a run of the same character at least as long as
    the opener, with no trailing info string."""
    in_fence = False
    fence_char = ""
    fence_len = 0
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        m = _FENCE.match(stripped)
        if in_fence:
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len \
                    and stripped.rstrip() == m.group(1):
                in_fence = False
            continue
        if m:
            in_fence = True
            fence_char = m.group(1)[0]
            fence_len = len(m.group(1))
            continue
        yield lineno, line


def _is_blockquote(line: str) -> bool:
    return line.lstrip().startswith(">")


def _strip_inline_code(line: str) -> str:
    """Blank out inline `code spans` so a link-shaped/date-shaped example
    inside them isn't read as a live claim. Identical to linkscan's helper —
    backtick runs must match in length (CommonMark)."""
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == "`":
            j = i
            while j < n and line[j] == "`":
                j += 1
            ticks = line[i:j]
            close = line.find(ticks, j)
            if close != -1 and line[close:close + len(ticks)] == ticks \
                    and (close + len(ticks) >= n or line[close + len(ticks)] != "`"):
                out.append(" " * (close + len(ticks) - i))
                i = close + len(ticks)
                continue
        out.append(line[i])
        i += 1
    return "".join(out)


def _is_quoted_mention(line: str, start: int, end: int) -> bool:
    """USE-vs-MENTION by punctuation: True if the match is immediately flanked
    by a matching pair of quote marks — the heuristic for 'prose about
    relative time' (see module docstring for its honest limits)."""
    before = line[start - 1] if start > 0 else ""
    after = line[end] if end < len(line) else ""
    return before in _QUOTE_PAIRS and after == _QUOTE_PAIRS[before]


def scan_text(path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for lineno, raw_line in _content_lines(text):
        if ALLOW_MARKER in raw_line:
            continue
        if _is_blockquote(raw_line):
            continue
        line = _strip_inline_code(raw_line)

        for m in RELATIVE_TIME_RX.finditer(line):
            if _is_quoted_mention(line, m.start(), m.end()):
                continue
            findings.append(Finding(
                path, lineno, "relative-time-word", m.group(0),
                "relative to the reader's 'now', not an absolute date — replace "
                "with an ISO-8601 date stamped from `date -u`"))

        for kind, rx in NON_ISO_PATTERNS:
            for m in rx.finditer(line):
                findings.append(Finding(
                    path, lineno, "non-iso-date", m.group(0),
                    f"not ISO-8601 ({kind}) — write YYYY-MM-DD"))

        for m in ISO_DATE_RX.finditer(line):
            y, mo, d = (int(g) for g in m.groups())
            try:
                date(y, mo, d)
            except ValueError:
                findings.append(Finding(
                    path, lineno, "invalid-iso-date", m.group(0),
                    "ISO-8601-shaped but not a real calendar date"))
    return findings


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".datescanignore"
    if not f.exists():
        return []
    globs: list[str] = []
    for raw in f.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            globs.append(line)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def iter_markdown(paths: list[Path], root: Path, globs: list[str]):
    for base in paths:
        if base.is_file():
            candidates = [base]
        else:
            candidates = [p for p in base.rglob("*")
                          if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in candidates:
            if p.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            if _ignored(_rel(p, root), globs):
                continue
            yield p


def scan_paths(paths: list[Path], root: Path) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text(_rel(md, root), text))
    return findings


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return "✓ datescan clean — no relative-time words or non-ISO dates found."
    lines = [f"✗ datescan: {len(findings)} finding(s)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.match!r} → {f.detail}")
    lines.append("\n  A real dating slip: fix the word/date (stamp from `date -u`, ISO-8601).")
    lines.append(f"  A deliberate exemption: append '<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .datescanignore.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="datescan",
        description="Check docs/** for relative-time words and non-ISO-8601 dates "
                    "(absolute-UTC dating discipline).")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: <root>/docs if present, "
                         "else the whole root)")
    ap.add_argument("--root", default=".",
                    help="repo root for .datescanignore and relative paths")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but always exit 0 (advisory / "
                         "warn-first rollout — this scanner is first-of-kind "
                         "and not yet reviewed; it must not gate)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"datescan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    if args.paths:
        targets = [Path(p) for p in args.paths]
    else:
        docs = root / "docs"
        targets = [docs] if docs.is_dir() else [root]

    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"datescan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    try:
        findings = scan_paths(targets, root)
    except OSError as e:
        print(f"datescan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "warn": args.warn,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings))
        if findings and args.warn:
            print("\n  (--warn: advisory only — not blocking this build.)")

    if args.warn:
        return 0
    return 1 if findings else 0


def _selftest() -> int:
    """Minimal smoke test so `datescan --selftest` proves the engine on any
    box, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="datescan-self-"))
    (tmp / "docs").mkdir()
    (tmp / "docs" / "note.md").write_text(
        "# Note\n\n"
        "Landed today after the change last week.\n"                    # 2 hits
        "Stamped 2026-07-23 correctly.\n"                                 # clean ISO
        "Filed on 23/07/2026 by hand.\n"                                  # non-iso slash
        "Filed on July 23, 2026 by hand.\n"                               # non-iso month-day-year
        "Bogus date 2026-13-40 here.\n"                                    # invalid iso
        "The rule bans relative-time words like \"today\" and \"yesterday\".\n"  # quoted mentions, exempt
        "`tomorrow` is just an example in code.\n"                        # code span, exempt
        "> quoted external text says it happened yesterday.\n"           # blockquote, exempt
        "```\nshipped tomorrow in this fenced block\n```\n"               # fenced, exempt
        "reduced scope by 3/4 of the work.\n"                             # fraction, not a date
        "allowed today  <!-- datescan:allow: selftest fixture -->\n"     # allow marker, exempt
    )
    findings = scan_paths([tmp / "docs"], tmp)
    kinds = sorted((f.kind, f.match.lower()) for f in findings)
    expected = sorted([
        ("relative-time-word", "today"),
        ("relative-time-word", "last week"),
        ("non-iso-date", "23/07/2026"),
        ("non-iso-date", "july 23, 2026"),
        ("invalid-iso-date", "2026-13-40"),
    ])
    ok = kinds == expected
    if not ok:
        print(f"FAIL: got {kinds}, expected {expected}")

    # main() plumbing: --warn always exits 0 even with findings; without it,
    # findings exit 1 and a clean scan exits 0.
    if main(["--warn", "--root", str(tmp), str(tmp / "docs")]) != 0:
        print("FAIL: --warn should always exit 0")
        ok = False
    if main(["--root", str(tmp), str(tmp / "docs")]) != 1:
        print("FAIL: findings without --warn should exit 1")
        ok = False
    clean = tmp / "clean"
    clean.mkdir()
    (clean / "ok.md").write_text("# OK\n\nStamped 2026-07-23, nothing relative here.\n")
    if main(["--root", str(tmp), str(clean)]) != 0:
        print("FAIL: a clean scan should exit 0")
        ok = False

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

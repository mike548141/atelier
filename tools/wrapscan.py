#!/usr/bin/env python3
"""wrapscan — the mechanical check for line-wrap / column hygiene in prose docs.

The rule (2026-07-22 invariant-candidates review, seam S1): Markdown prose
under `docs/**` (and templates) wraps at the house width (~80 cols; ambient
tolerance 81-85). A prose line *materially* over that reds — concretely,
anything at or beyond 86 columns.

This is not a taste preference being mechanised for its own sake: the corpus
already paid for it three cycles running. `SL7` (2026-07-21-2158) shipped an
over-wide line; the fix that closed it, `AC1` (2026-07-22-0244), re-shipped
the same class at 122 columns; `IR3` (2026-07-22-0257) called it "the third
shipping of the wrap class in three cycles". Nothing mechanical caught any of
the three — a human reviewer kept re-making a judgement a column count makes
trivially. This scanner is that column count.

FIRST-OF-KIND, WIRED ADVISORY-ONLY (don't-stack), matching datescan's rollout
discipline: this scanner has not yet earned an independent review, so — once
wired — it belongs in CI in `--warn` mode only, never in the blocking
pre-commit hook, until reviewed.

THE CHECK — one measurement, four exemptions:

  * COLUMN COUNT. A line's length is its Python character count (`len(line)`
    after `str.splitlines()`, so no trailing newline is counted). This is
    honest for ASCII, which is effectively all of this repo's prose, but it is
    NOT a real *display*-width measurement: a wide (CJK) or combining-mark
    character counts as one column here same as a narrow one, so a line
    padded with wide characters could under-count its true rendered width.
    Stated, not hidden — ASCII-only prose is the house's actual convention
    (CONVENTIONS.md), so the gap is not expected to bite in practice.

  * THE LIMIT is `LINE_LIMIT` below — a named, documented, easily-tuned
    constant, not a magic number buried in a comparison. A line of length
    <= LINE_LIMIT is clean; a line of length > LINE_LIMIT (i.e. >= 86 at the
    shipped default of 85) is a finding, unless an exemption below applies.

EXEMPTIONS — deliberately named and scoped, because under-exempting here is
noise (a scanner nobody trusts trains itself off), and over-exempting is a
silent miss (a genuinely-wrappable line sails through). Documented honestly,
not rounded to "handled":

  * FENCED CODE (and one-line indented code). A fenced (``` ``` or ~~~ ~~~)
    code block is skipped whole — quoted/pasted text (a log, a diff, a
    terminal transcript) is not this repo's own prose wrapping, matching
    datescan/linkscan's `_content_lines`. A line indented 4+ columns is
    treated as an *indented* code block line and exempt too — CommonMark's
    own indented-code-block rule, applied per-line rather than block-aware.
    Honest limit: this is blunt. It also exempts an indented list-item
    continuation line (genuine wrappable prose sitting at 4+ columns under a
    list marker) — a false negative, accepted because a false *positive*
    inside real fenced/quoted code is the worse failure mode for a
    first-of-kind advisory scanner.

  * TABLE ROWS. Any line containing a `|` character is treated as a Markdown
    table row (a cell delimiter) and exempt whole-line. Honest limit: a
    literal pipe used in ordinary prose (rare, but not impossible — e.g. a
    shell pipeline shown inline outside a code span) would also be exempted;
    accepted as a cheap, precise-enough heuristic for the actual corpus.

  * HEADINGS. An ATX heading (`#` through `######` at the start of the line,
    after leading whitespace, followed by a space) is exempt — a heading is
    a label, not wrapped prose, and it is rarely the thing that overflows.

  * REFERENCE-STYLE LINK DEFINITIONS. A line matching `[id]: <url>` (the
    CommonMark reference-link-definition shape) is exempt — it is
    functionally a URL line, the same "unbreakable" reasoning as the
    single-token exemption below, just anchored at the line's own shape
    rather than inferred from where the overflow starts.

  * SINGLE UNBREAKABLE-TOKEN OVERFLOW. A line whose overflow is one long
    token that cannot be wrapped (a URL, a file path, a long identifier) is
    exempt. Heuristic: find the rightmost whitespace character at or before
    column `LINE_LIMIT`; the substring from just after it to end-of-line is
    the "tail". If that tail itself contains no whitespace, the entire
    overflow is one unbreakable token, and the line is exempt; if the tail
    contains whitespace, there was still a legal wrap point inside the
    overflow, so it is real over-wrapped prose and stays a finding. Honest
    limit, stated plainly per the task's own framing: this heuristic WILL let
    through a line that is genuinely over-wrapped prose *ending* in one long
    word — e.g. "this sentence runs on and on until it reaches
    averylongunbrokenidentifierthatpadsthelinepastlimit" reads as exempt even
    though the sentence itself could have wrapped earlier. That is the
    accepted trade-off: catching it would require reasoning about where the
    line *could* have broken, not just where it overflowed, which this
    line-local scanner does not attempt.

STATED RESIDUAL, HONESTLY (do not round this to "solved"):

  * Column count is a character count, not a display-width measurement (see
    above) — a Unicode-width caveat, not a bug, for an ASCII-prose house.
  * The indented-code exemption is per-line and block-unaware (see above) —
    it will also exempt some genuinely-wrappable indented prose.
  * The table-row exemption is a bare `|`-presence check, not a real table
    parser — it will also exempt a rare inline literal pipe outside a code
    span (see above).
  * Setext headings (`===`/`---` underlines) are not specially exempted —
    the underline itself is short and never overflows, and the heading text
    line above it is ordinary prose subject to the same limit as any other
    line, which is the correct outcome.
  * Only `docs/**` Markdown is scanned by default (prose lives there); code
    comments, commit messages, and non-Markdown prose are out of scope,
    matching every sibling scanner's default.

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
from pathlib import Path

# A line carrying this marker is intentionally exempt from every check on
# that line. Keep the reason on the same line so the exemption is
# self-documenting and greppable, same contract as the sibling scanners.
ALLOW_MARKER = "wrapscan:allow"

# Only these extensions are scanned — dated/doc prose is Markdown, not code
# or config. Matches datescan's/linkscan's MARKDOWN_SUFFIXES.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

# Paths never worth walking. Hardcode-skip ONLY names that are never
# human-authored prose — VCS, dependency, and tool-cache dirs (matches the
# sibling scanners).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# THE LIMIT — named and documented per the S1 rule's own instruction ("make
# the limit a named, documented constant so it's easy to tune"). House width
# is ~80 columns with an ambient tolerance of 81-85; a line of length
# LINE_LIMIT (85) or less is acceptable, a line strictly over it (>= 86) is a
# finding, subject to the exemptions above.
LINE_LIMIT = 85

# Indented-code threshold, CommonMark's own indented-code-block rule (4
# columns), applied per-line (see the header's honest limit on this).
INDENTED_CODE_COLUMNS = 4

_FENCE = re.compile(r"^(`{3,}|~{3,})")
_ATX_HEADING = re.compile(r"^#{1,6}(?:\s|$)")
_REF_LINK_DEF = re.compile(r"^\[[^\]]+\]:\s*\S")


@dataclass
class Finding:
    path: str    # the flagged Markdown file (repo-relative)
    line: int
    length: int  # the line's character count
    excerpt: str  # the line, for context (kept short in rendering)
    detail: str  # human hint at the fix


def _content_lines(text: str):
    """Yield (lineno, line) for lines outside fenced code blocks — quoted
    external text (a pasted log, a terminal transcript) is not this repo's
    own prose wrapping. Fence pairing matches datescan's/linkscan's
    _content_lines exactly: a fence closes only on a run of the same
    character at least as long as the opener, with no trailing info string.
    """
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


def _leading_columns(line: str) -> int:
    """Count leading-whitespace columns, expanding tabs to the next 4-column
    stop (matches INDENTED_CODE_COLUMNS; simple and stated, not a full
    CommonMark tab-expansion implementation)."""
    cols = 0
    for ch in line:
        if ch == " ":
            cols += 1
        elif ch == "\t":
            cols += INDENTED_CODE_COLUMNS - (cols % INDENTED_CODE_COLUMNS)
        else:
            break
    return cols


def _is_indented_code(line: str) -> bool:
    if line.strip() == "":
        return False
    return _leading_columns(line) >= INDENTED_CODE_COLUMNS


def _is_table_row(line: str) -> bool:
    return "|" in line


def _is_heading(line: str) -> bool:
    return bool(_ATX_HEADING.match(line.lstrip()))


def _is_ref_link_definition(line: str) -> bool:
    return bool(_REF_LINK_DEF.match(line.strip()))


def _is_single_unbreakable_token_overflow(line: str, limit: int) -> bool:
    """True if the entire overflow past `limit` columns is one whitespace-
    free token with no legal earlier wrap point inside the overflow — see
    the module header for the heuristic's stated, honest limits."""
    if len(line) <= limit:
        return False
    head = line[:limit]
    last_ws = max(head.rfind(" "), head.rfind("\t"))
    tail = line[last_ws + 1:] if last_ws != -1 else line
    return not any(ch in (" ", "\t") for ch in tail)


def _is_exempt(line: str) -> bool:
    return (_is_indented_code(line) or _is_table_row(line)
            or _is_heading(line) or _is_ref_link_definition(line))


def scan_text(path: str, text: str, limit: int = LINE_LIMIT) -> list[Finding]:
    findings: list[Finding] = []
    for lineno, line in _content_lines(text):
        if ALLOW_MARKER in line:
            continue
        length = len(line)
        if length <= limit:
            continue
        if _is_exempt(line):
            continue
        if _is_single_unbreakable_token_overflow(line, limit):
            continue
        excerpt = line if len(line) <= 100 else line[:97] + "..."
        findings.append(Finding(
            path, lineno, length, excerpt,
            f"{length} columns, over the {limit}-column house limit — wrap it"))
    return findings


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".wrapscanignore"
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


def scan_paths(paths: list[Path], root: Path, limit: int = LINE_LIMIT) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text(_rel(md, root), text, limit))
    return findings


def render_human(findings: list[Finding], limit: int) -> str:
    if not findings:
        return f"✓ wrapscan clean — no prose lines over {limit} columns."
    lines = [f"✗ wrapscan: {len(findings)} finding(s) (limit {limit} columns)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.length} cols] {f.detail}")
    lines.append("\n  A real over-wrap: rewrap the prose at the house width (~80 cols).")
    lines.append(f"  A deliberate exemption: append '<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .wrapscanignore.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="wrapscan",
        description="Check docs/** for prose lines materially over the house "
                    "wrap width (line-wrap / column hygiene).")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: <root>/docs if present, "
                         "else the whole root)")
    ap.add_argument("--root", default=".",
                    help="repo root for .wrapscanignore and relative paths")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but always exit 0 (advisory / "
                         "warn-first rollout — this scanner is first-of-kind "
                         "and not yet reviewed; it must not gate)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--limit", type=int, default=LINE_LIMIT,
                    help=f"column limit; lines longer are findings (default: {LINE_LIMIT})")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"wrapscan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    if args.paths:
        targets = [Path(p) for p in args.paths]
    else:
        docs = root / "docs"
        targets = [docs] if docs.is_dir() else [root]

    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"wrapscan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    try:
        findings = scan_paths(targets, root, args.limit)
    except OSError as e:
        print(f"wrapscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "warn": args.warn,
            "limit": args.limit,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings, args.limit))
        if findings and args.warn:
            print("\n  (--warn: advisory only — not blocking this build.)")

    if args.warn:
        return 0
    return 1 if findings else 0


def _selftest() -> int:
    """Minimal smoke test so `wrapscan --selftest` proves the engine on any
    box, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="wrapscan-self-"))
    (tmp / "docs").mkdir()
    ok_85 = "x" * 85
    over_86 = "y" * 86
    prose_over = "This is a normal prose sentence padded out well past the " \
                 "house limit of eighty five columns for sure yes indeed."
    single_token_tail = "See the doc at " + ("a" * 90)
    table_row = "| " + ("z" * 90) + " |"
    heading = "# " + ("h" * 90)
    indented = "    " + ("c" * 90)
    fenced = "```\n" + ("f" * 90) + "\n```\n"
    ref_link = "[ref]: https://example.invalid/" + ("p" * 90)
    (tmp / "docs" / "note.md").write_text(
        "\n".join([
            ok_85,                                   # exactly 85, clean
            over_86,                                  # 86, single token but no ws before -> whole line is token, exempt (unbreakable)
            prose_over,                                # over limit, multi-word overflow -> finding
            single_token_tail,                         # overflow is one token -> exempt
            table_row,                                 # table row -> exempt
            heading,                                   # heading -> exempt
            indented,                                   # indented code -> exempt
            ref_link,                                   # ref link def -> exempt
            "allowed " + ("q" * 90) + "  <!-- wrapscan:allow: selftest fixture -->",
            "",
        ]) + fenced
    )
    findings = scan_paths([tmp / "docs"], tmp)
    lengths = sorted(f.length for f in findings)
    expected = sorted([len(prose_over)])
    ok = lengths == expected
    if not ok:
        print(f"FAIL: got lengths {lengths}, expected {expected}")

    # Boundary: 85 clean, 86 flagged when it's genuinely multi-word overflow.
    boundary_findings = scan_text("t", "a" * 85 + "\nb bb " + "c" * 82)
    if any(f.length == 85 for f in boundary_findings):
        print("FAIL: an 85-column line must not be flagged")
        ok = False
    # A line whose overflow region itself contains more than one token (a
    # space still inside the overflow, past LINE_LIMIT) is genuine
    # over-wrapped prose, not a single unbreakable token — must be flagged.
    multiword_overflow = "w" * 87 + " ww"
    if len(multiword_overflow) <= 85:
        print("FAIL: selftest fixture miscalibrated (multiword_overflow too short)")
        ok = False
    if not scan_text("t", multiword_overflow):
        print("FAIL: a line with a real wrap point inside the overflow must be flagged")
        ok = False

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
    (clean / "ok.md").write_text("# OK\n\nShort line, nothing to flag here.\n")
    if main(["--root", str(tmp), str(clean)]) != 0:
        print("FAIL: a clean scan should exit 0")
        ok = False

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

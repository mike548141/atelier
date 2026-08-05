#!/usr/bin/env python3
"""wrapscan — the mechanical check for line-wrap / column hygiene in prose docs.

The rule (2026-07-22 invariant-candidates review, seam S1): Markdown prose
under `docs/**` (and templates) wraps at the house width (~80 cols; ambient
tolerance 81-85). A prose line *materially* over that reds — concretely,
anything at or beyond 86 columns.

GATE SCOPE — the DOCTRINE SURFACE, not all of `docs/**` (WS1, 2026-07-23 S1
cold review; Mike's ruling: option A). The recurring defect this tool targets
— ordinary prose drifting past the house width — lives in `docs/method/`,
`docs/build/`, and `docs/decisions/` bodies; there the corpus is genuinely
near-clean and a finding is real signal. Scanning all of `docs/**` instead
buries that signal under the record/log/review stores' *deliberate*
one-line-per-entry format (`docs/SESSIONS.md`, `docs/sessions/`,
`docs/reviews/`, `docs/decisions/README.md`'s index, harvested
`*-DONE.md`/`*-ARCHIVE.md`) — hundreds of long-by-design grep-able lines that
are not this repo's own wrapped prose, at roughly 6:1 noise to signal on the
un-scoped baseline. So: `ci.yml` invokes this tool against the three doctrine
dirs explicitly, and `.wrapscanignore` (see below) is the belt-and-braces net
for any OTHER invocation — a default `docs/**` scan, a local run with no path
args — so it too stays quiet on the record-format class rather than
reformatting it (rewrapping a deliberate one-line-per-entry format fights the
format and would recur every session; see the review's own 🎯 disposition).

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

THE CHECK — one measurement, six exemptions:

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

  * TABLE ROWS. A line is treated as a Markdown table row (a cell delimiter)
    and exempt whole-line only when it carries a STRUCTURAL pipe signal: it
    starts or ends with `|` (stripped of surrounding whitespace), or it
    contains two or more `|` characters. WS2 (2026-07-23 S1 cold review): a
    bare single-pipe check exempted any line with one inline pipe anywhere —
    a fail-open hole (a long prose line with one shell pipe, `A|B`, or a
    regex would silently pass at any length). Requiring a structural signal
    closes that: a genuine table row always has a leading/trailing `|` or at
    least one interior cell separator (two-plus pipes), while a single
    mid-sentence pipe in prose does not. Honest limit: a contrived prose line
    with two literal pipes (rare) would still be exempted; accepted as a
    cheap, precise-enough heuristic for the actual corpus.

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

  * SIBLING-SCANNER ALLOW-MARKER PADDING. A line whose only reason for
    overflow is a trailing `<!-- <name>scan:allow: <reason> -->` marker
    belonging to ANY scanner in this repo (not just wrapscan's own) is
    exempt. WS4 (2026-07-23 S1 cold review): the marker contract (shared by
    every sibling scanner) requires the reason stay on the *same* line as
    the flagged content, so it can't itself be wrapped — a short, legitimate
    line can read long purely because a mandatory marker pads it (e.g.
    SIGNING.md:120, flagged at 149 cols solely by a trailing
    `leakscan:allow` marker; the prose before it is 62 columns). Heuristic:
    strip a trailing `<!-- <name>scan:allow: ... -->` (optionally followed
    by trailing whitespace) from the end of the line; if what remains is
    <= LINE_LIMIT, the marker alone caused the overflow and the line is
    exempt. Honest limit: this only recognises the house's own
    `<name>scan:allow:` marker shape — a differently-shaped trailing
    annotation is not covered — and only when the marker is the *sole*
    cause; a line that would already overflow without it still flags.

STATED RESIDUAL, HONESTLY (do not round this to "solved"):

  * Column count is a character count, not a display-width measurement (see
    above) — a Unicode-width caveat, not a bug, for an ASCII-prose house.
  * The indented-code exemption is per-line and block-unaware (see above) —
    it will also exempt some genuinely-wrappable indented prose.
  * The table-row exemption (WS2-tightened) requires a structural pipe
    signal (leading/trailing `|`, or two-plus pipes) — not a real table
    parser — it will still exempt a contrived prose line carrying two
    literal pipes (see above).
  * Setext headings (`===`/`---` underlines) are not specially exempted —
    the underline itself is short and never overflows, and the heading text
    line above it is ordinary prose subject to the same limit as any other
    line, which is the correct outcome.
  * UNCLOSED FENCE SWALLOWS THE TAIL (WS3, 2026-07-23 S1 cold review,
    ACCEPTED as a gate-time residual, not fixed). `_content_lines` pairs a
    closing fence by matching character + length, same as datescan's and
    linkscan's identical logic; a fence opened but never closed reads as
    "still inside a fenced block" for the rest of the *file* — every line
    after it, including genuine over-wrapped prose the author never meant as
    code, is silently skipped (proven by `test_malformed_unclosed_fence`,
    which asserts this on purpose). Judgement call: left as-is rather than
    reprocessing the tail, because the alternative — deciding a fence
    "doesn't count" once EOF is reached without it closing — would let a
    genuinely long *pasted* code block (a truncated log/transcript with no
    closing fence, plausible in a review or session note) get scanned as
    prose and flagged, which is the worse failure mode this tool has
    consistently chosen to avoid (see the fenced-code exemption above).
    Blast radius is bounded to the one malformed file, and the doctrine
    surface this tool now gates against is small and human-reviewed, so an
    unclosed fence is expected to be caught by inspection long before it
    hides a real over-wrap. Not solved — a scanner run over a file with a
    stray unclosed fence must not be read as "the rest of that file is
    clean."
  * DOTTED UNITTEST INVOCATION FAILS (WS5, Low, note only, no fix here).
    `python3 -m unittest tools.test_wrapscan` raises `ModuleNotFoundError` —
    only `python3 -m unittest discover -s tools` or `cd tools && python3 -m
    unittest test_wrapscan` work, because the test file imports `wrapscan`
    as a top-level module, not `tools.wrapscan`. Sibling-consistent wart:
    every scanner's test file in this repo has the identical wart (matches
    datescan's DSR7) — fixing it here alone would make wrapscan the odd one
    out, so it is left exactly as consistent as its siblings.
  * Only `docs/**` Markdown is scanned by default (prose lives there); code
    comments, commit messages, and non-Markdown prose are out of scope,
    matching every sibling scanner's default. The CI gate narrows this
    further to the doctrine surface only (see GATE SCOPE, above) —
    `docs/**` remains the *tool's* default fallback for an unscoped run, not
    what the gate itself scans.

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
from dataclasses import dataclass, field, asdict
from pathlib import Path

# A line carrying this marker is intentionally exempt from every check on
# that line. Keep the reason on the same line so the exemption is
# self-documenting and greppable, same contract as the sibling scanners.
ALLOW_MARKER = "wrapscan:allow"

ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r":[ \t]*(?P<reason>\w)")


def parse_allow(line: str) -> bool:
    """True if the line carries a REASONED allow-marker.

    wrapscan has exactly one rule (a line is over width or it is not), so the
    line IS the narrowest allowance available — there is no sub-rule to scope
    to, and inventing one would be ceremony, not narrowness
    (`method/GUARDS.md`, rule a). A marker with no reason does not exempt
    (rule c)."""
    return ALLOW_RX.search(line) is not None


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`."""
    by_marker: int = 0
    files_by_glob: int = 0

    @property
    def marker_total(self) -> int:
        return self.by_marker

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        return ("  suppressed: "
                f"{self.by_marker} by allow-marker · "
                f"{self.files_by_glob} file(s) by .wrapscanignore")


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

# WS4 — any sibling scanner's allow marker, not just wrapscan's own. Matches
# the shared house shape `<!-- <name>scan:allow: <reason> -->`, anchored at
# end-of-line (trailing whitespace allowed after the closing `-->`) because
# the exemption only applies when the marker is what's *padding the tail*,
# not merely present somewhere mid-line.
_SIBLING_ALLOW_MARKER = re.compile(r"<!--\s*\w+scan:allow:.*-->\s*$")


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
    """WS2-tightened: require a STRUCTURAL pipe signal, not a bare
    single-pipe presence check — a lone inline `|` in ordinary prose (a
    shell pipeline, `A|B`, a regex) must not exempt a long line. A genuine
    table row starts or ends with `|` (once surrounding whitespace is
    stripped), or has two or more cell-delimiting pipes; either is
    structural, one bare mid-line pipe is not."""
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("|") or stripped.endswith("|"):
        return True
    return stripped.count("|") >= 2


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


def _is_marker_padding_overflow(line: str, limit: int) -> bool:
    """WS4: True if the line's overflow past `limit` is caused SOLELY by a
    trailing sibling-scanner allow marker (`<!-- <name>scan:allow: ... -->`)
    — see the module header for the full reasoning and its stated limit."""
    if len(line) <= limit:
        return False
    m = _SIBLING_ALLOW_MARKER.search(line)
    if not m:
        return False
    return len(line[:m.start()].rstrip()) <= limit


def _is_exempt(line: str, limit: int = LINE_LIMIT) -> bool:
    return (_is_indented_code(line) or _is_table_row(line)
            or _is_heading(line) or _is_ref_link_definition(line)
            or _is_marker_padding_overflow(line, limit))


def scan_text(path: str, text: str, limit: int = LINE_LIMIT,
              tally: "Tally | None" = None) -> list[Finding]:
    findings: list[Finding] = []
    for lineno, line in _content_lines(text):
        allowed = parse_allow(line)
        length = len(line)
        if length <= limit:
            continue
        # FIND FIRST, SUBTRACT SECOND (rule b): the over-width line is
        # measured before the allowance is consulted, so the exemption is
        # counted instead of disappearing at the top of the loop.
        if allowed:
            if tally is not None:
                tally.by_marker += 1
            continue
        if _is_exempt(line, limit):
            continue
        if _is_single_unbreakable_token_overflow(line, limit):
            continue
        excerpt = line if len(line) <= 100 else line[:97] + "..."
        findings.append(Finding(
            path, lineno, length, excerpt,
            f"{length} columns, over the {limit}-column house limit — wrap it"))
    return findings


class IgnoreFileError(ValueError):
    """An ignore file granted an exemption with no reason stated anywhere."""

    def __init__(self, filename: str, entries: list[tuple[int, str]]):
        self.filename = filename
        self.entries = entries
        detail = "; ".join(f"line {n}: '{g}'" for n, g in entries)
        super().__init__(
            f"{filename}: {len(entries)} glob(s) with no stated reason — "
            f"{detail}. Every exemption states its reason where a reviewer "
            f"reads it (method/GUARDS.md): put a comment above the stanza, or "
            f"a trailing '# reason' on the line.")


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.wrapscanignore`, each of which MUST carry a stated reason.

    GUARDS.md rule (c): an ignore glob is the widest allowance this scanner
    grants — a whole path, every rule, indefinitely — so it is the last place
    an unexplained exemption should be possible. A glob is reasoned if it
    carries a trailing `# reason` (publishscan's form) OR sits under a comment
    block in its own stanza, which is how this estate's ignore files already
    document themselves and is the better documentation of the two. A blank
    line ends a stanza, so a bare glob under no comment at all is refused.

    An unreasoned glob is a CONFIG ERROR, not a warning: a scan that silently
    honours an exemption nobody explained is the failure the rule exists to
    stop. Callers surface it as exit 2 — a broken scan is not a pass."""
    f = root / ".wrapscanignore"
    if not f.exists():
        return []
    globs: list[str] = []
    unreasoned: list[tuple[int, str]] = []
    stanza_reason = False
    for n, raw in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line:
            stanza_reason = False
            continue
        if line.startswith("#"):
            stanza_reason = True
            continue
        glob, _, trailing = line.partition("#")
        glob = glob.strip()
        if not glob:
            continue
        if not trailing.strip() and not stanza_reason:
            unreasoned.append((n, glob))
        globs.append(glob)
    if unreasoned:
        raise IgnoreFileError(".wrapscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  tally: "Tally | None" = None):
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
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            yield p


def scan_paths(paths: list[Path], root: Path, limit: int = LINE_LIMIT,
               tally: "Tally | None" = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs, tally):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text(_rel(md, root), text, limit, tally))
    return findings


def render_human(findings: list[Finding], limit: int,
                 tally: "Tally | None" = None) -> str:
    if not findings:
        out = f"✓ wrapscan clean — no prose lines over {limit} columns."
        return out + ("\n" + tally.summary() if tally is not None else "")
    lines = [f"✗ wrapscan: {len(findings)} finding(s) (limit {limit} columns)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.length} cols] {f.detail}")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A real over-wrap: rewrap the prose at the house width (~80 cols).")
    lines.append(f"  A deliberate exemption: append '<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .wrapscanignore.")
    lines.append("  A marker with no reason exempts nothing.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
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
    tally = Tally()
    try:
        findings = scan_paths(targets, root, args.limit, tally)
    except OSError as e:
        print(f"wrapscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "warn": args.warn,
            "limit": args.limit,
            "findings": [asdict(f) for f in findings],
            "suppressed": {
                "by_allow_marker": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
            },
        }, indent=2))
    else:
        print(render_human(findings, args.limit, tally))
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



def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file that grants an exemption with no reason.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    try:
        return _main(argv)
    except IgnoreFileError as e:
        print(f"wrapscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())

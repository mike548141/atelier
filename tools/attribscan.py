#!/usr/bin/env python3
"""attribscan — an attribution to the principal carries his words, or says whose it is.

WHY (board `320/100`, the second slice of `320/810`). A record says the owner
ruled something, with no quotation of him and no citation of where he said it:
`ruled 2026-08-23`, `the owner's ruling`, `his instruction`, `[x] ruled by him`.
Some were his. Some were an agent's own decision filed under his name, and
later sessions then defended it against him, because the record said he ruled
it. Every other check passed the commits that wrote it: spelling, wrapping,
links, dates and secrets are all satisfied by a confident fabrication, and no
quotation marks means a quote-checker never looks.

THE MACHINE-DECIDABLE HALF is the FORM, not the truth (the item's own offer,
`320/100`). A line that attributes a decision to him, in a place where no
quotation of him, no citation of where his words live and no statement that it
is an agent's own call stands nearby, is reported. What it is NOT: a check that
the attribution is true. A quotation can be invented; that is `320/080`'s
corpus-checking problem and this scanner does not touch it.

WHAT COUNTS. An attribution is, case-insensitively, the word `ruled` (never
`overruled`, `ruled out`, `ruled it out`) in prose; `his ruling|instruction|
directive`, `the owner's ...`, `the principal's ...`; `he directed|instructed`;
and, case-sensitively, a capitalised name's `ruling` or `directive`. Evidence,
in the same block (the lines of the same paragraph or list item, at most three
either side, inline code removed so an example in backticks is not a quote): a
quotation in double quotes straight or curly, a `>` blockquote line, a citation
(`ADR` and a number, `decisions/`, `sessions/`, `transcript`, `session` and a
hex id, a board id such as `060/030`), or a demotion (`an agent's decision`, `the run's choice`, and the like:
`agent|run|session|worker|reviewer` then `'s`, an optional `own`, then
`decision|choice|reading|call|judgement`).

WHAT IT IGNORES, deliberately. Fenced code and inline code spans (a quoted
example is not a claim). `>` blockquote lines as attributions (a blockquote is a
quotation of somebody). `docs/ROADMAP.md` when `docs/roadmap/` exists (the
board's generated index: its lines are the item files', and counting both would
count one claim twice).

THE PLANES, and why this reads ADDITIONS only. Records are append-only history
(`method/RECORD.md`): an old `ruled` cannot be fixed without rewriting the record,
so a check that reddened on one would be a check nobody could clear.
  --staged       the hook plane: lines this commit adds, read against the index
                 copy of the file (context for the block comes from the whole
                 file, not only the added line).
  --against REV  the CI plane (`harvestscan`'s convention): lines added between
                 REV and HEAD. On the first commit `HEAD^` does not exist and the
                 run passes and says so.
  (neither)      whole tree, REPORT ONLY: exit 0 however many it finds, for
                 measuring what share of a repo's records carry the form.

THE DATE. Before `ATTRIBUTION_WARN_UNTIL` a finding on the staged or CI plane is
reported and exits 0. On and after it the finding exits 1, unless `--warn` was
given. The constant is compared with the UTC clock; no flag, environment
variable or config key moves it, in leakscan's `BINARY_GRACE_UNTIL` shape, and
`--warn` is the same advisory spelling every sibling takes. The date is the
run's choice, not his (`320/810`): none before 2027-01-11, one check per four
weeks, this one second.

EXEMPTION. `attribscan:allow: <reason>` on the line or anywhere in its block.
A bare marker exempts nothing.

WHAT IT DOES NOT SEE. Truth (see above). A quotation that is not his. A
capitalised possessive other than `ruling`/`directive` (`Mike's instruction`:
only role words carry `instruction`, because a capitalised word before
`instruction` is usually a product). Records outside the scope the floor hands
it (`docs` by default, narrowed or widened by `.atelier-floor.json`).

Exit codes: 0 nothing blocking (clean, a warning before the date, `--warn`, or
any whole-tree run) · 1 a finding on the staged or CI plane on or after the
date · 2 the scan itself is broken (a broken scan is not a pass).

Stdlib-only, like every sibling.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowmarker  # noqa: E402
import filewalk  # noqa: E402
import report  # noqa: E402

NAME = "attribscan"

# 320/810 slice 2 (see THE DATE above): before this date a finding is reported
# and exits 0; on and after it, it exits 1 unless `--warn` was given. Compared
# with the UTC clock, with no flag, environment variable or config key that
# moves it. A run's choice of date, not the principal's (four weeks after
# blockscan's `SUBSECTION_WARN_UNTIL`, `320/810` names the sequence).
ATTRIBUTION_WARN_UNTIL = datetime.date(2027, 2, 8)

ALLOW_MARKER = f"{NAME}:allow"
ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER, sep=allowmarker.SEP_ANY_SPACE,
                                 named_reason=False)

_SKIP_DIRS = frozenset({".git", "node_modules", ".venv", "venv", "__pycache__",
                        ".mypy_cache", ".pytest_cache", "dist", "build", ".tox"})

MAX_LISTED = 40   # findings printed before an over-cap line
WINDOW = 3        # lines either side of a hit, within the block

# The word itself, never `overruled`, `ruled out`, `ruled-out`, `ruled it out`.
_RULED_RX = re.compile(
    r"(?<![\w-])ruled(?![\w-])(?!\s+(?:it\s+|that\s+|them\s+|this\s+)?out\b)",
    re.IGNORECASE)
_ROLE_RX = re.compile(
    r"\b(?:his|the\s+owner['’]s|the\s+principal['’]s)\s+"
    r"(?:ruling|instruction|directive)\b|\bhe\s+(?:directed|instructed)\b",
    re.IGNORECASE)
# Case-sensitive on purpose: a capitalised word before `'s ruling` is a name.
_NAME_RULING_RX = re.compile(r"\b[A-Z][a-z]+['’]s\s+(?:ruling|directive)\b")

_QUOTE_RX = re.compile(r'["“][^"“”]{2,}["”]')
_CITATION_RX = re.compile(
    r"\bADR[- ]?\d|decisions/|sessions/|\btranscript\b|\bsession\s+[0-9a-f]{6,}\b"
    r"|\b\d{3}/\d{3}(?:/\d{3})?\b",
    re.IGNORECASE)
_DEMOTION_RX = re.compile(
    r"\b(?:agent|run|session|worker|reviewer)['’]s\s+(?:own\s+)?"
    r"(?:decision|choice|reading|call|judg(?:e)?ment)\b", re.IGNORECASE)

_INLINE_CODE_RX = re.compile(r"`+[^`]*`+")
_LIST_ITEM_RX = re.compile(r"^\s*(?:[-*+]\s|\d+\.\s)")
_FENCE_RX = re.compile(r"^(`{3,}|~{3,})")


class ConfigError(RuntimeError):
    """Something the scan needs is unusable; fail closed."""


def _utc_today() -> datetime.date:
    return datetime.datetime.now(datetime.timezone.utc).date()


def warn_only_today(today: datetime.date | None = None) -> bool:
    """True strictly before `ATTRIBUTION_WARN_UNTIL` (UTC). Tests patch
    `_utc_today`; nothing a caller can pass at the command line reaches it."""
    return (today or _utc_today()) < ATTRIBUTION_WARN_UNTIL


@dataclass
class Finding:
    path: str
    line: int
    word: str
    excerpt: str


# --------------------------------------------------------- the block scan --

def _fenced(lines: list[str]) -> set[int]:
    """Zero-based indexes of lines inside a fenced code block. The shared
    sibling rule: an opener is three or more backticks or tildes, closed only
    by a BARE run of the same character at least as long."""
    out: set[int] = set()
    fence_char = ""
    fence_len = 0
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        m = _FENCE_RX.match(stripped)
        if fence_len:
            out.add(i)
            if (m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len
                    and stripped.rstrip() == m.group(1)):
                fence_char, fence_len = "", 0
            continue
        if m:
            fence_char, fence_len = m.group(1)[0], len(m.group(1))
            out.add(i)
    return out


def _is_blockquote(line: str) -> bool:
    return line.lstrip().startswith(">")


def _block_bounds(lines: list[str], i: int) -> tuple[int, int]:
    """The (lo, hi) inclusive window of lines in the same block as line `i`:
    its paragraph or list item, at most `WINDOW` lines either side. A blank
    line, a heading, or another list item ends the block."""
    def stops(line: str) -> bool:
        return not line.strip() or line.lstrip().startswith("#")

    def is_item(line: str) -> bool:
        return bool(_LIST_ITEM_RX.match(line))

    lo = i
    # Going up: stop at the top of this item (include the line that opens it).
    while lo > 0 and i - lo < WINDOW and not is_item(lines[lo]):
        if stops(lines[lo - 1]):
            break
        lo -= 1
    hi = i
    while hi + 1 < len(lines) and hi - i < WINDOW:
        if stops(lines[hi + 1]) or is_item(lines[hi + 1]):
            break
        hi += 1
    return lo, hi


def _strip_code(text: str) -> str:
    return _INLINE_CODE_RX.sub(" ", text)


def _has_evidence(block: list[str]) -> bool:
    if any(_is_blockquote(ln) for ln in block):
        return True
    joined = "\n".join(block)
    text = _strip_code(joined)
    # A citation usually IS in backticks (a path, a board id), so it reads the
    # raw block; a quotation and a demotion read the block with code removed,
    # because an example in backticks is not his words or anybody's call.
    return bool(_QUOTE_RX.search(text) or _CITATION_RX.search(joined)
                or _DEMOTION_RX.search(text))


def _match_attribution(line: str) -> str | None:
    """The attribution word in `line` (inline code removed), or None."""
    text = _strip_code(line)
    for rx in (_RULED_RX, _ROLE_RX, _NAME_RULING_RX):
        m = rx.search(text)
        if m:
            return m.group(0)
    return None


def scan_text(text: str, path: str, lines_of_interest: set[int] | None = None) -> list[Finding]:
    """Findings in one Markdown file's text. `lines_of_interest` (one-based) is
    the added-line set of a diff plane; None means every line."""
    lines = text.splitlines()
    fenced = _fenced(lines)
    findings: list[Finding] = []
    for i, line in enumerate(lines):
        lineno = i + 1
        if lines_of_interest is not None and lineno not in lines_of_interest:
            continue
        if i in fenced or _is_blockquote(line):
            continue
        word = _match_attribution(line)
        if word is None:
            continue
        lo, hi = _block_bounds(lines, i)
        block = lines[lo:hi + 1]
        if _has_evidence(block):
            continue
        if allowmarker.present(ALLOW_RX, "\n".join(block)):
            continue
        findings.append(Finding(path, lineno, word,
                                report.safe_text(line.strip())[:120]))
    return findings


def _is_generated_board(root: Path, rel: str) -> bool:
    return rel == "docs/ROADMAP.md" and (root / "docs" / "roadmap").is_dir()


# ------------------------------------------------------------ the planes --

def _in_scope(rel: str, scopes: list[str]) -> bool:
    if not scopes:
        return True
    for s in scopes:
        if s in (".", "") or rel == s or rel.startswith(s.rstrip("/") + "/"):
            return True
    return False


def _rel_scopes(root: Path, paths: list[str]) -> list[str]:
    """Positional paths as repo-relative POSIX strings; an absolute one is
    rendered from `root` (the floor hands absolute paths on the CI plane)."""
    out = []
    for p in paths:
        if Path(p).is_absolute():
            try:
                out.append(Path(p).resolve().relative_to(root).as_posix())
            except ValueError:
                continue
        else:
            out.append(p.rstrip("/"))
    return out


def _note_read(cov: dict | None, text: str) -> None:
    """115/130 coverage: one more file opened, and the lines it held."""
    if cov is not None:
        cov["files"] = cov.get("files", 0) + 1
        cov["lines"] = cov.get("lines", 0) + len(text.splitlines())


def scan_staged(root: Path, paths: list[str],
                cov: dict | None = None) -> tuple[list[Finding], int]:
    """Added lines of every staged `.md` file, in scope, against its index copy."""
    added = report.staged_added_by_path()
    rc, kept = report.scope_staged(NAME, added, paths, "docs/")
    if rc is not None:
        raise SystemExit(rc)
    findings: list[Finding] = []
    scanned = 0
    for rel, linenos in sorted(kept.items()):
        if not rel.endswith(".md") or _is_generated_board(root, rel):
            continue
        with report.staged_blob(rel) as stream:
            text = stream.read().decode("utf-8", "replace")
        scanned += 1
        _note_read(cov, text)
        findings.extend(scan_text(text, rel, linenos))
    return findings, scanned


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True)


def _has_parent(root: Path) -> bool:
    out = _git(root, "rev-list", "--parents", "-n", "1", "HEAD")
    return out.returncode == 0 and len(out.stdout.split()) > 1


def scan_against(root: Path, rev: str, paths: list[str],
                 cov: dict | None = None) -> tuple[list[Finding], int, str]:
    """Added lines of every `.md` file between `rev` and HEAD, in scope.
    Returns (findings, files scanned, a note for the head line)."""
    verify = _git(root, "rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}")
    if verify.returncode != 0:
        if rev == "HEAD^" and not _has_parent(root):
            return [], 0, "first commit: nothing to compare"
        raise ConfigError(f"cannot resolve revision {rev!r}; refusing to pass over it")
    diff = _git(root, "diff", "--unified=0", "--no-ext-diff", "--no-color",
                "--no-renames", "--src-prefix=a/", "--dst-prefix=b/",
                rev, "HEAD", "--", "*.md")
    if diff.returncode != 0:
        raise ConfigError(f"git diff failed: {diff.stderr.decode('utf-8', 'replace').strip()}")
    scopes = _rel_scopes(root, paths)
    added: dict[str, set[int]] = {}
    for rel, lineno, _text in report.parse_added_lines(diff.stdout):
        added.setdefault(rel, set()).add(lineno)
    findings: list[Finding] = []
    scanned = 0
    for rel, linenos in sorted(added.items()):
        if not rel.endswith(".md") or not _in_scope(rel, scopes) \
                or _is_generated_board(root, rel):
            continue
        show = _git(root, "show", f"HEAD:{rel}")
        if show.returncode != 0:
            raise ConfigError(f"git show HEAD:{rel} failed: "
                              f"{show.stderr.decode('utf-8', 'replace').strip()}")
        scanned += 1
        text = show.stdout.decode("utf-8", "replace")
        _note_read(cov, text)
        findings.extend(scan_text(text, rel, linenos))
    return findings, scanned, ""


def scan_tree(root: Path, paths: list[str],
              cov: dict | None = None) -> tuple[list[Finding], int, int]:
    """Whole tree: every `.md` under the targets, every line. Report only."""
    targets = report.resolve_targets(root, paths or ["."])
    rc = report.refuse_missing_paths(NAME, targets)
    if rc is not None:
        raise SystemExit(rc)
    findings: list[Finding] = []
    scanned = 0
    touched = 0
    for target in targets:
        files = [target] if target.is_file() else filewalk.walk_files(target, _SKIP_DIRS)
        for path in files:
            if path.suffix != ".md" or not path.is_file():
                continue
            rel = path.resolve().relative_to(root).as_posix()
            if _is_generated_board(root, rel):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            _note_read(cov, text)
            hits = scan_text(text, rel)
            scanned += 1
            touched += 1 if hits else 0
            findings.extend(hits)
    return findings, scanned, touched


# ------------------------------------------------------------- reporting --

def render(findings: list[Finding], *, blocking: bool, mode: str, scanned: int,
           note: str, touched: int | None = None) -> str:
    until = ATTRIBUTION_WARN_UNTIL.isoformat()
    lines: list[str] = []
    if not findings:
        where = f"{note} " if note else ""
        lines.append(report.clean_head(
            NAME, f"{where}no attribution to the principal without his words "
                  f"({scanned} file(s) read)."))
    elif blocking:
        lines.append(report.findings_head(
            NAME, len(findings), "unquoted attribution(s)",
            " in added lines — commit blocked."))
    elif mode == "tree":
        lines.append(
            f"⚠ {NAME}: {len(findings)} unquoted attribution(s) in the tree "
            f"(whole-tree report only: exit 0). {touched} of {scanned} file(s).")
    else:
        lines.append(
            f"⚠ {NAME}: {len(findings)} unquoted attribution(s) in added lines "
            f"(warning; blocking from {until}).")
    for f in findings[:MAX_LISTED]:
        lines.append(f"  {f.path}:{f.line}  [{f.word}] {f.excerpt}")
    if len(findings) > MAX_LISTED:
        lines.append(report.over_cap_line(len(findings) - MAX_LISTED, MAX_LISTED))
    if findings:
        lines.append("  Quote him, cite where his words live, say it is an "
                     "agent's decision, or add '"
                     f"<!-- {ALLOW_MARKER}: <reason> -->'.")
    return "\n".join(lines)


def _main(argv: list[str] | None) -> int:
    ap = argparse.ArgumentParser(
        prog=NAME,
        description="An attribution to the principal carries a quotation of "
                    "him, a citation of where he said it, or says it is an "
                    "agent's decision.")
    ap.add_argument("paths", nargs="*",
                    help="files or directories to scan (default: the whole "
                         "repo). Repo-relative with --staged")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--staged", action="store_true",
                    help="the hook plane: lines this commit adds")
    ap.add_argument("--against", default=None, metavar="REV",
                    help="the CI plane: lines added between REV and HEAD")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but exit 0 for them")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the tool against its own fixtures, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return report.quiet_selftest(NAME, _selftest)
    if args.staged and args.against is not None:
        return report.broken(NAME, "--staged and --against are mutually exclusive")

    root = Path(args.root).resolve()
    rc = report.refuse_missing_root(NAME, root, args.root)
    if rc is not None:
        return rc

    note = ""
    touched: int | None = None
    cov: dict = {"files": 0, "lines": 0}
    if args.staged:
        rc = report.refuse_other_repo(NAME, root)
        if rc is not None:
            return rc
        try:
            findings, scanned = scan_staged(root, args.paths, cov)
        except report.STAGED_DIFF_FAILURES as e:
            return report.git_diff_failed(NAME, e)
        mode = "staged"
    elif args.against is not None:
        findings, scanned, note = scan_against(root, args.against, args.paths, cov)
        mode = "against"
    else:
        findings, scanned, touched = scan_tree(root, args.paths, cov)
        mode = "tree"

    gating = mode != "tree"
    blocks = gating and bool(findings) and not args.warn and not warn_only_today()
    reported_not_blocking = 0 if blocks else len(findings)

    if args.json:
        print(json.dumps({
            "clean": not blocks,
            "mode": mode,
            "warn": args.warn,
            "scanned_files": scanned,
            "files_with_findings": touched,
            "findings": [asdict(f) for f in findings],
            "blocking": blocks,
            "until": ATTRIBUTION_WARN_UNTIL.isoformat(),
            "coverage": report.coverage_dict(cov["files"], cov["lines"]),
        }, indent=2))
    else:
        print(render(findings, blocking=blocks, mode=mode, scanned=scanned,
                     note=note, touched=touched))
        print(report.advisory_count_line(NAME, reported_not_blocking))
        print(report.coverage_line(cov["files"], cov["lines"]))
        if args.warn and findings and gating:
            print(report.WARN_NOTICE)
    return report.exit_code(blocks)


def main(argv: list[str] | None = None) -> int:
    return report.guarded_main(NAME, _main, argv, (ConfigError,))


def _selftest() -> int:
    """Minimal smoke test: the shape of each detector over fixtures."""
    fails: list[str] = []

    def check(name: str, got, want) -> None:
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    def hits(text: str) -> int:
        return len(scan_text(text, "x.md"))

    check("a bare ruled", hits("We ruled this on 2026-08-23.\n"), 1)
    check("ruled out", hits("We ruled that out on 2026-08-23.\n"), 0)
    check("overruled", hits("It was overruled.\n"), 0)
    check("a quote nearby clears it",
          hits('He ruled, in his words: "Build the check".\n'), 0)
    check("his ruling", hits("See his ruling on this.\n"), 1)
    check("demoted", hits("Ruled by no one: the run's choice.\n"), 0)
    check("inline code", hits("`ruled 2026-08-23` is the phrase.\n"), 0)
    check("fenced", hits("```\nruled 2026-08-23\n```\n"), 0)
    check("blockquote line", hits("> ruled 2026-08-23\n"), 0)
    check("citation", hits("Ruled, see decisions/0005-going-public.md.\n"), 0)
    check("allow marker",
          hits("Ruled. <!-- attribscan:allow: a worked example -->\n"), 0)
    check("bare marker", hits("Ruled. <!-- attribscan:allow -->\n"), 1)
    for f in fails:
        print(f"{NAME} selftest FAIL: {f}", file=sys.stderr)
    print(f"{NAME} selftest: {'FAILED' if fails else 'ok'} ({len(fails)} failure(s))")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""indexscan — a hand-maintained index stays true to the directory it maps.

THE CLASS (board `200/010`, option C as ruled; `320/430` is the same class
filed from a child). A hand-maintained index — a decisions index, a session
log split into an index plus detail files, a tool or instrument catalogue —
names the files of one directory. Two things can drift apart, and only one of
them was guarded:

  * LISTED BUT MISSING — the index names a file that is not there. Already
    guarded, and NOT re-checked here: `linkscan` (enforced, whole tree, both
    planes) fails a Markdown link whose target does not exist, and `pathscan`
    (warn-only) reports a backtick-named path that does not resolve. A third
    copy of either check would be a second original of it.
  * UNLISTED — a file is in the directory and the index never names it. It is
    committed, and invisible to every session that reads only the index,
    which is what the index exists to make them do. NOTHING caught this:
    a link checker has nothing to fire on when there is no link. The census
    on `200/010` found 22 hand-maintained indexes of 7 kinds across the
    estate, guarded against this direction by none of them. THIS is the
    check this file adds.

ADOPTION IS OPT-IN, PER INDEX. An index declares, in its own text, which
directory it maps and which file pattern it covers. A file with no
declaration is never checked, so this scanner cannot red a repo that has not
declared one: an undeclared tree passes and says it checked nothing. The
declaration is a whole-line HTML comment, invisible when rendered:

    <!-- indexscan:maps dir=<path> match=<glob>[,<glob>…]
         [exclude=<glob>[,<glob>…]] [before=<YYYY-MM-DD>] -->

(on ONE line; wrapped here only for the column budget).

  dir=      the mapped directory, relative to the INDEX FILE's own directory
            (the way a Markdown link in it resolves) — `.` for an index that
            lives inside the directory it maps. Must stay inside --root.
  match=    which entries of that directory the index answers for, matched
            case-sensitively against each entry's NAME (fnmatch). An entry is
            a file or a subdirectory directly inside `dir` — a subdirectory is
            one entry, so an instrument that is a folder is listed once.
  exclude=  entries the index deliberately does not answer for (tests,
            fixtures, a template). The index file itself is always excluded.
  before=   the frozen-record precedent (`reviewscan`'s, `pathscan`'s FR2):
            an entry whose name STARTS with an ISO date earlier than this is
            blameless. Records written before the index was kept are not made
            to come clean by rewriting history. An entry with no leading date
            is never excluded by `before=`.

Several declarations in one index are allowed (one per directory it maps).

WHAT COUNTS AS LISTED. The index names an entry if, outside fenced code, it
carries either:

  * a Markdown link (inline `[t](dest)` or a reference definition) whose
    destination resolves — relative to the index, or to --root for a leading
    `/` — to the entry, or into it when the entry is a directory; or
  * an inline code span whose text (whole, or its first word) resolves to the
    entry relative to the mapped directory, the index's directory, or --root.
    That is how catalogues name things: `` `linkscan.py` `` in a heading,
    `` `ccrepo` `` in a table cell.

A usage example inside a fenced block is not a catalogue entry, so fences
are skipped. Loose by design in the other direction: ANY such link or span
counts, wherever it sits — a passing mention reads as an entry. What this does NOT check: whether a listed entry's line says
anything true about it (a session line whose date disagrees with the file
it links, `320/430`'s second residual, still passes — the link resolves).

EXEMPTIONS — fail noisy, then subtract (`method/GUARDS.md` rule b). Every
subtraction is counted on the summary line, known zeros included:

  * THE ALLOW MARKER, in the index, where the index's readers see it:
        <!-- indexscan:allow: <entry> <reason> -->
    The shared grammar (`tools/allowmarker.py`, unscoped, reason required);
    this scanner reads the reason's first word as the entry's name, so one
    marker exempts exactly one entry (rule a). A marker naming no reason
    after the entry exempts nothing (rule c). A marker that exempts nothing
    — its entry is listed, gone, or outside every `match=` — is reported as
    `stale-allow`: an exemption that outlived its cause is drift too.
  * `exclude=` / `before=` on the declaration are SCOPE, not exemptions: the
    declarer saying what the index answers for. Like `scope` on a softenable
    floor check they need no reason; they are counted all the same.
  * `.indexscanignore` at --root: a path glob exempts a FILE from being read
    for declarations (a fixture tree that quotes the syntax raw). Each glob
    carries a reason, as in every sibling ignore file.

THE FOURTH REQUIREMENT (`method/GUARDS.md`, declared): this guard MAKES THE
FAILURE CHEAP. It forbids nothing — an unlisted file still commits — and it
cannot: whether a file belongs in an index is the index-keeper's call. What it
does is name the drift at the commit that causes it, when the fix is one line.

Exit codes (house contract):
  0  clean — or findings under --warn (the floor registry's wiring)
  1  findings: an unlisted entry, a mapped directory that is gone, a stale
     allow marker
  2  usage / config error — a malformed or unknown-key declaration, a `dir=`
     escaping --root, a bad `before=` date, an unreasoned ignore glob, a path
     that does not exist. NEVER downgraded by --warn: a declaration the
     scanner cannot read is a check that is not running, not a clean pass.

Bounded: each file is read line by line, a physical line past
`MAX_LINE_CHARS` in chunks (a link straddling the cut is the named residual),
and what is held is the set of entries of the one directory being checked.
Zero third-party dependencies; stdlib only.
"""

from __future__ import annotations

import argparse
import datetime
import fnmatch
import json
import posixpath
import re
import sys
import urllib.parse
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402
import allowmarker  # noqa: E402
import report  # noqa: E402

ALLOW_MARKER = "indexscan:allow"
ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER)

# A declaration is a WHOLE LINE that opens an HTML comment with the keyword —
# documentation quoting the syntax inside a code span or a fence is never one
# (the stampscan precedent, ST1). Once a line opens like this it must parse,
# or the scan stops with exit 2.
DECL_START_RX = re.compile(r"^\s{0,3}<!--\s*indexscan:maps\b")
DECL_RX = re.compile(r"^\s{0,3}<!--\s*indexscan:maps\b(?P<body>.*?)-->\s*$")
DECL_KEYS = ("dir", "match", "exclude", "before")
ISO_DATE_RX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LEADING_DATE_RX = re.compile(r"^(\d{4}-\d{2}-\d{2})")

FENCE_RX = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
LINK_RX = re.compile(r"\]\(\s*<?([^)\s>]+)>?")
REFDEF_RX = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?([^\s>]+)>?")
CODE_RX = re.compile(r"`([^`\n]+)`")
SCHEME_RX = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")

INDEX_SUFFIXES = (".md", ".markdown")
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

MAX_LINE_CHARS = 1 << 20
MAX_MATERIALIZED_FINDINGS = 50_000


class ConfigError(ValueError):
    """A declaration that cannot be read. Exit 2, never softened."""


IgnoreFileError = allowmarker.IgnoreFileError


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.indexscanignore`, each carrying a stated reason —
    single-sourced in `tools/allowmarker.py`; this supplies only the name."""
    return allowmarker.load_ignore_globs(root, ".indexscanignore")


@dataclass(frozen=True)
class Decl:
    index: str                 # repo-relative path of the index file
    line: int
    dir: str                   # repo-relative mapped directory ("" = root)
    match: tuple[str, ...]
    exclude: tuple[str, ...]
    before: str | None


@dataclass
class Finding:
    path: str      # the index file
    line: int      # the declaration (or allow marker) the finding belongs to
    kind: str      # unlisted | missing-dir | stale-allow
    entry: str     # repo-relative path of the entry (or the mapped dir)
    detail: str


@dataclass
class Tally:
    indexes: int = 0
    declarations: int = 0
    entries: int = 0
    by_marker: int = 0
    by_exclude: int = 0
    by_before: int = 0
    files_by_glob: int = 0
    findings_over_cap: int = 0
    _materialized: int = field(default=0, repr=False, compare=False)

    def take_finding_slot(self) -> bool:
        if self._materialized < MAX_MATERIALIZED_FINDINGS:
            self._materialized += 1
            return True
        self.findings_over_cap += 1
        return False

    def summary(self) -> str:
        return (f"  checked: {self.declarations} declaration(s) in "
                f"{self.indexes} index file(s), {self.entries} entr(ies) mapped\n"
                + report.suppressed_line(
                    [f"{self.by_marker} by allow-marker",
                     f"{self.by_exclude} by exclude=",
                     f"{self.by_before} by before=",
                     f"{self.files_by_glob} file(s) by .indexscanignore",
                     report.cap_part(self.findings_over_cap,
                                     MAX_MATERIALIZED_FINDINGS)]))


def parse_allow(line: str) -> tuple[str, str] | None:
    """`(entry, reason)` for a reasoned marker, else None. The shared grammar
    finds the marker; its reason's first word names the entry, and the rest
    must still carry a reason (rule c) or the marker exempts nothing."""
    m = ALLOW_RX.search(line)
    if not m:
        return None
    rest = line[m.start("reason"):]
    rest = rest.split("-->", 1)[0].strip()
    entry, _, reason = rest.partition(" ")
    entry = entry.strip().rstrip("/")
    if not entry or not re.search(r"\w", reason):
        return None
    return entry, reason.strip()


def _iter_lines(path: Path):
    """`(lineno, text, at_line_start)`, bounded per read: a physical line
    longer than `MAX_LINE_CHARS` arrives as several chunks, only the first
    marked as a line start (fences and declarations are decided there)."""
    with open(path, encoding="utf-8", errors="replace", newline="") as fh:
        lineno = 0
        at_start = True
        while True:
            chunk = fh.readline(MAX_LINE_CHARS)
            if not chunk:
                return
            if at_start:
                lineno += 1
            yield lineno, chunk.rstrip("\r\n"), at_start
            at_start = chunk.endswith(("\n", "\r"))


def _unfenced(path: Path):
    """The lines of a Markdown file that are outside fenced code."""
    fence: str | None = None
    for lineno, text, at_start in _iter_lines(path):
        if at_start:
            m = FENCE_RX.match(text)
            if m:
                mark = m.group(1)
                if fence is None:
                    fence = mark
                    continue
                if mark[0] == fence[0] and len(mark) >= len(fence) \
                        and not text.strip()[len(mark):].strip():
                    fence = None
                    continue
        if fence is None:
            yield lineno, text, at_start


def _norm(path: str) -> str | None:
    """A repo-relative POSIX path, or None if it leaves the root."""
    p = posixpath.normpath(path)
    if p == ".":
        return ""
    if p.startswith("../") or p == ".." or p.startswith("/"):
        return None
    return p


def _join(base: str, rel: str) -> str | None:
    return _norm(posixpath.join(base, rel) if base else rel)


def _parse_decl(text: str, lineno: int, index_rel: str) -> Decl:
    where = f"{index_rel}:{lineno}"
    m = DECL_RX.match(text)
    if not m:
        raise ConfigError(f"{where}: an indexscan:maps declaration must be one "
                          "whole-line HTML comment ending in '-->'")
    fields: dict[str, str] = {}
    for tok in m.group("body").split():
        key, eq, value = tok.partition("=")
        if not eq or not value:
            raise ConfigError(f"{where}: {tok!r} is not key=value")
        if key not in DECL_KEYS:
            raise ConfigError(f"{where}: unknown key {key!r} — a mistyped key "
                              "would narrow the check without saying so; "
                              f"known keys: {', '.join(DECL_KEYS)}")
        if key in fields:
            raise ConfigError(f"{where}: {key!r} given twice")
        fields[key] = value
    for required in ("dir", "match"):
        if required not in fields:
            raise ConfigError(f"{where}: {required}= is required")
    raw_dir = fields["dir"]
    if raw_dir.startswith("/"):
        raise ConfigError(f"{where}: dir={raw_dir!r} must be relative to the index")
    mapped = _join(posixpath.dirname(index_rel), raw_dir.rstrip("/") or ".")
    if mapped is None:
        raise ConfigError(f"{where}: dir={raw_dir!r} resolves outside --root")

    def globs(key: str) -> tuple[str, ...]:
        if key not in fields:
            return ()
        out = tuple(g for g in fields[key].split(",") if g)
        if not out:
            raise ConfigError(f"{where}: {key}= names no glob")
        return out

    before = fields.get("before")
    if before is not None:
        if not ISO_DATE_RX.match(before):
            raise ConfigError(f"{where}: before={before!r} is not YYYY-MM-DD")
        try:
            datetime.date.fromisoformat(before)
        except ValueError:
            raise ConfigError(f"{where}: before={before!r} is not a real date")
    return Decl(index_rel, lineno, mapped, globs("match"), globs("exclude"), before)


def discover(path: Path, index_rel: str) -> tuple[list[Decl], dict[str, int]]:
    """Pass 1 over one Markdown file: its declarations and allow markers."""
    decls: list[Decl] = []
    allows: dict[str, int] = {}
    for lineno, text, at_start in _unfenced(path):
        if "indexscan:" not in text:
            continue
        if at_start and DECL_START_RX.match(text):
            decls.append(_parse_decl(text, lineno, index_rel))
            continue
        hit = parse_allow(text)
        if hit is not None:
            allows.setdefault(hit[0], lineno)
    return decls, allows


def _entries(root: Path, mapped: str) -> set[str] | None:
    """Names directly inside the mapped directory — files and subdirectories
    — that could be committed (the shared walk: git-aware, skip-dirs pruned,
    nested worktrees never entered). None if the directory is gone."""
    base = root / mapped if mapped else root
    if not base.is_dir():
        return None
    names: set[str] = set()
    for p in filewalk.walk_files(base, SKIP_DIR_NAMES):
        try:
            names.add(p.relative_to(base).parts[0])
        except (ValueError, IndexError):
            continue
    return names


def _references(path: Path, index_rel: str, mapped_dirs: set[str],
                wanted: set[str]) -> set[str]:
    """Pass 2: which of `wanted` (repo-relative entry paths) the index names."""
    index_dir = posixpath.dirname(index_rel)
    found: set[str] = set()

    def mark(candidate: str | None) -> None:
        while candidate:
            if candidate in wanted:
                found.add(candidate)
                return
            candidate = posixpath.dirname(candidate)

    for _lineno, text, _start in _unfenced(path):
        dests = LINK_RX.findall(text)
        m = REFDEF_RX.match(text)
        if m:
            dests.append(m.group(1))
        for dest in dests:
            if dest.startswith("#") or dest.startswith("//") or SCHEME_RX.match(dest):
                continue
            dest = urllib.parse.unquote(dest.split("#", 1)[0].split("?", 1)[0])
            if not dest:
                continue
            mark(_norm(dest.lstrip("/")) if dest.startswith("/")
                 else _join(index_dir, dest))
        for span in CODE_RX.findall(text):
            span = span.strip()
            tokens = {span, span.split()[0]} if span else set()
            for tok in tokens:
                tok = tok.rstrip("/")
                if not tok or tok.startswith("/") or SCHEME_RX.match(tok):
                    continue
                for base in (*mapped_dirs, index_dir, ""):
                    mark(_join(base, tok))
    return found


def _rel(p: Path, root: Path) -> str:
    try:
        return p.resolve().relative_to(root).as_posix()
    except ValueError:
        return p.as_posix()


def _index_files(paths: list[Path], root: Path, globs: list[str], tally: Tally):
    seen: set[str] = set()
    for base in paths:
        candidates = [base] if base.is_file() else filewalk.walk_files(base, SKIP_DIR_NAMES)
        for p in candidates:
            if p.suffix.lower() not in INDEX_SUFFIXES:
                continue
            rel = _rel(p, root)
            if rel in seen:
                continue
            seen.add(rel)
            if allowmarker.ignored(rel, globs):
                tally.files_by_glob += 1
                continue
            yield p, rel


def _add(findings: list[Finding], tally: Tally, f: Finding) -> None:
    if tally.take_finding_slot():
        findings.append(f)


def check_index(path: Path, index_rel: str, decls: list[Decl],
                allows: dict[str, int], root: Path, tally: Tally) -> list[Finding]:
    findings: list[Finding] = []
    tally.indexes += 1
    candidates: dict[str, Decl] = {}       # repo-relative entry -> its declaration
    for d in decls:
        tally.declarations += 1
        names = _entries(root, d.dir)
        if names is None:
            _add(findings, tally, Finding(
                index_rel, d.line, "missing-dir", d.dir or ".",
                "the declared directory does not exist — fix dir= or remove "
                "the declaration"))
            continue
        for name in sorted(names):
            entry = f"{d.dir}/{name}" if d.dir else name
            if entry == index_rel:
                continue
            if not any(fnmatch.fnmatchcase(name, g) for g in d.match):
                continue
            if any(fnmatch.fnmatchcase(name, g) for g in d.exclude):
                tally.by_exclude += 1
                continue
            if d.before:
                m = LEADING_DATE_RX.match(name)
                if m and m.group(1) < d.before:
                    tally.by_before += 1
                    continue
            tally.entries += 1
            candidates.setdefault(entry, d)
    listed = _references(path, index_rel, {d.dir for d in decls}, set(candidates))
    used: set[str] = set()
    for entry, d in sorted(candidates.items()):
        if entry in listed:
            continue
        name = posixpath.basename(entry)
        if name in allows:
            tally.by_marker += 1
            used.add(name)
            continue
        _add(findings, tally, Finding(
            index_rel, d.line, "unlisted", entry,
            "in the mapped directory and never named by the index — add its "
            "line, widen exclude=, or mark it "
            f"'<!-- {ALLOW_MARKER}: {name} <reason> -->'"))
    for name, line in sorted(allows.items(), key=lambda kv: kv[1]):
        if name not in used:
            _add(findings, tally, Finding(
                index_rel, line, "stale-allow", name,
                "this allow marker exempts nothing — the entry is listed, "
                "gone, or outside every match= — remove it"))
    return findings


def scan_paths(paths: list[Path], root: Path, tally: Tally) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel in _index_files(paths, root, globs, tally):
        decls, allows = discover(p, rel)
        if not decls:
            continue
        findings.extend(check_index(p, rel, decls, allows, root, tally))
    return findings


def render_human(findings: list[Finding], tally: Tally) -> str:
    total = len(findings) + tally.findings_over_cap
    if not total:
        head = report.clean_head(
            "indexscan",
            "every mapped entry is named by its index." if tally.declarations
            else "no index declares a mapped directory "
                 "(nothing to check; adoption is opt-in per index).")
        return head + "\n" + tally.summary()
    lines = [report.findings_head("indexscan", total)]
    for f in sorted(findings, key=lambda x: (x.path, x.line, x.entry)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.entry} → {f.detail}")
    if tally.findings_over_cap:
        lines.append(f"  …and {tally.findings_over_cap} more finding(s), counted "
                     "but not listed.")
    lines.append("")
    lines.append(tally.summary())
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="indexscan",
        description="Check that every hand-maintained index which declares a "
                    "mapped directory names every entry in it.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to search for declaring indexes (default: --root)")
    ap.add_argument("--root", default=".",
                    help="repo root: where dir= must stay, and .indexscanignore")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but exit 0 (the floor's warn-only "
                         "wiring); config errors still exit 2")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    rc = report.refuse_missing_root("indexscan", root, args.root)
    if rc is not None:
        return rc
    targets = report.resolve_targets(root, args.paths or [str(root)])
    rc = report.refuse_missing_paths("indexscan", targets)
    if rc is not None:
        return rc

    tally = Tally()
    try:
        findings = scan_paths(targets, root, tally)
    except ConfigError as e:
        return report.broken("indexscan", str(e))
    except OSError as e:
        return report.cannot_read("indexscan", e)

    total = len(findings) + tally.findings_over_cap
    if args.json:
        print(json.dumps({
            "clean": not total,
            "warn": args.warn,
            "findings": [asdict(f) for f in findings],
            "findings_over_cap": tally.findings_over_cap,
            "checked": {"indexes": tally.indexes,
                        "declarations": tally.declarations,
                        "entries": tally.entries},
            "suppressed": {"by_allow_marker": tally.by_marker,
                           "by_exclude": tally.by_exclude,
                           "by_before": tally.by_before,
                           "files_by_ignore_glob": tally.files_by_glob},
        }, indent=2))
    else:
        print(render_human(findings, tally))
        if total and args.warn:
            print(report.WARN_NOTICE)
    return report.exit_code(total, warn=args.warn)


def _selftest() -> int:
    """Prove the engine offline, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="indexscan-self-"))
    ok = True
    try:
        rec = tmp / "docs" / "records"
        rec.mkdir(parents=True)
        for name in ("2026-01-01-old.md", "2026-05-01-listed.md",
                     "2026-05-02-orphan.md", "2026-05-03-allowed.md",
                     "template.md"):
            (rec / name).write_text("# r\n", encoding="utf-8")
        (tmp / "docs" / "INDEX.md").write_text(
            "# Index\n"
            "<!-- indexscan:maps dir=records match=*.md exclude=template.md "
            "before=2026-02-01 -->\n"
            "<!-- indexscan:allow: 2026-05-03-allowed.md selftest fixture -->\n"
            "- [listed](records/2026-05-01-listed.md)\n"
            "```\n- [fenced](records/2026-05-02-orphan.md)\n```\n",
            encoding="utf-8")
        tally = Tally()
        got = sorted((f.kind, f.entry) for f in scan_paths([tmp], tmp.resolve(), tally))
        want = [("unlisted", "docs/records/2026-05-02-orphan.md")]
        if got != want:
            print(f"FAIL: got {got}, expected {want}")
            ok = False
        if (tally.by_marker, tally.by_exclude, tally.by_before) != (1, 1, 1):
            print(f"FAIL: subtraction counts {tally}")
            ok = False
        empty = tmp / "empty"
        empty.mkdir()
        (empty / "README.md").write_text("# nothing declared\n", encoding="utf-8")
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            undeclared = main(["--root", str(empty)])
        if undeclared != 0:
            print("FAIL: an undeclared tree must pass")
            ok = False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("selftest OK" if ok else "selftest FAILED")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    return report.guarded_main("indexscan", _main, argv, (IgnoreFileError,))


if __name__ == "__main__":
    sys.exit(main())

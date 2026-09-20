#!/usr/bin/env python3
"""conflictscan — the mechanical check that no unresolved merge-conflict
marker reaches git history.

THE INCIDENT (roadmap `320/200`, filed 2026-09-08). A merge into a public
child's `main` committed a live three-way conflict into a records index —
`<<<<<<< HEAD`, `=======`, `>>>>>>> <sha> (…)` — fencing two entries that both
belonged. The repo is public, so the markers were public for about a day
before an unrelated edit to the same file happened to surface them. Nothing
mechanical caught it: the floor was green on every commit, `wrapscan` cannot
fire (`<<<<<<< HEAD` is 14 columns against an 85-column limit), and the
child's own record-index gate asked "is each record named", which a fence
does not disturb. RULED (Mike, 2026-09-18, via the question device): option 1
of that item — a new small scanner, ENFORCED, with the usual per-line
allow-marker for docs that quote the markers.

ENFORCED FROM DAY ONE, NOT FIRST-OF-KIND ADVISORY. Unlike `datescan`/
`wrapscan`/`spellscan` (judgement-adjacent prose checks that landed
warn-first because their corpus wasn't clean yet), a committed conflict
marker is never correct — the same severity class as `secretscan`
(`advisory=None` in `tools/floor.py`'s registry): there is no "adopting the
check, N findings to clear" state for a marker that fences broken content.
It has no `--warn` flag and no advisory form; see the module's exit-code
contract below.

THE CHECK — four marker shapes, one deliberately gated on the other three:

  * OPENER  `^<<<<<<< ` (seven `<` then a space; the ref/branch name follows).
  * CLOSER  `^>>>>>>> ` (seven `>` then a space; ditto).
  * BASE    `^\\|\\|\\|\\|\\|\\|\\| ` (diff3's common-ancestor marker, seven
    `|` then a space) — only inside an OPEN region (see below).
  * SEPARATOR  `^=======$`, exactly seven `=` and nothing else on the line
    (a trailing `\\r` is stripped first, so a CRLF-saved file matches too) —
    only inside an OPEN region (see below).

  OPENER and CLOSER are flagged UNCONDITIONALLY: the seven-character run plus
  a trailing space is not a shape any real prose, code, or ASCII-art rule
  produces by accident, so no gating is needed and none is applied — this
  also means a truncated/malformed file (a `>>>>>>> ` with no matching
  opener earlier, e.g. only the tail of a diff was captured) still flags.

  THE `=======` AMBIGUITY (the reason this scanner isn't a three-line regex
  grep). A bare `=======` line is also a VALID Markdown/RST setext H1
  underline — `wrapscan`'s own doctrine files use exactly this shape for
  headings, and a naive "any line of only `=` characters" rule would fire on
  every one of them and get switched off in its first week, the fate this
  item's own § *Options* names as the risk of "a naive implementation".

  The chosen rule is BOTH of the item's two offered mitigations at once, not
  either alone:

    1. EXACT LENGTH. `^=======$` requires PRECISELY seven `=` characters,
       not "three or more" (RST/Markdown setext underlines are commonly
       longer, matching the heading's own width, or a conventional `---`/
       `===` of exactly one repeat) — narrower than a bare "line of only
       `=`" check, but NOT narrow enough alone: a heading exactly seven
       characters wide (`Legend\n=======`) produces a coincidentally
       identical line, so length alone is not sound.
    2. STATE. A `=======` (or `|||||||`) line is a finding ONLY when an
       earlier OPENER on the same file has not yet been closed by a CLOSER —
       i.e. the scanner is walking a file it believes is mid-conflict. A
       standalone setext underline, however wide, never sits after an
       unclosed `<<<<<<< ` line, so it never enters this state. Combined,
       the two checks close the gap either one leaves alone: length rules
       out most accidental matches, and state rules out the residual case
       (a coincidentally seven-character heading) UNLESS the file also
       carries a genuine, unclosed opener above it — at which point calling
       it a finding is the more honest reading of the file anyway.

  HONEST RESIDUAL, STATED, NOT ROUNDED UP: an OPENER with no matching CLOSER
  before end-of-file leaves the scanner believing every line is still inside
  the conflict for the REST of that file, so a later, otherwise-innocent
  `=======` or `|||||||` line downstream of a genuinely unclosed marker also
  flags. This is the opposite direction from `datescan`'s/`wrapscan`'s own
  "unclosed fence swallows the tail" residual (which UNDER-flags the rest of
  a file after a malformed fence) — here the tail is OVER-flagged instead.
  That is the accepted trade for this scanner's subject: a file that opened a
  conflict and never closed it is ALREADY the failure mode this check exists
  to catch, so treating everything after an unclosed opener as suspect is the
  safer of the two directions, not a bug to fix.

SCOPE — ALL tracked text files, not Markdown-only (unlike `datescan`/
`wrapscan`/`spellscan`/`pathscan`). A conflict marker can land in any file a
bad merge touches — source, config, JSON, YAML — so this scanner matches
`secretscan`'s/`leakscan`'s shape (whole-tree walk, binary skipped by a NUL
byte in the first 8KiB) rather than the Markdown-only doc scanners'. Like
every sibling here, "tracked" means the filesystem walk this repo's other
scanners already use (skip `.git`/build-cache dirs, honour
`.conflictscanignore`) — none of them consult `git ls-files`, and adding that
distinction here alone would make this scanner behave differently from its
neighbours for no reason this check's subject demands. Scanning an untracked
file too is a strict superset of the intended scope, never a hole.

NO FENCED-CODE EXEMPTION, ON PURPOSE. `datescan`/`wrapscan`/`pathscan` skip
fenced (``` ```) code blocks because those are Markdown-specific and an
illustrative example there is not a live claim. This scanner runs over EVERY
tracked file type, most of which have no such convention (a `.py` or `.json`
file has no "fenced block"), so a Markdown-only exemption here would be
inconsistent — quiet on a fenced example in a `.md` file and loud on the
identical text in a code comment. The item that grounds this scanner is
itself the worked case: it quotes the three markers inline (mid-line, so
none of its own prose lines match the anchored patterns above) rather than
in a fenced block, and states plainly that a scanner needs "the usual
per-line allow-marker for docs that quote them" — so THAT is the sanctioned
route for a doc that legitimately puts a marker at the start of a line, not
an automatic fenced-code pass.

`--staged` (the hook plane) reads only the ADDED lines of the staged diff,
the same shape and the same accepted limit as `secretscan`'s/`leakscan`'s own
`--staged` mode: a conflict fenced by a bad merge is new content in the
commit that introduces it, so the added-lines diff is expected to carry the
whole opener/…/closer run together, in order, exactly as it would appear on
disk. The CI plane reads the WHOLE TREE (`scan_paths`), which is the backstop
for anything the staged view cannot see (a marker that predates this
scanner's adoption, or one introduced by a mechanism other than `git commit`
on this machine).

EXEMPTIONS, same contract as every sibling scanner:

  * THE ALLOW MARKER. A line carrying `conflictscan:allow: <reason>` anywhere
    is exempt from the one finding that line could otherwise produce — see
    `parse_allow`. `conflictscan` has exactly one shape of rule per line (is
    this a conflict marker, in context), so — matching `wrapscan`'s own
    reasoning for the same shape of rule — there is no sub-kind worth scoping
    the marker to; the line itself is already the narrowest allowance
    (`method/GUARDS.md`, rule a).
  * `.conflictscanignore` at the scan root exempts a path wholesale, each
    glob carrying a stated reason — identical contract to every sibling
    ignore file (`method/GUARDS.md`, rule c): an unreasoned glob is a CONFIG
    ERROR (exit 2), not a silent pass.

Exit codes (fail-safe, no `--warn` — this check has no advisory form, so
there is nothing to soften to):
  0  clean
  1  findings — the commit is blocked
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can
run it with the system python3 and no install — and CI needs nothing but
Python.
"""

from __future__ import annotations

import argparse
import codecs
import fnmatch
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402

# A line carrying this marker is intentionally exempt from the one finding it
# could otherwise produce. Keep the reason on the same line so the exemption
# is self-documenting and greppable, same contract as the sibling scanners.
ALLOW_MARKER = "conflictscan:allow"

ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r":[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> bool:
    """True if the line carries a REASONED allow-marker.

    Like `wrapscan`, this scanner has exactly one rule per line (is this line
    a conflict marker, in the context read so far) — there is no sub-kind to
    scope the marker to, and inventing one would be ceremony, not narrowness
    (`method/GUARDS.md`, rule a). A marker with no reason does not exempt
    (rule c)."""
    return ALLOW_RX.search(line) is not None


# 020/380 — a fixed ceiling on how many `Finding` objects one run
# MATERIALIZES (builds and holds in memory), independent of how many the
# input actually contains. Same defect class `020/370` fixed in `secretscan`:
# a pathological tree (e.g. a huge merge scar repeated many times) can
# generate an unbounded NUMBER of findings independent of tree size.
# Reusing secretscan's own budget rather than re-deriving one: each held
# `Finding` costs on the order of 1 KiB (path + excerpt + object overhead),
# so a ~50 MiB findings budget — independent of input size — gives the same
# round cap. Findings past the cap are COUNTED (`Tally.findings_over_cap`),
# never dropped silently.
MAX_MATERIALIZED_FINDINGS = 50_000


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`.

    A guard that subtracts silently prints the same clean tick for "nothing
    matched" and "everything matched and was exempted"."""
    by_marker: dict[str, int] = field(default_factory=dict)
    files_by_glob: int = 0
    # 020/380 — see MAX_MATERIALIZED_FINDINGS above. Every finding here
    # blocks (conflictscan has no advisory tier), so one counter is enough.
    findings_over_cap: int = 0
    _materialized: int = field(default=0, repr=False, compare=False)

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def take_finding_slot(self) -> bool:
        """True if a finding may still be fully materialized (built and
        held); False once the run-wide cap is reached, in which case the
        caller counts it via `findings_over_cap` instead of building a
        `Finding` for it."""
        if self._materialized < MAX_MATERIALIZED_FINDINGS:
            self._materialized += 1
            return True
        self.findings_over_cap += 1
        return False

    def note_marker(self, kind: str) -> None:
        self.by_marker[kind] = self.by_marker.get(kind, 0) + 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        line = ("  suppressed: "
                f"{self.marker_total} by allow-marker · "
                f"{self.files_by_glob} file(s) by .conflictscanignore · "
                f"{self.findings_over_cap} beyond the "
                f"{MAX_MATERIALIZED_FINDINGS}-finding cap (counted, not listed)")
        if self.by_marker:
            detail = ", ".join(f"{k}×{n}" for k, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        return line


# Paths never worth walking. Hardcode-skip ONLY names that are never
# human-authored/committed content — VCS, dependency, and tool-cache dirs
# (matches every sibling scanner).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# The four marker shapes. OPENER/CLOSER/BASE are anchored at line start only
# (`re.match`, not `re.fullmatch`) — the ref/branch name or commit message
# that follows the marker varies and is not part of the shape being matched.
# SEPARATOR has no compiled pattern: it is checked by exact string equality
# after stripping a trailing `\r` (see `_strip_cr`), which is both simpler
# and impossible to get subtly wrong with an anchoring mistake.
OPENER_RX = re.compile(r"^<{7} ")
CLOSER_RX = re.compile(r"^>{7} ")
BASE_RX = re.compile(r"^\|{7} ")
SEPARATOR_TEXT = "=" * 7


def _strip_cr(line: str) -> str:
    """Drop one trailing `\\r`, so a CRLF-saved file's separator line (which
    various readers can leave as `'=======\\r'` after an LF-only split)
    still compares equal to the canonical seven-`=` shape."""
    return line[:-1] if line.endswith("\r") else line


@dataclass
class Finding:
    path: str          # the flagged file (repo-relative)
    line: int
    kind: str           # "opener" | "closer" | "base" | "separator"
    match: str          # the matched line, as written (trimmed for length)
    detail: str        # human hint at the fix


def _excerpt(line: str) -> str:
    stripped = line.rstrip("\r\n")
    return stripped if len(stripped) <= 100 else stripped[:97] + "..."


def _record(findings: list[Finding], tally: "Tally | None", finding: Finding) -> None:
    """Append `finding` unless the run-wide materialization cap (020/380,
    `MAX_MATERIALIZED_FINDINGS`) has been reached — in which case
    `tally.take_finding_slot` has already counted it. Same choke-point shape
    as `secretscan._record` (020/370)."""
    if tally is None or tally.take_finding_slot():
        findings.append(finding)


def _line_finding(path: str, lineno: int, window: str, is_final_window: bool,
                  in_conflict: bool) -> tuple["Finding | None", bool]:
    """Decide whether ONE physical line's content (or, for an overlong line,
    its FIRST window — see `_scan_file`) is a conflict-marker finding, and
    the new `in_conflict` state.

    Only ever called with the FIRST window of a physical line: OPENER/
    CLOSER/BASE are anchored at column 0, so the first window carries
    everything needed to decide them regardless of how much more of the
    line follows. SEPARATOR requires the line to be EXACTLY seven `=`
    characters, so it is only ever considered when this window is also the
    line's LAST (`is_final_window`) — an overlong line can never be exactly
    seven characters, so that case correctly never matches."""
    if OPENER_RX.match(window):
        return Finding(
            path, lineno, "opener", _excerpt(window),
            "unresolved merge-conflict opener — resolve the merge and "
            "remove the marker"), True
    if CLOSER_RX.match(window):
        return Finding(
            path, lineno, "closer", _excerpt(window),
            "unresolved merge-conflict closer — resolve the merge and "
            "remove the marker"), False
    if in_conflict and BASE_RX.match(window):
        return Finding(
            path, lineno, "base", _excerpt(window),
            "diff3 common-ancestor marker inside an open conflict — "
            "resolve the merge and remove the marker"), in_conflict
    if in_conflict and is_final_window and _strip_cr(window) == SEPARATOR_TEXT:
        return Finding(
            path, lineno, "separator", _excerpt(window),
            "merge-conflict separator inside an open conflict — resolve "
            "the merge and remove the marker"), in_conflict
    return None, in_conflict


def scan_text(path: str, text: str, tally: "Tally | None" = None) -> list[Finding]:
    """Walk `text` line by line, tracking whether we are inside what looks
    like an open conflict region (an OPENER seen with no CLOSER since) — see
    the module docstring's "THE `=======` AMBIGUITY" section for why
    SEPARATOR/BASE are gated on this state and OPENER/CLOSER are not.

    The staged-diff caller's shape: the diff's added lines are already held
    in memory, so this is the whole-blob convenience wrapper; `_scan_file`
    below is the streaming shape the whole-tree walk uses."""
    findings: list[Finding] = []
    in_conflict = False
    for lineno, raw in enumerate(text.splitlines(), start=1):
        finding, in_conflict = _line_finding(path, lineno, raw, True, in_conflict)
        if finding is None:
            continue
        if parse_allow(raw):
            if tally is not None:
                tally.note_marker(finding.kind)
            continue
        _record(findings, tally, finding)
    return findings


def _looks_binary(data: bytes) -> bool:
    """Matches `secretscan`'s/`leakscan`'s own heuristic exactly: a NUL byte
    in the first 8KiB is not valid text in any encoding this repo writes, and
    a binary container (an image, a compiled artefact) cannot carry a
    line-anchored text marker in any way this scanner could act on."""
    return b"\x00" in data[:8192]


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
    """Globs from `.conflictscanignore`, each of which MUST carry a stated
    reason. Identical contract to every sibling scanner's ignore file — see
    `datescan.load_ignore_globs`/`secretscan.load_ignore_globs` for the full
    reasoning; kept here verbatim rather than shared so each scanner stays a
    file a peer can copy alone."""
    f = root / ".conflictscanignore"
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
        raise IgnoreFileError(".conflictscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time. Single-sourced
    (115/080 part 1) in `tools/filewalk.py` — see that module's docstring
    for the mechanism and the 020/160 (E9) linked-worktree skip.
    `SKIP_DIR_NAMES` is this scanner's own per-guard parameter, passed in
    rather than shared."""
    return filewalk.walk_files(base, SKIP_DIR_NAMES)


def iter_files(paths: list[Path], root: Path, globs: list[str],
              tally: "Tally | None" = None):
    for base in paths:
        candidates = [base] if base.is_file() else _walk_files(base)
        for p in candidates:
            rel = _rel(p, root)
            if _ignored(rel, globs):
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            yield p, rel


# Streaming-read tuning (020/380, reusing secretscan's 020/370 constants
# verbatim — every FIXED size here is chosen once and independent of the
# file or tree being scanned, which is the entire fix). See `secretscan.py`'s
# module comment above its own copy of these for the full derivation.
READ_CHUNK_BYTES = 1 * 1024 * 1024        # raw bytes read from disk at a time
LINE_WINDOW_BYTES = 4 * 1024 * 1024       # a physical line (no '\n' in sight)
                                          # longer than this is scanned in
                                          # WINDOWS rather than buffered whole
LINE_WINDOW_OVERLAP = 64 * 1024           # carried from one window into the
                                          # next so an allow-marker straddling
                                          # the cut is still whole in one of
                                          # the two (see `_scan_file`)


def _iter_numbered_lines(path: Path):
    """Yield `(lineno, text, is_final_window)` for every physical line in
    `path`, reading and decoding it in fixed-size chunks so peak memory for
    ONE file is bounded by `LINE_WINDOW_BYTES + LINE_WINDOW_OVERLAP` —
    independent of the file's total size or its longest line. Yields nothing
    for a file that looks binary (checked on the first chunk only).

    This replaces the old `read_bytes()` → whole `str` → `splitlines()`
    list, which held the file THREE TIMES OVER at once (the same shape
    020/370 fixed in secretscan)."""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    lineno = 1
    pending = ""
    with open(path, "rb") as fh:
        first_chunk = True
        while True:
            chunk = fh.read(READ_CHUNK_BYTES)
            if first_chunk:
                first_chunk = False
                if _looks_binary(chunk):
                    return
            if not chunk:
                break
            pending += decoder.decode(chunk)
            while True:
                nl = pending.find("\n")
                if nl == -1:
                    break
                yield lineno, pending[:nl], True
                pending = pending[nl + 1:]
                lineno += 1
            if len(pending) >= LINE_WINDOW_BYTES:
                yield lineno, pending, False
                pending = pending[-LINE_WINDOW_OVERLAP:]
        pending += decoder.decode(b"", final=True)
        if pending:
            yield lineno, pending, True  # EOF: whatever remains is the last line


def _scan_file(path: Path, rel: str, tally: "Tally | None") -> list[Finding]:
    """Scan one file with memory bounded by a fixed constant regardless of
    the file's size (020/380) — see `_iter_numbered_lines`.

    OPENER/CLOSER/BASE are decided from the FIRST window of each physical
    line only (they are anchored at column 0, so later windows of the same
    overlong line carry nothing the decision needs); SEPARATOR is only
    considered when that first window is also the line's last, since an
    overlong line can never be exactly the seven-character separator. The
    allow-marker, unlike the finding shape, can sit ANYWHERE on the line, so
    it is searched for in EVERY window of the line and unioned — the same
    reason `secretscan`'s streaming reader carries `LINE_WINDOW_OVERLAP`
    between windows: a marker straddling a window cut must still be found in
    one of the two windows that contain it.

    UNLIKE `secretscan._scan_file`, an `OSError` here is NOT swallowed: the
    pre-existing `_main` wraps `scan_paths` in its own `except OSError`
    (`cannot read <file>` → exit 2, "a broken scan is not a pass") and that
    behaviour predates this fix, so it must survive unchanged rather than
    being silently narrowed to a per-file skip."""
    findings: list[Finding] = []
    in_conflict = False
    seen_lineno: int | None = None
    current_finding: "Finding | None" = None
    allow_hit = False
    for lineno, window, is_final in _iter_numbered_lines(path):
        if lineno != seen_lineno:
            seen_lineno = lineno
            current_finding, in_conflict = _line_finding(
                rel, lineno, window, is_final, in_conflict)
            allow_hit = parse_allow(window)
        elif not allow_hit and parse_allow(window):
            allow_hit = True
        if is_final:
            if current_finding is not None:
                if allow_hit:
                    if tally is not None:
                        tally.note_marker(current_finding.kind)
                else:
                    _record(findings, tally, current_finding)
            current_finding = None
            allow_hit = False
    return findings


def scan_paths(paths: list[Path], root: Path,
               tally: "Tally | None" = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p, rel in iter_files(paths, root, globs, tally):
        findings.extend(_scan_file(p, rel, tally))
    return findings


def staged_added_lines() -> dict[str, str]:
    """Path → the added-line text of the staged diff. Scans only what a
    commit would introduce (the pre-commit hot path), not the whole tree —
    identical shape to `secretscan.staged_added_lines`.

    `R` is in the diff filter deliberately (matches `secretscan`'s own
    review-B4 reasoning): a renamed-and-edited file's added lines can carry a
    conflict marker exactly as a modified file's can, and `ACM` alone would
    silently skip them."""
    out = subprocess.run(
        ["git", "diff", "--cached", "--unified=0", "--no-color",
         "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True).stdout
    files: dict[str, list[str]] = {}
    current: str | None = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
            files.setdefault(current, [])
        elif line.startswith("+") and not line.startswith("+++") and current:
            files[current].append(line[1:])
    return {path: "\n".join(lines) for path, lines in files.items() if lines}


def render_human(findings: list[Finding], tally: "Tally | None" = None) -> str:
    # 020/380 — a capped run's TRUE total lives on the tally, never on
    # `len(findings)`: everything past `MAX_MATERIALIZED_FINDINGS` was
    # counted there instead of being built as a `Finding` at all — see
    # `Tally.take_finding_slot`.
    over_cap = tally.findings_over_cap if tally is not None else 0
    if not findings and not over_cap:
        out = "✓ conflictscan clean — no conflict markers found."
        return out + ("\n" + tally.summary() if tally is not None else "")
    lines = [f"✗ conflictscan: {len(findings) + over_cap} finding(s) — commit blocked."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.match!r} → {f.detail}")
    if over_cap:
        lines.append(f"  …and {over_cap} more finding(s), counted but not listed "
                     f"(past the {MAX_MATERIALIZED_FINDINGS}-finding memory cap).")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A real conflict marker: finish resolving the merge and remove it —")
    lines.append("  there is no correct commit that keeps one.")
    lines.append(f"  A deliberate quote (docs *about* conflict markers): append "
                 f"'<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .conflictscanignore.")
    lines.append("  A marker with no reason exempts nothing.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="conflictscan",
        description="Check that no unresolved merge-conflict marker reaches "
                    "a commit.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--root", default=".",
                    help="repo root for relative paths/.conflictscanignore")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"conflictscan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    tally = Tally()

    if args.staged:
        try:
            staged = staged_added_lines()
        except subprocess.CalledProcessError as e:
            print(f"conflictscan: git diff failed: {e}", file=sys.stderr)
            return 2
        # An ABSOLUTE path in --staged mode matches no repo-relative prefix
        # git reports, so the filter silently empties and the scan covers
        # nothing while still exiting 0 — the same silent-success class
        # `secretscan`/`linkscan` already close. Refuse it rather than pass.
        absolute = [p for p in args.paths if Path(p).is_absolute()]
        if absolute:
            print(f"conflictscan: --staged needs repo-relative path(s), got "
                  f"absolute: {', '.join(absolute)}\n"
                  "  git lists staged paths relative to the repo root, so an "
                  "absolute path matches nothing\n"
                  "  and the scan would pass while covering nothing. Pass e.g. "
                  "'src/' instead.", file=sys.stderr)
            return 2
        prefixes = tuple(p.rstrip("/") + "/" for p in args.paths)
        if prefixes:
            staged = {path: text for path, text in staged.items()
                      if path.startswith(prefixes) or path in args.paths}
        globs = load_ignore_globs(root)
        findings = []
        for path, text in staged.items():
            if _ignored(path, globs):
                tally.files_by_glob += 1
                continue
            findings.extend(scan_text(path, text, tally))
    else:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = [(root / p) if not Path(p).is_absolute() else Path(p)
                   for p in (args.paths or [str(root)])]
        missing = [str(p) for p in targets if not p.exists()]
        if missing:
            # A typo'd path scanning nothing must never read as a clean pass.
            print(f"conflictscan: path does not exist: {', '.join(missing)}",
                  file=sys.stderr)
            return 2
        try:
            findings = scan_paths(targets, root, tally)
        except OSError as e:
            print(f"conflictscan: cannot read {e.filename}: {e.strerror}",
                  file=sys.stderr)
            return 2

    if args.json:
        print(json.dumps({
            "clean": not findings and not tally.findings_over_cap,
            "findings": [asdict(f) for f in findings],
            "findings_over_cap": tally.findings_over_cap,
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
            },
        }, indent=2))
    else:
        print(render_human(findings, tally))

    return 1 if (findings or tally.findings_over_cap) else 0


def _selftest() -> int:
    """Minimal smoke test so `conflictscan --selftest` proves the engine on
    any box, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="conflictscan-self-"))
    (tmp / "docs").mkdir()
    (tmp / "docs" / "broken.md").write_text(
        "# Records\n\n"
        "- entry A\n"
        "<<<<<<< HEAD\n"                                  # opener, flagged
        "- entry B\n"
        "=======\n"                                        # separator, flagged (in-conflict)
        "- entry C\n"
        ">>>>>>> deadbeef (branch)\n"                       # closer, flagged
        "- entry D\n",
        encoding="utf-8",
    )
    (tmp / "docs" / "heading.md").write_text(
        "Legend\n"
        "=======\n"                                        # setext underline, clean (no opener)
        "\n"
        "body text\n",
        encoding="utf-8",
    )
    (tmp / "docs" / "diff3.md").write_text(
        "<<<<<<< HEAD\n"
        "- ours\n"
        "||||||| merged common ancestors\n"                # diff3 base, flagged (in-conflict)
        "- base\n"
        "=======\n"
        "- theirs\n"
        ">>>>>>> branch\n",
        encoding="utf-8",
    )
    (tmp / "docs" / "quoted.md").write_text(
        "The three markers — `<<<<<<< HEAD`, `=======`, `>>>>>>> sha` — read "
        "inline here, so none of them starts a line and nothing fires.\n",
        encoding="utf-8",
    )
    (tmp / "docs" / "allowed.md").write_text(
        "<<<<<<< HEAD  <!-- conflictscan:allow: selftest fixture -->\n",
        encoding="utf-8",
    )
    findings = scan_paths([tmp / "docs"], tmp)
    got = sorted((f.path, f.kind) for f in findings)
    expected = sorted([
        ("docs/broken.md", "opener"),
        ("docs/broken.md", "separator"),
        ("docs/broken.md", "closer"),
        ("docs/diff3.md", "opener"),
        ("docs/diff3.md", "base"),
        ("docs/diff3.md", "separator"),
        ("docs/diff3.md", "closer"),
    ])
    ok = got == expected
    if not ok:
        print(f"FAIL: got {got}, expected {expected}")

    if main(["--root", str(tmp), str(tmp / "docs")]) != 1:
        print("FAIL: findings should exit 1")
        ok = False
    clean = tmp / "clean"
    clean.mkdir()
    (clean / "ok.md").write_text("# OK\n\nLegend\n=======\n\nnothing open here.\n")
    if main(["--root", str(tmp), str(clean)]) != 0:
        print("FAIL: a clean scan (setext heading, no opener) should exit 0")
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
        print(f"conflictscan: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

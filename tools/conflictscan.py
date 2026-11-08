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
It has no `--warn` flag and no advisory form for the conflict markers; see the
module's exit-code contract below (the one advisory tier is the tool-markup
shape, further down).

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

A FIFTH SHAPE, ADVISORY — TOOL-CALL MARKUP (roadmap `320/490`, filed by a
child 2026-10-02). Files written with the harness's file-write tool sometimes
end in the call's own closing markup, saved into the body: a last line of just
the content parameter's closing tag, then one of just the invoke block's. It
corrupts a record, a doc or an agent memory silently, and no scanner saw it.
Flagged, anchored at column 0: a line that is exactly that closing tag or the
invoke block's (an allow-marker may trail it), or one that starts with an
opening `invoke name=` or `parameter name=` tag. This is the scanner's second
response, the advisory tier `secretscan` and `licenscan` already use: reported
and counted (`conflictscan advisory: N finding(s) — reported, not blocking.`,
read by `tools/floor.py` onto the board) but NEVER gating, because the estate
holds real, frozen instances this scan had not met, and a blocking rule would
red a child on its next CI run for a file it may not touch. Everything above
about the four conflict shapes is unchanged and still blocks. The flip to
blocking is one edit (the `blocks=False` arguments in
`_tool_markup_finding`) once the estate is clean. A frozen record that carries the leak is exempted by a
reasoned glob in `.conflictscanignore`, never rewritten. Exemption routes are
the shared ones: the per-line allow-marker and the ignore glob.

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
  0  clean, or advisory (tool-markup) findings only — reported, never a gate
  1  conflict-marker findings — the commit is blocked
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
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402
import allowmarker  # noqa: E402
import report  # noqa: E402

# A line carrying this marker is intentionally exempt from the one finding it
# could otherwise produce. Keep the reason on the same line so the exemption
# is self-documenting and greppable, same contract as the sibling scanners.
ALLOW_MARKER = "conflictscan:allow"

ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER)


def parse_allow(line: str) -> bool:
    """True if the line carries a REASONED allow-marker.

    Like `wrapscan`, this scanner has exactly one rule per line (is this line
    a conflict marker, in the context read so far) — there is no sub-kind to
    scope the marker to, and inventing one would be ceremony, not narrowness
    (`method/GUARDS.md`, rule a). A marker with no reason does not exempt
    (rule c)."""
    return allowmarker.present(ALLOW_RX, line)


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
    # The advisory tier's share of the same budget (see TOOL MARKUP below):
    # findings past the cap that would not have blocked.
    advisory_over_cap: int = 0
    _materialized: int = field(default=0, repr=False, compare=False)

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def take_finding_slot(self, blocks: bool = True) -> bool:
        """True if a finding may still be fully materialized (built and
        held); False once the run-wide cap is reached, in which case the
        caller counts it via `findings_over_cap` (blocking) or
        `advisory_over_cap` instead of building a `Finding` for it."""
        if self._materialized < MAX_MATERIALIZED_FINDINGS:
            self._materialized += 1
            return True
        if blocks:
            self.findings_over_cap += 1
        else:
            self.advisory_over_cap += 1
        return False

    def note_marker(self, kind: str) -> None:
        self.by_marker[kind] = self.by_marker.get(kind, 0) + 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        return report.suppressed_line(
            [f"{self.marker_total} by allow-marker",
             f"{self.files_by_glob} file(s) by .conflictscanignore",
             report.cap_part(self.findings_over_cap + self.advisory_over_cap,
                             MAX_MATERIALIZED_FINDINGS)],
            breakdown=self.by_marker)


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

# TOOL MARKUP (roadmap `320/490`). The harness's file-write call sometimes
# saves its own closing markup into the body of the file it writes: a last
# line that is just the closing tag of the content parameter, then the closing
# tag of the invoke block. The same leak can carry an opening line of a
# call. Three shapes, all anchored at column 0:
#   * a CLOSING line: `</content>` or `</invoke>` and nothing else (an
#     allow-marker may trail it, since that is the only way a doc that quotes
#     the line on purpose can say so);
#   * an OPENING line starting `<invoke name=`;
#   * an OPENING line starting `<parameter name=`.
# ADVISORY BY CONSTRUCTION, for now: the estate holds real instances of the
# leak (frozen records in more than one repo) that no scan has met, so a
# blocking rule would red a child on its next CI run for a file it may not
# touch. It uses the scanner's second response (`Finding.blocks` False): the
# finding is reported, never gates, and its count reaches the board through
# `floor.py`'s advisory-count read, as `secretscan`'s and `licenscan`'s do.
# The flip to blocking is one line (`blocks=True` at the call site) once the
# estate is clean. Unlike a merge-conflict marker this has no
# open-region state: a stray line is a finding wherever it is.
TOOL_MARKUP_KIND = "tool-markup"
TOOL_CLOSE_RX = re.compile(r"^</(?:content|invoke)>(?P<rest>.*)$")
TOOL_OPEN_RX = re.compile(r"^<(?:invoke|parameter) name=")
ADVISORY_COUNT_PREFIX = "conflictscan advisory:"


def _strip_cr(line: str) -> str:
    """Drop one trailing `\\r`, so a CRLF-saved file's separator line (which
    various readers can leave as `'=======\\r'` after an LF-only split)
    still compares equal to the canonical seven-`=` shape."""
    return line[:-1] if line.endswith("\r") else line


@dataclass
class Finding:
    path: str          # the flagged file (repo-relative)
    line: int
    kind: str           # "opener" | "closer" | "base" | "separator" | "tool-markup"
    match: str          # the matched line, as written (trimmed for length)
    detail: str        # human hint at the fix
    blocks: bool = True  # False: advisory tier — reported, never gates


def _excerpt(line: str) -> str:
    stripped = line.rstrip("\r\n")
    return stripped if len(stripped) <= 100 else stripped[:97] + "..."


def advisory_count_line(n: int) -> str:
    """The one line that always says how many advisory findings this run made,
    zero included, so a count that vanishes is a defect somebody can see
    (the reasoning is `secretscan.advisory_count_line`'s; `floor.py` reads
    this line off the run)."""
    return f"  {ADVISORY_COUNT_PREFIX} {n} finding(s) — reported, not blocking."


def _tool_markup_finding(path: str, lineno: int, window: str,
                         is_final_window: bool) -> "Finding | None":
    m = TOOL_CLOSE_RX.match(window)
    if m is not None and is_final_window:
        rest = m.group("rest")
        # Bare (`</content>` with only whitespace after it) or carrying the
        # allow-marker's name — which parse_allow then exempts if reasoned.
        if not rest.strip() or ALLOW_MARKER in rest:
            return Finding(
                path, lineno, TOOL_MARKUP_KIND, _excerpt(window),
                "the write tool's closing markup saved into the file — "
                "delete the line, and check the file's tail for more",
                blocks=False)
    if TOOL_OPEN_RX.match(window):
        return Finding(
            path, lineno, TOOL_MARKUP_KIND, _excerpt(window),
            "a tool call's opening markup saved into the file — delete "
            "the line, and check the lines around it", blocks=False)
    return None


def _record(findings: list[Finding], tally: "Tally | None", finding: Finding) -> None:
    """Append `finding` unless the run-wide materialization cap (020/380,
    `MAX_MATERIALIZED_FINDINGS`) has been reached — in which case
    `tally.take_finding_slot` has already counted it. Same choke-point shape
    as `secretscan._record` (020/370)."""
    if tally is None or tally.take_finding_slot(finding.blocks):
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
    return _tool_markup_finding(path, lineno, window, is_final_window), in_conflict


def scan_lines(path: str, numbered_lines: "list[tuple[int, str]]",
               tally: "Tally | None" = None) -> list[Finding]:
    """Walk `(real line number, text)` pairs in order, tracking whether we are
    inside what looks like an open conflict region (an OPENER seen with no
    CLOSER since) — see the module docstring's "THE `=======` AMBIGUITY"
    section for why SEPARATOR/BASE are gated on this state and OPENER/CLOSER
    are not.

    The staged-diff caller's shape (115/300): a staged diff's added lines are
    not consecutive lines of the file, so each carries its real line number
    from `report.staged_added` and a finding is reported at THAT line. The
    open-conflict state still runs through the added lines in order, exactly
    as before: only the number a finding is reported at changed.
    `_scan_file` below is the streaming shape the whole-tree walk uses."""
    findings: list[Finding] = []
    in_conflict = False
    for lineno, raw in numbered_lines:
        finding, in_conflict = _line_finding(path, lineno, raw, True, in_conflict)
        if finding is None:
            continue
        if parse_allow(raw):
            if tally is not None:
                tally.note_marker(finding.kind)
            continue
        _record(findings, tally, finding)
    return findings


def scan_text(path: str, text: str, tally: "Tally | None" = None) -> list[Finding]:
    """Scan a whole text blob, numbering its lines from 1 — the whole-blob
    convenience wrapper over `scan_lines` (the selftest and the test suite
    use it); the staged plane passes real line numbers to `scan_lines`."""
    return scan_lines(path, list(enumerate(text.splitlines(), start=1)), tally)


def _looks_binary(data: bytes) -> bool:
    """Matches `secretscan`'s/`leakscan`'s own heuristic exactly: a NUL byte
    in the first 8KiB is not valid text in any encoding this repo writes, and
    a binary container (an image, a compiled artefact) cannot carry a
    line-anchored text marker in any way this scanner could act on."""
    return b"\x00" in data[:8192]


IgnoreFileError = allowmarker.IgnoreFileError


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.conflictscanignore`, each of which MUST carry a stated reason.
    Single-sourced (115/080 part 2) in `tools/allowmarker.py`; this
    scanner supplies only its own ignore-file name."""
    return allowmarker.load_ignore_globs(root, ".conflictscanignore")


def _ignored(rel: str, globs: list[str]) -> bool:
    return allowmarker.ignored(rel, globs)


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
            # Walk an offset forward and cut `pending` once per chunk. The
            # old `pending = pending[nl + 1:]` per line re-copied the whole
            # remainder for every line: quadratic in lines-per-chunk
            # (110/140; linkscan's reader had the same shape, 110/120).
            start = 0
            while True:
                nl = pending.find("\n", start)
                if nl == -1:
                    break
                yield lineno, pending[start:nl], True
                start = nl + 1
                lineno += 1
            if start:
                pending = pending[start:]
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


def staged_added_lines() -> dict[str, list[tuple[int, str]]]:
    """Path → [(real file line number, added-line text), ...] of the staged
    diff. Scans only what a commit would introduce (the pre-commit hot path),
    not the whole tree — identical shape to `secretscan.staged_added_lines`.

    The line number is the line's place in the file the commit produces, not
    its place among the file's added lines (115/300): a marker staged on line
    5 of a file whose lines 1-4 are unchanged is reported at 5, not at 1.

    `R` is in the diff filter deliberately (matches `secretscan`'s own
    review-B4 reasoning): a renamed-and-edited file's added lines can carry a
    conflict marker exactly as a modified file's can, and `ACM` alone would
    silently skip them."""
    # `report.staged_added` reads the diff by its structure (115/280): the
    # path of a quoted name is undone there (115/260), and an added line that
    # merely looks like a header (`++ b/x` prints as `+++ b/x`) can neither
    # move attribution nor be dropped from the scan.
    files: dict[str, list[tuple[int, str]]] = {}
    for path, lineno, text in report.staged_added():
        files.setdefault(path, []).append((lineno, text))
    return files


def _render_advisory(advisory: list[Finding], over_cap: int = 0) -> list[str]:
    """The advisory detail block. Shares no wording with the blocking block —
    not the head, not "commit blocked" — so a reader skimming two adjacent
    lists can tell which one stopped the commit, and it states its own
    exit-code consequence rather than leaving it to be inferred."""
    lines = ["",
             "🟡 ADVISORY FINDINGS — none of these blocked anything.",
             "   Tool-call markup saved into a file's body (roadmap 320/490): "
             "a leak of the",
             "   write tool's own syntax into a record, doc or memory."]
    for f in sorted(advisory, key=lambda x: (x.path, x.line)):
        lines.append(f"     {f.path}:{f.line}  [advisory/{f.kind}] "
                     f"{f.match!r} → {f.detail}")
    if over_cap:
        lines.append(report.over_cap_line(over_cap, MAX_MATERIALIZED_FINDINGS,
                                          noun="advisory finding(s)", indent="   "))
    lines.append("   A real leak: delete the line. A frozen record that must "
                 "stay as written:")
    lines.append(f"   a reasoned glob in .conflictscanignore. A doc quoting the "
                 f"markup on purpose:")
    lines.append(f"   '{ALLOW_MARKER}: <reason>' on the same line (a comment "
                 f"after the tag).")
    return lines


def render_human(findings: list[Finding], tally: "Tally | None" = None) -> str:
    # 020/380 — a capped run's TRUE total lives on the tally, never on
    # `len(findings)`: everything past `MAX_MATERIALIZED_FINDINGS` was
    # counted there instead of being built as a `Finding` at all — see
    # `Tally.take_finding_slot`.
    blocking = [f for f in findings if f.blocks]
    advisory = [f for f in findings if not f.blocks]
    over_cap = tally.findings_over_cap if tally is not None else 0
    advisory_over = tally.advisory_over_cap if tally is not None else 0
    count_line = advisory_count_line(len(advisory) + advisory_over)
    if not blocking and not over_cap:
        out = report.clean_head("conflictscan", "no conflict markers found.")
        out += ("\n" + tally.summary() if tally is not None else "")
        out += "\n" + count_line
        if advisory:
            out += "\n" + "\n".join(_render_advisory(advisory, advisory_over))
        return out
    lines = [report.findings_head("conflictscan", len(blocking) + over_cap,
                                  tail=" — commit blocked.")]
    for f in sorted(blocking, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.match!r} → {f.detail}")
    if over_cap:
        lines.append(report.over_cap_line(over_cap, MAX_MATERIALIZED_FINDINGS))
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append(count_line)
    lines.append("\n  A real conflict marker: finish resolving the merge and remove it —")
    lines.append("  there is no correct commit that keeps one.")
    lines.append(f"  A deliberate quote (docs *about* conflict markers): append "
                 f"'<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .conflictscanignore.")
    lines.append("  A marker with no reason exempts nothing.")
    if advisory:
        lines.extend(_render_advisory(advisory, advisory_over))
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="conflictscan",
        description="Check that no unresolved merge-conflict marker reaches "
                    "a commit.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo, or --staged). "
                         "With --staged, repo-root-relative paths in git's own "
                         "spelling and case ('.' is the whole diff); one git "
                         "does not know is refused (exit 2)")
    ap.add_argument("--staged", action="store_true",
                    help="scan only lines added in the git staging area (pre-commit hook)")
    ap.add_argument("--root", default=".",
                    help="repo root for relative paths/.conflictscanignore "
                         "(with --staged it must be the repo you run in)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return report.quiet_selftest("conflictscan", _selftest)

    root = Path(args.root).resolve()
    rc = report.refuse_missing_root("conflictscan", root, args.root)
    if rc is not None:
        return rc

    tally = Tally()

    if args.staged:
        rc = report.refuse_other_repo("conflictscan", root)
        if rc is not None:
            return rc
        try:
            staged = staged_added_lines()
        except report.STAGED_DIFF_FAILURES as e:
            return report.git_diff_failed("conflictscan", e)
        # An ABSOLUTE path in --staged mode matches no repo-relative prefix
        # git reports, so the filter silently empties and the scan covers
        # nothing while still exiting 0 — the same silent-success class
        # `secretscan`/`linkscan` already close. Refuse it rather than pass.
        # `report.scope_staged` also normalises the spelling (`.`, `./x`),
        # refuses one that escapes the repo, and lets git resolve what each
        # positional names, refusing one git does not know (115/360, 160/950).
        rc, staged = report.scope_staged("conflictscan", staged, args.paths, "src/")
        if rc is not None:
            return rc
        globs = load_ignore_globs(root)
        findings = []
        for path, lines in staged.items():
            if _ignored(path, globs):
                tally.files_by_glob += 1
                continue
            findings.extend(scan_lines(path, lines, tally))
    else:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = report.resolve_targets(root, args.paths or [str(root)])
        rc = report.refuse_missing_paths("conflictscan", targets)
        if rc is not None:
            return rc
        try:
            findings = scan_paths(targets, root, tally)
        except OSError as e:
            return report.cannot_read("conflictscan", e)

    blocking_total = (sum(1 for f in findings if f.blocks)
                      + tally.findings_over_cap)
    advisory_total = (sum(1 for f in findings if not f.blocks)
                      + tally.advisory_over_cap)
    if args.json:
        print(json.dumps({
            # `clean` keeps its meaning — nothing found at all — and
            # `blocked` tracks the exit code, as in `secretscan`'s output.
            "clean": not findings and not blocking_total and not advisory_total,
            "blocked": bool(blocking_total),
            "counts": {"blocking": blocking_total, "advisory": advisory_total},
            "findings": [asdict(f) for f in findings],
            "findings_over_cap": tally.findings_over_cap,
            "advisory_over_cap": tally.advisory_over_cap,
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
            },
        }, indent=2))
    else:
        print(render_human(findings, tally))

    return report.exit_code(blocking_total)


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
    (tmp / "docs" / "leak.md").write_text(
        "body\n" + "</" + "content>\n" + "</" + "invoke>\n",       # advisory
        encoding="utf-8")
    findings = [f for f in scan_paths([tmp / "docs"], tmp) if f.blocks]
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

    advisory = [f for f in scan_paths([tmp / "docs" / "leak.md"], tmp)]
    if [f.kind for f in advisory] != ["tool-markup"] * 2 \
            or any(f.blocks for f in advisory):
        print(f"FAIL: tool markup should be two advisory findings, got {advisory}")
        ok = False

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
    return report.guarded_main("conflictscan", _main, argv, (IgnoreFileError,))


if __name__ == "__main__":
    sys.exit(main())

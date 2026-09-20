#!/usr/bin/env python3
"""stampscan — the mechanical check for inlined-floor / child-template
restatement drift against its canonical parent (stamp-drift).

The rule (2026-07-22 invariant-candidates review, seam S4): where a child repo
or template INLINES a floor/pull-quote of canonical doctrine, the inlined
block must EQUAL the parent's canonical text — or legitimately NARROW it (a
documented subset, never a silent one) — never silently DROP or CONTRADICT an
item. The corpus already paid for this class without a scanner: `create-repo
C3` (nothing kept the stamped block equal to PROPAGATION's canonical text),
`method-layer P1` (an inlined floor silently dropped "new trust surfaces"),
`foundation Q2` (a pull-quote listed 4 of 6 floor items) — three real findings
a human reviewer had to catch by eye, each time.

REVIEWED, WIRED ADVISORY IN ATELIER ONLY. The first-of-kind cold pass ran
2026-07-26 (`docs/reviews/2026-07-26-2215-stampscan-s4-cold.md`,
PASS-WITH-FINDINGS: 3 MAJOR, 3 MINOR, 1 NIT) and the principal ruled its
counsel built on 2026-08-04. This file carries the three stated wiring
preconditions — ST1 (code-context-blind marker recognition, fixed below),
ST1's `.stampscanignore` companion at the repo root, and ST2 (narrowing to
nothing is drift) — which is exactly what the reviewer's step 1 asks for:
`--warn` in atelier's OWN `ci.yml` as a hand step, like pathscan's.

It is deliberately NOT in the `floor.py` registry, NOT in the reusable
`floor.yml`, and NOT in the pre-commit hook. Registry wiring reaches every
child (ADR 0008 — enforcement propagates by call), and ST3 is still open:
the template's stamp pins `source=docs/method/PROPAGATION.md`, a path that
exists only in atelier, so any scaffolded child that ran this scanner would
exit 2. The child-side resolution story must also be PIN-aware (a child
pinned at `atelier@<SHA>` may lawfully differ from atelier@main), and
`create-repo` must learn the markers are load-bearing scaffold content.
Blocking is a separate, later ruling after an advisory soak — wrapscan's
and datescan's rollout discipline, unchanged.

THE NEW MECHANISM — a stamp/region marker pair:

  A CHILD file (a template, a repo's CLAUDE.md — anything that inlines a
  floor/pull-quote) wraps the inlined block with:

      <!-- stamp:begin source=<repo-relative-path> region=<name> -->
      ...the inlined block, verbatim...
      <!-- stamp:end -->

  and, optionally, when the child DELIBERATELY carries less than the full
  canonical region (a documented, legitimate narrowing — e.g. a repo that
  genuinely doesn't need one floor concern), the begin marker adds a
  `narrow=<reason>` attribute:

      <!-- stamp:begin source=docs/method/PROPAGATION.md region=floor narrow=repo-x-omits-estate-pointer -->

  The CANONICAL PARENT names the region the stamp points at with its own
  begin/end pair, anchored at the region's name (not "stamp" — the parent
  is not itself a stamp of anything):

      <!-- floor:begin -->
      ...the canonical text...
      <!-- floor:end -->

  Both marker pairs are HTML comments — invisible in rendered Markdown, and
  in this repo's own usage placed OUTSIDE any fenced illustration of the
  block (see FENCED-PRESENTATION STRIPPING below), so adding them never
  changes one visible character of the text they bracket.

THE CHECK, per stamped block found in a scanned file:

  1. Extract the block's payload — every line strictly between its
     `stamp:begin`/`stamp:end` markers.
  2. Resolve `source` against `--root` and read it; resolve `region` in it
     by finding `<!-- <region>:begin -->` / `<!-- <region>:end -->` and
     extracting the lines strictly between them (see FENCED-PRESENTATION
     STRIPPING). Either failing to resolve is a FAIL-SAFE CONFIG ERROR
     (exit 2), never a silent pass — a stamp pointing nowhere is worse than
     no stamp at all. The resolved `source` must also sit INSIDE `--root`
     (see SOURCE CONFINEMENT below); one that escapes is the same class of
     config error.
  3. Compare payload to canonical region, per line, trailing whitespace
     ignored and a leading/trailing run of BLANK lines trimmed from each
     side first (a lone separator line touching a delimiter is formatting,
     not content — see `_trim_blank_boundary`; nothing else is normalised —
     no case-folding, no punctuation smoothing; this is a deliberately
     strict, honest comparison otherwise):
       - EQUAL                                          -> CLEAN (identical)
       - not equal, but the child's lines are an ORDERED SUBSEQUENCE of the
         canonical lines (obtainable by deleting lines only, never
         reordering or altering one) AND the stamp declared `narrow=` ->
         CLEAN, but NOTED as a legitimate narrow (reported, not a finding)
       - the same ordered-subsequence shape WITHOUT a `narrow=` declaration
         -> DRIFT, RED — mechanically this looks identical to a legitimate
         narrow (dropping is dropping), so the ONLY signal that separates
         "legitimately narrowed" from "silently dropped" is whether the
         author declared the narrowing. Undeclared = silent = red. This is
         the deliberate, load-bearing reading of the rule's word
         "legitimately" — see STATED RESIDUAL, this is a genuinely new
         judgement call this scanner makes, flagged for reviewer scrutiny.
         EXCEPT for the one canonical FLOOR region (see FLOOR IS VERBATIM,
         NEVER NARROWED below): there, `narrow=` never earns a pass.
       - anything else (an added line, a reordered line, a reworded line —
         any deviation that ISN'T obtainable by pure deletion) -> DRIFT, RED,
         REGARDLESS of a `narrow=` declaration — declaring narrow intent
         does not excuse an actual addition or contradiction; only a genuine
         subset counts as "legitimate".
       - one BOUNDARY case sits above all of the above: an EMPTY payload
         (0 of N canonical lines kept, N > 0) is DRIFT, RED, regardless of
         a `narrow=` declaration. Narrowing to nothing is not a narrowing —
         it is vacating the floor, and one token would otherwise delete a
         whole inlined floor while the scanner reported clean (2026-07-26
         cold pass ST2; ruled by the principal 2026-08-04, so the doctrine
         act is recorded rather than inferred from a subsequence identity).
         A genuine PARTIAL narrow — one or more canonical lines kept, in
         order — still passes exactly as before.

FLOOR IS VERBATIM, NEVER NARROWED (board 115/030, principal's ruling
2026-09-19: "Floor copy verbatim"): the one canonical block this applies to —
`source=docs/method/PROPAGATION.md region=floor`, the inlined atelier safety
floor — carries no legitimate narrowing at all, by identity rather than by
name. It is identified by the (`source`, `region`) PAIR, not by the region
name "floor" alone: this test suite (and a real child scaffold) is free to
name an unrelated region "floor" too, and doing so must not accidentally
trip the floor-specific rule. Only the one live pairing counts.

For that pairing, a `narrow=` declaration on an otherwise-genuine ordered
subset is DRIFT, RED, exactly like an undeclared silent drop — the
declaration buys nothing here, because the doctrine this scanner enforces no
longer recognises a legitimate narrowing of the floor (PROPAGATION.md drops
"may compress" for this region specifically). A byte-equal copy still passes
CLEAN; every other drift shape (empty, reworded, reordered, added) was
already RED before this change and stays RED. Non-floor regions are
completely unaffected — their `narrow=` keeps today's behaviour exactly.

FENCED-PRESENTATION STRIPPING: a canonical region is sometimes shown inside a
fenced code block in its own doc (PROPAGATION.md presents the floor block
this way, as a copy-paste illustration) — the fence itself is presentational,
not part of the compared text. If the FIRST line of an extracted canonical
region is a bare fence-open (```` ``` ```` or `~~~`, optionally with a info
string) and the LAST line is a bare matching fence-close, both are stripped
before comparison. Honest limit: this is a first/last-line convention, not a
real Markdown fence parser — a region whose real content happens to start or
end with a line that merely LOOKS like a fence delimiter would be
mis-stripped. Accepted for a first-of-kind tool; the one live pair this
change wires (PROPAGATION.md's floor region) exercises exactly this path.

CODE-CONTEXT BLINDNESS, AND ITS FIX (2026-07-26 cold pass ST1/ST7): markers
are hunted only OUTSIDE fenced code blocks and outside inline `code spans`,
exactly as datescan/linkscan/pathscan/wrapscan already do — because a document
that merely DOCUMENTS this syntax is not a stamp, and reading it as one made
the scanner unwireable (a stray/unpaired marker is a config error, and
`--warn` never suppresses one, so any doc about stampscan reddened the whole
floor). Two properties make this safe:

  * The stripping is for RECOGNITION ONLY. A stripped line still enters a
    stamp's payload VERBATIM, so a stamped block whose content contains a
    fenced example or a code span is compared character for character,
    unaffected. Only the question "is this line a marker?" sees the
    stripped view.
  * BOTH markers are now anchored at line start (`stamp:end` was previously
    a bare `.search()` anywhere on a line — forced by a placement compromise
    in `docs/build/templates/CLAUDE.md`, which closed its stamp inline on a
    `---` divider to avoid disturbing a frozen verbatim slice in
    `tools/test_templates.py`. ST7 took the cleaner fix: `template_block()`
    now strips marker lines, the template's `stamp:end` moved to its own
    line, and the regex re-anchored. That single change removes the widest
    contributor to the stray-end class — an inline-code MENTION of the end
    marker used to trip it.)

NAMED RESIDUAL of that fix: a RAW, line-start HTML-comment marker sitting in
bare prose — not fenced, not in a code span — is still read as a live marker,
because at that point it is indistinguishable from one. This is defensible
rather than merely tolerated: rendered Markdown HIDES a raw HTML comment, so
genuine documentation of the syntax has to use a code span or a fence to be
visible to a reader at all. A raw marker in prose is invisible prose — the
failure mode is self-correcting for anyone who looks at the rendered page.
The repo-level companion is `.stampscanignore`, which nets the stores that
quote probe material raw by nature (`docs/reviews/`, `.claude/worktrees/`).

SOURCE CONFINEMENT (2026-07-26 cold pass ST4): a resolved `source=` must sit
inside `--root`. `root / source` alone accepts `../` traversal, and pathlib
silently DISCARDS `root` for an absolute right-hand side — so a crafted
stamped document could aim the scanner at any file on the machine and get one
line of it echoed back in the drift hint. Out-of-root now fails as a config
error (exit 2), matching the fail-safe posture the tool takes everywhere else.

EXEMPTIONS — same shape as every sibling scanner:

  * THE ALLOW MARKER. A line carrying `stampscan:allow: <reason>` anywhere
    inside a stamped block (the begin line, the payload, or the end line)
    exempts that WHOLE BLOCK from comparison — reported as "skipped", not
    counted toward clean or drift. Tightened to the same word-boundary +
    non-empty-reason contract datescan uses (DSR8): a bare mention of the
    marker text, or an empty reason, does not exempt.
  * THE IGNORE FILE. A `.stampscanignore` glob at the scan root exempts a
    path wholesale from being scanned FOR stamped blocks (it does not affect
    that path's use as a canonical `source=` target — a file can be a
    canonical source without ever being scanned for stamps of its own).

MALFORMED STAMPS are a FAIL-SAFE CONFIG ERROR (exit 2), not a silent skip: a
`stamp:begin` with no matching `stamp:end` before end-of-file, a nested
`stamp:begin` before its predecessor closed, or a stray `stamp:end` with no
open `stamp:begin` are all reported and gate the exit code — a scanner that
silently ignored a malformed marker would be worse than one that never ran.

STATED RESIDUAL, HONESTLY (do not round this to "solved"):

  * The narrow-vs-drop distinction rests entirely on the author's own
    `narrow=` declaration — the scanner trusts the attribute's mere PRESENCE
    (any non-empty token), the same shallow-trust posture every sibling
    `<name>scan:allow:` marker already takes. It does not, and cannot,
    verify the declared reason is actually true.
  * Comparison is per-line and literal (trailing whitespace ignored only) —
    a reworded-but-equivalent line reads as drift, and a semantically
    contradictory line reads as drift too, for the identical mechanical
    reason (neither is byte-equal nor a pure subsequence). The scanner
    cannot and does not distinguish "reworded" from "contradicted" — both
    are reported as the same `drift` kind; only a human reading the diff
    can tell which.
  * The ordered-subsequence check is a standard greedy two-pointer match,
    and it is EXACT for subsequence membership — duplicate lines included.
    (An earlier version of this residual claimed a duplicate line "could be
    consumed by the wrong occurrence in a pathological case". That was
    wrong: greedy leftmost matching never rejects a genuine subsequence, and
    the cold pass's adversarial duplicate probes all returned correct
    answers. Erring safe does not make an overstated residual true —
    2026-07-26 cold pass ST6a.) What the check genuinely does not carry is
    WHICH occurrence of a duplicated line matched, so where a region repeats
    a line the drift hint below may name a different occurrence than a human
    would pick. The verdict is unaffected.
  * A fenced code block that OPENS inside a stamped payload and never closes
    swallows the rest of the file for marker recognition (the sibling
    scanners' shared fence convention), so the block's real `stamp:end` reads
    as never-arriving — an unterminated-stamp config error. That fails safe
    and loudly, which is the right direction, but the message will name the
    stamp rather than the unclosed fence that caused it.
  * A `region` name is resolved by its FIRST matching begin/end pair in the
    canonical source; a source file with two regions sharing one name is
    unsupported (first one wins, silently) — not exercised today, named so
    it isn't rediscovered as a surprise.
  * This scanner reports drift at whole-block granularity with a short
    diagnostic hint (line counts, one example offending line), not a full
    unified diff — enough to point a human at the file, not enough to skip
    reading it.
  * Only Markdown (`.md`/`.markdown`) is scanned for stamped blocks by
    default, matching every sibling scanner's default scope.

Exit codes (fail-safe — anything but a clean scan is non-zero, UNLESS --warn
for DRIFT findings specifically; a CONFIG ERROR always exits 2, --warn or
not, matching the sibling scanners' "a broken scan is not a pass"):
  0  clean (every stamp identical, legitimately narrow, or explicitly
     allow-marked); or --warn was given and only drift findings exist
  1  drift finding(s) present, and --warn was NOT given
  2  usage / config error — malformed stamp, unresolvable source or region,
     a source resolving outside --root, bad CLI arguments (NEVER downgraded
     by --warn)

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
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402

# A line carrying this marker (anywhere inside a stamped block) exempts that
# whole block from comparison. Same word-boundary + non-empty-reason
# contract as datescan's DSR8-tightened ALLOW_MARKER_RX — a bare mention or
# an empty reason must not silently exempt.
ALLOW_MARKER = "stampscan:allow"
ALLOW_MARKER_RX = re.compile(r"\b" + re.escape(ALLOW_MARKER) + r":\s*[\w\"\'“‘]")

# Only these extensions are scanned for stamped blocks — matches every
# sibling scanner's MARKDOWN_SUFFIXES.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

# The one canonical floor block (board 115/030, ruled 2026-09-19: "Floor copy
# verbatim") — identified by the (source, region) PAIR, never the region name
# alone. "floor" is also this scanner's own generic example region name
# (see test fixtures and the module selftest), so name-only matching would
# misfire on unrelated test/example stamps that happen to reuse the word.
# Only a stamp pointing at THIS source AND naming THIS region is the real
# inlined atelier safety floor.
FLOOR_SOURCE = "docs/method/PROPAGATION.md"
FLOOR_REGION = "floor"

# Paths never worth walking. Hardcode-skip ONLY names that are never
# human-authored prose — VCS, dependency, and tool-cache dirs (matches the
# sibling scanners).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# The stamp marker pair (child/copy side). `source` and `region` are bare
# tokens (no spaces) — a stated limit (see module header); `narrow`, if
# present, is the LAST attribute and may contain spaces (a short reason),
# captured non-greedily up to the closing `-->`. Anchored at line-start only
# (not end) — deliberately, so an allow-marker comment can trail on the same
# physical line (`... region=floor --> <!-- stampscan:allow: reason -->`),
# matching the house convention that the allow marker's own regex is a bare
# `.search()`, not an exact-line match.
_STAMP_BEGIN_RX = re.compile(
    r"^<!--\s*stamp:begin\s+source=(?P<source>\S+)\s+region=(?P<region>\S+)"
    r"(?:\s+narrow=(?P<narrow>.+?))?\s*-->"
)


def _narrow_of(m: "re.Match[str]") -> str | None:
    """The declared narrow reason, or None. Whitespace-only is None (SD4,
    ruled 2026-08-06): the raw capture could hold a lone space, which read
    as a truthy "declaration" — below even the stated shallow-trust bar of
    "any non-empty token". The marker still parses (so the diagnostics stay
    a clear silent-drop drift, not a confusing stray-end config error);
    only the declaration is void."""
    raw = m.group("narrow")
    if raw is None:
        return None
    return raw.strip() or None
# stamp:end is anchored at line start, exactly like stamp:begin. It used to
# be a bare `.search()` — the one live pair closed its stamp inline on a `---`
# divider so as not to disturb the span a frozen test (tools/test_templates.py
# `template_block()`) sliced verbatim. ST7 (2026-07-26 cold pass) took the
# cleaner fix instead: that test now strips marker lines, so the template's
# stamp:end sits on its own line and this regex can anchor. Search-anywhere was
# the widest single contributor to the stray-end class an inline-code MENTION
# of the marker used to trip (see module header, CODE-CONTEXT BLINDNESS).
_STAMP_END_RX = re.compile(r"^<!--\s*stamp:end\s*-->")

# Fenced-presentation stripping for a CANONICAL REGION (see module header).
# Matches the sibling scanners' own fence regex (`^(`{3,}|~{3,})`), plus an
# optional info string on the opener only (` ```markdown `), and requires a
# bare closer.
_FENCE_OPEN_RX = re.compile(r"^(`{3,}|~{3,})\S*$")

# Fence tracking for MARKER RECOGNITION — the sibling scanners' shared regex
# and pairing rule (datescan/linkscan/wrapscan/pathscan all carry this exact
# pair): a fence closes only on a run of the same character at least as long
# as the opener, with no trailing info string.
_FENCE = re.compile(r"^(`{3,}|~{3,})")


def _region_markers(name: str) -> tuple["re.Pattern[str]", "re.Pattern[str]"]:
    """Build the begin/end regexes for a named canonical region, e.g.
    `<!-- floor:begin -->` / `<!-- floor:end -->`."""
    esc = re.escape(name)
    return (re.compile(rf"^<!--\s*{esc}:begin\s*-->$"),
            re.compile(rf"^<!--\s*{esc}:end\s*-->$"))


def _is_floor_block(block: "StampBlock") -> bool:
    """True only for a stamp naming the one canonical (source, region) pair
    that is the inlined atelier safety floor — see FLOOR IS VERBATIM, NEVER
    NARROWED in the module header. Deliberately a pair match, not a region-
    name match: a generic region also named "floor" elsewhere (this file's
    own test fixtures included) must not be swept in."""
    return block.source == FLOOR_SOURCE and block.region == FLOOR_REGION


@dataclass
class StampBlock:
    path: str          # the file carrying the stamp (repo-relative)
    line: int          # line number of stamp:begin
    source: str        # the canonical source path, as written in the marker
    region: str        # the named region in that source
    narrow: str | None  # the declared narrow reason, if any
    payload: list[str]  # the lines strictly between begin and end
    allow: bool        # True if an allow-marker was found anywhere in block


@dataclass
class Finding:
    path: str
    line: int
    kind: str    # "identical" | "narrow" | "skipped" | "drift"
                 # | "missing-source" | "unconfined-source"
                 # | "missing-region" | "malformed"
    source: str | None
    region: str | None
    detail: str


# ---------------------------------------------------------------- parsing --

def _strip_inline_code(line: str) -> str:
    """Blank out inline `code spans`, preserving the line's length so column
    positions still line up. Identical to datescan's and linkscan's helper —
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


def _content_lines(text: str):
    """Yield `(lineno, raw_line, scan_line)` for every line in `text`.

    `scan_line` is the line as MARKER RECOGNITION should see it: empty inside
    a fenced code block, and with inline `code spans` blanked out elsewhere,
    so a document that merely *documents* the stamp syntax is not read as
    carrying stamps (2026-07-26 cold pass ST1 — the wiring blocker). Fence
    pairing matches datescan/linkscan/wrapscan/pathscan exactly.

    `raw_line` is untouched. Payload accumulation uses it, so a stripped line
    still enters a stamped block VERBATIM and payload comparison is
    unaffected — the stripping decides "is this a marker?", nothing else."""
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
            yield lineno, line, ""
            continue
        if m:
            in_fence = True
            fence_char = m.group(1)[0]
            fence_len = len(m.group(1))
            yield lineno, line, ""
            continue
        yield lineno, line, _strip_inline_code(line)


# Streaming-read tuning (020/380, reusing 020/370's secretscan/spellscan
# shape — see `tools/secretscan.py`'s `_iter_numbered_lines` and
# `tools/spellscan.py`'s `_iter_physical_lines`, duplicated rather than
# imported so this scanner stays copyable alone). Before this fix,
# `scan_paths` read every candidate file WHOLE (`md.read_text()`) and every
# canonical `source=` WHOLE too (`resolve_source`'s `candidate.read_text()`),
# each immediately re-split via `text.splitlines()` inside `_content_lines` —
# the same double-materialization shape secretscan's old `iter_files` and
# spellscan's old `scan_file` carried, so peak memory for ONE file scaled
# with that file's own size, independent of how small the stamped block or
# canonical region inside it actually was. `_MAX_LINE_BYTES` is two-plus
# orders of magnitude past any realistic Markdown line (a stamp marker, a
# doctrine bullet) so no real content is ever truncated; it exists to bound
# the pathological case (one absurd multi-MB "line") to a fixed constant
# instead of letting it scale with the file.
_READ_CHUNK_BYTES = 1 * 1024 * 1024
_MAX_LINE_BYTES = 8 * 1024


def _iter_physical_lines(path: Path, truncated: list[int] | None = None):
    """Yield `(lineno, text)` for every physical line in `path`, reading and
    decoding it in fixed-size chunks so peak memory for ONE file is bounded
    by `_MAX_LINE_BYTES` (plus one read chunk in flight) — independent of the
    file's total size or its longest line. A physical line longer than
    `_MAX_LINE_BYTES` is truncated to that many characters; the excess is
    still READ (so running time stays linear in bytes read) but never held,
    and `truncated` — a mutable counter list, appended to once per
    truncation, matching `iter_markdown`'s own `skipped` counter shape — is
    incremented rather than truncating silently."""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    lineno = 1
    pending = ""
    line_truncated = False

    def feed(text: str):
        nonlocal lineno, pending, line_truncated
        while text:
            nl = text.find("\n")
            piece, text = (text, "") if nl == -1 else (text[:nl], text[nl + 1:])
            room = _MAX_LINE_BYTES - len(pending)
            if room > 0:
                pending += piece[:room]
            if len(piece) > max(room, 0):
                line_truncated = True
            if nl != -1:
                if line_truncated and truncated is not None:
                    truncated.append(1)
                yield lineno, pending
                lineno += 1
                pending = ""
                line_truncated = False

    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(_READ_CHUNK_BYTES)
            if not chunk:
                break
            yield from feed(decoder.decode(chunk))
    tail = decoder.decode(b"", final=True)
    if tail:
        yield from feed(tail)
    if pending or line_truncated:
        if line_truncated and truncated is not None:
            truncated.append(1)
        yield lineno, pending


def _content_lines_from_file(path: Path, truncated: list[int] | None = None):
    """Streaming equivalent of `_content_lines`: same fence-pairing state
    machine, sourced from `_iter_physical_lines` instead of a whole-file
    `text.splitlines()` list (020/380)."""
    in_fence = False
    fence_char = ""
    fence_len = 0
    for lineno, line in _iter_physical_lines(path, truncated):
        stripped = line.lstrip()
        m = _FENCE.match(stripped)
        if in_fence:
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len \
                    and stripped.rstrip() == m.group(1):
                in_fence = False
            yield lineno, line, ""
            continue
        if m:
            in_fence = True
            fence_char = m.group(1)[0]
            fence_len = len(m.group(1))
            yield lineno, line, ""
            continue
        yield lineno, line, _strip_inline_code(line)


def find_stamp_blocks(path: str, text: str) -> tuple[list[StampBlock], list[Finding]]:
    """Parse every `stamp:begin ... stamp:end` pair in `text`. Returns
    (blocks, malformed_findings) — malformed markers (unterminated, nested,
    or a stray end) are reported as `malformed` findings, never silently
    dropped.

    Markers (and the allow marker) are recognised on the CODE-STRIPPED view
    of each line; payloads accumulate the RAW line (see `_content_lines`).

    Whole-text convenience wrapper over `_find_stamp_blocks_from_lines` —
    used by every existing test and by the (in-memory) canonical-region
    resolution path; `find_stamp_blocks_in_file` below is the bounded-memory
    disk variant `scan_paths` uses for a real scan (020/380)."""
    return _find_stamp_blocks_from_lines(path, _content_lines(text))


def find_stamp_blocks_in_file(path: str, file_path: Path,
                              truncated: list[int] | None = None
                              ) -> tuple[list[StampBlock], list[Finding]]:
    """Bounded-memory disk variant of `find_stamp_blocks` (020/380): streams
    `file_path` in fixed-size chunks instead of reading it whole — see
    `_content_lines_from_file`. `path` is the label (repo-relative) reported
    in findings, independent of where `file_path` actually lives."""
    return _find_stamp_blocks_from_lines(
        path, _content_lines_from_file(file_path, truncated))


def _find_stamp_blocks_from_lines(
        path: str, content_lines) -> tuple[list[StampBlock], list[Finding]]:
    """The shared engine underneath `find_stamp_blocks`/`find_stamp_blocks_in_file`
    — identical logic, generic over WHERE the `(lineno, raw_line, scan_line)`
    triples come from."""
    blocks: list[StampBlock] = []
    malformed: list[Finding] = []
    open_stamp: dict | None = None

    for lineno, raw_line, scan_line in content_lines:
        stripped = scan_line.strip()
        m_begin = _STAMP_BEGIN_RX.match(stripped)
        m_end = _STAMP_END_RX.match(stripped)

        if m_begin:
            if open_stamp is not None:
                malformed.append(Finding(
                    path, open_stamp["line"], "malformed", None, None,
                    "stamp:begin at line %d was never closed before another "
                    "stamp:begin at line %d — nested/unterminated stamps are "
                    "not supported" % (open_stamp["line"], lineno)))
            open_stamp = {
                "line": lineno,
                "source": m_begin.group("source"),
                "region": m_begin.group("region"),
                "narrow": _narrow_of(m_begin),
                "payload": [],
                "allow": bool(ALLOW_MARKER_RX.search(scan_line)),
            }
            continue

        if m_end:
            if open_stamp is None:
                malformed.append(Finding(
                    path, lineno, "malformed", None, None,
                    "stray stamp:end with no matching stamp:begin"))
                continue
            blocks.append(StampBlock(
                path=path, line=open_stamp["line"], source=open_stamp["source"],
                region=open_stamp["region"], narrow=open_stamp["narrow"],
                payload=open_stamp["payload"], allow=open_stamp["allow"]))
            open_stamp = None
            continue

        if open_stamp is not None:
            if ALLOW_MARKER_RX.search(scan_line):
                open_stamp["allow"] = True
            open_stamp["payload"].append(raw_line)

    if open_stamp is not None:
        malformed.append(Finding(
            path, open_stamp["line"], "malformed", None, None,
            "stamp:begin at line %d was never closed with a stamp:end "
            "before end of file" % open_stamp["line"]))

    return blocks, malformed


def extract_region(text: str, region: str) -> list[str] | None:
    """Extract the lines strictly between `<!-- <region>:begin -->` and
    `<!-- <region>:end -->` in `text`, stripping a bracketing fenced-code
    presentation if present (see FENCED-PRESENTATION STRIPPING). Returns
    None if the region's begin/end pair does not resolve — a missing region
    is a fail-safe config error, not an empty result.

    Region markers are recognised on the same CODE-STRIPPED view the stamp
    markers use (SD1, ruled 2026-08-06 — the ST1 fix previously covered the
    child side only): a fenced EXAMPLE of the region markers sitting above
    the real region used to bind first, so an identical copy read as drift
    against the example's text. Payload lines are still the RAW lines, so
    a region whose content is presented inside a fence (the live
    PROPAGATION.md shape) extracts verbatim exactly as before.

    Whole-text convenience wrapper over `_extract_region_from_lines` — used
    by every existing test; `extract_region_from_file` below is the bounded-
    memory disk variant `scan_paths` uses for a real scan (020/380): unlike
    this function, it never holds the WHOLE canonical source in memory, only
    the (typically much smaller) payload between the region's markers."""
    return _extract_region_from_lines(_content_lines(text), region)


def extract_region_from_file(path: Path, region: str,
                             truncated: list[int] | None = None) -> list[str] | None:
    """Bounded-memory disk variant of `extract_region` (020/380): streams
    `path` in fixed-size chunks (see `_content_lines_from_file`) instead of
    reading it whole. Peak memory for resolving one region is bounded by the
    REGION's own size (plus one physical line in flight), independent of how
    large the canonical source document containing it is — the source may be
    read to EOF looking for the markers, but nothing before `region:begin`
    is ever held, and reading stops as soon as `region:end` is found."""
    return _extract_region_from_lines(
        _content_lines_from_file(path, truncated), region)


def _extract_region_from_lines(content_lines, region: str) -> list[str] | None:
    """The shared engine underneath `extract_region`/`extract_region_from_file`."""
    begin_rx, end_rx = _region_markers(region)
    start_seen = False
    found_end = False
    payload: list[str] = []
    for _, raw, scan in content_lines:
        stripped = scan.strip()
        if not start_seen:
            if begin_rx.match(stripped):
                start_seen = True
            continue
        if end_rx.match(stripped):
            found_end = True
            break
        payload.append(raw)
    if not start_seen or not found_end:
        return None
    if payload and _FENCE_OPEN_RX.match(payload[0].strip()) \
            and payload[-1].strip().rstrip("`~") == "" \
            and payload[-1].strip()[:1] == payload[0].strip()[:1]:
        payload = payload[1:-1]
    return payload


# ------------------------------------------------------------- comparison --

def _is_ordered_subsequence(sub: list[str], full: list[str]) -> bool:
    """True if `sub` can be obtained from `full` by deleting zero or more
    lines only — never reordering, adding, or altering one. Standard greedy
    two-pointer subsequence check, which is EXACT for membership including
    duplicated lines (see STATED RESIDUAL — the only thing it does not carry
    is which occurrence of a duplicate matched)."""
    it = iter(full)
    return all(x in it for x in sub)


def _normalise(lines: list[str]) -> list[str]:
    """Strip trailing whitespace only — nothing else. Deliberately strict:
    no case-folding, no punctuation smoothing (see module header)."""
    return [ln.rstrip() for ln in lines]


def _trim_blank_boundary(lines: list[str]) -> list[str]:
    """Drop LEADING and TRAILING blank (whitespace-only) lines only — a lone
    separator line immediately inside a delimiter is formatting, not
    content. Applied to both sides before comparison (see module header):
    this is what lets a stamp:end marker share a line with a pre-existing
    structural element (e.g. `---<!-- stamp:end -->`) without the blank
    line ahead of it reading as an "added" line. Honest limit: this only
    trims the OUTER boundary — a blank line in the MIDDLE of a block still
    counts as real content and still drifts if it doesn't match."""
    start = 0
    end = len(lines)
    while start < end and lines[start].strip() == "":
        start += 1
    while end > start and lines[end - 1].strip() == "":
        end -= 1
    return lines[start:end]


def _first_offending_line(child: list[str], parent: list[str]) -> str | None:
    """A short, honest diagnostic hint — NOT a full diff (see STATED
    RESIDUAL). Names the first child line that does not appear anywhere in
    the parent at all, if any; otherwise names the first index where the
    two sequences diverge positionally."""
    parent_set = set(parent)
    for ln in child:
        if ln not in parent_set:
            return f"child line not found in canonical region: {ln!r}"
    for i, (c, p) in enumerate(zip(child, parent)):
        if c != p:
            return f"line {i + 1} differs: child={c!r} canonical={p!r}"
    return None


def evaluate_block(block: StampBlock, canonical: list[str]) -> Finding:
    """Compare one stamped block's payload to its resolved canonical
    region, applying the identical / legitimate-narrow / silent-drop-or-
    drift rules from the module header."""
    if block.allow:
        return Finding(block.path, block.line, "skipped", block.source,
                       block.region, "stampscan:allow — comparison skipped")

    child = _trim_blank_boundary(_normalise(block.payload))
    parent = _trim_blank_boundary(_normalise(canonical))

    if child == parent:
        return Finding(block.path, block.line, "identical", block.source,
                       block.region,
                       f"matches canonical region '{block.region}' "
                       f"({len(parent)} lines)")

    if not child and parent:
        # Narrowing to NOTHING is not a narrowing — it vacates the floor the
        # stamp exists to hold, and one `narrow=` token would otherwise
        # delete a whole inlined floor while this scanner reported clean
        # (2026-07-26 cold pass ST2; ruled 2026-08-04). Checked BEFORE the
        # subsequence branch, because the empty list is vacuously an ordered
        # subsequence of everything.
        return Finding(
            block.path, block.line, "drift", block.source, block.region,
            f"the stamped block is EMPTY — 0 of {len(parent)} canonical "
            f"lines kept" + (f" despite narrow={block.narrow!r}" if block.narrow
                              else "") + ". Narrowing to nothing is not a "
            "narrowing: a narrow= declaration does not cover it. Restore the "
            "canonical text, or remove the stamp markers if this block is no "
            "longer a stamped copy.")

    if _is_ordered_subsequence(child, parent):
        if block.narrow and _is_floor_block(block):
            # Board 115/030, ruled 2026-09-19: the floor is copied verbatim.
            # PROPAGATION.md no longer grants the floor a legitimate
            # narrowing, so a narrow= declaration here buys nothing — this
            # is mechanically the same ordered-subset shape as a silent
            # drop, and now carries the same verdict: RED, always.
            return Finding(
                block.path, block.line, "drift", block.source, block.region,
                f"the floor is copied verbatim — no compression, no "
                f"declared narrowing. narrow={block.narrow!r} declares a "
                f"narrowing on the atelier safety floor "
                f"({FLOOR_SOURCE} region={FLOOR_REGION}), but the floor has "
                f"no legitimate subset: restore the canonical text word for "
                f"word ({len(child)} of {len(parent)} canonical lines "
                f"kept); a `narrow=` declaration does not excuse it here.")
        if block.narrow:
            return Finding(
                block.path, block.line, "narrow", block.source, block.region,
                f"legitimate narrow (declared: {block.narrow!r}) — "
                f"{len(child)} of {len(parent)} canonical lines kept, in "
                f"order")
        return Finding(
            block.path, block.line, "drift", block.source, block.region,
            "an ordered subset of the canonical region, but no narrow= was "
            "declared — a silent drop reds; add `narrow=<reason>` to "
            "stamp:begin if this is deliberate, or restore the missing "
            "line(s)")

    hint = _first_offending_line(child, parent)
    return Finding(
        block.path, block.line, "drift", block.source, block.region,
        "does not match the canonical region and is not an ordered subset "
        "of it (an addition, reordering, or reword) — " + (hint or ""))


# ------------------------------------------------------------- filesystem --

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
    """Globs from `.stampscanignore`, each of which MUST carry a stated reason.

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
    f = root / ".stampscanignore"
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
        raise IgnoreFileError(".stampscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def resolve_source(root: Path, source: str) -> tuple[Path | None, str | None]:
    """Resolve a stamp's `source=` against `root` and confirm it exists.
    Returns `(path, error_kind)` — the resolved `Path` on success (NOT its
    content — see 020/380 below), or `(None, kind)` where kind is
    `"unconfined-source"` or `"missing-source"`.

    CONFINEMENT (2026-07-26 cold pass ST4): the resolved path must sit inside
    `root`. `root / source` alone accepts `../` traversal, and pathlib
    silently DISCARDS `root` when the right-hand side is absolute — so a
    crafted stamped document could aim the scanner at any file on the machine
    and have one of its lines echoed back in the drift hint. Escaping the root
    is a config error, matching the fail-safe posture everywhere else.

    020/380: this used to also READ the file whole and return its text —
    the caller (`scan_paths`) now streams the region out of it via
    `extract_region_from_file` instead, so peak memory for a canonical
    source is bounded by its REGION's size, not the whole document's."""
    root = root.resolve()
    candidate = (root / source).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None, "unconfined-source"
    if not candidate.is_file():
        return None, "missing-source"
    return candidate, None


def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time. Single-sourced
    (115/080 part 1) in `tools/filewalk.py` — see that module's docstring
    for the mechanism and the 020/160 (E9) linked-worktree skip.
    `SKIP_DIR_NAMES` is this scanner's own per-guard parameter, passed in
    rather than shared."""
    return filewalk.walk_files(base, SKIP_DIR_NAMES)


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  skipped: list[int] | None = None):
    for base in paths:
        candidates = [base] if base.is_file() else _walk_files(base)
        for p in candidates:
            if p.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            if _ignored(_rel(p, root), globs):
                if skipped is not None:
                    skipped.append(1)
                continue
            yield p


def scan_paths(paths: list[Path], root: Path,
               skipped: list[int] | None = None,
               truncated: list[int] | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    # Keyed by (source, region), not by source alone: this holds only the
    # EXTRACTED REGION (typically a small floor block), never a whole
    # canonical document — the 020/380 fix. A source resolution error is
    # cached too, so a stray/missing source is still only diagnosed once.
    region_cache: dict[tuple[str, str], tuple[list[str] | None, str | None]] = {}
    source_error_cache: dict[str, str] = {}

    for md in iter_markdown(paths, root, globs, skipped):
        rel = _rel(md, root)
        # 020/380 — streamed rather than `md.read_text()` + `_content_lines`:
        # peak memory for THIS file is now bounded by `_MAX_LINE_BYTES` (plus
        # whatever it happens to be currently accumulating inside an open
        # stamp block), independent of the file's own size.
        blocks, malformed = find_stamp_blocks_in_file(rel, md, truncated)
        findings.extend(malformed)

        for block in blocks:
            cache_key = (block.source, block.region)
            if cache_key in region_cache:
                canonical, region_error = region_cache[cache_key]
            elif block.source in source_error_cache:
                canonical, region_error = None, None
                findings.append(Finding(
                    block.path, block.line, source_error_cache[block.source],
                    block.source, block.region,
                    f"canonical source previously failed to resolve: "
                    f"{block.source}"))
                continue
            else:
                source_path, source_error = resolve_source(root, block.source)
                if source_path is None:
                    source_error_cache[block.source] = source_error
                    if source_error == "unconfined-source":
                        detail = (f"canonical source resolves OUTSIDE --root: "
                                  f"{block.source} (--root {root}) — a stamp "
                                  f"may only point at a file inside the "
                                  f"scanned tree")
                    else:
                        detail = (f"canonical source does not resolve: "
                                  f"{block.source} (resolved against --root "
                                  f"{root})")
                    findings.append(Finding(
                        block.path, block.line, source_error, block.source,
                        block.region, detail))
                    continue
                canonical = extract_region_from_file(
                    source_path, block.region, truncated)
                region_cache[cache_key] = (canonical, None)

            if canonical is None:
                findings.append(Finding(
                    block.path, block.line, "missing-region", block.source,
                    block.region,
                    f"region '{block.region}:begin'/'{block.region}:end' "
                    f"not found in {block.source}"))
                continue

            findings.append(evaluate_block(block, canonical))

    return findings


# -------------------------------------------------------------- reporting --

_CONFIG_ERROR_KINDS = {"missing-source", "unconfined-source",
                       "missing-region", "malformed"}
_DRIFT_KINDS = {"drift"}
_CLEAN_KINDS = {"identical", "narrow", "skipped"}


def _suppression_line(findings: list[Finding], files_by_glob: int,
                      lines_truncated: int = 0) -> str:
    """Rule (b) of `method/GUARDS.md`, known zeros printed (SD3, ruled
    2026-08-06): allow-skipped blocks were already visible as notes, but
    files skipped wholesale by `.stampscanignore` were silent — a whole
    exempted store looked identical to one with nothing in it.

    `lines_truncated` (020/380) is the same shape: a physical line over
    `_MAX_LINE_BYTES` is still scanned, just truncated to that many
    characters — counted here rather than silently short."""
    skipped_blocks = sum(1 for f in findings if f.kind == "skipped")
    return (f"  suppressed: {skipped_blocks} block(s) by allow-marker · "
            f"{files_by_glob} file(s) by .stampscanignore · "
            f"{lines_truncated} over-long line(s) scanned truncated")


def render_human(findings: list[Finding], files_by_glob: int = 0,
                 lines_truncated: int = 0) -> str:
    errors = [f for f in findings if f.kind in _CONFIG_ERROR_KINDS]
    drifts = [f for f in findings if f.kind in _DRIFT_KINDS]
    notes = [f for f in findings if f.kind in _CLEAN_KINDS]

    if not findings:
        return ("✓ stampscan clean — no stamped blocks found.\n"
                + _suppression_line(findings, files_by_glob, lines_truncated))

    lines: list[str] = []
    if errors:
        lines.append(f"✗ stampscan: {len(errors)} config error(s) (fail-safe).")
        for f in sorted(errors, key=lambda x: (x.path, x.line)):
            lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.detail}")
    if drifts:
        lines.append(f"✗ stampscan: {len(drifts)} drift finding(s).")
        for f in sorted(drifts, key=lambda x: (x.path, x.line)):
            lines.append(
                f"  {f.path}:{f.line}  source={f.source} region={f.region}  "
                f"{f.detail}")
    if not errors and not drifts:
        lines.append(f"✓ stampscan clean — {len(notes)} stamped block(s) verified.")
    if notes:
        # De-duplicated kinds (ST6c): the summary names WHICH dispositions
        # occurred, not one repeat per block — "identical, identical, …" for
        # a healthy tree of stamps was noise, and the per-block lines below
        # already carry the detail.
        lines.append(f"  ({len(notes)} note(s): "
                      + ", ".join(sorted({f.kind for f in notes})) + ")")
        for f in sorted(notes, key=lambda x: (x.path, x.line)):
            lines.append(f"    {f.path}:{f.line}  [{f.kind}] {f.detail}")
    lines.append(_suppression_line(findings, files_by_glob, lines_truncated))
    if drifts:
        lines.append(
            "\n  A real drift: make the block equal its canonical region, or "
            "add `narrow=<reason>` to stamp:begin if the narrowing is "
            "deliberate.")
        lines.append(
            f"  A deliberate exemption: append '<!-- {ALLOW_MARKER}: <reason> -->'")
        lines.append("  inside the stamped block, or add a path glob to "
                      ".stampscanignore.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="stampscan",
        description="Check docs/** for inlined-floor / child-template "
                    "restatements that drift from their canonical parent "
                    "(stamp-drift).")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan for stamped blocks (default: "
                         "<root>/docs if present, else the whole root)")
    ap.add_argument("--root", default=".",
                    help="repo root for .stampscanignore, canonical source= "
                         "resolution, and relative paths")
    ap.add_argument("--warn", action="store_true",
                    help="report drift findings but always exit 0 for them "
                         "(advisory rollout — this scanner is first-of-kind "
                         "and not yet reviewed; it must not gate). Does NOT "
                         "downgrade a config error, which always exits 2.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"stampscan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    if args.paths:
        # A RELATIVE target resolves against --root, never the caller's cwd:
        # mixing the two reads one repo's file under another repo's rules,
        # and neither half of the output says so (roadmap 010/110).
        targets = [(root / p) if not Path(p).is_absolute() else Path(p)
                   for p in args.paths]
    else:
        docs = root / "docs"
        targets = [docs] if docs.is_dir() else [root]

    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"stampscan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    _skipped: list[int] = []
    _truncated: list[int] = []
    try:
        findings = scan_paths(targets, root, _skipped, _truncated)
    except OSError as e:
        print(f"stampscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    errors = [f for f in findings if f.kind in _CONFIG_ERROR_KINDS]
    drifts = [f for f in findings if f.kind in _DRIFT_KINDS]

    if args.json:
        print(json.dumps({
            "clean": not errors and not drifts,
            "warn": args.warn,
            "findings": [asdict(f) for f in findings],
            "suppressed": {
                "blocks_by_allow_marker":
                    sum(1 for f in findings if f.kind == "skipped"),
                "files_by_ignore_glob": len(_skipped),
                "lines_truncated": len(_truncated),
            },
        }, indent=2))
    else:
        print(render_human(findings, len(_skipped), len(_truncated)))
        if drifts and args.warn and not errors:
            print("\n  (--warn: advisory only — drift not blocking this build.)")

    if errors:
        return 2  # fail-safe: NEVER downgraded by --warn
    if drifts:
        return 0 if args.warn else 1
    return 0


def _selftest() -> int:
    """Minimal smoke test so `stampscan --selftest` proves the engine on any
    box, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="stampscan-self-"))
    (tmp / "docs").mkdir()

    canonical_lines = ["- item one", "- item two", "- item three"]
    (tmp / "docs" / "PARENT.md").write_text(
        "# Parent\n\nSome prose.\n\n"
        "<!-- floor:begin -->\n"
        + "\n".join(canonical_lines) + "\n"
        "<!-- floor:end -->\n\nMore prose.\n"
    )

    # Identical stamp -> clean.
    (tmp / "docs" / "child_ok.md").write_text(
        "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
        + "\n".join(canonical_lines) + "\n"
        "<!-- stamp:end -->\n"
    )
    findings_ok = scan_paths([tmp / "docs" / "child_ok.md"], tmp)
    ok = [f.kind for f in findings_ok] == ["identical"]
    if not ok:
        print(f"FAIL: identical case got {[f.kind for f in findings_ok]}")

    # Declared narrow, genuine ordered subset -> clean/noted.
    (tmp / "docs" / "child_narrow.md").write_text(
        "<!-- stamp:begin source=docs/PARENT.md region=floor narrow=deliberate-drop -->\n"
        "- item one\n- item three\n"
        "<!-- stamp:end -->\n"
    )
    findings_narrow = scan_paths([tmp / "docs" / "child_narrow.md"], tmp)
    ok_narrow = [f.kind for f in findings_narrow] == ["narrow"]
    if not ok_narrow:
        print(f"FAIL: narrow case got {[f.kind for f in findings_narrow]}")
        ok = False

    # Same ordered subset, but NOT declared narrow -> silent drop, drift/red.
    (tmp / "docs" / "child_drop.md").write_text(
        "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
        "- item one\n- item three\n"
        "<!-- stamp:end -->\n"
    )
    findings_drop = scan_paths([tmp / "docs" / "child_drop.md"], tmp)
    ok_drop = [f.kind for f in findings_drop] == ["drift"]
    if not ok_drop:
        print(f"FAIL: silent-drop case got {[f.kind for f in findings_drop]}")
        ok = False

    # A contradiction (reworded line) -> drift/red, narrow= or not.
    (tmp / "docs" / "child_contra.md").write_text(
        "<!-- stamp:begin source=docs/PARENT.md region=floor narrow=x -->\n"
        "- item one\n- item TWO REWORDED\n- item three\n"
        "<!-- stamp:end -->\n"
    )
    findings_contra = scan_paths([tmp / "docs" / "child_contra.md"], tmp)
    ok_contra = [f.kind for f in findings_contra] == ["drift"]
    if not ok_contra:
        print(f"FAIL: contradiction case got {[f.kind for f in findings_contra]}")
        ok = False

    # An EMPTY payload -> drift, `narrow=` or not (ST2). Narrowing to
    # nothing is not a narrowing.
    (tmp / "docs" / "child_empty.md").write_text(
        "<!-- stamp:begin source=docs/PARENT.md region=floor narrow=we-dropped-it-all -->\n"
        "<!-- stamp:end -->\n"
    )
    findings_empty = scan_paths([tmp / "docs" / "child_empty.md"], tmp)
    ok_empty = [f.kind for f in findings_empty] == ["drift"]
    if not ok_empty:
        print(f"FAIL: empty-narrow case got {[f.kind for f in findings_empty]}")
        ok = False

    # THE FLOOR ITSELF (board 115/030, ruled 2026-09-19): the real
    # (source, region) pair, not the generic "floor" name the fixtures above
    # reuse — a narrow= declaration on it reds even though it is a genuine
    # ordered subset, exactly like a silent drop.
    (tmp / "docs" / "method").mkdir(parents=True)
    (tmp / "docs" / "method" / "PROPAGATION.md").write_text(
        "<!-- floor:begin -->\n" + "\n".join(canonical_lines) + "\n"
        "<!-- floor:end -->\n")
    (tmp / "docs" / "child_floor_narrow.md").write_text(
        "<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor "
        "narrow=shortened-for-readability -->\n"
        "- item one\n- item three\n"
        "<!-- stamp:end -->\n"
    )
    findings_floor_narrow = scan_paths(
        [tmp / "docs" / "child_floor_narrow.md"], tmp)
    ok_floor_narrow = [f.kind for f in findings_floor_narrow] == ["drift"]
    if not ok_floor_narrow:
        print(f"FAIL: floor-narrow case got "
              f"{[f.kind for f in findings_floor_narrow]}")
        ok = False
    (tmp / "docs" / "child_floor_verbatim.md").write_text(
        "<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n"
        + "\n".join(canonical_lines) + "\n"
        "<!-- stamp:end -->\n"
    )
    findings_floor_verbatim = scan_paths(
        [tmp / "docs" / "child_floor_verbatim.md"], tmp)
    ok_floor_verbatim = [f.kind for f in findings_floor_verbatim] == ["identical"]
    if not ok_floor_verbatim:
        print(f"FAIL: floor-verbatim case got "
              f"{[f.kind for f in findings_floor_verbatim]}")
        ok = False

    # Missing canonical source -> fail-safe config error.
    (tmp / "docs" / "child_missing.md").write_text(
        "<!-- stamp:begin source=docs/NOPE.md region=floor -->\n"
        "- item one\n"
        "<!-- stamp:end -->\n"
    )
    findings_missing = scan_paths([tmp / "docs" / "child_missing.md"], tmp)
    ok_missing = [f.kind for f in findings_missing] == ["missing-source"]
    if not ok_missing:
        print(f"FAIL: missing-source case got {[f.kind for f in findings_missing]}")
        ok = False

    # A source escaping --root -> fail-safe config error, not a scan (ST4).
    (tmp / "docs" / "child_escape.md").write_text(
        "<!-- stamp:begin source=../../etc/hosts region=floor -->\n"
        "- item one\n"
        "<!-- stamp:end -->\n"
    )
    findings_escape = scan_paths([tmp / "docs" / "child_escape.md"], tmp)
    ok_escape = [f.kind for f in findings_escape] == ["unconfined-source"]
    if not ok_escape:
        print(f"FAIL: unconfined-source case got {[f.kind for f in findings_escape]}")
        ok = False

    # A doc that merely DOCUMENTS the syntax is not a stamp (ST1) — fenced
    # examples and inline-code mentions alike. This is the wiring blocker.
    (tmp / "docs" / "about_stamps.md").write_text(
        "# How stamps work\n\n"
        "A child wraps the block in a marker pair:\n\n"
        "```markdown\n"
        "<!-- stamp:begin source=docs/PARENT.md region=floor -->\n"
        "...the inlined block...\n"
        "<!-- stamp:end -->\n"
        "```\n\n"
        "The closer is `<!-- stamp:end -->`, and the opener is "
        "`<!-- stamp:begin source=x region=y -->`.\n"
    )
    findings_doc = scan_paths([tmp / "docs" / "about_stamps.md"], tmp)
    ok_doc = findings_doc == []
    if not ok_doc:
        print(f"FAIL: documentation-of-syntax case got "
              f"{[f.kind for f in findings_doc]}")
        ok = False

    # main() plumbing: a config error always exits 2, --warn or not; a drift
    # finding exits 1 without --warn, 0 with --warn.
    if main(["--root", str(tmp), str(tmp / "docs" / "child_missing.md")]) != 2:
        print("FAIL: a config error should exit 2")
        ok = False
    if main(["--warn", "--root", str(tmp), str(tmp / "docs" / "child_missing.md")]) != 2:
        print("FAIL: a config error should exit 2 even with --warn")
        ok = False
    if main(["--root", str(tmp), str(tmp / "docs" / "child_drop.md")]) != 1:
        print("FAIL: a drift finding without --warn should exit 1")
        ok = False
    if main(["--warn", "--root", str(tmp), str(tmp / "docs" / "child_drop.md")]) != 0:
        print("FAIL: a drift finding with --warn should exit 0")
        ok = False
    if main(["--root", str(tmp), str(tmp / "docs" / "child_ok.md")]) != 0:
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
        print(f"stampscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())

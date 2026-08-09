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
    matching linkscan/sizescan; a 4-space-indented code block (CommonMark's
    other code-block form) is skipped per-line the same way wrapscan does
    (DSR6) — before this fix only fenced code was exempt. An inline
    `` `code span` `` is blanked before either check runs (linkscan's
    `_strip_inline_code`), so a literal `` `today` `` in a code example
    never fires.

    A blockquoted line (`>` at the start, after leading whitespace) is
    skipped whole. STATED HONESTLY, NOT ROUNDED UP (DSR1 finding on the
    original wording): `>` is not only how a quoted external source's words
    read in Markdown — it is ALSO this house's own callout-block style (see
    COMMUNICATION.md; `AUTONOMY.md`'s own `>` blocks; the `> 🎯 S1…` seam
    candidates in the S3 intent doc are the repo's own normative text, not a
    quotation). The blockquote skip therefore over-exempts: a relative-time
    claim inside the house's own `>`-styled callout is silently missed, not
    just a genuinely-quoted external source's. A per-line "is this an
    attribution quote or a callout" classifier was considered and rejected —
    the house's own icon vocabulary is deliberately NOT a fixed, closed set
    (COMMUNICATION.md: "don't ration the icon vocabulary to a fixed set"),
    so any icon-based classifier would itself silently miss callouts using an
    icon not on its list, trading one silent-miss class for another instead
    of removing it. This scanner picks the honest, simpler statement over a
    heuristic that would look more precise than it is: **every** `>` line is
    exempt, house callouts included, and that is a real gap, not a stated
    limit that turned out narrower in practice.

  * PROSE *ABOUT* RELATIVE TIME — the hard exemption, because "this rule bans
    the word today" and "the meeting is today" are structurally identical to
    a regex. The only mechanically-honest signal available is USE vs MENTION
    by punctuation: a relative-time word or phrase inside a quoted SPAN — a
    matching pair of quote marks with the opener before the match and the
    closer at or after it (`"today"`, `'yesterday'`, curly “last week”, or a
    multi-word phrase inside a longer quoted example like `"new this year"`)
    — is treated as a MENTION (the word itself is the topic) and exempted.
    This is exactly the shape the S3 rule's own worked examples use. DSR4:
    the span check (not just the two characters immediately flanking the
    match) is what makes the multi-word case work — the original adjacency-
    only check missed a banned phrase sitting mid-quote. It is a narrow,
    honest heuristic, not a parser: prose that discusses relative time WITHOUT
    quoting the word ("the meaning of yesterday drifts by design") still
    false-positives, and is meant to be closed with a `datescan:allow`; and
    the wider span check makes the OTHER direction (a genuine use that
    happens to sit inside an unrelated quoted sentence) slightly more likely
    too — both are accepted trade-offs, not new blind spots.

  * THE ALLOW MARKER / IGNORE FILE. A line carrying `datescan:allow: <reason>`
    anywhere is exempt from every check on that line (same contract as
    leakscan/linkscan). Tighter than sibling parity by one notch (the S3 cold
    review's DSR8): the marker must sit at a word boundary and be followed by
    a non-empty reason, so prose that merely *mentions* the marker text — with
    no colon-and-reason after it — does not silently exempt the line. A glob
    in `.datescanignore` at the scan root exempts a path wholesale (mirrors
    every sibling scanner's ignore file).

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
  * "today" is narrowed to date-adjacent contexts (a dating cue word, or an
    ISO date elsewhere on the line — see TODAY_RX/_is_date_adjacent_today,
    DSR3), because the reviewed corpus found it used ~9:1 as a "currently"
    hedge rather than a calendar-date claim. The accepted cost: a bare,
    genuine "today = this date" claim with no cue and no ISO date alongside
    it on the same line now scans clean — a real silent-miss, traded
    deliberately for killing the dominant noise source.
  * The non-ISO date patterns are common English/NZ shapes (slash-dates,
    dash-dates, "23 July 2026", "July 23, 2026") — not exhaustive of every
    locale's date grammar. A three-numeral slash/dash requirement
    (`DD/MM/YYYY`, not `DD/MM`) keeps ordinary fractions ("3/4 of the work")
    from false-firing. Named gap (DSR5): a slash date in ISO field order,
    `2026/07/23` (YYYY/MM/DD), still scans clean — the slash-date pattern
    only reads `DD/MM/YYYY`. The numeral-triple patterns (slash-date,
    dash-date) also require the pair to be a plausible (day, month) coordinate
    in either field order (`_plausible_date_fields`, DSR2) — this is what
    keeps a session number like `23/26/27` from false-firing as a date; it is
    a plausibility gate, not a real calendar-date check (that's ISO_DATE_RX's
    job on the actual ISO shape).
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
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path

# A line carrying this marker is intentionally exempt from every check on that
# line. Keep the reason on the same line so the exemption is self-documenting
# and greppable, same contract as the sibling scanners.
ALLOW_MARKER = "datescan:allow"

# DSR8: the sibling scanners (leakscan/linkscan/secretscan/wrapscan/spellscan)
# all treat ALLOW_MARKER as a bare substring — any prose that merely mentions
# the marker text exempts the whole line, and an empty reason is accepted.
# datescan tightens this past sibling parity: the marker must sit at a word
# boundary (so it can't hide inside a longer token) and must be followed by a
# colon and a non-empty reason, `datescan:allow: <reason>` — matching the
# documented contract this header and render_human() already advertise. The
# reason must start with a WORD character (not just any non-whitespace) so
# an empty-reason marker inside its own HTML comment, `<!-- datescan:allow:
# -->`, isn't mistaken for a reason of "-->" — the comment closer is the
# first non-whitespace character there, but it isn't a reason.
ALLOW_MARKER_RX = re.compile(r"\b" + re.escape(ALLOW_MARKER) + r":\s*[\w\"\'“‘]")

ALLOW_SCOPE_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    `""` means every kind on the line; a kind name means just that one.
    A marker with no reason returns None — a mention, not an exemption."""
    m = ALLOW_SCOPE_RX.search(line)
    if not m:
        return None
    return m.group("kind") or ""


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`.

    A guard that subtracts silently prints the same clean tick for "nothing
    matched" and "everything matched and was exempted"."""
    by_marker: dict[str, int] = field(default_factory=dict)
    files_by_glob: int = 0

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def note_marker(self, kind: str) -> None:
        self.by_marker[kind] = self.by_marker.get(kind, 0) + 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        line = ("  suppressed: "
                f"{self.marker_total} by allow-marker · "
                f"{self.files_by_glob} file(s) by .datescanignore")
        if self.by_marker:
            detail = ", ".join(f"{k}×{n}" for k, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        return line


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
#
# NOTE: "today" is deliberately NOT in this list — see TODAY_RX and
# _is_date_adjacent below (DSR3). Every other term here is unambiguous: they
# occur almost exclusively as a claim about a specific point in time. "today"
# is not — the corpus review found it used overwhelmingly as a weak-anchor
# hedge ("still correct today", i.e. "currently"), the exact class this list
# already excludes for "recently"/"currently"/"soon". "today" straddles both
# senses, so it gets its own narrower check instead of a bare denylist entry.
RELATIVE_TIME_TERMS = sorted([
    "tonight", "tomorrow", "yesterday",
    "last night", "last week", "last month", "last year",
    "next week", "next month", "next year",
    "this week", "this month", "this year",
    "the other day", "a few days ago", "a few weeks ago", "a few months ago",
], key=len, reverse=True)

RELATIVE_TIME_RX = re.compile(
    r"\b(?:" + "|".join(re.escape(t) for t in RELATIVE_TIME_TERMS) + r")\b",
    re.IGNORECASE)

# DSR3: "today" is checked separately, narrowed to DATE-ADJACENT contexts —
# a cue word/phrase that signals "today" is standing in for a specific
# calendar date, not just hedging "at present". Cues: an explicit dating verb
# ("date[d]", "stamp[ed]", "dating"), the "as of" construction, or an
# ISO-8601-shaped date appearing anywhere else on the same line (e.g. "Today,
# 2026-07-23" or "today (2026-07-23)" — comparing/pairing "today" with a real
# date is itself evidence it's being used as one).
#
# HONEST LIMIT (do not round this to "solved"): this narrows false positives
# at the cost of a real false-negative class — a bare, genuine calendar-date
# claim with no cue word and no ISO date alongside it on the same line
# ("Filed today.") now scans clean. That trade is deliberate: the reviewed
# corpus showed the hedge sense dominates ~9:1, so the bare form is now
# treated as the common (silent-miss-accepted) case rather than the flagged
# one — the same under-flag-over-noise call the denylist already makes for
# "recently"/"currently"/"soon".
TODAY_RX = re.compile(r"\btoday\b", re.IGNORECASE)
TODAY_CUE_RX = re.compile(r"\b(?:date[ds]?|dating|stamp(?:ed)?)\b|\bas\s+of\b",
                           re.IGNORECASE)
_TODAY_CUE_WINDOW = 40  # characters either side of the match to scan for a cue


def _is_date_adjacent_today(line: str, start: int, end: int) -> bool:
    """DSR3: True if a "today" match at [start, end) sits near a dating cue
    (see TODAY_CUE_RX) or an ISO-8601-shaped date NEARBY (same window) —
    the narrowing heuristic that keeps the currently-sense "today" quiet
    while still catching the calendar-date sense. Window-based, not
    grammar-aware: see the honest limit noted above TODAY_RX.

    Both checks are windowed around the match, NOT scanned over the whole
    line — an earlier version of this heuristic checked the ISO date over
    the whole line, which false-fired on long lines carrying an unrelated
    ISO-dated link path or citation far from the "today" match (found live
    in docs/SESSIONS.md during this fix's own re-baseline, e.g. a line
    linking to `sessions/2026-07-14-2142-....md` while separately using
    "today" in the currently-sense sixty-odd characters away)."""
    lo = max(0, start - _TODAY_CUE_WINDOW)
    hi = min(len(line), end + _TODAY_CUE_WINDOW)
    window = line[lo:hi]
    return bool(TODAY_CUE_RX.search(window) or ISO_DATE_RX.search(window))

# Non-ISO absolute-date shapes. A three-numeral slash date requires TWO
# slashes (`DD/MM/YYYY`), so an ordinary fraction ("3/4 of the work") never
# matches — only one slash there.
_MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
          r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|"
          r"Nov(?:ember)?|Dec(?:ember)?)")


def _plausible_date_fields(a: int, b: int) -> bool:
    """DSR2: True if the numeral pair (a, b) could plausibly be (day, month)
    or (month, day) in EITHER field order — used to keep the numeral-triple
    patterns below (slash-date, dash-date) from firing on ordinary numeric
    triples that are not dates at all, e.g. a session number `23/26/27`
    (23 is a plausible day, but 26 is not a plausible month in either
    reading). Deliberately not a full calendar-date validator — the ISO
    shape check owns real invalid-date detection (leap years etc); this is
    just a coordinate-plausibility gate ahead of the noisier free-form
    patterns."""
    return (1 <= a <= 31 and 1 <= b <= 12) or (1 <= a <= 12 and 1 <= b <= 31)


# Each entry is (kind, pattern, validator). The validator, if given, is
# called with the first two captured numeral groups (as ints); a False
# return drops the match as an implausible date rather than a finding —
# see _plausible_date_fields. Patterns with no numeral ambiguity (the month
# is spelled out) carry no validator.
NON_ISO_PATTERNS: list[tuple[str, "re.Pattern[str]", object]] = [
    ("slash-date", re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b"),
     _plausible_date_fields),
    # DSR5: dash DD-MM-YYYY (e.g. `23-07-2026`) — a form that scanned clean
    # before this fix. Requires a 4-digit year so it can't be confused with
    # an ISO date (which requires a 4-digit YEAR FIRST — ISO_DATE_RX owns
    # that shape) or a hyphenated identifier. The `(?<!\d{4}-)` lookbehind
    # is load-bearing: without it this pattern false-fires on the house's
    # own session-log ID convention, `YYYY-MM-DD-HHMM`
    # (e.g. `2026-07-22-1021` reads its trailing `07-22-1021` as a
    # plausible MM-DD-"year" triple — found live in docs/SESSIONS.md during
    # this fix's own re-baseline). Still doesn't cover every locale's
    # dash-date grammar (see the header's honest residual).
    ("dash-date", re.compile(r"(?<!\d{4}-)\b(\d{1,2})-(\d{1,2})-(\d{4})\b"),
     _plausible_date_fields),
    ("month-day-year", re.compile(
        rf"\b{_MONTH}\.?\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}}\b", re.IGNORECASE),
     None),
    ("day-month-year", re.compile(
        rf"\b\d{{1,2}}(?:st|nd|rd|th)?\s+(?:of\s+)?{_MONTH}\.?,?\s+\d{{4}}\b",
        re.IGNORECASE),
     None),
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


# DSR6: CommonMark's indented-code-block rule (4+ leading columns), applied
# per-line like wrapscan's INDENTED_CODE_COLUMNS/_is_indented_code — a
# 4-space-indented code example wasn't exempt before this fix (only fenced
# code was), so a relative-time word or non-ISO date inside one flagged.
INDENTED_CODE_COLUMNS = 4


def _leading_columns(line: str) -> int:
    """Count leading-whitespace columns, expanding tabs to the next 4-column
    stop. Simple and stated, not a full CommonMark tab-expansion
    implementation (matches wrapscan's helper of the same name/shape)."""
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
    """USE-vs-MENTION by punctuation: True if the match falls inside a quoted
    SPAN — the nearest matching pair of quote marks with the opener before
    the match and the closer at or after it. This is DSR4's fix: the
    original check only looked at the two characters immediately flanking
    the match, so a banned word inside a multi-word quoted example (`"new
    this year"`, matching the phrase "this year") was wrongly caught — the
    opening quote sits before "new", not immediately before "this". Checking
    the enclosing span instead of adjacency catches both the single-word
    case (`"today"`) and the multi-word case.

    Honest limit (unchanged from before DSR4, see module docstring): this is
    still punctuation-shaped, not semantic. A genuine USE that happens to
    sit inside an unrelated quoted sentence — a quote that itself says
    "we'll ship tomorrow" — is still wrongly exempted; a span check makes
    this slightly MORE likely (a wider net), not less. Accepted trade-off,
    same direction the header already documents."""
    for open_ch, close_ch in _QUOTE_PAIRS.items():
        open_pos = line.rfind(open_ch, 0, start)
        if open_pos == -1:
            continue
        close_pos = line.find(close_ch, end)
        if close_pos == -1:
            continue
        between = line[open_pos + 1:start]
        # Straight quotes reuse the same character for open and close, so a
        # stray same-char quote between the candidate opener and the match
        # means `open_pos` is really the CLOSE of some earlier, unrelated
        # quoted segment — not a genuine opener for this match.
        if close_ch == open_ch:
            if close_ch in between:
                continue
        elif open_ch in between:
            continue
        return True
    return False


def scan_text(path: str, text: str, tally: "Tally | None" = None) -> list[Finding]:
    findings: list[Finding] = []
    # Line -> allowance scope. Recorded, not acted on: the finding forms first
    # so the exemption can be counted (rule b, find first and subtract second).
    allow_by_line: dict[int, str] = {}
    for lineno, raw_line in _content_lines(text):
        scope = parse_allow(raw_line)
        if scope is not None:
            allow_by_line[lineno] = scope
        if _is_blockquote(raw_line):
            continue
        if _is_indented_code(raw_line):
            continue
        line = _strip_inline_code(raw_line)

        for m in RELATIVE_TIME_RX.finditer(line):
            if _is_quoted_mention(line, m.start(), m.end()):
                continue
            findings.append(Finding(
                path, lineno, "relative-time-word", m.group(0),
                "relative to the reader's 'now', not an absolute date — replace "
                "with an ISO-8601 date stamped from `date -u`"))

        for m in TODAY_RX.finditer(line):
            if _is_quoted_mention(line, m.start(), m.end()):
                continue
            if not _is_date_adjacent_today(line, m.start(), m.end()):
                continue
            findings.append(Finding(
                path, lineno, "relative-time-word", m.group(0),
                "relative to the reader's 'now', not an absolute date — replace "
                "with an ISO-8601 date stamped from `date -u`"))

        for kind, rx, validator in NON_ISO_PATTERNS:
            for m in rx.finditer(line):
                if validator is not None:
                    a, b = int(m.group(1)), int(m.group(2))
                    if not validator(a, b):
                        continue
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
    # SUBTRACT SECOND, scoped by finding kind so a marker written for a
    # relative-time word does not also exempt a non-ISO date on the line.
    kept: list[Finding] = []
    for f in findings:
        scope = allow_by_line.get(f.line)
        if scope is not None and scope in ("", f.kind):
            if tally is not None:
                tally.note_marker(f.kind)
            continue
        kept.append(f)
    return kept


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
    """Globs from `.datescanignore`, each of which MUST carry a stated reason.

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
    f = root / ".datescanignore"
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
        raise IgnoreFileError(".datescanignore", unreasoned)
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


def scan_paths(paths: list[Path], root: Path,
               tally: "Tally | None" = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs, tally):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text(_rel(md, root), text, tally))
    return findings


def render_human(findings: list[Finding], tally: "Tally | None" = None) -> str:
    if not findings:
        out = "✓ datescan clean — no relative-time words or non-ISO dates found."
        return out + ("\n" + tally.summary() if tally is not None else "")
    lines = [f"✗ datescan: {len(findings)} finding(s)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.match!r} → {f.detail}")
    lines.append("\n  A real dating slip: fix the word/date (stamp from `date -u`, ISO-8601).")
    lines.append(f"  A deliberate exemption: append '<!-- {ALLOW_MARKER}: <reason> -->'")
    lines.append("  to the line, or add a path glob to .datescanignore.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
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
    tally = Tally()
    try:
        findings = scan_paths(targets, root, tally)
    except OSError as e:
        print(f"datescan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "warn": args.warn,
            "findings": [asdict(f) for f in findings],
            "suppressed": {
                "by_allow_marker": tally.marker_total,
                "by_allow_marker_rule": tally.by_marker,
                "files_by_ignore_glob": tally.files_by_glob,
            },
        }, indent=2))
    else:
        print(render_human(findings, tally))
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
        "Landed today after the change last week.\n"                     # DSR3: bare "today" (no cue) exempt; "last week" flagged
        "Stamped 2026-07-23 correctly.\n"                                 # clean ISO
        "Filed on 23/07/2026 by hand.\n"                                  # non-iso slash-date
        "Filed on 23-07-2026 by hand too.\n"                              # DSR5: non-iso dash-date
        "Session 23/26/27 is not a date.\n"                               # DSR2: implausible numeral triple, exempt
        "Filed on July 23, 2026 by hand.\n"                               # non-iso month-day-year
        "Bogus date 2026-13-40 here.\n"                                   # invalid iso
        "The rule bans relative-time words like \"today\" and \"yesterday\".\n"  # quoted mentions, exempt
        "Banned phrases include \"new this year\" in the doc's own list.\n"  # DSR4: multi-word quoted mention, exempt
        "`tomorrow` is just an example in code.\n"                        # code span, exempt
        "> quoted external text says it happened yesterday.\n"           # blockquote, exempt
        "```\nshipped tomorrow in this fenced block\n```\n"               # fenced, exempt
        "    shipped tomorrow in this indented code block\n"              # DSR6: indented code, exempt
        "reduced scope by 3/4 of the work.\n"                             # fraction, not a date
        "Stamped today, all fields correct.\n"                            # DSR3: date-adjacent "today", flagged
        "allowed today  <!-- datescan:allow: selftest fixture -->\n"     # allow marker (with reason), exempt
    )
    findings = scan_paths([tmp / "docs"], tmp)
    kinds = sorted((f.kind, f.match.lower()) for f in findings)
    expected = sorted([
        ("relative-time-word", "last week"),
        ("relative-time-word", "today"),
        ("non-iso-date", "23/07/2026"),
        ("non-iso-date", "23-07-2026"),
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



def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file that grants an exemption with no reason.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    try:
        return _main(argv)
    except IgnoreFileError as e:
        print(f"datescan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())

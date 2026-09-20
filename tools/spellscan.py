#!/usr/bin/env python3
"""spellscan — the NZ-English spelling check for docs prose.

The rule (2026-07-22 invariant-candidates review, seam S5): `docs/**`
(including templates, which live under `docs/build/templates/`) uses
NZ-English spelling (artefact, organise, synthesise, colour, licence…), per
`method/CONVENTIONS.md`'s "NZ English with macrons" default. A US spelling
with an unambiguous NZ equivalent is flagged; the fix is either the NZ
spelling, or — for a genuine third-party term (an API name, a tool name) —
an inline code span or an allowlist entry, never loosening the rule.

OUT OF SCOPE, HONESTLY: this scanner checks US-vs-NZ spelling alternations
only. Macron correctness on te reo Māori (tohutō — e.g. catching "Maori" for
"Māori") is a *different* invariant from the same CONVENTIONS.md line and is
**not checked here** — it would need a te-reo wordlist this tool doesn't
have. Silently inferring macron coverage from the "NZ English with macrons"
grounding would be the same silent-failure class this scanner exists to
catch, so it is named rather than left implicit.

BORDERLINE, NOT-YET-REVIEWED. Named "borderline (cheapest scanner)" in the
mining record: the dedicated corpus findings are thin (2, +1 bundled) — the
promotion case rests on ROI (this is the cheapest scanner to write) plus a
spot-check showing "artifact" alone recurs 15+ times across `method/` docs
despite the house rule, i.e. the class is under-detected, not rare. Like
`datescan`, this has not yet earned an independent review, so wire it
advisory-only (`--warn`) and never into the blocking pre-commit hook until
reviewed.

THE DENYLIST — curated, not exhaustive. Two generative families (every
inflected form is derived from a stem list, not hand-typed, so there is one
source of truth per family and no typo'd inflection):

  * **-ize/-ization → -ise/-isation.** A curated stem list of common verbs
    that genuinely alternate between US "-ize" and NZ/UK "-ise" spellings
    (organize, synthesize, recognize, utilize, standardize, …). Each stem
    yields its bare/-s/-d/-ing forms; a second, smaller "noun-capable"
    subset additionally yields the regular "-ization"/"-izations" noun —
    deliberately NOT the full stem list, because several common verbs have
    an *irregular* noun with no NZ variant at all (recognize → recognition,
    not "recognisation"; synthesize → synthesis; emphasize → emphasis;
    criticize → criticism; apologize → apology; hypothesize → hypothesis;
    jeopardize → jeopardy; penalize → penalty). Inventing a wrong noun
    would be worse than missing a real one, so those stems stop at the verb
    forms — the verb `-ize`→`-ise` transform still fires for all of them,
    only the generated `-ization` noun is withheld. Words that are *always*
    spelled with a "z" in both dialects (size, seize, capsize, prize) are
    simply never on the stem list — there is no alternation to catch, so
    nothing to curate away.
  * **-yze/-yse → -yse.** A separate, smaller stem list (analyze, paralyze,
    catalyze) — same shape, kept apart because the letter that changes
    differs (y-z vs i-z) and because these three also have irregular nouns
    (analysis, paralysis, catalysis — spelled the same in both dialects, so
    no noun form is generated here either).

  * **Standalone irregular pairs.** Hand-listed because each has its own
    inflection quirks: artifact/artefact, color/colour (+ colored, coloring,
    colorful, colorless), behavior/behaviour (+ behavioral), defense/defence,
    center/centre (+ centered, centering), catalog/catalogue (+ cataloged,
    cataloguing), favor/favour (+ favorite, favorable), honor/honour
    (+ honorable), fulfill/fulfil (+ fulfillment/fulfilment — note
    fulfilled/fulfilling are identical in both dialects, so are NOT listed).

  * **Deliberately excluded (a judgement call, not an oversight): license/
    practice.** Both are US/NZ homograph pairs where American English
    collapses a noun/verb distinction NZ/UK keeps apart: NZ/UK spells the
    NOUN "licence" and the VERB "license" (same split for "practice" the
    noun vs "practise" the verb); American spells both "license"/
    "practice". A scanner with no part-of-speech tagging cannot tell "a
    driving license" (should be "licence") from "to license the software"
    (correctly "license" even in NZ) or from "MIT License"/
    "SPDX-License-Identifier" (a proper noun / fixed metadata key that is
    correctly "License" regardless of dialect). Guessing would trade a thin
    real signal for a noisy, wrong-most-of-the-time one — exactly the trade
    the house has already rejected once (sizescan's prose-cold-content
    residual). Left out, named here rather than silently absent.

EXEMPTIONS (a false positive costs a comment; a noisy scanner trains itself
away — the house's stated preference, same as datescan):

  * **Fenced code blocks** and **inline `code spans`** — stripped/skipped
    exactly as datescan does (identical `_content_lines`/`_strip_inline_code`
    helpers).
  * **Blockquoted lines** (`>` at the start) — quoted external text is not
    this repo's own spelling.
  * **URLs and file/dir paths.** Any whitespace-delimited token containing a
    "/" is blanked before matching — this mechanically covers a path
    (`docs/method/PRINCIPLES.md`) and most tool/action names
    (`actions/upload-artifact`) without needing per-term curation.
  * **A quote-flanked MENTION** (`"artifact"`) — the same USE-vs-MENTION
    heuristic as datescan: a denylisted word immediately surrounded by a
    matching pair of quote marks is prose *about* the word (a worked
    example, a naming discussion), not a live spelling claim.
  * **ALL-CAPS tokens** (`COLOR_RESET`, `LICENSE`) — read as an identifier,
    env var, or filename convention, not prose.
  * **A small, named ALLOWLIST_PHRASES** for known-legit bare-prose API/
    product/term-of-art phrases that would otherwise false-positive with no
    code span or slash to save them: GitHub's own feature/action names
    ("artifact attestations", "upload-artifact"/"download-artifact", written
    without a preceding `actions/`); the CI/build/release/SBOM sense of
    "artifact" ("release-artifact signing", "deployable-artifact"/
    "deployable artifact", "build-artifact", "artifact signing",
    "artifact-signing-now", "published artifact", "artifact layer" — the
    software-supply-chain term of art, where "artifact" is the industry-
    standard spelling even in NZ/UK technical prose, distinct from the
    *general* "a produced thing" sense (a session record, a web page),
    which stays flagged as a genuine NZ breach); and the OWASP ASVS/SAMM
    proper-noun chapter names ("Prepare the Organization", "Encoding &
    Sanitization", "Validation, Sanitization & Encoding") — a standards
    body's own published chapter titles are not this repo's prose to
    re-spell. Kept deliberately tiny: growing it is how a real miss gets
    buried, so a new entry should be added only for a confirmed proper-
    noun/API-term/term-of-art false positive, never to quiet a genuine
    prose spelling.
  * **The allow marker / ignore file** — `spellscan:allow: <reason>` on a
    line, or a glob in `.spellscanignore` — mirrors every sibling scanner.

STATED RESIDUAL, HONESTLY:

  * **Bare-prose API-term false positives are a known, structural limit.**
    "artifact" legitimately names a CI/CD build output, a GitHub product
    feature, or a tool ("actions/upload-artifact") — this scanner cannot
    distinguish that from ordinary NZ-English prose meaning "artefact"
    without a part-of-speech/entity model it doesn't have. The fix at a
    real site is to inline-code the term or add it to ALLOWLIST_PHRASES,
    **never** to loosen or drop the denylist entry.
  * The denylist is **curated, not exhaustive** — real US spellings outside
    it (practice/practise, "-yse" words not listed, rarer irregular nouns)
    pass silently. Promote-on-ROI, not promote-on-completeness, per the
    mining record's own framing of this scanner as borderline.
  * The quote-flanked MENTION heuristic is punctuation-shaped, not
    semantic, and the ALL-CAPS identifier exemption will also hide a
    genuinely mis-spelled SHOUTED heading — both accepted trade-offs, named
    rather than hidden, same honesty as datescan's stated limits.

Exit codes (fail-safe — anything but a clean scan is non-zero, UNLESS --warn):
  0  clean; or --warn was given (advisory rollout — never blocks)
  1  findings, and --warn was NOT given
  2  usage / config error (a broken scan is NOT a pass)

Zero third-party dependencies; stdlib only.
"""

from __future__ import annotations

import argparse
import codecs
import fnmatch
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

ALLOW_MARKER = "spellscan:allow"

ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<rule>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    `""` means everything on the line; a name means just that one. A marker
    with no reason returns None — a mention, not an exemption
    (`method/GUARDS.md`, rule c)."""
    m = ALLOW_RX.search(line)
    if not m:
        return None
    return m.group("rule") or ""


@dataclass
class Tally:
    """What the scan removed AFTER finding it — rule (b) of `method/GUARDS.md`."""
    by_marker: dict[str, int] = field(default_factory=dict)
    files_by_glob: int = 0
    # 020/380 — a physical line longer than `_MAX_LINE_BYTES` is scanned only
    # up to that cap (see `_iter_physical_lines`); counted so the truncation
    # is REPORTED rather than silent.
    lines_truncated: int = 0

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def note_marker(self, rule: str) -> None:
        self.by_marker[rule] = self.by_marker.get(rule, 0) + 1

    def note_line_truncated(self) -> None:
        self.lines_truncated += 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        line = ("  suppressed: "
                f"{self.marker_total} by allow-marker · "
                f"{self.files_by_glob} file(s) by .spellscanignore · "
                f"{self.lines_truncated} over-long line(s) scanned truncated")
        if self.by_marker:
            detail = ", ".join(f"{r}×{n}" for r, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        return line


MARKDOWN_SUFFIXES = {".md", ".markdown"}

SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# ---------------------------------------------------------------------------
# The -ize/-ization family. Bare US "-ize" verbs that genuinely alternate
# with NZ/UK "-ise" (see module docstring for why words like "size"/"seize"/
# "capsize" are never on this list — there's no alternation to catch).
IZE_VERB_BASES = [
    "organize", "recognize", "realize", "utilize", "standardize",
    "characterize", "initialize", "customize", "prioritize", "minimize",
    "maximize", "optimize", "summarize", "emphasize", "generalize",
    "finalize", "normalize", "specialize", "authorize", "synchronize",
    "synthesize", "modernize", "capitalize", "categorize", "apologize",
    "criticize", "memorize", "familiarize", "formalize", "legalize",
    "localize", "materialize", "mobilize", "neutralize", "rationalize",
    "sanitize", "socialize", "stabilize", "symbolize", "sympathize",
    "systematize", "visualize", "harmonize", "equalize", "civilize",
    "colonize", "idealize", "monopolize", "industrialize", "immunize",
    "jeopardize", "fantasize", "hypothesize", "mesmerize", "energize",
    "dramatize", "publicize", "penalize",
]

# Subset of the above whose regular "-ization" noun is a real, unambiguous
# word (not an irregular noun like recognize → recognition, or one better
# served by an unrelated word like apologize → apology). Deliberately a
# subset, not the full list — see the docstring's "inventing a wrong noun"
# note.
IZE_NOUN_CAPABLE = {
    "organize", "realize", "standardize", "characterize", "initialize",
    "customize", "prioritize", "minimize", "maximize", "optimize",
    "summarize", "generalize", "finalize", "normalize", "specialize",
    "authorize", "synchronize", "modernize", "capitalize", "categorize",
    "familiarize", "formalize", "legalize", "localize", "materialize",
    "mobilize", "neutralize", "rationalize", "sanitize", "socialize",
    "stabilize", "symbolize", "systematize", "visualize", "harmonize",
    "equalize", "civilize", "colonize", "idealize", "monopolize",
    "industrialize", "immunize", "memorize", "dramatize",
}

# The -yze/-yse family — kept separate because the alternating letter pair
# is "yz"/"ys", not "iz"/"is", and because all three have irregular nouns
# (analysis, paralysis, catalysis — identical in both dialects), so no noun
# form is generated.
YZE_VERB_BASES = ["analyze", "paralyze", "catalyze"]


def _ize_forms(base: str) -> dict[str, str]:
    """US inflections of an '-ize' bare verb → their NZ '-ise' equivalents.
    `base` ends in 'ize' (e.g. 'organize'); the stem is `base[:-1]` (drops
    the trailing 'e'). NZ form is always the US form with the *last* 'z'
    (the one in '-iz-') turned to 's' — inflection never adds another z."""
    stem = base[:-1]  # "organiz"
    us_forms = [base, stem + "es", stem + "ed", stem + "ing"]
    if base in IZE_NOUN_CAPABLE:
        us_forms += [stem + "ation", stem + "ations"]
    out: dict[str, str] = {}
    for us in us_forms:
        # Replace only the final 'z' — the one belonging to the -iz- root —
        # not any other 'z' (none of these stems have a second one, but stay
        # precise rather than a blind global replace).
        idx = us.rindex("z")
        nz = us[:idx] + "s" + us[idx + 1:]
        out[us] = nz
    return out


def _yze_forms(base: str) -> dict[str, str]:
    stem = base[:-1]  # "analyz"
    us_forms = [base, stem + "es", stem + "ed", stem + "ing"]
    out: dict[str, str] = {}
    for us in us_forms:
        idx = us.rindex("z")
        nz = us[:idx] + "s" + us[idx + 1:]
        out[us] = nz
    return out


# ---------------------------------------------------------------------------
# Standalone irregular pairs — each hand-listed because inflection doesn't
# follow a single mechanical rule shared across the family.
_STANDALONE_PAIRS: list[tuple[str, str]] = [
    ("artifact", "artefact"), ("artifacts", "artefacts"),
    ("color", "colour"), ("colors", "colours"), ("colored", "coloured"),
    ("coloring", "colouring"), ("colorful", "colourful"),
    ("colorless", "colourless"), ("colorfully", "colourfully"),
    ("behavior", "behaviour"), ("behaviors", "behaviours"),
    ("behavioral", "behavioural"), ("behaviorally", "behaviourally"),
    ("defense", "defence"), ("defenses", "defences"),
    ("center", "centre"), ("centers", "centres"),
    ("centered", "centred"), ("centering", "centring"),
    ("catalog", "catalogue"), ("catalogs", "catalogues"),
    ("cataloged", "catalogued"), ("cataloging", "cataloguing"),
    ("favor", "favour"), ("favors", "favours"), ("favored", "favoured"),
    ("favoring", "favouring"), ("favorite", "favourite"),
    ("favorites", "favourites"), ("favorable", "favourable"),
    ("favorably", "favourably"),
    ("honor", "honour"), ("honors", "honours"), ("honored", "honoured"),
    ("honoring", "honouring"), ("honorable", "honourable"),
    ("honorably", "honourably"),
    ("fulfill", "fulfil"), ("fulfills", "fulfils"),
    ("fulfillment", "fulfilment"),
]

# Assembled once at import time: the single lowercase US-word → NZ-word map
# every scan uses, sorted longest-first so alternation never lets a shorter
# entry shadow a longer one (not load-bearing today — no entry is a strict
# prefix of another with a word-boundary regex — but keeps the invariant
# honest, matching datescan's own note).
def _build_denylist() -> dict[str, str]:
    table: dict[str, str] = {}
    for base in IZE_VERB_BASES:
        table.update(_ize_forms(base))
    for base in YZE_VERB_BASES:
        table.update(_yze_forms(base))
    for us, nz in _STANDALONE_PAIRS:
        table[us] = nz
    return table


DENYLIST: dict[str, str] = _build_denylist()

_DENYLIST_RX = re.compile(
    r"\b(?:" + "|".join(re.escape(w) for w in
                         sorted(DENYLIST, key=len, reverse=True)) + r")\b",
    re.IGNORECASE)

# Known-legit bare-prose terms that would otherwise false-positive with no
# code span or path slash to save them. Kept tiny and documented — see the
# module docstring's "growing it is how a real miss gets buried" note.
ALLOWLIST_PHRASES = [
    # GitHub's own feature/action names.
    "artifact attestations",
    "upload-artifact",
    "download-artifact",
    # The CI/build/release/SBOM software-supply-chain sense of "artifact" —
    # an industry-standard term of art, not this repo's prose to re-spell.
    # The *general* "a produced thing" sense (a session record, a web page)
    # is deliberately NOT here — it stays flagged as a genuine NZ breach.
    "release-artifact signing",
    "release-artifact",
    "deployable-artifact",
    "deployable artifact",
    "build-artifact",
    "artifact signing",
    "artifact-signing-now",
    "published artifact",
    "artifact layer",
    "artifacts* + a deterministic sbom",
    # OWASP ASVS/SAMM proper-noun chapter names — a standards body's own
    # published chapter titles, not this repo's own prose.
    "prepare the organization",
    "encoding & sanitization",
    "validation, sanitization & encoding",
]

_QUOTE_PAIRS = {'"': '"', "'": "'", "“": "”", "‘": "’"}

_FENCE = re.compile(r"^(`{3,}|~{3,})")

# A whitespace-delimited token — used to find and blank a path/URL-shaped
# token (see `_strip_paths_and_urls`).
#
# 020/380: the ORIGINAL approach matched the whole path/URL shape directly —
# `\S*/\S+` — but that pattern is O(n^2) REGARDLESS of the prefix's exact
# character class. `X*` followed by a required literal that never occurs
# forces the engine to backtrack `X*` one character at a time — O(line
# length) — at EVERY one of the O(line length) starting positions `.sub()`
# tries once a position fails, which is O(n^2) however narrowly `X` is
# defined (tightening `\S*` to `[^\s/]*`, tried first while building this
# fix, only removed the class OVERLAP, not the backtracking itself — it
# measured just as slow: 1.8s at 20,000 characters with no "/" anywhere).
# Measured on the ORIGINAL pattern: 21.5s for a single 100,000-character
# token — the exact cause of `spellscan one-huge-line` timing out past the
# board item's own 120s measurement-harness ceiling.
#
# The fix tokenises FIRST (`\S+`, a single quantified class with nothing
# after it to fail and force reconsideration — no backtracking possible) and
# then checks each token for "/" with Python's native `in`, which is a
# single linear scan with no regex engine involved. Total cost is one
# tokenising pass plus one substring scan per token — genuinely O(n).
_TOKEN_RX = re.compile(r"\S+")


@dataclass
class Finding:
    path: str
    line: int
    kind: str          # always "us-spelling"
    match: str          # the matched text, as written
    suggestion: str     # the NZ spelling, case-matched to the original
    detail: str


def _content_lines(text: str):
    """Yield (lineno, line) outside fenced code blocks. Identical fence
    pairing to datescan/linkscan: a fence closes only on a run of the same
    character at least as long as the opener, with no trailing info string."""
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
    """Blank inline `code spans` (length preserved). Identical to datescan/
    linkscan's helper — backtick runs must match in length (CommonMark)."""
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


def _strip_paths_and_urls(line: str) -> str:
    """Blank any whitespace-delimited token containing a '/' (length
    preserved) — the mechanical URL/path exemption (see module docstring).

    HONEST, NARROW behaviour widening from the pre-020/380 regex (see
    `_TOKEN_RX`'s comment for why it had to change): a token that is
    NOTHING BUT a trailing "/" with no character after it within the same
    whitespace-delimited run (`abc/` followed by whitespace or end-of-line)
    is now blanked too — the old `\\S*/\\S+` required at least one non-
    whitespace character AFTER the "/" and so left that one shape alone.
    Accepted: a token ending in a bare "/" is not real prose to spell-check
    either way, and this is a WIDER exemption, never a narrower one — it
    cannot cause a US spelling to go unflagged that used to flag; it can
    only additionally hide a shape (a bare trailing slash) that was never a
    denylisted word to begin with."""
    def repl(m: "re.Match[str]") -> str:
        token = m.group(0)
        return " " * len(token) if "/" in token else token
    return _TOKEN_RX.sub(repl, line)


def _is_quoted_mention(line: str, start: int, end: int) -> bool:
    """USE-vs-MENTION by punctuation, identical heuristic to datescan: a
    match immediately flanked by a matching quote-mark pair is prose ABOUT
    the word, not a live spelling claim."""
    before = line[start - 1] if start > 0 else ""
    after = line[end] if end < len(line) else ""
    return before in _QUOTE_PAIRS and after == _QUOTE_PAIRS[before]


def _in_allowlist_phrase(line_lower: str, start: int, end: int) -> bool:
    for phrase in ALLOWLIST_PHRASES:
        i = line_lower.find(phrase)
        while i != -1:
            if i <= start and end <= i + len(phrase):
                return True
            i = line_lower.find(phrase, i + 1)
    return False


def _match_case(original: str, nz: str) -> str:
    """Case-match the suggestion to the matched word: Title-case if the
    original was Title-cased, otherwise lowercase (an ALL-CAPS original
    never reaches here — it's exempted before this is called)."""
    if original[:1].isupper():
        return nz[:1].upper() + nz[1:]
    return nz


# Streaming-read tuning (020/380, reusing 020/370's secretscan shape — see
# `tools/secretscan.py`'s `_iter_numbered_lines`, duplicated rather than
# imported so this scanner stays copyable alone). `_MAX_LINE_BYTES` is
# two-plus orders of magnitude past any realistic wrapped-prose line — real
# content is never truncated; it exists to bound the pathological case (one
# absurd multi-MB "line") to a fixed, cheap constant instead of letting it
# scale with the file. It also caps the worst case of the (now-fixed, see
# `_PATH_OR_URL_RX`) quadratic regex cost to a small, bounded amount per
# line, as defence in depth against any OTHER pattern in this file turning
# out to share that shape.
_READ_CHUNK_BYTES = 1 * 1024 * 1024
_MAX_LINE_BYTES = 8 * 1024


def _iter_physical_lines(path: Path):
    """Yield `(lineno, text, truncated)` for every physical line in `path`,
    reading and decoding it in fixed-size chunks so peak memory for ONE file
    is bounded by `_MAX_LINE_BYTES` (plus one read chunk in flight) —
    independent of the file's total size or its longest line. Replaces the
    old `read_text()` whole-file string → `text.splitlines()` whole-file
    list, which held the file's content twice over at once (measured while
    building this fix: ~94 MB of growth for a 23 MB larger many-line file)."""
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    lineno = 1
    pending = ""
    truncated = False

    def feed(text: str):
        nonlocal lineno, pending, truncated
        while text:
            nl = text.find("\n")
            piece, text = (text, "") if nl == -1 else (text[:nl], text[nl + 1:])
            room = _MAX_LINE_BYTES - len(pending)
            if room > 0:
                pending += piece[:room]
            if len(piece) > max(room, 0):
                truncated = True
            if nl != -1:
                yield lineno, pending, truncated
                lineno += 1
                pending = ""
                truncated = False

    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(_READ_CHUNK_BYTES)
            if not chunk:
                break
            yield from feed(decoder.decode(chunk))
    tail = decoder.decode(b"", final=True)
    if tail:
        yield from feed(tail)
    if pending or truncated:
        yield lineno, pending, truncated


def _content_lines_from_file(path: Path, tally: "Tally | None" = None):
    """Streaming equivalent of `_content_lines`: same fence-pairing state
    machine, sourced from `_iter_physical_lines` instead of a whole-file
    `text.splitlines()` list (020/380). A truncated over-long line is scanned
    only up to the cap; the truncation is counted, never silent."""
    in_fence = False
    fence_char = ""
    fence_len = 0
    for lineno, line, truncated in _iter_physical_lines(path):
        if truncated and tally is not None:
            tally.note_line_truncated()
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


def scan_text(path: str, text: str, tally: "Tally | None" = None) -> list[Finding]:
    return _scan_numbered_lines(path, _content_lines(text), tally)


def scan_file(path: Path, rel: str, tally: "Tally | None" = None) -> list[Finding]:
    """Bounded-memory disk variant of `scan_text` (020/380): streams `path`
    in fixed-size chunks instead of reading it whole — see
    `_iter_physical_lines`. A file that vanishes/becomes unreadable mid-walk
    reports nothing from it, matching the old `read_text()` behaviour's own
    lack of a per-file guard."""
    try:
        return _scan_numbered_lines(rel, _content_lines_from_file(path, tally), tally)
    except OSError:
        return []


def _scan_numbered_lines(path: str, numbered_lines, tally: "Tally | None" = None) -> list[Finding]:
    findings: list[Finding] = []
    # Line -> allowance scope. Recorded, not acted on, so the finding forms
    # first and the exemption is counted rather than vanishing (rule b).
    allow_by_line: dict[int, str] = {}
    for lineno, raw_line in numbered_lines:
        scope = parse_allow(raw_line)
        if scope is not None:
            allow_by_line[lineno] = scope
        if _is_blockquote(raw_line):
            continue
        line = _strip_inline_code(raw_line)
        line = _strip_paths_and_urls(line)
        line_lower = line.lower()

        for m in _DENYLIST_RX.finditer(line):
            word = m.group(0)
            if word.isupper() and len(word) > 1:
                continue  # ALL-CAPS: identifier/env-var/filename convention
            if _is_quoted_mention(line, m.start(), m.end()):
                continue
            if _in_allowlist_phrase(line_lower, m.start(), m.end()):
                continue
            nz = DENYLIST[word.lower()]
            suggestion = _match_case(word, nz)
            findings.append(Finding(
                path, lineno, "us-spelling", word, suggestion,
                f"US spelling — NZ-English prose uses {suggestion!r}"))
    # SUBTRACT SECOND. The scope names the WORD (`spellscan:allow:color:`),
    # which is the narrowest unit this scanner has: a marker written for one
    # US spelling must not also exempt a different one on the same line.
    kept: list[Finding] = []
    for f in findings:
        scope = allow_by_line.get(f.line)
        if scope is not None and scope.lower() in ("", f.match.lower()):
            if tally is not None:
                tally.note_marker(f.match.lower())
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
    """Globs from `.spellscanignore`, each of which MUST carry a stated reason.

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
    f = root / ".spellscanignore"
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
        raise IgnoreFileError(".spellscanignore", unreasoned)
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
    """Every regular file under `base`, streamed one at a time via `os.walk`,
    pruning skip-dirs in place so the walk never descends into them at any
    depth (020/380, reusing secretscan's `_walk_files` shape). Replaces
    `base.rglob("*")` funnelled through a list comprehension, which forced
    Python to enumerate the ENTIRE subtree and hold every `Path` before a
    single file was even considered."""
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_file():  # excludes broken symlinks, matching the old rglob filter
                yield p


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  tally: "Tally | None" = None):
    for base in paths:
        candidates = [base] if base.is_file() else _walk_files(base)
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
        findings.extend(scan_file(md, _rel(md, root), tally))
    return findings


def render_human(findings: list[Finding], tally: "Tally | None" = None) -> str:
    if not findings:
        out = "✓ spellscan clean — no US spellings found."
        return out + ("\n" + tally.summary() if tally is not None else "")
    lines = [f"✗ spellscan: {len(findings)} finding(s)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.match!r} → {f.suggestion!r}")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A real US spelling: replace with the NZ-English form.")
    lines.append(f"  A legit API/tool term: inline-code it, add to ALLOWLIST_PHRASES,")
    lines.append(f"  or append '<!-- {ALLOW_MARKER}: <reason> -->' to the line, or add")
    lines.append("  a path glob to .spellscanignore.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="spellscan",
        description="Check docs/** for US spellings with a curated NZ-English "
                    "equivalent (NZ-English prose discipline).")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: <root>/docs if present, "
                         "else the whole root)")
    ap.add_argument("--root", default=".",
                    help="repo root for .spellscanignore and relative paths")
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
        print(f"spellscan: root does not exist: {args.root}", file=sys.stderr)
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
        print(f"spellscan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    tally = Tally()
    try:
        findings = scan_paths(targets, root, tally)
    except OSError as e:
        print(f"spellscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
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
    """Minimal smoke test so `spellscan --selftest` proves the engine on any
    box, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="spellscan-self-"))
    (tmp / "docs").mkdir()
    (tmp / "docs" / "note.md").write_text(
        "# Note\n\n"
        "The build artifact was organized and synthesized this way.\n"  # 3 hits
        "Stamped in colour and licence, all NZ-English already.\n"       # clean
        "`artifact` is just an example in code.\n"                       # code span, exempt
        "> quoted external text says color, verbatim.\n"                 # blockquote, exempt
        "```\nartifact stays artifact in this fenced block\n```\n"       # fenced, exempt
        "see docs/method/artifact-notes.md for the path.\n"               # path, exempt
        "the term \"artifact\" is discussed here as a naming choice.\n"  # quoted mention, exempt
        "read the GitHub artifact attestations feature docs.\n"          # allowlist phrase, exempt
        "the env var COLOR is an identifier, not prose.\n"               # ALL-CAPS, exempt
        "allowed color  <!-- spellscan:allow: selftest fixture -->\n"    # allow marker, exempt
    )
    findings = scan_paths([tmp / "docs"], tmp)
    matches = sorted(f.match.lower() for f in findings)
    expected = sorted(["artifact", "organized", "synthesized"])
    ok = matches == expected
    if not ok:
        print(f"FAIL: got {matches}, expected {expected}")

    if main(["--warn", "--root", str(tmp), str(tmp / "docs")]) != 0:
        print("FAIL: --warn should always exit 0")
        ok = False
    if main(["--root", str(tmp), str(tmp / "docs")]) != 1:
        print("FAIL: findings without --warn should exit 1")
        ok = False
    clean = tmp / "clean"
    clean.mkdir()
    (clean / "ok.md").write_text("# OK\n\nAll NZ-English: colour, licence, organise.\n")
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
        print(f"spellscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())

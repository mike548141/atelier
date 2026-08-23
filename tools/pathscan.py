#!/usr/bin/env python3
"""pathscan — the mechanical check that a NAMED repo path resolves.

The rule (2026-07-22 invariant-candidates review, seam S2): a doc that names a
repo path — a directory, a file, a template dir — must have that path exist,
whether the reference is a Markdown link *or bare prose*. `linkscan` already
resolves Markdown `[text](path)` links; this scanner's new value is the other
half — a path NAMED in running prose or wrapped in a single backtick span,
with no `](...)` around it at all. The occurrences that motivated this (S2's
own citations): `foundation H2` (a README listing `docs/decisions/` before it
existed), `post-method B14` (an ACCESS pointer at a map that doesn't exist),
`post-method B11` ("seed from `templates/`" — no such dir). All three are bare
prose, none is a Markdown link — exactly the gap `linkscan` cannot see.

STATUS — WIRED ADVISORY, REVIEWED ONCE, NOT GATING. It is invoked from
`ci.yml` with `--warn` (never blocks), and is NOT in `tools/floor.py`'s
registry — a bespoke step, which the review flagged (PS5) as the
vendored-policy shape the registry exists to end; promoting it is a later,
separate phase. Its first-of-kind cold review (rule 4, Fable, 2026-07-26)
returned PASS-WITH-FINDINGS — 3 MAJOR, 5 MINOR — and recommended KEEPING IT
ADVISORY until four preconditions land. This delta is the funded rescope
(Mike's ruling, 2026-08-04) discharging three of them: the fourth anchor and
root-file scope (PS1), the gated-surface residual burn-down (one true
positive fixed, the false positives marked), and the docstring corrections
(PS2, PS3, PS6, PS7, PS8). Registry promotion (PS5) is explicitly deferred.
THE FLIP TO BLOCKING IS STILL A DECISION, not this build's to take.

THE CHECK, deliberately narrow (a broad flaky path-guesser is worse than a
sharp honest one):

  1. Read each Markdown file outside fenced (``` ```) code blocks — a fenced
     block is an illustrative example, not a live claim (matches every
     sibling scanner). Only FENCED blocks are exempt: an INDENTED (four-space)
     code block is still scanned, so a path inside one is a live claim as far
     as this scanner is concerned. That is a knowing limit, not an oversight —
     the sibling scanners share it — but it is worth stating plainly here
     because step 1's rationale ("a fenced block is an illustrative example")
     would otherwise read as if example-exemption were general.

  2. Blank out two things that are NOT this scanner's job before hunting for
     candidates, so their content can't seed a false one:
       - ANGLE-BRACKET PLACEHOLDERS, `<...>` — `<repo>/docs/foo.md` is an
         illustrative slot-filler, not a real pointer (the S2 rule's own
         "angle-bracket placeholders" exemption). The whole bracketed span is
         blanked, which also stops its tail (`/docs/foo.md`) being picked up
         as a bare candidate — see BLIND SPOT below on why that is a
         deliberate trade, not an oversight.
       - MARKDOWN LINK DESTINATIONS, `](dest)` — already `linkscan`'s job.
         Blanking the destination (not the link TEXT before it) keeps this
         scanner from re-litigating what `linkscan` already owns, while
         still catching a backtick-wrapped path sitting in the visible link
         text (`` [see `docs/foo.md`](docs/foo.md) `` — the text half is
         still scanned).
       - SCHEME URLS (`https://…`, `mailto:…`) and PROTOCOL-RELATIVE
         (`//host/…`) — external, not this repo's filesystem; a different
         tool's job (same exemption `linkscan` states).

  3. Over what remains — bare prose AND single-backtick `` `code span` ``
     text alike (deliberately NOT stripped, unlike the sibling scanners:
     backtick-wrapping a path is this house's *normal* way to name one in
     running prose, not an "it's just an example" signal) — find PATH-SHAPED
     tokens: two or more `/`-separated segments of word/dot/hyphen
     characters. A single trailing sentence period is trimmed (`` `foo.md`. ``
     at a sentence's end must not read as target `foo.md.`).

  4. A path-shaped token is a CANDIDATE only if it starts with a known
     top-level repo directory (`docs/`, `tools/`, `skills/`, `commands/`,
     `instruments/`, `.github/`, `.claude/`, `.claude-plugin/`) OR ends in a
     known doc/code extension (`.md`, `.markdown`, `.py`, `.yml`, `.yaml`,
     `.json`, `.sh`, `.txt`). This is the load-bearing heuristic — see
     DETECTION HEURISTIC below for why, and its stated failure modes.

  5. A candidate is resolved against FOUR anchors, and passes if it exists
     under ANY of them (see `_resolves` for the full rationale):
       - the SCAN ROOT — `README.md` at the repo root writes `docs/decisions/`
         root-relative;
       - the CANDIDATE FILE's OWN DIRECTORY — matches `linkscan`'s
         link-relative convention;
       - for a file UNDER `docs/`: the OUTERMOST ENCLOSING `docs/` DIRECTORY,
         at whatever depth the referencing file sits — a doc
         `docs/build/REPO-STANDARD.md` still writes `method/RECORD.md` meaning
         `docs/method/RECORD.md`, dropping the `docs/` prefix regardless of
         its OWN nesting under `docs/build/` (OUTERMOST, not nearest — see
         `_outermost_named_ancestor` on why: `docs/build/templates/docs/` is
         itself a nested `docs`-named dir);
       - for a file NOT under `docs/`: `<root>/docs/` — DOCS-RELATIVE
         SHORTHAND, the dominant convention in this house's ROOT files. A root
         `README.md` or `CHANGELOG.md` writes `method/REVIEW.md` meaning
         `docs/method/REVIEW.md` exactly the way a doc inside `docs/` does;
         it just has no `docs/` ancestor for anchor 3 to find. Without this
         anchor the root files a gate most wants to cover false-positive
         wholesale (51 of 64 findings on the doctrine surface + root `*.md`
         were this one shape before it was added).
     Each candidate is also retried with `.md`/`.markdown` APPENDED under
     every anchor when the token has no extension at all — GitHub's
     directory-index convention, so `tools/README` finds `tools/README.md`
     (see STATED RESIDUAL for the silent-mask cost this buys).
     Running this scanner over the live repo found anchors 3 and 4 were not
     optional. Widening what counts as "resolves" can only ever DROP a
     finding, never invent one: a genuinely broken path fails under all four
     and is still flagged. The flip side is a real, named cost — see the
     silent-false-negative bullet under STATED RESIDUAL.

DETECTION HEURISTIC — the genuinely hard, judgement-heavy part, stated
honestly, not rounded up:

  Distinguishing "a real repo-path reference that should resolve" from
  "arbitrary prose that happens to contain a slash" has no clean rule. The
  heuristic chosen — known-top-dir-prefix OR known-extension-suffix — was
  picked because it is the cheapest test that rejects the dominant false-
  positive shape (an ordinary fraction, ratio, or date-as-numerals: `3/4`,
  `50/50`, `23/07/2026` start with neither a repo dir nor end in a doc
  extension, so none of them become candidates) while still catching two of
  the three cited occurrences (`docs/decisions/` and the ACCESS-style
  pointer) without a repo-specific allowlist of "real" paths to maintain.

  THE THIRD CITED OCCURRENCE IS NOT CAUGHT, and an earlier version of this
  paragraph claimed it was. B11 as the intent record states it — "seed from
  `templates/`" — is a SINGLE-segment token, and `_PATH_TOKEN` requires two
  or more `/`-separated segments, so it yields no candidate at all. The
  single-segment floor is itself a deliberate, defensible choice (see the
  first FALSE NEGATIVE below); the overclaim was the defect, and it is
  corrected here rather than quietly dropped.

  FALSE POSITIVES (a candidate that isn't really a repo-path claim), named:
    - A path-shaped mention of ANOTHER project's tree that happens to share a
      known extension or a coincidental top-dir-shaped prefix (e.g. a worked
      example describing a *different* repo's `docs/method.py`) will be
      checked against THIS repo and flagged if absent, even though the prose
      never claimed it lives here.
    - A version-like or identifier-like token that happens to end in a known
      extension by coincidence has no realistic example in this corpus, but
      is not ruled out by construction.
    - The extension-suffix leg alone (with no top-dir prefix) is the noisier
      of the two — `some/other/thing.py` is a candidate purely because it
      ends `.py`, even in a sentence not making a repo-path claim at all.

  FALSE NEGATIVES (a real broken reference this scanner will NOT catch),
  named:
    - A single-segment top-level file mentioned with no directory at all
      (`see LICENSE`, `read CLAUDE.md`) never matches — the token regex
      requires at least one `/`, a deliberate floor against flagging every
      dotted abbreviation and version number in ordinary prose ("e.g.",
      "v1.2.3") as a one-segment "path".
    - A path built by string concatenation, a variable, or split across a
      line-wrap is invisible to a line-local regex. The same line-local limit
      applies to the BLANKING pass of step 2, in the opposite direction: an
      angle-bracket placeholder span that WRAPS across a line break is never
      matched by `_ANGLE_PLACEHOLDER`, so a path sitting inside it is not
      blanked and is scanned as if it were a live claim — a false POSITIVE
      arising from the same one-line horizon. The date-placeholder exemption
      below covers the common shape of this; the allow marker covers the rest.
    - EMPHASIS-WRAPPED paths are invisible: `**docs/x.md**`, `*docs/x.md*`
      and `_docs/x.md_` all fail to match, because `_PATH_TOKEN`'s lookbehind
      excludes `*`, and an underscore is itself a word character, so no match
      can start inside the emphasis run. Emphasis PLUS backticks — the shape
      `` **`docs/x.md`** `` — IS caught: the backticks give a clean
      boundary. Emphasis runs are not stripped before token-hunting: the
      house names paths in backticks, so this shape is rare here, and
      stripping `*`/`_` runs correctly (they nest, and `_` is legal inside a
      filename) is more machinery than the class earns. A named gap, not a
      fixed one.
    - A genuinely broken path sharing a line with a `TODO` cue about
      something ELSE scans clean. The stub exemption below is LINE-level by
      design (the narrowing is stated there), and this is its cost:
      ``fix `docs/ghost.md` — TODO tidy this prose later`` yields no finding
      even though the TODO was never about the path.
    - A genuinely broken reference that avoids both legs of the heuristic —
      no known top-dir prefix, no known extension (a bare directory name with
      no extension, one level deep, e.g. a made-up `foo/bar` with neither
      cue) — scans clean. This is the accepted cost of a heuristic that does
      not hard-code every real directory name as a second allowlist.
    - Leading `/` ROOT-ANCHORED bare-prose mentions (`/docs/x.md`,
      `/.well-known/security.txt`) are not picked up as candidates: the
      token regex's lookbehind excludes `/`, so no match can start at the
      first segment of such a path. Same shape as the angle-bracket blind
      spot above — distinguishing a genuine root-relative repo mention from
      a site URL path or the tail of a just-blanked placeholder is not
      attempted; all of them are skipped rather than guessed at. Note the
      leading `/` is the ONLY reason they are skipped, not "the match must
      start at a word character": the token class also admits `.`, `-`, `*`
      and `?` as a first character, so `.github/workflows/ci.yml` in bare
      prose IS a candidate.
      UNTIL 2026-08-10 THIS BULLET DESCRIBED AN INTENT THE CODE DID NOT
      HONOUR (E8, reported by a child repo). The skip was not whole: a
      hyphen anywhere before the token's last `/` let the match resync
      mid-path, so `/.well-known/security.txt` was extracted as
      `known/security.txt` and reported missing — a truncated path nobody
      wrote, flagged against a file that existed. `/docs/x.md` (no hyphen)
      really was skipped, which is why the class hid behind a bullet that
      read as true. Fixed at the regex, not at the call site: see
      `_PATH_TOKEN`'s comment for the invariant that closes it.

  The fabricated-quote subset of the S2 proposal (`foundation H3` — a quote
  attributed to a doc that never said it) is explicitly OUT OF SCOPE per the
  brief: it requires reading semantic meaning, not resolving a path, and
  stays review-only.

EXEMPTIONS, same three-layer shape as the sibling scanners:

  * STUB / DELIBERATELY-FUTURE PATHS. If the SAME LINE carries a `TODO` cue
    (case-insensitive, e.g. `<!-- TODO -->`) or the literal phrase
    "(none yet)" (case-insensitive), the whole line is exempt — the doc is
    explicitly flagging the path as not-yet-real, not silently claiming it
    exists. Narrowed to the same line, not a fuzzy "nearby" window: a
    line-local cue is unambiguous; guessing whether a cue two lines up still
    applies is not (an honest narrowing, not a rounding-up).
  * ILLUSTRATIVE / PLACEHOLDER PATHS. A token containing a glob wildcard
    (`*` or `?`) is skipped (`src/**/*.go`); a token starting with the literal
    `path/to` (case-insensitive) is skipped (the S2 rule's own named
    placeholder shape); angle-bracket-wrapped spans are blanked before
    candidate-hunting even starts (see THE CHECK, step 2); a token
    immediately followed by an ellipsis (`…` or `...`) is skipped — a
    "truncated for brevity" marker, e.g. `` `docs/reviews/2026-07-10-…` ``
    (found live on this repo's own baseline run), the same shape-not-claim
    signal as `path/to/thing`; and a token carrying a DATE/TIME PLACEHOLDER
    segment — the literal uppercase `YYYY` or `HHMM` — is skipped, because
    `docs/reviews/YYYY-MM-DD-HHMM-slug.md` is a naming-convention TEMPLATE,
    not a claim that some file of that literal name exists. Deliberately
    narrow: only `YYYY` and `HHMM` are cues. `MM` and `DD` alone are not,
    because two-letter uppercase runs occur in ordinary filenames and would
    exempt real paths; a template that reaches for `MM`/`DD` in practice
    always writes `YYYY` first.
  * THE ALLOW MARKER / IGNORE FILE. `pathscan:allow: <reason>` anywhere on a
    line exempts every candidate on that line — same tightened contract as
    `datescan` (word-boundary, colon, non-empty reason so a bare mention of
    the marker text doesn't accidentally exempt itself). A glob in
    `.pathscanignore` at the scan root exempts a path wholesale.

STATED RESIDUAL, HONESTLY (do not round this to "solved" or "clean"):

  * This is a FIRST-OF-KIND heuristic, reviewed ONCE (see STATUS above). Its
    accuracy is bounded, not proven — see DETECTION HEURISTIC above for the
    named false-positive and false-negative shapes, several of which the
    review added because the first version of this header missed them. A
    noisy baseline over this repo's own RECORDS is EXPECTED and permanent,
    not a bug to silently round away; see SCOPE below for which surface that
    noise does and does not live on.
  * Four-anchor resolution (root / own-directory / enclosing-docs / root-docs,
    see THE CHECK step 5) closes the dominant noise sources found on this
    repo's own corpus, but is still a fixed set of heuristic anchors, not a
    grammar: a path meant relative to some OTHER file's directory, or a
    repo whose doc tree isn't named `docs/`, still won't resolve and is
    flagged even if a human reader would understand it from context. The
    `docs` name is hard-coded in anchors 3 and 4 — atelier-shaped, and a
    stated residual for any adopter whose doc tree is named otherwise.
  * SILENT FALSE NEGATIVE, the price of every widening above: because a
    candidate passes if it resolves under ANY anchor, a reference that is
    genuinely WRONG can be masked by a same-named file under a different
    anchor. `method/RECORD.md` written from a root file, meaning some other
    repo's `method/RECORD.md`, resolves against `<root>/docs/` and scans
    clean. The scanner checks EXISTENCE SOMEWHERE, not correctness — it can
    prove a path is broken, never that it is right.
  * A bare mention with no extension at all (`tools/README`,
    `instruments/README` — GitHub's directory-index convention) IS now
    retried with `.md`/`.markdown` appended under every anchor, so
    `tools/README` finds `tools/README.md`. Monotone-safe (it can only drop
    findings) and grounded in the convention, not in the count. Its cost is
    the masking class above in miniature: a reference to a genuinely absent
    DIRECTORY `foo/bar` scans clean if a file `foo/bar.md` happens to exist.
    Only a fully extensionless token is retried; `docs/decisions/0001` is
    tried as `0001.md` and, no such file existing, stays flagged.
  * Directories and files are both accepted as "resolves" — a candidate
    ending in a known extension that turns out to be a directory on disk (or
    vice versa) is NOT distinguished; only existence is checked, matching
    `linkscan`'s own file-vs-directory looseness.
  * SCOPE, and why the default is not the whole story. With no paths given
    the scanner walks `<root>/docs` (mirrors `datescan`); code comments,
    commit messages, and non-Markdown prose are out of scope entirely. But
    `docs/` alone CANNOT SEE THIS SCANNER'S OWN MOTIVATING CASE — S2's first
    citation is a ROOT README naming `docs/decisions/`. Root-level `*.md`
    files are fully scannable (pass them as explicit paths) and, since
    anchor 4, they come back clean rather than false-positiving wholesale.
    The scope a GATE should bind on is therefore the DOCTRINE SURFACE plus
    the root files that are live doctrine — `docs/method docs/build
    docs/decisions README.md CLAUDE.md SECURITY.md` — all of it prose that
    is true NOW and must resolve NOW.
    RECORDS are deliberately NOT gateable, and that includes two root-level
    `*.md` files: `CHANGELOG.md` and `ROADMAP-DONE.md` are records as much
    as `docs/reviews/` and `docs/sessions/` are. A record legitimately names
    the tree as it stood when it was written — since-renamed tools, other
    repos' trees, ephemeral worktrees, gitignored paths — and this scanner
    has no time axis, so records can never come clean without mass
    allow-markers that would falsify the record itself. Scan them advisory
    or not at all. So `*.md` at the root is NOT the right gate glob; name
    the live root files. Where the gate is actually wired is a decision for
    the caller, not a claim made here.

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
# that line. Same tightened contract as datescan (DSR8): word boundary, then
# a colon and a non-empty reason, so a bare mention of the marker text alone
# does not silently exempt the line.
ALLOW_MARKER = "pathscan:allow"
ALLOW_MARKER_RX = re.compile(r"\b" + re.escape(ALLOW_MARKER) + r":\s*[\w\"\'“‘]")

ALLOW_SCOPE_RX = re.compile(
    r"\b" + re.escape(ALLOW_MARKER) + r"(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(line: str) -> str | None:
    """The scope of the line's allow-marker, or None if it carries none.

    `""` is the only scope: this scanner has one finding kind, so the line
    already IS the narrowest allowance and a sub-rule would be ceremony
    rather than narrowness (`method/GUARDS.md`, rule a).
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
    files_by_records: int = 0

    @property
    def marker_total(self) -> int:
        return sum(self.by_marker.values())

    def note_marker(self, kind: str) -> None:
        self.by_marker[kind] = self.by_marker.get(kind, 0) + 1

    def summary(self) -> str:
        """One stable line, known zeros printed, so two runs compare."""
        line = ("  suppressed: "
                f"{self.marker_total} by allow-marker · "
                f"{self.files_by_glob} file(s) by .pathscanignore · "
                f"{self.files_by_records} record file(s) excluded by default")
        if self.by_marker:
            detail = ", ".join(f"{k}×{n}" for k, n in sorted(self.by_marker.items()))
            line += f"\n    allow-marker breakdown: {detail}"
        return line


# Only these extensions are scanned as SOURCE files — dated/dotted repo docs,
# not code or config elsewhere. Matches linkscan/datescan's MARKDOWN_SUFFIXES.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

# Paths never worth walking — VCS, dependency, and tool-cache dirs. Matches
# the sibling scanners (see linkscan.py's header for why an ambiguous name
# like `build`/`dist` is deliberately absent from this list).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache",
                  ".idea", ".vscode"}

# Known top-level repo directories. A candidate path starting with one of
# these is very likely a genuine repo-path claim, not incidental prose.
KNOWN_TOP_DIRS = (
    "docs/", "tools/", "skills/", "commands/", "instruments/",
    ".github/", ".claude/", ".claude-plugin/",
)

# Known doc/code file extensions. A candidate path ENDING in one of these,
# even without a known top-dir prefix, is likely a genuine file reference —
# the noisier of the two legs (see header's DETECTION HEURISTIC).
KNOWN_EXTENSIONS = (
    ".md", ".markdown", ".py", ".yml", ".yaml", ".json", ".sh", ".txt",
)

# A path-shaped token: 2+ segments joined by `/`, not preceded by another
# such character (so it's matched whole, not as a substring of a longer
# run). The character class includes `*` and `?` so a glob example
# (`src/**/*.go`) is captured WHOLE — letting the placeholder filter (which
# checks for those characters) see them, rather than the regex silently
# truncating the token before the wildcard and leaving a shorter, innocent-
# looking candidate behind. The lookbehind EXCLUDES `*`/`?` too (not just
# `\w./`) for the same reason — without it, a match could spuriously START
# right after a wildcard character (e.g. `toolu_*.txt/.json` splitting into
# a truncated `.txt/.json` candidate, found live on this repo's own baseline
# run), defeating the very placeholder check the whole-token capture above
# was for. Deliberately excludes a leading `/` via the lookbehind — a
# leading `/` (root-relative, or the tail of a just-blanked `<placeholder>`)
# is out of scope, see the header's named false-negative.
#
# THE LOOKBEHIND MUST EXCLUDE EVERY CHARACTER THE TOKEN CLASS ACCEPTS, plus
# `/`. That is the whole invariant, and the ONE character missing from it —
# the hyphen — was a real defect (E8, reported by a child repo 2026-08-09,
# fixed 2026-08-10). A run of token characters is only ever blocked at its
# START by a preceding `/`, because every other lookbehind character is
# itself in the token class and so would have been consumed as part of the
# same run. So a hyphen inside a `/`-anchored run was the one place a match
# could resync mid-token: `/.well-known/security.txt` yielded
# `known/security.txt` — a path nobody wrote, reported missing against a file
# that plainly existed. Same shape as the `*`/`?` hole above, same fix. The
# leading-`/` skip is therefore now what the header always claimed it was:
# the token is skipped WHOLE, never truncated into a plausible-looking lie.
_PATH_TOKEN = re.compile(r"(?<![\w.\-/*?])[\w.\-*?]+(?:/[\w.\-*?]+)+")

# Angle-bracket placeholder span, e.g. `<repo>/docs/foo.md` or bare `<repo>`.
_ANGLE_PLACEHOLDER = re.compile(r"<[^<>]*>")

# A scheme URL (http:, mailto:, ftp'ish…) or protocol-relative `//host`.
_SCHEME_URL = re.compile(r"\b[a-zA-Z][a-zA-Z0-9+.\-]*://\S+|//\S+|\bmailto:\S+")

# A Markdown link/image DESTINATION only — `](dest)` or `](dest "title")` —
# matches linkscan's own destination shape, so the same span is skipped here.
_LINK_DEST = re.compile(
    r"\]\(\s*(<[^>]*>|(?:[^()\s]|\([^()\s]*\))+)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")

_FENCE = re.compile(r"^(`{3,}|~{3,})")

# Same-line stub cues: a TODO marker anywhere, or the literal phrase
# "(none yet)" — see header's STUB exemption.
_STUB_CUE_RX = re.compile(r"\btodo\b|\(none yet\)", re.IGNORECASE)

# A date/time PLACEHOLDER segment inside a token — the literal uppercase
# `YYYY` or `HHMM` of a naming-convention template such as
# `docs/reviews/YYYY-MM-DD-HHMM-slug.md`. Case-SENSITIVE and deliberately
# narrow: `MM`/`DD` alone are not cues (two-letter uppercase runs occur in
# real filenames), and a template that uses them writes `YYYY` first anyway.
# This is the placeholder shape angle-bracket blanking misses when the
# `<...>` span wraps across a line break — see header, FALSE NEGATIVES.
_DATE_PLACEHOLDER_RX = re.compile(r"YYYY|HHMM")

# Suffixes tried when an extensionless token might be naming a directory
# index (GitHub's convention): `tools/README` is really `tools/README.md`.
_INDEX_SUFFIXES = (".md", ".markdown")


@dataclass
class Finding:
    path: str          # the flagged Markdown file (repo-relative)
    line: int
    kind: str          # "missing-path"
    target: str        # the candidate token, as matched (post-trim)
    detail: str        # human hint at what's missing


def _content_lines(text: str):
    """Yield (lineno, line) for lines outside fenced code blocks. Fence
    pairing matches linkscan/datescan exactly: a fence closes only on a run
    of the same character at least as long as the opener, no trailing info
    string on the closer."""
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


def _blank_span(line: str, m: "re.Match[str]") -> str:
    return line[:m.start()] + " " * (m.end() - m.start()) + line[m.end():]


def _strip_non_candidates(line: str) -> str:
    """Blank angle-bracket placeholders, scheme URLs, and Markdown link
    destinations before candidate-hunting — see header, THE CHECK step 2."""
    out = line
    for rx in (_ANGLE_PLACEHOLDER, _SCHEME_URL):
        while True:
            m = rx.search(out)
            if not m:
                break
            out = _blank_span(out, m)
    while True:
        m = _LINK_DEST.search(out)
        if not m:
            break
        out = _blank_span(out, m)
    return out


def _is_stub_marked(line: str) -> bool:
    return bool(_STUB_CUE_RX.search(line))


def _is_placeholder(token: str) -> bool:
    if "*" in token or "?" in token:
        return True
    if token.lower().startswith("path/to"):
        return True
    if _DATE_PLACEHOLDER_RX.search(token):
        return True
    return False


def _is_known_candidate(token: str) -> bool:
    lower = token.lower()
    if lower.startswith(KNOWN_TOP_DIRS):
        return True
    return lower.endswith(KNOWN_EXTENSIONS)


def _trim_trailing_period(token: str) -> str:
    """A single trailing sentence period (`` `foo.md`. `` at a sentence's
    end) is not part of the path. Only ONE trailing dot is trimmed — a
    literal `..` or more is left alone rather than guessed at."""
    if token.endswith(".") and not token.endswith(".."):
        return token[:-1]
    return token


def _is_elided(match_text: str, cleaned: str, match_end: int) -> bool:
    """True if the token is truncated by an ellipsis — a deliberate "shown
    for brevity, not a complete path" marker (`docs/reviews/2026-07-10-…`,
    found live on this repo's own baseline run), the same shape-not-claim
    signal as `path/to/thing`. Two forms, checked differently because a
    literal ASCII `...` is made of `.` characters the token regex's own
    character class already accepts — so a 3+ dot run gets SWALLOWED INTO
    the match itself, not left dangling after it (unlike a single Unicode
    `…`, which isn't in the class and so naturally stops the match right
    before it):
      - the match's own tail is a run of 3+ literal dots (ASCII `...`);
      - OR the match is immediately followed by a single Unicode `…`."""
    if match_text.endswith("..."):
        return True
    return cleaned[match_end:match_end + 1] == "…"


def iter_candidates(line: str):
    """Yield candidate path tokens (trimmed, filtered) from one already-
    de-fenced line — bare prose AND backtick-wrapped spans alike (backticks
    are not stripped; see header on why that's deliberate here)."""
    cleaned = _strip_non_candidates(line)
    for m in _PATH_TOKEN.finditer(cleaned):
        if _is_elided(m.group(0), cleaned, m.end()):
            continue
        token = _trim_trailing_period(m.group(0))
        if not token or "/" not in token:
            continue
        if _is_placeholder(token):
            continue
        if not _is_known_candidate(token):
            continue
        yield token


def _outermost_named_ancestor(p: Path, name: str) -> Path | None:
    """The ancestor directory literally named `name` CLOSEST TO THE ROOT
    (not the nearest to p) — None if p isn't under one. Deliberately
    outermost, not nearest: atelier's own `docs/build/templates/docs/` is a
    literal nested `docs/`-named directory (repo-craft scaffolding that
    mimics a CHILD repo's docs/ folder for templating purposes), so a file
    under it has TWO ancestors named `docs`. The templated file's bare-prose
    mentions (e.g. `docs/build/templates/docs/ROADMAP.md` naming
    `method/REVIEW.md`) mean the REAL atelier doctrine at
    `docs/method/REVIEW.md`, not a same-shaped file nested inside the
    template — found live on this repo's own baseline run, not a
    theoretical edge case."""
    found = None
    for parent in p.parents:
        if parent.name == name:
            found = parent
    return found


def _is_extensionless(token: str) -> bool:
    """True if the token's LAST segment carries no `.` at all — the shape
    the directory-index retry applies to. `tools/README` qualifies;
    `tools/README.md` does not (it already names its extension), and neither
    does `docs/x.md/y` — only the last segment is inspected, which is where
    an extension would sit."""
    return "." not in token.rsplit("/", 1)[-1]


def _exists_under(anchor: Path, token: str) -> bool:
    """Existence of `token` under one anchor, with the directory-index
    retry: an EXTENSIONLESS token is also tried with `.md`/`.markdown`
    appended, so a bare `tools/README` finds `tools/README.md` (GitHub's
    directory-index convention — see module docstring, STATED RESIDUAL, for
    the masking cost this buys). Monotone: the retry can only ever drop a
    finding, never invent one."""
    if (anchor / token).exists():
        return True
    if _is_extensionless(token):
        return any((anchor / (token + s)).exists() for s in _INDEX_SUFFIXES)
    return False


def _docs_anchor(root: Path, md_file: Path) -> Path:
    """Anchor 3 or anchor 4, whichever applies — they are mutually exclusive
    by construction. A file UNDER a `docs/` ancestor gets that ancestor
    (outermost); a file with no such ancestor — a ROOT file — gets
    `<root>/docs`. See `_resolves`."""
    docs_dir = _outermost_named_ancestor(md_file, "docs")
    return docs_dir if docs_dir is not None else root / "docs"


def _under_docs(md_file: Path) -> bool:
    return _outermost_named_ancestor(md_file, "docs") is not None


def _resolves(root: Path, md_file: Path, token: str) -> bool:
    """A candidate resolves if it exists under ANY of four anchors — widening
    what counts as "resolves" can only DROP a finding, never invent one, so
    stacking anchors is safe (see module docstring, THE CHECK step 5):

      1. The SCAN ROOT — `docs/decisions/` written from README.md at the
         repo root.
      2. The candidate FILE's OWN DIRECTORY — matches linkscan's own
         link-relative convention.
      3. (file UNDER `docs/`) The OUTERMOST ENCLOSING `docs/` DIRECTORY,
         whichever depth the referencing file sits at — running this scanner
         over atelier's own corpus found this is the DOMINANT bare-prose
         convention: a file two or three levels under docs/
         (`docs/build/REPO-STANDARD.md`, `docs/decisions/README.md`) still
         writes `method/RECORD.md` meaning `docs/method/RECORD.md`, not a
         path relative to its OWN directory. Anchor #2 alone does not catch
         this — only the outermost `docs/` ancestor, regardless of nesting
         depth, does (see `_outermost_named_ancestor` on why OUTERMOST, not
         nearest).
      4. (file NOT under `docs/`) `<root>/docs` — DOCS-RELATIVE SHORTHAND.
         The same convention as anchor 3, written from a file that has no
         `docs/` ancestor for anchor 3 to find: a root `README.md` or
         `CHANGELOG.md` writes `method/REVIEW.md` meaning
         `docs/method/REVIEW.md`. Anchor 3's absence, not a different rule —
         which is why the two are mutually exclusive, and why a scanner
         pointed only at `docs/` never needed anchor 4 to exist.

    The masking cost of all this widening is named in the module docstring's
    STATED RESIDUAL: existence-somewhere is not correctness.
    """
    if _exists_under(root, token):
        return True
    if _exists_under(md_file.parent, token):
        return True
    return _exists_under(_docs_anchor(root, md_file), token)


def scan_text(md_file: Path, root: Path, text: str,
              tally: "Tally | None" = None) -> list[Finding]:
    rel = _rel(md_file, root)
    # Anchors 3 and 4 are mutually exclusive (see _resolves) — name the one
    # actually tried, so a reader of the finding can check it by hand.
    docs_anchor_note = ("its outermost enclosing docs/ directory"
                       if _under_docs(md_file)
                       else "the repo's docs/ (docs-relative shorthand)")
    findings: list[Finding] = []
    seen_on_line: set[tuple[int, str]] = set()
    # Line -> allowance scope, recorded rather than acted on (rule b).
    allow_by_line: dict[int, str] = {}
    for lineno, raw_line in _content_lines(text):
        scope = parse_allow(raw_line)
        if scope is not None:
            allow_by_line[lineno] = scope
        if _is_stub_marked(raw_line):
            continue
        for token in iter_candidates(raw_line):
            key = (lineno, token)
            if key in seen_on_line:
                continue
            seen_on_line.add(key)
            if _resolves(root, md_file, token):
                continue
            findings.append(Finding(
                rel, lineno, "missing-path", token,
                f"{token} does not exist (checked repo-root-relative, "
                f"relative to {rel}'s own directory, and relative to "
                f"{docs_anchor_note})"))
    # SUBTRACT SECOND. One finding kind, so the line is the whole scope.
    kept: list[Finding] = []
    for f in findings:
        if allow_by_line.get(f.line) is not None:
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
    """Globs from `.pathscanignore`, each of which MUST carry a stated reason.

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
    f = root / ".pathscanignore"
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
        raise IgnoreFileError(".pathscanignore", unreasoned)
    return globs


def _ignored(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(rel, g.rstrip("/") + "/*")
               for g in globs)


# Records name the tree as it stood when they were written and can never come
# clean without markers that would falsify the record — the registry's own
# rationale for scoping atelier's records OUT, which children's default scope
# then contradicted by pulling theirs IN (FR2, the principal's ruling
# 2026-08-23: records-excluding by default, estate-wide). Excluded only when a
# DIRECTORY is expanded; a records file named explicitly as a path argument is
# always scanned — the same contract as plainscan's RECORDS_GLOBS.
RECORDS_GLOBS = ["docs/SESSIONS.md", "docs/sessions", "docs/ROADMAP-DONE.md",
                 "docs/reviews", "CHANGELOG.md"]


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def iter_markdown(paths: list[Path], root: Path, globs: list[str],
                  tally: "Tally | None" = None,
                  include_records: bool = False):
    for base in paths:
        expanded = base.is_dir()
        if base.is_file():
            candidates = [base]
        else:
            candidates = [p for p in base.rglob("*")
                          if p.is_file() and not (SKIP_DIR_NAMES & set(p.parts))]
        for p in candidates:
            if p.suffix.lower() not in MARKDOWN_SUFFIXES:
                continue
            rel = _rel(p, root)
            if _ignored(rel, globs):
                if tally is not None:
                    tally.files_by_glob += 1
                continue
            if expanded and not include_records and _ignored(rel, RECORDS_GLOBS):
                if tally is not None:
                    tally.files_by_records += 1
                continue
            yield p


def scan_paths(paths: list[Path], root: Path,
               tally: "Tally | None" = None,
               include_records: bool = False) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs, tally,
                            include_records=include_records):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text(md, root, text, tally))
    return findings


def render_human(findings: list[Finding], tally: "Tally | None" = None) -> str:
    if not findings:
        out = "✓ pathscan clean — every candidate repo-path reference resolves."
        return out + ("\n" + tally.summary() if tally is not None else "")
    lines = [f"✗ pathscan: {len(findings)} finding(s)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.target} → {f.detail}")
    if tally is not None:
        lines.append("")
        lines.append(tally.summary())
    lines.append("\n  A real stale path: fix the reference (or restore/rename the target).")
    lines.append("  A false positive or deliberate stub: append "
                 f"'<!-- {ALLOW_MARKER}: <reason> -->' to the line, or add a "
                 "path glob to .pathscanignore.")
    lines.append("  Heuristic detection, reviewed once — see this tool's module "
                 "docstring for its named false-positive/false-negative modes, "
                 "and for which surface is worth gating (records never come "
                 "clean).")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="pathscan",
        description="Check that named repo-path references (bare prose or "
                    "backtick-wrapped, not already a Markdown link) resolve.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: <root>/docs if present, "
                         "else the whole root). The default is NOT the gateable "
                         "scope: root-level *.md are scannable and clean, and "
                         "the surface worth gating is the doctrine surface plus "
                         "root Markdown — 'docs/method docs/build docs/decisions "
                         "README.md CLAUDE.md SECURITY.md'. Records "
                         "(docs/reviews, docs/sessions, CHANGELOG.md) are "
                         "point-in-time and never come clean; scan them "
                         "advisory. See the module docstring, STATED RESIDUAL.")
    ap.add_argument("--root", default=".",
                    help="repo root for path resolution and .pathscanignore")
    ap.add_argument("--warn", action="store_true",
                    help="report findings but always exit 0 (advisory / "
                         "warn-first rollout — its cold review recommended "
                         "staying advisory, and the flip to blocking is a "
                         "decision, not a default)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--include-records", action="store_true",
                    help="also scan the records (docs/reviews, docs/sessions, "
                         "docs/SESSIONS.md, docs/ROADMAP-DONE.md, "
                         "CHANGELOG.md), excluded by default since 2026-08-23 "
                         "(FR2): they name the tree as it stood when written "
                         "and never come clean. A records file named "
                         "explicitly as a path argument is always scanned.")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"pathscan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    if args.paths:
        targets = [Path(p) for p in args.paths]
    else:
        docs = root / "docs"
        targets = [docs] if docs.is_dir() else [root]

    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"pathscan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    tally = Tally()
    try:
        findings = scan_paths(targets, root, tally,
                              include_records=args.include_records)
    except OSError as e:
        print(f"pathscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
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
    """Minimal smoke test so `pathscan --selftest` proves the engine on any
    box, even where the unittest file isn't shipped."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="pathscan-self-"))
    (tmp / "docs").mkdir()
    (tmp / "tools").mkdir()
    (tmp / "tools" / "real.py").write_text("# real\n")
    (tmp / "docs" / "sub" / "other").mkdir(parents=True)
    (tmp / "docs" / "sub" / "other" / "thing.md").write_text("# thing\n")
    (tmp / "docs" / "sub" / "note2.md").write_text(
        "See `other/thing.md` here — resolves relative to THIS file's own "
        "directory (docs/sub/), not the repo root; proves anchor #2 (THE "
        "CHECK step 5).\n"
    )
    (tmp / "docs" / "deep" / "sub2").mkdir(parents=True)
    (tmp / "docs" / "method").mkdir()
    (tmp / "docs" / "method" / "far.md").write_text("# far\n")
    (tmp / "docs" / "deep" / "sub2" / "note3.md").write_text(
        "See `method/far.md` here — NOT relative to THIS file's own "
        "directory (docs/deep/sub2/, which has no method/ child), but to "
        "the nearest ENCLOSING docs/ two levels up; proves anchor #3 (THE "
        "CHECK step 5), the dominant real-corpus shape.\n"
    )
    (tmp / "docs" / "note.md").write_text(
        "# Note\n\n"
        "See `tools/real.py` for the implementation.\n"                    # resolves (backtick)
        "See tools/real.py in bare prose too.\n"                           # resolves (bare)
        "But `tools/ghost.py` does not exist.\n"                          # BREAK 1
        "Nor does docs/ghost/plan.md in bare prose.\n"                    # BREAK 2
        "A markdown link [here](tools/also-ghost.py) is linkscan's job.\n"  # skipped (link dest)
        "See <repo>/tools/real.py for the pattern (placeholder).\n"       # skipped (angle-bracket)
        "Try `src/**/*.go` as a glob example.\n"                          # skipped (glob)
        "Copy from `path/to/thing.md` as a placeholder.\n"                # skipped (path/to)
        "A fraction like 3/4 of the work is not a path.\n"                # skipped (no top-dir/ext)
        "See https://example.com/tools/real.py — a URL, skipped.\n"       # skipped (scheme)
        "`docs/future/plan.md` is a stub (none yet).\n"                    # skipped (stub cue)
        "`docs/other-future.md` TODO: not built yet.\n"                    # skipped (stub cue)
        "```\n`tools/fenced-ghost.py` inside a fenced example\n```\n"      # skipped (fenced)
        "`tools/allowed-ghost.py` is fine  <!-- pathscan:allow: fixture -->\n"  # skipped (allow marker)
        "A trailing mention of `tools/real.py`.\n"                         # resolves, trailing period trimmed
    )
    findings = scan_paths([tmp / "docs"], tmp)
    targets = sorted(f.target for f in findings)
    expected = sorted(["tools/ghost.py", "docs/ghost/plan.md"])
    ok = targets == expected
    if not ok:
        print(f"FAIL: got {targets}, expected {expected}")

    # Anchor #4 (docs-relative shorthand from a file with no docs/ ancestor)
    # and the extensionless directory-index retry — both proved from a ROOT
    # file, the shape the docs-only default scope cannot reach.
    (tmp / "tools" / "README.md").write_text("# tools\n")
    (tmp / "README.md").write_text(
        "See `method/far.md` — docs-relative shorthand from a root file, "
        "resolved via <root>/docs/; proves anchor #4.\n"
        "See `tools/README` — extensionless, retried as tools/README.md.\n"
        "But `method/ghost.md` resolves under no anchor at all.\n"      # BREAK
    )
    root_findings = scan_paths([tmp / "README.md"], tmp)
    root_targets = sorted(f.target for f in root_findings)
    if root_targets != ["method/ghost.md"]:
        print(f"FAIL: root-file scan got {root_targets}, "
              "expected ['method/ghost.md']")
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
    (clean / "ok.md").write_text("See `tools/real.py`, which exists.\n")
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
        print(f"pathscan: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())

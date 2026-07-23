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

FIRST-OF-KIND, NOT YET WIRED, NOT YET REVIEWED. This tool stands alone: it is
not invoked from `ci.yml`, `docs/build/templates/floor.yml`, or the
pre-commit hook. It ships with `--warn` support so a future advisory wiring
needs no code change, matching `datescan`'s rollout shape — but wiring it in
is a decision for whoever reviews it, not this build.

THE CHECK, deliberately narrow (a broad flaky path-guesser is worse than a
sharp honest one):

  1. Read each Markdown file outside fenced (``` ```) code blocks — a fenced
     block is an illustrative example, not a live claim (matches every
     sibling scanner).

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

  5. A candidate is resolved against THREE anchors, and passes if it exists
     under ANY of them (see `_resolves` for the full rationale):
       - the SCAN ROOT — `README.md` at the repo root writes `docs/decisions/`
         root-relative;
       - the CANDIDATE FILE's OWN DIRECTORY — matches `linkscan`'s
         link-relative convention;
       - the OUTERMOST ENCLOSING `docs/` DIRECTORY, at whatever depth the
         referencing file sits — a doc `docs/build/REPO-STANDARD.md` still
         writes `method/RECORD.md` meaning `docs/method/RECORD.md`, dropping
         the `docs/` prefix regardless of its OWN nesting under `docs/build/`
         (OUTERMOST, not nearest — see `_outermost_named_ancestor` on why:
         `docs/build/templates/docs/` is itself a nested `docs`-named dir).
     Running this scanner over the live repo found this last anchor was not
     optional — before it, roughly 6 in 10 findings were this exact shape
     (see STATED RESIDUAL). Widening what counts as "resolves" can only ever
     DROP a finding, never invent one: a genuinely broken path fails under
     all three and is still flagged.

DETECTION HEURISTIC — the genuinely hard, judgement-heavy part, stated
honestly, not rounded up:

  Distinguishing "a real repo-path reference that should resolve" from
  "arbitrary prose that happens to contain a slash" has no clean rule. The
  heuristic chosen — known-top-dir-prefix OR known-extension-suffix — was
  picked because it is the cheapest test that rejects the dominant false-
  positive shape (an ordinary fraction, ratio, or date-as-numerals: `3/4`,
  `50/50`, `23/07/2026` start with neither a repo dir nor end in a doc
  extension, so none of them become candidates) while still catching every
  cited occurrence (`docs/decisions/`, `templates/`, an ACCESS-style pointer)
  without a repo-specific allowlist of "real" paths to maintain.

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
      line-wrap is invisible to a line-local regex.
    - A genuinely broken reference that avoids both legs of the heuristic —
      no known top-dir prefix, no known extension (a bare directory name with
      no extension, one level deep, e.g. a made-up `foo/bar` with neither
      cue) — scans clean. This is the accepted cost of a heuristic that does
      not hard-code every real directory name as a second allowlist.
    - Leading `/` root-relative bare-prose mentions ("/docs/x.md") are not
      picked up as candidates (the token regex requires the match to start at
      a word character, not `/`) — same shape as the angle-bracket blind
      spot above: distinguishing a genuine root-relative bare mention from
      the tail of a just-blanked placeholder is not attempted; both are
      silently skipped rather than guessed at.

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
    signal as `path/to/thing`.
  * THE ALLOW MARKER / IGNORE FILE. `pathscan:allow: <reason>` anywhere on a
    line exempts every candidate on that line — same tightened contract as
    `datescan` (word-boundary, colon, non-empty reason so a bare mention of
    the marker text doesn't accidentally exempt itself). A glob in
    `.pathscanignore` at the scan root exempts a path wholesale.

STATED RESIDUAL, HONESTLY (do not round this to "solved" or "clean"):

  * This is a FIRST-OF-KIND, UNREVIEWED heuristic. Its accuracy is unproven —
    see DETECTION HEURISTIC above for the named false-positive and false-
    negative shapes. A noisy baseline on first run against this repo's own
    docs is EXPECTED, not a bug to silently round away.
  * Triple-anchor resolution (root / own-directory / nearest-docs-ancestor,
    see THE CHECK step 5) closes the dominant noise source found on this
    repo's own corpus, but is still a fixed set of heuristic anchors, not a
    grammar: a path meant relative to some OTHER file's directory, or a
    repo whose doc tree isn't named `docs/`, still won't resolve and is
    flagged even if a human reader would understand it from context.
  * A bare `README` mention with no extension (`tools/README`,
    `instruments/README`, GitHub's own directory-index convention) is NOT
    tried with `.md`/`.markdown` appended — a named gap, not a guess added
    to close it; `tools/README.md` is the real file, `tools/README` alone
    stays flagged.
  * Directories and files are both accepted as "resolves" — a candidate
    ending in a known extension that turns out to be a directory on disk (or
    vice versa) is NOT distinguished; only existence is checked, matching
    `linkscan`'s own file-vs-directory looseness.
  * Only `docs/**` Markdown is scanned by default (mirrors `datescan`); code
    comments, commit messages, and non-Markdown prose are out of scope.

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
# that line. Same tightened contract as datescan (DSR8): word boundary, then
# a colon and a non-empty reason, so a bare mention of the marker text alone
# does not silently exempt the line.
ALLOW_MARKER = "pathscan:allow"
ALLOW_MARKER_RX = re.compile(r"\b" + re.escape(ALLOW_MARKER) + r":\s*\w")

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
_PATH_TOKEN = re.compile(r"(?<![\w./*?])[\w.\-*?]+(?:/[\w.\-*?]+)+")

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


def _resolves(root: Path, md_file: Path, token: str) -> bool:
    """A candidate resolves if it exists under ANY of three anchors — widening
    what counts as "resolves" can only DROP a finding, never invent one, so
    stacking anchors is safe (see module docstring, THE CHECK step 5):

      1. The SCAN ROOT — `docs/decisions/` written from README.md at the
         repo root.
      2. The candidate FILE's OWN DIRECTORY — matches linkscan's own
         link-relative convention.
      3. The OUTERMOST ENCLOSING `docs/` DIRECTORY, whichever depth the
         referencing file sits at — running this scanner over atelier's own
         corpus found this is the DOMINANT bare-prose convention: a file two
         or three levels under docs/ (`docs/build/REPO-STANDARD.md`,
         `docs/decisions/README.md`) still writes `method/RECORD.md` meaning
         `docs/method/RECORD.md`, not a path relative to its OWN directory.
         Anchor #2 alone does not catch this — only the outermost `docs/`
         ancestor, regardless of nesting depth, does (see
         `_outermost_named_ancestor` on why OUTERMOST, not nearest).
    """
    if (root / token).exists():
        return True
    if (md_file.parent / token).exists():
        return True
    docs_dir = _outermost_named_ancestor(md_file, "docs")
    if docs_dir is not None and (docs_dir / token).exists():
        return True
    return False


def scan_text(md_file: Path, root: Path, text: str) -> list[Finding]:
    rel = _rel(md_file, root)
    findings: list[Finding] = []
    seen_on_line: set[tuple[int, str]] = set()
    for lineno, raw_line in _content_lines(text):
        if ALLOW_MARKER_RX.search(raw_line):
            continue
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
                f"relative to {rel}'s own directory, and relative to its "
                "outermost enclosing docs/ directory)"))
    return findings


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".pathscanignore"
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


def scan_paths(paths: list[Path], root: Path) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for md in iter_markdown(paths, root, globs):
        text = md.read_text(encoding="utf-8", errors="replace")
        findings.extend(scan_text(md, root, text))
    return findings


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return "✓ pathscan clean — every candidate repo-path reference resolves."
    lines = [f"✗ pathscan: {len(findings)} finding(s)."]
    for f in sorted(findings, key=lambda x: (x.path, x.line)):
        lines.append(f"  {f.path}:{f.line}  [{f.kind}] {f.target} → {f.detail}")
    lines.append("\n  A real stale path: fix the reference (or restore/rename the target).")
    lines.append("  A false positive or deliberate stub: append "
                 f"'<!-- {ALLOW_MARKER}: <reason> -->' to the line, or add a "
                 "path glob to .pathscanignore.")
    lines.append("  FIRST-OF-KIND, UNREVIEWED heuristic — see this tool's module "
                 "docstring for its named false-positive/false-negative modes.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="pathscan",
        description="Check that named repo-path references (bare prose or "
                    "backtick-wrapped, not already a Markdown link) resolve.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: <root>/docs if present, "
                         "else the whole root)")
    ap.add_argument("--root", default=".",
                    help="repo root for path resolution and .pathscanignore")
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
    try:
        findings = scan_paths(targets, root)
    except OSError as e:
        print(f"pathscan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "warn": args.warn,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings))
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


if __name__ == "__main__":
    sys.exit(main())

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

FIRST-OF-KIND, ADVISORY, NOT WIRED. This scanner has not yet earned an
independent review. It is NOT wired into CI, `floor.yml`, or the pre-commit
hook by this change — that wiring is a separate, deliberate act for whoever
promotes it, matching wrapscan's and datescan's own rollout discipline
(reviewed first, wired `--warn`-only after, never blocking before review).

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
     no stamp at all.
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
       - anything else (an added line, a reordered line, a reworded line —
         any deviation that ISN'T obtainable by pure deletion) -> DRIFT, RED,
         REGARDLESS of a `narrow=` declaration — declaring narrow intent
         does not excuse an actual addition or contradiction; only a genuine
         subset counts as "legitimate".

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
  * The ordered-subsequence check is a standard greedy two-pointer match; it
    does not handle a canonical region containing duplicate lines specially
    — a duplicate line could be consumed by the wrong occurrence in a
    pathological case. Not expected to bite on prose floor blocks in
    practice, and not exercised by the one live pair this change wires.
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
     bad CLI arguments (NEVER downgraded by --warn)

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

# A line carrying this marker (anywhere inside a stamped block) exempts that
# whole block from comparison. Same word-boundary + non-empty-reason
# contract as datescan's DSR8-tightened ALLOW_MARKER_RX — a bare mention or
# an empty reason must not silently exempt.
ALLOW_MARKER = "stampscan:allow"
ALLOW_MARKER_RX = re.compile(r"\b" + re.escape(ALLOW_MARKER) + r":\s*\w")

# Only these extensions are scanned for stamped blocks — matches every
# sibling scanner's MARKDOWN_SUFFIXES.
MARKDOWN_SUFFIXES = {".md", ".markdown"}

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
# stamp:end is deliberately matched by SEARCH, not anchored to line-start —
# the one live pair this change wires needs it to trail arbitrary prefix
# content on its own line (docs/build/templates/CLAUDE.md closes its stamp
# on the same line as the file's pre-existing `---` section divider,
# `---<!-- stamp:end -->`, so as not to add a new line inside the exact span
# a pre-existing, unrelated frozen test — tools/test_templates.py's
# `template_block()` — slices verbatim; see module header, STATED RESIDUAL).
_STAMP_END_RX = re.compile(r"<!--\s*stamp:end\s*-->")

# Fenced-presentation stripping (see module header). Matches the sibling
# scanners' own fence regex (`^(`{3,}|~{3,})`), plus an optional info string
# on the opener only (` ```markdown `), and requires a bare closer.
_FENCE_OPEN_RX = re.compile(r"^(`{3,}|~{3,})\S*$")


def _region_markers(name: str) -> tuple["re.Pattern[str]", "re.Pattern[str]"]:
    """Build the begin/end regexes for a named canonical region, e.g.
    `<!-- floor:begin -->` / `<!-- floor:end -->`."""
    esc = re.escape(name)
    return (re.compile(rf"^<!--\s*{esc}:begin\s*-->$"),
            re.compile(rf"^<!--\s*{esc}:end\s*-->$"))


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
                 # | "missing-source" | "missing-region" | "malformed"
    source: str | None
    region: str | None
    detail: str


# ---------------------------------------------------------------- parsing --

def _content_lines(text: str):
    for lineno, line in enumerate(text.splitlines(), start=1):
        yield lineno, line


def find_stamp_blocks(path: str, text: str) -> tuple[list[StampBlock], list[Finding]]:
    """Parse every `stamp:begin ... stamp:end` pair in `text`. Returns
    (blocks, malformed_findings) — malformed markers (unterminated, nested,
    or a stray end) are reported as `malformed` findings, never silently
    dropped."""
    blocks: list[StampBlock] = []
    malformed: list[Finding] = []
    open_stamp: dict | None = None

    for lineno, raw_line in _content_lines(text):
        stripped = raw_line.strip()
        m_begin = _STAMP_BEGIN_RX.match(stripped)
        m_end = _STAMP_END_RX.search(stripped)

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
                "narrow": m_begin.group("narrow"),
                "payload": [],
                "allow": bool(ALLOW_MARKER_RX.search(raw_line)),
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
            if ALLOW_MARKER_RX.search(raw_line):
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
    is a fail-safe config error, not an empty result."""
    begin_rx, end_rx = _region_markers(region)
    lines = text.splitlines()
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if start_idx is None:
            if begin_rx.match(line.strip()):
                start_idx = i
            continue
        if end_idx is None and end_rx.match(line.strip()):
            end_idx = i
            break
    if start_idx is None or end_idx is None:
        return None
    payload = lines[start_idx + 1:end_idx]
    if payload and _FENCE_OPEN_RX.match(payload[0].strip()) \
            and payload[-1].strip().rstrip("`~") == "" \
            and payload[-1].strip()[:1] == payload[0].strip()[:1]:
        payload = payload[1:-1]
    return payload


# ------------------------------------------------------------- comparison --

def _is_ordered_subsequence(sub: list[str], full: list[str]) -> bool:
    """True if `sub` can be obtained from `full` by deleting zero or more
    lines only — never reordering, adding, or altering one. Standard
    greedy two-pointer subsequence check (see STATED RESIDUAL for the
    duplicate-line caveat)."""
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

    if _is_ordered_subsequence(child, parent):
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

def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".stampscanignore"
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
    source_cache: dict[str, str] = {}

    for md in iter_markdown(paths, root, globs):
        rel = _rel(md, root)
        text = md.read_text(encoding="utf-8", errors="replace")
        blocks, malformed = find_stamp_blocks(rel, text)
        findings.extend(malformed)

        for block in blocks:
            source_path = root / block.source
            if block.source not in source_cache:
                if not source_path.is_file():
                    source_cache[block.source] = None  # type: ignore[assignment]
                else:
                    source_cache[block.source] = source_path.read_text(
                        encoding="utf-8", errors="replace")
            source_text = source_cache[block.source]

            if source_text is None:
                findings.append(Finding(
                    block.path, block.line, "missing-source", block.source,
                    block.region,
                    f"canonical source does not resolve: {block.source} "
                    f"(resolved against --root {root})"))
                continue

            canonical = extract_region(source_text, block.region)
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

_CONFIG_ERROR_KINDS = {"missing-source", "missing-region", "malformed"}
_DRIFT_KINDS = {"drift"}
_CLEAN_KINDS = {"identical", "narrow", "skipped"}


def render_human(findings: list[Finding]) -> str:
    errors = [f for f in findings if f.kind in _CONFIG_ERROR_KINDS]
    drifts = [f for f in findings if f.kind in _DRIFT_KINDS]
    notes = [f for f in findings if f.kind in _CLEAN_KINDS]

    if not findings:
        return "✓ stampscan clean — no stamped blocks found."

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
        lines.append(f"  ({len(notes)} note(s): "
                      + ", ".join(sorted(f"{f.kind}" for f in notes)) + ")")
        for f in sorted(notes, key=lambda x: (x.path, x.line)):
            lines.append(f"    {f.path}:{f.line}  [{f.kind}] {f.detail}")
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


def main(argv: list[str] | None = None) -> int:
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
        targets = [Path(p) for p in args.paths]
    else:
        docs = root / "docs"
        targets = [docs] if docs.is_dir() else [root]

    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"stampscan: path does not exist: {', '.join(missing)}",
              file=sys.stderr)
        return 2
    try:
        findings = scan_paths(targets, root)
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
        }, indent=2))
    else:
        print(render_human(findings))
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


if __name__ == "__main__":
    sys.exit(main())

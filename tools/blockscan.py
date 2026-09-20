#!/usr/bin/env python3
"""blockscan — the mechanical check that a ruling which moves house doctrine
also moves the child block's copy of it (and the scaffold template's).

THE INCIDENT THIS CLOSES (board `320/300`, split out of `320/250`
2026-09-18). A 2026 ruling reworded the ask rule in `docs/method/
COMMUNICATION.md`. The standard child doctrine block — the `<!-- floor:begin
-->` region in `docs/method/PROPAGATION.md` — and the scaffold template that
stamps it (`docs/build/templates/CLAUDE.md`) both kept the OVERTURNED wording
for weeks and copied it into every child at pin bump. `stampscan` already
checks a CHILD's inlined copy against atelier's own region (drift once the
block moves); nothing checked atelier's region against the method docs it
claims to summarise in the first place. This is that check, one layer up.
RULED (Mike, 2026-09-19, via the question device): "Build the check."

THE RULE — a staged-plane CO-CHANGE check, no hashes, no section-text
diffing against a stored baseline:

  If a commit changes lines INSIDE a mapped section of a source method doc,
  it must ALSO change the corresponding block bullet in BOTH
  `docs/method/PROPAGATION.md`'s floor region and
  `docs/build/templates/CLAUDE.md`'s stamped copy — or carry a scoped
  `blockscan:allow: <reason>` marker. Otherwise: a finding naming the
  section, the bullet, and which of the two files did not move.

THE MAP (`tools/blockscan_map.json`, hand-maintained, read at every run —
never baked into this module): each bullet the block's own prose already
attributes to a source doc is keyed by a short stable id, an `anchor` (the
bullet's own bold lead-in text, copied verbatim — this is how the SAME bullet
is found in both PROPAGATION.md's region and the template's stamped copy
without inventing a hidden id neither file otherwise carries), and one or
more `sources`, each a `{path, heading}` pair naming the exact Markdown
heading the bullet is filed under. NOT EVERY BULLET IS MAPPED: the floor
region has nine bullets and this map carries six. The three left out —
**Source & drift**, **Estate resources — point up, don't re-derive**, and
**This repo's visibility** — cite no source-doc section at all in their own
text (the first is PROPAGATION's own pin-bump mechanism describing itself,
the second points at a private estate-root repo outside atelier's `docs/
method/` entirely, the third is a per-repo fact substituted at scaffold
time). Mapping them would be inventing a citation the bullet never made, the
opposite of grounding this tool's job is to check.

A SECTION, for this tool's purposes, is NON-RECURSIVE: the lines strictly
between a heading and the NEXT heading OF ANY LEVEL (not just the same or a
shallower one). `00-APEX.md`'s `## Honesty is absolute` has three `###`
subsections nested under it; mapping the **apex** bullet to the whole `##`
span would make every edit to `### The principal's authority...` (which the
**stop-and-confirm** and **asking** bullets already cite on their own) also
demand an apex-bullet edit that bullet's own prose never claimed to need.
Non-recursive extraction is what lets six bullets share one file's headings
without echoing every edit onto bullets that never cited that text.

THE CHECK, three modes because the co-change rule needs two states to
compare and the integrity checks do not:

  --staged (the hook plane — see WIRING RESIDUAL below for why this is not
    yet reachable from atelier's actual pre-commit hook). For every mapped
    source path and for the region
    and template files themselves, reads the OLD content (`git show HEAD:
    <path>`) and the NEW content about to be committed (`git show :<path>`,
    the index blob — this is "the state after the commit", not the working
    tree, so an edit made but never `git add`ed is correctly invisible here).
    For each bullet's source heading: extracts the OLD and NEW section text
    and compares them (trailing whitespace ignored only, matching stampscan's
    comparison strictness). Unchanged -> nothing to check. Changed -> the
    corresponding bullet's OLD/NEW text is extracted from both the region and
    the template and compared the same way; either one failing to move is a
    `violation` finding, UNLESS a `blockscan:allow: <reason>` marker (a
    reason required, a bare mention exempts nothing — the same tightened
    contract every sibling scanner's allow marker uses) is present in the
    NEW text of the changed source section, the NEW region bullet, or the
    NEW template bullet — any one of the three, so the marker can sit
    wherever the author is already editing.

  --against REV (a co-change check between REV, old, and HEAD, new — the
    actual CI plane, since a CI checkout's index equals HEAD exactly and
    reading it as "staged" would be vacuous). Runs the identical co-change
    logic as --staged with `git show <REV>:<path>` standing in for `HEAD`
    and `git show HEAD:<path>` standing in for the index — matching
    harvestscan's own `--against HEAD^` convention: the CI plane asks "did
    the commit that just landed move both copies" in place of the hook
    plane's "is this staged commit about to move both copies".

  --check (whole tree, no git needed — the default with none of the three
    flags given). Verifies ONLY the map's own integrity, against
    whatever is on disk: every mapped heading still resolves to EXACTLY ONE
    line in its source doc (a renamed or duplicated heading reds, never
    silently no-ops), and every bullet anchor still resolves to EXACTLY ONE
    bullet in both the region and the template. This is the check that
    catches the map itself going stale — a source doc's heading renamed
    without the map being told is a defect in the MAP, not a co-change
    violation, and is reported as a distinct, non-suppressible finding kind
    (no allow marker exempts it — a map that cannot find what it claims to
    map must fail loudly, never quietly pass on a wrong assumption). The
    same integrity check also runs, silently, as the first step of --staged
    (against the NEW/staged content) before any co-change comparison is
    attempted, for the same reason: comparing OLD to NEW is meaningless once
    either side cannot be located.

ONE STATED ASSUMPTION, honestly, not rounded away: every mapped path (the
region, the template, every source) is assumed to ALREADY EXIST at `HEAD` —
`--staged` mode calls `git show HEAD:<path>` unconditionally and reports a
`missing-file` config error if it fails, rather than treating a brand-new
file as "nothing to compare yet". This is a deliberate simplification, not
an oversight: every path this map names is a foundational, long-standing
method doc or the scaffold template itself, never a file this tool would
plausibly see introduced in the same commit as its first mapping. A repo
that genuinely needs that case does not have one today.

WIRING RESIDUAL, stated honestly rather than left implicit in a registry
diff (the board item's own design asked for registration "the way pathscan
is registered" — this is the one point where building that literally turned
out unworkable, not a redesign taken lightly):

  This scanner is DELIBERATELY NOT IN `tools/floor.py`'s SCANNERS registry,
  for the identical reason `stampscan` is not (see that module's own
  docstring, ST3): the registry is shared verbatim by every child's hook AND
  CI (children run atelier's own `floor.py` via `hooks.atelierTools`/
  `ATELIER_TOOLS`, not a vendored copy), and every path this map names —
  `docs/method/00-APEX.md`, `docs/method/COMMUNICATION.md`,
  `docs/method/CONCURRENCY.md`, `docs/method/ECONOMICS.md`,
  `docs/method/RECORD.md`, `docs/method/PROPAGATION.md`,
  `docs/build/templates/CLAUDE.md` — exists ONLY in atelier. A child running
  this check under `--check` (the mode a bare registry line would select
  with `--warn`, since neither `--staged` nor a staged diff exists on the CI
  plane either) would hit `missing-file` on its very first mapped path,
  which is a CONFIG ERROR — exit 2, fail-safe, NEVER downgraded by `--warn`
  — on every hook and every CI run, fleet-wide, from the commit this lands.
  Registering it plainly would not be "warn-only for now"; it would be a
  blocking outage for every child that is not atelier, from the moment this
  merges to `main`.

  What IS wired: a bespoke advisory step in atelier's OWN
  `.github/workflows/ci.yml`, this repo only, matching `stampscan`'s exact
  precedent — see that step for the reasoning. It runs
  `--check` (integrity only) there, plus `--against HEAD^` for the co-change
  rule itself (the CI plane's stand-in for a staged diff — see THE CHECK
  above). What is NOT wired anywhere: the `--staged` mode never runs as part
  of an actual pre-commit hook. `.githooks/pre-commit` is the one file
  ADR 0008 deliberately keeps scanner-agnostic ("THIS FILE NAMES NO
  SCANNER, AND THAT IS THE POINT") — it calls only `floor.py --plane hook`,
  so there is no bespoke-step seam at the hook level the way `ci.yml` offers
  at the CI level. The practical cost: a commit made from a fresh atelier
  clone is not checked for this class of drift until the NEXT push's CI run
  (`--against HEAD^`) catches it one commit later, reported but not
  blocking. Closing that gap needs either a new "atelier-only, hook-plane,
  not-in-the-shared-registry" seam in `floor.py` (machinery this item did
  not ask for and this build does not add), or accepting the one-push
  lag — a decision for whoever owns `floor.py`'s seam design next, not this
  build's to take unilaterally.

EXEMPTIONS:

  * THE ALLOW MARKER. `blockscan:allow: <reason>` — see THE CHECK above for
    where it may sit. It exempts exactly one `violation` finding (one
    bullet/source-heading pair); it never exempts a `stale-heading` or
    `missing-bullet` integrity finding — see above for why.
  * No ignore file. This scanner's unit is a fixed, hand-maintained map, not
    a path list walked over the tree — there is nothing an ignore glob would
    narrow that editing the map itself does not already narrow more
    precisely.

Exit codes (fail-safe, matching pathscan's own advisory-first posture — this
check is first-of-kind and not yet reviewed, so its one live wiring
(atelier's own `ci.yml`, see WIRING RESIDUAL above) passes `--warn`; THE
FLIP TO BLOCKING IS A SEPARATE RULING, not this build's to take):
  0  clean; or --warn was given and only `violation` findings exist
  1  `violation` finding(s) present, and --warn was NOT given
  2  usage / config error — a malformed map, an unresolvable region/template/
     source file, a stale heading, a missing bullet anchor, a `git show`
     failure, bad CLI arguments (NEVER downgraded by --warn — a broken scan
     is not a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can
run it with the system python3 and no install — and CI needs nothing but
Python.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# A line/span carrying this marker exempts exactly one `violation` finding —
# never an integrity finding (`stale-heading`, `missing-bullet`, `missing-
# file`, `missing-region`). Same tightened contract as every sibling
# scanner's allow marker (datescan's DSR8): word boundary, colon, a
# non-empty reason, so a bare mention of the marker text does not silently
# exempt anything.
ALLOW_MARKER = "blockscan:allow"
ALLOW_MARKER_RX = re.compile(r"\b" + re.escape(ALLOW_MARKER) + r":\s*[\w\"'“‘]")

DEFAULT_MAP_NAME = "blockscan_map.json"

_HEADING_RX = re.compile(r"^#{1,6}\s")
_TOP_BULLET_RX = re.compile(r"\n-\s\*\*")


class ConfigError(RuntimeError):
    """The map, a mapped file, or the git plumbing is unusable. Fail closed —
    never scan on a guess about what the map meant."""


@dataclass
class Finding:
    kind: str        # "violation" | "stale-heading" | "missing-bullet"
                      # | "missing-file" | "missing-region" | "skipped"
                      # | "moved"
    bullet: str | None
    source_path: str | None
    heading: str | None
    line: int
    detail: str


# --------------------------------------------------------------- the map --

def load_map(map_path: Path) -> dict:
    """Parse and structurally validate `blockscan_map.json`. Raises
    ConfigError on anything the rest of this module could not safely act on
    — an unreadable map must never read as "nothing to check"."""
    try:
        raw = json.loads(map_path.read_text(encoding="utf-8"))
    except OSError as e:
        raise ConfigError(f"cannot read map {map_path}: {e}") from e
    except json.JSONDecodeError as e:
        raise ConfigError(f"map {map_path} is not valid JSON: {e}") from e

    for key in ("region", "template", "bullets"):
        if key not in raw:
            raise ConfigError(f"map {map_path} is missing top-level `{key}`")

    for side in ("region", "template"):
        entry = raw[side]
        for field in ("path", "begin_marker", "end_marker"):
            if not entry.get(field):
                raise ConfigError(f"map {map_path}: `{side}.{field}` is required")

    bullets = raw["bullets"]
    if not isinstance(bullets, dict) or not bullets:
        raise ConfigError(f"map {map_path}: `bullets` must be a non-empty object")
    for bid, decl in bullets.items():
        if not decl.get("anchor"):
            raise ConfigError(f"map {map_path}: bullet `{bid}` needs an `anchor`")
        sources = decl.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ConfigError(
                f"map {map_path}: bullet `{bid}` needs a non-empty `sources` list")
        for s in sources:
            if not s.get("path") or not s.get("heading"):
                raise ConfigError(
                    f"map {map_path}: bullet `{bid}` has a source with no "
                    "`path`/`heading`")
    return raw


# ----------------------------------------------------------- text helpers --

def extract_between(text: str, begin_name: str, end_name: str) -> str | None:
    """The lines strictly between a `<!-- <begin_name> ... -->` marker (its
    trailing attributes, if any — the template's `stamp:begin` carries
    `source=` and `region=` — are not otherwise inspected here; `blockscan`
    is not `stampscan`, it does not resolve them) and a bare
    `<!-- <end_name> -->` marker. None if either does not resolve to exactly
    one marker line — a config error to the caller, never a silent empty
    region."""
    begin_rx = re.compile(r"^<!--\s*" + re.escape(begin_name) + r"\b.*-->\s*$")
    end_rx = re.compile(r"^<!--\s*" + re.escape(end_name) + r"\s*-->\s*$")
    lines = text.splitlines()
    start = end = None
    for i, line in enumerate(lines):
        s = line.strip()
        if start is None:
            if begin_rx.match(s):
                start = i
            continue
        if end is None and end_rx.match(s):
            end = i
            break
    if start is None or end is None:
        return None
    return "\n".join(lines[start + 1:end])


def _heading_line_index(text: str, heading: str) -> int | None:
    """The zero-based line index of `heading` in `text`, or None if it does
    not resolve to EXACTLY ONE line — missing or ambiguous are both the map
    going stale, never a silent pick of "the first one"."""
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.strip() == heading.strip()]
    return matches[0] if len(matches) == 1 else None


def extract_section(text: str, heading: str) -> list[str] | None:
    """The lines strictly between one heading line (matched EXACTLY, after
    stripping) and the next heading line OF ANY LEVEL — non-recursive, see
    module docstring. None if the heading does not resolve to EXACTLY ONE
    line in `text` (see `_heading_line_index`)."""
    idx = _heading_line_index(text, heading)
    if idx is None:
        return None
    lines = text.splitlines()
    start = idx + 1
    end = len(lines)
    for i in range(start, len(lines)):
        if _HEADING_RX.match(lines[i]):
            end = i
            break
    return lines[start:end]


def extract_bullet(region_text: str, anchor: str) -> tuple[str, int] | None:
    """The full text of the top-level bullet whose bold lead-in is `anchor`
    — from the start of its own line to (not including) the next top-level
    bullet (`\\n- **...`) or the end of `region_text`. Returns
    `(bullet_text, start_index)`, the index used only to report a line
    number. None if `anchor` does not resolve to EXACTLY ONE occurrence."""
    first = region_text.find(anchor)
    if first == -1:
        return None
    if region_text.find(anchor, first + 1) != -1:
        return None
    line_start = region_text.rfind("\n", 0, first) + 1
    m = _TOP_BULLET_RX.search(region_text, first + len(anchor))
    end = m.start() if m else len(region_text)
    return region_text[line_start:end], line_start


def _normalise(lines: list[str]) -> list[str]:
    return [ln.rstrip() for ln in lines]


def _has_allow(*texts: str) -> bool:
    return any(ALLOW_MARKER_RX.search(t) for t in texts)


# -------------------------------------------------------------- git plane --

def git_show(root: Path, rev: str, relpath: str) -> str:
    """`git show <rev>:<relpath>`, decoded. Raises ConfigError on ANY
    failure — see module docstring's ONE STATED ASSUMPTION: every mapped
    path is assumed to already exist at every revision this tool reads."""
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{rev}:{relpath}"],
        capture_output=True, text=True)
    if result.returncode != 0:
        raise ConfigError(
            f"git show {rev}:{relpath} failed: {result.stderr.strip()}")
    return result.stdout


def git_show_staged(root: Path, relpath: str) -> str:
    """`git show :<relpath>` — the INDEX blob, i.e. the content this commit
    is about to make true. Git's own object spec is `:<path>` with no
    revision before the colon (an empty rev, not the literal string ":"),
    so this is a distinct helper rather than `git_show(root, ":", relpath)`
    — that call would build `::<relpath>`, which git refuses outright."""
    result = subprocess.run(
        ["git", "-C", str(root), "show", f":{relpath}"],
        capture_output=True, text=True)
    if result.returncode != 0:
        raise ConfigError(
            f"git show :{relpath} failed: {result.stderr.strip()}")
    return result.stdout


# --------------------------------------------------------- integrity mode --

def check_integrity(cfg: dict, read_text) -> list[Finding]:
    """Verify the map's own integrity against whatever `read_text(path)`
    returns — every mapped heading resolves to exactly one line in its
    source doc, and every bullet anchor resolves to exactly one bullet in
    both the region and the template. Never suppressible by an allow
    marker (see module docstring)."""
    findings: list[Finding] = []

    region_full = read_text(cfg["region"]["path"])
    region_body = extract_between(
        region_full, cfg["region"]["begin_marker"], cfg["region"]["end_marker"])
    if region_body is None:
        findings.append(Finding(
            "missing-region", None, cfg["region"]["path"], None, 0,
            f"markers {cfg['region']['begin_marker']!r}/"
            f"{cfg['region']['end_marker']!r} not found in "
            f"{cfg['region']['path']}"))

    template_full = read_text(cfg["template"]["path"])
    template_body = extract_between(
        template_full, cfg["template"]["begin_marker"], cfg["template"]["end_marker"])
    if template_body is None:
        findings.append(Finding(
            "missing-region", None, cfg["template"]["path"], None, 0,
            f"markers {cfg['template']['begin_marker']!r}/"
            f"{cfg['template']['end_marker']!r} not found in "
            f"{cfg['template']['path']}"))

    source_cache: dict[str, str] = {}
    for bullet_id, decl in cfg["bullets"].items():
        if region_body is not None:
            if extract_bullet(region_body, decl["anchor"]) is None:
                findings.append(Finding(
                    "missing-bullet", bullet_id, cfg["region"]["path"], None, 0,
                    f"anchor {decl['anchor']!r} does not resolve to exactly "
                    f"one bullet in {cfg['region']['path']}'s "
                    f"{cfg['region']['begin_marker']} region"))
        if template_body is not None:
            if extract_bullet(template_body, decl["anchor"]) is None:
                findings.append(Finding(
                    "missing-bullet", bullet_id, cfg["template"]["path"], None, 0,
                    f"anchor {decl['anchor']!r} does not resolve to exactly "
                    f"one bullet in {cfg['template']['path']}'s "
                    f"{cfg['template']['begin_marker']} region"))
        for src in decl["sources"]:
            path = src["path"]
            if path not in source_cache:
                source_cache[path] = read_text(path)
            section = extract_section(source_cache[path], src["heading"])
            if section is None:
                findings.append(Finding(
                    "stale-heading", bullet_id, path, src["heading"], 0,
                    f"heading {src['heading']!r} does not resolve to exactly "
                    f"one line in {path} — renamed, removed, or duplicated"))

    return findings


# ------------------------------------------------------------ staged mode --

def check_costaged(root: Path, cfg: dict, read_old, read_new) -> list[Finding]:
    """The co-change rule, generic over WHERE "old" and "new" come from.

    `--staged` (the hook plane) calls this with OLD = `HEAD` and NEW = the
    index — what the commit is about to make true, per PROPAGATION.md's own
    framing of the staged plane. `--against <rev>` (the CI backstop, matching
    harvestscan's own `--against HEAD^` convention) calls it with OLD =
    `<rev>` and NEW = `HEAD`, because a CI checkout's index is identical to
    `HEAD` — there is no staged diff to read there, so the question CI can
    actually ask is "did the commit that just landed move both copies",
    exactly the question `--staged` asks of the index before a commit exists
    at all. Runs the integrity check against the NEW content first
    (comparing OLD to NEW is meaningless once a heading or bullet cannot be
    located); then, for every bullet whose mapped section text changed,
    requires both the region's and the template's bullet text to have
    changed too, or a scoped allow marker."""

    findings = list(check_integrity(cfg, read_new))
    if any(f.kind in ("missing-region", "missing-bullet", "stale-heading")
           for f in findings):
        # The map cannot be trusted against the state about to be
        # committed — reporting a co-change violation on top of that would
        # be building on a resolution we already know is broken.
        return findings

    region_new_full = read_new(cfg["region"]["path"])
    region_old_full = read_old(cfg["region"]["path"])
    template_new_full = read_new(cfg["template"]["path"])
    template_old_full = read_old(cfg["template"]["path"])
    region_new_body = extract_between(
        region_new_full, cfg["region"]["begin_marker"], cfg["region"]["end_marker"])
    region_old_body = extract_between(
        region_old_full, cfg["region"]["begin_marker"], cfg["region"]["end_marker"])
    template_new_body = extract_between(
        template_new_full, cfg["template"]["begin_marker"], cfg["template"]["end_marker"])
    template_old_body = extract_between(
        template_old_full, cfg["template"]["begin_marker"], cfg["template"]["end_marker"])

    new_source_cache: dict[str, str] = {}
    old_source_cache: dict[str, str] = {}

    for bullet_id, decl in cfg["bullets"].items():
        region_new_bullet = extract_bullet(region_new_body, decl["anchor"])
        region_old_bullet = extract_bullet(region_old_body, decl["anchor"])
        template_new_bullet = extract_bullet(template_new_body, decl["anchor"])
        template_old_bullet = extract_bullet(template_old_body, decl["anchor"])
        # Already proven present in the NEW content above; the OLD side is
        # allowed to fail to resolve (a bullet's wording moved this commit,
        # not just its body — treated as "the bullet changed", the safe
        # direction: it can only turn a would-be violation into a pass).
        region_changed = (region_old_bullet is None
                          or region_old_bullet[0] != region_new_bullet[0])
        template_changed = (template_old_bullet is None
                            or template_old_bullet[0] != template_new_bullet[0])

        for src in decl["sources"]:
            path = src["path"]
            if path not in new_source_cache:
                new_source_cache[path] = read_new(path)
                old_source_cache[path] = read_old(path)
            new_section = extract_section(new_source_cache[path], src["heading"])
            old_section = extract_section(old_source_cache[path], src["heading"])
            if new_section is None:
                continue  # already reported as stale-heading above
            if old_section is not None and _normalise(old_section) == _normalise(new_section):
                continue  # this source did not change in this commit

            # +2: the heading's own 0-based line index, plus one to land on
            # the section's first body line, plus one for 1-based display.
            line = _heading_line_index(new_source_cache[path], src["heading"]) + 2

            if region_changed and template_changed:
                findings.append(Finding(
                    "moved", bullet_id, path, src["heading"], line,
                    "source section changed; both the region bullet and the "
                    "template bullet changed with it"))
                continue

            new_section_text = "\n".join(new_section)
            allowed = _has_allow(
                new_section_text,
                region_new_bullet[0] if region_new_bullet else "",
                template_new_bullet[0] if template_new_bullet else "")
            if allowed:
                findings.append(Finding(
                    "skipped", bullet_id, path, src["heading"], line,
                    f"blockscan:allow — comparison skipped ("
                    f"region_changed={region_changed}, "
                    f"template_changed={template_changed})"))
                continue

            missing = []
            if not region_changed:
                missing.append(cfg["region"]["path"])
            if not template_changed:
                missing.append(cfg["template"]["path"])
            findings.append(Finding(
                "violation", bullet_id, path, src["heading"], line,
                f"{path} § {src['heading']!r} changed in this commit but "
                f"bullet {decl['anchor']!r} did not change in: "
                + ", ".join(missing)
                + f". Either move the bullet in both files, or add "
                  f"'<!-- {ALLOW_MARKER}: <reason> -->' to the changed "
                  f"section or the bullet."))

    return findings


# -------------------------------------------------------------- reporting --

_CONFIG_ERROR_KINDS = {"missing-region", "missing-bullet", "stale-heading",
                       "missing-file"}
_VIOLATION_KINDS = {"violation"}
_CLEAN_KINDS = {"moved", "skipped"}


def _suppression_line(findings: list[Finding]) -> str:
    skipped = sum(1 for f in findings if f.kind == "skipped")
    return f"  suppressed: {skipped} finding(s) by allow-marker"


def render_human(findings: list[Finding]) -> str:
    errors = [f for f in findings if f.kind in _CONFIG_ERROR_KINDS]
    violations = [f for f in findings if f.kind in _VIOLATION_KINDS]
    notes = [f for f in findings if f.kind in _CLEAN_KINDS]

    if not findings:
        return "✓ blockscan clean — nothing to check moved without its block bullet."

    lines: list[str] = []
    if errors:
        lines.append(f"✗ blockscan: {len(errors)} config error(s) (fail-safe, map is stale).")
        for f in sorted(errors, key=lambda x: (x.bullet or "", x.source_path or "")):
            lines.append(f"  [{f.kind}] bullet={f.bullet} {f.source_path} "
                        f"heading={f.heading!r}  {f.detail}")
    if violations:
        lines.append(f"✗ blockscan: {len(violations)} co-change violation(s).")
        for f in sorted(violations, key=lambda x: (x.bullet or "", x.source_path or "")):
            lines.append(f"  {f.source_path}:{f.line}  bullet={f.bullet}  {f.detail}")
    if not errors and not violations:
        lines.append(f"✓ blockscan clean — {len(notes)} mapped section(s) checked.")
    if notes:
        lines.append(f"  ({len(notes)} note(s): "
                     + ", ".join(sorted({f.kind for f in notes})) + ")")
        for f in sorted(notes, key=lambda x: (x.bullet or "", x.source_path or "")):
            lines.append(f"    {f.source_path}:{f.line}  [{f.kind}] bullet={f.bullet}  {f.detail}")
    lines.append(_suppression_line(findings))
    if violations:
        lines.append(
            "\n  A real co-change violation: move the bullet in BOTH "
            "docs/method/PROPAGATION.md's floor region and "
            "docs/build/templates/CLAUDE.md's stamped copy.")
        lines.append(
            f"  A deliberate exemption: add '<!-- {ALLOW_MARKER}: <reason> -->' "
            "to the changed section or the bullet. A marker with no reason "
            "exempts nothing.")
    if errors:
        lines.append(
            "\n  A stale map: docs/method/... changed heading text, or the "
            "block/template lost a bullet. Fix tools/blockscan_map.json or "
            "the doc/block/template it points at — never suppress this with "
            "an allow marker, it has none.")
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="blockscan",
        description="Check that a change to a mapped method-doc section "
                    "also moves the child block's copy of it, and the "
                    "scaffold template's.")
    ap.add_argument("paths", nargs="*",
                    help="ignored; accepted for symmetry with sibling "
                         "scanners — blockscan's unit is the hand-maintained "
                         "map (tools/blockscan_map.json), not a path list")
    ap.add_argument("--root", default=".",
                    help="repo root for the map, git plumbing, and relative "
                         "paths inside it")
    ap.add_argument("--map", default=None,
                    help="path to the map file (default: "
                         f"<root>/tools/{DEFAULT_MAP_NAME})")
    ap.add_argument("--staged", action="store_true",
                    help="the co-change check against the git index (the "
                         "hook plane) — what this commit is about to make "
                         "true, per PROPAGATION.md's own framing")
    ap.add_argument("--check", action="store_true",
                    help="whole-tree integrity-only mode: verifies the map "
                         "still resolves against what's on disk, with no "
                         "co-change check (that needs --staged or --against). "
                         "This is also what runs with none of the three given.")
    ap.add_argument("--against", default=None, metavar="REV",
                    help="the co-change check between REV (old) and HEAD "
                         "(new) — the CI backstop, for a checkout with no "
                         "staged diff to read (matches harvestscan's own "
                         "--against HEAD^ convention: 'did the commit that "
                         "just landed move both copies')")
    ap.add_argument("--warn", action="store_true",
                    help="report violation findings but always exit 0 for "
                         "them (advisory rollout — first-of-kind, not yet "
                         "reviewed). Never downgrades a config error.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    modes_given = sum([args.staged, args.check, args.against is not None])
    if modes_given > 1:
        print("blockscan: --staged, --check, and --against are mutually "
              "exclusive", file=sys.stderr)
        return 2

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"blockscan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    map_path = Path(args.map).resolve() if args.map else root / "tools" / DEFAULT_MAP_NAME
    try:
        cfg = load_map(map_path)
        if args.staged:
            findings = check_costaged(
                root, cfg,
                read_old=lambda p: git_show(root, "HEAD", p),
                read_new=lambda p: git_show_staged(root, p))
        elif args.against is not None:
            findings = check_costaged(
                root, cfg,
                read_old=lambda p: git_show(root, args.against, p),
                read_new=lambda p: git_show(root, "HEAD", p))
        else:
            def read_disk(relpath: str) -> str:
                p = root / relpath
                if not p.is_file():
                    raise ConfigError(f"mapped path does not exist: {relpath}")
                return p.read_text(encoding="utf-8", errors="replace")
            findings = check_integrity(cfg, read_disk)
    except ConfigError as e:
        print(f"blockscan: {e}", file=sys.stderr)
        return 2

    errors = [f for f in findings if f.kind in _CONFIG_ERROR_KINDS]
    violations = [f for f in findings if f.kind in _VIOLATION_KINDS]

    if args.json:
        print(json.dumps({
            "clean": not errors and not violations,
            "warn": args.warn,
            "findings": [asdict(f) for f in findings],
            "suppressed": {"by_allow_marker":
                          sum(1 for f in findings if f.kind == "skipped")},
        }, indent=2))
    else:
        print(render_human(findings))
        if violations and args.warn and not errors:
            print("\n  (--warn: advisory only — not blocking this build.)")

    if errors:
        return 2  # fail-safe: NEVER downgraded by --warn
    if violations:
        return 0 if args.warn else 1
    return 0


def _selftest() -> int:
    """Minimal smoke test so `blockscan --selftest` proves the engine on any
    box, even where the unittest file isn't shipped. Builds a tiny git repo
    (blockscan's --staged mode needs real git plumbing) with a stripped-down
    map, region, template, and source doc, and exercises the co-change
    rule end to end."""
    import shutil
    import tempfile

    tmp = Path(tempfile.mkdtemp(prefix="blockscan-self-"))
    run = lambda *a: subprocess.run(  # noqa: E731 - local test helper
        ["git", "-C", str(tmp), *a], check=True,
        capture_output=True, text=True)

    (tmp / "docs" / "method").mkdir(parents=True)
    (tmp / "docs" / "build" / "templates").mkdir(parents=True)
    (tmp / "tools").mkdir()

    def write_apex(body: str) -> None:
        (tmp / "docs" / "method" / "APEX.md").write_text(
            "# Apex\n\n## Honesty is absolute\n\n" + body + "\n"
            "## Adaptation is continuous\n\nOther text.\n")

    def write_propagation(bullet: str) -> None:
        (tmp / "docs" / "method" / "PROPAGATION.md").write_text(
            "# Propagation\n\n<!-- floor:begin -->\n"
            "## Doctrine\n\n" + bullet + "\n"
            "- **Concurrency:** other bullet text.\n"
            "<!-- floor:end -->\n")

    def write_template(bullet: str) -> None:
        (tmp / "docs" / "build" / "templates" / "CLAUDE.md").write_text(
            "<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n"
            "## Doctrine\n\n" + bullet + "\n"
            "- **Concurrency:** other bullet text.\n"
            "<!-- stamp:end -->\n")

    map_doc = {
        "region": {"path": "docs/method/PROPAGATION.md",
                  "begin_marker": "floor:begin", "end_marker": "floor:end"},
        "template": {"path": "docs/build/templates/CLAUDE.md",
                    "begin_marker": "stamp:begin", "end_marker": "stamp:end"},
        "bullets": {
            "apex": {
                "anchor": "**The apex:**",
                "sources": [{"path": "docs/method/APEX.md",
                            "heading": "## Honesty is absolute"}],
            }
        },
    }
    (tmp / "tools" / "blockscan_map.json").write_text(json.dumps(map_doc))

    write_apex("Original honesty text.")
    write_propagation("- **The apex:** Original block wording.\n")
    write_template("- **The apex:** Original block wording.\n")

    run("init", "-q", "-b", "main")
    run("config", "user.email", "test@example.com")  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
    run("config", "user.name", "Test")
    run("add", "-A")
    run("commit", "-q", "-m", "init")

    ok = True

    # 1. Unchanged everything -> clean.
    r = subprocess.run([sys.executable, __file__, "--staged", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: unchanged-tree case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False

    # 2. Source section changed, block NOT moved -> violation, exit 1.
    write_apex("Reworded honesty text.")
    run("add", "-A")
    r = subprocess.run([sys.executable, __file__, "--staged", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 1 or "violation" not in r.stdout:
        print(f"FAIL: unmoved-block case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False
    run("commit", "-q", "-m", "reword (violation, not fixed)")

    # 3. Source section AND both block copies changed -> clean.
    write_apex("Reworded again honesty text.")
    write_propagation("- **The apex:** Updated block wording.\n")
    write_template("- **The apex:** Updated block wording.\n")
    run("add", "-A")
    r = subprocess.run([sys.executable, __file__, "--staged", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: moved-both case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False
    run("commit", "-q", "-m", "reword and move both")

    # 4. Source changed, only ONE block copy moved -> violation naming the other.
    write_apex("Third wording of honesty text.")
    write_propagation("- **The apex:** Updated again wording.\n")
    # template left unmoved
    run("add", "-A")
    r = subprocess.run([sys.executable, __file__, "--staged", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 1 or "docs/build/templates/CLAUDE.md" not in r.stdout:
        print(f"FAIL: half-moved case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False

    # 5. Same half-moved change, but with an allow marker -> clean.
    write_apex("Third wording of honesty text. "
              "<!-- blockscan:allow: deliberate, template pending -->")
    run("add", "-A")
    r = subprocess.run([sys.executable, __file__, "--staged", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: allow-marker case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False
    run("commit", "-q", "-m", "reword with allow marker")

    # 6. Renamed heading -> stale-heading config error, exit 2, staged.
    write_apex("## Honesty absolutely\n\nSome text.")
    # (deliberately mis-titled so the mapped heading no longer resolves)
    (tmp / "docs" / "method" / "APEX.md").write_text(
        "# Apex\n\n## Honesty absolutely\n\nRenamed heading body.\n"
        "## Adaptation is continuous\n\nOther text.\n")
    run("add", "-A")
    r = subprocess.run([sys.executable, __file__, "--staged", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 2 or "stale-heading" not in r.stdout:
        print(f"FAIL: renamed-heading case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False
    run("checkout", "--", ".")  # discard the rename for the remaining checks

    # 7. Unknown bullet id in a hand-broken map -> missing-bullet, exit 2,
    #    exercised through --check (no git needed for this one).
    bad_map = json.loads(json.dumps(map_doc))
    bad_map["bullets"]["ghost"] = {
        "anchor": "**Does not exist anywhere:**",
        "sources": [{"path": "docs/method/APEX.md",
                    "heading": "## Adaptation is continuous"}],
    }
    (tmp / "tools" / "blockscan_map.json").write_text(json.dumps(bad_map))
    r = subprocess.run([sys.executable, __file__, "--check", "--root", str(tmp)],
                       capture_output=True, text=True)
    if r.returncode != 2 or "missing-bullet" not in r.stdout:
        print(f"FAIL: unknown-bullet-id case exited {r.returncode}: {r.stdout}{r.stderr}")
        ok = False

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    try:
        return _main(argv)
    except ConfigError as e:
        print(f"blockscan: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

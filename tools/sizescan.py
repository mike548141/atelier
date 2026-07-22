#!/usr/bin/env python3
"""sizescan — the signal that a current-truth file carries relocatable cold content.

The operating model assumes a session resumes *cold* by reading a handful of
files at the start: the roadmap (what's open), the session index (where the last
one stopped), the README, the architecture note. That only stays cheap if those
files stay honest. RECORD.md already prescribes the fix — a **current-truth /
history split**: `ROADMAP.md` holds what's open and completed detail moves to
`ROADMAP-DONE.md`; `SESSIONS.md` is a one-line-per-session index and detail lives
in `docs/sessions/`; specs live in a grepped-on-demand `SPECS.md`. The split
works — but nothing *triggered* it. The discipline decayed silently: a roadmap
grew past three thousand lines, each finished item accreting a running log of how
it got done, and no signal fired. sizescan is that missing signal.

**What it meters — cost is size × read-frequency** (Mike's ruling, 2026-07-20,
which reversed an earlier line-count gate). A hot-path file — read every session
(`CLAUDE`, `ROADMAP`, the `SESSIONS` tail, the start-path docs) — pays its length
at every open; a cold store — grepped on demand (`ROADMAP-DONE`, session detail,
archives) — is nearly free. So the enemy is never *size*: it is **cold content
sitting on the hot path** — completed work, closed cycles, resolved narrative
that has stopped being current-truth and now just taxes every read. Move it to
the cold store and the hot file shrinks *losslessly*, no content harmed. That is
the whole game, and it makes the two-sided rule below fair:

  * A hot file that is large **purely from live current-truth** — a roadmap of a
    hundred genuinely-open items — is **never** penalised. Fulsomeness on the hot
    path is not a defect when the bulk is current; there is nothing to relocate,
    and trimming a true signal to hit a number is the failure this tool was
    reworked to stop causing (the flat-300-line gate redding a 315-line roadmap
    for being fulsome, on a number grounded in nothing).

  * A hot file that carries **relocatable cold content** *is* flagged — and, under
    `--check`, **gates**, because the remedy is a pure-win move (harvest to the
    `-DONE` store), never a reword. There is no magic number here: the trigger is
    *"is there cold content to relocate"*, not *"> N lines"*.

**Detecting cold content — the crisp signal and the honest edge.** The one form
of cold content a machine can name without guessing is a **completed checkbox
item** — a `- [x]` line in a file whose convention is a checkbox worklog
(`ROADMAP.md`). By that file's own doctrine (the current-truth/history split) a
done item belongs in `ROADMAP-DONE.md`; left inline it is pure cost with a
lossless fix. So *that* is what `--check` gates on: the presence of `[x]` items
on the hot path. **Prose-shaped cold content** — resolved narrative packed under
a still-open `[ ]` item, a closed-cycle write-up with no checkbox — is real cold
content too, but it cannot be detected without guessing, so it is **caught at
review, never measured**. The line-count advisory below is the pointer to that
review: an unusually long hot file is the cue for a human to look for un-marked
resolved narrative. This mirrors the tool's standing one-sided honesty — a
too-*thin* file (a hollow ARCHITECTURE.md that lies by omission) is the worse
defect, but thinness is judgement caught at review under the stub-honestly rule
(`00-APEX.md`), never a measured floor.

**Line count is advisory — it never gates.** Every hot-path file's length is
reported for visibility, and flagged when it runs past a **class reference
point** (`ROADMAP.md` ~300, `SESSIONS.md` ~250, and so on — grounded in where the
fleet's *healthy* instances sit, not tuned). That flag is a nudge, not a verdict:
"large — check for un-marked resolved narrative; if it is all live current-truth,
this is fine." It is exactly what surfaces a `SESSIONS.md` that has regressed from
a lean index back to a flat log — the size balloons, the advisory fires, a human
splits it. But a reference point is not a target: crossing it can never fail a
build, so it can never induce the line-golf it once did (source made *worse* —
a wrapped bullet merged into one over-long line — purely to hit a round number).

Scope — two directions, by design:

  * Only the files **supposed to stay lean** are metered: the session-start reads
    and current-truth docs (`ROADMAP.md`, `SESSIONS.md`, `README.md`,
    `ARCHITECTURE.md`, `CLAUDE.md`). A long *reference* doc (`PRINCIPLES.md`, a
    doctrine file) is read on demand, not every session — not budgeted.

  * The **append-only stores are never size-metered** — `ROADMAP-DONE.md`,
    `CHANGELOG.md`, `SPECS.md`, and everything under `sessions/`, `reviews/`,
    `decisions/`, and archive dirs. Those are the *destinations* the split moves
    detail into; they are meant to grow. Flagging their size would punish the
    very fix the tool exists to encourage.

**Harvest integrity — the archive must hold no live state** (Mike's ruling,
2026-07-22, after a real incident: an un-harvested `[x]` on the hot path had
already redded the floor for three pushes, and the first manual sweep of the
archive found a `[ ]` parent whose children were all DONE). The named archive
stores (`*-DONE.md`, `*-ARCHIVE.md`) record *finished* history, so a live state
marker there — an open `[ ]`, a claimed `[~]`, a queued `⏳` list item — is
either a **botched harvest** (open work silently buried where no session will
re-read it) or an **untrue state** (done work whose box was never flipped).
Under `--check` that **gates**, same contract as cold content: the state is
machine-checkable and the incident class is real. What the gate demands is
*state coherence only* — it never verifies that `[x]` items were actually
delivered (deliberately: that overhead belongs to review, not a scanner). The
box grammar is a work-owed tri-state (Mike's ruling, 2026-07-22): `[ ]` work
still owed · `[~]` claimed/underway · `[x]` **no more work owed** — whether
delivered, superseded, or declined, with the disposition said in the item's
own text (a dated note), never a fourth bracket. Parent and child lines fire
independently, so a live parent over done children and a stray live child
under a done parent are both caught. Stores are checked **wherever they
live** — the growth-store directory skip bounds *metering*, never integrity
(HI-F1). One accepted edge (HI-F6): a live marker in unfenced, indent-only
example code is line-indistinguishable from a nested child item and will
fire — acceptable because the remedy below is investigative (a false
positive costs a look, never a wrong fix); fence examples to avoid it. On a
hit the remedy is **investigative, never automatic**: the session that reds weighs the evidence (the item's
children, the session log, the code), then puts a recommendation to the
principal — flip to `[x]` with a dated disposition note, un-harvest back to
the roadmap, or reformat a parent that was only ever a heading. Never
silently fix.

Hatches (header-only — the first 15 lines, never the body, so a file that merely
*mentions* a marker in prose does not silently exempt itself):

  * `sizescan:allow` — exempt the file from **everything** (advisory *and* the
    cold-content gate). For a repo that deliberately keeps, say, a flat session
    log; keep the reason on the marker line so the exemption is self-documenting.
  * `sizescan:budget=N` — override the advisory **reference point** for a
    legitimately large all-current file, to quiet its size nudge. It does **not**
    touch the gate (the gate is cold content, not length), and — like any
    reference — it must be GROUNDED in the file's *class*, never derived from the
    file's current length. A number picked to sit just above today's line count is
    circular: it can't be exceeded the moment it's written and says nothing about
    what the file *should* be. Fix the file or ground the number; a true signal
    beats a silenced one.
  * A glob in `.sizescanignore` — skip a path wholesale.

Advisory by default. A bare `sizescan` **reports and exits 0** — drop it in CI to
surface the numbers without ever breaking a build. `--check` is the opt-in gate,
and it fails **only** on relocatable cold content (a `[x]` item on the hot path),
whose fix is lossless. Reviewed 2026-07-14 (cold, PASS-WITH-FINDINGS) and
reworked to this cold-content model 2026-07-20 (Mike's ruling, same day).

Exit codes (fail-safe — anything but a clean/advisory run is non-zero):
  0  clean; any advisory finding (size over reference); or gated findings
     present but --check was not given
  1  --check was given AND a hot-path file carries relocatable cold content
     ([x] items) or an archive store carries live state markers
  2  usage / config error (a scan that read nothing is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install — and CI needs nothing but Python.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# A file whose HEADER carries this marker is exempt from EVERYTHING — the size
# advisory and the cold-content gate (e.g. a repo that deliberately keeps a flat
# session log rather than an index). Keep the reason on the same line so the
# exemption is self-documenting.
ALLOW_MARKER = "sizescan:allow"

# A per-file override of the advisory REFERENCE POINT in the HEADER:
# `sizescan:budget=400` (or `: 400`, or a space). Lets a legitimately long
# all-current file quiet its size nudge. It does NOT affect the gate — the gate
# is relocatable cold content, not length — so this only moves an advisory line.
_BUDGET_MARKER = re.compile(r"sizescan:budget\s*[=:]?\s*(\d+)")

# Markers are honoured ONLY in the file's header — the first MARKER_SCAN_LINES
# lines — never in the body. Matching anywhere let a file that merely *mentions*
# a marker in prose (a roadmap item about budgets, a doc of the hatch) silently
# exempt or re-reference itself (F2), a per-file blast radius blunter than the
# sibling scanners' per-line allows. A real exemption is a deliberate declaration
# at the top of the file, where a reader meets it first.
MARKER_SCAN_LINES = 15


def _header(text: str) -> str:
    return "\n".join(text.splitlines()[:MARKER_SCAN_LINES])


# The current-truth files that must stay lean, and the **advisory reference
# point** (not a gate) each is measured against. Keyed by exact basename. These
# are the files a session loads at start or leans on as "what's true / open now";
# a reference doc read on demand is not here by design. The numbers are grounded,
# not tuned: across the fleet the healthy instances of each sit well under them
# (session-index ~74, small-repo roadmaps 120-240); a file that clears one by a
# wide margin is worth a human's eye — but crossing it never fails a build.
SIZE_REFERENCE = {
    "ROADMAP.md": 300,        # open + prioritised only; done detail → ROADMAP-DONE.md
    "SESSIONS.md": 250,       # one line per session; detail → docs/sessions/
    "README.md": 250,
    "ARCHITECTURE.md": 250,
    "CLAUDE.md": 200,
}

# Files whose convention is a **checkbox worklog**, where a completed item
# (`- [x]`) is relocatable cold content by the file's own doctrine (the
# current-truth/history split: a done item belongs in ROADMAP-DONE.md). These are
# the files whose cold content the `--check` gate fires on. Keyed by basename; a
# child repo's ROADMAP inherits the convention, so this travels with the name.
COLD_CHECKBOX_FILES = {"ROADMAP.md"}

# A completed checkbox list item — the one crisp, un-guessable form of cold
# content. Anchored to a list bullet so a `[x]` inside prose (a sentence about
# checkbox states, a quoted example) is not miscounted; `[X]` tolerated. Every
# Markdown bullet marker counts — `-`, `*`, `+`, and ordered (`1.` / `1)`) — so a
# done item written in any list style is caught. Open `[ ]`, claimed `[~]`, and
# the review-queued `⏳` are LIVE states, not cold.
_COLD_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\[[xX]\]")

# A fenced-code-block delimiter (``` or ~~~). A `[x]` line inside a fence is a
# quoted example, not a work item — the counters toggle on these so they never
# fire on documentation that *shows* checkbox syntax. A fence left UNCLOSED at
# EOF gets no such immunity (HI-F2): the swallowed tail is counted as if the
# fence never opened, because "everything after a stray ```" silently reading
# as quoted was a fail-open — an unclosed fence is a defect to surface, never
# a hatch.
_FENCE = re.compile(r"^\s*(?:```|~~~)")

# The named archive stores — where harvested / rotated detail comes to rest.
# Matched by basename suffix so the convention travels to children and to any
# future store that adopts the naming (`SESSIONS-ARCHIVE.md` etc.).
ARCHIVE_STORE_SUFFIXES = ("-DONE.md", "-ARCHIVE.md")

# A LIVE state marker as a list item: open `[ ]`, claimed `[~]`, or the queued
# `⏳` — states that mean *work is not finished*. In an archive store any of
# these is a harvest-integrity defect (a botched harvest, or a box never
# flipped). Anchored to a list bullet exactly like _COLD_ITEM, so a prose
# mention ("the `[ ]` state means…") or a backticked reference never fires —
# and a BLOCKQUOTED item (`> - [ ]`) deliberately doesn't either: the `>`
# breaks the bullet anchor, and quoted material is not a work item, the same
# rationale as fences (HI-F5 — documented so the skip is a decision, not an
# accident of regex shape).
# Superseded / declined work is archived as `[x]` with a dated disposition
# note in the item's text — the box is a work-owed tri-state, never a
# disposition (Mike's ruling, 2026-07-22).
_LIVE_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\[ \]|\[~\]|⏳)")


def is_archive_store(basename: str) -> bool:
    return basename.endswith(ARCHIVE_STORE_SUFFIXES)

# `README.md` and `CLAUDE.md` are current-truth only at the **repo root** — the
# front door and the session onramp. A nested `tools/README.md` or
# `docs/decisions/README.md` is a reference index, read on demand, and metering
# it would dilute the signal. The other names are singular by convention (one
# ROADMAP, one SESSIONS index per repo) so they're metered wherever they live —
# root or `docs/`.
ROOT_ONLY = {"README.md", "CLAUDE.md"}

# Where completed / append-only detail is *meant* to accumulate — never metered.
# `ROADMAP-DONE.md`, `CHANGELOG.md`, `SPECS.md` fall out naturally (their
# basenames aren't in SIZE_REFERENCE); these path components catch a metered
# basename that lives inside a growth store (an `ARCHITECTURE.md` snapshotted
# under `_archive/`, a `README.md` inside `reviews/`).
SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv", "venv",
                  ".mypy_cache", ".ruff_cache", ".pytest_cache", ".idea",
                  ".vscode", "sessions", "reviews", "decisions",
                  "_archive", "archive", "intake"}


@dataclass
class Finding:
    path: str            # the flagged file, repo-relative
    lines: int           # its actual line count (advisory context, always shown)
    cold_items: int      # relocatable `[x]` items on the hot path (0 = none)
    reference: int       # the advisory size reference for its class
    over: int            # max(0, lines - reference); 0 = within reference
    store: str           # where its cold content / overflow belongs
    gated: bool          # True = fails --check (cold content or live markers)
    live_items: int = 0  # live state markers ([ ]/[~]/⏳) in an archive store


# The harvest hint per current-truth file — where its overflow belongs, so the
# report points at the fix, not just the symptom.
_STORE_HINT = {
    "ROADMAP.md": "harvest completed [x] items to ROADMAP-DONE.md (keep only what's open)",
    "SESSIONS.md": "if a flat log, split to an index + docs/sessions/ detail; if "
                   "already an index, rotate older entries to SESSIONS-ARCHIVE.md "
                   "(keep the recent tail)",
    "README.md": "move depth to docs/ (ARCHITECTURE.md, a guide) and point to it",
    "ARCHITECTURE.md": "split by subsystem or move detail to a design doc",
    "CLAUDE.md": "point to docs/ for detail; the onramp stays a thin index",
}


def reference_for(text: str, basename: str) -> int | None:
    """The advisory size reference this file is measured against, or None if it
    isn't a metered current-truth file. A header `sizescan:budget=N` overrides the
    class default for a legitimately long file — it moves the *advisory* line
    only, never the gate."""
    m = _BUDGET_MARKER.search(_header(text))
    if m:
        return int(m.group(1))
    return SIZE_REFERENCE.get(basename)


def _count_list_items(text: str, pattern: re.Pattern) -> int:
    """Count pattern-matching list items outside fenced code blocks. A fence
    that closes properly keeps its contents quoted; a fence still open at EOF
    is treated as if it never opened (HI-F2) — the swallowed tail is counted,
    fail-safe, because an unclosed fence must surface a marker, never hide
    one."""
    count = 0
    in_fence = False
    swallowed: list[str] = []   # lines inside a fence that may prove unclosed
    for line in text.splitlines():
        if _FENCE.match(line):
            in_fence = not in_fence
            if not in_fence:
                swallowed.clear()   # fence closed — its contents stay quoted
            continue
        if in_fence:
            swallowed.append(line)
        elif pattern.match(line):
            count += 1
    if in_fence:                    # EOF inside a fence: count the tail
        count += sum(1 for line in swallowed if pattern.match(line))
    return count


def live_item_count(text: str, basename: str) -> int:
    """Count live state markers (`[ ]` / `[~]` / `⏳` list items) in an archive
    store. Zero for any non-archive file — live states are the *point* of a
    roadmap; only in the finished-history store are they a defect. Fenced
    regions are skipped for the same reason as cold_item_count: a quoted
    example is not a work item."""
    if not is_archive_store(basename):
        return 0
    return _count_list_items(text, _LIVE_ITEM)


def cold_item_count(text: str, basename: str) -> int:
    """Count relocatable cold content: completed `[x]` checkbox items in a file
    whose convention is a checkbox worklog. Zero for any other file — a `[x]` in
    a README or a doctrine doc is prose, not a harvestable work item. A `[x]`
    inside a fenced code block is a quoted example, not a work item, so fenced
    regions are skipped."""
    if basename not in COLD_CHECKBOX_FILES:
        return 0
    return _count_list_items(text, _COLD_ITEM)


def count_lines(text: str) -> int:
    """Line count, newline-agnostic and not fooled by a trailing newline (a file
    ending in "\\n" is not one line longer than the same file without it)."""
    if not text:
        return 0
    return len(text.splitlines())


def load_ignore_globs(root: Path) -> list[str]:
    f = root / ".sizescanignore"
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


def _in_skipped_dir(p: Path, walk_base: Path) -> bool:
    """Is p inside a growth-store directory *within the scanned tree*? The skip
    names are matched against the path **relative to the scan base**, never the
    absolute path. Matching absolute parts was a fail-open bug (F1): a repo that
    merely *lives under* an ancestor named `archive`/`sessions`/`reviews`/… — the
    store names are ordinary English words — had every file skipped, so the scan
    read nothing and reported "clean", the exact contract violation the tool's
    own exit codes forbid ("a scan that read nothing is NOT a pass")."""
    try:
        rel_parts = p.relative_to(walk_base).parts
    except ValueError:
        rel_parts = (p.name,)
    return bool(SKIP_DIR_NAMES & set(rel_parts[:-1]))   # intermediate dirs only


def iter_candidates(paths: list[Path], root: Path, globs: list[str]):
    """Yield candidate files under the given paths, skipping growth-store dirs
    and ignored globs. A file is a candidate iff its basename is a metered
    current-truth file OR a named archive store (integrity-checked, never
    size-metered). Results are de-duplicated by resolved path so overlapping
    args (`sizescan . docs`) don't double-report the same file (F4)."""
    seen: set[Path] = set()
    for base in paths:
        base = base.resolve()
        walk_base = base if base.is_dir() else base.parent
        candidates = [base] if base.is_file() else [
            p for p in base.rglob("*") if p.is_file()]
        for p in candidates:
            rp = p.resolve()
            if rp in seen or (p.name not in SIZE_REFERENCE
                              and not is_archive_store(p.name)):
                continue
            # Archive stores bypass the skip-dir filter (HI-F1): SKIP_DIR_NAMES
            # exists to keep growth stores un-METERED, but integrity is checked
            # wherever a store lives — a `*-DONE.md` under `sessions/` or
            # `_archive/` silently escaping the gate was the fail-open class
            # ("a scan that read nothing is NOT a pass") reintroduced.
            if _in_skipped_dir(p, walk_base) and not is_archive_store(p.name):
                continue
            if p.name in ROOT_ONLY and rp.parent != root.resolve():
                continue
            if _ignored(_rel(p, root), globs):
                continue
            seen.add(rp)
            yield p


def scan_paths(paths: list[Path], root: Path) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    for p in iter_candidates(paths, root, globs):
        text = p.read_text(encoding="utf-8", errors="replace")
        if ALLOW_MARKER in _header(text):
            continue
        if is_archive_store(p.name):
            # Integrity only — an archive store is never size-metered. A live
            # marker gates under --check; a clean archive stays silent.
            live = live_item_count(text, p.name)
            if live:
                findings.append(Finding(
                    _rel(p, root), count_lines(text), 0, 0, 0,
                    "investigate, then recommend to the principal: flip to [x] "
                    "with a dated disposition note, or un-harvest to the "
                    "roadmap — never silently fix",
                    True, live))
            continue
        reference = reference_for(text, p.name)
        if reference is None:
            continue
        n = count_lines(text)
        cold = cold_item_count(text, p.name)
        over = max(0, n - reference)
        # Emit a finding only if there's something to say: relocatable cold
        # content (gates) or an over-reference size (advisory). A lean, all-open
        # hot file is silent.
        if cold or over:
            findings.append(Finding(_rel(p, root), n, cold, reference, over,
                                    _STORE_HINT.get(p.name, ""), cold > 0))
    return findings


def render_human(findings: list[Finding]) -> str:
    if not findings:
        return ("✓ sizescan clean — no relocatable cold content on the hot "
                "path; archive stores hold no live markers.")
    n_cold = sum(1 for f in findings if f.cold_items)
    n_live = sum(1 for f in findings if f.live_items)
    n_gated = sum(1 for f in findings if f.gated)
    n_adv = sum(1 for f in findings if not f.gated)
    head = (f"⚠ sizescan: {len(findings)} file(s) flagged "
            f"({n_cold} cold-content · {n_live} harvest-integrity · "
            f"{n_adv} size-advisory).\n")
    lines = [head]
    # Gated first (cold content, then archive integrity), then advisory;
    # within each, worst first.
    for f in sorted(findings, key=lambda x: (not x.gated, -x.cold_items,
                                             -x.live_items, -x.over)):
        lines.append(f"  {f.path}  {f.lines} lines")
        if f.cold_items:
            lines.append(f"      → {f.cold_items} completed [x] item(s) to harvest "
                         f"[cold-content, gated]")
            if f.store:
                lines.append(f"        {f.store}")
        if f.live_items:
            lines.append(f"      → {f.live_items} live state marker(s) "
                         f"([ ]/[~]/⏳ list items) in an archive store "
                         f"[harvest-integrity, gated]")
            if f.store:
                lines.append(f"        {f.store}")
        if f.over:
            lines.append(f"      → over the ~{f.reference}-line reference (+{f.over}) "
                         f"[size-advisory]")
    if n_live:
        lines.append("\n  Harvest-integrity (fails --check): a live marker in an "
                     "archive store is either a botched harvest (open work "
                     "silently buried) or an untrue state (done work never "
                     "flipped). Investigate the evidence — the item's children, "
                     "the session log, the code — then put a recommendation to "
                     "the principal: flip to [x] with a dated disposition note "
                     "(delivered / superseded / declined — say which), or "
                     "un-harvest back to the roadmap. Never silently fix, and "
                     "never verify [x] delivery here — state coherence only.")
    if n_cold:
        lines.append("\n  Cold-content (fails --check): a completed [x] item on the "
                     "hot path is pure cost with a lossless fix — move it to "
                     "ROADMAP-DONE.md (RECORD.md, the current-truth/history split). "
                     "Never reword to fit.")
    if n_adv:
        lines.append("\n  Size-advisory (never fails --check): the file is long. "
                     "Check for un-marked resolved narrative or a closed-cycle "
                     "write-up and harvest it; if the bulk is live current-truth, "
                     "this is fine — fulsomeness on the hot path is not a defect.")
    lines.append(f"  Legitimately long all-current file: declare 'sizescan:budget=N' "
                 f"in the first {MARKER_SCAN_LINES} lines (GROUNDED in the file's "
                 f"class, never its current length — see the module doc) to quiet the "
                 f"size advisory; '{ALLOW_MARKER}' to exempt fully; or a glob in "
                 f".sizescanignore. Neither hatch silences the cold-content gate — "
                 f"for that, harvest the [x] items.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="sizescan",
        description="Flag current-truth files (roadmap, session index, README…) "
                    "that carry relocatable cold content, or have grown past their "
                    "size reference.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo)")
    ap.add_argument("--root", default=".",
                    help="repo root for .sizescanignore and relative paths")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if a hot-path file carries relocatable cold "
                         "content (a completed [x] item — lossless remedy) or "
                         "an archive store carries live state markers "
                         "([ ]/[~]/⏳ — harvest integrity); the size advisory "
                         "never fails the build "
                         "(default: everything advisory, exit 0)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"sizescan: root does not exist: {args.root}", file=sys.stderr)
        return 2
    targets = [Path(p) for p in (args.paths or [str(root)])]
    missing = [str(p) for p in targets if not p.exists()]
    if missing:
        # A typo'd path scanning nothing must never read as a clean pass.
        print(f"sizescan: path does not exist: {', '.join(missing)}", file=sys.stderr)
        return 2
    try:
        findings = scan_paths(targets, root)
    except OSError as e:
        print(f"sizescan: cannot read {e.filename}: {e.strerror}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "clean": not findings,
            "findings": [asdict(f) for f in findings],
        }, indent=2))
    else:
        print(render_human(findings))

    # Advisory by default: everything is a report, exit 0. --check gives teeth to
    # the ONE thing whose remedy is a pure-win move — relocatable cold content (a
    # [x] item on the hot path). Size-over-reference is never a failure: a file
    # large purely from live current-truth has nothing to relocate, and gating it
    # would be the trim-a-true-signal trap the tool was reworked to stop.
    return 1 if (args.check and any(f.gated for f in findings)) else 0


def _selftest() -> int:
    """Minimal smoke test so `sizescan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped. Builds a tiny tree and asserts the
    core behaviours: cold content ([x] items) flags and gates; a large all-current
    file is advisory only (never gates); growth stores and reference docs are
    ignored; the hatches behave."""
    import tempfile
    import shutil

    tmp = Path(tempfile.mkdtemp(prefix="sizescan-self-"))
    docs = tmp / "docs"
    docs.mkdir()
    (docs / "sessions").mkdir()

    ref = SIZE_REFERENCE["ROADMAP.md"]
    over = "x\n" * (ref + 5)                 # over every reference, but no [x] items
    under = "x\n" * (min(SIZE_REFERENCE.values()) - 5)
    cold = "- [ ] open\n- [x] done one\n- [x] done two\n"   # small, but 2 cold items

    (docs / "ROADMAP.md").write_text(cold)                       # cold content → GATED
    (docs / "ROADMAP-DONE.md").write_text(over)                  # growth store → ignore
    (docs / "SPECS.md").write_text(over)                         # on-demand → ignore
    (tmp / "CHANGELOG.md").write_text(over)                      # append-only → ignore
    (tmp / "PRINCIPLES.md").write_text(over)                     # reference doc → not metered
    (docs / "sessions" / "SESSIONS.md").write_text(over)         # inside a store → ignore
    (tmp / "README.md").write_text(under)                        # root README, under → silent
    (tmp / "tools").mkdir()
    (tmp / "tools" / "README.md").write_text(over)               # nested README → not metered
    (tmp / "ARCHITECTURE.md").write_text(over)                   # large, no [x] → advisory only

    findings = {f.path.replace("\\", "/"): f for f in scan_paths([tmp], tmp)}
    ok = True

    # ROADMAP with [x] items: flagged, gated, count correct.
    r = findings.get("docs/ROADMAP.md")
    if not r or not r.gated or r.cold_items != 2:
        print(f"FAIL: cold-content ROADMAP not gated with 2 items: {r}")
        ok = False

    # Large ARCHITECTURE with no [x]: flagged advisory, NOT gated.
    a = findings.get("ARCHITECTURE.md")
    if not a or a.gated or a.cold_items != 0 or a.over <= 0:
        print(f"FAIL: large all-current ARCHITECTURE should be advisory, not gated: {a}")
        ok = False

    # Only the two above should appear; stores / reference docs / under-ref silent.
    unexpected = set(findings) - {"docs/ROADMAP.md", "ARCHITECTURE.md"}
    if unexpected:
        print(f"FAIL: unexpected findings {sorted(unexpected)}")
        ok = False

    # --check gates on the cold content (exit 1); no --check exits 0.
    if main(["--check", str(tmp), "--root", str(tmp)]) != 1:
        print("FAIL: --check did not gate on cold content")
        ok = False
    if main([str(tmp), "--root", str(tmp)]) != 0:
        print("FAIL: advisory-default run did not exit 0")
        ok = False

    # A large all-current roadmap (no [x]) must NOT gate — the reworked contract.
    ac = tmp / "allcurrent"
    (ac / "docs").mkdir(parents=True)
    (ac / "docs" / "ROADMAP.md").write_text("- [ ] open item\n" * (ref + 50))
    if main(["--check", str(ac), "--root", str(ac)]) != 0:
        print("FAIL: a large all-OPEN roadmap gated — live current-truth penalised")
        ok = False
    acf = {f.path.replace("\\", "/"): f for f in scan_paths([ac], ac)}
    if not acf.get("docs/ROADMAP.md") or acf["docs/ROADMAP.md"].gated:
        print("FAIL: all-open roadmap should be advisory (over-reference), not gated")
        ok = False

    # allow-marker exempts a would-be-gated file entirely.
    (docs / "ROADMAP.md").write_text(f"<!-- {ALLOW_MARKER}: living doc -->\n" + cold)
    if any(f.path.replace("\\", "/") == "docs/ROADMAP.md" for f in scan_paths([tmp], tmp)):
        print("FAIL: allow-marker did not exempt")
        ok = False

    # F1: a repo living UNDER a store-named ancestor must still be scanned.
    anc = tmp / "archive" / "child"
    (anc / "docs").mkdir(parents=True)
    (anc / "docs" / "ROADMAP.md").write_text(cold)
    if not any(f.path.replace("\\", "/") == "docs/ROADMAP.md" for f in scan_paths([anc], anc)):
        print("FAIL: F1 — repo under a store-named ancestor was skipped (fail-open)")
        ok = False

    # F2: a marker only *mentioned* in the body (below the header) must NOT exempt.
    body_mention = ("t\n" * 20) + f"discussion of {ALLOW_MARKER}\n" + cold
    (tmp / "F2").mkdir()
    (tmp / "F2" / "ROADMAP.md").write_text(body_mention)
    if not any(f.path.replace("\\", "/") == "ROADMAP.md"
               for f in scan_paths([tmp / "F2"], tmp / "F2")):
        print("FAIL: F2 — a body-only marker mention silently exempted the file")
        ok = False

    # cold_item_count: anchored to list bullets — a [x] in prose is not a work item.
    if cold_item_count("a line about [x] states in a sentence\n", "ROADMAP.md") != 0:
        print("FAIL: a [x] in prose was miscounted as a cold item")
        ok = False
    if cold_item_count("  - [x] indented done\n- [X] caps done\n", "ROADMAP.md") != 2:
        print("FAIL: indented / caps [x] items not counted")
        ok = False
    if cold_item_count("- [x] done\n", "README.md") != 0:
        print("FAIL: [x] outside a checkbox-worklog file should not count")
        ok = False
    if cold_item_count("+ [x] plus\n1. [x] ordered\n2) [x] ordered paren\n",
                       "ROADMAP.md") != 3:
        print("FAIL: +/ordered-bullet [x] items not counted")
        ok = False
    if cold_item_count("```\n- [x] a quoted example\n```\n", "ROADMAP.md") != 0:
        print("FAIL: a [x] inside a code fence was miscounted as a cold item")
        ok = False

    # Harvest integrity: a live marker in an archive store gates; a clean
    # archive (all [x], prose ⏳ mentions, fenced examples) stays silent.
    hi = tmp / "HI"
    (hi / "docs").mkdir(parents=True)
    (hi / "docs" / "ROADMAP-DONE.md").write_text(
        "- [x] done, harvested\n- [ ] buried open item\n")
    hif = {f.path.replace("\\", "/"): f for f in scan_paths([hi], hi)}
    h = hif.get("docs/ROADMAP-DONE.md")
    if not h or not h.gated or h.live_items != 1:
        print(f"FAIL: live [ ] in archive store not gated: {h}")
        ok = False
    if main(["--check", str(hi), "--root", str(hi)]) != 1:
        print("FAIL: --check did not gate on a live archive marker")
        ok = False
    (hi / "docs" / "ROADMAP-DONE.md").write_text(
        "- [x] done (dropped 2026-07-22: superseded)\n"
        "prose about the `[ ]` state\n"
        "```\n- [ ] quoted example\n```\n")
    if any(f.path.replace("\\", "/") == "docs/ROADMAP-DONE.md"
           for f in scan_paths([hi], hi)):
        print("FAIL: clean archive store flagged (prose/fence/[x] misfired)")
        ok = False

    # HI-F1: an archive store inside a growth-store dir (`sessions/`,
    # `_archive/`…) is integrity-checked wherever it lives — the dir skip
    # bounds metering, never integrity.
    (hi / "docs" / "sessions").mkdir(parents=True, exist_ok=True)
    (hi / "docs" / "ROADMAP-DONE.md").write_text("- [x] fine\n")
    (hi / "docs" / "sessions" / "SESSIONS-ARCHIVE.md").write_text("- [ ] buried\n")
    if main(["--check", str(hi), "--root", str(hi)]) != 1:
        print("FAIL: HI-F1 — live marker in a store under sessions/ not gated")
        ok = False
    (hi / "docs" / "sessions" / "SESSIONS-ARCHIVE.md").write_text("- [x] done\n")

    # live_item_count: archive-only, all three live markers, bullet-anchored.
    if live_item_count("- [ ] a\n- [~] b\n- ⏳ c\n", "ROADMAP-DONE.md") != 3:
        print("FAIL: live markers in archive store not all counted")
        ok = False
    if live_item_count("- [ ] open\n", "ROADMAP.md") != 0:
        print("FAIL: live marker outside an archive store counted")
        ok = False

    # count_lines: trailing newline doesn't inflate the count.
    if count_lines("a\nb\n") != 2 or count_lines("a\nb") != 2:
        print("FAIL: count_lines mishandles trailing newline")
        ok = False

    # reference_for: inline override beats the default; unmetered basename is None.
    if reference_for("sizescan:budget=42\n", "ROADMAP.md") != 42:
        print("FAIL: inline reference override not honoured")
        ok = False
    if reference_for("body\n", "PRINCIPLES.md") is not None:
        print("FAIL: non-current-truth basename should not be metered")
        ok = False

    # budget override moves the advisory only — a huge budget quiets the size
    # nudge but must NOT suppress a cold-content gate.
    (tmp / "B").mkdir()
    (tmp / "B" / "ROADMAP.md").write_text("sizescan:budget=100000\n" + cold)
    bf = {f.path.replace("\\", "/"): f for f in scan_paths([tmp / "B"], tmp / "B")}
    br = bf.get("ROADMAP.md")
    if not br or not br.gated or br.over != 0:
        print(f"FAIL: budget override should quiet advisory but keep the gate: {br}")
        ok = False

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

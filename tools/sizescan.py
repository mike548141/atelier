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
    hundred genuinely-open items — is **never** penalised or even mentioned.
    Fulsomeness on the hot path is not a defect when the bulk is current; there
    is nothing to relocate, and trimming a true signal to hit a number is the
    failure this tool was reworked to stop causing.

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
review, never measured**, and nothing in this tool points at it. This mirrors the
tool's standing one-sided honesty — a too-*thin* file (a hollow ARCHITECTURE.md
that lies by omission) is the worse defect, but thinness is judgement caught at
review under the stub-honestly rule (`00-APEX.md`), never a measured floor.

**There is no size check at all** (Mike's rulings, 2026-10-05 and 2026-10-16).
sizescan once also reported a hot file's length against a class reference point
(`ROADMAP.md` ~300 lines, `SESSIONS.md` ~250, and so on) as an advisory that
never failed a build, with a `sizescan:budget=N` marker to override the number.
Mike's ruling: "I specifically do not want artibuary limits like a fixed kb or
line count as limits because that is contrary to the purpose". Asked what the
advisory was for, and told that removing it loses the only pointer to prose-
shaped cold content, he answered "Remove it". The reference points, the budget
marker and the advisory output are gone, and no file is ever reported for its
length. A file's line count still appears beside a finding as context, never as
a trigger.

Scope — two directions, by design:

  * Cold content is looked for in **`ROADMAP.md`** only, wherever it lives (root
    or `docs/`): the one file whose convention is a checkbox worklog. The other
    current-truth names (`SESSIONS.md`, `ARCHITECTURE.md`, and the root `README.md`
    and `CLAUDE.md`) are no longer measured for anything. Their first 15 lines are
    still read, for one reason only: so a hatch left in them is named as inert
    (below), never silently accepted.

  * The **append-only stores are never scanned for cold content** —
    `ROADMAP-DONE.md`, `CHANGELOG.md`, `SPECS.md`, and everything under
    `sessions/`, `reviews/`, `decisions/`, and archive dirs. Those are the
    *destinations* the split moves detail into; they are meant to grow. Flagging
    them would punish the very fix the tool exists to encourage.

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
live** — the growth-store directory skip bounds where cold content is looked
for, never integrity (HI-F1) — though non-content directories (VCS internals,
vendored packages, virtualenvs, caches) are outside the scan entirely: nothing
there is this repo's record (HA1). One accepted edge (HI-F6): a live marker in
unfenced, indent-only example code is line-indistinguishable from a nested
child item and will fire — acceptable because the remedy below is
investigative (a false positive costs a look, never a wrong fix); fence
examples to avoid it. On a hit the remedy is **investigative, never
automatic**: the session that reds weighs the evidence (the item's children,
the session log, the code), then puts a recommendation to the principal — flip
to `[x]` with a dated disposition note, un-harvest back to the roadmap, or
reformat a parent that was only ever a heading. Never silently fix.

**Nothing silences the cold-content gate** (Mike's ruling, 2026-10-05, in his
words: "Never allow it as I don't want any of my repo's to run a flat running
log, they should all being using the new method where the main board (aka
roadmap) is a simple list of the work and its state, all the detail that
defines the work etc is in a standalone file"). No marker and no ignore glob
exempts a file that carries completed `[x]` items from the cold-content gate.
A repo that keeps a flat running log is exactly the defect the gate exists to
name. Where a hatch is present on a file that carries cold content, the report
says so plainly (`sizescan:allow header present and inert — it cannot exempt
cold content`) — a hatch is never silently ignored.

And the gate does not leave the session to infer what is done: every flagged
file lists each completed item it counted (line number and item text), so the
move to the archive is a lookup, not a judgement. The listing is bounded the way
every scanner's findings are (`MAX_MATERIALIZED_FINDINGS`, run-wide): past the
cap the items are counted, never silently dropped, and the report says how many.

Hatches (header-only — the first 15 lines, never the body, so a file that merely
*mentions* a marker in prose does not silently exempt itself). Since the size
advisory went, only two hatches can still exempt anything, and both only on an
archive store:

  * `sizescan:allow` — unscoped, or scoped `harvest-integrity` — exempts an
    archive store's harvest-integrity check. Keep the reason on the marker line
    so the exemption is self-documenting.
  * A glob in `.sizescanignore` skips an archive store wholesale.

**Everything else is present and inert, and is named, never silently accepted.**
A hatch that can no longer exempt anything — any `sizescan:allow` on a hot-path
file (it only ever quieted the retired size advisory), a scope that does not
cover the file's own kind (`size-advisory`, `cold-content`, or
`harvest-integrity` on a roadmap), a `.sizescanignore` glob matching a hot-path
file, a leftover `sizescan:budget=N` — is reported under "Inert hatches" with
its path, and counted on the `suppressed:` line. It changes no verdict and no
exit code; remove it. No new exemption exists: this only stops a stale marker
reading as if it still did something. `size-advisory` stays in
`FINDING_KINDS` as a retired name so a stale scope naming it is not mistaken for
the unscoped form, which WOULD exempt an archive store.

Report by default. A bare `sizescan` **reports and exits 0** — drop it in CI to
surface findings without ever breaking a build. `--check` is the opt-in gate,
and it fails on relocatable cold content (a `[x]` item on the hot path, whose fix
is lossless) and on live state in an archive store. Reviewed 2026-07-14 (cold,
PASS-WITH-FINDINGS), reworked to the cold-content model 2026-07-20 (Mike's
ruling, same day), and stripped of its size advisory 2026-10-16 (115/270 c).

Exit codes (fail-safe — anything but a clean run is non-zero):
  0  clean; or gated findings present but --check was not given. Inert hatches
     are named but never change the code.
  1  --check was given AND a hot-path file carries relocatable cold content
     ([x] items) or an archive store carries live state markers
  2  usage / config error (a scan that read nothing is NOT a pass)

Zero third-party dependencies; stdlib only, so a peer who adopts atelier can run
it with the system python3 and no install — and CI needs nothing but Python.
"""

from __future__ import annotations

import argparse
import codecs
import fnmatch
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import filewalk  # noqa: E402
import allowmarker  # noqa: E402
import report  # noqa: E402

# A file whose HEADER carries this marker, unscoped or scoped `harvest-integrity`,
# has an archive store's harvest-integrity check exempted: the only thing left
# for it to exempt, now the size advisory is gone. It never exempts cold content
# (Mike's 2026-10-05 ruling: no hatch silences that gate). Anywhere else it is
# inert, and the report says so. Keep the reason on the same line so the
# exemption is self-documenting.
ALLOW_MARKER = "sizescan:allow"

# GUARDS.md rule (c): a marker only counts with a colon and a non-empty reason,
# so prose that merely mentions the marker text exempts nothing. Tightened
# 2026-08-05 — a bare marker used to exempt on a substring match.
ALLOW_RX = allowmarker.marker_rx(ALLOW_MARKER, scope="one", group="kind")


def parse_allow(text: str) -> str | None:
    """The scope of the allow-marker, or None if there is no reasoned one.

    Header-scoped: sizescan exempts a whole FILE, deliberately blunter than
    the sibling scanners' per-line allows, because a file-level exemption is
    a deliberate declaration rather than a passing convenience (F2). A marker
    with no reason returns None — a mention, not an exemption."""
    return allowmarker.scope_of(ALLOW_RX, text, "kind")


# The kinds a header marker's scope can name (115/080; AM4). Two are live
# findings, the bracketed tags on the report lines: `cold-content` (which no
# marker exempts, 115/270 a) and `harvest-integrity` (which an unscoped marker
# or this scope exempts on an archive store). `size-advisory` is RETIRED
# (115/270 c): it is no longer a finding, but the name stays here so that a
# stale `sizescan:allow:size-advisory:` marker is still read as scoped to a
# kind it does not cover, never as the unscoped form, which would exempt an
# archive store's integrity check. Dropping it from this set would widen a
# live exemption without anyone writing one. `allowmarker.covers` reads it.
FINDING_KINDS = frozenset({"cold-content", "harvest-integrity",
                           "size-advisory"})

# The retired `sizescan:budget=N` header marker (115/270 c). Nothing reads its
# number any more; it is matched only so that one left in a file is named as
# inert in the report instead of being silently accepted. Same shape as it
# always had: `=400`, `: 400`, or a space.
_RETIRED_BUDGET_MARKER = re.compile(r"sizescan:budget\s*[=:]?\s*(\d+)")

# Markers are honoured ONLY in the file's header — the first MARKER_SCAN_LINES
# lines — never in the body. Matching anywhere let a file that merely *mentions*
# a marker in prose (a roadmap item about budgets, a doc of the hatch) silently
# exempt or re-reference itself (F2), a per-file blast radius blunter than the
# sibling scanners' per-line allows. A real exemption is a deliberate declaration
# at the top of the file, where a reader meets it first.
MARKER_SCAN_LINES = 15


# The current-truth files a session loads at start or leans on as "what's true /
# open now", by exact basename. Only `ROADMAP.md` is looked at for content
# (`COLD_CHECKBOX_FILES`, below). The rest are walked solely so that a hatch left
# in their header — a `sizescan:allow` or `sizescan:budget` from when length was
# reported — or a `.sizescanignore` glob matching them is named as inert rather
# than silently accepted (115/270 c). There is no number attached to any of them.
HOT_PATH_FILES = frozenset({"ROADMAP.md", "SESSIONS.md", "README.md",
                            "ARCHITECTURE.md", "CLAUDE.md"})

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
# fire on documentation that *shows* checkbox syntax. The immunity holds only
# while the delimiters BALANCE (HI-F2, sharpened by HA2): one stray delimiter
# shifts every pairing after it, so a file that ends inside a fence is
# recounted whole with fences ignored — as if no fence ever opened. False
# positives only, never a hidden marker; an unclosed fence is a defect to
# surface, never a hatch.
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
# `docs/decisions/README.md` is a reference index, read on demand, and reading
# it would dilute the signal. The other names are singular by convention (one
# ROADMAP, one SESSIONS index per repo) so they're read wherever they live —
# root or `docs/`.
ROOT_ONLY = {"README.md", "CLAUDE.md"}

# Two skip classes, deliberately separate (HA1 — one set conflated them and
# the archive-store bypass leaked into vendored code):
#
# Non-content dirs — VCS internals, vendored packages, virtualenvs, caches,
# IDE state. Nothing in them is this repo's record, so NOTHING in them is
# ever scanned: a vendored package's `ROADMAP-DONE.md` is not a store where
# this repo's history lives, and integrity-checking it reds the build on a
# file the repo owner doesn't own.
NON_CONTENT_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv",
                         "venv", ".mypy_cache", ".ruff_cache",
                         ".pytest_cache", ".idea", ".vscode"}

# Growth-store dirs — where completed / append-only detail is *meant* to
# accumulate. `ROADMAP-DONE.md`, `CHANGELOG.md`, `SPECS.md` fall out naturally
# (their basenames aren't in HOT_PATH_FILES); these path components catch a
# hot-path basename that lives inside a growth store (an `ARCHITECTURE.md`
# snapshotted under `_archive/`, a `README.md` inside `reviews/`, a
# `ROADMAP.md` kept as a frozen copy). This skip bounds where cold content is
# looked for only — an archive store inside one is still integrity-checked
# (HI-F1): the skip keeps stores from being read as hot files, never unread.
STORE_DIR_NAMES = {"sessions", "reviews", "decisions",
                   "_archive", "archive", "intake"}


# A completed item's title is held to this many characters (an ellipsis counts
# as one), so the listing fits the house 85-column limit after its indent and
# `line N:` lead, and so a pathological multi-KB bullet costs a fixed amount.
_TITLE_CHARS = 60

# A completed item's bullet and checkbox, stripped to leave just its text.
_COLD_LEAD = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\[[xX]\]\s*")

# The run-wide cap on completed items held for the listing, the same bound
# every other scanner puts on the findings it builds (`leakscan`,
# `linkscan`, … `MAX_MATERIALIZED_FINDINGS`, derived there): each held item
# costs on the order of 100 B here, so memory stays fixed however many `[x]`
# lines the tree holds. Items past the cap are COUNTED (the file's
# `cold_items` is always the true count), never dropped silently, and the
# report prints how many were not listed (`report.over_cap_line`).
MAX_MATERIALIZED_FINDINGS = 50_000


@dataclass
class ColdItem:
    line: int            # 1-based physical line number of the completed item
    title: str           # its text, bullet and box stripped, capped at _TITLE_CHARS


def _item_title(text: str) -> str:
    """The text of a completed item: bullet and box stripped, whitespace
    collapsed, capped at `_TITLE_CHARS` with an ellipsis."""
    title = " ".join(_COLD_LEAD.sub("", text, count=1).split())
    if not title:
        return "(no text)"
    if len(title) > _TITLE_CHARS:
        return title[:_TITLE_CHARS - 1].rstrip() + "…"
    return title


@dataclass
class Finding:
    path: str            # the flagged file, repo-relative
    lines: int           # its line count, shown beside the finding as context only
    cold_items: int      # relocatable `[x]` items on the hot path (0 = none)
    store: str           # where its cold content belongs / what to do about it
    gated: bool          # True = fails --check (cold content or live markers)
    live_items: int = 0  # live state markers ([ ]/[~]/⏳) in an archive store
    # The completed items counted in `cold_items`, in file order (115/270 b),
    # up to the run-wide cap; `cold_items - len(cold_listed)` were counted but
    # not listed.
    cold_listed: list = field(default_factory=list)
    # The hatches present on a file that carries cold content. None of them can
    # exempt it (115/270 a), and since the size advisory went (115/270 c) none
    # can exempt anything else on a hot-path file either. Named in the report so
    # a marker or glob is never silently ignored.
    cold_hatches: list = field(default_factory=list)


@dataclass
class InertHatch:
    """A hatch present where it can no longer exempt anything (115/270 c)."""
    path: str            # the file it sits on (or matches), repo-relative
    hatch: str           # what it is, e.g. `sizescan:allow header (unscoped)`


# Where a hot file's cold content belongs, so the report points at the fix, not
# just the symptom.
_COLD_STORE_HINT = ("harvest completed [x] items to ROADMAP-DONE.md "
                    "(keep only what's open)")


def _count_list_items(text: str, pattern: re.Pattern) -> int:
    """Count pattern-matching list items outside fenced code blocks. Fence
    pairing is only trustworthy when the delimiters balance: one stray
    delimiter shifts every pairing after it, so a tail-only fix still hid
    markers between the stray delimiter and the next one (HI-F2, sharpened by
    HA2). If the file ends inside a fence, the whole file is therefore
    recounted with fences ignored — genuinely "as if no fence ever opened".
    Fail-safe by construction: a malformed file can only false-positive
    (the remedy is investigative, so that costs a look), never hide a
    marker."""
    lines = text.splitlines()
    count = 0
    in_fence = False
    for line in lines:
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and pattern.match(line):
            count += 1
    if in_fence:   # delimiters unbalanced — pairing untrustworthy; recount all
        return sum(1 for line in lines
                   if not _FENCE.match(line) and pattern.match(line))
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


IgnoreFileError = allowmarker.IgnoreFileError


def load_ignore_globs(root: Path) -> list[str]:
    """Globs from `.sizescanignore`, each of which MUST carry a stated reason.
    Single-sourced (115/080 part 2) in `tools/allowmarker.py`; this
    scanner supplies only its own ignore-file name."""
    return allowmarker.load_ignore_globs(root, ".sizescanignore")


def _ignored(rel: str, globs: list[str]) -> bool:
    return allowmarker.ignored(rel, globs)


def _rel(p: Path, root: Path) -> str:
    try:
        return str(p.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(p)


def _dir_parts(p: Path, walk_base: Path) -> set[str]:
    """The intermediate directory names between the scan base and p. Matched
    against the path **relative to the scan base**, never the absolute path.
    Matching absolute parts was a fail-open bug (F1): a repo that merely
    *lives under* an ancestor named `archive`/`sessions`/`reviews`/… — the
    store names are ordinary English words — had every file skipped, so the
    scan read nothing and reported "clean", the exact contract violation the
    tool's own exit codes forbid ("a scan that read nothing is NOT a pass")."""
    try:
        rel_parts = p.relative_to(walk_base).parts
    except ValueError:
        rel_parts = (p.name,)
    return set(rel_parts[:-1])   # intermediate dirs only


# 020/380 applied 020/370's bounded-memory fix to this guard: the old
# `iter_candidates` walked with `base.rglob("*")` funnelled through a list
# comprehension — a generator that LOOKS lazy, but wrapping it in `[...]`
# forces Python to enumerate the ENTIRE subtree and hold every `Path` before
# a single file is even considered, the same shape secretscan's `iter_files`
# carried before its own fix. `_walk_files` below WAS that same fix
# duplicated rather than imported; it is now single-sourced in
# `tools/filewalk.py` (115/080 part 1) — see that module's docstring.
def _walk_files(base: Path):
    """Every regular file under `base`, streamed one at a time. Single-sourced
    (115/080 part 1) in `tools/filewalk.py` — see that module's docstring
    for the mechanism and the 020/160 (E9) linked-worktree skip (measured in
    `faves` 2026-08-15: double-reported files from a nested checkout).
    `NON_CONTENT_DIR_NAMES` is this scanner's own per-guard parameter, passed
    in rather than shared. Growth-store directories (`sessions/`,
    `_archive/`, …) are deliberately NOT in that set — an archive store can
    legitimately live inside one and must still be integrity-checked
    (HI-F1) — that filter stays a per-file check in `iter_candidates`, same
    as before this fix."""
    return filewalk.walk_files(base, NON_CONTENT_DIR_NAMES)


# Streaming-read tuning (020/380, reusing 020/370's secretscan shape). Every
# constant is a FIXED size, independent of the file or tree being scanned.
# sizescan's own regexes (`_COLD_ITEM`, `_LIVE_ITEM`, `_FENCE`, the header
# markers) are all anchored at the START of a line (`^\s*...`), so — unlike
# secretscan's arbitrary-position matching — a physical line only ever needs
# to be held up to a short prefix to decide every check this scanner makes.
# `_MAX_LINE_BYTES` is set two-plus orders of magnitude past any realistic
# Markdown list-item line (a checkbox bullet with its text rarely exceeds a
# few hundred characters) so no real content is ever truncated; it exists
# purely to bound the pathological case (one absurd multi-MB "line") to a
# fixed, cheap constant instead of letting it scale with the file.
_READ_CHUNK_BYTES = 1 * 1024 * 1024
_MAX_LINE_BYTES = 8 * 1024


def _iter_physical_lines(path: Path):
    """Yield `(lineno, text, truncated)` for every physical line in `path`,
    reading and decoding it in fixed-size chunks so peak memory for ONE file
    is bounded by `_MAX_LINE_BYTES` (plus one read chunk in flight) —
    independent of the file's total size or its longest line (020/380). A
    physical line longer than `_MAX_LINE_BYTES` is truncated to that many
    characters for `text`; `truncated=True` says so — the excess is still
    READ (so running time stays linear in bytes read) but never held, and
    the caller counts the truncation rather than scanning silently short."""
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


def _scan_file_metrics(path: Path, basename: str, item_slots: int = 0
                       ) -> tuple[str, int, int, int, list[ColdItem]]:
    """Stream `path` once (twice only in the rare unbalanced-fence case) to
    compute `(header, line_count, cold_items, live_items, items)` without ever
    holding the whole file, or a per-line record of it, in memory (020/380).
    `items` is the first `item_slots` completed items (line number and capped
    title only, 115/270 b), so what is held is bounded by the caller's slots,
    never by the file; the count in `cold_items` is always the true one.

    Replaces the old `p.read_text()` followed by a line counter and
    `cold_item_count`/`live_item_count`, each of which re-derived
    `text.splitlines()` over the WHOLE file — the same
    double-materialization shape secretscan's old `scan_paths` carried. The fence-balance fallback (HI-F2/HA2: if the file
    ends inside an open fence, recount as if none ever opened) is done with a
    SECOND STREAMING PASS rather than a buffered per-line flag list — the
    flag list would itself grow with the file's LINE COUNT, which is exactly
    the not-allowed-to-scale-with-input-size shape this fix exists to remove.
    Two bounded passes is still linear in bytes read, just a larger constant
    factor, and the common (balanced) case never pays it at all."""
    want_cold = basename in COLD_CHECKBOX_FILES
    want_live = is_archive_store(basename)

    def one_pass(ignore_fences: bool):
        header_lines: list[str] = []
        n = 0
        in_fence = False
        cold = live = 0
        items: list[ColdItem] = []
        for lineno, text, _truncated in _iter_physical_lines(path):
            n = lineno
            if lineno <= MARKER_SCAN_LINES:
                header_lines.append(text)
            stripped = text.lstrip()
            if _FENCE.match(stripped):
                if not ignore_fences:
                    in_fence = not in_fence
                continue
            if ignore_fences or not in_fence:
                if want_cold and _COLD_ITEM.match(text):
                    cold += 1
                    if len(items) < item_slots:
                        items.append(ColdItem(lineno, _item_title(text)))
                if want_live and _LIVE_ITEM.match(text):
                    live += 1
        return "\n".join(header_lines), n, cold, live, items, in_fence

    header, n, cold, live, items, unbalanced = one_pass(ignore_fences=False)
    if unbalanced:
        header, n, cold, live, items, _ = one_pass(ignore_fences=True)
    return header, n, cold, live, items


def _read_header(path: Path) -> str:
    """The first `MARKER_SCAN_LINES` lines of `path` and nothing more, for a
    hot-path file that is read only to find a stale hatch (115/270 c). Streamed
    and stopped early, so a huge file costs one chunk, not a full pass."""
    header_lines: list[str] = []
    for lineno, text, _truncated in _iter_physical_lines(path):
        header_lines.append(text)
        if lineno >= MARKER_SCAN_LINES:
            break
    return "\n".join(header_lines)


def iter_candidates(paths: list[Path], root: Path, globs: list[str],
                    skipped: list[int] | None = None,
                    evaluate_ignored: bool = False):
    """Yield candidate files under the given paths, skipping growth-store dirs
    and ignored globs. A file is a candidate iff its basename is a hot-path
    file (`HOT_PATH_FILES`) OR a named archive store (integrity-checked).
    Results are de-duplicated by resolved path so overlapping args
    (`sizescan . docs`) don't double-report the same file (F4).

    A `.sizescanignore` match is skipped wholesale and counted in `skipped`,
    EXCEPT with `evaluate_ignored` (what `scan_paths` passes): a hot-path
    file is then still yielded, because no glob exempts it from the
    cold-content gate (115/270 a) and a glob over it exempts nothing at all
    now (115/270 c); the caller works out which were ignored and names the
    glob as inert. An ignored archive store is skipped either way — that is
    the one place a glob still has an effect."""
    seen: set[Path] = set()
    for base in paths:
        base = base.resolve()
        walk_base = base if base.is_dir() else base.parent
        candidates = [base] if base.is_file() else _walk_files(base)
        for p in candidates:
            rp = p.resolve()
            if rp in seen or (p.name not in HOT_PATH_FILES
                              and not is_archive_store(p.name)):
                continue
            # Non-content dirs are never scanned at all (HA1); growth-store
            # dirs bound where cold content is looked for only — an archive
            # store inside one is still integrity-checked (HI-F1): a
            # `*-DONE.md` under `sessions/` or `_archive/` silently escaping
            # the gate was the fail-open class ("a scan that read nothing is
            # NOT a pass") reintroduced.
            parts = _dir_parts(p, walk_base)
            if parts & NON_CONTENT_DIR_NAMES:
                continue
            if parts & STORE_DIR_NAMES and not is_archive_store(p.name):
                continue
            if p.name in ROOT_ONLY and rp.parent != root.resolve():
                continue
            if _ignored(_rel(p, root), globs):
                if not evaluate_ignored or is_archive_store(p.name):
                    if skipped is not None:
                        skipped.append(1)
                    continue
            seen.add(rp)
            yield p


def _inert_hatches(basename: str, header: str, scope: str | None,
                   ignored_by_glob: bool) -> list[str]:
    """The hatches present on this file that can exempt nothing (115/270 c),
    named for the report, so a stale marker never reads as if it still did
    something. Three things can still exempt, and only on an archive store: an
    allow-marker that covers `harvest-integrity` (unscoped, `harvest-integrity`,
    or a scope naming no kind) and a `.sizescanignore` glob (which skips the
    store before it is read, so it is never seen here). Everything else is
    inert: any marker on a hot-path file, a scope on an archive store that is
    not `harvest-integrity` (`cold-content`, the retired `size-advisory`), a glob
    over a hot-path file, and a leftover `sizescan:budget=N`. This invents no
    exemption: it only reports one that has stopped working."""
    out = []
    if scope is not None and not (
            is_archive_store(basename)
            and allowmarker.covers(scope, "harvest-integrity", FINDING_KINDS)):
        out.append(f"{ALLOW_MARKER}:{scope} header" if scope
                   else f"{ALLOW_MARKER} header (unscoped)")
    if ignored_by_glob and not is_archive_store(basename):
        out.append(".sizescanignore glob")
    if _RETIRED_BUDGET_MARKER.search(header):
        out.append("sizescan:budget header")
    return out


def scan_paths(paths: list[Path], root: Path,
               counts: dict[str, int] | None = None,
               inert: list[InertHatch] | None = None) -> list[Finding]:
    globs = load_ignore_globs(root)
    findings: list[Finding] = []
    files_allowed = 0
    n_inert = 0
    skipped: list[int] = []
    slots = MAX_MATERIALIZED_FINDINGS
    cold_over_cap = 0
    for p in iter_candidates(paths, root, globs, skipped, evaluate_ignored=True):
        # 020/380 — streamed rather than `p.read_text()` + whole-file regex
        # passes: peak memory for this file is now bounded by `_MAX_LINE_BYTES`
        # regardless of the file's own size. `header` is already the
        # first-`MARKER_SCAN_LINES`-lines slice, so `parse_allow` needs no
        # change. A hot-path file with no cold-content convention is read for
        # its header alone: it has nothing to count, only hatches to name.
        looked_at = p.name in COLD_CHECKBOX_FILES or is_archive_store(p.name)
        try:
            if looked_at:
                header, n, cold, live, items = _scan_file_metrics(p, p.name, slots)
            else:
                header, n, cold, live, items = _read_header(p), 0, 0, 0, []
        except OSError:
            continue
        slots -= len(items)
        cold_over_cap += cold - len(items)
        scope = parse_allow(header)
        rel = _rel(p, root)
        # A hatch is counted as a suppression only where it still exempts
        # something: an allow-marker on an archive store that covers its
        # harvest-integrity check. Every other hatch is inert (115/270 c).
        exempt = (scope is not None and is_archive_store(p.name)
                  and allowmarker.covers(scope, "harvest-integrity",
                                         FINDING_KINDS))
        if exempt:
            files_allowed += 1
        hatches = _inert_hatches(p.name, header, scope, _ignored(rel, globs))
        if is_archive_store(p.name):
            # Integrity only — an archive store holds no cold content to look
            # for. A live marker gates under --check; a clean archive stays
            # silent.
            if live and not exempt:
                findings.append(Finding(
                    rel, n, 0,
                    "investigate, then recommend to the principal: flip to [x] "
                    "with a dated disposition note, or un-harvest to the "
                    "roadmap — never silently fix",
                    True, live))
        elif cold:
            # Relocatable cold content gates. No marker or glob takes that
            # away (115/270 a) — `cold` is left as counted, and the hatches
            # that cannot exempt it are named on the finding itself.
            findings.append(Finding(
                rel, n, cold, _COLD_STORE_HINT, True,
                cold_listed=items, cold_hatches=hatches))
        n_inert += len(hatches)
        if inert is not None:
            inert.extend(InertHatch(rel, h) for h in hatches)
    # Rule (b): report the suppression counts through the caller's optional
    # `counts` dict, so a clean report cannot look identical to one where every
    # file was exempted. An out-param rather than a changed return type: the
    # selftest and tests call scan_paths in a dozen places and a tuple return
    # would churn them all for no gain.
    if counts is not None:
        counts["files_allowed"] = files_allowed
        counts["files_by_glob"] = len(skipped)
        counts["cold_over_cap"] = cold_over_cap
        counts["inert_hatches"] = n_inert
    return findings


def _kinds(f: Finding) -> list[str]:
    """The kinds one file's finding carries, in report order."""
    return ([k for k, n in (("cold-content", f.cold_items),
                            ("harvest-integrity", f.live_items)) if n])


def _suppression_line(files_allowed: int, files_by_glob: int,
                      cold_over_cap: int = 0, inert_hatches: int = 0) -> str:
    """Rule (b): known zeros printed, so two runs can be compared. The cap part
    is the house one (`report.cap_part`), printed as a zero when nothing was
    held back. The inert count is a tally of hatches that exempt nothing, so it
    is not a suppression: it sits here so a stale hatch can never be absent from
    the line a reader compares across runs (115/270 c)."""
    return report.suppressed_line(
        [f"{files_allowed} file(s) by sizescan:allow header",
         f"{files_by_glob} file(s) by .sizescanignore",
         f"{inert_hatches} inert hatch(es) (exempt nothing)",
         report.cap_part(cold_over_cap, MAX_MATERIALIZED_FINDINGS)])


def _inert_block(orphans: list[InertHatch]) -> list[str]:
    """The report's section for inert hatches that are not already named under
    a cold-content finding. Empty when there are none."""
    if not orphans:
        return []
    out = ["\n  Inert hatches (change no verdict): present, but each exempts "
           "nothing, because sizescan no longer has a size advisory for it to "
           "quiet. Remove them, so a stale marker does not read as if it still "
           "did something."]
    out.extend(f"    {h.path}: {h.hatch}" for h in orphans)
    return out


def render_human(findings: list[Finding], files_allowed: int = 0,
                 files_by_glob: int = 0, cold_over_cap: int = 0,
                 inert: list[InertHatch] | None = None) -> str:
    # `inert` is every inert hatch the scan found; the ones on a cold-content
    # finding are printed under that finding, the rest in their own section.
    # Both count on the suppressed line.
    on_finding = {f.path for f in findings if f.cold_items}
    orphans = [h for h in (inert or []) if h.path not in on_finding]
    n_inert = len(orphans) + sum(len(f.cold_hatches) for f in findings)
    tally = _suppression_line(files_allowed, files_by_glob, cold_over_cap, n_inert)
    if not findings:
        return "\n".join([report.clean_head(
            "sizescan", "no relocatable cold content on the hot path; "
                        "archive stores hold no live markers.")]
                         + _inert_block(orphans) + [tally])
    n_cold = sum(1 for f in findings if f.cold_items)
    n_live = sum(1 for f in findings if f.live_items)
    head = (f"⚠ sizescan: {len(findings)} file(s) flagged "
            f"({n_cold} cold-content · {n_live} harvest-integrity).\n")
    lines = [head]
    # Cold content first, then archive integrity; within each, worst first.
    for f in sorted(findings, key=lambda x: (not x.gated, -x.cold_items,
                                             -x.live_items)):
        lines.append(f"  {f.path}  {f.lines} lines")
        if f.cold_items:
            lines.append(report.with_id(
                f"      → {f.cold_items} completed [x] item(s) to harvest "
                f"[cold-content, gated]", "sizescan", "cold-content"))
            if f.store:
                lines.append(f"        {f.store}")
            if f.cold_listed or f.cold_items:
                lines.append("        completed items counted (line: item):")
            for it in f.cold_listed:
                lines.append(f"          line {it.line}: {it.title}")
            unlisted = f.cold_items - len(f.cold_listed)
            if unlisted > 0:
                lines.append(report.over_cap_line(
                    unlisted, MAX_MATERIALIZED_FINDINGS,
                    noun="completed item(s)", indent="          "))
            for hatch in f.cold_hatches:
                lines.append(f"        note: {hatch} present and inert — it "
                             f"cannot exempt cold content.")
        if f.live_items:
            lines.append(report.with_id(
                f"      → {f.live_items} live state marker(s) "
                f"([ ]/[~]/⏳ list items) in an archive store "
                f"[harvest-integrity, gated]", "sizescan", "harvest-integrity"))
            if f.store:
                lines.append(f"        {f.store}")
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
                     "Never reword to fit. No marker and no glob in "
                     "`.sizescanignore` silences this gate: harvest the "
                     "completed [x] items listed above.")
    lines.extend(_inert_block(orphans))
    lines.append("")
    lines.append(tally)
    return "\n".join(lines)


def _main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="sizescan",
        description="Flag a roadmap that carries relocatable cold content (a "
                    "completed [x] item), and an archive store that carries live "
                    "state markers. Never reports a file for its length.")
    ap.add_argument("paths", nargs="*",
                    help="files/dirs to scan (default: whole repo)")
    ap.add_argument("--root", default=".",
                    help="repo root for .sizescanignore and relative paths")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if a hot-path file carries relocatable cold "
                         "content (a completed [x] item — lossless remedy) or "
                         "an archive store carries live state markers "
                         "([ ]/[~]/⏳ — harvest integrity) "
                         "(default: report only, exit 0)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="run built-in checks and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    rc = report.refuse_missing_root("sizescan", root, args.root)
    if rc is not None:
        return rc
    # A RELATIVE target resolves against --root, never the caller's cwd:
    # mixing the two reads one repo's file under another repo's rules,
    # and neither half of the output says so (roadmap 010/110).
    targets = report.resolve_targets(root, args.paths or [str(root)])
    rc = report.refuse_missing_paths("sizescan", targets)
    if rc is not None:
        return rc
    try:
        counts: dict[str, int] = {"files_allowed": 0, "files_by_glob": 0,
                                  "cold_over_cap": 0, "inert_hatches": 0}
        inert: list[InertHatch] = []
        findings = scan_paths(targets, root, counts, inert)
    except OSError as e:
        return report.cannot_read("sizescan", e)

    if args.json:
        print(json.dumps({
            "clean": not findings,
            # Completed items counted but not listed (past the run-wide cap):
            # known zero printed, so two runs compare (rule b).
            "cold_items_over_cap": counts["cold_over_cap"],
            # Every hatch present where it exempts nothing (115/270 c): a known
            # zero is printed too. Those on a cold-content file are also on its
            # finding's `cold_hatches`.
            "inert_hatches": [asdict(h) for h in inert],
            # One finding per FILE, carrying up to two kinds, so `ids` (a
            # list, one per kind present) rather than the one `id` the
            # per-line scanners give.
            "findings": [dict(asdict(f), ids=[report.finding_id("sizescan", k)
                                              for k in _kinds(f)])
                         for f in findings],
        }, indent=2))
    else:
        print(render_human(findings, counts["files_allowed"],
                           counts["files_by_glob"], counts["cold_over_cap"],
                           inert))

    # Report-only by default: exit 0. --check gives teeth to what has a
    # pure-win remedy — relocatable cold content (a [x] item on the hot path) and
    # live state in an archive store. Nothing about length is ever reported, and
    # an inert hatch is named but never changes the verdict.
    return report.exit_code(args.check and any(f.gated for f in findings))


def _selftest() -> int:
    """Minimal smoke test so `sizescan --selftest` proves the engine on any box,
    even where the unittest file isn't shipped. Builds a tiny tree and asserts the
    core behaviours: cold content ([x] items) flags and gates; a large all-current
    file is never mentioned (there is no size check); growth stores and reference
    docs are ignored; the hatches behave, and a hatch that exempts nothing is
    named as inert."""
    import tempfile
    import shutil

    tmp = Path(tempfile.mkdtemp(prefix="sizescan-self-"))
    docs = tmp / "docs"
    docs.mkdir()
    (docs / "sessions").mkdir()

    big = "x\n" * 5000                       # long, but no [x] items
    cold = "- [ ] open\n- [x] done one\n- [x] done two\n"   # small, but 2 cold items

    (docs / "ROADMAP.md").write_text(cold)                       # cold content → GATED
    (docs / "ROADMAP-DONE.md").write_text(big)                   # growth store → ignore
    (docs / "SPECS.md").write_text(big)                          # on-demand → ignore
    (tmp / "CHANGELOG.md").write_text(big)                       # append-only → ignore
    (tmp / "PRINCIPLES.md").write_text(big)                      # reference doc → ignore
    (docs / "sessions" / "SESSIONS.md").write_text(big)          # inside a store → ignore
    (tmp / "README.md").write_text(big)                          # long root README → silent
    (tmp / "tools").mkdir()
    (tmp / "tools" / "README.md").write_text(big)                # nested README → ignore
    (tmp / "ARCHITECTURE.md").write_text(big)                    # long, no [x] → silent

    findings = {f.path.replace("\\", "/"): f for f in scan_paths([tmp], tmp)}
    ok = True

    # ROADMAP with [x] items: flagged, gated, count correct.
    r = findings.get("docs/ROADMAP.md")
    if not r or not r.gated or r.cold_items != 2:
        print(f"FAIL: cold-content ROADMAP not gated with 2 items: {r}")
        ok = False

    # Only that one appears: no file is ever reported for its length.
    unexpected = set(findings) - {"docs/ROADMAP.md"}
    if unexpected:
        print(f"FAIL: unexpected findings {sorted(unexpected)}")
        ok = False

    # --check gates on the cold content (exit 1); no --check exits 0.
    if main(["--check", str(tmp), "--root", str(tmp)]) != 1:
        print("FAIL: --check did not gate on cold content")
        ok = False
    if main([str(tmp), "--root", str(tmp)]) != 0:
        print("FAIL: report-only run did not exit 0")
        ok = False

    # A large all-current roadmap (no [x]) is clean: no gate, no finding.
    ac = tmp / "allcurrent"
    (ac / "docs").mkdir(parents=True)
    (ac / "docs" / "ROADMAP.md").write_text("- [ ] open item\n" * 350)
    if main(["--check", str(ac), "--root", str(ac)]) != 0:
        print("FAIL: a large all-OPEN roadmap gated — live current-truth penalised")
        ok = False
    if scan_paths([ac], ac):
        print("FAIL: an all-open roadmap was reported for its length")
        ok = False

    # No hatch exempts cold content (115/270 a): an unscoped allow header, a
    # `cold-content` scope and a `.sizescanignore` glob each still gate the
    # file and are named in the report as inert.
    for label, header, named in (
            ("unscoped", f"<!-- {ALLOW_MARKER}: living doc -->\n",
             f"{ALLOW_MARKER} header (unscoped)"),
            ("cold-content scope",
             f"<!-- {ALLOW_MARKER}:cold-content: harvested -->\n",
             f"{ALLOW_MARKER}:cold-content header")):
        (docs / "ROADMAP.md").write_text(header + cold)
        hf = {f.path.replace("\\", "/"): f for f in scan_paths([tmp], tmp)}
        h = hf.get("docs/ROADMAP.md")
        if not h or not h.gated or h.cold_items != 2:
            print(f"FAIL: {label} allow-marker exempted cold content: {h}")
            ok = False
        elif h.cold_hatches != [named]:
            print(f"FAIL: {label} allow-marker should be named in the report: {h}")
            ok = False
    (docs / "ROADMAP.md").write_text(cold)
    (tmp / ".sizescanignore").write_text("# selftest fixture\ndocs/ROADMAP.md\n")
    hf = {f.path.replace("\\", "/"): f for f in scan_paths([tmp], tmp)}
    h = hf.get("docs/ROADMAP.md")
    if (not h or not h.gated
            or h.cold_hatches != [".sizescanignore glob"]):
        print(f"FAIL: .sizescanignore glob exempted cold content: {h}")
        ok = False
    (tmp / ".sizescanignore").unlink()

    # An inert hatch where there is no cold content is named, never silently
    # accepted, and changes no exit code (115/270 c): a stale allow and budget
    # marker on a session index, and a glob over a clean roadmap.
    ih = tmp / "inert"
    (ih / "docs").mkdir(parents=True)
    (ih / "docs" / "SESSIONS.md").write_text(
        f"<!-- {ALLOW_MARKER}: long index -->\n<!-- sizescan:budget=400 -->\n"
        + big)
    (ih / "docs" / "ROADMAP.md").write_text("- [ ] open\n")
    (ih / ".sizescanignore").write_text("# selftest fixture\ndocs/ROADMAP.md\n")
    named: list[InertHatch] = []
    ic: dict[str, int] = {}
    if scan_paths([ih], ih, ic, named) != [] or sorted(
            (x.path.replace("\\", "/"), x.hatch) for x in named) != [
            ("docs/ROADMAP.md", ".sizescanignore glob"),
            ("docs/SESSIONS.md", f"{ALLOW_MARKER} header (unscoped)"),
            ("docs/SESSIONS.md", "sizescan:budget header")] or (
            ic["inert_hatches"] != 3):
        print(f"FAIL: inert hatches not named: {named} {ic}")
        ok = False
    if main(["--check", str(ih), "--root", str(ih)]) != 0:
        print("FAIL: an inert hatch changed the exit code")
        ok = False

    # The finding names each completed item: line number and text.
    (docs / "ROADMAP.md").write_text(cold)
    h = {f.path.replace("\\", "/"): f for f in scan_paths([tmp], tmp)}.get(
        "docs/ROADMAP.md")
    if not h or [(i.line, i.title) for i in h.cold_listed] != [
            (2, "done one"), (3, "done two")]:
        print(f"FAIL: the completed items were not named by line and text: {h}")
        ok = False
    elif "line 3: done two" not in render_human([h]):
        print("FAIL: the report did not list the completed items")
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

    # The one thing a marker still exempts: an archive store's integrity check
    # (unscoped, or `harvest-integrity`). A scope that does not cover it
    # (`cold-content`, the retired `size-advisory`) exempts nothing and is named.
    for scope, exempt in (("", True), (":harvest-integrity", True),
                          (":cold-content", False), (":size-advisory", False)):
        (hi / "docs" / "ROADMAP-DONE.md").write_text(
            f"<!-- {ALLOW_MARKER}{scope}: parked on purpose -->\n- [ ] parked\n")
        named = []
        got = {f.path.replace("\\", "/") for f in scan_paths([hi], hi, None, named)}
        if (("docs/ROADMAP-DONE.md" in got) == exempt
                or bool(named) == exempt):
            print(f"FAIL: allow marker scope {scope!r} on an archive store: "
                  f"found {sorted(got)}, inert {named}")
            ok = False

    # HI-F1: an archive store inside a growth-store dir (`sessions/`,
    # `_archive/`…) is integrity-checked wherever it lives — the dir skip
    # bounds where cold content is looked for, never integrity.
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

    print("selftest OK" if ok else "selftest FAILED")
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    """Exit 2 on an ignore file that grants an exemption with no reason.

    A broken scan is not a pass (the house exit-code contract), and an
    unexplained exemption makes the scan's own scope untrustworthy."""
    return report.guarded_main("sizescan", _main, argv, (IgnoreFileError,))

if __name__ == "__main__":
    sys.exit(main())

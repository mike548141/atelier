#!/usr/bin/env python3
"""pointerscan — a queued-review pointer says only what it may, and only what is
still true, and a NEW one is queued on grounds.

FOUR FAILURES, ONE PARSE
------------------------
`ROADMAP.md`'s own preamble states the pointer's ceiling: **refs only** — name
the delta and the intent record, carry no evaluative account, because the
account belongs in the session record where the reviewer's deferral discipline
governs when it is read. `REVIEW.md` rule 4 states the same ceiling at the point
a pointer is written.

Four things go wrong with a pointer, and one parse answers all of them:

  1. GRAMMAR — *what may it say, and what must it name by path and bound*. A pointer that seeds the reviewer's first
     question steers the pass it is queuing. Recorded three times; the third
     instance was written hours after its author read the finding recording the
     first two, in the same file. Three instances of a trivial failure is a
     defect in the system producing it, which is the argument for a forcing
     function rather than a fourth restatement.
  2. CYCLE STATE — *is it still true*. An item asserting a review is owed while
     the same item carries the verdict of the review that ran is a mechanical
     contradiction. Five such residues came out of one commit; a sixth was
     still standing when this tool was built and is what it found on day one.
  3. QUEUE STATE — *does the state line count true* (130/020, added
     2026-10-05). The board legend makes the queued glyph mean one thing: a
     review is queued and its pass has not returned a verdict. Two ways it
     miscounts, one detector for each: a pointer whose own pass has RUN still
     wearing the glyph (27 items on 2026-10-03, a session reported "20 queued"
     when none were), and a queued review written as an ordinary open item
     (a re-review on 2026-10-05), which a glyph count misses. Measured over
     every item version the split board has held (768): the first fires on
     exactly the 27 items one commit later proved against their verdicts — on
     no other item — including earlier versions of four of them that were
     either already stale or carried a further pass queued inside the landed
     item, a shape the legend now rules out; the second fires on the one
     re-review and nothing else.
  4. DELTA BOUND — *does the pointer name its commits by something a commit
     cannot omit* (PK21, the cold pass on `160/1810`, 2026-11-25). A pointer
     that said "the commits citing `210/600`" missed three of the seven
     commits on its own path list, because a commit that touches the paths
     need not cite the item. A pointer names its delta by path and bound. A
     bound that is only a citation ("commits citing", "commits that cite",
     "commits naming" and the rest of that family) is flagged, under the
     `grammar` detector (the grammar of what a pointer names), unless a commit
     range (`a1b2c3d..e4f5a6b`) is written out, or a list of two or more
     commit hashes in the sentence that names the delta. One start hash is not
     enough: the citation still selects, and the start only trims; and hashes
     that bind nothing (a pinned verdict, session ids) do not count (DP19).
     Advisory like the rest; `grammar` is reused rather than a fourth kind
     added, so the kinds other tools pin stay three.

WHY NOT `reviewscan`
--------------------
The first sketch said reviewscan was the natural home. It is not. reviewscan
**refuses to lint ROADMAP sections**, and that refusal is a recorded decision
(`docs/decisions/2026-07-18-0820-…`): a lint demanding a review line under every
roadmap heading fires on prose and gets trained away. That refusal is honoured
here, and this check is deliberately a different rung: it demands **nothing**
under any heading. It reads a narrow, self-identifying item class and reports
content that class is already forbidden to carry. A check that requires a field
everywhere fires on every author; a check that forbids a phrase in one item type
fires only on the failure.

The bar gate below (460/030) does ask something of the pointer class: the
intent record of a NEW queued pass must carry the review bar's answers. That is
still not a demand under every heading. It fires only on the item class that is
queuing a pass, only on what the commit adds, and a principal-ordered pass or a
reasoned `review: not warranted` stands in. Whether that is the same rung the
0820 record refused is the cold pass's question, not settled by this comment.

Why not fold it into `sizescan` either: sizescan's unit is a file's weight and
its harvest integrity. A child declaring `sizescan` advisory would silently
soften this too, and one scanner name covering two unrelated policies is exactly
the kind of hidden coupling the floor registry exists to make visible.

So: its own tool, sharing the one thing that must not be re-originated — the
scope decision below, which `harvestscan.is_pointer()` now imports from here
rather than keeping a second, narrower copy (B4 cold pass, HV2).

THE PRIOR QUESTION, SETTLED ON THE CORPUS: WHAT IS A POINTER?
--------------------------------------------------------------
Getting this wrong makes the check cover nothing while reporting clean — this
programme's organising defect. So it was decided on the four real specimens
rather than on the obvious marker.

The obvious scope — the queued-review marker glyph on the bullet — **provably
misses the live specimen.** The ADR 0008 entry carries a full reviewer agenda,
is marked as an ordinary open item, and states its review obligation mid-body.
`harvestscan.is_pointer()` had the same limit (marker, or a lead-6-words
phrase). The four shapes actually in the record are:

  a. the glyph as the bullet's own marker                        (instance 3)
  b. the glyph in the state prefix, after a claim stamp          (instance 1,
                                                                  pre-verdict)
  c. no glyph at all; the obligation stated in an emphasis run   (instance 1,
                                                                  live today)
  d. no checkbox at all; the bullet opens with a verdict stamp   (the five
                                                                  residues)

Shapes (c) and (d) are why the settled rule is **not** about the marker:

  An item is a queued-review pointer when the glyph stands in its MARKER or in
  its STATE PREFIX (the run before the item's own subject), **or** when a
  review-obligation phrase appears inside one of its EMPHASIS runs.

Emphasis, not plain prose, is the discriminating half, and it was measured
rather than assumed. Scoping on plain prose picks up two items on the live tree
that merely *discuss* pointers — this build's own funding entry, which quotes
the residues' wording, and a doctrine-candidate item mentioning "a fifth review
queued at close". Both are prose about the mechanism, not claims by the item
about itself. Emphasis-scoped, the live tree yields exactly the two genuine
pointer-class items and neither false positive. An author asserting an
obligation about their own item bolds it; an author writing prose about
obligations does not.

Code spans are stripped first, so a doc that names the marker syntax in
backticks is not swept in — stampscan's context-blindness lesson, applied at
the point where this tool is most likely to fire on the very doctrine that
describes it.

PASS TYPE IS A LAWFUL FIELD (FG6, settled here on the corpus)
--------------------------------------------------------------
The boundary specimen: a pointer carrying *"Design/intent pass per REVIEW.md
§ …"* — an instruction to the reviewer, but a procedural one. Ruled a lawful
fourth field beside {delta, intent record, tier}, on three grounds:

  * **Tier already is one, and it is the same class of fact.** The sanitised
    pointer produced when instance 3 was stripped — the corpus's own model of a
    compliant pointer — carries *"Cold pass owed per rule 4; the tier bar
    applies"*. Tier selects the reviewer; pass type selects the lens. Neither
    says anything about the delta's merits.
  * **The ceiling forbids an evaluative account, not routing.** REVIEW.md's
    words are "no evaluative account". A pass type is a routing fact, decidable
    without reading the delta.
  * **The failure the ceiling exists to stop is steering, and pass type does
    not steer.** The three real breaches all pre-framed a conclusion or
    volunteered the author's doubt. "Which lens" tells a reviewer where to
    stand; it does not tell them what they will see.

So the grammar check fires on *evaluative* direction, never on a bare pass-type
or tier reference.

WHAT DETECTOR 2 CARRIES: CYCLE STATE, READ FROM THE ITEM ITSELF
----------------------------------------------------------------
Two designs were open (recorded): existence-of-verdict, or reading the cycle
states — owed → reviewed → ruled → applied → closed. **This carries the cycle
states, read from the item's own text**, on four grounds:

  * It catches every recorded residue. The defect is *internal*: the same item
    asserts "owed" and links the verdict of the review that ran.
  * Existence-of-verdict needs a key joining an item to a verdict file, and the
    only mechanical keys available are the title and the heading. This repo has
    **measured** title-matching against roadmap items at a near-total
    false-positive rate (the 2026-07-26 audit, 362 commits — the finding that
    made `harvestscan` fingerprint content). Building this guard on that key
    would import the failure harvestscan was built to avoid.
  * It names the sharper defect. All five residues said the review was queued
    when what was actually owed was the principal's ruling. A guard that only
    knows "a verdict exists" cannot say that; one that reads states can.
  * It needs no cross-file join, so it has no CROSS-FILE plane seam. The
    single-file index-versus-worktree seam remains: `scan()` reads the working
    tree and the hook invocation passes no `--staged`, so a pointer staged and
    then reverted in the working tree scans clean. That is the accepted
    residual of the hygiene-scanner class (linkscan, datescan, wrapscan and
    spellscan read the working tree at the hook the same way); only the
    boundary scanners read the index (PG1).

**Stated residual, not defended against:** a pointer that is stale against a
verdict it never links is invisible here. That is the price of refusing the
title key, and it is the cheaper error — a missed warning, not a false one on
every healthy edit.

THE BAR GATE: A NEW PASS IS QUEUED ON GROUNDS (460/030)
--------------------------------------------------------
The review bar (`REVIEW.md` § *Whether work earns a review at all*) says a
session answers three questions in the work's intent record before it queues a
pass, or writes `review: not warranted — <grounds>` there instead, and that a
subject with an unrun, unbriefed pass has that pointer widened rather than a
second one opened. Nothing checked either, so the bar was one more judgement a
session could skip. This is the check, and it reads only what is NEW, so no
existing pointer is failed retroactively (460/040 handles those).

  * WHAT IS NEW. An item is read as new when it queues a pass (a pointer, or
    any non-`[x]` item in a `160-` review-owed section) and the base revision
    (`--base`, default HEAD) did not hold it as a pointer. A file the base lacks
    is all new; a renamed file is compared with its old path; a pointer whose
    title was reworded while it stayed the file's only pointer is the same
    pointer. Candidates come from the diff against the base, so an unchanged
    pointer is never read.
  * THE THREE ANSWERS, AS THE GATE READS THEM. The pointer stays refs only
    (rule 4), so the answers are in the intent record it links. The gate follows
    the markdown links after the pointer's `Intent record` label (a link into
    `reviews/` is a verdict, not a record), and in a linked record looks for
    three LABELLED lines, each at the start of a line (a list bullet and
    emphasis are allowed): `Commitment:`, `Worst failure:` and `Why the floor
    misses it:`, each followed by at least four words (an answer may wrap onto
    the lines beneath it; a `<placeholder>` counts as nothing; a fenced example
    is not read), OR a line `review: not warranted — <grounds>` with at least
    three words of grounds. A record that carries either passes; this checks
    that an answer EXISTS in a record the pointer names, never that it is a good
    one, and never that it is about THIS work rather than another pass sharing
    the record. A pass the principal ordered is owed whatever the answers, so
    it carries his words in an allow-marker (`pointerscan:allow:grammar:
    <reason>`), which is greppable.
  * A SECOND POINTER. A new pointer whose delta paths (the backticked paths
    after its `Delta` label, less the cross-cutting CHANGELOG and README
    files) overlap those of an open, unbriefed pointer (the queued glyph, no
    `brief written`, no landed verdict) is flagged (overlap: the same path, or
    one inside the other; a bare top-level directory such as `tools` holds too
    many subjects to count), naming the pointer to
    widen, unless the new pointer names the open one by its board ref (the two
    exceptions: the open pass is briefed, or the principal ordered this one on
    its own terms). Subject is read as shared delta paths because that is what
    can be read; a subject the paths do not show is not caught.
  * SAME KIND, NOT A NEW KIND. These findings are `grammar` findings (PK21's
    precedent: the kinds other tools pin stay three), marked `bar`, so a
    `pointerscan:allow:grammar:` marker exempts them and the printed ID is
    `pointerscan:grammar`.
  * PLANES. By default the new check reads the working tree against the base,
    like the rest of this tool, and only reports. `--staged` reads the INDEX
    instead (the commit that is about to happen: every detector, not just this
    one, so a sibling session's unstaged draft is nobody's business), and
    `--block` makes a bar finding exit 1 (it is the only finding that ever
    does). The floor's registry runs this tool warn-only with neither flag, so
    until that line is changed the check reports at the commit hook and blocks
    nothing; a check that cannot find a base says `NOT RUN` in its output (and
    exits 2 under `--block`) rather than reading as a pass.

ADVISORY, ALWAYS (but the bar gate under `--block`)
----------------------------------------------------
Findings exit 0. Every detector reads judgement-adjacent text and the honest
posture is to warn at the one moment the fix is free: a pointer is fixable in
the commit that writes it. A line carrying `pointerscan:allow: <reason>`
anywhere in an item exempts it — the same greppable hatch as the sibling
scanners. There is also a FILE-level form: the same marker on a roadmap file's
FIRST line exempts the whole file (unscoped), or drops one detector across it
(`pointerscan:allow:<detector>: <reason>`). It is a bigger lever than the
per-item hatch, so it is kept visible: the run summary's suppressed count
includes every file it exempts (PG2). The reviewer offered document-or-drop;
documented, because a file-level scope has been in use since AM4.

Exit codes:
  0  scanned (clean or with findings — this never blocks, but see --block)
  1  only under --block: a new pointer fails the bar gate
  2  environment error (a path that does not exist; under --block or --staged,
     no git base or index to read)

Usage:
  pointerscan --root . docs        scan the roadmaps under docs/
  pointerscan --root . .           scan the whole tree for roadmap files
  pointerscan --staged --block ... the commit gate: index plane, bar gate blocks
  pointerscan --base REV ...       what counts as new is what REV lacks
  pointerscan --json               machine-readable
  pointerscan --selftest           prove the rules on the recorded specimens
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import allowmarker  # noqa: E402
import filewalk  # noqa: E402
import report  # noqa: E402  (only `with_id`/`finding_dicts`, 115/080)

# The files this reads. The pointer grammar is a ROADMAP convention; nothing
# else in the tree carries it, and pointing this at prose would be the
# fires-on-every-author failure the 0820 record rejected.
ROADMAP_NAMES = ("ROADMAP.md",)

# The split board (ADR 2026-08-15): items live one-per-file under a directory
# named `roadmap`, and every such file speaks the same pointer grammar the
# monolithic ROADMAP.md did — so they are IN scope by directory, not by name.
# The generated index (`ROADMAP.md` opening with board.py's marker) is OUT: its
# one-line item renderings are projections, and linting a projection against
# the refs-only grammar would flag every healthy pointer the board renders.
ROADMAP_DIR_NAMES = ("roadmap",)
# Both spellings: board.py dropped the `tools/` prefix on 2026-08-17 (the path
# was false in every child), and an index generated before that keeps its skip
# until its next rebuild. Matched as a prefix, as board.py's own check is.
GENERATED_MARKS = ("<!-- GENERATED by board.py",
                   "<!-- GENERATED by tools/board.py")

ALLOW_MARKER = "pointerscan:allow:"
ALLOW_BASE = "pointerscan:allow"

# GUARDS.md rule (c): a marker only counts with a colon and a non-empty reason,
# so prose that merely mentions the marker text exempts nothing. Tightened
# 2026-08-05 — a bare marker used to exempt on a substring match.
ALLOW_RX = allowmarker.marker_rx(ALLOW_BASE, scope="one", group="kind")


def parse_allow(text: str) -> str | None:
    """The scope of the allow-marker, or None if there is no reasoned one.

    `""` means the whole item. A marker with no reason returns None — a
    mention, not an exemption."""
    return allowmarker.scope_of(ALLOW_RX, text, "kind")


# The three detectors — the bracketed kind on each finding line. A marker
# scoped to one (`pointerscan:allow:cycle: <reason>`) exempts that detector's
# findings only (115/080; AM4). The unscoped form, and a scope naming none of
# these, still exempt the whole item (or file), as they always did —
# `allowmarker.covers`.
FINDING_KINDS = frozenset({"grammar", "cycle", "state"})


# Directories holding nothing this repo authors.
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv",
             ".mypy_cache", ".ruff_cache", ".pytest_cache", ".idea", ".vscode"}

# The queued-review marker glyph. Held as a constant so no doc, comment or
# message in this file has to write it bare — the same discipline this tool
# enforces on the roadmap.
QUEUED = "⏳"

_FENCE = re.compile(r"^\s*(?:```|~~~)")
# Any top-level list bullet. DELIBERATELY wider than harvestscan's tri-state
# grammar: shape (d) in the docstring — the five residues — opens with a verdict
# stamp and no checkbox at all, so a checkbox-anchored parser cannot see the
# items where the defect was actually recorded.
_BULLET = re.compile(r"^(?:[-*+]|\d+[.)])\s+(.*)$")
# The state token a bullet may open with, if any.
_MARKER = re.compile(r"^(\[[ xX~]\]|" + QUEUED + r")\s*")
# A continuation line: indented, and not a new top-level bullet.
_CONT = re.compile(r"^\s+\S")

# Everything before the item's own subject. An author writes the state prefix
# first — claim stamp, marker, verdict stamp — and the subject in the first
# emphasis run. Capped as well as delimited so an item with no emphasis at all
# cannot turn the prefix test into a whole-body test.
_LEAD_CAP = 200

_EMPH = re.compile(r"\*\*(.+?)\*\*", re.S)
_CODE = re.compile(r"`[^`]*`")

# A claim, BY THE ITEM ABOUT ITSELF, that a review is owed. Every alternative
# here is lifted from a real pointer in this repo's history; none is invented to
# round out the pattern.
_CLAIM = re.compile(
    r"\breview(?:\s+is)?\s+(?:owed|queued)\b"
    r"|\b(?:cold|design|intent|application|terminal)\s+pass\s+owed\b"
    r"|\breviewer\s+needed\b"
    r"|\bqueued\s+for\s+a\s+non-?author\b",
    re.I)

# Evaluative direction at the reviewer. Kept SHORT on purpose and grounded one
# family per recorded instance — a speculative phrase list is a tuning surface,
# and an unfired pattern is an ungrounded claim about what goes wrong. It grows
# when a real instance shows it must, never before.
_STEER = (
    # Instance 1, verbatim family.
    (re.compile(r"\baim (?:a|the|your) reviewer\b", re.I),
     "aims the reviewer at a conclusion"),
    # Instance 3, verbatim family.
    (re.compile(r"\b(?:the\s+)?pass'?s?\s+first\s+question\b"
                r"|\bfirst\s+question\s+(?:is|the\s+work)\b", re.I),
     "seeds the pass's first question"),
    # The generic form of both: an instruction about what to conclude.
    (re.compile(r"\bthe reviewer (?:should|must|needs to|will want)\b"
                r"|\breviewer'?s? first (?:question|task)\b", re.I),
     "instructs the reviewer"),
)

# Evidence, inside the item, that the review has already run.
_REVIEWED = re.compile(
    r"\]\(\s*(?:\.\./)*reviews/[^)]+\)"      # a link into the verdict store
    r"|\bREVIEWED\s+\d{4}-\d{2}-\d{2}\b"
    r"|\bPASS-WITH-FINDINGS\b"
    r"|\bthe verdict is (?:above|below)\b",
    re.I)
# Evidence the cycle has moved past the review — used to name the state, so the
# warning can say what is actually owed rather than only that something is.
_RULING_OWED = re.compile(r"\bawaits?\s+(?:\w+'s\s+)?ruling\b"
                          r"|\bawait\s+(?:\w+'s\s+)?ruling\b", re.I)
_RULED = re.compile(r"\bRULED\b|\brulings? (?:verbatim|applied)\b")
# An explicit resolution of the obligation the claim phrase states. The corpus's
# own cleaned form says the pointer was queued at landing and has since been
# TAKEN; that is a historical account, not a live claim, and must stay silent.
_RESOLVED = re.compile(r"\*\*taken\*\*"
                       r"|\btaken\b\s*;"
                       r"|\bthe verdict is (?:above|below)\b", re.I)

# Evidence that THIS item's own pass has run — the stamps the house's closes
# actually write when a verdict lands ("The pass RAN 2026-09-26 and the cycle
# stays OPEN", "the cycle CLOSES on this pass", "Five rule-4 Fable cold passes
# ran 2026-08-05"). Deliberately NOT `_REVIEWED`: a pointer queuing a further
# pass links the verdicts before it, so a verdict link is provenance, not
# landing. A dated RAN stamp or a stated cycle outcome is the item speaking
# about its own pass. The date ends on a not-a-digit lookahead, never `\b`: an
# ISO 8601 stamp with a time ("RAN 2026-11-15T20:40Z") has no word boundary
# between the day and the `T` (board 115/400).
_LANDED = re.compile(
    r"\bRAN\s+\d{4}-\d{2}-\d{2}(?!\d)"
    r"|(?i:\bpass(?:es)?\s+ran\s+\d{4}-\d{2}-\d{2}(?!\d))"
    r"|\bcycle\s+(?:CLOSED|CLOSES|stays\s+OPEN)\b")
# The state line's own title claiming a queued or owed pass — the words a
# pointer's title carries ("Rule-4 cold pass queued: …", "Rule-4 review
# queued (tier: …)", "Rule-4 cold pass owed on …").
_TITLE_LEAD = re.compile(r"^[^\w*]*\*\*")
_TITLE_QUEUED = re.compile(r"\b(?:review|pass)\s+(?:is\s+)?(?:queued|owed)\b",
                           re.I)


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    detector: str      # "grammar" | "cycle"
    reason: str
    excerpt: str
    # True for a finding of the bar gate (a NEW pass queued without grounds, or
    # a second open pass on one subject): the only findings `--block` fails on.
    bar: bool = False


@dataclass(frozen=True)
class Item:
    line: int
    marker: str
    body: str


def strip_code(text: str) -> str:
    """Drop code spans. A doc naming the marker syntax in backticks is
    describing the convention, not asserting it — and this tool's own doctrine
    is exactly such a doc."""
    return _CODE.sub(" ", text)


def parse_items(text: str) -> list[Item]:
    """Every top-level list item, continuations and sub-bullets folded in.

    Fenced regions are skipped: a quoted example is not a work item, the same
    rule sizescan applies for the same reason."""
    items: list[Item] = []
    current: list[str] | None = None
    start, marker = 0, ""
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        if _FENCE.match(line):
            in_fence = not in_fence
            if current is not None:
                items.append(Item(start, marker, " ".join(current)))
                current = None
            continue
        if in_fence:
            continue
        m = _BULLET.match(line)
        if m:
            if current is not None:
                items.append(Item(start, marker, " ".join(current)))
            rest = m.group(1)
            mk = _MARKER.match(rest)
            marker = mk.group(1) if mk else ""
            current = [rest[mk.end():] if mk else rest]
            start = n
        elif current is not None and _CONT.match(line):
            current.append(line.strip())
        elif current is not None and not line.strip():
            continue          # a blank line inside an indented item body
        elif current is not None:
            items.append(Item(start, marker, " ".join(current)))
            current = None
    if current is not None:
        items.append(Item(start, marker, " ".join(current)))
    return items


def state_prefix(body: str) -> str:
    """The run before the item's own subject — where the state tokens live."""
    head = body.split("**", 1)[0]
    return head[:_LEAD_CAP]


def is_pointer(marker: str, body: str) -> bool:
    """Is this item a queued-review POINTER? The scope decision, single-sourced.

    `harvestscan` imports this so its pointer exclusion and this tool's cover
    cannot drift apart (B4 cold pass, HV2): every item this forgives there is an
    item this polices here, which is the only arrangement in which the
    exclusion is safe.

    Signature matches harvestscan's original: (marker, body). Either half may be
    empty — shape (d) has no marker at all."""
    # A completed item is not a pointer, whatever its prose says. The checkbox
    # is a work-owed tri-state (Mike, 2026-07-22): `[x]` means no more work is
    # owed, so an obligation phrase inside it is narration of a closed cycle by
    # construction. Measured, not assumed — without this the guard reported a
    # 2026-07-13 archived item that closes with "applied-batch cold pass owed
    # (above)", pointing at a live item elsewhere.
    if marker.strip().lower() == "[x]":
        return False
    if QUEUED in marker:
        return True
    text = strip_code(body)
    if QUEUED in state_prefix(text):
        return True
    return any(_CLAIM.search(run) for run in _EMPH.findall(text))


# A delta chosen by the commits' own citation of an item ("the four commits
# citing `115/510`"): a commit that touches the delta's paths and does not cite
# the item is not in it (PK21). The citing family, not one phrase (DP19):
# "commits citing", "commits that cite", "commits naming", "commits which
# reference", "commits mentioning". A bare present-tense verb ("commits name
# their files") says what commits do and selects none, so it is not matched.
_CITED_DELTA = re.compile(
    r"\bcommits?\s+(?:(?:that|which)\s+(?:cite|name|reference|mention)s?"
    r"|citing|naming|referencing|mentioning)\b", re.I)
# A commit hash: seven or more hex digits with at least one digit, so an
# English word spelled in hex ("defaced") is not one.
_HEX = r"(?=[0-9a-f]*\d)[0-9a-f]{7,40}"
_HASH = re.compile(r"\b" + _HEX + r"\b")
_HASH_RANGE = re.compile(r"\b" + _HEX + r"\.\.\.?" + _HEX + r"\b")
# Two or more hashes written as one list: only commas, "and", "+" or "&"
# between them, backticks allowed.
_HASH_LIST = re.compile(
    r"`?\b" + _HEX + r"\b`?(?:\s*(?:,\s*(?:and\s+)?|and\s+|[+&]\s*)`?\b"
    + _HEX + r"\b`?)+")
_SENTENCE_END = re.compile(r"(?<=[.;])\s+")


def delta_by_citation(body: str) -> bool:
    """Does the pointer name its delta's commits by citation alone (PK21)?

    True when the prose names commits by what they cite ("commits citing",
    "commits that cite", "commits naming" and the like) and binds no delta in
    hashes: neither a commit range (`a..b`) anywhere, nor a list of two or more
    hashes in a sentence that names the delta or carries the citation. Hashes
    elsewhere (a start hash, a pinned verdict, session ids) bind nothing, so
    they do not silence it (DP19). Hashes are read from the raw body,
    backticks included: they are normally written as code."""
    if not _CITED_DELTA.search(strip_code(body)):
        return False
    if _HASH_RANGE.search(body):
        return False
    for sentence in _SENTENCE_END.split(body):
        names_delta = ("delta" in sentence.lower()
                       or _CITED_DELTA.search(strip_code(sentence)))
        if not names_delta:
            continue
        for run in _HASH_LIST.finditer(sentence):
            if len(set(_HASH.findall(run.group(0)))) >= 2:
                return False
    return True


def grammar_findings(body: str) -> list[str]:
    """Reviewer-steering content inside a pointer. Pass type and tier are lawful
    (FG6, see the docstring) and are not matched by anything here."""
    text = strip_code(body)
    out: list[str] = []
    if "?" in text:
        out.append("carries a question — a pointer names refs, it does not "
                   "seed the pass's questions")
    for pattern, reason in _STEER:
        if pattern.search(text):
            out.append(reason)
    if delta_by_citation(body):
        out.append("names its delta's commits by citation alone — a commit "
                   "that touches the paths and does not cite the item is "
                   "missed; name the delta by path and a bound (a commit "
                   "range, or the hashes listed as the delta)")
    return out


def cycle_findings(body: str) -> list[str]:
    """A pointer whose claimed state contradicts the evidence in its own body.

    ORDER IS THE DISCRIMINATOR, and it is what makes this precise enough to
    wire. A verdict link inside an item is not on its own a contradiction: this
    repo's cycles routinely queue a *further* pass while citing the verdicts of
    the one before — "Review queued — the Track A application … Verdicts
    applied: …" is a correct pointer, not a stale one. What the residues share
    is the opposite order: the item's LEAD announces the review has run, and the
    owed-claim survives further down as residue nobody stripped.

    So: flag only when the review-has-run evidence stands BEFORE the claim.
    An author states the current state first and the history after; when the
    history is first, the item is a pointer citing its provenance.

    Measured: without this leg the guard reported three legitimate
    application-pass pointers over the history — the false-positive class that
    would have earned it an allow-marker."""
    text = strip_code(body)
    claim = _CLAIM.search(text)
    if not claim:
        return []                      # scoped in by the marker alone; no claim
    ran = _REVIEWED.search(text)
    if not ran:
        return []                      # genuinely owed as far as this item says
    if ran.start() > claim.start():
        return []                      # a pointer citing prior verdicts
    if _RESOLVED.search(text):
        return []                      # says so, and says it is resolved
    if _RULING_OWED.search(text):
        owed = "the ruling is what is owed, not the review"
    elif _RULED.search(text):
        owed = "the findings are ruled; what is owed is the application"
    else:
        owed = "the review has run"
    return [f"says a review is owed while carrying its own verdict — {owed}"]


def queued_state(marker: str, body: str) -> bool:
    """Does the item's STATE say a review is queued? The glyph as the marker,
    or in the state prefix after a claim stamp (a taken pass still running).
    A glyph inside a code span is a mention, not a state."""
    if QUEUED in marker:
        return True
    return marker.strip() != "[x]" and QUEUED in state_prefix(strip_code(body))


def landed_findings(marker: str, body: str) -> list[str]:
    """A pointer whose own pass has run, still wearing the queued glyph.

    The board legend's rule (130/020): the glyph means a review is queued and
    its pass has not yet returned a verdict, so it is the one thing a session
    counts to size the review queue. The commit that lands the verdict takes
    the glyph off the state line. ORDER IS NOT CONSULTED here, unlike
    `cycle_findings`: on the split board the state line is the item's first
    line, so a landed pointer always presents its glyph first and its verdict
    after, the exact layout the order rule reads as healthy (130/010, probed
    2026-08-18). What makes this precise instead is the evidence: a dated RAN
    stamp or a stated cycle outcome, which a pointer queuing a further pass
    has no reason to carry."""
    if not queued_state(marker, body):
        return []
    if not _LANDED.search(strip_code(body)):
        return []
    return ["records its own pass as run while its state line still says "
            "queued — the verdict has landed, so the glyph comes off: `[ ]` "
            "with what is owed named (🎯 when it is the principal's ruling), "
            "or `[x]` when nothing is"]


def unmarked_findings(marker: str, body: str) -> list[str]:
    """The inverse: an open item whose title says its review is queued, with no
    queued glyph and no record of the pass having run. A session counting the
    queue by its glyph misses it — found live, 2026-10-05, on a re-review
    queued as an ordinary open item."""
    if marker.strip() != "[ ]" or queued_state(marker, body):
        return []
    text = strip_code(body)
    # The TITLE: an emphasis run the item opens with, eye-flags aside. An item
    # opening on a verdict stamp and bolding an obligation mid-body is the
    # older shape detector 2 already reads.
    if not _TITLE_LEAD.match(text):
        return []
    runs = _EMPH.findall(text)
    if not runs or not _TITLE_QUEUED.search(runs[0]):
        return []
    if _LANDED.search(strip_code(body)):
        return []
    return ["its title says a review is queued and nothing records the pass "
            "as run, but the state line is not the queued glyph — a session "
            "counting the queue misses it"]


def scan_text(text: str, path: str = "",
              suppressed: list[int] | None = None,
              file_scope: str | None = None,
              cov: dict | None = None) -> list[Finding]:
    """Pure, so the selftest and the tests drive it with no filesystem.

    `suppressed` collects one entry per item an allow-marker exempted, so the
    caller can report the subtraction (`method/GUARDS.md`, rule b) instead of
    printing the same clean tick either way.

    `file_scope` is the detector a file-level marker (the file's first line)
    names, when it names one: that detector's findings are dropped across the
    file. A file-level marker exempting every kind never reaches here.

    `cov`, when given, gains one per item evaluated under `items` (115/130)."""
    out: list[Finding] = []
    for item in parse_items(text):
        if cov is not None:
            cov["items"] = cov.get("items", 0) + 1
        unmarked = unmarked_findings(item.marker, item.body)
        scope = parse_allow(item.body)
        if scope is not None:
            if suppressed is not None and (
                    unmarked or is_pointer(item.marker, item.body)):
                suppressed.append(1)
            if allowmarker.is_blanket(scope, FINDING_KINDS):
                continue
        # SUBTRACT SECOND: the item's findings form exactly as for an
        # unmarked item, then a marker naming one detector takes that one
        # away (115/080).
        out.extend(f for f in _item_findings(item, path, unmarked)
                   if not allowmarker.covers(scope, f.detector, FINDING_KINDS)
                   and not allowmarker.covers(file_scope, f.detector,
                                              FINDING_KINDS))
    return out


def _item_findings(item: "Item", path: str,
                   unmarked: list[str]) -> list[Finding]:
    """Every finding one item produces, before any allow-marker applies."""
    out: list[Finding] = []
    excerpt = " ".join(item.body.split())[:120]
    # Detector 3, the inverse half: outside the pointer scope by
    # construction (no glyph, and a title is not an emphasis-run CLAIM),
    # so it is read before the scope test rather than after it.
    for reason in unmarked:
        out.append(Finding(path, item.line, "state", reason, excerpt))
    if not is_pointer(item.marker, item.body):
        return out
    for reason in grammar_findings(item.body):
        out.append(Finding(path, item.line, "grammar", reason, excerpt))
    landed = landed_findings(item.marker, item.body)
    for reason in landed:
        out.append(Finding(path, item.line, "state", reason, excerpt))
    if landed:
        return out          # the sharper statement of the same contradiction
    for reason in cycle_findings(item.body):
        out.append(Finding(path, item.line, "cycle", reason, excerpt))
    return out


def _in_board_dir(p: Path) -> bool:
    """Is this file inside a split-board directory (any `roadmap/` segment)?"""
    return any(part in ROADMAP_DIR_NAMES for part in p.parts[:-1])


def roadmaps(paths: list[str], root: Path) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        p = (root / raw) if not Path(raw).is_absolute() else Path(raw)
        if p.is_file():
            if p.name in ROADMAP_NAMES or _in_board_dir(p):
                found.append(p)
            continue
        # 115/250: a directory is enumerated by the shared `tools/filewalk.py`
        # (110/110: git's tracked + untracked-not-ignored set inside a work
        # tree; 020/160: never read inside a linked worktree), not a bare
        # `rglob`, so a hand run does not count a sibling session's checkout.
        # `SKIP_DIRS` is this scanner's own per-guard parameter. Sorted so
        # the order is the one `rglob` gave.
        for sub in sorted(q for q in filewalk.walk_files(p, SKIP_DIRS)
                          if q.name.endswith(".md")):
            if sub.name in ROADMAP_NAMES or _in_board_dir(sub):
                found.append(sub)
    # A path may be named twice (`--root . .` plus an explicit docs/).
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in found:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            unique.append(p)
    return unique


class GitError(Exception):
    """git could not give this tool what it needs (no work tree, no such base,
    no index). Carried to `main`, which exits 2: a scan that cannot read its
    plane must not read as a pass."""


def _git(root: Path, *args: str, check: bool = True) -> bytes:
    """`git -C root <args>`, stdout bytes. Inherits the environment on purpose:
    a hook runs with `GIT_INDEX_FILE` set, and the index read must come from
    the same index the commit is made from."""
    try:
        r = subprocess.run(["git", "-C", str(root), *args],
                           capture_output=True)
    except OSError as e:
        raise GitError(f"git cannot run: {e}") from e
    if check and r.returncode != 0:
        raise GitError(f"git {' '.join(args[:2])} failed: "
                       f"{r.stderr.decode('utf-8', 'replace').strip()[:200]}")
    return r.stdout if r.returncode == 0 else b""


def _blob(root: Path, spec: str) -> str | None:
    """One blob by git object spec (`:0:path` the index, `REV:path` a revision);
    None when it does not exist there."""
    try:
        r = subprocess.run(["git", "-C", str(root), "cat-file", "blob", spec],
                           capture_output=True)
    except OSError as e:
        raise GitError(f"git cannot run: {e}") from e
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace")


def _blobs(root: Path, specs: list[str]) -> dict[str, str | None]:
    """Many blobs through ONE `git cat-file --batch` (a board holds hundreds of
    files, and a process per file is minutes); None for a spec that is not
    there."""
    if not specs:
        return {}
    try:
        r = subprocess.run(["git", "-C", str(root), "cat-file", "--batch"],
                           input="".join(s + "\n" for s in specs).encode(),
                           capture_output=True)
    except OSError as e:
        raise GitError(f"git cannot run: {e}") from e
    if r.returncode != 0:
        raise GitError("git cat-file --batch failed: "
                       + r.stderr.decode("utf-8", "replace").strip()[:200])
    out: dict[str, str | None] = {}
    data, pos = r.stdout, 0
    for spec in specs:
        eol = data.index(b"\n", pos)
        head = data[pos:eol].split()
        pos = eol + 1
        if len(head) == 3 and head[1] == b"blob":
            size = int(head[2])
            out[spec] = data[pos:pos + size].decode("utf-8", "replace")
            pos += size + 1
        else:
            out[spec] = None            # "<spec> missing"
    return out


def _is_roadmap_rel(rel: str) -> bool:
    """The roadmap-file test `roadmaps()` applies, for a repo-relative path."""
    p = Path(rel)
    if not rel.endswith(".md") or any(x in SKIP_DIRS for x in p.parts[:-1]):
        return False
    return p.name in ROADMAP_NAMES or _in_board_dir(p)


def _scope_specs(paths: list[str], root: Path) -> list[str]:
    """The scan paths as repo-relative git pathspecs (an absolute path under
    the root is made relative; one outside it names nothing here)."""
    out: list[str] = []
    for raw in paths:
        p = Path(raw)
        if p.is_absolute():
            try:
                p = p.resolve().relative_to(root.resolve())
            except ValueError:
                continue
        out.append(posixpath.normpath(p.as_posix()))
    return out


def _check_work_tree(root: Path) -> None:
    top = _git(root, "rev-parse", "--show-toplevel").decode().strip()
    if Path(top).resolve() != root.resolve():
        raise GitError("the root is not the top of a git work tree")


def _iter_texts(paths: list[str], root: Path, staged: bool):
    """(repo-relative path, text) for every roadmap file in scope: from the
    working tree, or with `staged` from the INDEX (what the commit will hold).
    Files that cannot be read are skipped, as they always were."""
    if not staged:
        for p in roadmaps(paths, root):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            try:
                rel = p.resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                rel = p.as_posix()
            yield rel, text
        return
    _check_work_tree(root)
    listed = _git(root, "ls-files", "-z", "--", *(_scope_specs(paths, root)
                                                  or ["."]))
    rels = sorted(r for r in (x.decode("utf-8", "replace")
                              for x in listed.split(b"\0") if x)
                  if _is_roadmap_rel(r))
    blobs = _blobs(root, [f":0:{r}" for r in rels])
    for rel in rels:
        text = blobs[f":0:{rel}"]
        if text is not None:
            yield rel, text


def scan(paths: list[str], root: Path,
         suppressed: list[int] | None = None,
         cov: dict | None = None,
         staged: bool = False) -> list[Finding]:
    """`cov`, when given, is filled with what the scan looked at (115/130):
    `files` = roadmap files read, `items` = the items evaluated in them. A side
    channel, so the return value callers compare keeps its shape. `staged`
    reads the index copies instead of the working tree's (the hook plane)."""
    out: list[Finding] = []
    for rel, text in _iter_texts(paths, root, staged):
        if cov is not None:
            cov["files"] = cov.get("files", 0) + 1
        if text.startswith(GENERATED_MARKS):
            continue        # the board index — projections, not items (above)
        file_scope = parse_allow(text.split("\n")[0])
        if file_scope is not None:
            if suppressed is not None:
                suppressed.append(1)
            if allowmarker.is_blanket(file_scope, FINDING_KINDS):
                continue
        out.extend(scan_text(text, rel, suppressed, file_scope, cov))
    return out


# --- the bar gate (460/030) ---------------------------------------------------
# See the module docstring, THE BAR GATE. Everything here reads only what is NEW
# against a base revision.

# The three answers the review bar asks of the work's intent record, as the
# labels the gate reads (`REVIEW.md` § Whether work earns a review at all).
BAR_ANSWERS = (("commitment", "Commitment"),
               ("worst failure", "Worst failure"),
               ("why the floor misses it", "Why the floor misses it"))
BAR_MIN_WORDS = 4        # an answer shorter than this is a placeholder
NOT_WARRANTED_MIN_WORDS = 3

# Section directories whose every new item queues a pass (atelier's `160`).
_REVIEW_OWED_DIR = re.compile(r"(?:^|/)160-[^/]+/[^/]+\.md$")
# Cross-cutting files a change to almost anything also touches: sharing one of
# these is not sharing a subject.
_SHARED_SURFACES = frozenset({
    "CHANGELOG.md", "README.md", "tools/README.md", "instruments/README.md",
    "docs/ROADMAP.md", "docs/README.md"})

_LEAD = r"^\s*(?:(?:[-+>]|\d+[.)])\s+)*"       # list bullets before a label
_LABEL_RX = {key: re.compile(_LEAD + label + r"\s*:\s*(.*)$", re.I)
             for key, label in BAR_ANSWERS}
_NOT_WARRANTED_RX = re.compile(
    _LEAD + r"review\s*:\s*not\s+warranted\s*(?:—|–|--?)\s*(.*)$", re.I)
_BLOCK_STOP = re.compile(r"^\s*(?:[-+>#|]|\d+[.)]\s)")
_PLACEHOLDER = re.compile(r"<[^>\n]*>")
_WORD = re.compile(r"[A-Za-z0-9][\w'’-]*")
_INTENT_LABEL = re.compile(r"intent\s+records?", re.I)
_NEXT_LABEL = re.compile(r"\*\*[^*\n]{1,120}\*\*|\*[A-Za-z][^*\n]{0,60}:\*")
_LINK = re.compile(r"\]\(\s*<?([^)\s>#]+)(?:#[^)\s]*)?>?(?:\s+\"[^\"]*\")?\s*\)")
_DELTA_LABEL = re.compile(r"\bdelta\b", re.I)
_BRIEFED = re.compile(r"\bbrief\s+written\b", re.I)
_REF_PATH = re.compile(r"roadmap/(\d+)-[^/]+/(\d+)-[^/]+\.md$")


def _record_lines(text: str) -> list[str]:
    """A record's lines with fenced regions dropped (a quoted example is not an
    answer) and emphasis marks removed, so `**Commitment:**` reads as
    `Commitment:`. Backticks stay: a label in a code span is a mention."""
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if _FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(re.sub(r"[*_]", "", line))
    return out


def _words(text: str) -> int:
    return len(_WORD.findall(_PLACEHOLDER.sub(" ", text)))


def _labelled(lines: list[str], rx: "re.Pattern[str]", minimum: int) -> bool:
    """Does any line carry the label with at least `minimum` words after it,
    counting the lines that wrap beneath it?"""
    for i, line in enumerate(lines):
        m = rx.match(line)
        if not m:
            continue
        parts = [m.group(1)]
        for nxt in lines[i + 1:]:
            if (not nxt.strip() or _BLOCK_STOP.match(nxt)
                    or _NOT_WARRANTED_RX.match(nxt)
                    or any(r.match(nxt) for r in _LABEL_RX.values())):
                break
            parts.append(nxt.strip())
        if _words(" ".join(parts)) >= minimum:
            return True
    return False


def record_gaps(text: str) -> list[str]:
    """What a record lacks of the bar: [] when it carries all three answers or
    a `review: not warranted` line with grounds; else the answers it lacks."""
    lines = _record_lines(text)
    if _labelled(lines, _NOT_WARRANTED_RX, NOT_WARRANTED_MIN_WORDS):
        return []
    return [label for key, label in BAR_ANSWERS
            if not _labelled(lines, _LABEL_RX[key], BAR_MIN_WORDS)]


def intent_links(body: str, rel: str) -> list[str]:
    """Repo-relative paths of the markdown records a pointer names as its
    intent record: the links after each `Intent record` label, up to the next
    label. A verdict (a link into `reviews/`), a URL and a non-`.md` target are
    not records."""
    text = strip_code(body)
    out: list[str] = []
    for lab in _INTENT_LABEL.finditer(text):
        tail = text[lab.end():]
        nxt = _NEXT_LABEL.search(tail)
        region = tail[:nxt.start()] if nxt else tail
        for target in _LINK.findall(region):
            if "://" in target or not target.endswith(".md"):
                continue
            path = posixpath.normpath(
                posixpath.join(posixpath.dirname(rel), target))
            if (path.startswith("..") or path.startswith("/")
                    or "/reviews/" in "/" + path):
                continue
            if path not in out:
                out.append(path)
    return out


def _norm_path(tok: str) -> str | None:
    """A backticked token as a comparable repo path, or None if it is not one."""
    tok = tok.strip()
    if not tok or " " in tok or "://" in tok or tok.startswith("<"):
        return None
    if re.fullmatch(r"\d+/\d+", tok) or ".." in tok:
        return None
    if "/" not in tok and not re.search(r"\.[A-Za-z0-9]{1,5}$", tok):
        return None
    if tok.startswith("./"):
        tok = tok[2:]
    tok = re.sub(r"(?:/\*\*?|/)$", "", tok).rstrip("*")
    tok = tok.rstrip("/")
    if not tok or tok in _SHARED_SURFACES:
        return None
    if tok.startswith(("docs/roadmap", "docs/reviews", "docs/sessions")):
        return None
    return tok


def delta_paths(body: str) -> list[str]:
    """The paths a pointer's delta names: backticked, from its `Delta` label to
    its `Intent record` label (or the end)."""
    m = _DELTA_LABEL.search(body)
    if not m:
        return []
    raw = body[m.start():]
    stop = _INTENT_LABEL.search(raw)
    if stop:
        raw = raw[:stop.start()]
    out: list[str] = []
    for tok in re.findall(r"`([^`\n]+)`", raw):
        p = _norm_path(tok)
        if p and p not in out:
            out.append(p)
    return out


def _paths_overlap(a: str, b: str) -> bool:
    """Do two delta paths name one subject? The same path, or one inside the
    other. A bare top-level directory (`tools`, `skills`) holds every subject
    in it, so it is too broad to make two passes one subject."""
    if a == b:
        return True
    inner, outer = (a, b) if a.startswith(b + "/") else (b, a)
    return inner.startswith(outer + "/") and "/" in outer


def board_ref(rel: str) -> str | None:
    """`160/1880` for `docs/roadmap/160-…/1880-….md`, or None."""
    m = _REF_PATH.search(rel)
    return f"{m.group(1)}/{m.group(2)}" if m else None


def _item_key(body: str) -> str:
    runs = _EMPH.findall(strip_code(body))
    return " ".join((runs[0] if runs else body[:80]).lower().split())


def _queues(item: "Item", fresh_owed: bool) -> bool:
    """Does this item queue a pass? A pointer does; so does any open item newly
    added to a review-owed section."""
    if is_pointer(item.marker, item.body):
        return True
    return fresh_owed and item.marker.strip().lower() != "[x]"


def new_items(cur: list["Item"], base: list["Item"] | None,
              fresh_owed: bool) -> list["Item"]:
    """The items of a file that queue a pass and that the base did not hold as a
    pointer. `base` None means the file is new."""
    queuing = [i for i in cur if _queues(i, fresh_owed and base is None)]
    if base is None:
        return queuing
    base_ptrs = [i for i in base if is_pointer(i.marker, i.body)]
    keys = {_item_key(i.body) for i in base_ptrs}
    cur_ptrs = [i for i in cur if is_pointer(i.marker, i.body)]
    out = []
    for it in queuing:
        if is_pointer(it.marker, it.body):
            if _item_key(it.body) in keys:
                continue
            if len(base_ptrs) == 1 and len(cur_ptrs) == 1:
                continue          # reworded, still the file's one pointer
        out.append(it)
    return out


def open_unbriefed(item: "Item") -> bool:
    """An open pass with no brief yet: the queued glyph still on, no verdict
    landed, no brief written."""
    if item.marker.strip().lower() == "[x]" or not is_pointer(item.marker,
                                                              item.body):
        return False
    if not queued_state(item.marker, item.body):
        return False
    text = strip_code(item.body)
    return not _LANDED.search(text) and not _BRIEFED.search(text)


@dataclass
class BarRun:
    """What the bar gate did: it states whether it looked, so a run that could
    not read a base never reads as a pass."""
    ran: bool = False
    note: str = ""
    new_pointers: int = 0
    base: str = ""
    plane: str = ""
    findings: list = None

    def __post_init__(self):
        if self.findings is None:
            self.findings = []

    def line(self) -> str:
        if not self.ran:
            return f"  bar check: NOT RUN — {self.note}"
        return (f"  bar check: {self.new_pointers} new queued pass(es) read "
                f"against {self.base} ({self.plane} plane)")


def _changed_files(root: Path, base: str, staged: bool) -> dict[str, str | None]:
    """Added or modified files (a rename maps to the path it came from) between
    the base and the plane: {path: old path or None}."""
    args = ["diff", "--name-status", "-z", "--find-renames",
            "--diff-filter=AMR"]
    if staged:
        args.append("--cached")
    raw = _git(root, *args, base, "--").split(b"\0")
    changed: dict[str, str | None] = {}
    i = 0
    while i < len(raw) and raw[i]:
        status = raw[i].decode("utf-8", "replace")
        if status.startswith("R"):
            old, new = (raw[i + 1].decode("utf-8", "replace"),
                        raw[i + 2].decode("utf-8", "replace"))
            changed[new] = old
            i += 3
        else:
            changed[raw[i + 1].decode("utf-8", "replace")] = None
            i += 2
    if not staged:
        for x in _git(root, "ls-files", "-z", "--others",
                      "--exclude-standard").split(b"\0"):
            if x:
                changed.setdefault(x.decode("utf-8", "replace"), None)
    return changed


def bar_scan(paths: list[str], root: Path, *, base: str = "HEAD",
             staged: bool = False,
             suppressed: list[int] | None = None) -> BarRun:
    """The bar gate over what is new against `base` (module docstring)."""
    run = BarRun(base=base, plane="index" if staged else "working-tree")
    if not base:
        run.note = "no base revision given"
        return run
    try:
        _check_work_tree(root)
        if subprocess.run(
                ["git", "-C", str(root), "rev-parse", "--verify", "--quiet",
                 base + "^{commit}"], capture_output=True).returncode != 0:
            run.note = f"base `{base}` is not a commit here"
            return run
        changed = _changed_files(root, base, staged)
        texts = dict(_iter_texts(paths, root, staged))
        read = ((lambda rel: _blob(root, f":0:{rel}")) if staged else
                (lambda rel: _read_worktree(root, rel)))
        cand: list[tuple[str, "Item"]] = []
        for rel, text in sorted(texts.items()):
            if (rel not in changed or text.startswith(GENERATED_MARKS)
                    or Path(rel).name == "README.md"):
                continue            # a section's README is not a board item
            old = changed[rel] or rel
            base_text = _blob(root, f"{base}:{old}")
            base_items = parse_items(base_text) if base_text is not None else None
            fresh = base_text is None and bool(_REVIEW_OWED_DIR.search(rel))
            for it in new_items(parse_items(text), base_items, fresh):
                cand.append((rel, it))
        run.ran = True
        run.new_pointers = len(cand)
        if not cand:
            return run
        siblings = _open_siblings(texts)
        new_keys = {(rel, it.line) for rel, it in cand}
        for rel, it in cand:
            reasons = _bar_reasons(rel, it, read, siblings, new_keys)
            file_scope = parse_allow(texts[rel].split("\n")[0])
            scope = parse_allow(it.body)
            excerpt = " ".join(it.body.split())[:120]
            for reason in reasons:
                if (allowmarker.covers(scope, "grammar", FINDING_KINDS)
                        or allowmarker.covers(file_scope, "grammar",
                                              FINDING_KINDS)):
                    if suppressed is not None:
                        suppressed.append(1)
                    continue
                run.findings.append(
                    Finding(rel, it.line, "grammar", reason, excerpt, True))
    except GitError as e:
        run.ran = False
        run.note = str(e)
    return run


def _read_worktree(root: Path, rel: str) -> str | None:
    try:
        return (root / rel).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def _open_siblings(texts: dict[str, str]) -> list[tuple[str, "Item", list[str]]]:
    """Every open, unbriefed pointer in the plane that names delta paths."""
    out = []
    for rel, text in texts.items():
        if text.startswith(GENERATED_MARKS) or Path(rel).name == "README.md":
            continue
        for it in parse_items(text):
            if open_unbriefed(it):
                paths = delta_paths(it.body)
                if paths:
                    out.append((rel, it, paths))
    return out


def _bar_reasons(rel: str, it: "Item", read, siblings, new_keys) -> list[str]:
    reasons: list[str] = []
    links = intent_links(it.body, rel)
    if not links:
        reasons.append(
            "queues a pass but names no intent record by a markdown link "
            "after an `Intent record` label — the review bar's three answers "
            "(REVIEW.md, Whether work earns a review at all) live in that "
            "record, so there is nowhere to read them")
    else:
        gaps: list[list[str]] = []
        missing: list[str] = []
        for path in links:
            text = read(path)
            if text is None:
                missing.append(path)
                continue
            g = record_gaps(text)
            if not g:
                gaps = []
                missing = []
                break
            gaps.append(g)
        else:
            if gaps:
                best = min(gaps, key=len)
                reasons.append(
                    "its intent record carries neither the review bar's three "
                    "answers nor `review: not warranted — <grounds>` "
                    f"(no labelled answer for: {', '.join(best)}); write each "
                    "as a line `Commitment:`, `Worst failure:` and `Why the "
                    "floor misses it:` in the record, or the not-warranted "
                    "line (a pass the principal ordered carries his words in "
                    "a `pointerscan:allow:grammar:` marker)")
            elif missing:
                reasons.append(
                    "the intent record it names was not found: "
                    + ", ".join(missing))
    mine = delta_paths(it.body)
    if mine:
        for srel, sit, spaths in siblings:
            if srel == rel:
                continue
            if (srel, sit.line) in new_keys and (srel, sit.line) > (rel, it.line):
                continue            # two new together: the later one is flagged
            shared = [a for a in mine for b in spaths if _paths_overlap(a, b)]
            if not shared:
                continue
            ref = board_ref(srel)
            if (ref and re.search(r"(?<![\w/])" + re.escape(ref) + r"(?![\w/])",
                                  it.body)) or Path(srel).name in it.body:
                continue            # names the open sibling: an exception
            reasons.append(
                f"opens a second pass on a subject that already has an open, "
                f"unbriefed one (`{ref or srel}`, sharing `{shared[0]}`): widen "
                f"that pointer's delta instead; or name it here if it is "
                f"briefed or the principal ordered this pass on its own terms "
                f"(REVIEW.md, One open pass per subject)")
            break
    return reasons


# --- the recorded specimens, as the selftest's fixtures ----------------------
# Trimmed to the load-bearing sentence and reproduced here so the rules can be
# proven with no git and no filesystem. The full versions live in history at the
# commits named beside each.

# Instance 1, as it stands live: no marker glyph, obligation in an emphasis run,
# a reviewer agenda and a seeded question.
_SPEC_LIVE = (
    "- [ ] REVIEWED 2026-07-26 (rule-4 cold pass): PASS-WITH-FINDINGS\n"
    "      3M/5m/1L/1n — [verdict](reviews/2026-07-26-2215-adr0008-cold.md);\n"
    "      EP1-EP10 await Mike's ruling (rule 3). **ADR 0008 review owed** —\n"
    "      self-authored, so this session may not review it (rule 4). Aim a\n"
    "      reviewer at the one real trade: moving every repo onto a floating\n"
    "      caller swaps a slow silent failure for a fast loud estate-wide one.\n"
    "      Is that right for a security floor?\n")

# Instance 3, written at ff8080b and stripped at 7ca1f1d — the must-flag half.
_SPEC_INSTANCE_3 = (
    "- " + QUEUED + " **B4 - harvestscan, the roadmap-deletion guard.** Delta:\n"
    "  the tool, its tests, and the B4 entry carrying its measurement. Intent\n"
    "  record: the Track B session entry. Cold pass owed per rule 4; the tier\n"
    "  bar applies. **The pass's first question is whether a 26.9% firing rate\n"
    "  is the right ground for the verdict, or whether the measurement itself\n"
    "  is mis-shaped** - the author reached that verdict on his own instrument.\n")

# The same pointer after 7ca1f1d stripped it — the must-stay-silent half, and
# the corpus's own model of a compliant pointer.
_SPEC_INSTANCE_3_CLEAN = (
    "- " + QUEUED + " **B4 - the roadmap-deletion guard: the item, and the work\n"
    "  addressing it** (queued at Mike's request). Delta: the tool, its tests,\n"
    "  the B4 entry in this file, which carries both the measurement and the\n"
    "  verdict. Intent record: the Track B session record. Cold pass owed per\n"
    "  rule 4; the tier bar applies (cold review passes run on Fable).\n")

# The FG6 boundary specimen: an instruction to the reviewer, but procedural.
_SPEC_PASS_TYPE = (
    "- [ ] **F1 - rebuild the block-vs-advise model from base.**\n"
    "      **" + QUEUED + " Review queued for a non-author.** Cold passes run on\n"
    "      **Fable**. *Delta:* this item (records-only). *Intent record:*\n"
    "      [the session record](sessions/2026-08-02-2340-frame.md).\n"
    "      Design/intent pass per REVIEW.md section *Review the design, not\n"
    "      only the build*.\n")

# Shape (d): one of the five residues, exactly as 98cef9e left it — no checkbox,
# a verdict stamp in the bullet, and the stale claim mid-body.
_SPEC_RESIDUE = (
    "- REVIEWED 2026-07-26 (rule-4 cold pass): PASS-WITH-FINDINGS 0M/3m/3n\n"
    "  - [verdict](reviews/2026-07-26-2215-evidence-escalation-rung-cold.md);\n"
    "  EE1-EE6 await Mike's ruling (rule 3). **Capture to doctrine: escalating\n"
    "  to the principal is not a rung** - APPLIED 2026-07-26. **" + QUEUED + "\n"
    "  review queued for a non-author** (self-authored doctrine, rule 4).\n"
    "  *Delta:* the paragraph landed this commit. Rides the normal review cycle\n"
    "  when a qualifying session takes it.\n")

# The same residue after 49f1a8f cleaned it — the must-stay-silent half.
_SPEC_RESIDUE_CLEAN = (
    "- REVIEWED 2026-07-26 (rule-4 cold pass): PASS-WITH-FINDINGS 0M/3m/3n\n"
    "  - [verdict](reviews/2026-07-26-2215-evidence-escalation-rung-cold.md);\n"
    "  EE1-EE6 await Mike's ruling (rule 3). **Capture to doctrine: escalating\n"
    "  to the principal is not a rung** - APPLIED 2026-07-26. **Review queued\n"
    "  at landing** (self-authored doctrine, rule 4) - **taken**; the verdict\n"
    "  is above. *Delta:* the paragraph landed this commit.\n")

# A pointer queuing a FURTHER pass while citing the verdicts of the one before
# (f52b703's Track A application pointer). Correct, and the shape that makes
# "carries a verdict link" too blunt a test on its own.
_SPEC_FURTHER_PASS = (
    "- " + QUEUED + " **Review queued — the Track A application (A1-A5b).**\n"
    "  Rule 4: each application earns a further cold pass while a MAJOR stood,\n"
    "  and two did. **Delta:** the floor and its tests. **Intent record:**\n"
    "  [the Track A session](sessions/2026-07-27-2301-track-a-fail-opens.md).\n"
    "  **Verdicts applied:** [ADR 0008 cold pass](reviews/2026-07-26-2215-adr\n"
    "  0008-enforcement-propagation-cold.md).\n")

# A COMPLETED item narrating a closed cycle and pointing at a live one. The
# checkbox is a work-owed tri-state, so this is not a pointer at all.
_SPEC_ARCHIVED = (
    "- [x] **Cold review of CONCURRENCY \"Claiming work\"** — RAN 2026-07-13,\n"
    "      un-briefed: **PASS-WITH-FINDINGS**, verdict in\n"
    "      `reviews/2026-07-13-concurrency-claiming-work.md`. Mike ruled all\n"
    "      seven fixed, applied same day. **Applied-batch cold pass owed**\n"
    "      (above).\n")

# Detector 3, both halves, in the split board's shape (130/020). A pointer
# whose own pass has run, still wearing the glyph — the layout the 27 items
# had before 1d96efa: claim in the lead, outcome in a sub-bullet beneath.
_SPEC_LANDED = (
    "- " + QUEUED + " **Rule-4 cold pass queued: the widget rule.** Delta:\n"
    "      the paragraph. Intent record: the session record.\n"
    "      - [ ] **The pass RAN 2026-09-26 and the cycle stays OPEN — a MAJOR\n"
    "            stands.** [verdict](../../reviews/2026-09-25-0715-w.md).\n")
# The same item once the verdict has landed and the glyph is off.
_SPEC_LANDED_FIXED = _SPEC_LANDED.replace("- " + QUEUED + " ", "- [ ] 🎯 ", 1)
# A re-review queued as an ordinary open item (2026-10-05's shape).
_SPEC_UNMARKED = (
    "- [ ] 🛑 **Rule-4 cold pass queued: the widget hardening.** Tier: the\n"
    "      principal-named review tier. Delta: the tool and its tests.\n"
    "      Intent record: the session record.\n")
_SPEC_UNMARKED_FIXED = _SPEC_UNMARKED.replace("- [ ] 🛑 ", "- " + QUEUED + " ", 1)

# Prose ABOUT pointers, in an ordinary work item. The scope must not sweep it in
# — this is the shape of this build's own funding entry.
_SPEC_PROSE = (
    "- [ ] **Mechanise the pointer grammar.** All five said \"review queued\"\n"
    "      when the review had run. Is this the same rung the 0820 record\n"
    "      rejected? The first question the work must answer, not assume.\n")


# PK21: the shape of the `160/1810` pointer, synthetic values.
_SPEC_CITED_DELTA = (
    f"- {QUEUED} **Rule-4 cold pass queued: the widget fixes.** Tier: the review\n"
    "      tier. *Delta, scoped to paths:* `tools/widget.py`, `docs/widget.md`:\n"
    "      the commits citing `210/600`, on `main`, after `a1cc5f2d`.\n")


def _selftest() -> int:
    fails: list[str] = []

    def check(label: str, got, want) -> None:
        if got != want:
            fails.append(f"{label}: expected {want}, got {got}")

    def dets(text: str) -> list[str]:
        """Which detectors fire, deduplicated — one item can trip a detector on
        two grounds at once (the live specimen trips grammar on both the seeded
        question and the reviewer instruction), and the count of grounds is not
        what these legs are pinning."""
        return sorted({f.detector for f in scan_text(text)})

    # --- scope ---------------------------------------------------------------
    check("live specimen is in scope",
          [is_pointer(i.marker, i.body) for i in parse_items(_SPEC_LIVE)], [True])
    check("marker shape is in scope",
          [is_pointer(i.marker, i.body) for i in parse_items(_SPEC_INSTANCE_3)],
          [True])
    check("no-checkbox residue is in scope",
          [is_pointer(i.marker, i.body) for i in parse_items(_SPEC_RESIDUE)],
          [True])
    check("prose about pointers is OUT of scope",
          [is_pointer(i.marker, i.body) for i in parse_items(_SPEC_PROSE)],
          [False])

    # --- detector 1: grammar -------------------------------------------------
    check("live specimen flagged", dets(_SPEC_LIVE), ["cycle", "grammar"])
    check("live specimen trips BOTH grammar legs",
          len([f for f in scan_text(_SPEC_LIVE) if f.detector == "grammar"]), 2)
    check("instance 3 flagged", dets(_SPEC_INSTANCE_3), ["grammar"])
    check("instance 3 cleaned is silent", dets(_SPEC_INSTANCE_3_CLEAN), [])
    check("pass type is lawful (FG6)", dets(_SPEC_PASS_TYPE), [])
    check("prose item is silent", dets(_SPEC_PROSE), [])
    check("a delta named by citation alone is flagged (PK21)",
          dets(_SPEC_CITED_DELTA), ["grammar"])
    check("the same delta with a commit range is silent",
          dets(_SPEC_CITED_DELTA.replace(
              "`210/600`", "`210/600`, `a1cc5f2d..9b4a8f8f`")), [])

    # --- detector 2: cycle state ---------------------------------------------
    check("stale residue flagged", dets(_SPEC_RESIDUE), ["cycle"])
    check("cleaned residue is silent", dets(_SPEC_RESIDUE_CLEAN), [])
    check("the state is named",
          any("ruling is what is owed" in f.reason
              for f in scan_text(_SPEC_RESIDUE)), True)
    check("a further pass citing prior verdicts is silent",
          dets(_SPEC_FURTHER_PASS), [])
    check("a completed item is not a pointer",
          [is_pointer(i.marker, i.body) for i in parse_items(_SPEC_ARCHIVED)],
          [False])
    check("a completed item is silent", dets(_SPEC_ARCHIVED), [])

    # --- detector 3: queue state (130/020) -----------------------------------
    check("a landed pointer still wearing the glyph is flagged",
          dets(_SPEC_LANDED), ["state"])
    check("the landed pointer, glyph off, is silent", dets(_SPEC_LANDED_FIXED), [])
    check("a queued review without the glyph is flagged",
          dets(_SPEC_UNMARKED), ["state"])
    check("the same review wearing the glyph is silent",
          dets(_SPEC_UNMARKED_FIXED), [])
    check("a further pass citing prior verdicts is not landed",
          [f.detector for f in scan_text(_SPEC_FURTHER_PASS)], [])

    # --- the bar gate (460/030): the reading of a record, git-free ----------
    answers = ("- **Commitment:** a gate that blocks every widget commit\n"
               "- **Worst failure:** it reads green while checking nothing\n"
               "- **Why the floor misses it:** the tests only run known cases\n")
    check("a record with the three answers has no gaps",
          record_gaps(answers), [])
    check("a record with none lacks all three",
          len(record_gaps("# nothing asked here\n")), 3)
    check("one answer removed is the one named",
          record_gaps(answers.replace("Worst failure", "Other")),
          ["Worst failure"])
    check("a not-warranted line with grounds stands in",
          record_gaps("review: not warranted — a wording fix only\n"), [])
    check("a placeholder answer is no answer",
          record_gaps(answers.replace("a gate that blocks every widget commit",
                                      "<what rests on it>")), ["Commitment"])
    check("a link into reviews/ is not an intent record",
          intent_links("**x.** *Intent record:* [v](../../reviews/v.md)",
                       "docs/roadmap/160-a/010-b.md"), [])
    check("an intent record link resolves from the pointer's directory",
          intent_links("**x.** *Intent record:* [s](../../sessions/s.md)",
                       "docs/roadmap/160-a/010-b.md"),
          ["docs/sessions/s.md"])

    # --- hatch ---------------------------------------------------------------
    check("allow marker exempts",
          dets(_SPEC_INSTANCE_3.replace("Delta:",
                                        f"{ALLOW_MARKER} quoted; Delta:")), [])

    # --- parsing -------------------------------------------------------------
    check("fenced examples are skipped",
          len(parse_items("```\n- " + QUEUED + " a queued example\n```\n")), 0)
    check("sub-bullets fold into the item",
          len(parse_items("- [ ] head\n  - sub one\n  - sub two\n")), 1)

    for f in fails:
        print(f"pointerscan selftest FAIL: {f}", file=sys.stderr)
    print(f"pointerscan selftest: {'FAILED' if fails else 'ok'} "
          f"({len(fails)} failure(s))")
    return 1 if fails else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="pointerscan", description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*", default=["."],
                    help="files or trees to scan (roadmaps within them)")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--json", action="store_true", help="machine-readable")
    ap.add_argument("--staged", action="store_true",
                    help="read the INDEX copy of every roadmap file (the "
                         "commit about to be made), not the working tree; "
                         "needs a git work tree at --root")
    ap.add_argument("--base", default="HEAD",
                    help="the revision the bar gate compares against: what it "
                         "lacks is new (default HEAD)")
    ap.add_argument("--block", action="store_true",
                    help="exit 1 when a new pointer fails the bar gate (the "
                         "only finding that ever blocks); exit 2 when the "
                         "gate could not run")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"pointerscan: root does not exist: {args.root}", file=sys.stderr)
        return 2
    paths = args.paths or ["."]
    for raw in paths:
        p = (root / raw) if not Path(raw).is_absolute() else Path(raw)
        if not p.exists():
            print(f"pointerscan: path does not exist: {raw}", file=sys.stderr)
            return 2

    _suppressed: list[int] = []
    cov: dict = {"files": 0, "items": 0}
    try:
        findings = scan(paths, root, _suppressed, cov, staged=args.staged)
    except GitError as e:
        return report.broken("pointerscan", f"--staged cannot read the "
                                            f"index: {e}")
    bar = bar_scan(paths, root, base=args.base, staged=args.staged,
                   suppressed=_suppressed)
    findings = findings + bar.findings
    blocking = [f for f in findings if f.bar]
    rc = 0
    if args.block:
        rc = 2 if not bar.ran else (1 if blocking else 0)

    if args.json:
        print(json.dumps({"findings": report.finding_dicts(
            "pointerscan", findings, lambda f: f.detector),
            "coverage": report.coverage_dict(
                cov["files"], cov["items"], unit_key="items_checked"),
            "bar": {"ran": bar.ran, "note": bar.note, "base": bar.base,
                    "plane": bar.plane, "new_pointers": bar.new_pointers,
                    "blocking": args.block}},
            indent=2))
        return rc

    if not findings:
        print("✓ pointerscan clean — every queued-review pointer is "
              "refs-only and current.")
        print(f"  suppressed: {len(_suppressed)} pointer(s) by allow-marker")
        print(report.coverage_line(cov["files"], cov["items"],
                                   unit="item(s) checked",
                                   noun="roadmap file(s) opened"))
        print(bar.line())
        if args.block and not bar.ran:
            print("  --block: the bar gate did not run, so this is not a "
                  "pass.", file=sys.stderr)
        return rc

    grammar = [f for f in findings if f.detector == "grammar" and not f.bar]
    cycle = [f for f in findings if f.detector == "cycle"]
    state = [f for f in findings if f.detector == "state"]
    barf = [f for f in findings if f.bar]
    print(f"⚠ pointerscan: {len(findings)} finding(s) in queued-review "
          f"pointers ({len(grammar)} grammar · {len(cycle)} cycle state · "
          f"{len(state)} queue state · {len(barf)} review bar).")
    print()
    for f in findings:
        tag = "bar" if f.bar else f.detector
        print(report.with_id(f"  {f.path}:{f.line}  [{tag}] {f.reason}",
                             "pointerscan", f.detector))
        print(f"      {f.excerpt}")
    print()
    if grammar:
        print("  GRAMMAR. The pointer is refs only — the delta, the intent "
              "record, the tier,")
        print("  and the pass type. An evaluative account belongs in the intent "
              "record, where")
        print("  the reviewer's deferral discipline governs when it is read; in "
              "the pointer it")
        print("  steers the pass before a brief exists to defer it.")
        print("  A delta is named by path and a bound (a commit range, or the "
              "hashes listed as")
        print("  the delta); \"the commits citing X\" alone misses a commit "
              "that touches the paths")
        print("  and does not cite X.")
    if cycle:
        print("  CYCLE STATE. The item asserts a review is owed and carries the "
              "verdict of the")
        print("  review that ran. Say which state it is actually in — "
              "reviewed, ruled, applied")
        print("  — so the next session reads the queue and not the residue.")
    if state:
        print("  QUEUE STATE. The queued glyph on a state line means a review "
              "is queued and its")
        print("  pass has not returned a verdict — it is what a session counts "
              "to size the queue")
        print("  (board legend, 130/020). The commit that lands a verdict takes "
              "it off; a review")
        print("  still to run wears it, or the count misses it.")
    if barf:
        print("  REVIEW BAR. A new queued pass is queued on grounds: the intent "
              "record the")
        print("  pointer names carries lines `Commitment:`, `Worst failure:` "
              "and `Why the floor")
        print("  misses it:` (REVIEW.md, Whether work earns a review at all), "
              "or `review: not")
        print("  warranted — <grounds>`; and a subject with an open, unbriefed "
              "pass has that")
        print("  pointer widened, not a second one opened.")
    print()
    if args.block:
        print("  BLOCKING (--block): a new pointer that fails the review bar "
              "fails the commit;")
        print("  every other finding above stays advisory.")
    else:
        print("  ADVISORY ONLY — this never fails a build. A pointer is "
              "fixable in the commit")
        print("  that writes it, which is the one moment the fix costs "
              "nothing. Genuinely fine?")
    print(f"  Put `{ALLOW_MARKER} <reason>` in the item"
          + (" (`pointerscan:allow:grammar:` for a bar finding)."
             if barf else "."))
    # 115/130: the findings path says what it covered too, not only a clean run.
    print(report.coverage_line(cov["files"], cov["items"],
                               unit="item(s) checked",
                               noun="roadmap file(s) opened"))
    print(bar.line())
    if args.block and not bar.ran:
        print("  --block: the bar gate did not run, so this is not a pass.",
              file=sys.stderr)
    return rc


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""pointerscan — a queued-review pointer says only what it may, and only what is
still true.

TWO FAILURES, ONE PARSE
------------------------
`ROADMAP.md`'s own preamble states the pointer's ceiling: **refs only** — name
the delta and the intent record, carry no evaluative account, because the
account belongs in the session record where the reviewer's deferral discipline
governs when it is read. `REVIEW.md` rule 4 states the same ceiling at the point
a pointer is written.

Two things go wrong with a pointer, and one parse answers both:

  1. GRAMMAR — *what may it say*. A pointer that seeds the reviewer's first
     question steers the pass it is queuing. Recorded three times; the third
     instance was written hours after its author read the finding recording the
     first two, in the same file. Three instances of a trivial failure is a
     defect in the system producing it, which is the argument for a forcing
     function rather than a fourth restatement.
  2. CYCLE STATE — *is it still true*. An item asserting a review is owed while
     the same item carries the verdict of the review that ran is a mechanical
     contradiction. Five such residues came out of one commit; a sixth was
     still standing when this tool was built and is what it found on day one.

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
  * It needs no cross-file I/O, so it reads staged content honestly and has no
    plane seam.

**Stated residual, not defended against:** a pointer that is stale against a
verdict it never links is invisible here. That is the price of refusing the
title key, and it is the cheaper error — a missed warning, not a false one on
every healthy edit.

ADVISORY, ALWAYS
----------------
Findings exit 0. Both detectors read judgement-adjacent text and the honest
posture is to warn at the one moment the fix is free: a pointer is fixable in
the commit that writes it. A line carrying `pointerscan:allow: <reason>`
anywhere in an item exempts it — the same greppable hatch as the sibling
scanners.

Exit codes:
  0  scanned (clean or with findings — this never blocks)
  2  environment error (a path that does not exist)

Usage:
  pointerscan --root . docs        scan the roadmaps under docs/
  pointerscan --root . .           scan the whole tree for roadmap files
  pointerscan --json               machine-readable
  pointerscan --selftest           prove the rules on the recorded specimens
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# The files this reads. The pointer grammar is a ROADMAP convention; nothing
# else in the tree carries it, and pointing this at prose would be the
# fires-on-every-author failure the 0820 record rejected.
ROADMAP_NAMES = ("ROADMAP.md",)

ALLOW_MARKER = "pointerscan:allow:"
ALLOW_BASE = "pointerscan:allow"

# GUARDS.md rule (c): a marker only counts with a colon and a non-empty reason,
# so prose that merely mentions the marker text exempts nothing. Tightened
# 2026-08-05 — a bare marker used to exempt on a substring match.
ALLOW_RX = re.compile(
    r"\b" + re.escape(ALLOW_BASE) + r"(?::(?P<kind>[A-Za-z0-9_-]+))?:[ \t]*(?P<reason>[\w\"\'“‘])")


def parse_allow(text: str) -> str | None:
    """The scope of the allow-marker, or None if there is no reasoned one.

    `""` means the whole item. A marker with no reason returns None — a
    mention, not an exemption."""
    m = ALLOW_RX.search(text)
    if not m:
        return None
    return m.group("kind") or ""


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


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    detector: str      # "grammar" | "cycle"
    reason: str
    excerpt: str


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


def scan_text(text: str, path: str = "",
              suppressed: list[int] | None = None) -> list[Finding]:
    """Pure, so the selftest and the tests drive it with no filesystem.

    `suppressed` collects one entry per item an allow-marker exempted, so the
    caller can report the subtraction (`method/GUARDS.md`, rule b) instead of
    printing the same clean tick either way."""
    out: list[Finding] = []
    for item in parse_items(text):
        if parse_allow(item.body) is not None:
            if suppressed is not None and is_pointer(item.marker, item.body):
                suppressed.append(1)
            continue
        if not is_pointer(item.marker, item.body):
            continue
        excerpt = " ".join(item.body.split())[:120]
        for reason in grammar_findings(item.body):
            out.append(Finding(path, item.line, "grammar", reason, excerpt))
        for reason in cycle_findings(item.body):
            out.append(Finding(path, item.line, "cycle", reason, excerpt))
    return out


def roadmaps(paths: list[str], root: Path) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        p = (root / raw) if not Path(raw).is_absolute() else Path(raw)
        if p.is_file():
            if p.name in ROADMAP_NAMES:
                found.append(p)
            continue
        for sub in sorted(p.rglob("*.md")):
            if any(part in SKIP_DIRS for part in sub.parts):
                continue
            if sub.name in ROADMAP_NAMES:
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


def scan(paths: list[str], root: Path,
         suppressed: list[int] | None = None) -> list[Finding]:
    out: list[Finding] = []
    for p in roadmaps(paths, root):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if parse_allow(text.split("\n")[0]) is not None:
            if suppressed is not None:
                suppressed.append(1)
            continue
        try:
            rel = p.resolve().relative_to(root.resolve()).as_posix()
        except ValueError:
            rel = p.as_posix()
        out.extend(scan_text(text, rel, suppressed))
    return out


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

# Prose ABOUT pointers, in an ordinary work item. The scope must not sweep it in
# — this is the shape of this build's own funding entry.
_SPEC_PROSE = (
    "- [ ] **Mechanise the pointer grammar.** All five said \"review queued\"\n"
    "      when the review had run. Is this the same rung the 0820 record\n"
    "      rejected? The first question the work must answer, not assume.\n")


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
    findings = scan(paths, root, _suppressed)

    if args.json:
        print(json.dumps({"findings": [asdict(f) for f in findings]}, indent=2))
        return 0

    if not findings:
        print("✓ pointerscan clean — every queued-review pointer is "
              "refs-only and current.")
        print(f"  suppressed: {len(_suppressed)} pointer(s) by allow-marker")
        return 0

    grammar = [f for f in findings if f.detector == "grammar"]
    cycle = [f for f in findings if f.detector == "cycle"]
    print(f"⚠ pointerscan: {len(findings)} finding(s) in queued-review "
          f"pointers ({len(grammar)} grammar · {len(cycle)} cycle state).")
    print()
    for f in findings:
        print(f"  {f.path}:{f.line}  [{f.detector}] {f.reason}")
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
    if cycle:
        print("  CYCLE STATE. The item asserts a review is owed and carries the "
              "verdict of the")
        print("  review that ran. Say which state it is actually in — "
              "reviewed, ruled, applied")
        print("  — so the next session reads the queue and not the residue.")
    print()
    print("  ADVISORY ONLY — this never fails a build. A pointer is fixable "
          "in the commit")
    print("  that writes it, which is the one moment the fix costs nothing. "
          "Genuinely fine?")
    print(f"  Put `{ALLOW_MARKER} <reason>` in the item.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

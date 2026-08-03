#!/usr/bin/env python3
"""harvestscan — did a roadmap item get harvested, or did it just vanish?

THE GAP THIS FILLS
-------------------
`sizescan` already catches the two adjacent failures in this family:

  - a completed `[x]` item left on the hot path (cold-content), and
  - a live `[ ]` / `[~]` / `⏳` marker buried in an archive (harvest integrity).

There is a third, and it is the only one that loses work: **an item REMOVED from
ROADMAP.md that arrives nowhere.** It passes every check that exists, because
every check reads a file as it stands and this failure is only visible as a
difference between two versions of it.

It is not hypothetical. On 2026-07-25 a session removed 185 lines of roadmap
sections having compared HEADING NAMES ONLY, asserted "duplicates" in the commit
message without diffing a single body, and one of those sections was a genuine
loss — a completed item whose only roadmap trace went with it. Git remembered
the text. Git does not remember that the work was supposed to happen, and **a
roadmap item that vanishes means the work does not get done**, which is closer
to irreversible than the mechanism suggests.

WHY IT FINGERPRINTS CONTENT, NEVER TITLES
------------------------------------------
The obvious implementation — match items by their heading or first line — was
measured and rejected. The 2026-07-26 audit walked 362 commits and found
title-matching has a near-total false-positive rate, for a structural reason: a
healthy roadmap **rewrites titles and re-homes items constantly**, and to a
title-matcher a retitle is indistinguishable from a deletion. A guard that fires
on every healthy edit is a guard that gets `allow`-markered into silence, which
is worse than no guard because it looks like cover.

So an item is fingerprinted by the *bag of distinctive words in its body*, and a
removed item counts as SURVIVING if a sufficiently similar body exists in one of
the stores named in `DEFAULT_SURVIVOR_STORES` — the roadmap itself (re-homed or
retitled), the archive (harvested), or a session/review record (written up).
Only an item with no surviving relative in those is reported.

That list is stated exactly, and it is stated because it used to be a claim
rather than a fact: the docstring said "anywhere in the tracked records … or any
other record" while the search was two files (B4 cold pass, HV3). Two things had
to change for the widening to be real. The file list, obviously — and the
extractor, less obviously: a harvest into a session record is almost never a
checkbox item, it is a paragraph, so widening the files alone was **measurably
inert**. Replayed over the whole history it changed the firing set by exactly
nothing until `paragraphs()` was applied to the destinations.

Measured over the 429 commits touching the records, with the pointer exclusion
held constant, so the two folds can be read apart (`--replay`, no gate):

  as it shipped: items only, two files ........ fired on 107 (24.9%), 160 items
  + wider file list, items only ............... fired on 107 (24.9%), 160 items
  + prose in the destinations ................. fired on  88 (20.5%), 132 items

and the HV2 fold — the widened pointer exclusion — is worth a further 3 commits
and 5 items on top (85, 19.8%, 127). Under the shipped gate all of that
collapses to one number: 6 in scope, 3 warn, and 15 items rather than 17.

MEASURED, SHELVED, THEN WIRED — SCOPED AND ADVISORY
----------------------------------------------------
The first verdict on this tool was its author's own: *do not wire, not even
advisory*, the counsel `stampscan` earned. It rested on this measurement, over
all 390 commits touching `docs/ROADMAP.md`, each replayed against its parent as
the hook would see it:

  raw body, Jaccard ≥ 0.6 .................. fired on 165 (42.3%), 257 items
  + bookkeeping stripped, containment ...... fired on 120 (30.8%), 179 items
  + review pointers excluded ............... fired on 105 (26.9%), 158 items

Each step fixed a *cause* rather than moving the threshold, and each bought less
than the last. Roughly one roadmap commit in four would warn — the rate that
gets a guard `allow`-markered into silence.

**That verdict was OVERTURNED** by its own cold pass (2026-07-29, HV1) and
ruled by the principal the same day. The finding: the verdict generalised from
the *unscoped* measurement, and the entry listed three scoped variants without
measuring any. Measured over the same history, scoping the guard to
**net-bulk-delete roadmap commits** leaves **6 in-scope commits, of which 3
warn** — the motivating incident, and two mass harvests condensing 9 and 12
items into the archive, which are exactly the diffs that merit eyes. ~0.8% of
commits, against the 26.9% that grounded the fatigue argument.

The pass also killed the entry's *first-ranked* variant: scoping to commits
that only DELETE would have missed the incident, which carried 48 additions
alongside its 184 deletions. Net line loss is the workable scope, not strict
delete-only.

Re-measured at this landing, over the 429 commits now touching the records:
**6 in scope, 3 warn, 15 items** — `dd7fcb74` (the incident, 2 items) and two
mass harvests (4 and 9). The pass's figures reproduce. Run `--replay
--only-bulk-deletes` to reproduce them again rather than trusting this line.

So it is in the registry, **warn-only and never blocking** — the threshold below
is honestly ungrounded, and a check whose constant cannot be grounded may not
red a build. Tuning `SURVIVAL_SIMILARITY` to improve a number remains off the
table; the scope came from measuring a variant, not from moving a line.

WHAT THE HOOK ACTUALLY READS (HV4)
-----------------------------------
The two planes read different things, and saying "staged/working" as if they
were interchangeable was the wording this tool shipped with:

  --staged   the INDEX — what is about to be committed. Old text comes from
             HEAD, survivors from the staged content. This is the hook plane.
  default    the WORKING TREE, against `--against` (HEAD by default). This is
             the hand-run and CI form.

Usage:
  harvestscan --root . --staged --only-bulk-deletes    the hook plane
  harvestscan --root . .                    working tree vs HEAD, no gate
  harvestscan --against <rev>               compare against another revision
  harvestscan --replay                      re-measure over the whole history
  harvestscan --json                        machine-readable
  harvestscan --selftest                    prove the matching logic, offline
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
# Imported for ONE function: what makes an item a queued-review pointer. That
# question now has a single statement (`pointerscan`'s docstring settles it on
# the corpus), and the exclusion below is only safe while the items it forgives
# here are the items policed there. A second, narrower copy lived in this file
# and provably missed two of the four recorded pointer shapes — B4 cold pass,
# HV2, which named the dependency and required them to build together.
import pointerscan  # noqa: E402

# The records this WATCHES — an item removed from one of these is what the
# guard is about.
DEFAULT_RECORDS = ("docs/ROADMAP.md", "docs/ROADMAP-DONE.md")

# Where a removed item may legitimately have LANDED. Wider than the watched set
# (B4 cold pass, HV3): the docstring claimed "anywhere in the tracked records"
# while the search was exactly the two files above, so an item harvested into a
# session record or a review verdict read as vanished. Directories are walked
# for their `.md` files; the effect of widening is measured by `--replay`.
DEFAULT_SURVIVOR_STORES = DEFAULT_RECORDS + ("docs/sessions", "docs/reviews")

# The scope that made this wireable (HV1, ruled by the principal 2026-07-29 on
# the cold pass's measurement): a roadmap commit that sheds at least this many
# NET lines. Not fitted here — it is a recorded ruling, and the number came from
# measuring a variant the shelved entry had named but never measured. Net, not
# delete-only: the incident this guard exists for was +48/−184, and a
# delete-only scope would have missed it.
NET_BULK_DELETE_LINES = 50

# The gate is measured on the CURRENT-TRUTH record alone, not on the watched set.
# Measuring both together nets a harvest to nothing — lines leave `ROADMAP.md`
# and land in `ROADMAP-DONE.md` in the same commit — which would exempt exactly
# the bulk moves the guard exists to look at. Measured: gating on the pair puts
# 1 commit in scope across the whole history; gating on `ROADMAP.md` puts 6 in
# scope, reproducing the cold pass's figure. The ruling says "net lines removed
# from ROADMAP.md" and it says it for this reason.
GATE_RECORDS = ("docs/ROADMAP.md",)

# A list item: the tri-state checkbox grammar, plus the queued-review marker.
ITEM_RE = re.compile(r"^\s*-\s+(\[[ x~]\]|⏳)\s*(.*)$")
# Continuation lines of the same item — indented, not themselves a new item.
CONT_RE = re.compile(r"^\s{4,}\S")

# Words carrying no distinguishing signal. Kept SHORT on purpose: an aggressive
# stop-list is itself a tuning surface, and the shingle comparison already
# discounts ubiquitous terms by sheer overlap.
NOISE = frozenset("""
a an the and or but if then than that this these those of to in on at by for
with from as is are was were be been being it its it's not no so such which
who whom whose what when where how why all any each every some more most other
""".split())

# BOOKKEEPING, not subject. Measured over 390 roadmap commits: fingerprinting
# the raw body fired on 42% of them, and the samples showed why — an item that
# moves from "⏳ review queued (claimed …, wt: …)" to "🎯 REVIEWED … verdict"
# has barely changed as a piece of WORK while most of its words changed. That is
# the title-matching trap one level in: matching on the part that churns.
# Stripped before fingerprinting so the comparison sees the item's subject.
STAMP_RE = re.compile(
    r"\(claimed[^)]*\)"                       # (claimed 2026-07-28-1233, wt: x)
    r"|\bwt:\s*\S+"                           # bare worktree refs
    r"|\b\d{4}-\d{2}-\d{2}(?:-\d{3,4})?\b"    # ISO dates, with optional -HHMM
    r"|\b\d{3,4}\s*UTC\b"
    r"|\b[0-9a-f]{7,40}\b"                    # commit shas
    r"|[⏳🎯📦🚩🔎💡🛑🔥⚠️✅❌🎉🚀]",
    re.IGNORECASE)
BOOKKEEPING = frozenset("""
claimed claim queued queue review reviewed reviewer verdict pass passes cold
rule ruled ruling session sessions record records roadmap done landed landing
commit commits worktree merged applied application terminal cycle closed close
major minor note notes findings finding
""".split())

# Containment at or above which a removed item counts as having survived
# somewhere. UNGROUNDED, and left that way on purpose: it is a tuning constant,
# and moving it to improve the measured firing rate would be fitting a number to
# the corpus it is measured on. The firing rate came down by fixing causes (see
# the docstring's table); it did not come down enough, and the honest response
# to that is not to adjust this line.
SURVIVAL_SIMILARITY = 0.6
# Below this many distinctive words an item cannot be fingerprinted reliably at
# all, so it is skipped rather than guessed at. A one-line item is exactly the
# kind of thing a healthy roadmap rewrites wholesale.
MIN_SIGNAL_WORDS = 8


def normalise(text: str) -> list[str]:
    """An item's distinctive words: lower-cased, markdown and punctuation
    stripped, noise words dropped. Order is discarded deliberately — a rewritten
    item usually keeps its vocabulary while losing its phrasing."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # links -> label
    text = re.sub(r"`[^`]*`", " ", text)                    # code spans
    text = STAMP_RE.sub(" ", text)                          # claim/date stamps
    text = re.sub(r"[*_~#>]", " ", text)                    # emphasis, headings
    text = re.sub(r"[^\w\s-]", " ", text)                   # residual punctuation
    return [w for w in text.lower().split()
            if len(w) > 2 and w not in NOISE and w not in BOOKKEEPING]


def similarity(a: list[str], b: list[str]) -> float:
    """How much of `a` survives in `b` — CONTAINMENT, not Jaccard.

    Jaccard was the first shape and it was wrong for this corpus in a way the
    measurement made obvious: roadmap items routinely get ABSORBED into larger
    ones — merged with a sibling, or rewritten with three paragraphs of new
    reasoning attached. Jaccard punishes that by the size of what was added, so
    a healthy expansion reads as a deletion. Containment asks the question the
    guard actually cares about — *is this item's substance still present
    somewhere* — and is indifferent to how much grew around it.

    Order is discarded deliberately: a rewritten item usually keeps its
    vocabulary while losing its phrasing."""
    sa, sb = set(a), set(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa)


def parse_items(text: str) -> list[tuple[int, str, str]]:
    """(line number, marker, body) for every list item, continuations folded in.

    The body is what gets fingerprinted, so an item's sub-bullets and its
    explanatory paragraphs count as part of it — which is the whole point, since
    the title is exactly the part that gets rewritten. The marker is carried
    because one of them means "this is not work" — see `is_pointer`."""
    items: list[tuple[int, str, str]] = []
    current: list[str] | None = None
    start = 0
    marker = ""
    for n, line in enumerate(text.splitlines(), 1):
        m = ITEM_RE.match(line)
        if m:
            if current is not None:
                items.append((start, marker, " ".join(current)))
            current, start = [m.group(2)], n
            marker = m.group(1)
        elif current is not None and CONT_RE.match(line):
            current.append(line.strip())
        elif current is not None and not line.strip():
            continue          # a blank line inside an indented item body
        elif current is not None:
            items.append((start, marker, " ".join(current)))
            current = None
    if current is not None:
        items.append((start, marker, " ".join(current)))
    return items


def is_pointer(marker: str, body: str) -> bool:
    """Is this a queued-review POINTER rather than a unit of work?

    Not a heuristic dodge — it follows from what a pointer IS. The ROADMAP's own
    preamble defines it as **refs only**: it names a delta and an intent record
    and carries no evaluative account, because the account lives in the session
    record so a taker meets the work cold. An item that by definition holds no
    work-content cannot lose any when it goes, and it is *supposed* to disappear
    when its cycle closes — that is the mechanism working.

    Measured: pointers dominated the noise, because a closing cycle deletes the
    pointer and writes a differently-worded record, which is indistinguishable
    from a loss to anything reading words alone.

    The TEST itself is `pointerscan`'s, not this file's. The copy that lived
    here read the marker or the item's first six words, and the recorded corpus
    has four pointer shapes of which that saw two — so the exclusion was
    forgiving items nothing then policed, which is the fail-open this whole
    programme is about (B4 cold pass, HV2)."""
    return pointerscan.is_pointer(marker, body)


def git_show(root: Path, rev: str, rel: str) -> str | None:
    r = subprocess.run(["git", "-C", str(root), "show", f"{rev}:{rel}"],
                       capture_output=True, text=True, check=False)
    return r.stdout if r.returncode == 0 else None


# `source` names WHICH version of the tree to read, and there are exactly three.
# Held as one vocabulary because the plane confusion HV4 found came from having
# no name for the distinction at all.
WORKTREE = "worktree"
INDEX = "index"


def read_source(root: Path, rel: str, source: str) -> str | None:
    """One file, from the working tree, the index, or a revision."""
    if source == WORKTREE:
        p = root / rel
        try:
            return p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None
    if source == INDEX:
        return git_show(root, "", rel)      # `git show :path` — the staged blob
    return git_show(root, source, rel)


def list_markdown(root: Path, store: str, source: str) -> list[str]:
    """Tracked `.md` files under a store, as of `source`.

    A store may be a file or a directory. Tracked only: an untracked scratch
    file is not a record, and letting one count as a survivor would be a guard
    that passes on content nobody is committing."""
    if source in (WORKTREE, INDEX):
        cmd = ["git", "-C", str(root), "ls-files", "--", store]
    else:
        cmd = ["git", "-C", str(root), "ls-tree", "-r", "--name-only",
               source, "--", store]
    r = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return []
    return [line for line in r.stdout.splitlines() if line.endswith(".md")]


def paragraphs(text: str) -> list[str]:
    """Blank-line-separated prose blocks.

    Needed because a harvest into a session record or a verdict is almost never
    a checkbox item — it is a paragraph in a write-up. Widening the survivor
    file list without this was measurably inert: over the whole history it
    changed the firing set by exactly nothing, because the extractor was still
    only reading list items and those stores contain almost none.

    Applied to the harvest DESTINATIONS only, never to the watched roadmaps.
    There the item grammar is the unit, and fingerprinting the roadmap's own
    prose would let a removed item "survive" in a section heading's narration
    — a false negative in the one file the guard exists to watch."""
    blocks = re.split(r"\n\s*\n", text)
    return [b for b in blocks if b.strip()]


def survivors(root: Path,
              stores: tuple[str, ...] = DEFAULT_SURVIVOR_STORES,
              source: str = WORKTREE,
              watched: tuple[str, ...] = DEFAULT_RECORDS) -> list[list[str]]:
    """Every surviving body in the survivor stores, fingerprinted.

    `source` decides which version is authoritative, and the hook's answer is
    the INDEX: the question at commit time is whether the item survives in what
    is about to be committed, which is neither HEAD nor an unstaged edit (HV4).
    """
    out: list[list[str]] = []
    seen: set[str] = set()
    for store in stores:
        for rel in list_markdown(root, store, source):
            if rel in seen:
                continue
            seen.add(rel)
            text = read_source(root, rel, source)
            if text is None:
                continue
            out.extend(normalise(body) for _, _, body in parse_items(text))
            if rel not in watched:
                out.extend(normalise(b) for b in paragraphs(text))
    return out


def net_line_loss(root: Path, rels: tuple[str, ...],
                  old: str, new: str = INDEX) -> int:
    """Lines removed minus lines added across `rels`, between two versions.

    `new` takes the same three-valued vocabulary as `read_source`: the INDEX
    (the hook's question — what is this commit about to shed?), the WORKTREE, or
    a revision."""
    cmd = ["git", "-C", str(root), "diff", "--numstat"]
    if new == INDEX:
        cmd += ["--cached", old]
    elif new == WORKTREE:
        cmd += [old]
    else:
        cmd += [old, new]
    cmd += ["--", *rels]
    r = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return 0
    loss = 0
    for line in r.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 3 or "-" in (parts[0], parts[1]):
            continue                    # binary, or an unparseable row
        loss += int(parts[1]) - int(parts[0])
    return loss


def vanished(old_text: str, alive: list[list[str]]) -> list[tuple[int, str]]:
    """Items in `old_text` with no sufficiently similar survivor anywhere.

    Pure, so the selftest drives it offline."""
    gone: list[tuple[int, str]] = []
    for line, marker, body in parse_items(old_text):
        if is_pointer(marker, body):
            continue
        finger = normalise(body)
        if len(finger) < MIN_SIGNAL_WORDS:
            continue
        if any(similarity(finger, other) >= SURVIVAL_SIMILARITY
               for other in alive):
            continue
        gone.append((line, body))
    return gone


def scan(root: Path, rev: str,
         records: tuple[str, ...] = DEFAULT_RECORDS,
         stores: tuple[str, ...] = DEFAULT_SURVIVOR_STORES,
         source: str = WORKTREE) -> list[dict]:
    alive = survivors(root, stores, source, records)
    findings: list[dict] = []
    for rel in records:
        old = git_show(root, rev, rel)
        if old is None:
            continue        # new file, or not tracked at that revision
        for line, body in vanished(old, alive):
            findings.append({"file": rel, "line": line,
                             "excerpt": body[:160].strip()})
    return findings


def replay(root: Path, records: tuple[str, ...], stores: tuple[str, ...],
           gate: int | None,
           gate_records: tuple[str, ...] = GATE_RECORDS) -> dict:
    """Re-measure over the whole history: every commit touching the watched
    records, judged against its parent exactly as the hook would see it.

    This SHIPS, unlike the measurement it reproduces. The B4 cold pass had to
    rebuild the harness from the tool's pure functions to check the recorded
    figures, and HV3 requires the effect of widening the survivor search to be
    measured before landing — neither is possible against a harness that lives
    only in a session's scratch space."""
    r = subprocess.run(
        ["git", "-C", str(root), "log", "--format=%H", "--", *records],
        capture_output=True, text=True, check=False)
    revs = r.stdout.split()
    in_scope = fired = items = 0
    firing: list[tuple[str, int, int]] = []
    for rev in revs:
        parent = f"{rev}^"
        if gate is not None:
            loss = net_line_loss(root, gate_records, parent, rev)
            if loss < gate:
                continue
        in_scope += 1
        alive = survivors(root, stores, rev, records)
        n = 0
        for rel in records:
            old = git_show(root, parent, rel)
            if old is None:
                continue
            n += len(vanished(old, alive))
        if n:
            fired += 1
            items += n
            firing.append((rev[:7], n,
                           net_line_loss(root, gate_records, parent, rev)))
    return {"commits": len(revs), "in_scope": in_scope, "fired": fired,
            "items": items, "firing": firing}


def _selftest() -> int:
    fails: list[str] = []

    def check(label: str, got, want) -> None:
        if got != want:
            fails.append(f"{label}: expected {want}, got {got}")

    body = ("**Schedule the conformance check.** floorfleet is the instrument "
            "that turns hoping the policy propagated into knowing it did, and "
            "nothing runs it automatically today.")
    old = f"- [ ] {body}\n"

    # Harvested verbatim: survives.
    check("verbatim harvest",
          len(vanished(old, [normalise(body)])), 0)

    # Retitled and lightly reworded, same subject: must still count as
    # surviving. This is the case that makes title-matching useless.
    reworded = ("**Put the conformance check on a schedule.** The floorfleet "
                "instrument turns hoping policy propagated into knowing it "
                "did, and today nothing runs it automatically.")
    check("retitled + reworded survives",
          len(vanished(old, [normalise(reworded)])), 0)

    # Genuinely gone: nothing resembling it anywhere.
    check("vanished is reported",
          len(vanished(old, [normalise("something entirely unrelated about "
                                       "licence classifiers and SPDX headers "
                                       "in vendored source files")])), 1)

    # Too short to fingerprint: skipped rather than guessed at.
    check("short item skipped", len(vanished("- [ ] fix it\n", [])), 0)

    # Continuation lines are part of the item body, not separate items.
    multi = "- [ ] title here\n      and its indented continuation line\n"
    check("continuations fold in", len(parse_items(multi)), 1)

    # The tri-state grammar and the queued marker are all items.
    grammar = "- [ ] one\n- [x] two\n- [~] three\n- ⏳ four\n"
    check("all four markers parse", len(parse_items(grammar)), 4)

    # The pointer exclusion is pointerscan's test now (HV2). Pinned here so a
    # change over there that narrows the scope shows up as this tool's problem
    # too — the exclusion is only safe while the two agree.
    check("marker-shaped pointer excluded", is_pointer("⏳", "anything"), True)
    check("obligation in an emphasis run excluded",
          is_pointer("[ ]", "**ADR 0008 review owed** — self-authored."), True)
    check("an ordinary work item is not a pointer",
          is_pointer("[ ]", "**Schedule the conformance check.** Nothing runs "
                            "it automatically today."), False)

    check("identical is 1.0", similarity(["a", "b"], ["a", "b"]), 1.0)
    check("disjoint is 0.0", similarity(["a"], ["b"]), 0.0)
    check("empty is 0.0", similarity([], ["a"]), 0.0)

    for f in fails:
        print(f"harvestscan selftest FAIL: {f}", file=sys.stderr)
    print(f"harvestscan selftest: {'FAILED' if fails else 'ok'} "
          f"({len(fails)} failure(s))")
    return 1 if fails else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="harvestscan", description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*", help="ignored; accepted for symmetry "
                                             "with the other scanners")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--against", default="HEAD",
                    help="revision to compare the working records against")
    ap.add_argument("--records", action="append",
                    help="record store to WATCH (repeatable; default: "
                         "docs/ROADMAP.md + docs/ROADMAP-DONE.md)")
    ap.add_argument("--survivor-store", action="append",
                    help="file or directory a removed item may legitimately "
                         "have landed in (repeatable; default: the watched "
                         "records + docs/sessions + docs/reviews)")
    ap.add_argument("--staged", action="store_true",
                    help="read the INDEX — what is about to be committed — "
                         "rather than the working tree. The hook plane.")
    ap.add_argument("--only-bulk-deletes", action="store_true",
                    help=f"report nothing unless the change sheds at least "
                         f"{NET_BULK_DELETE_LINES} net lines from the watched "
                         f"records (HV1, the scope that made this wireable)")
    ap.add_argument("--replay", action="store_true",
                    help="re-measure over every commit touching the records")
    ap.add_argument("--json", action="store_true", help="machine-readable")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"harvestscan: root does not exist: {args.root}", file=sys.stderr)
        return 2

    records = tuple(args.records) if args.records else DEFAULT_RECORDS
    stores = (tuple(args.survivor_store) if args.survivor_store
              else records + tuple(s for s in DEFAULT_SURVIVOR_STORES
                                   if s not in DEFAULT_RECORDS))

    if args.replay:
        gate = NET_BULK_DELETE_LINES if args.only_bulk_deletes else None
        m = replay(root, records, stores, gate)
        if args.json:
            print(json.dumps(m, indent=2))
            return 0
        scope = (f"net loss ≥ {gate}" if gate is not None else "every commit")
        print(f"harvestscan replay — {m['commits']} commit(s) touch the "
              f"records; scope: {scope}")
        print(f"  in scope: {m['in_scope']}   fired: {m['fired']}   "
              f"items: {m['items']}")
        for sha, n, loss in m["firing"]:
            print(f"    {sha}  {n} item(s)   net −{loss} lines")
        return 0

    source = INDEX if args.staged else WORKTREE
    if args.only_bulk_deletes:
        loss = net_line_loss(root, GATE_RECORDS, args.against, source)
        if loss < NET_BULK_DELETE_LINES:
            if args.json:
                print(json.dumps({"against": args.against,
                                  "records": list(records),
                                  "net_line_loss": loss,
                                  "in_scope": False, "findings": []}, indent=2))
            else:
                print(f"✓ harvestscan not in scope — this change sheds "
                      f"{loss} net line(s) from the records, under the "
                      f"{NET_BULK_DELETE_LINES}-line bulk-deletion gate.")
            return 0

    findings = scan(root, args.against, records, stores, source)

    if args.json:
        print(json.dumps({"against": args.against, "records": list(records),
                          "survivor_stores": list(stores),
                          "source": source, "findings": findings}, indent=2))
        return 0

    if not findings:
        print("✓ harvestscan clean — every removed roadmap item still exists "
              "somewhere.")
        return 0

    print(f"⚠ harvestscan: {len(findings)} removed item(s) with no surviving "
          f"copy (vs {args.against}).")
    print()
    for f in findings:
        print(f"  {f['file']}:{f['line']}  {f['excerpt']}")
    print()
    print("  These were removed and nothing resembling them exists in the "
          "records now.")
    print("  If that is a harvest, the destination is missing. If it is a "
          "deletion, git")
    print("  remembers the text but not that the work was supposed to happen "
          "— which is")
    print("  the failure this checks for. Diff it before you commit, or say in "
          "the commit")
    print("  message what went and why.")
    print()
    print("  ADVISORY ONLY — this never fails a build. Its similarity "
          "threshold is a")
    print("  tuning constant that cannot be grounded, so it warns rather than "
          "blocks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

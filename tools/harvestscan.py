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
removed item counts as SURVIVING if a sufficiently similar body exists anywhere
in the tracked records — the same file (re-homed or retitled), the archive
(harvested), or any other record. Only an item whose content has no surviving
relative anywhere is reported.

MEASURED, AND DELIBERATELY NOT WIRED YET
-----------------------------------------
**Do not add this to the registry, not even advisory** — the same counsel
`stampscan` earned, for the same reason and on the same kind of evidence.

Measured over all 390 commits touching `docs/ROADMAP.md`, replaying each commit
against its parent exactly as the hook would see it:

  raw body, Jaccard ≥ 0.6 .................. fired on 165 (42.3%), 257 items
  + bookkeeping stripped, containment ...... fired on 120 (30.8%), 179 items
  + review pointers excluded ............... fired on 105 (26.9%), 158 items

Each step fixed a *cause* rather than moving the threshold, and each bought
less than the last. **Roughly one roadmap commit in four would warn**, and the
audit that motivated this item already established what that rate does: a guard
that fires on healthy edits gets `allow`-markered into silence, at which point
it is worse than absent because it looks like cover.

**The signal is real, though, and that is why this is shelved rather than
binned.** Replayed against `dd7fcb74` — the commit that removed 185 lines on a
heading-only comparison and lost a completed item — it reports 2 items,
including work that genuinely vanished. The detector works; the discriminator
does not yet.

**What would make it wireable**, in rough order of expected value: scope it to
commits that *only* delete (a commit rewriting a section is the noisy case and
is also the one a human is already looking at); compare against the merge-base
of a branch rather than the previous commit, so a multi-commit rewrite is judged
once at its end state rather than at every intermediate step; or narrow it to
items carrying a decision marker, since those are the ones whose loss costs
something. **None of those is a threshold change.** Tuning
`SURVIVAL_SIMILARITY` to make this number look better would be fitting a
constant to the corpus it is measured on, which this repo already has a name
for.

Until then it earns its keep run by hand before a deliberate bulk deletion —
which is the one moment the 2026-07-25 failure would have been caught.

Usage:
  harvestscan --root . .            compare staged/working records against HEAD
  harvestscan --against <rev>       compare against another revision
  harvestscan --json                machine-readable
  harvestscan --selftest            prove the matching logic, offline
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# The record stores this reasons about. A removed item may legitimately reappear
# in any of them, so all are searched for a survivor before anything is
# reported.
DEFAULT_RECORDS = ("docs/ROADMAP.md", "docs/ROADMAP-DONE.md")

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

    Not a heuristic dodge — it follows from what a `⏳` pointer IS. The ROADMAP's
    own preamble defines it as **refs only**: it names a delta and an intent
    record and carries no evaluative account, because the account lives in the
    session record so a taker meets the work cold. An item that by definition
    holds no work-content cannot lose any when it goes, and it is *supposed* to
    disappear when its cycle closes — that is the mechanism working.

    Measured: pointers dominated the noise, because a closing cycle deletes the
    pointer and writes a differently-worded record, which is indistinguishable
    from a loss to anything reading words alone."""
    if "⏳" in marker:
        return True
    lead = " ".join(body.split()[:6]).lower()
    return "review queued" in lead or "review owed" in lead


def git_show(root: Path, rev: str, rel: str) -> str | None:
    r = subprocess.run(["git", "-C", str(root), "show", f"{rev}:{rel}"],
                       capture_output=True, text=True, check=False)
    return r.stdout if r.returncode == 0 else None


def survivors(root: Path, records: tuple[str, ...]) -> list[list[str]]:
    """Every item body currently in the record stores, fingerprinted.

    Read from the WORKING TREE, not from HEAD: this runs at commit time, and the
    question is whether the item survives in what is about to be committed."""
    out: list[list[str]] = []
    for rel in records:
        p = root / rel
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        out.extend(normalise(body) for _, _, body in parse_items(text))
    return out


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
         records: tuple[str, ...] = DEFAULT_RECORDS) -> list[dict]:
    alive = survivors(root, records)
    findings: list[dict] = []
    for rel in records:
        old = git_show(root, rev, rel)
        if old is None:
            continue        # new file, or not tracked at that revision
        for line, body in vanished(old, alive):
            findings.append({"file": rel, "line": line,
                             "excerpt": body[:160].strip()})
    return findings


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
                    help="record store to check (repeatable; default: "
                         "docs/ROADMAP.md + docs/ROADMAP-DONE.md)")
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
    findings = scan(root, args.against, records)

    if args.json:
        print(json.dumps({"against": args.against, "records": list(records),
                          "findings": findings}, indent=2))
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

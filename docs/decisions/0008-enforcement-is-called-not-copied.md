# 0008 — enforcement is called, not copied; and conformance is enumerated

**Status**: accepted • **Date**: 2026-07-26

review: queued — `docs/reviews/` pointer owed; the author of this change may not
review it (REVIEW.md rule 4). The sharpest thing to aim a reviewer at: whether
moving every repo onto a floating `@main` caller trades a slow, silent failure
for a fast, loud, estate-wide one — and whether that trade is right.

## Context

Mike, 2026-07-25: *"some of the policy we have written into atelier, things we
specifically made policy as code because otherwise doctrine may not be enforced,
is not propagating to child repos."*

He was right, and the measurement was worse than the report. Of 13 children, 12
carried a `floor.yml` frozen at their scaffold date and therefore ran **none** of
the five checks added since — `sizescan`, `datescan`, `wrapscan`, `spellscan`,
`reviewscan`. Every guard in every clone was additionally machine-local, because
`.git/hooks/` is untracked.

The trigger was concrete. `sizescan`'s harvest-integrity gate was built on
2026-07-22 after a real incident and CI-wired in atelier. Three days later a
child session spent hours reconstructing, by hand, seven live items buried in
that child's archive. Pointed at the child for the first time, the existing gate
found exactly those seven in one run. Two were security findings.

The scanners were never the problem: they are zero-dep, tested, fetched fresh
from `atelier@main` at CI time, and `sizescan` was explicitly written to travel
(archive stores matched by basename *"so the convention travels to children"*).
**Code was one-source; policy was vendored.** 247 lines of `floor.yml` per repo,
plus four hard-coded `run_scan` lines per clone, each naming the scanners of the
day.

The failure is already named in our own doctrine and we applied it to the wrong
half. `PROPAGATION.md` prescribes **thin anchor, fat pointer** for doctrine
*prose*, and closes by warning "do not mistake the anchor for the enforcement."
The enforcement layer is precisely what got copied.

One more thing the record should carry, because it is the more general lesson: a
session **saw** this gap on 2026-07-22, wrote it down as "a discipline the child
should honour manually", and moved on. An intention was logged where a one-line
edit was available, and it decayed silently for three days — the same failure
mode the guard exists to prevent, reproduced one level up.

## Decision

**1. A repo calls the floor; it never copies it.** The scanner list lives in
`tools/floor.py` — one registry, two planes (a pre-commit hook reading the staged
diff at full cover; CI reading the whole tree with `leakscan` structural-only and
permanently so). `.github/workflows/floor.yml` in atelier is a reusable workflow;
a child's `floor.yml` is a ~30-line caller naming no scanner. A check added to the
registry is live estate-wide on the next push, with no child edit.

**2. Non-enforcement must be declared, never absent.** The old opt-out was
"delete the `run_scan` line" — invisible the moment it was done and
indistinguishable from a line nobody ever added. A repo that does not enforce a
check now says so in a committed `.atelier-floor.json`, as `advisory` (runs,
reports, does not block — for a one-off re-baseline) or `disabled` (with a stated
reason). A repo may also declare *where* a check looks (`scope`) and *how it is
tuned* (`flags`) — a networking repo scanning only its shareable subtree with
leakscan's IP/MAC rules off is the worked case, since those shapes are legitimate
content there. What a repo may **not** do is change whether a check blocks: the
mode-changing flags are refused, and the boundary and integrity scanners have no
advisory form at all. A burned secret, a leaked personal fact and a botched
harvest are not re-baselining problems.

**3. Conformance is enumerated, not assumed.** `tools/floorfleet.py` walks every
child (reusing `pins.discover`, as `signfleet` does) and reports what state each
repo's floor is in, with `--remote` reading GitHub's default branch — what will
actually run on a push. `--check` exits non-zero if any repo is unguarded.
**Scaffolding is not proof:** `create-repo` only covers repos it created and sees
nothing that drifts afterwards. This is what makes the answer cover future repos.

**4. The hook is tracked.** `.githooks/pre-commit` plus `core.hooksPath`, so the
hook file travels with the clone and stays current.

**5. The parent is not special.** atelier runs the floor it ships, with its own
scoping declared in its own `.atelier-floor.json`. A parent with a private list
is this same bug, one level up.

## Rejected

- **Keep vendoring, add a drift-detector.** Detects staleness *after* it happens
  and still means hand-editing 13 files every time we write a policy, forever.
  It treats the symptom and keeps the cause.
- **Pin the caller to a SHA by default.** Reproducible, and it re-introduces
  exactly the staleness being removed — a child would sit on an old floor until
  someone bumped it, which is the status quo with extra steps. Children may pin
  deliberately; the shipped default floats.
- **Push scanners into each child (vendor the code too).** Multiplies the
  supply-chain surface and guarantees divergence.
- **A scheduled job that opens PRs against children to sync their floor.**
  Automates the copying instead of removing it, and needs write access to every
  repo — a much larger trust surface than a read-time `uses:`.
- **Fold `signscan` into the registry.** It needs a trust list resolved from the
  child's own pin (never floating `main` — 2026-07-12 review G7) and a second
  GitHub-API plane. It is not a tree scanner; forcing it into that shape would
  misrepresent what it does.

## Consequences

- A new guard reaches every wired repo on its next push. That is the point, and
  it is also the risk: **a bad change to the registry now breaks the whole estate
  at once**, where staleness previously insulated children from parent mistakes.
  Accepted deliberately, on the same reasoning already recorded for floating the
  scanner code — for a security floor, newest is safest — and the blast radius is
  why the registry carries its own contract tests.
- **Adopting repos will go red first.** Fifteen findings already sit behind these
  gates estate-wide, in four repos. That red is the signal the gate exists to
  give; the declared-advisory state is how a repo keeps the finding visible while
  it works through it, rather than silencing it.
- `atelier` being **public** (ADR 0005) is now load-bearing in a new way: a public
  repo's reusable workflow is callable by private repos. If atelier ever went
  private this mechanism breaks for private children.
- One `git config core.hooksPath` per clone is still manual. `floorfleet` reports
  the gap; CI remains the backstop, because a hook can never be guaranteed.
- `floorfleet` proves a repo **calls** the floor, never that the floor is green
  there. Conformance and compliance stay separate claims.

## Evidence

- Estate measurement, 2026-07-25: 13/13 children drifted from the template;
  12/13 ran none of the five newer checks; `kainga` alone was current, and only
  because it was scaffolded after the update.
- `sizescan --check` across the fleet, before any wiring: 15 findings, 4 repos
  red — the gap was never theoretical.
- The registry's own fail-open, caught by the planted-secret commit tests during
  this change: the first draft rendered **absolute** paths on the staged plane,
  which match nothing against git's repo-relative path list, so every boundary
  check silently passed. Recorded here because it is the same shape as the defect
  being fixed — a check that runs, reports success, and covers nothing.

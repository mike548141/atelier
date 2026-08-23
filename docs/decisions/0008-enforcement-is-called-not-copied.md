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

**6. A repo may ADD a check of its own — it still may never soften one.**
*(Added 2026-08-06, on the cold pass's EP6. The mechanism landed on 2026-07-26
in `f526dea`/`76f4acc`, its doctrine written at every point of use — but not
here, so this record described only subtraction and a reader concluded the seam
did not exist.)* The `local` block in `.atelier-floor.json` declares checks the
**child** owns and ships: a rule that is genuinely repo-specific and could never
be fleet-wide — the forcing case is a tripwire whose blocklist names the estate's
own tokens, a list that can never live in a shared repo. Such a check runs inside
the floor, on both planes, from the child's own script. Three properties keep it
an extension point rather than a hole, and the seam's full doctrine lives with
the code, in `tools/floor.py` § THE REPO-LOCAL SEAM: it only **adds** (a name
colliding with a registered scanner is a hard config error, so it cannot replace,
shadow or weaken a fleet check — `PROPAGATION.md`'s narrow-not-contradict applied
to enforcement); it fails **closed** (a declared check whose script is missing
blocks, exactly as a missing shared scanner does); and it is **visible** (local
checks appear in `--list`, in `--json`, in the render and on the `floorfleet`
board, so a repo's own rules are estate-legible even though their code is not
shared). Clause 2 above is unchanged and still binds: `local` is the only way a
child adds, and nothing here lets it change whether a shared check blocks.

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
- **The control that makes a floating `@main` safe is atelier `main`'s own
  protection, not the pin.** *(Added 2026-08-06, on the cold pass's EP7 — the
  risk was accepted above without ever naming what holds it.)* A floating `uses:`
  executes atelier's code in every child's CI on every push, unreviewed at read
  time. Published Actions hardening guidance accepts `@main` for a callee inside
  the same trust boundary and treats every floating ref outside one as a
  supply-chain entry point — so this decision rests entirely on the boundary
  claim, and the boundary is **who can write atelier's `main`**: branch
  protection, signed commits, and review on the registry are the control, and
  they are load-bearing in a way the `uses:` line does not show. State the
  consequence at full strength: a compromise of atelier `main` is **arbitrary
  code running in every child's CI**, not merely a broken floor. That is a
  larger blast radius than the "one bad registry change reds the estate" risk
  accepted at the top of this list, and it is the reason the signing trust root
  is deliberately pinned while the scanners deliberately float (Rejected, last
  item; 2026-07-12 review G7) — the two calls point opposite ways on purpose.
  This is not an argument for pinning the caller: it is the named, checkable
  control that pinning would not provide either, since a pinned child still runs
  whatever that SHA contains.

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

## Amended 2026-08-23 — the boundary control stated at its true strength (AP1), and Decision 2's softenable list corrected (AP2)

**AP1 (MAJOR, the EP application cold pass; the principal's ruling,
2026-08-23).** The Consequences control clause named branch protection,
signed commits and registry review as what makes the floating `@main` call
safe. A live read (2026-08-09, re-affirmed at this amendment) shows none of
the three is in force as named: `main` carries no branch protection and no
ruleset, signature verification is warn-first on both planes, and registry
changes land under the standing autonomy grant with review after landing.
The controls actually in force are: a single-owner account with 2FA as the
only writer, public visibility (every push is published and inspectable),
the warn-first signature planes, and review-after-landing under the review
doctrine. Branch protection is deliberately **not** enabled — it would break
the direct-to-`main` workflow the estate's sessions and claim mechanics run
on, and the principal ruled the trade-off that way informed. The named
control is an **aspiration with a funded path**: a machine-checked boundary
(a parent-row check that reads branch-protection/ruleset state and reds when
the declared control is absent) is queued at board item `115/180`. Until it
lands, this clause is the truth of the boundary, not the earlier claim.

**AP2 (MODERATE, same pass).** Decision 2 said the boundary and integrity
scanners "have no advisory form at all" and only the prose-hygiene checks
carry one. That prose went stale: at HEAD the registry offers advisory forms
on sizescan and publishscan (deliberately — a size budget and a publish
surface are legitimate re-baselines), and the no-advisory set is secretscan,
leakscan, linkscan, reviewscan, board and licenscan. The registry
(`advisory=` non-None), not any prose list, is the authority; `floor.py`'s
docstring is corrected in the same change, and a test pinning the prose
lists to `Scanner.advisory` is queued at `020/340`. Decision 2's *intent* —
what a child may soften is not the child's call — stands unchanged.

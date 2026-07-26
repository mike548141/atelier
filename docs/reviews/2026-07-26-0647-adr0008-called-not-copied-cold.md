# Cold review — ADR 0008 "enforcement is called, not copied" + the estate rollout (rule-4 pass)

**Brief written by the reviewer (the taker), not the author.** REVIEW.md rule 4:
self-authored doctrine earns a cold *spawn*, not merely a cold context, and the
brief is written by the non-author who takes the `⏳` item.

## Spawn provenance

- **Spawned by**: Mike, in a fresh session, with the instruction *"Please do any
  review work, there are parallel sessions so take precautions"* — the queue was
  not pre-filtered for me and no author was in the loop.
- **Author's involvement**: none. This session did not write ADR 0008
  (`docs/decisions/0008-enforcement-is-called-not-copied.md`), `tools/floor.py`,
  `tools/floorfleet.py`, `.github/workflows/floor.yml`, `.githooks/pre-commit`,
  the `.atelier-floor.json` convention, or any of the 13 child-repo wirings; it
  did not instruct or schedule the sessions that did.
- **Rule 4's criterion** — *the review comes from a session the author neither
  started nor instructed* — passes.
- **Claim**: `docs/ROADMAP.md`, claimed 2026-07-26 0647 UTC, wt
  `atelier-review-0647-take`.

## Scope

Widest the work admits (REVIEW.md, *What a review actually checks*): the
decision itself, the design it commits to, the implementation that enacts it,
the tests, the child-facing template, and the live behaviour — re-run, not read.

**Non-goals** (and this narrowing is itself reviewable):

- The individual scanners' own detection quality (`sizescan`, `datescan`,
  `wrapscan`, `spellscan`, `reviewscan`, `leakscan`, `secretscan`, `linkscan`,
  `licenscan`). Each has, or is owed, its own first-of-kind review. What *is* in
  scope is how the registry composes and invokes them.
- The 15 pre-existing findings the rollout surfaced in four repos. They are
  those repos' work; the rollout says so.
- Private child repos' contents. atelier is public; nothing about a private
  child's internals gets written down here.

## What the work is (as this reviewer establishes it from the ADR and HEAD)

A rewrite of *how* the guard layer reaches 13 child repos. Previously each child
vendored a ~247-line `floor.yml` naming the scanners of its scaffold date, so 12
of 13 ran none of the five checks added since. Now:

1. `tools/floor.py` is the single registry, with two invocation planes — a
   pre-commit hook over the staged diff, and CI over the whole tree.
2. `.github/workflows/floor.yml` in atelier is a **reusable workflow**; each
   child's `floor.yml` is a ~30-line caller that names no scanner and resolves
   the workflow from `atelier@main` — floating, deliberately, on a
   "for a security floor, newest is safest" argument.
3. `.atelier-floor.json` per repo declares non-enforcement (`advisory` /
   `disabled`), scope, and flags — with a stated carve-out that a repo may not
   change *whether* a check blocks, and no advisory form at all for the boundary
   and integrity scanners.
4. `tools/floorfleet.py` enumerates conformance across the fleet,
   `--remote` reading GitHub's default branches.
5. `.githooks/pre-commit` + `core.hooksPath` so the hook is tracked, not
   machine-local.

The ADR's own framing — *"code was one-source; policy was vendored"*, and the
`PROPAGATION.md` thin-anchor/fat-pointer rule applied to the wrong half — is the
author's account of what the work is, and is therefore itself attackable
(rule 1).

## Attack surface (the reviewer's own, committed before any deferred material)

Named first, as lens 1 requires, and before opening the intent record, the
rollout session record, or the ADR's steer to a reviewer.

**A1 — "For a security floor, newest is safest" is the load-bearing premise, and
this repo has already ruled the opposite way once.** A floating `@main` reusable
workflow is a supply-chain dependency pointing *from* every child *into*
atelier's default branch: whoever can push there executes code in 13 repos' CI.
The ADR rejects vendoring the scanner code because it *"multiplies the
supply-chain surface"* — but floating the caller concentrates that surface into
one branch with no review lag. Sharper: the ADR's own *Rejected* list says
`signscan` must resolve its trust list from *"the child's own pin (never floating
`main` — 2026-07-12 review G7)"*. So a prior review already held that floating
`main` is unsafe for a trust-bearing check, and this decision floats the entire
floor. Either the two cases are genuinely different and the ADR must say why, or
the earlier ruling is being quietly overridden. **Is the trade named honestly,
and is the counter-evidence in the ADR's own text acknowledged?**

**A2 — Is the "may not change whether a check blocks" boundary actually
enforced, or only asserted?** `advisory` changes exactly that, for the checks
where it is allowed. So the guarantee reduces to: the carve-out list is correct,
and the code refuses what the prose refuses. Attack: which scanners have no
advisory form, is that list complete, does the code refuse mode-changing flags
as claimed, and what happens on a malformed, hostile, or absent
`.atelier-floor.json`? A declaration file that fails *open* would be the ADR's
own named defect class reproduced in the fix.

**A3 — Enumeration is only as good as its cadence, and the ADR's own Context
convicts intention-without-mechanism.** The ADR's most quotable lesson is that a
session *saw* the gap, wrote it down as a discipline to honour manually, and
watched it decay for three days. `floorfleet --check` is the answer to drift —
but if nothing *runs* it on a schedule, it is precisely an intention logged where
an edit was available. **Is floorfleet wired to anything, or is conformance
re-checked only when a human remembers?**

**A4 — Fail-open paths in the registry itself.** The ADR's Evidence section
records one fail-open caught in-build (absolute vs repo-relative paths on the
staged plane, so every boundary check silently passed). One found is a reason to
look for siblings, not a reason for confidence. Attack the exit-code and error
paths: a scanner that crashes, a scanner named in the registry but absent from
the fetched tree, a scope glob matching nothing, an empty staged diff, a
non-zero exit distinguished from a finding.

**A5 — Two children were installed with `--no-verify`, and the ADR does not say
so.** The rollout bypassed the very gate it was installing, twice, because the
gate failed on pre-existing content. That is recorded in the ROADMAP but is
absent from the decision record's Consequences. A decision record that omits the
compromise its own rollout required is incomplete for anyone reading it later
as the authority.

**A6 — Every "proven live" claim re-run.** The ROADMAP asserts *"All 13 children
call the floor; `floorfleet --remote --check` exits 0 against GitHub's default
branches"* and *"Proven live in CI, not just locally"*. Re-run both. A recorded
proof can be stale at the commit that recorded it.

**A7 — Security lens on the workflow itself** (mandatory, not a specialist
add-on). A reusable workflow inherits the caller's context: what `permissions:`
does it declare, what trigger does the child caller use, does it check out or
execute caller-supplied content, does it need or receive secrets, and does a
public reusable workflow called by a private repo leak anything about that repo
into a public surface? The `pull_request` vs `pull_request_target` distinction
is the classic hole in this exact shape.

**A8 — The parent-is-not-special claim.** Point 5 says atelier runs the floor it
ships with its own scoping declared. Verify against `.atelier-floor.json` and
`ci.yml`: does atelier actually route through the same registry, or does it keep
a second path that would let the parent's floor and the children's drift?

**A9 — Reversibility, and what happens when atelier is unreachable.** A
GitHub outage, a rename, a visibility flip, or a rate limit takes the floor out
in all 13 repos simultaneously. Does the caller fail closed (build red, work
blocked) or open (build green, unguarded)? Either is defensible; the ADR should
say which, and PRINCIPLES §1 ("design the way out before the way in") applies to
the estate's newest hard dependency.

---

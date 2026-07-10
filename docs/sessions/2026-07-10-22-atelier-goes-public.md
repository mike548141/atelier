# 2026-07-10 · atelier goes public — ADR 0005, named worked example (Opus)

Started as the CI-scan-distribution question (the thrice-deferred "how does a
child run atelier's scanners in CI" gap). Mike reframed it in one move: *what if
we publish all of atelier publicly, not just the scanners?* — which turned a
tooling question into the repo's whole reason to exist, and its biggest floor
action. Taken this session, deliberately, with his confirmation.

## The publication-readiness audit (real scan, not hand-wave)

The floor deserves grounding, so I scanned before advising:

- **Hard boundary held.** The sensitive categories — health, family, finance,
  address, pet, medication names — all scanned **zero** in tracked content (the
  alarming first counts were substring noise: identity words hiding inside common
  words). leakscan clean whole-tree; secretscan clean over all 44 commits;
  licenscan `--expect Apache-2.0` green. `.claude/settings.local.json` gitignored,
  not tracked; the template's is generic. (These literal terms are deliberately
  *not* enumerated here — the record for a public repo is itself in scope.)
- **Two real exposures, both identity not data.** (1) The principal's name is
  woven through by design (APEX literally addresses "telling \[the principal] the
  truth"), plus the GitHub handle and personal email — a *voice* question, not a
  leak. (2) Git history: 44 commits, single author, name+email frozen once public
  — the one irreversible call.
- **Dangling grounding.** The docs cite `ros`/`tiki` ~214× as their evidence
  base; those repos stay private, so a public reader can't verify the citations.

Data-safe ≠ publication-ready, but the audit moved the decision from "is it
dangerous" to "is the framing right".

## Mike's calls

- **Voice: named worked example** (not genericise). His sharpening: named only
  works for adopters if the docs say *you are the principal; Mike is the instance
  you read then instantiate as yourself* — otherwise it's voyeurism, not a
  template. That framing became the deliverable, not an afterthought.
- **Grounding: provenance note** — frame ros/tiki as the private origin, not
  broken links.
- **History: accept it** — his own authorship on his own scan-clean commits.
- **numen: leave it.** The audit surfaced that publishing reveals a private
  `mike548141/numen` repo ("home-automation… a great butler + house staff").
  Honest sharpening that decided it: numen is in *history* too, so a working-tree
  scrub is **cosmetic** — real removal is a history rewrite, which he declined
  for identity and which ADR 0005 argues against. numen is harmless (no address/
  family/health), so "leave it" is the only non-theatrical option. Left.

## What landed

- **ADR 0005** "atelier goes public" — supersedes 0003 (marked superseded),
  engages each of 0003's rejections: the peer-of-two never became a peer-of-three
  so public *is* the friction mechanism; named voice keeps the grounding that
  makes doctrine credible; history stays as-authored.
- **README** — new "If you're adopting this" (you become the principal; ros/tiki
  as provenance); Sharing → public + every-commit boundary.
- **CLAUDE.md** — visibility PRIVATE→PUBLIC; the making-public floor is **spent**
  (ADR 0005 was the confirmation), live floor is the next widening (announce/
  package/plugin); no-personal-data now load-bearing continuously; stale
  "genericise at publish" allow-note refreshed to the named-worked-example call.

## The gate earned its keep, live

The pre-publish scan blocked the work **twice**, both times on the author's own
literal contact/health terms written *into the record itself*: first a personal
email in ADR 0005's prose, then — in this very session file — the enumerated
medication/family terms and email I'd listed to describe what scanned clean. Both
reworded to categories, not literals: no reason to add a fresh copy of sensitive
strings to a now-public repo just to say they're absent. A §14 honest-instrument
moment, doubled — the scanner's "blocked" was a true claim that changed the work,
and the boundary bit its own author writing the boundary's record.

## The flip (act, then record)

Ordered so no committed doc claimed public before it was true: prep committed
**local** (hook ran both scanners clean) → `gh repo edit --visibility public`
(verified `isPrivate: false` / `PUBLIC`) → `git push` (remote HEAD `22e41f9`
matches local) → this record. https://github.com/mike548141/atelier is public.

## Through-line: the small question dissolved into the big one

The CI-scan-distribution gap that opened the session is now *solved by the
decision that replaced it*: with atelier public, a child's CI can fetch the
public scanners — no secret, no vendored copy, no drift. The original four-option
question (publish scanners / fetch-with-token / vendor / defer) collapses to
"atelier is public, point CI at it". Wiring that into the CI templates is the
natural next build — now unblocked, no longer a floor question.

## Now true for every future session

- atelier is **public**. The no-personal-data boundary is load-bearing on *every*
  commit, not a pre-publish check — the scan hook is the continuous gate.
- The next widening (announcement, packaged plugin/skills bundle, one real peer
  adoption) is the live floor item — Mike's call, not the agent's.
- Owed, now unblocked: wire the (public) scanners into the child CI templates;
  atelier's own CI (dogfood the test suite + scan triad + link check).

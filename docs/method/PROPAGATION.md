# Propagation — how the house doctrine reaches every repo

*How a child repo (ros, faves, any future project) stays current with atelier
without a second source of truth drifting from the first. The review-endorsed
shape (2026-07-10): **thin anchor, fat pointer** — a dependency with a lockfile,
for doctrine instead of code.*

## The problem

atelier is canonical. But a child session runs in the child repo, reads the
child's `CLAUDE.md`, and may never open atelier at all. Three failure modes to
avoid at once:

- **Silent staleness** — the child drifts behind the house doctrine and no one
  notices. (The exact failure `PRINCIPLES.md` §6 legibility exists to kill.)
- **N copies** — vendoring the doctrine into every child rebuilds the
  divergence-by-neglect problem DRY forbids.
- **Machinery to distribute machinery** — a session-start pull/hook is
  heavyweight, and fails unsafe if atelier is unreachable.

Rejected accordingly: bare-reference (staleness invisible), vendored copy
(N copies), pull-hook (over-built, fail-unsafe).

## The mechanism — thin anchor, fat pointer

Five moving parts, no engine, no new machinery:

1. **atelier is versioned by its commit SHA.** The SHA *is* the version — no
   tag ceremony required. `CHANGELOG.md` carries one human-readable line per
   doctrine change; tags are optional and reserved for milestones a peer would
   cite. To answer "what version am I on?", read the pin; to answer "what
   changed?", read the CHANGELOG or `git log`.

2. **Every child `CLAUDE.md` carries the standard doctrine block** (spec below):
   an inlined safety floor + a pointer to atelier + a version pin + a drift
   check + a repo-visibility fact.

3. **The floor is inlined, so it binds even if atelier is never read.** This is
   the fail-safe: an agent that only ever reads the child `CLAUDE.md` still
   inherits honesty, the Laws, and the always-confirm floor. atelier being
   unreachable degrades *richness* (the fat pointer), never *safety* (the thin
   anchor).

4. **The drift check rides the session-start read.** The child `CLAUDE.md` is
   already read at session start; it now ends the doctrine block with one
   command — `git -C <atelier-path> log --oneline <PIN>..HEAD`. Empty output ⇒
   current. Any output ⇒ the house doctrine has moved since the pin: read the
   changes, decide if they bear on this repo, and bump the pin **deliberately**.
   No polling, no hook — the CLAUDE.md read *is* the propagation event
   (events-over-polling).

5. **Bumping the pin is a per-repo human-in-the-loop act.** A doctrine change in
   atelier does not silently rewrite every child; it becomes *visible* in every
   child at the next session, and each repo adopts it on purpose. This is the
   lockfile discipline: the pin moves when someone moves it.

**Honest caveat (the apex requires it):** the pin makes staleness *observable*,
not *enforced*. Nothing here compels a session to run the drift check or act on
it. Enforcement is a separate thing — see the enforcement clause below.

## The standard child doctrine block

Copy this to the **top** of a child repo's `CLAUDE.md`, fill the three
placeholders (`<atelier-path>`, `<SHA>`, `<visibility fact>`), and keep it under
~20 lines of substance (the 2026-07-10 review found the original ~15-line
squeeze had dropped two floor cases — compress prose, never floor coverage). `create-repo` stamps it on new repos; existing repos are
retrofitted once. Everything below the block is repo-specific onramp.

```markdown
## Doctrine — inherited from atelier (pinned `atelier@<SHA>`)

This repo works by the atelier operating model. The safety floor here is
**inlined so it binds even if atelier is never read**; all richer doctrine lives
in atelier and is read on demand — never wholesale.

- **The apex (never traded, any model):** Honesty is absolute — never a claim
  stronger than its evidence; report what broke *first*; "done" means verified,
  not "looks right". Then the Laws, in order: avoid harm → obey your principal →
  self-preserve. Surface a genuine dilemma; never silently resolve it.
- **Always stop and confirm (the floor):** making a private repo public or
  widening its audience; anything truly destructive or irreversible; secrets;
  spending money; anything touching people's safety; widening your own grant
  (record the principal's decision, never originate it); a lockout-class change
  that could sever your own access; a new trust surface (deploy key, webhook,
  CI secret, OAuth/app grant); installing an unapproved tool. Everything
  recoverable — commit/push/PR included — just proceed. (On a deploy-on-push
  repo, a push that publishes a *new class* of content is the private→public
  line above, not routine push.)
- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`. At
  session start run `git -C <atelier-path> log --oneline <SHA>..HEAD`; any output
  means the house doctrine moved — read it, then bump the pin above deliberately.
- **This repo's visibility:** <visibility fact>. Verify:
  `gh repo view <owner/repo> --json visibility`.
```

The inlined floor is a **narrowing-free restatement** of the apex + AUTONOMY
floor — it may compress but must not contradict them. When atelier's apex or
floor changes, the block's wording is part of what a pin bump reviews.

## The layer-override rule

atelier is the parent; a child repo is a layer over it, the same shape tiki's
config uses (default → org → site → device). The merge is read by an agent, not
computed by an engine, so the rule is a discipline:

- A child may **narrow** (make a rule stricter — e.g. faves forbids a build
  step; atelier is silent on it) or **append** (add repo-specific doctrine —
  e.g. ros's tiki bearings).
- A child may **never silently contradict** the parent. A child rule that is
  *looser* or *opposite* to a house rule is a **defect to surface**, not a
  quiet local win. Raise it: either the house doctrine is wrong (change atelier)
  or the child is (fix the child). Silence is the one disallowed resolution.
- On a live collision, the **stricter/safer** reading wins until the conflict is
  resolved upward. Children point up; the parent never points down for truth.

## The enforcement clause (read ≠ complied)

The category error to name in writing: **a doctrine that is read is not a
doctrine that is complied with.** The propagation mechanism distributes the
*documents* and makes staleness *visible* — that is all a document can do.

Enforcement was always a separate practice: **independent review by a capable
model** (`REVIEW.md`). The documents are the standard; the peer review is what
checks the work against the standard before it is trusted (see
`MODEL-ECONOMICS.md` review-trigger policy). A pin that is current and a floor
that is inlined still only *inform* the agent; the review loop is what *catches*
the session that ignored them — with an honest window: reviews trigger on
structural or irreversible work, so a routine session that skips the drift check
may go uncaught until the next reviewed slice. The mechanism bounds staleness;
it does not eliminate it. Do not mistake the anchor for the enforcement.

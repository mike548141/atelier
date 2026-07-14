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
   command — `git -C "<atelier-path>" log --oneline <PIN>..HEAD`. Empty output ⇒
   current. Any output ⇒ the house doctrine has moved since the pin: read the
   changes, decide if they bear on this repo, and bump the pin **deliberately**.
   Bump even when the delta turns out not to bear on this repo (tool commits,
   session logs) — the pin means "inspected up to here", and a check that keeps
   re-surfacing old noise trains sessions to skim it (alarm fatigue kills the
   signal). No polling, no hook — the CLAUDE.md read *is* the propagation event
   (events-over-polling).

5. **Bumping the pin is a per-repo human-in-the-loop act.** A doctrine change in
   atelier does not silently rewrite every child; it becomes *visible* in every
   child at the next session, and each repo adopts it on purpose. This is the
   lockfile discipline: the pin moves when someone moves it.

**Honest caveat (the apex requires it):** the pin makes staleness *observable*,
not *enforced*. Nothing here compels a session to run the drift check or act on
it. Enforcement is a separate thing — see the enforcement clause below.

The drift check above is *per-child and pull-based* — a child only learns it is
behind when a session happens to open in it. The fleet-level companion is
`tools/pins.py`: stood in atelier, it reads every child's pin and reports who is
behind and by how much (one roll-up instead of N separate session-starts). It is
deliberately **read-only** — it never bumps a pin, because bumping stays the
per-repo human-in-the-loop act point 5 describes. So it widens *observability*
(per-child → fleet), and changes nothing about enforcement; the caveat above
still holds in full.

## The standard child doctrine block

Copy this to the **top** of a child repo's `CLAUDE.md`, fill the four
placeholders (`<atelier-path>`, `<SHA>`, `<owner/repo>`, `<visibility fact>`
— quote the path if it contains spaces; the sibling-relative `../atelier` is
the house shape), and keep it under
~15 lines of substance. `create-repo` stamps it on new repos; existing repos are
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
  that could sever your own access; installing an unapproved tool or adding a
  new trust surface (deploy keys, webhooks, OAuth/app grants). Each such
  confirmation is an *informed* one — the agent puts what it wants to do, why,
  and the likely impact in plain language first; an approval given without that
  account is not a decision the doctrine recognises (`00-APEX.md`). Everything
  recoverable — commit/push/PR included — just proceed.
- **Concurrency:** `git pull --rebase --autostash` at session start; push after
  each commit. Uncommitted changes this session didn't make ⇒ another session
  is live: move to a worktree — never work around or absorb them. Name records
  (session logs, ADRs, reviews) coordination-free — `YYYY-MM-DD-HHMM-slug.md`,
  never a next-N counter; files named under retired schemes keep their names.
- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`. At
  session start run `git -C "<atelier-path>" log --oneline <SHA>..HEAD`; any
  output means the house doctrine moved — read it, then bump the pin above
  deliberately.
- **Estate resources — point up, don't re-derive:** providers & account plans,
  financial constraints & plan entitlements, licences, credentials, shared
  estate tooling, and the estate inventory live in the operator's **private
  estate-root repo** (atelier's private counterpart). Reference it for these;
  never re-derive them locally or copy its contents down. If **this** repo is
  public, reference the root by local-path convention, never by name — a public
  repo naming the estate's credential/inventory root is reconnaissance.
- **This repo's visibility:** <visibility fact>. Verify:
  `gh repo view <owner/repo> --json visibility`.
```

The inlined floor is a **narrowing-free restatement** of the apex + AUTONOMY
floor, and the concurrency line restates `CONCURRENCY.md`'s sync bookends,
dirty-tree backstop, and record-identifier rule — each may compress but must
not contradict its source. The **estate-resources** line points at the *other*
root: atelier is the doctrine root; the estate's facts (its inventory, provider
plans and financial constraints, credentials, shared tooling) live in a separate
**private estate-root repo** — the knowing-root that atelier deliberately is not
(atelier is public and holds no inventory). Every child inherits both pointers:
up to atelier for *how we work*, up to the estate root for *what the estate has*.
The estate root is named only in a **private** child's own onramp — never in this
public canonical text, and never in a **public** child's tree: a public child
references it by a local-path convention, so the repo's name is never coupled to
the sensitive posture it holds (RECORD's name↔posture split). Its contents are
never copied down into any child.
When atelier's apex, floor, concurrency, or estate-pointer doctrine changes, the
block's wording is part of what a pin bump reviews.

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

Enforcement was always a separate practice: **independent review** — who
reviews, at what capability, and which changes earn one live in `REVIEW.md`.
The documents are the standard; the peer review is what checks the work against
the standard before it is trusted (`REVIEW.md` carries the lifecycle;
`MODEL-ECONOMICS.md` the trigger economics). A pin that is current and
a floor that is inlined still only *inform* the agent; the review loop is what
*catches* the session that ignored them. Do not mistake the anchor for the
enforcement.

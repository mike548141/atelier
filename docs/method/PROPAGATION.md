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
   inherits honesty, adaptation, the Laws, and the always-confirm floor. atelier
   being unreachable degrades *richness* (the fat pointer), never *safety* (the
   thin anchor).

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
the house shape), and keep it **deliberately lean**: the block is the hottest
read path in the fleet — every child session pays its length at every open —
so a line earns its place or moves behind a pointer. **Structural rule (SR2,
2026-07-20; the number dropped after review, 2026-07-21):** one bullet per
irreducible floor concern — seven today (apex + Laws, the always-stop floor,
concurrency, session rhythm, source & drift, estate resources, this repo's
visibility), each as tight as it can be while stating its concern in full and
pointing up for the rest. That structure *is* the spec — there is deliberately
**no line figure**: a number picked to sit just above what the block weighs
today is circular (it can't be exceeded the moment it's written), and nothing
gates on length here anyway, so a figure would be decoration with a circularity
liability. A block that has grown means a concern has accreted narratable detail
that belongs behind its pointer, not that it "broke a budget"; a concern can
only *leave* the block by being genuinely redundant with another, never by
trimming a live safety statement. (The earlier "~15 lines" and "~50 lines"
figures are both retired — the first was dead on arrival, the second tracked the
measurement it claimed to be independent of.) `create-repo` stamps it on new
repos; existing repos are retrofitted once. Everything below the block is
repo-specific onramp.

<!-- floor:begin -->
```markdown
## Doctrine — inherited from atelier (pinned `atelier@<SHA>`)

This repo works by the atelier operating model. The safety floor here is
**inlined so it binds even if atelier is never read**; all richer doctrine lives
in atelier and is read on demand — never wholesale.

- **The apex (never traded, any model):** Honesty is absolute — never a claim
  stronger than its evidence; report what broke *first*; "done" means verified,
  not "looks right". Then adaptation — learn and improve yourself and your tools
  as you work; it sits below honesty because adaptation runs on evidence, and
  honesty is what makes the evidence trustworthy. Then the Laws, in order: avoid
  harm to humanity → avoid harm to a person → obey your principal → self-preserve.
  Surface a genuine dilemma; never silently resolve it.
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
- **Concurrency:** assume another session may be live — a clean tree is not
  proof you're alone. `git pull --rebase --autostash` at session start; push
  after each commit. Take a worktree by default for write-heavy or multi-commit
  work; uncommitted changes this session didn't make are positive proof ⇒ move
  to a worktree — never work around or absorb them (`CONCURRENCY.md`). Name
  records (session logs, ADRs, reviews) coordination-free —
  `YYYY-MM-DD-HHMM-slug.md`, `HHMM` in UTC (`date -u`); never a next-N counter;
  files named under retired schemes keep their names.
- **Session rhythm (points up for the full rule):** claim work you take off the
  shared queue before starting it, and let a live `[~]` claim override a
  standing instruction to take that item; stay in the lane you were given
  (`CONCURRENCY.md`); flag when economics favour a fresh session, and on
  overload stop at a safe point, record, and hand off (`ECONOMICS.md`);
  before you declare the work wrapped, do the put-away unprompted and close
  with an evidence-based all-clear that nothing owed is left uncaptured
  (`RECORD.md`).
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
<!-- floor:end -->

The inlined floor is a **narrowing-free restatement** of the apex + AUTONOMY
floor, and the concurrency line restates `CONCURRENCY.md`'s flipped prior
(assume concurrent; worktree by default for heavy writes), sync bookends,
dirty-tree backstop, and record-identifier rule — each may compress but must
not contradict its source. The **estate-resources** line points at the *other*
root: atelier is the doctrine root; the estate's facts (its inventory, provider
plans and financial constraints, credentials, shared tooling) live in a separate
**private estate-root repo** — the knowing-root that atelier deliberately is not
(atelier is public and holds no inventory). Every child inherits both pointers:
up to atelier for *how we work*, up to the estate root for *what the estate has*.
The estate root is named only in a **private** child's own onramp — never in any
public tree, so the repo's name is never coupled to the sensitive posture it
holds (RECORD's name↔posture split). A public tree references it by a local-path
convention instead. Its contents are never copied down into any child.

**"Any public tree" includes atelier's own, records and all** — and it has to be
said, because the narrower wording did not hold. This rule previously read
*"never in this public canonical text, and never in a public child's tree"*,
which binds the doctrine prose and the children and quietly exempts the one
public repo doing most of the writing: atelier itself. The doctrine stayed
clean and the **records** did not. As of 2026-07-28 `CHANGELOG.md`,
`docs/SESSIONS.md` and `docs/ROADMAP-DONE.md` name the estate root in eight
places, twice beside exactly what it holds — the financial inventory, the
credential registry. That is the coupling this rule exists to prevent, written
by sessions that were following the rule as it was worded.

The scrub is **forward-only** (Mike's ruling, 2026-07-28): the mentions already
pushed stay. A public repo cannot be un-published, and rewriting eight records
would buy nothing back from forks, clones and caches while costing the
history's integrity. What changes is that no *new* mention is written. Naming
the leak's location precisely is itself safe here — this text already says the
root is private and holds credentials; what it withholds is which repo that is.

The general lesson is the one the policy-as-code programme keeps re-learning: a
boundary is only as good as the place it is enforced, and a rule that names
*categories* of repo will exempt whichever category the writer is standing in.
Bind the property — public — not the role.
When atelier's apex, floor, concurrency, or estate-pointer doctrine changes, the
block's wording is part of what a pin bump reviews.

### The bundled-mode variant (plugin-only adopters)

An adopter who holds only the installed plugin — no atelier checkout — has no
git history to log against, so the drift check above cannot run. The stamped
block degrades the **pin's referent, not the block**: the same text with two
substitutions, and only these (the ADR 0002 fork named in
`docs/decisions/2026-07-21-0748-deinstance-create-repo-for-the-plugin.md` — the
pin still exists; its referent becomes the plugin version). This is the
canonical bundled-mode text: `create-repo` stamps it verbatim, filling
`<plugin-path>` (the plugin's install directory, absolute) and `<VERSION>` (the
`version` in the plugin's `.claude-plugin/plugin.json` at scaffold time) — a
scaffold never improvises its own wording.

The heading line becomes:

```markdown
## Doctrine — inherited from atelier (pinned plugin `atelier@<VERSION>`)
```

and the **Source & drift** bullet becomes:

```markdown
- **Source & drift:** canonical doctrine is the installed atelier plugin's
  `docs/method/` (`<plugin-path>`). This repo pins plugin version `<VERSION>`.
  At session start run
  `grep '"version"' "<plugin-path>/.claude-plugin/plugin.json"`; a version
  other than `<VERSION>` means the house doctrine moved — read the plugin's
  `CHANGELOG.md`, then bump the pin above deliberately.
```

Every other line is identical to the block above — the floor, concurrency,
session rhythm, estate pointer, and visibility fact do not vary by mode. Drift
is tracked by plugin version because that is the pin a plugin-only adopter can
actually check: the command runs against exactly what they have installed.

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

## Enforcement propagates too — by call, never by copy

*(Added 2026-07-26, ADR 0008, after this file's own rule was applied to prose
and not to the machinery.)*

Thin anchor, fat pointer is not only for doctrine text. **It binds hardest on
the mechanical controls**, because a stale document merely misinforms a reader
who can still think, while a stale *gate* silently enforces whatever standard
was current on the day it was copied — and reports success while doing it.

The rule, stated so it cannot be read as prose-only:

> A child repo **calls** the parent's enforcement. It never holds a copy of
> *which* checks run. Anything a child must edit to receive a new check is a
> vendored policy, and it will go stale.

The distinction that matters, and the one we got wrong: sharing the *code* of a
control is not sharing the *policy*. Our scanners were always fetched fresh from
atelier — and the **list of which scanners ran** was copied into every child at
scaffold time. On 2026-07-25 that meant 12 of 13 children ran none of the five
checks added since they were created, including one built after a real incident
three days earlier. Nothing was broken. Nothing reported it either.

So the test to apply to any new control is not "have we written it down and
pointed at it?" but:

- **What must a child edit to receive this?** If the answer is anything, the
  mechanism is a copy. Make it a call.
- **What does a child that opts out have to say?** If opting out is deleting a
  line, it is invisible and indistinguishable from a line never added. Require a
  *declaration* — and let the declaration be readable estate-wide.
- **How would we know a repo never adopted it?** If the answer is "someone would
  notice", there is no answer. See the next section.

The parent is not exempt. atelier runs the floor it ships, scoped by the same
config a child uses. A parent enforcing something its children don't — or missing
something they have — is this defect one level up, and is exactly how a
"canonical" repo drifts from its own canon.

## Enumeration, not assumption (how we know it landed)

**Scaffolding is not proof.** A scaffolder covers only the repos it created, and
sees nothing that drifts afterwards. A pin bump proves a child *read* something,
never that a control *runs* there.

The only thing that closes this is an instrument that walks every child and
reports the ones that are unguarded — `tools/floorfleet.py` for the scanner
floor, `tools/signfleet.py` for signing. Both enumerate; both fail-safe (an
estate that could not be verified is never reported green); both are cheap to
re-run, which is what makes them true rather than a one-off audit.

An absence never raises its hand. Something has to go looking for it.

## The enforcement clause (read ≠ complied)

The category error to name in writing: **a doctrine that is read is not a
doctrine that is complied with.** The propagation mechanism distributes the
*documents* and makes staleness *visible* — that is all a document can do.

Enforcement was always a separate practice: **independent review** — who
reviews, at what capability, and which work earns one live in `REVIEW.md`.
The documents are the standard; the peer review is what checks the work against
the standard before it is trusted (`REVIEW.md` carries the lifecycle;
`ECONOMICS.md` the trigger economics). A pin that is current and
a floor that is inlined still only *inform* the agent; the review loop is what
*catches* the session that ignored them. Do not mistake the anchor for the
enforcement.

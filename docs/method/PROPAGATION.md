# Propagation — how the house doctrine reaches every repo

*How a child repo (a private child, faves, any future project) stays current
with atelier without a second source of truth drifting from the first. The
review-endorsed shape (2026-07-10): **thin anchor, fat pointer** — a dependency
with a lockfile, for doctrine instead of code.*

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
   inherits honesty, adaptation, and the always-confirm floor. atelier
   being unreachable degrades *richness* (the fat pointer), never *safety* (the
   thin anchor).

4. **The drift check rides the session-start read.** The child `CLAUDE.md` is
   already read at session start; it now ends the doctrine block with one
   command — `git -C "<atelier-path>" fetch -q && git -C "<atelier-path>" log
   --oneline <PIN>..origin/main`: measured against the parent's published
   mainline (its remote is assumed to be `origin`), never the branch its
   checkout happens to be parked on. The two are joined with `&&` because a
   failed fetch must not reach the `log`: its empty output would read as
   "current" when a fetch error is *no result*, not *no drift*. Empty output
   after a good fetch ⇒ current. Any output ⇒ the house doctrine has moved
   since the pin: read the changes, decide if they bear on this repo, and bump
   the pin **deliberately**.
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
irreducible floor concern — **nine** today (the apex, the always-stop floor,
asking, concurrency, session rhythm, doctrine problems point up, source & drift,
estate resources, this repo's visibility), each as tight as it can be while
stating its concern in full and pointing up for the rest. *(The count read
"seven" until 2026-08-23 and was wrong by one before this change: the **asking**
bullet landed 2026-08-22 without it. Corrected by counting the block rather than
incrementing the sentence — which is the only way this line can be trusted, and
the reason it is worth keeping a count at all.)* That structure *is* the spec —
there is deliberately
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
  honesty is what makes the evidence trustworthy. Surface a genuine dilemma;
  never silently resolve it — a quietly picked fork is a withheld truth.
- **Always stop and confirm (the floor):** making a private repo public or
  widening its audience; anything truly destructive or irreversible; secrets;
  spending money; anything touching people's safety; widening your own grant
  (record the principal's decision, never originate it); a lockout-class change
  that could sever your own access; installing an unapproved tool or adding a
  new trust surface (deploy keys, webhooks, OAuth/app grants). Each such
  confirmation is an *informed* one — the agent puts what it wants to do, why,
  and the likely impact in plain language first. The principal's authority is
  absolute — never overrule him, even if you believe him uninformed; an approval
  given without that account is open to challenge on the briefing, and the
  challenge is raised to him by re-briefing (`00-APEX.md`) — and at *this*
  floor the re-briefing comes **before** the action, never after it, because
  what the floor guards cannot be taken back. Everything
  recoverable — commit/push/PR included — just proceed.
- **Asking — any question, decision or ruling:** put the ask in the harness's
  structured question device where one exists (Claude Code:
  `AskUserQuestion`), never buried in prose. The account must have *reached*
  the principal before the choice is put — always as a finished message of its
  own, ahead of the device, in every view (one extra turn) — and the device
  carries only the choice; never trim the account to fit. Give the real
  options, each with its pros, cons, impacts, risks and costs, plus **a
  recommendation** with its reasoning shown. Every fact in the ask is
  verified, or plainly marked as assumed where verifying would cost more than
  the decision is worth.
  (`00-APEX.md` for what an ask must contain; `COMMUNICATION.md` § *Asking for
  a ruling* for how it travels.)
- **Concurrency:** assume another session may be live — a clean tree is not
  proof you're alone. At session start read `git status` first — dirty work
  this session didn't make means stop and move, never autostash it — then,
  where the branch has an upstream, `git pull --rebase --autostash`; push after each
  commit. Take a worktree by default for write-heavy or multi-commit
  work; uncommitted changes this session didn't make are positive proof ⇒ move
  to a worktree — never work around or absorb them (`CONCURRENCY.md`). Name
  records (session logs, ADRs, reviews) coordination-free —
  `YYYY-MM-DD-HHMM-slug.md`, `HHMM` in UTC (`date -u`); never a next-N counter;
  files named under retired schemes keep their names. Where sessions can message
  each other, announce your **file set** on open and answer peers' — a claim says
  what, never which files. A message reserves nothing; only a pushed artefact
  does, so check a shared allocator (identifiers, version constants) **after**
  the push. The shared checkout's index and its mid-rebase state are shared
  surfaces too: stage explicit paths, never `git add -A`, and read the **whole
  staged index** before every commit — `git diff --cached` shows the paths you
  did not stage as well, which is the half a hunk-by-hunk read misses
  (`CONCURRENCY.md` § The trigger).
- **Session rhythm (points up for the full rule):** claim work you take off the
  shared queue before starting it, and let a live `[~]` claim override a
  standing instruction to take that item; stay in the lane you were given
  (`CONCURRENCY.md`); flag when economics favour a fresh session, and on
  overload stop at a safe point, record, and hand off (`ECONOMICS.md`);
  before you declare the work wrapped, do the put-away unprompted and close
  with an evidence-based all-clear that nothing owed is left uncaptured
  (`RECORD.md`).
- **Doctrine problems point up (every repo, atelier included):** if a house rule
  is wrong, unworkable, ambiguous, contradictory, stale, missing or unfindable,
  **report it to atelier** — with evidence where evidence exists, marked
  unevidenced where it does not. Consideration and remediation are atelier's;
  the reporting session stops at the report and never silently works around a
  rule it thinks is wrong, because the workaround destroys the only evidence the
  house would get. Check the parent's actual file first — this block is a lossy
  summary and is not evidence about what the house says. File it in atelier's
  board directly, or hand it over the peer channel, or — where neither is
  reachable — hold it in this repo's record marked owed upstream. Describe the
  problem by its class only: atelier is public and a push cannot be retracted,
  so a private repo never names itself or its contents (hosts, clients,
  secrets) on the branch, PR title, commit subject, PR body or item. Filing
  without harming the parent: name the branch for the report, say it is a
  hand-up in the first line, open the PR before you stop, and touch nothing but
  your own item. (`PROPAGATION.md` § *Pointing up*.)
- **Source & drift:** canonical doctrine is `<atelier-path>/docs/method/`. At
  session start run `git -C "<atelier-path>" fetch -q && git -C
  "<atelier-path>" log --oneline <SHA>..origin/main` — the parent's published
  mainline (its remote is assumed to be `origin`), never whatever branch its
  checkout is parked on. A fetch error is *no result*, not *no drift*; any
  output means the house doctrine moved — read it, then bump the pin above
  deliberately.
- **Estate resources — point up, don't re-derive:** providers & account plans,
  financial constraints & plan entitlements, licences, credentials and the
  estate inventory live in the operator's **private estate-root repo**
  (atelier's private counterpart). Reference it for these; never re-derive
  them locally or copy its contents down. The **expected toolbox** (which
  tools to expect, and how to find them) is atelier's: `method/TOOLBOX.md`.
  The root is a private repo like any other: it may be named, and in a
  public tree what it holds and its condition go by type only
  (`RECORD.md` § *The record is public*).
- **This repo's visibility:** <visibility fact>. Verify:
  `gh repo view <owner/repo> --json visibility`.
```
<!-- floor:end -->

**The markers bracketing that block are a stamp, and they are mechanical.** The
`floor:begin` / `floor:end` HTML comments above name this text as a canonical
**region**; a child that inlines it wraps its copy in a matching
`stamp:begin source=… region=…` / `stamp:end` pair. Both are HTML comments —
invisible in rendered Markdown — so stamping changes not one visible character
of the text it brackets. `tools/stampscan.py` reads the pair and compares the
copy against this region, which is what turns "a pin bump reviews this wording
too" from a hope into a check. It was a hope for a while: the `create-repo` C3
finding was precisely that nothing mechanical diffed the copy against its
canonical text.

A copy may **narrow** — carry genuinely less than the canonical region — but
only by *declaring* it, with `narrow=<reason>` on the copy's own begin marker.
The declaration is the entire signal, because a silent drop and a legitimate
omission are mechanically identical (both are the canonical text minus some
lines); undeclared, a drop reds. Three boundaries on that:

- **Narrowing to nothing is not a narrowing.** An empty stamped block is drift
  however it is declared. A floor exists to bind even where nothing else is
  read, and one token must not be able to vacate all of it while the check
  reports clean (2026-07-26 cold pass ST2, ruled 2026-08-04).
- **A declaration excuses omission only.** A reworded, reordered, or added line
  reds regardless of `narrow=` — the scanner cannot tell a harmless reword from
  a contradiction, and will not pretend to.
- **Who may declare it: the child, in its own tree, with the reason written
  down.** Narrowing is the child repo's call about its own needs — never
  atelier's on a child's behalf, and never a bare `narrow=` with no stated
  reason. The reason is unverifiable by machine, exactly like every
  `<name>scan:allow:` marker in the house; what it buys is a name attached to
  the decision. atelier's own stamped copies narrow nothing.
- **The safety floor never narrows.** A child's copy of the `floor` region is
  the canonical text word for word — no compression, no declared narrowing.
  The rule keys on the stamp of *this file's* `floor` region, which the
  scanner identifies by the file the stamp's `source=` resolves to, not by how
  the path is spelled, so a respelling of the path is still the floor. A
  `narrow=` on such a stamp that narrows anything reds instead of excusing it
  (ruled 2026-09-19, `115/030`: *"Floor copy verbatim"*); on a copy that is
  already word for word it narrows nothing and changes nothing. Nor can a
  `stampscan:allow` marker inside the stamp switch the comparison off: the
  block is compared whatever markers it carries (the principal's answer of
  2026-11-09, `160/340` FV2: a specific "never" beats the general escape).
  The floor is the one text that must bind where nothing else of the child's
  is read, so a child that finds a line of it wrong reports it upward
  (§ *Pointing up*) instead of dropping it locally. The declaration above
  stays for any other stamped region; as of 2026-11-09 the floor is the only
  one.

The inlined floor is a **narrowing-free restatement** of the apex + AUTONOMY
floor, and the concurrency line restates `CONCURRENCY.md`'s flipped prior
(assume concurrent; worktree by default for heavy writes), sync bookends,
dirty-tree backstop, and record-identifier rule — atelier's canonical text of
each may compress its source but must not contradict it; a child's copy of
that canonical text is verbatim (above). The **estate-resources** line points at the *other*
root: atelier is the doctrine root; the estate's facts (its inventory, provider
plans and financial constraints, credentials, shared tooling) live in a separate
**private estate-root repo** — the knowing-root that atelier deliberately is not
(atelier is public and holds no inventory). Every child inherits both pointers:
up to atelier for *how we work*, up to the estate root for *what the estate has*.
The estate root is a private repo like any other: it may be named, in a private
or a public tree, and what it holds and the condition it is in go by type only
in a public record (`RECORD.md` § *The record is public*). Its contents are
never copied down into any child.

*(2026-11-09, `320/380`, filed from a child 2026-09-20; Mike's pick from options
offered, so an answer and not a ruling in his words.)* The floor's visibility
test now reads "is public, or is ever made public". A present-tense test
returns false on every read of a private-now, public-candidate repo until the
day it flips, by which time the content it exists to keep out is committed. And
a compliant example that spells the real path discloses the name it hides.
Children's copies carry the old wording until their next pin bump. *(Superseded
the same day by `020/050`, below: the sentence this note reworded, which told a
public repo to reference the estate root by path and never by name, is gone.)*

**The earlier, stricter rule for the estate root is withdrawn** (2026-11-09,
`020/050` and `020/030`; Mike's pick from options offered was *"Treat like any
private repo"*, an answer and not a ruling in his words). This
section used to say the estate root is named only in a private child's own
onramp, never in any public tree, and that "any public tree" included
atelier's own records. It is now an ordinary private repo under `RECORD.md`:
the name is allowed; what it holds and its condition go by type only. The
stricter rule did not hold: the root was named 63 times across 19 files of
this repo's records when measured on 2026-07-28, and the programme recorded
the same breach at least five times. The name is in pushed history for good
either way, so the harm was never the name; it was the name beside what the
repo holds, and that join stays barred. Forward only: nothing already written
is scrubbed or rewritten, and the idea of putting the name on the leak
scanner's term list is dropped with the rule.

The general lesson the policy-as-code programme keeps re-learning stands: a
boundary is only as good as the place it is enforced, and a rule that names
*categories* of repo will exempt whichever category the writer is standing in.
Bind the property, not the role.
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

**What the version signal is worth, stated (`160/520` SY6).** A skill is
doctrine by function: `queue-run` is the first thing an orchestrator executes,
and a change to it reaches a plugin-only adopter only inside the plugin. Since
2026-10-18 the plugin carries no `version` (each commit is its own version, the
trade chosen on `180/040`), so the `grep '"version"'` above finds nothing to
compare, and the drift check in this mode is **weaker than it reads**. The one
signal left is the plugin's `CHANGELOG.md`: a commit that changes what a skill,
command or method file tells a session to do carries its entry in the same
commit. Whether to put a `version` back, and bump it when a skill's behaviour
moves, is the principal's call (it reverses that choice), and is not taken here.

## The layer-override rule

atelier is the parent; a child repo is a layer over it, the same shape tiki's
config uses (default → org → site → device). The merge is read by an agent, not
computed by an engine, so the rule is a discipline:

- A child may **narrow** (make a rule stricter — e.g. faves forbids a build
  step; atelier is silent on it) or **append** (add repo-specific doctrine —
  e.g. a private child's product-specific bearings).
- A child may **never silently contradict** the parent. A child rule that is
  *looser* or *opposite* to a house rule is a **defect to surface**, not a
  quiet local win. Raise it: either the house doctrine is wrong (change atelier)
  or the child is (fix the child). Silence is the one disallowed resolution.
- On a live collision, the **stricter/safer** reading wins until the conflict is
  resolved upward. Children point up; the parent never points down for truth.
- A later date on a **default** is a ruled looseness, not drift; a later date
  on a **mandate** is the defect, unless the principal grants the exemption and
  it is recorded in the child. `GUARDS.md` § *Who may move a deferment's date*
  says which is which; an unlabelled date reads as a mandate.

### Who is a child, and what a child may hold (Mike's ruling, 2026-08-09)

Stated as doctrine because it was being applied without being written down —
which is how the economics-doc duplication survived across four repos while
every one of them passed every check.

**Adoption is the default, not the choice.** Every repo the principal works an
agent in is an atelier child, unless the principal rules a specific exclusion.
There is no third category of "repo we happen to use Claude in" — a repo outside
the model is one the doctrine, the floor and the review loop do not reach, and
that has to be a decision someone made rather than one nobody noticed. The
enumerating instruments (`tools/floorfleet.py`, `tools/pins.py`) answer *is it
current*; this rule is what makes "is it a child at all" answerable too, because
the honest denominator for both boards is **every repo the principal uses**, not
every repo already wired.

**A child may add. A child may not repeat, and may not conflict.** Three verbs,
and only the first is free:

- **Add** — repo-specific doctrine and extra guardrails, including ones stricter
  than the house. Unrestricted, and actively wanted; a child that has learned
  something its parent has not is the mechanism working.
- **Repeat** — restating doctrine the parent already owns. **Forbidden.** This
  is DRY, and the failure is not tidiness: a restatement is a second original
  that drifts silently, and readers cannot tell which copy is current. Point up
  instead, or use a **stamped** copy (§ *One statement, stamped copies*) where a
  pointer genuinely will not be read from where the reader stands.
- **Conflict** — a rule looser than, or opposite to, a house rule. **Forbidden
  unless the principal rules a specific exemption**, and the exemption is
  recorded in the child. This is the lane the bullets above were missing: an
  unresolved contradiction is a defect to surface, but a *ruled* one is
  legitimate and must be readable as such, or the next session reads a deliberate
  exemption as drift and "fixes" a decision the principal made.

The grounding, so this is not written from a heading. The estate's economics
doctrine was restated in four children — two private, plus `rpi` and `faves`.
Three of them carried a two-pool billing model the parent had already superseded
with billing-state-of-the-marginal-token, and a fixed model-to-role mapping the
house had already replaced with tier-by-risk; one private child named another —
a sibling — as "the canonical version", minting a second root. `faves` hit the
sharp end first: its copy "drifted 17 days behind a provider change, and misled
a session into arguing from a falsified fact", and was trimmed to repo-local
facts on the DRY ruling of 2026-08-09. That is the whole failure mode in one
repo: a repeat is not a redundant copy, it is a *falsifiable* copy, and it
falsifies quietly.

**Only parent and child is modelled here** (`390/010`, 2026-11-09; Mike's pick
from options offered, so an answer and not a ruling in his words). atelier does
not model a repo that consumes another's asset, nor repos that group by subject.
Those relationships, where the estate records them at all, belong in the estate
root's registry.

## Pointing up — reporting a doctrine problem to the house

*The route that was missing. § The layer-override rule says children point up
and the parent never points down for truth; § Who is a child says a child may
add but never repeat. Neither says **where** a child files a rule the house
owns — so the only mechanism a child session actually had was to write the rule
into its own onramp and note the debt in prose. Grounded on a private child,
2026-08-18 (§ The instance, below). Widened from "when a child earns a house
rule" to any problem with the doctrine on the principal's commission,
2026-08-23 — the section keeps its short name, which is how the rest of the
estate cites it.*

### The duty — every repo reports, atelier remediates

**Every repo of the principal's that works by this doctrine owes the house its
problems with that doctrine, and atelier is not exempt from its own rule** (the
principal's commission, 2026-08-23: *"the doctrine will direct all of my repos
that use it (incl atelier itself) to report potential issues they have with the
doctrine (with evidence where it is available) to atelier for consideration and
remediation by atelier"*). The commission is his repos, and the duty is no wider
than it (`160/300` RU5). An adopter outside that estate is not bound by it and
has no sibling checkout to write into and no peer channel to use, so the shapes
below that reach it are hold-and-flag, a fork and pull request, or an issue on
the public repo (issues are enabled); a vulnerability goes to `SECURITY.md`. The
stamped bullet in the child block reads "every repo" for such an adopter too:
read it as the principal's.

**What counts as a problem** — deliberately wider than the earned-rule case the
rest of this section was written for. A rule that is **wrong**; that is
**unworkable** in a situation it plainly covers; that is **ambiguous** enough
that two competent sessions read it two ways; that **contradicts** another rule;
that has gone **stale** against the world it describes; that is **missing**
(§ The test — whose rule is it); or that is **unfindable** — the parent owns it
and the reader could not get to it. *Potential* is the standard: a suspicion
with a real incident behind it is reportable, and no session has to be sure the
house is wrong before saying so.

**With evidence where evidence exists.** The incident, the command and its
output, the commit, the two readings — whatever makes the problem checkable by
someone who was not there (`EVIDENCE.md`). Where there is none, report it
anyway and **mark it unevidenced**: a suspicion labelled as one is useful, and a
suspicion dressed as a finding is the apex violation this whole model exists to
prevent.

**Consideration and remediation are atelier's.** The reporting session stops at
the report — it does not write the house's doctrine, and it does not get to
decide the report is unfounded on the parent's behalf. What it must equally not
do is **silently work around a rule it thinks is wrong**: the workaround costs
nothing today and destroys the only evidence the house would ever get, and it
leaves the next repo to rediscover the same problem from scratch. Working around
in silence is the failure this duty closes; the visible pair — narrow locally
*and* report up — is step 3 of § The route.

**A hand-up's mechanism claim is re-driven before it becomes house text.** A
report is testimony: the incident is evidence, but the child's account of
*why* it happened is a hypothesis (`CONCURRENCY.md` § The channel: a peer's
claim is a hypothesis to re-run; `00-APEX.md`: doctrine changes ride on
repeatable proof). Before atelier writes a mechanism into a method file it
runs the mechanism, and the record says it did. Three clauses adopted as
written from one hand-up each had to be corrected after a cold pass measured
them (`160/310`: the stash, the no-upstream and the remote-for-upstream
claims).

**atelier is bound identically, and the only difference is distance.** An
atelier session that finds its own doctrine wrong files a board item in
section `320` (findings filed via this section, whoever found them) exactly as
a child's finding would arrive there, rather than
fixing the wording in passing and moving on. The reason is not symmetry for its
own sake: a doctrine defect found and quietly patched leaves no trace of *what
was wrong*, so the class cannot be counted, and § When a rule keeps breaking —
which decides whether to restate a rule or climb to a mechanism — has nothing
to read.

### Check the parent's file first — never your own block

**The floor block is a lossy summary, and it is not evidence about what the
house doctrine says.** A child session that believes it has earned a house rule
opens the parent's actual doctrine file before it says so. Reasoning from the
inlined block instead is the failure that produces every defect below at once,
because a compression that drops a qualifier reads exactly like a rule that
never had one — and the gap the session then "finds" is a gap in the summary,
not in the house.

This is § One statement, stamped copies with its consequence followed all the
way down. A stamped copy drifting is the known hazard; the *second-order*
hazard is a copy being read as the source, because then it does not merely
misinform — it manufactures phantom debt, and the debt looks like diligence.

So the check that comes first, before any of the route below:

- **Open the canonical file, in full, at the section that owns the subject.**
  Not the block, not a grep of the block, not what a previous session's
  paraphrase implied.
- **If the parent already owns the rule, you have found a findability defect,
  not a doctrine gap.** File it as one: the pointer that failed you, the
  wording that misread, the section it should have named. That is a real and
  valuable finding, and it lands in a different place than a new rule would.
- **Only if the parent genuinely does not own it** does the route below apply.

**The check covers both shapes of deciding a house question locally.** One is
inventing the rule; the other is closing an open house question as settled,
and the check binds it identically: a house question is closed by the house,
and a ruling that looks adjacent is not a ruling on your question. The second
shape is the worse one. An invented rule is visible text a reviewer can find
and challenge; a wrong closure leaves a citable artefact wearing the
principal's authority, so the next session reads a ruling instead of an open
question and cites it. Grounding: a child that tried both (`310/090`,
2026-08-19); a capture recording an assistant's proposal as the
principal's, quoted back at him as his own position (`310/080`); and a
ruling on whether the bracket carries a disposition, read as refusing the
indexing question nobody had put (`310/060`).

### The test — whose rule is it

**Would this rule be true in a repo that shares none of this repo's stack?** If
no, it is the child's: add it locally and you are done — § Who is a child makes
adding free and actively wanted. If yes, it is the house's, and the child is
not its home.

The seam to watch: a rule can be *learned* on a child's stack and still be
*about* something every repo has. A rule learned while staging paths in a
shared checkout is about git, which every child has, so it is the house's from
its first sentence.

### The route

Four steps, none of them large.

1. **File it in the parent's board, not the child's onramp.** A board item under
   atelier's `docs/roadmap/` (its format, numbering and rebuild step are in
   `docs/roadmap/README.md`), carrying the incident, the class it belongs to,
   and the doctrine file it would land in. This is not delivering a fix from
   another session (`CONCURRENCY.md` § Stay in your lane) — filing a finding in
   the repo that owns the subject *is* the lane. Writing the doctrine is an
   atelier session's work; the child's session stops at the finding.

   **Filing has three working shapes, and a repo uses whichever it can reach**
   (PU-3, ruled 2026-08-22; the text named only the first, while the route's own
   first live exercise used the second). They are ordered by directness, not by
   preference — the one you can reach is the right one:

   - **Write the item directly** into a sibling atelier checkout. The
     queue-never-deliver carve-out sanctions it, and § Report without harming
     the parent is what makes it safe.
   - **Hand it over the cross-session channel** and let an atelier session file
     it (`CONCURRENCY.md` § The channel). This is how the first nine findings in
     board section `320` arrived (the section holds many more now, and most
     of the later ones came by the first shape's branch and PR). Note the
     channel's own law: a message reserves nothing and is volatile, so the
     hand-up is not *filed* until the atelier session lands the item — until
     then the finding lives only in the child's own record.
   - **Hold and flag** where neither exists — a fresh clone elsewhere, a CI
     context, no channel. Write the finding into the child's own session record
     marked as owed upstream, naming what it is owed to. That is not filing and
     must not be recorded as filing; it is a durable note for the next session
     in that repo that *can* reach the parent. Stating this shape is what stops
     an unreachable-parent session concluding it has no duty at all.

   **A doctrine defect that is itself a vulnerability takes the private route
   first** (`160/300` RU6). `SECURITY.md` puts "doctrine that, followed as
   written, leads an adopter into an unsafe practice" in scope and routes it
   privately; this section routes everything else to a public board item, and
   neither used to name the other. For that class: GitHub's private
   vulnerability reporting for an adopter, the private estate root for a member
   of the estate. The public item lands with the fix, not before.

2. **Carry the class, never the child's specifics.** atelier is public. A
   finding filed from a private child names the *shape* of what broke and the
   guarantee that failed — never the repo, its hosts, its clients or its
   secrets. Where the class cannot be stated without them, the finding belongs
   in the private estate root and the parent's item points at it.

   **This rule governs every surface the filing creates, not just the item's
   prose, and it outranks any rule about how to name one** (the principal's
   ruling, 2026-09-19, on the contradiction filed as `320/190`). **Branch
   names, PR titles, commit subjects and PR bodies are all published the
   moment the filing is pushed**, and a branch form of
   `report-<reporting-repo>-<subject>` — which this section's own reporting
   rules used to prescribe — publishes exactly what this rule forbids. So a
   private child's filing carries **no repo token on any of them**; where two
   rules disagree about a name, this one wins and the other yields. The
   contradiction was live, not theoretical: it was found because a public
   pull-request list already carried a private child's name in a head ref and
   a title, and **that cannot be retracted** — a deleted branch leaves the
   ref and title behind in the forge's own history. Which is the argument for
   the precedence: the failure mode here is one-way.

   **The same precedence reaches this doctrine's own prose** (`320/330`,
   2026-11-09; Mike's pick from options offered, so an answer and not a ruling
   in his words, and it replaces PU-2's 2026-08-22 choice to name the filing
   child). A worked example, bearing or instance in a public doctrine file
   names no private child repo: it says "a private child" and keeps the
   narrative. A public child may be named. Not worked examples, and so outside
   this rule: an act done to a repo (a grant table, an adoption list, a pin
   bump), which `RECORD.md` § *The record is public* still allows, and the
   provenance citations of the repo this doctrine was extracted from (the
   README, and pointers into its files), kept pending his word.
3. **The child keeps the consequence, not the rule.** The child still has to be
   safe in the window between learning and landing, and that need is real — it
   is what drives the local write. So the child may add **one line of
   repo-shaped instruction**: what a session in *this* repo must do, marked
   pending-upstream and naming the parent item it waits on. Not the
   generalisation, not the reasoning, not the incident narrative. A
   pending-upstream line is a **narrowing** (§ The layer-override rule), which
   a child may always do; it is also dated, addressed, and removable at the
   next pin bump — watched by nobody until an enumerator lands (`310/020`) —
   which is what separates it from a second original. (The principal ruled this
   allowance in preference to holding nothing, 2026-08-18: forbidding the local
   write without removing the exposure that causes it would leave the child
   knowingly unprotected, and that exposure is what produced the instance
   below.)

   **The marker: a convention now, a tool later** (`310/020`, 2026-11-09;
   Mike's pick from options offered, so an answer and not a ruling in his
   words). Every pending-upstream line, and every hold-and-flag note from
   shape 3, begins with the literal words `Pending upstream:`, then the date
   it was written (ISO, UTC) and the parent item it waits on, or `unfiled`
   where nothing is filed yet, then the one line. For example:
   `Pending upstream: 2026-11-09, 320/380 — the instruction for this repo.`
   One literal phrase means a plain `grep -rn 'Pending upstream:'` over a
   child's tree lists everything that repo owes the house, and a future
   enumerator has one thing to walk. The convention is all that is decided.
   The enumerator (the upstream mirror of `floorfleet`, reading for lines
   older than the item they name) is not built, and wants its own ruling,
   priced against the registry wiring `stampscan` is waiting on.

4. **The incident goes in the child's record.** A session log is the right home
   for what happened. `GUARDS.md` § A rule with no home is not a rule bars a
   record from being the home of the **rule**, not of the **evidence**; the two
   statements are not in tension. Evidence stays where it happened, the rule
   travels to where it governs.

**Closing the loop.** When the parent lands the doctrine, the child's
pending-upstream line is replaced by a pointer at its next pin bump — the pin
bump is already the occasion on which a child reviews its block against a moved
parent (§ The standard child doctrine block), so this needs no new ceremony: the
same occasion runs the `grep` above. A pending-upstream line that survives a pin
bump past its parent item is drift, and should read as one.

### Report without harming the parent

*Added 2026-08-23 on the principal's observation — "it shows we need a way for
those reports to occur without causing harm" — after a hand-up that was correct
in substance cost the parent three separate things in one evening. The report is
owed; the collateral is not, and none of it was necessary.*

**The instance.** A private child's session filed board section `380` by shape 1,
writing directly into atelier's tree. The finding was good and is now merged.
What it cost:

- It **re-used a branch name the parent had deleted minutes earlier**
  (`worktree-report-lies-0823`), so the branch reappeared pointing at unfamiliar
  commits. The atelier session read it as a rival session competing for its own
  line of work, stopped touching an area it had every right to work in, and
  wrote that misreading into a session record.
- It **left the finding on an unmerged branch with no PR** and went quiet. The
  item existed in a commit and on no board. Nine hours later it was still
  invisible to `docs/ROADMAP.md`.
- It **rebuilt the shared generated index** from a base the parent had already
  moved past — recoverable, but the merge is the parent's to carry.

So four rules, each answering one of those:

- **Name the branch for the report, not for the parent's work** — and name it
  `report-<subject>-<HHMM>`, with **no repo token**. The `report-` prefix is
  what reads as a hand-up in a branch list; a name shaped like the parent's own
  worktree branches reads as competition. The form used to be
  `report-<reporting-repo>-<subject>`, and it was **wrong on a public parent**:
  a branch name is published on push, so it disclosed the very thing § *The
  route* rule 2 forbids a private child to disclose. Rule 2 wins (the
  principal's ruling, 2026-09-19); this rule yields, and the neutral form is
  now uniform rather than conditional on a visibility the parent cannot see
  from its own tree. And **never re-use or re-create a branch name** — the
  parent may have just finished with it, and a name coming back from the dead
  is the single most misleading thing a branch can do.
- **Say what it is in the first line of the commit and in the PR body:** that
  this is a filed finding rather than parent work, and — **only if the
  reporting repo is one whose name may be published** — which repo it is. A
  private child says *"a private child"* and nothing more; commit subjects, PR
  titles and PR bodies are all public on a public parent, so rule 2 reaches all
  three. The parent should never have to infer the *kind* of change from the
  diff; it does not need the reporter's identity to triage it.
- **Open the PR before you stop.** A finding on an unmerged branch is a message
  left in a drawer — it has none of the properties filing was for. If the
  session cannot open one, that is the hold-and-flag shape above, and the
  finding goes in the reporting repo's record instead. Merging is the parent's
  call and may take days; leaving nothing to merge is the failure.
- **Touch your own item and nothing else.** Generated indexes are rebuilt, never
  hand-merged (`CONCURRENCY.md` § Claiming work). Claim nothing from the
  parent's queue, edit no doctrine, and take no worktree in the parent for
  anything but the filing itself. **Expect an index conflict rather than try to
  avoid it:** a rebuilt index made from a base the parent has since moved past
  arrives conflicting though its floor run is green, and resolving it is the
  parent's (below). Do not rebase onto a moved `main` to dodge it. **Your item
  number is provisional until the parent lands it:** two filers on one base take
  the same next number and the forge sees two new files with different names, so
  carry no reference to your own number inside the filing.

**And the parent's half, which this instance also exposed.** A filed finding
with no PR has no owner at all — the reporter has stopped and the parent does
not know it is there. So an atelier session that finds one **lands it**: open
the PR, merge on the floor's own evidence, and say plainly in the PR that the
content is the child's and unreviewed. That is not adopting the finding; it is
putting it on the board where consideration can happen. Do not rewrite the
reporter's history to tidy it — a rebase of someone else's pushed branch buys
nothing and destroys the record of how it arrived. Four things make that half
something a session does rather than something it means to do (`160/300`
RU2–RU4, RU12):

- **Look at open hand-ups at open.** Landing one was written as an act and had
  no trigger: eleven stood open for three weeks until the principal asked. An
  atelier session's start-of-session read includes the open hand-up PRs
  (`gh pr list --state open --json number,title,headRefName,createdAt`, read for
  a `report-` head ref or a hand-up title), and landing any it finds is the first
  act of the session, ahead of its own work. The read is one command, so it does
  not wait for the enumerator `310/020` waits on.
- **Check before merging, by command, because the harm is one-way.** For each
  PR: `gh pr view <n> --json headRefName,title,body,files`. The head ref starts
  `report-` and carries no repo token unless that repo is public; the title and
  body say it is a hand-up and name no private repo; the files are the filed
  item, the regenerated index and nothing else. A branch name and a title are
  published once pushed and cannot be retracted, so a failure here is a note on
  the PR and a record, not something a merge or a deletion undoes. A
  branch-name and title lint at the reporter's push, or a `handupscan` run at
  merge, is the next rung (`GUARDS.md`); it is not built, and is not this
  section's to build.
- **Resolve an index conflict by merging, in the parent's own worktree.** A hand-up
  that rebuilt `docs/ROADMAP.md` over a base `main` has since passed arrives
  `DIRTY` although its floor run is green. In an integration worktree of the
  parent, `git merge --no-ff` the report branch, take the conflicting index by
  running `tools/board.py --rebuild` rather than by hand, and commit the merge: a
  merge commit, never a rewrite of the reporter's branch. That is the move the
  parent already makes, now written where the parent reads.
- **Run `board.py --check` after each landing, and settle a number collision
  yourself.** The number a hand-up takes is settled at the parent's merge, not
  at the reporter's push, so only the parent can see a collision. The
  later-landing item moves to the section's next free number, and the parent
  makes the move, never the reporter.

### The same route between any two repos

*Added 2026-11-09 from `310/120` and `310/140`, two commissions drafted as one
rule; Mike's pick from options offered, so an answer and not a ruling in his
words. The first, 2026-09-12: "Find better ways for sessions working on child
repos to feed back ideas, problems or whatever to 'parent' repos like atelier
to consider and act upon", and likewise a child of the estate root wanting to
add an asset back to it. The second, 2026-09-29: "PR's could be the best way
for a session working in one repo to send an idea or whatever to another repo".*

§ *Pointing up* is the case where the target is atelier, which is public, and
the subject is doctrine. The same route serves any pair of repos (a child to a
parent that is not atelier, a repo to a sibling, a parent to a child), with
three differences and one carry-over:

1. **The carrier files an idea or finding; it never delivers the fix.** The PR
   adds a board item or a request file to the target, in the target's own
   format, and the target's session decides and does the work. Work lands in
   the repo it changes, and a PR that carries the fix reduces the target's
   session to pressing merge, which is delivery from another session
   (`CONCURRENCY.md` § *What the channel is not*: queue, never deliver).
2. **Redaction keys on the target's visibility.** A public target gets rule 2
   of § *The route* unchanged: the class only, and no repo token on the branch,
   PR title, commit subject or body. A private target may be sent specifics
   (names, hosts, the sender's own detail), because the filing publishes
   nothing to a wider audience. That relaxes what the target's readers may see
   and nothing else: a secret value never travels in a PR, in either direction.
3. **No write access to the target means an issue.** Where an issue cannot be
   opened either, hold and flag (shape 3 above), with the `Pending upstream:`
   marker.
4. **The harm-avoidance rules carry over, not a difference:** a
   `report-<subject>-<HHMM>` branch with no repo token where the target is
   public, a first line that says this is a filed finding, the PR opened before
   the session stops, and nothing touched but the sender's own item (§ *Report
   without harming the parent*). The target's half carries over too: a session
   that finds an orphaned report lands it.

**Not decided: how the target learns a PR arrived.** The orphaned-report
failure was a PR nobody looked for. The candidates are the enumerator
`310/020` prices, or a talk-first message to the target's live session
(`CONCURRENCY.md` § *The channel*). Until one is chosen, the sender names where
it filed in its own record, and the route is as unwatched as § *The instance*
says the upward one is.

### The instance

A private child, 2026-08-18. (This text named the repo from 2026-08-22, on
PU-2, whose grounds are in the verdict
`docs/reviews/2026-08-21-0820-pointing-up-cold.md`; it was withdrawn on
2026-11-09, `320/330`, by rule 2 above.) A session staged two
paths explicitly, committed, and destroyed a sibling's session-log entry that
had been sitting in the shared checkout's index before it arrived. Real failure,
correctly diagnosed down to the cause — an index outliving the ref that fed it.

It then reached for the rule and read **its own block**, which compresses the
house rule to *read the staged hunk headers before every commit*. Read that way,
the rule only covers what you staged, so the session concluded the house had a
gap, wrote roughly three hundred words of new rule into the child's floor block,
and marked it owed upstream.

The house owned the rule, but it prescribed a path-blind command for it. As
`CONCURRENCY.md` § The trigger stood on 2026-08-18 it said to run
`git diff --cached -U0 | grep '^@@'` and compare the hunk headers, which prints
no path; the block's phrase was a faithful compression of the parent's own
sentence, not a lossy one. The command was corrected on 2026-08-22 (PU-1) to
plain `git diff --cached`, which reads the whole index, including the paths you
did not stage. What was owed upstream was **that finding**, filed by the route
this section teaches, and not a second copy of a rule the parent already owned:
the debt marker pointed at a rule with an owner.

Four things went wrong and the session could see none of them from where it
stood, which is why this section exists rather than a correction to that child:

- **The debt had no owner and no enumerator.** A marker in a child's onramp is
  read by future *child* sessions; the act it asks for belongs to an atelier
  session. `floorfleet.py` and `pins.py` enumerate the estate downward — *is
  this child current?* Nothing enumerates upward — *is anything owed to the
  house?* That is § Enumeration, not assumption aimed at the direction it was
  never pointed at.
- **It minted a second original that could not even be stamped.** A stamped
  copy names its canonical source; a rule authored in a child has none to name,
  because the child *is* the only original. The moment the parent writes it, the
  child holds an unstamped duplicate — and `stampscan` cannot see it, because it
  never claimed to be a copy.
- **It spent the hottest read path in the fleet.** § The standard child doctrine
  block is lean by design because every child session pays its length at every
  open. House-shaped narrative is precisely what belongs behind the pointer.
- **It set the parent's frame from the child.** Doctrine here is *extracted from
  evidence*. Had this landed, atelier would have been rewriting a child's
  paragraph — inheriting its vocabulary, its symptom list and its framing as the
  default shape.

**And the block's own pointer was part of the cause.** The concurrency bullet
sent the reader to `CONCURRENCY.md` § The channel; the index rule lives in
§ The trigger. A session that *did* follow the pointer landed in the wrong
section and found nothing. Both defects — the pointer and the lossy phrase —
were fixed in the canonical block on this commit and reach the fleet at each
child's next pin bump.

**Stated honestly: this section is rung 1 until something enumerates it**
(§ When a rule keeps breaking). Nothing today answers *what does the estate owe
the house?*, and the failure addressed here is exactly an unenumerated absence
— the same defect `floorfleet.py` closes in the other direction. The instrument
is queued as its own board item. Until it exists the discipline rests on a
child session filing at the moment it is earned, so do not read the route above
as a closed loop: it is a route, and it is currently unwatched.

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

## When a rule keeps breaking — climb, never restate

*Mike, 2026-07-29: sessions keep hitting an issue that is written down three
times. Writing it a fourth time reaches exactly the readers the first three
reached.* Three rungs, cheapest first — **stop at the first that fits**,
where *fits* means **would have prevented the recorded occurrences**: test
the rung against the incidents before stopping on it, because rung 1 always
fits in the weak sense (a rewording is always available) and the worked
example below is one where rungs 1 and 2 both had answers that would have
failed (RL1, 2026-08-02). All
three change the *system*; none changes the wording, which is the move that
feels like progress and reliably is not.

1. **Framing — was the rule findable from where the reader stood?** A rule can
   be present, correct, and still invisible to the person who needed it,
   because its grammar assumed a situation they were not in. Grounded: the
   review trigger was phrased around *a change*, so a reader holding a design
   rather than a diff found every sentence shaped for the diff and concluded
   the answer was no (Mike, 2026-07-19; `REVIEW.md`). The fix lands at the
   point of use — re-key the trigger — never in a louder sentence.

2. **Mechanise at the moment of failure.** Can a check see the instant the rule
   breaks? Then build it, and aim it at the **trigger**, not at the rule text:
   all three occurrences of the private-repo × posture join happened at one
   identical moment, and a check aimed at that moment would have caught all
   three. Recurrence, not severity, is what earns a check — a severe-but-once
   failure is a judgement call; a trivial-but-thrice failure is a defect in the
   system that keeps producing it. `reviewscan`'s review-line lint is the
   worked example: a rule that had been written three times became a check
   once, and stopped recurring.

3. **Remove the situation.** Where no check can see the failure, ask whether
   the *arrangement that produces it* can be deleted. This rung is the newest
   and the least reached for. Worked example, 2026-07-29: cold reviewers kept
   reading a brief's deferred section before committing their own findings.
   Rungs 1 and 2 both had answers — reword the label, lint the label — and both
   would have failed, because **reading a file is atomic** and the label sat
   inside the very thing it warned about. The fix was to move the bytes: the
   deferred material into a sibling file, so the failure has nowhere left to
   happen (`REVIEW.md` rule 1). The question that finds this rung: *what would
   have to stop being true for this failure to be impossible?*

**What is owed, and what is earned (2026-11-09).** The ladder above is for a
rule that has *broken*. The policy-as-code programme's aim, that doctrine be
both enforced and directive, asked a prior question: is a rule owed both
framing and a check from the day it is written? The answer has two parts.

- **Framing is owed by every rule, up front.** Each rule is written down
  clearly and keyed to the situation the reader will be standing in when they
  decide, not to a condition a scanner can evaluate. This is rung 1 made a
  design obligation, not a remedy held back until the third breakage.
- **A mechanism is owed only where its value beats its cost.** A check is added
  where it is worth building, ranked against every other piece of work on the
  board like any other item; no rule is owed one by existing. Recurrence is the
  cheapest evidence of value, so rung 2's *recurrence earns a check* stands as
  the usual way a rule qualifies, not the only one.

So the ladder is unchanged in how it is climbed (stop at the first rung that
would have prevented the recorded occurrences), and gains a floor under it:
rung 1 is never skipped, and a check not built is a decision with its reason
recorded, not silence. Mike, 2026-11-09, `020/240`: *"Written always, checker
by value"*, his pick from options the queue run offered, so an answer and not
a ruling in his own words. It rests on his words of 2026-11-08
on `115/170` (the proportionality question), asked whether to cap guard work:
*"This sounds like yet another artifical limit that is not helpful. It is about
balancing importance and priority to do the work that is most valuable"*. No
blanket check-building follows from the aim; where each rule stands is the
census's output (`020/220`).

**The ladder only gets climbed if the trigger is countable.** Nothing here can
currently answer "how many times has this broken?" — recurrence is noticed by
someone's unease, which is how a rule reaches its third occurrence unpromoted.
Making the count mechanical is the anti-slop registry's mining work, and it
earns a **cadence rather than one pass**: a survey run once tells you about the
past, and the defect this rung addresses is continuous. Until that runs, treat
a second occurrence you *happen* to notice as the trigger — the ladder is
cheap, and rung 1 costs a paragraph. Two thresholds, two acts, deliberately
(RL3, 2026-08-02): a *second* noticed occurrence triggers climbing this
ladder, while the **>2 promotion rule** (act at the third instance) governs
promoting a recurring pattern into doctrine — the ladder is cheap enough to
start early; minting doctrine is not. Both stand until R1 makes the count
mechanical.

## One statement, stamped copies — never three originals

*Mike, 2026-07-29: the same point should not sit in three different places;
where three repeats say slightly different things, consolidate them into one
clean statement that covers all of it.* Agreed, with the distinction that
decides which repetitions are defects and which are the mechanism working:

- **Three independent statements of one rule is the defect.** They drift apart
  the moment one is edited; none is canonical, so a reader who finds one has no
  way to know the other two exist, and whoever fixes one leaves two wrong.
  Consolidate: merge the angles into a single statement in the file that owns
  the subject — *covering* all three readings, not picking one and deleting the
  rest, since three formulations usually means three real facets and a
  consolidation that drops two is a silent scope-cut.

- **One canonical statement plus copies at the point of use is correct**, and
  frequently necessary: rung 1 above says non-compliance is usually a
  findability failure, and a pointer is less findable than a sentence sitting
  where the reader already is. The copy is legitimate only when it is
  **stamped** — marked as a copy, naming its canonical source, and
  narrowing-free: it may compress the parent, never contradict it — except
  the safety floor, whose copies are verbatim (§ *The standard child doctrine
  block*). The child
  doctrine block, `skills/review-brief`, and the reviews-README template all
  carry that header for this reason.

- **The failure mode of a stamped copy is drift**, and it is real rather than
  theoretical: the review-brief skill was found still carrying an
  artefact-shaped trigger its parent had already retired (2026-07-19 F3), and
  the reviews template had drifted the same way one sweep earlier. `stampscan`
  was built to catch exactly this class; its parser defect was fixed and the
  scanner **wired advisory in atelier's own CI** (2026-08-05, the D2 ruling —
  it watches this repo's stamps and warns, without blocking). Registry wiring
  to children stays barred on the child-side `source=` resolution story
  (ROADMAP, D2 residue), and the blocking flip is a separate later ruling —
  so the discipline is watched-advisory here and convention in the children.
  Said plainly rather than implied away: for a child repo, an unwatched
  convention is still rung 1 territory, not rung 2. (This paragraph
  previously recorded the pre-fix state — corrected 2026-08-06, SD2.)

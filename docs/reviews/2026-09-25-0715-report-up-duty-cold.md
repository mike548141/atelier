# Cold pass — the doctrine-reporting duty, the route's three shapes, and the no-harm rules for a hand-up

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md`.
**Why it earns a review:** this is the rule by which every repo in the fleet
reports a defect in the house doctrine to the parent; if the route is wrong or
harmful, defects stop arriving or arrive in a form that damages the public
parent.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `5bb78f2` (2026-08-24) — the landing commit
- `54201e0` (2026-09-18) — the widening: step 3's "self-removing" reworded
  (`310/110`)
- ⚠️ `48c181f` (2026-09-20) — later, separately-queued work (`160/360`) rewrote
  § *The route* rule 2 and the first two bullets of § *Report without harming
  the parent*. Review this delta's surfaces at HEAD and name what the later
  commit changed

Delta paths:

- `docs/method/PROPAGATION.md` § *Pointing up* — the widened subtitle; the new §
  *The duty — every repo reports, atelier remediates*; the three filing shapes
  inside § *The route* step 1; the new § *Report without harming the parent*
- `docs/method/PROPAGATION.md` § *The standard child doctrine block* — the
  bullet-count sentence, and the `floor` region's new **Doctrine problems point
  up** bullet
- `docs/build/templates/CLAUDE.md` — the same bullet, stamped
- `CLAUDE.md` — atelier's own § *Hard constraints* gains the duty

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the three filing shapes cover the cases a child actually meets (a child
with no remote; a child whose principal is not atelier's; a private child whose
finding cannot be stated without private detail) — the fleet's hand-ups since
2026-08-24 are the evidence: read the merged `320/…` items at HEAD as *data
about which shape each took*, not as verdicts. Whether the no-harm rules are
checkable by the parent at merge (what does a parent session actually run to
verify a hand-up did no harm) or only aspirational. Whether the bullet-count
sentence is right by counting at HEAD. **Non-goal:** the principal's commission
of the duty.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   duty says *every repo reports, atelier remediates* — attack whether a duty
   with no check behind it is the class the house keeps re-breaking, and whether
   the route's step 1 gives a child enough to file without reading atelier's
   internals.
2. **Correctness & quality.** Diff the three commits for the in-scope paths.
   Check every cross-reference resolves at HEAD; check the stamped bullet is
   inside the floor region the scanner compares; count the bullets.
3. **Completeness / harvest.** Search for every other surface describing how a
   child reports: `skills/`, `docs/build/REPO-STANDARD.md`, `CONTRIBUTING.md`
   and its template, `SECURITY.md` (does the security-disclosure route and the
   doctrine-report route agree on where a *security* doctrine defect goes?).
4. **Security & privacy** — mandatory. atelier is PUBLIC and hand-ups arrive
   from private children. The no-harm rules are the privacy control: test them
   against the worst case — a child whose finding *is* a leak (a term, a path, a
   person) — and say whether the rules as written stop the finding from carrying
   the leak into the parent's public board. Discharge the house scanner by
   grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `stampscan`, `blockscan` (if registered), `linkscan`, `pathscan` over
  `docs/method`, `docs/build`, `CLAUDE.md` at HEAD, floor invocations
- the floor on both planes at HEAD
- the bullet count, by counting

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-08-23-1314-recovery-then-five-defects-in-the-instruments.md`
  and `docs/sessions/2026-09-18-0114-queue-run-hand-up-fixes.md`
- the board items `docs/roadmap/310-*/110-*.md` and the
  `320-*/…reachable-parent…` item that the landing commit widened

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `RU`: `RU1`, `RU2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

# Verdict — phase 1, written 2026-09-25T07:18Z

## Provenance, repeated

- **Spawn:** a fresh Fable subagent (`claude-fable-5-1`), spawned by the batch
  orchestrator with this brief as its only framing. I am not the author's session
  and was not instructed by it; the orchestrator holds the `.deferred.md` sibling
  outside the worktree and had released nothing of it when this section was
  written. Reviewer-plus-orchestrator shape, both seats Fable, disclosed above.
- **Tier:** Fable, checked at spawn.
- **What I read:** this brief; `docs/method/REVIEW.md` and `00-APEX.md` at HEAD;
  the three named commits' diffs and `--stat` lists; the delta paths at HEAD
  (`PROPAGATION.md` in full, the scaffold template, atelier's `CLAUDE.md`); the
  cross-referenced sections of `CONCURRENCY.md`, `GUARDS.md`, `SECURITY.md` and
  its template, the `CONTRIBUTING.md` template, `docs/build/REPO-STANDARD.md`, the
  `skills/` tree by grep, `docs/roadmap/README.md`, section `320`'s README and the
  headline line of each `320` item, the `310` items other than the two barred
  ones, `.githooks/pre-commit`, `.github/workflows/ci.yml`, `tools/floor.py` and
  `tools/blockscan_map.json`. Forge data by `gh` (read-only): the PR list with
  titles and head refs, four PRs' file lists and check states, three child
  repos' visibility. **Barred and not opened:** the queue pointer, `310/100`,
  `310/110`, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, every
  prior verdict, every other `2026-09-25-0715-*` brief. Sweeps ran through
  `tools/coldsweep.py` with the three item paths added; no `--include-barred`.
- **Brief-framing correction (rule 1):** the brief bars "the `320-*/…reachable-
  parent…` item". That item is `310/100`, not `320`; I barred it by its real
  path. And the brief's list of scanners to re-run includes `blockscan` "if
  registered" — it is not in the registry; it runs as a bespoke CI step, and I
  ran it in that form.

## Lens answers

### Lens 1 — approach and assumptions

Load-bearing assumptions, named by me: (A1) a duty stated in the floor block is
read by a session that never opens atelier, so the block must carry enough to
file *safely*, not only enough to file; (A2) a child that can reach the parent
can also produce a filing the parent can merge; (A3) "the parent lands it" is
an act some atelier session will be triggered to perform; (A4) "every repo" is
the estate's children.

**Is "a duty with no check behind it" the class the house keeps re-breaking?**
The evidence cuts both ways and the honest reading is the narrower one. The
child-side half works as a discipline: `320` held nine items when the delta
landed and holds **forty** at HEAD, and the adding commits since 2026-08-24 show
a steady arrival (twenty-one hand-up PRs between 2026-08-26 and 2026-09-24).
atelier's own half is exercised too — `310/130` and `320/340` were filed by
atelier sessions against atelier's own doctrine rather than patched in passing.
What is *not* working is everything the duty asks of the **parent** and of the
**filing's surfaces**: two of the three open hand-up PRs are unmergeable and
have stood five days through thirteen commits on `main` (RU3, RU4); two closed
PRs carry a private child's name where no scanner looks (RU2); and the block a
private child reads never tells it not to name itself (RU1). So the class is
not "duty unmet" — it is **"duty met, harm unchecked"**: the four no-harm rules
protect the parent from confusion (recoverable) and reached the floor; the one
rule that protects a child from a one-way disclosure did not. A1 fails.

**Does step 1 give a child enough to file without reading atelier's
internals?** No. Step 1 names the item's *content* and never its *form*: which
section, the item grammar, the tri-state, that the index is generated, or the
`docs/roadmap/README.md` that says all of that. Real filers diverged exactly
here — two rebuilt the index and arrived DIRTY, one did not touch it (RU3, RU11).
A2 fails in the common case where the parent moves.

A3 has no trigger anywhere in the onramp (RU4). A4 is the silent narrowing —
the doctrine explicitly supports plugin-only adopters with no checkout, and for
them none of the three shapes reaches atelier (RU5).

### Lens 2 — correctness and quality

- **The three commits, diffed for the in-scope paths.** `5bb78f2` adds § *The
  duty*, the three shapes under step 1, § *Report without harming the parent*,
  the floor bullet (canonical and template), the atelier `CLAUDE.md` constraint,
  and the count. `54201e0` rewords step 3's "self-removing" to "removable at
  the next pin bump — watched by nobody until `310/020`'s enumerator lands"
  (correct: nothing removes it). `48c181f` adds the "governs every surface"
  paragraph to § *The route* rule 2 and rewrites the first two no-harm bullets
  (branch form `report-<subject>-<HHMM>`, no repo token; first line names the
  repo only if it may be published). **It did not touch the floor bullet or the
  template** — see RU1 for why that matters and why no check saw it.
- **Cross-references at HEAD:** every section the delta cites resolves —
  `CONCURRENCY.md` § *The channel*, § *Stay in your lane* (the "queue, never
  deliver" carve-out is there verbatim), § *Claiming work* (generated index
  regenerated, never hand-merged), § *Integration hygiene*; `GUARDS.md` § *A rule
  with no home is not a rule*; `PROPAGATION.md` § *The test — whose rule is it*,
  § *When a rule keeps breaking*, § *Enumeration, not assumption*; `310/020`
  exists and is open; `EVIDENCE.md` exists. `linkscan` clean over the in-scope
  paths.
- **The stamped bullet is inside the compared region** — line 171 of the
  canonical `floor` region, line 83 of the template's `stamp` region;
  `stampscan` reports the copy identical (91 lines), and a text diff of the two
  regions is empty.
- **The count, by counting:** nine `- **` bullets between `floor:begin` and
  `floor:end`; nine in the template's stamped region. "Nine" is right.
- **Overclaims found:** one stale-by-growth sentence (RU8); the parent-side
  "lands it" is written as a rule and behaves as a hope (RU4).

### Lens 3 — completeness and harvest

Surfaces that describe how a child reports, swept: the floor bullet (canonical
and template), § *Pointing up* itself, `CLAUDE.md` § *Hard constraints*,
`GUARDS.md` § *A rule with no home* (points at § *Pointing up*),
`CONCURRENCY.md` § *The trigger* bearing (points at it), `README.md` line 67
("point up"). `skills/` carries nothing on reporting beyond `queue-run`'s
tier hand-up, which is a different sense of the phrase. `REPO-STANDARD.md`
and the `CONTRIBUTING.md` template describe the doctrine block and the floor,
never the report route — consistent, since both point at the block. **The
security-disclosure route and the doctrine-report route disagree at their
intersection and neither names the other** (RU6). **No surface names a route
for an adopter outside the estate** (RU5): the repo has issues enabled and no
doctrine, README or root `CONTRIBUTING.md` mentions them. Both `310/120` (a
different *parent*) and `310/130` (parent-only accommodations) are adjacent
and neither covers RU5 or RU6.

### Lens 4 — security and privacy (mandatory)

`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which in this shared worktree is other passes' unstaged drafts, and this
is a landed-delta review. The work has no code surface — prose in four Markdown
files — so the OWASP code-altitude catalogue has nothing to bite on; the lens
runs at design altitude, where the delta *is* the privacy control for a public
parent receiving reports from private children.

**Worst case tested — a child whose finding *is* a leak** (a term, a path, a
person). Rules as written: rule 2 forbids the specifics in the item and, after
`48c181f`, on the branch name, PR title, commit subject and PR body; the
estate-root pointer takes what cannot be stated as a class. Mechanical backstop:
the floor scans **tree files only** — `.githooks/` holds `pre-commit` and
nothing else; `tools/floor.py` has no plane for commit messages, branch names or
PR metadata (grep for any of them: none). `leakscan` with the term list runs on
the filer's hook, so a listed *term* in the item body is caught on a machine
that holds the list and not in CI; a *path* or a *repo name* is caught by
nothing unless it is a listed term; and the four surfaces `48c181f` names as
published-on-push and irretractable are reached by no scanner at all. So the
rules stop the leak **only where the filer read the full section**; the block
a private child reads is silent on it (RU1), and nothing at merge checks
(RU2). The delta's own threat enumeration at landing covered the parent's three
costs and not the child's disclosure — the threat that was then found live
(`320/190`) — and the delta's own prose names a private child (RU7).

House scanner, discharged by grounds in one line: the floor ran green on both
planes at HEAD (ledger below) and `leakscan` ran with the local term list on
the hook plane; neither reaches the surfaces this lens is about.

## Findings

### RU1 — MAJOR — the floor bullet carries the parent-protecting rules, not the child-protecting one

The block "binds even if atelier is never read" — that is its stated purpose.
Its *Doctrine problems point up* bullet (canonical line 171, template line 83)
tells a child to name the branch for the report, say it is a hand-up in the
first line, open the PR and touch only its own item. It never says **carry the
class, never your specifics**, and it never says a private repo's name must
not appear on the branch, title, subject, body or item. A private child
following the block to the letter can file a compliant-looking hand-up that
discloses itself on four irretractable surfaces. The two recoverable-harm rules
reached the floor; the one one-way-harm rule did not.

Grounding: `48c181f` (2026-09-20) rewrote the canonical bullets on the
principal's ruling and left the block untouched. The co-change check that
exists for exactly this (`blockscan`, `320/300`) was not on that commit's branch
(`merge-base --is-ancestor be8a003 48c181f` → no), and at HEAD it **cannot see
the change** — `blockscan --against 48c181f^` reports nothing for the
`doctrine-problems` bullet, because the edit sits in `###` subsections of the
mapped `##` section (`320/340` records the class). Post-ruling filings comply
(four of four branches `report-<subject>-<HHMM>`, four of four titles say "a
private child" or name a public repo), but those came from sessions that read
the section, not the block.

*Counsel:* one clause in the bullet, both copies: "class only — a private repo
names itself on none of the surfaces a filing creates (branch, title, subject,
body, item); rule 2 of § *The route*". And extend `blockscan`'s map to the
subsections, or accept `320/340`'s residual explicitly in the map's comment.

### RU2 — MODERATE — the no-harm rules are checkable at merge by eye only; one-way surfaces unread

The brief asked what a parent session actually runs to verify a hand-up did no
harm. The answer at HEAD is: **nothing named.** I ran `gh pr list --json
headRefName,title` and `gh pr view --json files` by hand and that was the
check. Two closed PRs (2026-08-26 and 2026-09-06) carry a private child's name
in head ref and title — `48c181f`'s own message says so, and says it cannot be
retracted. That is two recorded occurrences, which § *When a rule keeps
breaking* names as the ladder's trigger; the rung-2 check (a branch-name and
title lint at pre-push, or a `handupscan` the parent runs at merge) is cheap and
does not exist.

*Counsel:* write the parent's merge-time check into "the parent's half" as a
command (branch form, title says hand-up, no repo token unless the repo is
public, files are the item plus the index and nothing else). Queue the rung-2
instrument as its own item; it is not `310/020`, which waits on a child-side
marker convention this needs nothing of.

### RU3 — MODERATE — shape 1 on a generated index arrives unmergeable once the parent moves

PRs 84 and 86 (both 2026-09-20): `floor` SUCCESS, `mergeStateStatus: DIRTY` —
each rebuilt `docs/ROADMAP.md` from a base `main` moved past (thirteen commits
since 2026-09-20T12:00Z). PR 87 (2026-09-24) touched no index and is CLEAN,
but it edits an existing item; a *new* item without a rebuild reds the `board`
check on CI ("the generated roadmap index never drifts from its item files",
enforced). So a child adding an item cannot produce a PR that is both
floor-green and conflict-free unless the parent stands still. The no-harm rule
4 ("generated indexes are rebuilt, never hand-merged") and the parent's half
("do not rewrite the reporter's history … a rebase … destroys the record") are
both right and together name no way through: the move that works — merge
`main` into the report branch and rebuild, a merge commit rather than a
rewrite; or `rebuild --from-index` at the parent's local resolution — is
written nowhere the parent will read at the moment it matters. The instance
paragraph records this exact cost as "recoverable, but the merge is the
parent's to carry", and rule 4 answered a different cost.

*Counsel:* state the resolution in the parent's half in one sentence, and
tell the filer in rule 4 to expect the index conflict rather than to avoid it.

### RU4 — MODERATE — "an atelier session that finds one lands it" has no trigger

Three hand-up PRs stand open (two since 2026-09-20, one since 2026-09-24);
`main` took thirteen commits from at least three sessions in that window, and
none landed them. Nothing in atelier's read order, `session-open`, or the
`queue-run` skill says to look at open PRs — the parent-side enumerator is one
`gh pr list`, so this is not blocked on `310/020`. The section already calls
itself "unwatched"; that honesty covers the child side. On the parent side the
rule is written as an act and is performed by nobody, which is the "message
left in a drawer" the section says is the failure — now on the parent's side of
the drawer.

*Counsel:* add "open hand-up PRs" to the session-start read (a `gh pr list`
filtered on the `report-` head or the hand-up title), and let the claim-and-land
be the first act of any atelier session that finds one.

### RU5 — MODERATE — the duty binds "every repo"; the shapes reach atelier only from the estate

Shape 1 assumes a sibling checkout the filer can push a branch to (the
worked instances all have push rights); an adopter can only fork and PR, which
the text never names. Shape 2 is the estate's peer channel. Shape 3 is
hold-and-flag, which by the text's own admission "is not filing". The doctrine
explicitly supports **plugin-only adopters with no checkout** (§ *The
bundled-mode variant*) and stamps them the identical bullet, so for that class
the duty is unmeetable as written. The repo has issues enabled (verified) and
no live surface says so; `README.md` mentions neither adopters, issues nor
forks; there is no root `CONTRIBUTING.md`; `SECURITY.md` is the only
external-reporter route and is security-only. `310/120` is about a different
*parent* and does not cover this.

*Counsel:* name the external form of shape 1 (fork + PR, or an issue) and say
plainly which shapes are estate-only. Cheap, and it is the difference between a
duty every adopter can meet and one only the estate can.

### RU6 — MODERATE — the security-disclosure and doctrine-report routes disagree where they meet

`SECURITY.md` puts "doctrine that, followed as written, leads an adopter into
an unsafe practice" in scope and routes it **privately**; § *The duty* routes
every doctrine problem to a **public** board item. Neither names the other. The
intersection is live: `320/190` was a doctrine rule that, followed as written,
leaked a private child's name — filed publicly, safe only because its class was
public-safe. The next such defect may not be.

*Counsel:* one sentence in § *The route*: a doctrine defect that is itself a
vulnerability (SECURITY.md's third in-scope bullet) takes the private route
first — GitHub's advisory for an adopter, the estate root for a member — and
its public item lands with the fix.

### RU7 — MODERATE — the delta's own no-harm section names a child the forge reports PRIVATE

§ *Report without harming the parent* § *The instance* names the reporting
child. `gh repo view` on 2026-09-25 returns `PRIVATE` for it. The naming
carries no ruling of its own: the `cbom` naming in the other instance cites
PU-2 and its veil-defeated reasoning; this one, added 2026-08-23, was the
author's choice. Sixty lines above it, rule 2 now says a private child's name
belongs on none of a filing's surfaces. `320/330` already holds the question
for the principal; what this pass adds is that the surface under review is the
one carrying it, and that the PU-2 reasoning was never stated for it.

*Counsel:* `320/330` option (a) for this instance at least — "a private child"
keeps every word of the narrative that does work.

### RU8 — minor — "how board section 320's nine findings actually arrived" is stale by growth

`320` holds forty items at HEAD; the adding commits since 2026-08-24 show the
majority arrived by shape 1 (branch and PR), not the channel. The sentence was
true on 2026-08-23 and reads as a description of the section. *Counsel:* date
it, or say "the section's first nine".

### RU9 — minor — atelier's own reports have no named section

§ *The duty* says an atelier session "files a board item under
`docs/roadmap/` exactly as a child's finding would arrive there" and names no
section; `320` is titled *child-filed findings*; atelier's own have landed in
`320` (`340`) and `310` (`130`). *Counsel:* name the home, or retitle `320` to
"filed via § *Pointing up*".

### RU10 — minor — § *The route* step 1 never points at the board's format

"A board item under atelier's `docs/roadmap/`" names the content and not the
form; `docs/roadmap/README.md` holds the grammar, the tri-state and the rebuild
and is cited nowhere in the section. The divergent index behaviour of real
filers (RU3) is the cost. *Counsel:* one pointer.

### RU11 — note — out-of-scope reds met during the re-runs, for their owners

`pathscan` (warn-only) reds `docs/method/session-open/session-open-prompt.md:15`
on a sibling-relative path — pre-existing, not this delta. `blockscan --against
48c181f^` reports a `session-rhythm` co-change violation in `CONCURRENCY.md`
§ *Claiming work* from a later commit — not this delta. `pointerscan`
(warn-only) flags `160/380`'s grammar — not this pass. Recorded, not owned.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR (RU1), 6 MODERATE (RU2–RU7), 3 minor (RU8–RU10),
1 note (RU11).** The duty, the three shapes and the count are correct and
grounded; the no-harm rules are the right four answers to the wrong three
costs — they reached the floor, and the privacy rule that outranks them did
not. Under rule 3 every finding above is the principal's to decide; nothing is
applied here.

## Re-run ledger (all at HEAD `c4b9cd0`, 2026-09-25T07:09Z–07:19Z, in the worktree)

| Command | Result |
|---|---|
| `python3 tools/floor.py --plane hook --root . --tools tools` | exit 0; 11 enforced green, `leakscan` structural + local; advisories: `sizescan` ×2, `pointerscan` ×1, `pathscan` ×1 (RU11) |
| `python3 tools/floor.py --plane ci --root .` | exit 0; `secretscan` 22 advisory (entropy), `leakscan` structural-only as declared; same three advisories |
| `python3 tools/stampscan.py --warn --root . .` | exit 0; 1 block verified, identical (91 lines) |
| `python3 tools/blockscan.py --check --warn --root .` | exit 0; clean |
| `python3 tools/blockscan.py --against HEAD^ --warn --root .` | exit 0; clean |
| `python3 tools/blockscan.py --against 48c181f^ --warn --root .` | 1 violation (`session-rhythm`, out of scope); **nothing for `doctrine-problems`** — RU1 |
| `python3 tools/blockscan.py --against 5bb78f2^ --warn --root .` | `doctrine-problems` reported `[moved]` (bullet and section changed together at landing) |
| `python3 tools/linkscan.py --root . docs/method docs/build CLAUDE.md` | exit 0; clean |
| `python3 tools/pathscan.py --warn --root . docs/method docs/build CLAUDE.md` | exit 0; 1 finding, pre-existing, out of scope (RU11) |
| bullet count: `awk` over `floor:begin`…`floor:end` / `stamp:begin`…`stamp:end`, `grep -c '^- \*\*'` | 9 and 9; region text diff empty |
| `git merge-base --is-ancestor be8a003 48c181f` | no — `blockscan` post-dates the later commit's branch |
| `ls docs/roadmap/320-*/[0-9]*.md \| wc -l` | 40 (RU8) |
| `gh pr list --state all --json number,title,headRefName,state,createdAt` | 21 hand-up PRs 2026-08-26…09-24; 2 pre-ruling carry a private child's name; 4 post-ruling comply (RU1, RU2) |
| `gh pr view 84/86/87 --json files,mergeStateStatus,statusCheckRollup` | 84, 86: floor SUCCESS, DIRTY; 87: floor SUCCESS, CLEAN, no index change (RU3) |
| `gh repo view <three children> --json visibility` | the no-harm instance's child PRIVATE; the other named instance's repo not resolvable under the owner; the public-named reporter PUBLIC (RU7) |
| `gh repo view mike548141/atelier --json hasIssuesEnabled` | true (RU5) |
| `git log origin/main --since=2026-09-20T12:00:00Z` | 13 commits (RU4) |
| `python3 tools/coldsweep.py … 'report-<'` | 10 hits, all doctrine or `320` items; no other live surface prescribes a branch form |
| `python3 tools/coldsweep.py … 'nine findings\|seven today\|eight today'` | `PROPAGATION.md:508` (RU8); `CHANGELOG.md:1780` is a dated history line, left |
| `python3 tools/coldsweep.py … -i 'private vulnerability\|security advisor'` | `SECURITY.md`, its template, `REPO-STANDARD.md` only (RU6) |
| `python3 -m unittest discover -s tools` | **not run** — not on the brief's re-run list, and the machine is shared |

## Follow-up checklist (for the principal's ruling round; nothing applied here)

- [ ] RU1 — rule 2's class-only clause into the floor bullet, both copies; `blockscan` map to
      subsections or its residual stated.
- [ ] RU2 — name the parent's merge-time check; queue the branch/title lint as its own item.
- [ ] RU3 — state the index-conflict resolution in the parent's half; set the filer's expectation.
- [ ] RU4 — open hand-up PRs into the session-start read.
- [ ] RU5 — name the adopter's shape (fork + PR, or an issue); mark estate-only shapes.
- [ ] RU6 — security-class doctrine defects take the private route first.
- [ ] RU7 — `320/330` option (a) for the no-harm instance.
- [ ] RU8–RU10 — the three wording fixes, in one application commit.
- [ ] RU11 — hand the three out-of-scope reds to their owners.
- [ ] Phase 2 — reconcile against the sibling on release; overall line restated there.

# Cold pass — the naming precedence — rule 2 governs every surface a filing creates, and the branch form loses its repo token

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/360-rule-4-cold-pass-queued-the-naming-precedence.md`.
**Why it earns a review:** this is the rule a private child follows when it
names the branch, commit and PR that carry a finding into the public parent; a
wrong precedence either leaks the child's identity or strips the parent of what
it needs to land the filing.

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

- `48c181f` (2026-09-20) — the landing commit

Delta paths:

- `docs/method/PROPAGATION.md` § *The route* rule 2 — the precedence paragraph
- `docs/method/PROPAGATION.md` § *Report without harming the parent* — its first
  two bullets (the branch form; what the commit and PR may say)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether rule 2 and the two bullets now agree with each other and with the rest
of § *Pointing up* (which `160/300`'s delta wrote and this one edits — review
the section at HEAD as one text). Whether the uniform branch form can be obeyed
by the child *and* triaged by the parent: read the merged hand-up branches on
`origin` (`git branch -r`) as data about what children actually named, and say
what the parent could and could not tell from the name alone. Whether "say what
it is" gives a parent enough to land a filing it cannot attribute. **Non-goal:**
the principal's ruling on precedence.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   precedence presumes that a neutral name costs the parent nothing it needed —
   test that against the 2026-09-17 batch of eleven hand-ups, where the parent
   found six number collisions: would neutral names have made that triage harder
   or easier?
2. **Correctness & quality.** Diff `48c181f`. Check the two bullets against rule
   2 word by word; check the branch-form example is itself compliant with the
   rule it illustrates.
3. **Completeness / harvest.** Every other surface naming the branch or commit
   form for a hand-up: `CONTRIBUTING.md` and its template, `skills/`,
   `docs/build/REPO-STANDARD.md`, `SECURITY.md`'s disclosure route.
4. **Security & privacy** — mandatory. This rule is a privacy control on a
   public repo. Test the worst case: a child whose finding cannot be stated
   without naming a private term — do the two bullets at HEAD stop the term
   reaching the branch name, the commit subject, the PR title, and the PR body?
   Discharge the house scanner by grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `git branch -r` and `gh pr list --state merged --limit 30` as data about
  actual hand-up names (public API data about a public repo)
- `linkscan`, `pathscan`, `wrapscan`, `spellscan` over `docs/method` at HEAD;
  the floor on both planes

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
`docs/roadmap/160-doctrine-review-owed/360-rule-4-cold-pass-queued-the-naming-precedence.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`
- the board items `docs/roadmap/320-*/190-*.md`, any
  `…naming-rule-cannot-both-be-obeyed.md` and
  `…naming-precedence-reach-doctrines-own-prose.md` items

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/360-rule-4-cold-pass-queued-the-naming-precedence.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `NP`: `NP1`, `NP2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1, written 2026-09-25 0720 UTC

### Provenance, repeated

- **Spawned by:** the batch orchestrator (`claude-fable-5-1`), with this brief as my only
  framing. I am not the author's session and was not instructed by it. The orchestrator
  holds the `.deferred.md` sibling; I have not seen it. Shape: reviewer-plus-orchestrator,
  both Fable, as the brief discloses.
- **Tier:** Fable (`claude-fable-5-1`), checked at spawn.
- **Worktree:** `/Users/mike/worktrees/atelier-review-batch-0925` at `c4b9cd0`, read-only
  except this file; no git write run there. Probes ran in two scratch clones under my
  scratchpad prefix, one parked at `c4b9cd0`, one at `48c181f`.
- **What I read:** this brief; `docs/method/REVIEW.md` and `00-APEX.md` at HEAD;
  `docs/method/PROPAGATION.md` at HEAD in full; `git show 48c181f -- docs/method/PROPAGATION.md`
  (the delta only — the landing commit also touched barred records and board items, which I
  did not diff); `CHANGELOG.md` lines 36–62; `.githooks/pre-commit`, `tools/floor.py`,
  `.github/workflows/ci.yml`, `.atelier-floor.json`, `tools/blockscan_map.json`;
  `SECURITY.md`, `docs/build/REPO-STANDARD.md`, the `docs/build/templates/` copies of
  `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`; `README.md` and `CONCURRENCY.md` by grep
  only; `git branch -r`; `gh pr list` (merged, closed, open) and `gh pr view` for PRs 67–87
  (head ref, title, files, commit times). Two `coldsweep` runs.
- **Exposure, disclosed.** Four things I met that I would rather not have:
  1. My first `coldsweep` passed `--also-exclude` for the queue pointer only, so single grep
     lines from the barred board items `320/190` and `320/330` printed (option labels, a
     "rule 2 wins, everywhere" fragment, `330`'s title line). I opened neither file; every
     later sweep barred both paths explicitly.
  2. `git log` on `docs/roadmap/320-*/340-*` (run to learn who filed it before deciding
     whether to open it) showed its title — filed by the author session two minutes after
     the landing commit. I did not open it. It appears to concern the same guard blind spot
     my NP6 reproduces independently; reconcile should check that.
  3. `git show 48c181f` printed the landing commit's full message, i.e. the author's
     rationale for the delta. I read it. Where this verdict cites it, it says so.
  4. The floor run's `pointerscan` printed the first line of another pass's pointer
     (`160/380`). A fragment; not this pass's subject.

  `--include-barred` was not used. `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, prior verdicts and my queue pointer were not opened.

### Lens 1 — approach and assumptions

The load-bearing assumptions, named by me, and what each did under test:

- **A1 — a neutral name costs the parent nothing it needs to land a filing.** Tested on the
  2026-09-17 batch (eleven PRs, all merged at `2026-09-17T08:18:05Z`). Four of the eleven
  head refs carried a child's token; one said `private-child`; six were subject-only. The
  item-number collisions I can reconstruct from `gh pr view --json files` are: `320/140`
  (PR 67 vs 68), `320/150` (67 vs 71 vs 75), `320/160` (69 vs 72), `320/240` (79 vs 80) —
  four numbers, five pairs. Every one was resolved by the item's *file path and content*;
  the branch name played no part, with or without a token. So neutral names would have made
  that triage **neither harder nor easier**. Where identity *did* carry information was
  recurrence: PR 68's branch (`report/320-140-second-instance`) told the parent this was a
  re-filing of an existing item, and it did that by citing the **item number**, not the
  child. Distinctness, not identity, is what the parent needs — and the doctrine does not
  say so (NP4). A1 holds for landing; it is under-stated for recurrence.
- **A2 — the parent cannot see a child's visibility, so the branch form must be uniform.**
  Stated in the delta. But bullet 2 keeps the commit/PR wording *conditional* on that same
  visibility, judged by the child ("only if the reporting repo is one whose name may be
  published"). The parent can verify neither. The uniform/conditional split is not argued
  from one principle (NP5).
- **A3 — the failure is one-way.** Verified: PRs 67 and 69's head refs are absent from
  `git branch -r` (the parent deletes on merge — `REPO-STANDARD.md` lines 224–226) and
  `gh pr view` still returns both refs and titles. The paragraph's claim holds.
- **A4 — the uniform form is obeyable by a child.** Verified on the live namespace: all four
  hand-up branches on `origin` at review time (`…-1107`, `…-1110`, `…-1152`, `…-0331`) obey
  `report-<subject>-<HHMM>`, and their PR titles say "from a private child" or "from a
  public child". Obeyable — but `<HHMM>` is under-specified (NP3).
- **A5 — implicit: prose is enough.** No tool in `tools/` reads a branch name or a commit
  message (`grep` for `abbrev-ref|symbolic-ref|commit-msg|COMMIT_EDITMSG` hits only
  `worktree.py` and two test files); the hook plane's `leakscan` reads staged *file content*;
  the CI plane's is structural-only by design; `.githooks/` holds `pre-commit` only. The
  precedence is rung 1 on every one of the four surfaces it names (NP2).

**What the parent can and cannot tell from the name alone** (the brief's question, answered
from the data above): *can* tell it is a hand-up (`report-` prefix) and roughly what about;
*cannot* tell which child, whether the child is public or private, which item it lands on
(one branch in twenty carried the number), or whether it is a re-filing. Landing needs none
of those; the file path in the diff supplies the item. Recurrence counting needs the last.

### Lens 2 — correctness and quality

Diffed `48c181f` on the doctrine path. Word-by-word against rule 2:

- The rule-2 paragraph names four surfaces (branch, PR title, commit subject, PR body);
  bullet 1 covers the branch and bullet 2 the other three — the sets agree.
- "which this section's own reporting rules used to prescribe" — true: the removed lines
  prescribed `report-<reporting-repo>-<subject>`.
- Both bullets and the paragraph cite the same ruling and date; `CHANGELOG.md` lines 45–48
  match the delta.
- The bullet's example `report-<subject>-<HHMM>` is a placeholder and complies with the rule
  it illustrates; the old form is quoted as a placeholder too. Compliant.
- The floor block (`PROPAGATION.md` line 181) and its stamped template copy (`stampscan`:
  identical, 91 lines) still say "name the branch for the report, say it is a hand-up in
  the first line" — not contradicted by the delta, but not carrying it either (NP6).

Defects: the bullets' operative instruction is "no **repo token**", which is a proper subset
of rule 2's list — *the repo, its hosts, its clients or its secrets* (NP1). "A private child
says *'a private child'* and nothing more" reads literally as the whole PR body; the intended
sense (nothing more *about identity*) is recoverable from context (note, folded into NP1).

### Lens 3 — completeness and harvest

Every surface the brief names, checked:

| Surface | Names a hand-up branch/commit form? | State |
|---|---|---|
| root `CONTRIBUTING.md` | file does not exist | — |
| `docs/build/templates/CONTRIBUTING.md` | no | nothing to harvest |
| `SECURITY.md` and its template | no; disclosure via GitHub advisories | separate channel, consistent |
| `docs/build/REPO-STANDARD.md` | no; sets delete-branch-on-merge (224–226) | consistent with "never re-create" |
| `skills/*` | no hits for hand-up, branch, pointing up | nothing to harvest |
| floor block + stamped copy | "name the branch for the report…" | silent on the precedence (NP6) |
| `CHANGELOG.md` | entry present, accurate | ✓ |

Guard check: `blockscan` did not exist at `48c181f`. I laid HEAD's `blockscan.py` and map
over a clone parked there and ran `--against HEAD^`: **clean**. The map keys the
"doctrine-problems" bullet to the `## Pointing up` heading; the delta edited `###`
subsections beneath it, and the guard reported nothing moved. So the one mechanical check
that asks "did the floor bullet move with its section" is blind to exactly this delta (NP6).

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which
in this shared worktree is other passes' unstaged drafts; this is a landed-delta review of
Markdown, a file class its exclusions bar anyway.

*Design altitude — the worst case the brief sets.* A child whose finding cannot be stated
without a private term. The rule-2 paragraph's general clause ("every surface the filing
creates") reaches the branch, commit, PR title and body in principle, and rule 2's own
escape — file in the private estate root, point at it from a neutral parent item — is the
right answer. But the bullets a filing session actually follows stop only a **repo token**;
the subject slug, the item filename, the commit body and the PR body are free text; and no
mechanism on either plane reads any of the four named surfaces. So the term is stopped by
the session's reading of a general clause, and by nothing else (NP1, NP2). Rule 2's list
also names *hosts, clients and secrets* — a secret in a branch name is a credential
exposure with no rotation path for the ref. That case is unaddressed by the bullets'
wording.

*Code altitude.* The delta has no code surface; OWASP catalogue not applicable — stated,
not skipped.

*Lifecycle.* `REVIEW.md` says a confirmed security finding carries a severity and a
recurrence-prevention step. `320/190` is a privacy finding; the delta's prevention step is
the wording. See NP2.

### Findings

**NP1 — MODERATE.** The operative instruction is narrower than the rule it applies. Rule 2
forbids *the repo, its hosts, its clients or its secrets*; both bullets say "no repo token".
A session obeying the bullets literally may put a host or client name in the subject slug,
the item filename, or the PR body and be compliant with the letter. On a public forge that
is the one-way failure the paragraph itself describes.
*Counsel:* make the bullets' noun match rule 2's list — "no repo token, host, client or
secret on any of them" — and name the subject slug and item filename as surfaces.

**NP2 — MODERATE.** The precedence is prose-only on all four surfaces, and the delta neither
says so nor climbs. No hook or scanner reads a branch name, commit subject or PR title
(probe above). The failure has occurred at least three times in head refs (PRs 67, 69, 79;
the author's commit message counts two as a private child's — its claim, not verified by
me). § *When a rule keeps breaking* says a second noticed occurrence triggers the ladder and
that "none [of the rungs] changes the wording"; the delta's response is a wording change.
`REVIEW.md`'s security-finding lifecycle asks for a recurrence-prevention step.
*Counsel:* a rung-2 candidate exists on the machine that holds the term list: a pre-push
check that runs `leakscan`'s term list over the refs being pushed and their commit
messages, in the same hook family as `pre-commit`. Failing that, state in the section that
the four surfaces are unwatched, as § *The instance* already does for enumeration.

**NP3 — minor.** `<HHMM>` is new in this delta and has no stated frame or referent — UTC or
local, session start or filing time. The house's other four-digit branch suffixes are
`MMDD` (`worktree-…-0823`, `-0824`), and PR 69's `-0907` is a date; of the four live
branches, three are consistent with UTC time and one (`-1152`) cannot be reconciled with
its commit times either way. And with the repo token gone, a minute is the form's only
discriminator against "never re-use or re-create a branch name".
*Counsel:* say "`HHMM` in UTC, `date -u`, at filing", as `CONCURRENCY.md` line 217 does for
records; consider `<YYYY-MM-DD-HHMM>` for the same coordination-free reason.

**NP4 — minor.** Recurrence needs distinctness, not identity, and the doctrine does not say
how a neutral filing supplies it. PR 68 did it by citing the item number in the branch;
that is the pattern, and it costs no identity.
*Counsel:* in bullet 2 — "a re-filing names the item it is a further instance of".

**NP5 — minor.** The rationale is asymmetric: the branch form is uniform *because* the
parent cannot see visibility, while the commit and PR wording stays conditional on a
visibility the child self-declares and the parent cannot check. Either the visibility
judgement is safe to leave with the child (then the branch could be conditional too), or it
is not (then the wording should be uniform). Mike's call; recorded as a dilemma, not
resolved.

**NP6 — MODERATE.** The safety floor — the text that "binds even if atelier is never read"
and the hottest read path in the fleet — carries neither rule 2's class-not-specifics nor
the precedence; its pointing-up bullet says only "name the branch for the report, say it is
a hand-up in the first line". The stamped copy is identical. And the co-change guard that
would have asked whether the bullet should move did not fire on this delta (reproduced with
HEAD's `blockscan` at `48c181f`: clean), because the map keys the `##` heading and the delta
edited `###` subsections. A private child session that reads only its block has no floor
line against naming itself on a branch. A board item filed by the author two minutes after
the landing appears, by its title, to name the guard half of this; I did not open it.
*Counsel:* one clause in the floor's pointing-up bullet — "carry the class, never this repo's
name, on the item, the branch, the commit and the PR" — and a map entry per `###` under
§ *Pointing up*, or a guard that walks subsections.

**NP7 — note.** The brief's "six number collisions" did not reproduce from PR file lists (I
count four numbers across five pairs). The brief's framing is attackable and this is a
small instance; it changes no conclusion.

**NP8 — note.** The section that now forbids a repo token on any surface names two children
in its own prose within sixty lines. Whether the precedence reaches doctrine's prose is
already a board question (I saw its title) and the principal's; recorded, not judged.

**NP9 — note.** Two warn-only findings in the floor run are not this work's: `pathscan` on
`docs/method/session-open/session-open-prompt.md:15` (last touched by `c38b7da`, an earlier
commit than the delta) and `pointerscan` grammar on `160/380` (another pass's pointer).

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (NP1, NP2, NP6) · 3 minor (NP3, NP4, NP5) ·
3 notes (NP7, NP8, NP9).** The delta says what the ruling said, consistently across the
paragraph, both bullets and the changelog, and the live namespace shows children obeying it.
What it does not do is carry the control to the surfaces where it fails one-way: the floor
block, the bullets' own noun, and any mechanism.

### Re-run ledger

All commands run 2026-09-25 between 0709 and 0720 UTC. Exit codes read directly, never off a
pipe.

| Command | Where | Result |
|---|---|---|
| `git show 48c181f -- docs/method/PROPAGATION.md` | worktree | the two hunks reviewed above |
| `git branch -r` | worktree | `main` + 4 `report-<subject>-<HHMM>` branches, no repo token |
| `gh pr list --state merged --limit 30` | API | 30 rows; 11 merged `2026-09-17T08:18:05Z` |
| `gh pr view N --json headRefName,title,files,commits` for 67–75, 79, 80 | API | collision reconstruction in lens 1 |
| `gh pr list --state closed` / `--state open` | API | 1 closed-unmerged (83, neutral title), 3 open (84, 86, 87, neutral refs) |
| `git log -1 origin/report-*` (×4) | worktree | commit times vs `HHMM` — NP3 |
| `python3 tools/{linkscan,pathscan,wrapscan,spellscan}.py --selftest` | worktree | all `selftest OK`, exit 0 |
| `python3 tools/linkscan.py --root . docs/method` | worktree | clean, exit 0 |
| `python3 tools/pathscan.py --warn --root . docs/method` | worktree | 1 warn (NP9, pre-existing), exit 0 |
| `python3 tools/wrapscan.py --root . docs/method` | worktree | clean, exit 0 |
| `python3 tools/spellscan.py --root . docs/method` | worktree | clean, exit 0 |
| `floor.py --plane hook --root . --tools tools` | clone @ `c4b9cd0` | exit 0; 11 ✅, 3 👁️ (1 pointerscan, 1 pathscan warn) |
| `floor.py --plane ci --root .` | clone @ `c4b9cd0` | exit 0; secretscan 22 advisory, leakscan 🟡 structural — both by design |
| `stampscan.py --warn --root . .` | clone @ `c4b9cd0` | clean; template copy identical to the floor region |
| `blockscan.py --against HEAD^ --warn --root .` (HEAD's tool laid over) | clone @ `48c181f` | clean — guard blind to this delta (NP6) |
| `python3 tools/blockscan.py --check --warn --root .` | clone @ `48c181f` | clean |
| `coldsweep` ×2 (patterns for the branch form, rule 2, hand-up) | worktree | 117 and 25 hits; second run barred `190`, `330`, the pointer |
| full Python suite | — | **not run**: the delta has no code surface; the four named scanners' selftests and the floor on both planes are the relevant mechanical leg |

Floor invocations were lifted from `tools/floor.py`'s registry (`--root {root} {scope}`
shapes, `--warn` for pathscan) and `.github/workflows/ci.yml` (`--plane ci --root .`;
stampscan and blockscan bespoke steps); `.githooks/pre-commit` calls `--plane hook`.

### Follow-up checklist

- [ ] NP1 — principal's ruling: widen the bullets' noun to rule 2's list; name slug and
      filename as surfaces.
- [ ] NP2 — principal's ruling: a pre-push term check on the hook plane, or an honest
      "unwatched" line in the section.
- [ ] NP3 — principal's ruling: state `HHMM`'s frame and referent; consider a date component.
- [ ] NP4 — principal's ruling: re-filings cite the prior item.
- [ ] NP5 — principal's ruling: uniform or conditional, from one reason.
- [ ] NP6 — principal's ruling: floor bullet clause; blockscan subsection coverage (check the
      existing board item at reconcile).
- [ ] NP7 — orchestrator: note the collision count in the record.
- [ ] NP8 — already on the board; no new item.
- [ ] NP9 — no action from this pass.
- [ ] Phase 2: reconcile against the sibling and the intent record; verify any `[fixed]`
      claims found there.

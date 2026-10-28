# Cold pass — the index projects each item's logical first paragraph, with a dated grace

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes the pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well.
**Status:** PASS RAN 2026-10-28 — PASS-WITH-FINDINGS, 0 MAJOR · 2 MODERATE · 5 minor ·
4 notes (PP1–PP11); `board` is doctrine by function, so every finding is the principal's
(rule 3). Run on Fable 5.1 through the Claude Platform API by an orchestrating session
(`f7b25adb`) that started and instructed neither the delta's authors nor the brief-writer; both
phases below, the held-back sibling folded in verbatim at the end. Brief written 2026-10-26 UTC
by an Opus 5.5 brief-writer subagent of session 5070f22b.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/970-rule-4-cold-pass-queued-paragraph-projection-and-grace.md`.
**Why it earns a review:** `board --check` blocks in every adopting child's CI and has no
advisory form. This change alters what every child's committed index must contain, and adds a
dated acceptance of the old form that switches itself off on a calendar date with no commit in
the child. The worst failures are a check that reds children who changed nothing, a grace that
accepts an index it should not (a silent pass on a gate whose green is read as "current"), or
an end date that behaves differently from what the notice to children says.

## Spawn provenance

- **Author of the delta:** a Mike-opened Opus 5.5 queue run, session `8e498ef1`, 2026-10-18,
  worktree `atelier-qr-010-170` by the pointer's account, and the Opus worker it dispatched,
  which the pointer says wrote the code. Neither is opened here beyond the pointer.
- **Who wrote this brief:** an Opus 5.5 subagent (`claude-opus-5-5`) dispatched on 2026-10-26
  by session `5070f22b`, a headless Opus 5.5 brief-writing session started on the principal's
  instruction of that day to have every queued brief ready for a reviewer. Session `5070f22b`
  authored none of this delta, and neither did this subagent. It is **off-tier for review,
  disclosed: it forms no finding and writes no severity**, and stops after this brief and its
  sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier orchestrator conditions
  apply and are disclosed in the claim, the pointer and the verdict. The reviewer repeats its
  own provenance in its verdict.
- **Barred from taking the pass:** session `8e498ef1` and every worker it dispatched; session
  `5070f22b` and every subagent it dispatched, this brief-writer included.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing). It read:
  - its dispatch prompt and the dispatcher's common instruction file for this batch;
  - `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` lines 20–230 and 320–450;
  - for shape, the brief `docs/reviews/2026-10-18-0511-template-history-privacy-cold.md` and
    its sibling, both whole (another pass, other surfaces), and the brief section of
    `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md` above its first divider,
    whose header line states that pass's verdict and finding counts (another pass, on
    `coldsweep`); no verdict text below any divider was opened;
  - the queue pointer whole, claim line included;
  - **the intent record whole** (`010/170`), including the author's closing account below
    the principal's words; that account is held in the sibling;
  - board items `010/180` and `010/190` whole, the hand-up `320/730` whole, the first three
    lines of `320/450`, and, through a listing command, the first two lines of `180/170`;
  - the delta through `python3 tools/coldsweep.py --root . --commit 28ef94a`: subject, stat
    and the diffs of `CHANGELOG.md`, `tools/board.py` and `tools/test_board.py`; the
    `docs/ROADMAP.md` hunks were not read line by line. **No commit message body was read**;
  - `tools/board.py` lines 729–830 at HEAD and its `--help`; commit subjects, dates and stats
    from `git log` / `git show --stat --format` for the commits named below.

  It did **not** open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or any
  prior verdict on these surfaces. Its harness also loaded user-level and repo instruction files
  and a memory index, which hold private context this brief does not carry. Everything
  evaluative it formed is in the sibling, which holds one intent-record pointer, three
  locations of the author's account and one of other held-back framing, ten hypotheses and
  twelve re-run results.

## The acceptance test: the principal's own words

The intent record quotes the recommendation the principal answered and his answer. Read **only**
those lines, before phase 1:

```
sed -n '11,14p' docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md
```

Stop at the end of his quoted answer on line 14; the rest of line 14 onward, and lines 1–10, are
the author's account and are barred until phase 2. The same words are quoted again in a comment
in `tools/board.py` (the LEGACY block); that comment is the delta and readable, and where the
two differ the intent record governs. Judge the work against those words: the projection
change, a grace in which the check accepts both forms, its end, and telling the children.

## What the work is

- `28ef94a` (2026-10-18 09:00 UTC, on `main`) — board: project each item's logical first
  paragraph, with a grace for children. **Delta paths:** `tools/board.py`, `tools/test_board.py`,
  `CHANGELOG.md` (the `010/170` entry only) and the rebuilt `docs/ROADMAP.md`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit 28ef94a` (add `--path <p>` per
file to narrow). Plain `git show` is barred: it prints the message body before the diff, and
reading is atomic (rule 1). Review the paths at HEAD as well as in the diff. Confirm with
`git log --oneline 28ef94a..HEAD -- tools/board.py tools/test_board.py CHANGELOG.md` which later
commits touched the delta paths; a later commit on `CHANGELOG.md` that is not about `010/170` is
not this delta.

Adjacent commits, **not the delta**: `63720eb` (09:01 UTC) closed the intent record, filed
`010/180` and queued the pointer. Read its subject and stat only, with
`git show --stat --format='%h %cI %s' 63720eb`; its body and its hunks on the intent record,
`010/180` and the pointer are barred until phase 2.

**The grace's removal is out of scope but in view.** It is open board work at
`docs/roadmap/010-board-store-migration-per-item-files-mik/190-remove-the-two-adoption-graces-after-their-date.md`
(filed at `0dad7ca`, 2026-10-18 09:33 UTC). You may read it in phase 1: it names what is to be
removed, and whether that list matches the code's own removal instruction in the LEGACY block
is in scope. Doing the removal, and the second grace it names in another tool (`020/150`,
queued separately at `160/980`), are not. **If `010/190` has landed by the day you run**, the
grace is gone from HEAD: review it at `28ef94a` from an extracted copy
(`git archive 28ef94a tools | tar -x -C <scratch>/at-28ef94a`), and record what HEAD now does.

**Related later evidence: the hand-up `320/730`**,
`docs/roadmap/320-child-filed-findings-via-pointing-up/730-hand-up-the-paragraph-projection-joins-a-claim-into-an-index-line-wrapscan-refuses.md`,
landed as PR #122 at `b0a17f6` (2026-10-18 12:40 UTC), after the delta, handed up by a
child's session that is not the delta's author. **It is not a prior verdict and not part of
the delta.** Its *report* of how the delta behaves in a child is **in scope as evidence of
real-world behaviour**: read lines 1–24 in phase 1, as claims to re-drive, never as findings to
adopt. Lines 25–32 carry its
author's remediation options and review note; that framing is barred until phase 2. Choosing a
remedy for it is atelier's open work under that item and **out of scope** here; whether the
delta or its notice to children should have met the case is in scope.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Probe, at least:

- **The projection.** What `item_state` now takes as the logical first paragraph, against the
  item files that exist: on this board and, read-only, on the adopting child repos on the
  machine. Every way a paragraph can end or fail to end (blank lines, unindented lines, the
  block-start pattern, tabs, CRLF, comments, fences, a state line with an empty head), and what
  each field (title, claim, flags, allow-markers) reads.
- **The grace, on both sides of its boundary.** The CLI has no date flag; `run_check` takes an
  injectable `today=` and the module reads the date through `_today_utc()`. Drive
  `board.run_check(root, fix=False, today=date(...))` from Python (or patch `_today_utc`) on the
  day before `LEGACY_INDEX_ACCEPTED_UNTIL`, on that day and after, on both planes (worktree and
  `source=board.INDEX`), for an old-form index, a new-form index, an index matching neither, and
  an index that matches the old form but where the board also has problems. **Then re-check the
  grace's behaviour on the date you actually run**, with no date injected, and state that date
  in UTC: if you run on or after 2026-11-18 the grace should already refuse the old form, and
  whether it does is a live result, not an inference.
- **The legacy renderer.** It claims to reproduce the pre-delta rendering byte for byte. Extract
  the pre-delta tools (`git archive 28ef94a^ tools | tar -x -C <scratch>/pre`) and compare its
  index against `_index_entry_v1`'s over copies of real boards.
- **The children.** Read-only, over the adopting child repos on the machine, **by count only**:
  how many have a split board, how many pass today, pass only under the grace, or fail, and how
  each count moves on the grace's end date. Establish which `board.py` each child plane runs (CI
  from `floor.yml@main`, the commit hook from the child's pinned copy) and what that means at
  the boundary. Never name a child, quote its content or write to it.
- **The notice.** The `CHANGELOG.md` entry as what reaches the children, against the acceptance
  words and the code's actual behaviour (dates, planes, the remedy command it names).
- **The tests.** Do they fail if the grace or the projection breaks? Mutate the code in a
  scratch copy (an off-by-one on the date, the grace applied under `--rebuild`, the paragraph
  stop removed) and re-run; a suite that stays green on a broken behaviour is a finding.

**Non-goals:** the board store's per-item design (`010`), and the second grace landed the same
day in another tool. The decision to have a grace at all is the principal's and is not under
review; how it was built, sized and announced is.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first, then attack
   the ones below and any you add.
2. **Correctness & quality.** Diff the commit; run the probes above live; record any overclaim
   against the text that makes it (docstrings, comments, the CHANGELOG entry, check output).
3. **Completeness / harvest.** Every surface that states how the index is projected or how
   children adopt a board change (board README, the board item template, the reviews and
   queue-run skills, any child-facing doc). Is a man page, stamp or doc change owed?
4. **Security & privacy** — mandatory. The tool reads item files and shells out to git through
   `harvestscan`; check path and argument handling against the OWASP catalogue (A03 Injection)
   by hand, and that every test fixture is synthetic. Aim `/security-review` at the code diff
   only from a clean tree (see *House rules*), or discharge it in one line with grounds.

## Load-bearing assumptions to attack

Each is a falsifiable claim; damage it with a probe or confirm it by re-driving.

1. A child that changed nothing still passes `board --check` until the grace ends, on both
   planes.
2. On and after the end date the old form reds exactly as any stale index does, and before it
   the grace never accepts an index that is stale for any other reason.
3. The legacy renderer is byte-identical to the pre-delta projection on every real board.
4. The logical-first-paragraph rule matches what a Markdown renderer shows as the item's first
   paragraph, for the item shapes that exist on this board and on the children.
5. Flags read only from the state line, and allow-markers only from the lines the title and
   claim came from, lose nothing an index line needs and carry nothing it should not.
6. The new projection produces index lines every adopting child's own enforced guards accept.
7. The CHANGELOG entry tells a child everything it needs to act before the end date.
8. The end date, as the code computes it, is the date the notice states.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. Each line below was run once by the
brief-writer from its worktree root, in the foreground; its results are held in the sibling,
not offered here. Read exit codes explicitly; check `uptime` before the heavy ones.

- `python3 tools/coldsweep.py --root . --commit 28ef94a`
- `python3 -m unittest discover -s tools -p test_board.py -v` and
  `python3 tools/board.py --selftest`
- `python3 tools/board.py --check --root .` and `python3 tools/board.py --check --staged --root .`
- `python3 tools/wrapscan.py --root . tools/board.py tools/test_board.py`
- `git log --oneline 28ef94a..HEAD -- tools/board.py tools/test_board.py CHANGELOG.md`
- the legacy byte-identity comparison and the boundary probe described under *Scope*, from a
  script in your scratchpad that imports the worktree's `tools/board.py` by path
- the count-only child probe described under *Scope*, read-only, check mode only
- `nice -n 10 python3 -m unittest discover -s tools` (the full suite, once)
- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane ci --root .`

## House rules for this run

- Name the worktree you review from in the verdict; it is read-only to you except for THIS
  file. Other sessions may be live on this machine: touch nothing outside your worktree and your
  scratchpad. Never open another `docs/reviews/2026-10-26-*` file; each is another pass's
  framing.
- No git command that writes in the worktree, beyond committing this one file at the end of
  each phase (or handing it to your orchestrator to commit). Read-only git is fine. Extracted
  trees, board copies, mutated copies and probe scripts go under your session scratchpad, named
  by your prefix, and are deleted when you finish; never mutate the worktree's `tools/`.
- Child repos: read-only, check mode only (never `--rebuild` against a child), no scanner other
  than `board` pointed at them, and results by count. Never write a child's name, path or
  content into this file, a commit message, the pointer or a session log: this repo is PUBLIC.
- One heavy process at a time, under `nice`; the full suite at most once, in the foreground.
  Never run an installed tool by bare name from `PATH`.
- `/security-review` reads the session's pending diff, not this delta: reproduce the diff in a
  scratch clone, or discharge it by grounds — never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or
  a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer, this brief's sibling
`docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.deferred.md`, the message bodies
of `28ef94a` and `63720eb`, lines 25–32 of the `320/730` hand-up, and these board items (the
intent record beyond lines 11–14, the author's follow-up item, and the upstream hand-up the
work was split from):

- `docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md`
- `docs/roadmap/010-board-store-migration-per-item-files-mik/180-the-paragraph-projection-loses-two-small-signals.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/450-a-wrapped-claim-does-not-project-and-two-more-from-a-child-s-cold-passes.md`

Code comments and docstrings in `tools/board.py` carry the author's reasons; they are the
delta, and reading the delta is never barred.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/970-rule-4-cold-pass-queued-paragraph-projection-and-grace.md
--also-exclude docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.deferred.md
--also-exclude
docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md
--also-exclude
docs/roadmap/010-board-store-migration-per-item-files-mik/180-the-paragraph-projection-loses-two-small-signals.md
--also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/450-a-wrapped-claim-does-not-project-and-two-more-from-a-child-s-cold-passes.md
<pattern>`; `--include-barred` only with disclosure in the verdict. The generated
`docs/ROADMAP.md` projects each barred item's title and claim; a sweep that hits it shows the
same one line the index shows everyone, and is not a breach.

## Process

**Phase 1.** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions, the probes and the re-run list. Append your verdict below a `---` divider in THIS
file: provenance repeated (how you were spawned, your tier, what you read, the UTC date you
ran), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds,
the grace's boundary results on each plane and on your run date, the child counts, findings
with stable IDs (prefix `PP`: `PP1`, `PP2`, …) and severities (MAJOR / MODERATE / minor /
note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger (commands
and results) and a follow-up checklist. Then STOP and commit this file unrevised before opening
the sibling. Edit no other file.

**Phase 2.** Open the sibling, the rest of the intent record, `010/180`, `320/450`, lines 25–32
of `320/730`, and the two barred commit bodies. Append `### Reconcile` beneath your verdict:
per-finding notes against the sibling's hypotheses, the author's account and the hand-up's
options, any finding formed at reconcile marked as such, and the overall line restated. Never
revise phase-1 text. Then fold the sibling in below the reconcile and delete it.

`board` is a CI gate that every child inherits, so it is doctrine by function (rule 3): record
all findings and apply nothing; the principal decides. Counsel per finding is welcome, labelled
as counsel and kept beneath it.

---

*Act 1 run by `claude-fable-5-1` at effort xhigh through the Claude Platform
API (an API harness, read-only sandboxed tools), 58 turn(s), metered US$8.47;
orchestrated by session f7b25adb, 2026-10-28.*

## Verdict — act 1 (phase 1), run 2026-10-28 UTC

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`, effort xhigh), called through the Claude Platform
  API by a harness on the principal's monthly API credit (his approval of 2026-10-28). Tier
  checked at selection: Fable, the principal-named review tier (ruling 2026-08-04).
- **Orchestrator:** session `f7b25adb` (Opus 5.5), off-tier and disclosed: it claimed the pass,
  made the worktree and holds the context partition; it formed no finding and wrote no severity.
  The brief's `.deferred.md` sibling was withheld from this act by removal; the harness refuses
  any path naming it, and I did not look for it elsewhere.
- **Independence:** I was neither started nor instructed by session `8e498ef1` (the delta's
  author) or any worker it dispatched, nor by session `5070f22b` (the brief-writer) or any of
  its subagents. The brief's barred list does not reach me.
- **Worktree:** a pass worktree, HEAD
  `0a2b7a7`, read-only to me; `010/190` has **not** landed, so `tools/board.py` at HEAD is
  byte-identical to `28ef94a`'s (checked with `diff`).
- **Run date:** 2026-10-28, 09:54–10:23 UTC. The grace end `2026-11-18` is 21 days away.

### Limits of this pass (sandbox)

- No network, no writes outside `/private/tmp`, no `tar`, `nice`, `uptime` or `date` binaries,
  and `git archive` is refused. I extracted the pre-delta and delta `tools/` trees with
  `git ls-tree` + `git show` from Python instead; the UTC date came from Python.
- The sandbox's global git config signs commits with a key it cannot reach, so the suite's
  git-backed `StagedPlane` fixture errors (exit 128) unless `commit.gpgsign=false` is injected
  through `GIT_CONFIG_*`. Every test and probe below that needed a commit ran with that
  override, disclosed per line in the ledger.
- The **full suite** (`python3 -m unittest discover -s tools`) was killed at the sandbox's
  300 s cap and did not complete; `test_board.py` ran to completion (59/59).
- The CI-plane floor ran; every check passed except `leakscan`, which crashed on a
  machine-local terms file outside the sandbox's readable roots — an environment limit, not
  a repo defect. `board` itself reported the index current.
- `/security-review` is a Claude Code harness command and does not exist here; lens 4 is
  discharged by hand with grounds (below).
- Child repos: 11 split boards were found under the primary-checkout root the harness exposed;
  worktrees or checkouts elsewhere on the machine were not reachable. Everything on children
  is by count, read-only, check mode only.
- My scratchpad (`/private/tmp/fable-api-scratch/pp-160-970`) was deleted at the end of the
  act; four entries another live session left in the scratch root were not touched.

### Disclosure — what I read before writing

The brief; `docs/method/REVIEW.md` whole; intent record `010/170` **lines 11–14 only**;
`010/190` whole; `320/730` lines 1–24; `010/070` and `010/130` state lines (the first 12–14
lines, both unbarred); the delta through `coldsweep` per path; `tools/board.py` whole at HEAD;
`tools/test_board.py`, `tools/floor.py`, `tools/wrapscan.py`, `tools/harvestscan.py`,
`.githooks/pre-commit`, `.github/workflows/floor.yml`, `tools/README.md` (board section and
grace grep), `docs/roadmap/README.md`, `.wrapscanignore`, `.atelier-floor.json` — in part.
No session log, no `ROADMAP-DONE.md`, no prior verdict, no `docs/reviews/2026-10-26-*` file.
Incidental exposure, named: a `git log` range I ran to place the primary checkout printed the
**subjects** of other 2026-10-26 pass commits (their verdict counts; no topic, no file opened);
the harness's directory listing showed repo names and one floor traceback printed a
machine-local path — neither is written here.

### The acceptance test — the principal's words, and what was built

Lines 11–14: the queue run recommended *"build it with a one-release grace period, where the
check accepts both the old and the new index, and tell the children"*; Mike, 2026-10-18:
*"I agree"*. The LEGACY block quotes the same words, verbatim. Four things are owed: the
projection change, a check that accepts both forms, an end to that, and telling the children.
All four exist. "One release" was realised as a calendar date (31 days of acceptance), chosen
by the queue-run orchestrator and said so in the code comment — honest, but a realisation the
principal did not rule on, in a repo whose CHANGELOG says nothing is tagged (PP8).

### Lens 1 — approach and assumptions

**Load-bearing assumptions, named first by me**, then attacked:

- *A. The state is the item's first paragraph.* True for this board's grammar (title and claim
  share the state line). On the children, 49 `[~]` items exist; the paragraph read rescued
  exactly **1** claim, **14** claims sit as a sub-bullet (`- (claimed …)`) further down and
  project under neither rule, and 34 `[~]` items carry no `(claimed …)` at all. A renderer
  would not show those 14 in the first paragraph either, so the rule is consistent; the
  notice's "a claim wrapped onto line two now shows" is true and narrower than a reader of
  the children might expect.
- *B. The old form can be re-rendered from the current items.* The grace compares `have`
  against a fresh v1 render, not against a stored index. Holds: byte-identical to the
  pre-delta tool on **12 of 12** real boards (this one plus 11 children), problems lists equal.
  Consequence: during the grace a child on the old form may change line-two content — a title
  tail, even a new claim — and stay green, because the old form never carried line two. That
  is what "accept the old form" means; no regression, stated as the grace's bound.
- *C. Both child planes run the current tool.* On this machine, yes: all 11 hooks resolve
  `hooks.atelierTools` to the shared primary checkout's `tools/` (its `board.py` is
  byte-identical to HEAD's), and all 11 CI workflows call `floor.yml@main` with `atelier-ref`
  at its default `main`. The brief's "the commit hook from the child's pinned copy" is not the
  geometry here: no child vendors or pins a copy, so at the boundary both planes flip together,
  and also together the day `010/190` lands if that is earlier than 2026-11-18.
- *D. Index-line width is someone else's problem.* The code's own comment (lines 309–318)
  reasons about wrapscan's single-token exemption; `tools/README.md` lines 108–112 record the
  residual that the index cannot pass a repo-wide wrapscan and tells children to scope it off;
  and `010/130` (open since 2026-08-17) names the claim-fragment case exactly. The delta joins
  an unbounded claim ahead of the link anyway (PP1).
- *E. A calendar date is a safe switch.* It is what was agreed; what it does is turn a ⚠️ into
  a red with no commit in the child. Two children are on that path today (counts below).

**The brief's eight**, each probed:

1. *Unchanged child passes until the grace ends, both planes.* **Confirmed** on the 2 children
   still on the old form (worktree and staged, no date injected), and on a synthetic board on
   2026-11-17. Qualified: any state-line edit before then forces the migration, because
   `rebuild` writes only the new form — expected, but "any time before that date" overstates
   the child's freedom.
2. *From the date the old form reds like any stale index; before it the grace never accepts an
   otherwise-stale index.* **Confirmed**: on 2026-11-18 and after, `1/STALE` on both planes;
   an index matching neither form is `1/STALE` on every date; old form plus a board problem
   returns 1 with the problem printed (PP8 notes the ⚠️ "accepted" line printed beside it).
3. *Legacy renderer byte-identical.* **Confirmed**, 12/12 boards. Not pinned by any test (PP3).
4. *Paragraph rule matches a renderer's first paragraph.* **Mostly.** Stops on blank line and
   on list, quote, comment, fence, heading and table starts match CommonMark's interrupt rules
   closely (`2.`, `#x` and a lone `|` are stricter than CommonMark; no live harm found). It
   diverges on lazy (unindented) continuation, which a renderer continues and the tool stops —
   9 child items, each then projected exactly as before. Stated in the docstring ("INDENTED").
5. *Flags from head, markers from title/claim lines, lose nothing and carry nothing extra.*
   Flags: identical to the pre-delta read (head = line one). Markers: by count, children
   dropped 1 line-one marker (PP6) and the carry does not follow the plain-title fallback's
   reach (PP2); otherwise 2 gained, 2 changed, 0 harmful.
6. *New lines pass every child's enforced guards.* **One exception**, live: one child's claimed
   item renders 166 → 482 columns and fails that child's repo-wide wrapscan (the hand-up's
   case, re-driven by estimate from `board`'s output using wrapscan's exact rules; no scanner
   but `board` was pointed at a child). Old form: 0 such lines across the children; new form: 1.
7. *CHANGELOG tells a child everything it needs.* **Partly** — dates, planes and the notice are
   right; it omits the width consequence and the README's standing advice (PP1), the
   plain-title re-rendering (PP2), `--from-index` at a dirty checkout and UTC (PP5, PP8).
8. *End date as computed equals the notice's date.* **True on 2026-10-28** by inspection
   (`date(2026, 11, 18)`, "first day it is refused"; CHANGELOG "from 2026-11-18 … stale";
   notice text the same). Nothing mechanical ties them: a moved constant stays green (PP3).

### Lens 2 — correctness and quality

- The projection, driven over 2,305 real items: titles that wrapped now render whole (278 of
  this board's 300 changed lines; 492 of the children's 724), no claim is lost that the old form
  carried, and the index at HEAD is current on both planes.
- Synthetic matrix (CRLF, tab indent, empty head, each block-start kind, lazy continuation,
  stray backtick, backticked claim, flag in prose, three-line title, leading comment): every
  case behaved as the docstrings state, with the three gaps recorded as PP2, PP6 and lens 1(4).
- Overclaims against their own text: `projected_markers` — "the state line always" (PP6);
  `index_line` — the plain-text fallback "over the whole paragraph" is stated, its consequence
  for plain-title items is not (PP2); LEGACY comment — "30 days" is 31 (PP8).
- `--rebuild` under the grace writes the new form on both planes (probed); the hook's remedy
  adds `--from-index`; the CLI has no date flag and reads UTC.

### Lens 3 — completeness and harvest

- `010/130` (open, same section, 2026-08-17) describes the claim-on-index-line width collision
  the delta re-raises; the delta neither cites nor closes it, and `320/730` is a second report
  of the same class (PP1).
- `010/190`'s removal list matches the LEGACY block's instruction, and both are incomplete
  (PP4).
- `tools/README.md`'s board section says nothing of the projection rule or the grace, while
  the sibling grace landed the same day with a README paragraph (PP7, V3).
- No skill or template states the first-line rule, so no mirror contradicts the delta.
  `docs/roadmap/README.md` says "checkbox line first, detail beneath" — still true.

### Lens 4 — security and privacy

Discharged by hand: the delta adds no subprocess, no new file read and no new argument path;
`harvestscan.git_show` and `_index_sections` use list-argv `git` with no shell, and the path
arrives after `:` so it cannot be read as an option (OWASP A03 checked, not recalled). The new
regexes are linear or bounded by the existing `BoundedMemory` test. Privacy at design altitude:
the index now reproduces more of each item (the claim's `wt:` value, up to 70 title chars) —
text already committed in the same repo, so no new boundary is crossed. Every fixture in the
delta is synthetic (reserved-domain identity, `example-wt`, 2026-01-02 stamps). `/security-review`
could not be aimed at the work in this harness; nothing it would read is markdown-only here,
so its absence is a gap in tooling reach, weighed as nothing.

### Standing checklist

- **V1** — three overclaims recorded (PP2, PP6, PP8); no "verified" claim stronger than its
  evidence elsewhere.
- **V2** — re-run: the delta's tests, the selftest, both planes' checks, wrapscan, the legacy
  identity, the boundary, the children, the floor; the code comment's "458 sub-bullets / 45
  flag mentions" re-measured at HEAD as 139 items stopping on a list and 48 with a glyph in
  prose (units differ; consistent).
- **V3** — one mirror gap (PP7).
- **V4** — the acceptance words live in the intent record and are copied into the LEGACY
  comment with the record named as governing; the end date lives in the constant, the notice,
  the CHANGELOG and `010/190` — four homes, none stamped, held together by a test that does
  not pin it (PP3).
- **V5** — code, notice and CHANGELOG agree on the end-exclusive date; "30 days" disagrees
  with the arithmetic (PP8); `010/190` agrees with the code's removal list and both omit the
  same things (PP4).
- **V6** — lens 4 above.
- **V7** — provenance stated above and in the brief.

### The grace at its boundary — synthetic board, both planes, `run_check(today=…)`

```
form      plane     2026-11-17   2026-11-18   2026-11-19   no date (run 2026-10-28)
old       worktree  0 ⚠️ notice   1 stale      1 stale      0 ⚠️ notice
old       staged    0 ⚠️ notice   1 stale      1 stale      0 ⚠️ notice
new       worktree  0 current    0 current    0 current    0 current
new       staged    0 current    0 current    0 current    0 current
neither   worktree  1 stale      1 stale      1 stale      1 stale
neither   staged    1 stale      1 stale      1 stale      1 stale
old+problem (both)  1, ⚠️ notice and the ✗ problem line both printed (2026-11-17)
rebuild / rebuild --from-index on an old-form index (2026-11-17): writes the new form, exit 0
```

CLI with no date, on 2026-10-28: `--check` and `--check --staged` both exit 0 with the notice,
the staged remedy carrying `--from-index`. Live result, not inference: the grace is open today
and I did not run on or after 2026-11-18.

### The children, by count (read-only, `board` check mode only)

- Split boards found: **11** of the repos the harness exposed.
- On 2026-10-28 (no date injected): **9** pass on the new form; **2** pass only under the grace; **0**
  fail — identical on the worktree and staged planes.
- On 2026-11-18 (`today=` injected, both planes): the same 9 pass; the **2** red as stale.
- Of the 2: one has bumped its doctrine pin past the delta (and committed an old-form index
  after it — the hand-up's stopgap); one has not bumped its pin, so by the house's own channel
  (pin bump → CHANGELOG) it has not yet been told.
- Which `board.py` each plane runs: hook → the shared primary checkout's `tools/` (11/11),
  currently the delta's code; CI → `floor.yml@main`, `atelier-ref` default `main` (11/11).
  No child pins or vendors a copy.
- Guards: 1 child's rebuilt index would carry 1 line its own enforced wrapscan refuses while a
  multi-line claim is live; 0 lines on the other 10; this repo scopes wrapscan to doctrine
  dirs, so it never meets the case.

### Findings

**PP1 — MODERATE. The projected claim is unbounded, and in one child the notice's remedy
cannot be followed while a claim is live.** The title is capped at `TITLE_MAX` (70); the claim
is `\(claimed [^)]*\)` with no cap, now joined across lines and placed ahead of the link — the
one position the code's own comment (lines 309–318) says breaks wrapscan's single-token
exemption. Live: one child, 166 → 482 columns, refused by that child's hook; `010/130` has
named this class, open, since 2026-08-17, and `tools/README.md` lines 108–112 already tell
children to scope wrapscan off the index — the notice repeats neither. From 2026-11-18 that
child reds on `board` on both planes with no clean path but closing claims or rescoping. Not
MAJOR because `board` itself never reds for it, the trigger is the child's own wrapscan scope
against the README's advice, it is one child today, and atelier holds it as open work
(`320/730`, remedy out of scope here).
*Counsel (not applied):* project the claim as the legend defines it — `(claimed <stamp>, wt:
<name>)`, the first two fields, or cap it as the title is capped — and say in the CHANGELOG
what the README already says; close or cite `010/130` with whichever is chosen.

**PP2 — MODERATE. The plain-text title fallback widened to the whole paragraph, undisclosed,
and the marker carry did not follow it.** For a head with no `**`, the title is now the first
70 characters of the paragraph with `…`, where it was the whole first line. Children: 78 index
lines re-titled this way (69 `[ ]`, 9 `[x]`), 0 on this board, which is why the selftest and
the suite never see it (every fixture title is bold). Structural half, proven synthetically: a
line-two fragment such as `(15/7/26) <!-- datescan:allow: … -->` is reproduced into the index
line while `projected_markers` (`end` models only a bold title and a claim) drops the marker —
the exact class the marker carry exists for (comment at lines 175–178). No live instance in
2,305 items; the CHANGELOG does not mention plain-title items.
*Counsel:* keep the fallback to the head (the paragraph read exists for wrapped bold titles and
claims), or extend `end` to the fallback title's reach and say so in the notice.

**PP3 — minor. The suite proves the mechanism, not the contract.** Ten mutations of a scratch
copy: seven caught (date off-by-one, grace under `--rebuild`, paragraph stop removed, flags from
prose, grace worktree-only, markers from the whole paragraph, title from head only). Three stay
green: the constant moved to 2026-11-19 (every test derives from the constant); `_index_entry_v1`
drifted (claim masked) — byte-identity with the pre-delta tool is pinned by nothing but my
probe; unindented continuation joined. The default-date path (`_today_utc`) is exercised by no
test.

**PP4 — minor. The removal instruction is incomplete, in the code and in `010/190`.** Both name
the constant, the two `_v1` functions, `_legacy_accepted` and the one branch. Following that
verbatim in a scratch copy leaves `today`, `_today_utc`, the `_entry` seam, the `date`/`Callable`
imports and "LEGACY" docstring text behind, and `test_board.py` fails to **import** (the
`LegacyGrace` class body reads `board.LEGACY_INDEX_ACCEPTED_UNTIL`), so all 59 tests go unrun
until the remover notices. Self-correcting, but owed in the instruction.

**PP5 — minor. The in-band notice does not reach where a child looks.** It is a ⚠️ line on
stdout with exit 0. `floor.py` streams it (inside a collapsed `::group::` on CI, no
`::warning::`), and the summary line reads `✅ board enforced`; `board` is not wired to
`advisory_count`, the mechanism that lifts secretscan's and licenscan's counts into that
summary. So the only signal that survives a green summary is the CHANGELOG, which one of the
two old-form children has not reached. The CHANGELOG's remedy also names bare `board.py
--rebuild` without the `--from-index` form the hook prints for a dirty checkout.
*Counsel:* wire the grace line to `advisory_count` (or a CI `::warning::`) for the grace's
duration; `010/190`'s "list goes to Mike" step then has a mechanical feed.

**PP6 — minor. A code span that wraps from the state line masks the rest of line one.**
`_mask_code` runs over the joined paragraph, so an odd backtick on line one pairs with one on a
later line; a line-one allow-marker inside that span is dropped (1 live child line, 243 → 144
columns, no width harm today) and a claim placed after it would be too. `projected_markers`'
"the state line always" is not true for this shape.

**PP7 — note. V3 mirror gap.** `tools/README.md`'s board paragraph carries neither the paragraph
rule nor the grace, while the same-day sibling grace (`020/150`) got its own README paragraph
with the same end date.

**PP8 — note. Wording and arithmetic.** "30 days from 2026-10-18" is 31 days of acceptance;
"one-release" became a date in a repo that tags nothing, disclosed only in the code comment;
the end is UTC in code and output but the CHANGELOG does not say so (a hook on a UTC+13 machine
flips at 13:00 local on 2026-11-18); when other problems exist the ⚠️ "accepted" line prints
beside an exit 1.

**PP9 — note, pre-existing, not the delta's.** `StagedPlane.setUp` sets a git identity but not
`commit.gpgsign=false`, so where a global config signs with an unreachable key the 12 tests
error rather than skip (hit in this sandbox). The delta added one test to that class.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE (PP1, PP2) · 4 minor (PP3–PP6) · 3 notes
(PP7–PP9). The four owed things exist and behave as the principal's words require on both
planes and on both sides of the date; the findings are about what the projection does beyond
those words and what the notice leaves unsaid. `board` is doctrine by function (rule 3): all
findings recorded, nothing applied, counsel labelled; the principal decides.

### Re-run ledger (worktree root; exit codes read explicitly)

| command | result |
|---|---|
| `python3 tools/coldsweep.py --root . --commit 28ef94a` (per `--path`) | 0; body not read; 0 barred files touched |
| `git log --oneline 28ef94a..HEAD -- tools/board.py tools/test_board.py CHANGELOG.md` | 2 commits, both leakscan, `CHANGELOG.md` only |
| `git show --stat --format='%h %cI %s' 63720eb` | 4 files; body and hunks unread |
| `python3 -m unittest discover -s tools -p test_board.py -v` (as given) | 1; 47 ok, 12 `StagedPlane` errors: `git commit` 128, signing key unreachable |
| same, with `GIT_CONFIG_*` `commit.gpgsign=false` | 0; 59/59 OK |
| `python3 tools/board.py --selftest` | 0, `board selftest OK` |
| `python3 tools/board.py --check --root .` | 0, index current |
| `python3 tools/board.py --check --staged --root .` | 0, index current (staged) |
| `python3 tools/wrapscan.py --root . tools/board.py tools/test_board.py` | 0, clean |
| legacy identity: pre-delta `build_index` vs HEAD `_entry=_index_entry_v1`, 12 real boards | 12/12 identical, problems equal |
| boundary probe (table above), synthetic git board, signing off | as tabled |
| CLI, no date, old-form fixture: `--check`, `--check --staged` | 0 and 0, notice printed |
| child probe, 11 boards, both planes, 2026-10-28 and 2026-11-18 | 9 ok / 2 grace → 9 ok / 2 stale |
| hook and CI resolution, doctrine pins, by count | 11 shared checkout; 11 `@main`; 9 pins ≥ delta, 2 before |
| projection census, 2,305 items; synthetic matrix of 20 shapes | counts and gaps recorded above |
| width estimate from `board` output with wrapscan's rules (no scanner at children) | old 0 / new 1 line flagged |
| 10 mutations + verbatim removal, scratch copies, signing off | 7 caught; m2, m7, m10 green; removal: import error |
| `python3 -m unittest discover -s tools` (full suite, once, signing off; no `nice`) | killed at 300 s — not completed |
| `python3 tools/floor.py --plane ci --root .` (no `nice`) | 1: `leakscan` only, machine-local terms file unreadable here; `board` ✅; pathscan 1 warn-only pre-existing |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] PP1 — decide the claim's projected shape or cap, alongside `320/730`; cite or close
      `010/130`; add the README's wrapscan-scope advice to the notice.
- [ ] PP2 — decide whether the plain-title fallback stays widened; if so, carry markers to its
      reach and say so in the CHANGELOG; if not, restore the head-only fallback.
- [ ] PP3 — pin `LEGACY_INDEX_ACCEPTED_UNTIL` to 2026-11-18 in a test, pin `_index_entry_v1`
      against a stored pre-delta rendering, cover `_today_utc` and the indented-only rule.
- [ ] PP4 — complete the removal list in the LEGACY comment and `010/190` (tests, `today`,
      `_today_utc`, `_entry`, imports).
- [ ] PP5 — wire the grace notice to `advisory_count` or a CI annotation; add `--from-index`
      and "UTC" to the CHANGELOG entry.
- [ ] PP6 — mask code spans per physical line, or document the wrapping-span case.
- [ ] PP7 — one README line for the grace's duration, matching the sibling grace's treatment.
- [ ] PP8 — correct "30 days"; say UTC; consider suppressing the ⚠️ line when exit is 1.
- [ ] PP9 — `StagedPlane.setUp`: set `commit.gpgsign=false` (pre-existing; outside the delta).
- [ ] Orchestrator — the full suite and `leakscan` need a run outside this sandbox before close.

ACT 1 SAVED

---

*Act 2 run by `claude-fable-5-1` at effort xhigh through the Claude Platform
API (an API harness, read-only sandboxed tools), 5 turn(s), metered US$1.22;
orchestrated by session f7b25adb, 2026-10-28.*

### Reconcile (act 2, 2026-10-28 UTC)

Opened for this act, after act 1 was written into the brief: the sibling (released by session
`f7b25adb`); intent record `010/170` whole (lines 1–10 and 14–33 newly); `010/180` whole;
`320/450` whole; `320/730` lines 25–32; the bodies of `28ef94a` and `63720eb`. Two small
read-only probes were run to answer sibling hypotheses 4 and 8; nothing in act 1 is revised.

#### Against the sibling's ten hypotheses

1. *UTC day.* Confirmed in act 1 (PP8, PP5): `_today_utc()` reads UTC; the flip is 13:00 NZDT
   on 2026-11-18; the CHANGELOG names no zone. Stands as a note.
2. *Two planes, two versions.* Attacked and not the geometry on this machine (lens 1, C): no
   child vendors or pins a copy; all 11 hooks resolve to the shared primary checkout, whose
   `board.py` is byte-identical to HEAD's, and all 11 CI calls float at `main`. So no child is
   red in CI and green at the hook; both planes flip together on 2026-11-18, and together the
   day `010/190` lands if that comes first.
3. *The pointer landed 59 s after the code.* Not examined in act 1 (the brief barred the close
   commit's hunks). Reconciled now: `28ef94a` landed the code and `63720eb`, in the same
   session, closed the record, filed `010/180` and queued the pointer — a two-commit series
   whose last commit completes the item, the shape TA9 (2026-07-28) accepted as meeting the
   rule's intent. The two later commits on `CHANGELOG.md` are hours after and not the delta's.
   Recorded as **PP10 (note, formed at reconcile)**: met in intent; the delta commit and the
   pointer commit are distinct, so a future reader of `git log` meets the work one commit
   before its pointer.
4. *This pass's own pointer as a specimen of `010/180`'s third class.* At HEAD the pointer is
   `[ ]` again (the brief-writing claim was released), so the live line shows only the
   truncated title (168 columns, `…`). The mechanism reproduces synthetically: `TITLE_RE`'s
   group carries a claim written *inside* the bold span into the title text (then cut at 70),
   and `CLAIM_RE` places the same fragment in the claim slot — twice on one line. `010/140`
   closed this duplication for the fallback path only; the bold path is new reach. The author
   filed it as `010/180` (3); it sits beside PP1 and is not re-numbered here.
5. *Block-start pattern stops too early.* Measured in act 1 (lens 1, 4): the stricter stops
   (`#x`, lone `|`, `2.`) fire on 28 indented headings and ~28 table rows across the children;
   **no** real item loses title or claim text to them (0 unclosed titles; the 14 unprojected
   claims are sub-bullets).
6. *Narrower than the renderer on lazy continuation.* 9 child items; each projects exactly as
   before the delta; stated in the docstring. No finding.
7. *"One release" became 30 days.* Act 1 held it as a note inside PP8. The newly read account
   (record lines 29–30, commit body) says the span was the orchestrator's choice "not a
   ruling", and the record shows the principal met the date only in the closing account, after
   landing. Under rule 3 an approval is "conditioned on being informed", so the end date stands
   as the principal's word but is open to challenge on the briefing. Raised as **PP11 (minor,
   formed at reconcile)**: put the mapping — "one release" → 2026-11-18, in a repo that tags
   nothing — to the principal explicitly at the `010/190` step, with the child counts, before
   the cut-off reds anyone.
8. *A real flag wrapped onto line two is dropped.* Measured now: 22 of 2,305 items open their
   first continuation line with a board flag glyph; in all 22 the bold title already opened on
   line one, so by the tool's own definition they are mentions; **0** are flags pushed past the
   wrap. The author's "flags read line one" loses nothing measured.
9. *Grace path with problems.* Probed in act 1: problem lines print first, then the ⚠️ line,
   exit 1 — order is right; the "accepted" wording beside exit 1 is PP8's last point.
10. *Mirror sites.* No README, skill or template states the first-line rule, so nothing is now
    false (PP7); but `320/450` §1's "children need one README sentence" and `010/180`'s "say in
    the board README where a claim goes when the title wraps" are the same unlanded sentence
    the author named twice — PP7 gains that grounding.

#### Against the author's account

- *Counts* (record lines 22–25; body): 297 changed lines on 2026-10-18 with 274 titles made
  whole; at HEAD my census reads 300 and 278 (the board moved). Consistent.
- *"Probed: the old index from `main` passes with the notice, and fails on the end date"*:
  re-driven on both planes, on real and synthetic boards, either side of the date and on the
  run date. Holds.
- *"The old form is reproduced byte for byte (confirmed: atelier's own pre-rebuild index, and
  origin/main's)"*: widened to 12 real boards against the extracted pre-delta tool. Holds.
- *"59 board tests, 1963 Python tests green"*: 59 confirmed; the full suite exceeded this
  sandbox's cap (the sibling's own run on 2026-10-26 reports 2032 OK in 566 s).
- *Allow-markers "never from further down (one item here would otherwise have exempted its
  index line … for prose the index never shows)"*: the reason is sound for bold titles and
  claims; it does not reach the plain-title fallback's widened window (PP2) or a code span that
  wraps from line one (PP6), neither of which the account considers.
- *"Removing the grace is deleting the LEGACY block and the one `run_check` branch"* (body;
  repeated in `010/190`): PP4 shows the verbatim removal leaves seams and reds the suite at
  import.
- *`010/180`'s three residuals*, found by the author reading every changed line: (1) 11 wrapped
  titles lose a leading non-flag glyph, (2) a leading `--` is stripped, (3) the claim-in-title
  duplication above. Honest and filed; none reached the CHANGELOG, which is PP2's pattern
  (rendering changes a child meets without being told). PP2's own class — plain-title items
  re-titled to a 70-character cut, 78 lines on the children, 0 here — is not among the three,
  because the author's reading was of this board's changed lines only.
- *The acceptance words*: the record's line 16 adds "the notice children read at their pin
  bump" as the realisation of "tell the children"; that is the house channel (PROPAGATION), and
  PP5's point is only that it is the sole one that survives a green summary.

#### Against the hand-up's options (`320/730` lines 25–32) and `320/450` §1

The child offers three shapes — exempt the index from wrapscan, keep claims short, or a
projection that caps or wraps the claim — and notes "the CHANGELOG notice may want to name the
case so other children meet it at their pin bump rather than at a landing". PP1 was formed
before reading this and arrives at the same two halves independently: a bounded claim in the
projection (atelier's), and the notice naming the case and the README's standing advice. The
remedy choice stays atelier's open work under `320/730`; PP1 records only what the delta owed.
`320/450` §1's severity note (the child's MAJOR against BS2's MODERATE) is the same divergence
PP1 states: `board` never reds for it, the child's own width gate does.

#### Against the sibling's twelve re-run results

Items 1–6 and 9 agree with the ledger. Item 7 (full suite OK) and item 8 (floor exit 0) could
not be reproduced inside this sandbox for environmental reasons stated in act 1's limits; the
sibling's results stand as the brief-writer's. Item 10 covered the worktree plane only; act 1
adds the staged plane, the day after the date, and the "neither" and "old + problem" cases.
Item 11 counted **6** children under the grace on 2026-10-26 (worktree plane, possibly dirty
checkouts); act 1 counts **2** on 2026-10-28 on both planes, the staged plane agreeing — so
four boards were rebuilt in the two days between, or carried uncommitted rebuilds then. Item
12's rough measure (1 claimed line over 100 columns in 1 repo) matches act 1's exact-rule
estimate (1 line, 1 child, old 0 → new 1).

#### Findings formed at reconcile

- **PP10 — note.** The pointer landed one commit after the code (59 s, same session); meets
  rule 4's intent per TA9, grammar aside.
- **PP11 — minor.** The realisation of "one release" as 2026-11-18 was the orchestrator's and
  reached the principal only in the closing account; raise it to him with the counts at the
  `010/190` step, as a briefing question, before the cut-off.

#### Overall, restated

**PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE (PP1, PP2) · 5 minor (PP3–PP6, PP11) · 4 notes
(PP7–PP10). Act 1's text and severities are unchanged; the reconcile added one minor and one
note. `board` is doctrine by function (rule 3): nothing applied; the principal decides.

#### Fold-in

I cannot write files. The sibling is already removed from the worktree (`git status` shows it
deleted); its full text, as released above, is to be appended verbatim beneath this reconcile
by session `f7b25adb` and the sibling file left deleted, so the record keeps the one-file shape
`EVIDENCE` §9 asks for.

ACT 2 SAVED

---

## Deferred sibling, folded below the verdict

*Folded by the orchestrator, session f7b25adb, 2026-10-28: the held-back
sibling's text follows verbatim, as REVIEW.md rule 1 requires, and the sibling
file is removed in this commit.*

# Sibling to the paragraph-projection and grace cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

Holds: one intent-record pointer, three locations of the author's account and one of other
held-back framing, ten hypotheses and twelve re-run results.

## Intent record

- `docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md`
  — read in full by the brief-writer. Filed at `e1ce2a1` (2026-10-18 08:36 UTC), closed at
  `63720eb`. Lines 11–14 (to the end of the quoted answer) are the acceptance test. The
  principal's own words are only the two-word answer on line 14; the longer quote on lines
  11–13 is the queue run's recommendation that he answered.

## The author's account, by location

- Intent record lines 1–10: the author's statement of the problem and the planned fix, written
  at filing, before the build. Line 14 after the quote, through line 16: what the author took
  to be owed.
- Intent record lines 17–33: the author's closing account — the paragraph rule as built, which
  field reads what and why, counts of changed index lines by class, two classes that got worse
  (filed at `010/180`), how the grace works, that the 30-day span was the queue run's choice
  and not a ruling, one probe of the old index from `main` either side of the date, the
  CHANGELOG entry as the notice to children, and test counts at the time.
- `docs/roadmap/010-board-store-migration-per-item-files-mik/180-the-paragraph-projection-loses-two-small-signals.md`
  whole: the author's own residual list, filed in the pointer-landing commit, with shapes to
  weigh. The comments and docstrings in `tools/board.py` also carry the author's reasons, but
  they are the delta and were readable in phase 1.
- Not the author, but framing held back for the same reason: `320/730` lines 25–32 (a child
  session's remediation options and its review note), and line 10 of the same item, which
  calls the line-two claim reaching the index "as intended". The bodies of `28ef94a` and
  `63720eb` were not read by the brief-writer.

## Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. **The end date is a UTC day.** `_today_utc()` reads the UTC date, so the old form is refused
   from 2026-11-18 00:00 UTC, which is 13:00 on 18 November in New Zealand daylight time. The
   CHANGELOG entry says "before 2026-11-18" with no timezone. Does a child reading it locally
   get the same day the code uses?
2. **Two planes, two versions.** A child's CI floats at `floor.yml@main` and runs the new
   projection; its commit hook runs its pinned copy. Before a pin bump, a rebuild with the
   pinned copy writes the old form, which CI accepts only until the end date. After it, does
   every child that has not bumped its pin red in CI on any commit that changes its board,
   with the hook still green? The child counts in the re-run results suggest how many
   children that touches.
3. **The pointer did not land in the landing commit.** The work landed at `28ef94a` and its
   pointer at `63720eb`, 59 seconds later. Rule 4 asks for the pointer in the commit that lands
   the work, or in the last commit of a series. Does a close-and-queue commit after the code
   commit meet that, or is it the gap the rule closes?
4. **This pass's own pointer is a live specimen of `010/180`'s third class.** Its claim was
   inserted on line two, inside the wrapped bold title. Its index line now shows a truncated
   title ending in "…" and about 180 columns of claim fragment before the link. Which part of
   the projection produces each, and is either the behaviour the delta meant?
5. **The block-start pattern stops too early on prose.** `_BLOCK_START_RE` matches `#` and `|`
   with no following space, so a wrapped line that begins `#122` or a pipe in prose ends the
   paragraph, which CommonMark would not. Does any real item lose title or claim text that way?
6. **The paragraph rule is narrower than the renderer's.** CommonMark keeps an unindented
   line in the paragraph (lazy continuation); the code stops at the first unindented line. Do
   any real items wrap with no indent?
7. **"One release" became 30 days.** The acceptance words ask for a one-release grace. This
   repo keeps everything under _Unreleased_ and children float at `main`, so there is no
   release to count. The code says the span was the orchestrator's choice. Is the mapping
   grounded anywhere, and did the principal see it?
8. **A flag wrapped onto line two is dropped.** Flags read the state line alone. A long title
   can push a real flag past the wrap. Is that loss measured, or only the opposite case (a
   glyph mentioned in prose)?
9. **The grace path with problems.** When the index matches the old form and the board also
   has problems, the grace prints its notice and returns 1. Is the stale-versus-problem message
   clear to a child, and do the problem lines print first?
10. **Mirror sites.** `docs/roadmap/README.md` describes state lines and what the index lifts.
    Does any README, template or skill still say the index reads the first line, or say where a
    claim goes when a title wraps?

## Re-run results held back from the brief

Run once by the brief-writer, 2026-10-26 UTC, from its worktree root at `6f78d85`, in the
foreground, on this machine:

1. `coldsweep --commit 28ef94a`: exit 0; four files; nothing left out as barred; closing line
   present.
2. `test_board.py`: 59 tests, OK, exit 0 (also with `-v`).
3. `board.py --selftest`: OK, exit 0.
4. `board.py --check` on both planes: exit 0, index current.
5. `wrapscan` over `tools/board.py` and `tools/test_board.py`: clean, exit 0.
6. `git log 28ef94a..HEAD`: nothing on `tools/board.py` or `tools/test_board.py`; two later
   commits on `CHANGELOG.md`, both for another tool's items.
7. Full Python suite under `nice`: 2032 tests, OK, exit 0, about 566 s. The intent record's
   count is from 2026-10-18; later commits added tests.
8. Floor, ci plane, under `nice`: exit 0. leakscan shows 🟡 (the ci plane does not pass
   `--require-terms`); four guards are warn-only by wiring.
9. Legacy byte-identity, on a copy of this repo's board: the pre-delta `board.py` (extracted
   from `28ef94a^`) and `_index_entry_v1` render identical indexes; the new and old forms
   differ on 300 lines today (the intent record counted 297 on 2026-10-18).
10. Boundary probe, worktree plane only, on a copy of this board with an old-form index:
    `today=2026-11-17` exit 0 with the notice; `today=2026-11-18` exit 1, stale; no date
    injected (run date 2026-10-26) exit 0 with the notice. The staged plane was exercised only
    by the delta's own unit test.
11. Child probe, read-only, check mode, worktree plane of each primary checkout (which may
    carry uncommitted edits), by count: 30 other repos in the machine's repo directory; 11
    with a split board; 5 current today and on the end date; 6 pass today only under the grace
    and red stale on 2026-11-18.
12. Claimed lines over the same 11 children, new projection: 55 claimed index lines; 1 whose
    text before the title link exceeds 100 columns, in 1 repo. Rough measure: it splits at the
    last ` [` before the link and ignores each child's own wrap width and exemptions.

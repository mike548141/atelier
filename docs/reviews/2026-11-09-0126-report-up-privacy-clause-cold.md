# Cold pass — the class-only privacy clause in the report-up duty, applied (`160/300`, RU1, RU8–RU10)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RAN — act 1 2026-11-15 UTC, act 2 (reconcile) 2026-11-16 UTC. PASS-WITH-FINDINGS
(0 MAJOR · 1 MODERATE · 4 minor · 3 note, HU1–HU8; HU7, HU8 formed at reconcile). Findings are the
principal's to decide (rule 3); the sibling is folded in below by the orchestrator.
**Sizing:** **small** — one commit, about 50 lines of doctrine across three surfaces and one stamped
copy.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1050-rule-4-cold-pass-queued-report-up-privacy-clause.md`.
**Why it earns a review:** Every child reads this bullet at session start, and it is the rule that
decides what a private repo may say on a public, irretractable surface. Worst failure: a private
repo's name or contents published because the clause left a surface uncovered or two copies
disagreed, which a push cannot undo.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-08, in its ruling round, and the Sonnet worker it dispatched, which wrote it (per the
  queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `84e3aa7f` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). Neither authored any of this delta,
  and neither was started or instructed by the author. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing its briefs. It ran
  no review and used no Fable model. The principal's rule: whoever writes a brief does not run it.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  list of board items, the run constraints, and the principal's request verbatim, "Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done". It carried no framing of the
  work. The brief-writer had no contact with the author or its workers.
- **Who reviews:** a fresh Fable 5.1 session or subagent started for this pass alone, from a spawner
  that passes rule 4's criterion. **Barred from reviewing:** session `722ac2e2` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; excerpts of the intent record: the lines naming the applied findings and
  the principal's answers, which include one-line summaries of the earlier verdict's findings;
- the delta body-free through `tools/coldsweep.py --commit 94df4aad` (subject, stat, diff, never the
  message body), `--help` of `coldsweep`, `board`, `leakscan` and `reviewscan`, commit subjects
  through `git log`, and file names under `docs/reviews/` and
  `docs/roadmap/160-doctrine-review-owed/`;
- the last three index lines of `docs/SESSIONS.md` and one earlier session record, read for the
  format of its own closing record; and the results of the re-run lines below, held in the sibling.

It did **not** open `docs/ROADMAP-DONE.md`, any other session record, any other prior verdict, or
any delta commit's message body. Its harness also loaded user-level and repo instruction files and a
memory index, which hold private context this brief does not carry. Everything evaluative it formed
is in the sibling.

## The acceptance test

The principal's answer of 2026-11-08, as the delta's changelog entry records it: chose *"add privacy
line now"*. An answer to options offered, not a ruling in his own words. The clause's substance is
`docs/method/PROPAGATION.md` § *The route*, rule 2 (*Carry the class, never the child's specifics*),
which predates this delta.

## What the work is

One commit on `main`, `94df4aad` (first confirm your tree has it: `git merge-base --is-ancestor
94df4aad HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 94df4aad \
  --path docs/method/PROPAGATION.md \
  --path docs/build/templates/CLAUDE.md \
  --path CLAUDE.md \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 94df4aad..HEAD -- docs/method/PROPAGATION.md docs/build/templates/CLAUDE.md CLAUDE.md CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- The `floor` region's report-up bullet now says a private repo describes the problem by its class
  only and names neither itself nor its contents on the branch, PR title, commit subject, PR body or
  item.
- The stamped copy (`docs/build/templates/CLAUDE.md`) and atelier's own `CLAUDE.md` carry it.
- Children pick it up at their next pin bump, where `stampscan` reds a stale copy.
- RU8–RU10: the "nine findings" sentence, § *The duty* naming section `320`, and § *The route* step
  1 pointing at `docs/roadmap/README.md`.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** The findings of the earlier report-up pass that the principal has not decided
(RU2–RU7, RU12), and any guard for this clause, which the delta says is not built.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. This delta **is** a privacy control. Trace every surface a
hand-up creates, against the clause, and state which it covers. Check the open catalogues for the
information-exposure class (CWE-200 family) if you want a checklist; the surfaces are this repo's,
so the walk is yours.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane hook --root .` and `--plane ci`
- `python3 tools/stampscan.py --root . .`

## House rules for this run

**Live systems:** read-only reads of live systems as needed, no live writes. A check that would need
a write is marked **NOT RUN**, with what it would have checked. No push and no `gh` call that
writes, except committing this one file as the process below says.

- Never print a secret, and quote no key body, fixture bytes, personal data, private repo name or
  private path. This repo is PUBLIC; a child is referred to by type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Scratch
  repos, mutated copies and fixtures go under your session scratchpad and are deleted when you
  finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `instruments/`.
- One heavy process at a time, foreground, long timeout, `uptime` first. Never run an installed tool
  by bare name from `PATH`: run it from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it only from a clean tree
  at a scratch clone of the code, or discharge it by grounds; never with this brief or its sibling
  dirty. A clean pass over markdown is weighed as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, The earlier verdict is
`docs/reviews/2026-09-25-0715-report-up-duty-cold.md`. the queue pointer above, this brief's sibling
`docs/reviews/2026-11-09-0126-report-up-privacy-clause-cold.deferred.md`, every delta commit's
message body, and the intent record
`docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md` beyond its
first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred. This pass reviews the application of an earlier pass's findings, so the delta's own
text carries that verdict's finding identifiers and decision stamps: `REVIEW.md` § *Applying
decisions to doctrine* names this as a residual exposure that cannot be closed. Review the edited
text at HEAD and commit your findings first.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1050-rule-4-cold-pass-queued-report-up-privacy-clause.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/300-rule-4-cold-pass-queued-report-up-duty.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`94df4aad`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `HU`: `HU1`, `HU2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling
is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (2026-11-15 UTC)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 3 minor · 2 note** (HU1–HU6).

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection. Run on 2026-11-15 UTC
  from worktree `atelier-160-1050-2217` (read-only to me except this file), HEAD `f24bbaf9`, which
  carries `94df4aad` (`merge-base --is-ancestor` exit 0).
- **Spawn:** started by headless orchestrator session `9ec596e5` (Opus 5.5), itself started by
  drain session `21a271a5` (Opus 5.5) under the principal's `/fable-drain` order of 2026-11-16
  06:53 NZDT (2026-11-15 17:53 UTC), the approval this brief waited for. Both are rule-4 off-tier
  orchestrators: they hold the context partition, form no finding and write no severity. Neither
  wrote the brief or the delta. Neither barred session (`722ac2e2` and what it started, `84e3aa7f`,
  `74f2b8cd`) started or instructed me, and no contact with any of them occurred.
- **Spawn prompt, in substance (process only):** my identity and item; the worktree path and the
  no-`cd`, absolute-path rule; the brief's path and an order to read it first and follow it;
  `REVIEW.md` for the verdict shape; the partition (the `.deferred.md` sibling removed from the
  worktree, its path released after act 1 is committed, no search for it elsewhere); a running
  work log at a user-local path, appended to the review at the fold; what I may write (this file
  and that log); no git command that writes, the orchestrator commits; read-only live reads
  allowed, no live writes; scratch under the session scratchpad; load rules (`uptime`, `nice`,
  one heavy process at a time); the public-repo rules (session ids only, no private repo name or
  path, a child by type only); and the act-1 / act-2 stop points. It carried no question about
  the delta, no pointer to where the risk lives, and no request about any finding.
- **Barred-set choice:** the brief's list, unchanged: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
  `docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer `160/1050`, the
  sibling, every delta commit's message body, and the intent record `160/300` beyond its title.
  Every tree sweep ran through `tools/coldsweep.py` with both board items added by
  `--also-exclude`; `--include-barred` was not used. Both landing commits were read with
  `coldsweep --commit`, scoped by `--path` to the four delta paths; no board file was shown.
- **Exposure, disclosed:** the harness loaded the user-level instruction file and a memory index
  that hold private context and one line about two other passes' owed rulings; nothing in them
  concerns this delta. The harness also showed the worktree's `git status` and five recent commit
  subjects (claims and another pass's fold), none an account of this delta. I skipped the
  session-log step of the read order (rule 2). I read `CLAUDE.md` whole at HEAD: it is a delta
  surface, and reading the delta is never barred.
- **Method trail:** every command, file range and result is in the work log the orchestrator
  folds in below the reconcile (`REVIEW.md` § *The lifecycle*, the principal's ruling of
  2026-11-15 UTC on method). The summary here is enough to repeat each check.
- **Interrupted and resumed, disclosed:** the weekly usage limit cut this session off at about
  2026-11-15T22:30Z, after the act-1 text above was written to this file and before its Status
  line and scanner runs. On the principal's word (*"resume to finish everything that was partly
  done i.e. in-progress"*) the same session resumed at 2026-11-15T23:54Z, re-read its own log,
  and finished act 1: no finding or severity was formed or changed after the resume. The sibling
  stayed unopened throughout.

### What I examined, and how

- The delta `94df4aad` body-free (subject, stat, diff; 4 files, +49/−14); its successor
  `6bea4d10` body-free, scoped the same way (1 file, +4/−4); the later `160/300` application
  `3312cdbd` body-free, scoped the same way, because it edits the sections the delta edits.
- Each delta path at HEAD: `PROPAGATION.md` lines 115–229 (the floor region and stamp mechanics),
  329–374 (bundled variant) and 475–864 (§ *Pointing up* whole);
  `docs/build/templates/CLAUDE.md` 85–105; `CLAUDE.md` 36–75; the changelog entry at
  1437–1458, diffed against its text in
  `94df4aad` (identical).
- The sites the clause points at or depends on: `docs/roadmap/README.md` whole, the section `320`
  README (1–25) and its newest item's head, `RECORD.md` § *The record is public*,
  `tools/README.md` § `namescan`, `tools/blockscan_map.json` 48–66, `tools/pins.py` docstring,
  `--help` of
  `coldsweep`, `stampscan`, `wrapscan`, `pins`.
- Live, read-only: `gh run list --commit` for both landing commits; `gh pr list --state open`
  with the fields `number,title,headRefName,createdAt`; the two open PR bodies grepped for the
  hand-up words (counts only); the visibility of two child repos whose names sit in pre-clause
  index lines.
- Not examined, and why: the sibling, the pointer, the intent record's body, prior verdicts and
  the session records (barred until act 2); any child repo's tree (none is in this worktree, and
  the clause reaches a child only through its own pin bump — see HU2); the delta commits'
  message bodies.

### Lens 1 — approach and assumptions (named first, then probed)

- **A1 — a session in a child can tell that its repo is private.** Confirmed: the floor carries
  the repo's own visibility fact (`PROPAGATION.md` 220–221), so the clause's trigger is a fact the
  reader already holds, not something it must infer.
- **A2 — the floor is the text that binds where nothing else of atelier is read.** Confirmed by
  design (119–121) and by `stampscan`: the template's copy is identical to the region (105 lines).
  The right altitude: the harm the clause prevents is one-way and lands on the child, and the
  floor is the one place a child session is guaranteed to read before it pushes anything.
- **A3 — the surfaces the floor enumerates are the surfaces a hand-up publishes.** Damaged: the
  commit message body is published on push and is not in the list (HU1).
- **A4 — children receive the clause at their next pin bump, and a stale copy reds.** Mechanism
  confirmed in `tools/pins.py` (the floor-copy report, `160/340`), but not as the changelog
  describes it (HU2).
- **A5 — the clause's substance predates the delta in § *The route* rule 2.** Confirmed
  (641–660, the principal's ruling of 2026-09-19). The floor is a narrowing-free summary of it:
  it drops rule
  2's escape (a class that cannot be stated without specifics goes to the private estate root,
  644–645) but says it is a lossy summary and points at the section (194–195, 203). No finding.
- **A6 — "add privacy line now" is an answer to options, not a ruling in his words.** The
  changelog records it as his choice, not his ruling. Correct as written.

### Lens 2 — correctness and quality

- The floor bullet, the stamped copy and atelier's `CLAUDE.md` carry the clause (94df4aad diff;
  HEAD 197–203, template 97–103, `CLAUDE.md` 71–75). RU8 (539–541: the first nine of section
  `320`, which holds 87 items), RU9 (§ *The duty* names section `320`) and RU10 (step 1 points at
  `docs/roadmap/README.md`) are each present at HEAD as the changelog says.
- Overclaims: one, in the changelog's mechanism sentence (HU2). The delta's wrap slip (a
  102-column line in the RU8 sentence) passed `wrapscan` (limit 85, "materially over", and it
  reported clean on the `94df4aad` copy) and was rewrapped by the next commit (HU4).
- The cross-references reach their rules: the floor's "§ *Pointing up*" reaches the section that
  holds the route (475); `CLAUDE.md`'s "§ *The route*, rule 2" reaches the rule (641). Step 1's
  pointer reaches the format and rebuild rules but not a numbering rule (HU5).

### Lens 3 — completeness and harvest

- Mirror sites swept (`coldsweep`, barred set plus both board items excluded): the clause's words
  appear only in the floor region, the stamped copy, atelier's `CLAUDE.md`, § *The route* and
  § *Report without harming the parent*, and the changelog. No copy lives in `skills/`,
  `docs/build/REPO-*.md` or the bundled-mode variant (which inherits the bullet by construction,
  359–360). `tools/blockscan_map.json` anchors the bullet on its bold lead, which the delta did
  not change, and maps it to § *Pointing up*; still correct.
- Three wordings now exist: the canonical floor region, its stamped copy (watched) and atelier's
  own `CLAUDE.md` sentence (unwatched, and addressed to the wrong actor — HU3).
- What the delta did not cover and the brief names a non-goal: a guard. For the record, atelier
  has since grown `namescan` (branch name and commit title, message plane, warning until
  2027-05-03) and `leakscan --messages`; § *Report without harming the parent* at HEAD (797–800)
  still says the lint "is not built". Both are term-list guards in atelier's own tree and reach a
  shape-1 filer's commit through atelier's hooks only; neither reads a child's tree. Not a finding
  on this delta; the stale "not built" is the application `3312cdbd`'s text, noted for its own
  pass.

### Lens 4 — security and privacy (the delta is a privacy control)

The surfaces a hand-up creates, traced against the clause as the floor states it:

| Surface | Published on push? | Named by the floor clause | Named elsewhere |
|---|---|---|---|
| Branch name | yes | yes | § Report w/o harming, rule 1 |
| Commit subject | yes | yes | § Report w/o harming, rule 2 |
| **Commit message body** | **yes** | **no** | not named anywhere (HU1) |
| Commit author identity | yes | no | the published identity; `PERSONAL-DATA.md` |
| PR title | yes (on open) | yes | § Report w/o harming, rule 2 |
| PR body | yes (on open) | yes | § Report w/o harming, rule 2 |
| PR comments | yes | no | none; no hand-up seen carrying one |
| Item file name (slug), index line | yes | "item", read widely | index generated from the item |
| Item body | yes | yes | § The route rule 2 |
| CI log of the floor run on the PR | yes | no | derived from the item's content |
| Parent's merge commit, PR note | yes | no (not the filing's) | `RECORD.md` § *Record is public* |
| Child's own record, `Pending upstream:` line | no | — | private tree |

Every surface except the commit body is either named by the clause, derived from a named surface,
or owned by a rule that already reaches it. Live state: the two open hand-up PRs (#135, #136) carry
`report-<subject>-<HHMM>` heads with no repo token and a body that says hand-up; the twelve most
recent merge subjects on `main` say "land hand-up #n" and name no child. Two pre-clause index lines
(items `320/280`, `320/710`) carry a child repo's token in a title or file name; both repos are
public (checked live), which the rule allows. `/security-review`: discharged — a landed-delta
review of Markdown, which the scanner's exclusions bar, so its clean pass would weigh as nothing;
and the
worktree is not clean (the sibling shows as deleted), so it was not aimed. Information-exposure
class checked against CWE-200's shape (exposure through a published channel the author did not
count as output): that is exactly HU1's commit-body gap.

### Findings

- **HU1 — MODERATE. The floor's surface list is closed and omits the commit message body.** The
  floor says "on the branch, PR title, commit subject, PR body or item" (`PROPAGATION.md` 199–200;
  template 102–103). A commit body is published the moment the branch is pushed, and the house's
  own convention asks for a "why-dense body" (`CLAUDE.md` § Conventions), which is where a filer
  writes the incident — the host, the client, the path. The canonical rule frames its list as
  "every surface the filing creates" (647) and atelier's own `CLAUDE.md` copy keeps that frame
  ("on any surface the filing creates (…)", 73–74); the floor copy, the one text a child reads,
  drops the frame and keeps only the list. § *Report without harming the parent* (750–756) names
  the first line of the commit and never the body. A child already filed that no scanner read a
  commit body (`320/550`); `leakscan --messages` and `namescan` now do, by term list, in atelier's
  hooks. *Counsel:* restore the frame in the floor and make the body explicit — "on every surface
  the filing creates: the branch, the commit message, the PR title and body, the item" — so the
  list reads as examples, not a fence; the stamped copy follows at the next pin bump.
- **HU2 — minor (V1). The changelog's mechanism sentence names the wrong tool and a response not
  yet in force.** "Children pick it up at their next pin bump, where `stampscan` reds a stale
  copy" (1449–1450). `stampscan` cannot run in a child: it cannot resolve a child's `source=`
  (ST3, 270–271). What compares a child's copy is `tools/pins.py`, from atelier, against the
  floor *as it stood at the child's pin*, and it is report-only until 2026-12-09 (271–279;
  `pins.py` docstring). Two consequences the sentence hides: nothing in a child reds; and a child
  that never bumps compares clean at its own pin, so the clause reaches it only when it chooses to
  bump. *Counsel:* "`tools/pins.py` reports a copy that differs from the floor at its pin, and
  fails the fleet check from 2026-12-09."
- **HU3 — minor (V4, V5). atelier's `CLAUDE.md` sentence binds an actor who is not its reader.**
  The sentence (71–75) sits in the bullet about atelier reporting *its own* problems — atelier
  is public and may name itself — and speaks of "the reporter" of "a report from a private repo",
  which no reader of atelier's onramp is. The actor that onramp should bind is the atelier
  session that files on a private child's behalf by shape 2 (619–625) or lands a hand-up
  (read-order step 6; the merge check at 791–800), and neither duty is stated there; step 6
  reaches the merge check by pointer only. The result is a third, unstamped wording addressed to
  nobody present. *Counsel:* reword to the atelier session — "when this repo files or lands a
  private child's report, it carries the class only and names no private repo on any surface" —
  or drop the sentence and let step 6's pointer carry it.
- **HU4 — minor. The delta is two commits, and the first shipped a line over the house width.**
  `94df4aad` left the RU8 sentence at 102 columns (`PROPAGATION.md` line 529 at that commit); the
  next commit, `6bea4d10` (the pointer's landing), rewrapped it (+4/−4 in `PROPAGATION.md`). The
  brief and its sizing say "one commit". `wrapscan` passed the `94df4aad` copy (limit 85,
  "materially over"), so no floor break, and no CI run exists for `94df4aad` alone (pushed with
  `6bea4d10`, whose floor run succeeded 2026-11-08T11:31Z). `docs/roadmap/README.md` (AW6) says a
  later commit touching a queued delta's surfaces widens the pointer's delta list. Whether the
  pointer names `6bea4d10` is barred until act 2. *Counsel:* act 2 checks the pointer; if it names
  `94df4aad` alone, widen it.
- **HU5 — note (V5). Step 1's pointer promises a numbering rule the README does not hold.** RU10
  made step 1 say the README holds the board's "format, numbering and rebuild step" (604–605). The
  README holds the file-name shape `<NNN>-<section>/<NNN>-<slug>.md` and the rebuild
  (`board.py --rebuild`, `--rebuild --from-index`), and no allocation rule; the only text a filer
  meets on choosing a number is § *Report without harming the parent* (808–812, "next free
  number"). *Counsel:* say "format and rebuild step", or add the allocation line to the README.
- **HU6 — note (V5). § *The duty* sends atelier's own findings to a section whose name and README
  say "child-filed".** RU9's text (539–541) says section `320` takes findings "whoever found
  them"; the directory is `320-child-filed-findings-via-pointing-up` and its README's second
  paragraph keeps the items together *because a child filed them* and calls that evidence about
  the route. atelier's self-reports filed there dilute the section's stated purpose. *Counsel:*
  widen the README's purpose line, or name a different home for atelier's own.

### The standing checklist

- **V1** — HU2; otherwise the changelog's claims re-drive (RU8–RU10 present; copies carry the
  clause; the earlier verdict's path exists as a file name, content barred).
- **V2** — re-run ledger below; the one recorded CI success (`6bea4d10`) read live.
- **V3** — swept (lens 3): three sites carry the clause and the stamped copy is identical; no
  further mirror found in skills, templates or the bundled variant.
- **V4** — one canonical home (§ *The route* rule 2) with the floor as its stamped summary; the
  `CLAUDE.md` sentence is an unwatched third wording (HU3).
- **V5** — HU5, HU6; the two cross-references in the delta reach the rules they name (lens 2).
- **V6** — lens 4 walked surface by surface; `/security-review` discharged with grounds.
- **V7** — stated above, in the brief and here.

### Per-commit ledger

| Commit | Body-free | `--path` scope | Findings |
|---|---|---|---|
| `94df4aad` (the delta) | yes | 4 delta paths | HU1, HU2, HU3, HU5, HU6 |
| `6bea4d10` (pointer landing, rewrap) | yes | 4 paths, 1 matched; 3 board files left out | HU4 |
| `3312cdbd` (later `160/300` application) | yes | 4 paths, 3 matched | none; see lens 3 |

### Re-run ledger (2026-11-15 UTC, from the worktree root, `python3` 3.14.6, `nice -n 10`)

| Line | Result |
|---|---|
| `floor.py --plane hook --root .` | exit 0; every enforced check ✅; `attribscan` read 0 files |
| `floor.py --plane ci --root .` | exit 0; `secretscan` 28, `leakscan` 3 advisory; 🟡 0/21 declared |
| `stampscan.py --root . .` | exit 0; 1 block verified, template line 18 identical to `floor` |
| `gh run list --commit <sha>` | `94df4aad`: no run; `6bea4d10`: `floor` success 2026-11-08T11:31Z |

### Follow-up checklist (each the principal's to decide; nothing applied)

- [ ] HU1 — open the floor's frame and name the commit message (one stamped-copy bump follows).
- [ ] HU2 — correct the changelog's mechanism sentence.
- [ ] HU3 — reword or drop atelier's `CLAUDE.md` sentence.
- [ ] HU4 — act 2 checks the pointer's delta list for `6bea4d10`.
- [ ] HU5 — "format and rebuild step", or a numbering line in the README.
- [ ] HU6 — widen section `320`'s purpose line, or name another home.
- [ ] Not a finding here, for `3312cdbd`'s own pass: § *Report without harming the parent* says the
      branch-and-title lint "is not built"; `namescan` exists since.

### Reconcile (act 2, 2026-11-16 UTC)

Opened after act 1 was committed as `e10058e3` (brief only, unrevised): the held sibling; the
message bodies of `94df4aad` and `6bea4d10`; the queue pointer `160/1050`; the intent record
`160/300`; the prior verdict `docs/reviews/2026-09-25-0715-report-up-duty-cold.md` (RU1, RU2,
RU8–RU11, its counsel, reconcile and overall); the session index lines for 2026-11-08 and
2026-11-09 and the author's record `docs/sessions/2026-11-08-1059-ruling-round-722a.md`. No act-1
text is revised. Two findings are formed here and marked as such.

**Against the sibling's questions.**

- *Pointer:* "every surface a hand-up creates" — HU1 is the answer (the commit body is the surface
  left out); "the stamped copy and its canonical region still agree" — confirmed, identical.
- *Q1* (step 1 says the item carries "the incident"; the floor says class only): not weighed in
  act 1. **HU7 — minor (V5), formed at reconcile.** § *The route* step 1 (603–606) tells the
  filer the item carries "the incident, the class it belongs to, and the doctrine file"; rule 2
  (641–645) and the floor say the class and never the specifics. They reconcile — § *The duty*
  wants evidence, and an incident can be told as its class — but step 1 gives no cue that the
  incident is told that way, and a filer reads step 1 before rule 2. *Counsel:* "carrying the
  incident, told as its class (rule 2), …".
- *Q2* (surfaces not named): the lens-4 table holds the slug, the commit body, a PR comment, the
  CI log and the author line. The peer-channel message, which the sibling adds, is not published:
  it travels between sessions on one machine, and the atelier session that files from it becomes
  the writer — which is HU3's actor. Nothing further.
- *Q3* (does `CLAUDE.md`'s citation reach rule 2): yes, lens 2.
- *Q4* (who decides "private"; a repo about to go public; a public repo reporting about a private
  sibling): the floor's own visibility fact decides (A1). A hand-up publishes to atelier the
  moment it is pushed, so present visibility is the right test for the filer's own name, and the
  `320/380` "is public, or is ever made public" test governs the child's tree, not this. The third
  case is a gap: **HU8 — note, formed at reconcile.** The clause binds "a private repo" naming
  "itself or its contents"; a public child's hand-up that names a private sibling's contents or
  condition is reached only by `RECORD.md` § *The record is public* (the join rule), once the item
  is atelier's record — a file the child's floor does not point at from this bullet. *Counsel:*
  "names no private repo's contents, its own or another's".
- *Q5* (two commits; landing = queuing): HU4 reached it cold. With the pointer now read: its delta
  is **scoped to paths and names no SHA**, so `6bea4d10`'s rewrap of `PROPAGATION.md` is inside
  its scope and the follow-up "widen the pointer" is already met; "one commit" was the brief's
  narrowing, not the pointer's. The pointer landed in the commit after the landing, pushed
  together (one CI run, at `6bea4d10`): TA9's series reading, and `6bea4d10`'s body says the
  pointer was "written here at the landing". HU4's severity stands as written; the owed action
  reduces to none.
- *Q6* (does `stampscan` red or warn): HU2, sharpened — atelier's CI runs it `--warn` (advisory,
  `.github/workflows/ci.yml` line 199), it is not in the floor registry's plane tables, and in a
  child it cannot run (ST3). The changelog's "reds" is true of none of the three places.

**Against the author's account.**

- `94df4aad`'s body names the same five surfaces as the floor and says "stampscan: identical"
  (re-run, true). The list follows RU1's counsel verbatim ("branch, title, subject, body, item";
  RU1 itself said "four irretractable surfaces"), so **HU1 is a gap in the applied counsel carried
  faithfully into the floor, not a misapplication**. The severity stands: the floor is the text a
  child obeys, and the body it omits is published all the same.
- `6bea4d10`'s body: "rewraps one over-long line in PROPAGATION.md" — HU4, as found.
- The intent record: the option Mike picked read "describe a problem by its type, never name the
  reporting repo or its contents"; the applied clause matches it. The record already lists, as
  needing his word, RU1's second counsel (`blockscan`'s subsection map, or accepting `320/340`'s
  residual) and **RU9's other option, retitling section `320`** — which is HU6's subject. HU6
  stands as the open half of RU9, and the ask to him should name that earlier note so he rules
  with it in front of him (AR8).
- The prior verdict: RU8 counted 40 items in `320` (87 now); RU10's counsel named "the grammar,
  the tri-state and the rebuild" and never numbering, so **HU5 is the applier's word, not the
  prior pass's**. RU2 recorded two closed PRs carrying a private child's name in head ref and
  title; the live read in act 1 found every open and recently merged hand-up compliant, which is
  consistent with RU1's own note that post-ruling filers had read the section.
- The 2026-11-08 record names `160/300` among the items applied and says nothing more about this
  delta; no framing met there or in the session index.
- The brief-writer's disclosed exposure matches what the sibling holds; its two re-run lines
  reproduce (stamp identical; hook and CI exit 0 at HEAD).

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 4 minor · 3 note (HU1–HU8).**
HU7 (minor) and HU8 (note) were formed at reconcile; HU1–HU6 stand as written. No MAJOR, so under
`REVIEW.md` § *Applying decisions to doctrine* the cycle closes here: what remains is decided into
the backlog, and the application does not spawn another full ceremony. Every finding is the
principal's to decide (rule 3); nothing was applied. Counsel is beneath each finding, labelled.

- [ ] HU7 — step 1: "the incident, told as its class (rule 2)".
- [ ] HU8 — the floor clause reaches another private repo's contents too.
- [ ] HU4 — no action owed: the pointer is path-scoped and already covers `6bea4d10`.
- [ ] HU6 — put to him beside the intent record's note on RU9's retitle option.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

*Released to the reviewer only after its act-1 findings were committed (`e10058e3`, local; it
landed on `main` as `33ed4cbd` after the rebase onto newer commits, and the reconcile and log above
and below cite the pre-rebase hash verbatim); folded here verbatim (headings demoted two levels)
and the sibling file removed, per the brief. The orchestrator (headless Opus 5.5 session
`9ec596e5`, started by drain session `21a271a5`, itself Opus 5.5) held the partition, formed no
finding and wrote no severity. The weekly usage limit cut the reviewer off during act 1; it was
resumed in the same session after the reset, on the principal's resume order.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-report-up-privacy-clause-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

#### The queue pointer's questions (author-written, verbatim)

> whether the clause closes RU1's leak path on every surface a hand-up creates; whether the stamped
copy and its canonical region still agree.

#### The brief-writer's own questions

1. § *The route* step 1 (unchanged) still says the item carries "the incident". The floor bullet now
says class only. Do they agree, and which one does a child in a hurry obey?
2. List every surface a hand-up creates that the clause does not name: the item's file name and
slug, the commit *body*, a PR comment, CI logs, a co-author line, the peer-channel message.
3. `CLAUDE.md` cites "§ *The route*, rule 2". Does that reach the rule, not only the file (V5)?
4. A "private" repo is the trigger. Who decides, and what of a repo about to go public or a public
repo reporting about a private sibling?
5. The landing commit and the pointer commit are separate (`94df4aad`, then `6bea4d10`). Check
against rule 4's landing-equals-queuing.
6. "Reds a stale copy": run the claim. Does `stampscan` red it, or warn?

#### What the brief-writer ran, and what it got

- `stamp`: exit 0; one stamped block verified identical to its canonical region.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*The reviewer's work log, kept outside the worktree while the pass ran and read by no other session
until act 2 was saved; appended here verbatim at the fold (headings demoted two levels, form only)
and the working file deleted.*

### Review log — atelier 160/1050, report-up privacy clause cold pass

Reviewer: Fable 5.1 (claude-fable-5-1). Spawned by orchestrator session 9ec596e5 (Opus 5.5), itself
started by drain session 21a271a5 (Opus 5.5). Worktree: /Users/mike/worktrees/fable/atelier-160-1050-2217/atelier
Started 2026-11-15 UTC (local 2026-11-16 11:20 NZDT). Commands, files and evidence only.

#### Steps

1. `git merge-base --is-ancestor 94df4aad HEAD` -> exit 0. HEAD = f24bbaf9. uptime load 4.53.
2. Read brief docs/reviews/2026-11-09-0126-report-up-privacy-clause-cold.md lines 1-206 in full.
   Barred list noted: ROADMAP-DONE.md, SESSIONS.md, docs/sessions/, prior verdicts in docs/reviews/,
   the queue pointer 160/1050, the sibling .deferred.md, delta commit message bodies, intent record
   160/300 beyond its first line.
3. Read docs/method/REVIEW.md lines 25-561 (rules 1-4, four lenses, re-run rule, V1-V7, lifecycle,
   method-trail ruling 2026-11-15).
4. `python3 tools/coldsweep.py --root . --commit 94df4aad --path docs/method/PROPAGATION.md --path
   docs/build/templates/CLAUDE.md --path CLAUDE.md --path CHANGELOG.md` -> subject, stat, diff only;
   4 files, +49/-14; body not printed; no board file touched; no barred file touched.
5. `git log --oneline 94df4aad..HEAD -- <4 delta paths>` -> 290 commits since; of note 3312cdbd
   (160/300 RU2-RU6, RU12 applied, same intent record), 9c8cb7e7 (320/330), e76250cf, 38536e4c,
   6b6110c9 (tools: warn on private names in branch names and commit titles), 49f3d407 (leakscan
   --messages), 55f23034 (commit-message plane).
6. `coldsweep --commit 3312cdbd` scoped to delta paths -> read body-free; it edits § The duty, § The
   route step 1 (RU6 block), § Report without harming the parent (parent's half, RU2-RU4, RU12),
   CLAUDE.md read-order step 6, CHANGELOG. It does not touch the floor region or the template.
7. Read at HEAD: docs/method/PROPAGATION.md 115-229 (floor region) and 475-864 (§ Pointing up whole);
   CLAUDE.md 36-66 (read order step 6, § Hard constraints).
8. Read at HEAD: docs/build/templates/CLAUDE.md 85-105 (stamped bullet); CHANGELOG.md 1437-1458
   (the delta's entry; `diff` against 94df4aad's lines 8-29 -> IDENTICAL); docs/method/PROPAGATION.md
   225-374 (stamp mechanics, § The bundled-mode variant); docs/roadmap/README.md whole (74 lines);
   docs/roadmap/320-*/README.md 1-25; newest 320 item (860) lines 1-12; RECORD.md 497-544
   (§ The record is public); tools/README.md § namescan (1998-2030); tools/blockscan_map.json 48-66.
9. `ls docs/roadmap/320*/ | grep -c .md` -> 87 items (RU8 "many more than nine" holds).
   `ls docs/roadmap/320*/ | grep ^340` -> 340-blockscans-map-cannot-see-a-subsection.md exists.
10. Line widths: `git show 94df4aad:<file> | awk 'length>100'` -> PROPAGATION.md line 529 = 102 cols
    (the RU8 sentence); CLAUDE.md 86 = 202 (pre-existing allow-marked identity line); CHANGELOG many
    pre-existing. HEAD: PROPAGATION.md none. `git log -S'<the 102-col text>'` -> rewrapped by
    6bea4d10 "board: land 160/300's privacy clause; queue its cold pass as 160/1050" (the commit
    after 94df4aad). coldsweep --commit 6bea4d10 scoped to delta paths -> only PROPAGATION.md,
    +4/-4, the rewrap; 3 board files left out by default (index, 1050 pointer, 300 record).
    wrapscan on the 94df4aad copy (scratchpad) -> clean (limit 85, "materially over"); so no floor
    break, a house-width slip only.
11. coldsweep sweeps (barred set + both board items excluded): 'class only|names itself|repo token|
    hosts, clients' -> hits only in CHANGELOG, CLAUDE.md:72-73, templates/CLAUDE.md:100-101,
    PROPAGATION.md:198-199, 654, 739, 793, 836, 845. 'Doctrine problems point up' -> template:90,
    PROPAGATION:188, blockscan_map.json:55 (anchor unchanged by the delta), CHANGELOG. -i 'hand-up|
    pointing up|...' -> no copy of the route in skills/; REPO-BOUNDARY.md 88-133 cites § Pointing up
    only; docs/ROADMAP.md index lines 636 and 679 carry a child repo token in a title / file name
    (items 280 and 710, both pre-clause).
12. Live reads (read-only `gh`): `gh run list --commit <full sha>` -> 94df4aad: no run (pushed with
    6bea4d10); 6bea4d10: floor success 2026-11-08T11:31Z. `gh pr list --state open --json
    number,title,headRefName,createdAt` -> 2 open hand-ups (#135, #136), both head refs of the form
    report-<subject>-<HHMM> with no repo token; #135 title says "a hand-up from a private child";
    #136 title carries an item number (020/470) and no hand-up word.
13. `nice -n 10 python3 tools/stampscan.py --root . .` -> clean, 1 stamped block verified,
    docs/build/templates/CLAUDE.md:18 [identical] matches canonical region 'floor' (105 lines); exit 0.
14. `nice -n 10 python3 tools/floor.py --plane hook --root .` (load 3.5 before) -> every enforced
    check ✅; warn-only: harvestscan, pointerscan, pathscan, indexscan, sweepscan. attribscan read 0
    files on this plane (nothing staged), stated by the tool.
15. `nice -n 10 python3 tools/floor.py --plane ci --root .` -> exit 0; secretscan 28 and leakscan 3
    advisory (non-blocking by design); namescan, quotescan warn-only; declarations 🟡 (21 checks, 0
    meet all five). Output kept at scratchpad/floor-ci.txt.
16. `grep -n -i floor tools/pins.py` -> the floor-copy report (160/340) lives in pins.py, reference =
    floor text at the child's pin; report-only until 2026-12-09 (confirms PROPAGATION 270-279).
    `gh pr view <135|136> --json body` grepped for 'hand-up|private child' -> 1 hit each (counts
    only). `git log --merges --oneline -12` -> subjects read "land hand-up #n", no child named.
    `gh repo view mike548141/<repo> --json visibility` for the two repos whose tokens sit in index
    lines 636/679 (items 320/280, 320/710) -> both PUBLIC, so allowed by the rule.
    `grep -n 'NNN|next free|allocate' docs/roadmap/README.md` -> line 4 only (file-name shape; no
    allocation rule).
17. Act 1 appended below the `---` divider (brief lines 207-449) at ~22:29Z. Findings: HU1 MODERATE
    (floor's surface list closed; commit body omitted), HU2 minor (changelog names stampscan; the
    mechanism is pins.py, report-only until 2026-12-09), HU3 minor (CLAUDE.md sentence binds an
    actor not its reader), HU4 minor (two commits; 102-col line rewrapped by 6bea4d10), HU5 note
    (README holds no numbering rule), HU6 note (section 320 named child-filed). Sound: A1, A2, A5,
    A6; stamped copy identical; RU8-RU10 present at HEAD; cross-refs reach their rules.
18. INTERRUPTED by the weekly usage limit at ~22:30Z after step 17, before the Status line and the
    brief scanners. RESUMED 2026-11-15T23:54Z in the same session on the principal's resume order.
    Verified on disk: brief 449 lines with act 1 intact; log through step 14; scratchpad at94/ and
    floor-ci.txt survive. Edited the Status line and added an interruption note to the provenance.
    No finding or severity formed or changed after the resume. Sibling not sought or opened.
19. Brief scanners from the worktree on the brief: datescan ✓, spellscan ✓ (file skipped by
    .spellscanignore, scanned nothing — stated), wrapscan ✓ (same, .wrapscanignore), linkscan ✓ (0
    internal links; the sibling link is a bare path, not a link, so no expected hit), leakscan ✓,
    reviewscan ✓ (1 brief keeps deferred material out). Reflowed my act-1 lines to ≤100 characters
    (`awk length` counts bytes; measured in characters with python3). Status line updated.
20. Final width pass: all act-1 lines ≤100 characters; leakscan and datescan rerun clean. ACT 1 SAVED 2026-11-15T23:56Z.

#### Act 2 (reconcile), 2026-11-16 UTC

21. Orchestrator reported act 1 committed as e10058e3 (brief only, +256/-2). `git log -1` confirms;
    `git status` shows only the deleted sibling. Read the held sibling at
    ~/.claude/fable-held/atelier--2026-11-09-0126-report-up-privacy-clause-cold.deferred.md whole
    (the pointer's two questions; six brief-writer questions; its runs: stampscan identical, floor
    hook/ci exit 0 at c132cc1c, pathscan 3 warn-only).
22. Read the barred records: `git log -1 --format=%B` for 94df4aad and 6bea4d10 (message bodies);
    the queue pointer 160/1050 whole (delta "scoped to paths", no SHA named); the intent record
    160/300 whole (72 lines: Mike's 2026-11-08 answer "Add privacy line now" and the option text;
    APPLIED 2026-11-08; 2026-11-09 "Approve all 13"); prior verdict
    docs/reviews/2026-09-25-0715-report-up-duty-cold.md lines 350-392 (RU1, RU2), 479-510
    (RU8-RU11), 546-556 (counsel), 581-592 and 630-640 (reconcile), 679-680 (overall);
    docs/SESSIONS.md index lines 335-340; docs/sessions/2026-11-08-1059-ruling-round-722a.md
    (grep: 160/300 at line 14 only; 160/1050 at 58, 67).
23. `grep stampscan .github/workflows/ci.yml` -> runs as `--warn` (advisory, atelier-only, line 199);
    stampscan is not in the floor registry's plane tables (the hook/ci summaries of steps 14-15
    list no stampscan). Answers sibling Q6: it warns in atelier and cannot run in a child.
24. Appended `### Reconcile (act 2, 2026-11-16 UTC)` beneath the act-1 verdict. Formed at reconcile:
    HU7 minor (§ The route step 1 "carrying the incident" vs the class-only floor; prompted by the
    brief-writer's Q1) and HU8 note (a public child naming a private sibling's contents is reached
    only by RECORD.md's join rule, not the floor clause; prompted by Q4). HU4's owed action reduces to
    none: the pointer is path-scoped and names no SHA. HU1 is a gap in RU1's own counsel carried
    faithfully; HU5 is the applier's word (RU10 never said numbering); HU6 is the open half of RU9,
    already noted in the intent record as needing his word. Overall restated: PASS-WITH-FINDINGS
    0 MAJOR · 1 MODERATE · 4 minor · 3 note. Status line updated to RAN. Act-1 text unrevised.
25. Scanners on the brief after act 2 (datescan, spellscan, wrapscan, linkscan, leakscan, reviewscan)
    rerun from the worktree; all act-2 lines ≤100 characters. Sibling not modified, not deleted.
ACT 2 logged 2026-11-16T00:00Z

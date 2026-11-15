# Cold pass — `namescan`, no private name in a branch name or commit title

**Board:** `docs/roadmap/160-doctrine-review-owed/1410-rule-4-cold-pass-queued-namescan.md`
**Status:** RUN. Act 1 (the verdict below the divider) written 2026-11-15 UTC by a Fable 5.1 cold
reviewer, spawned by a headless orchestrator under drain session `21a271a5`; act 2 (reconcile
against the sibling and the barred records) written the same day; sibling folded below the
verdict. Overall FAIL, 14 findings (2 MAJOR). Brief written 2026-11-14 UTC by a headless
Opus 5.5 brief-writer (`cclive` lists it as session `51ccf0f9`).

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium. The scanner's share of one landing commit is about 530 added
lines (255 the tool, 158 its tests, 23 the floor registry entry, 29 floor tests, 14 a hook test, 36
the README section, 11 the changelog entry), plus a 3-line test hunk from a later commit and the
scanner's entry in a later floor-wide declarations commit. The shared message reader it calls
(`tools/commitmsg.py`, 149 lines) is read as a dependency.
**Why it earns a review:** it is guard code registered in the floor for every child repo, and on
2027-05-03 it starts to block commits by itself, with no edit, in every repo that declares itself
public. Its subject is a one-way harm: a branch name or a commit title is published the moment it
is pushed and cannot be retracted. The worst failure is a **false clear**: a green run read as
"titles and branches are safe" while the route the harm actually took (a ref named at push time, a
pull-request title, a CI runner with no term list) is never read, so sessions stop checking by hand.
The second is **a leak through the check itself**: a scanner whose input is the private term list
printing a term, or part of one, into a log that a public repo's CI publishes.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `51ccf0f9`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `51ccf0f9` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; **the queue pointer whole**; **the intent
  records `160/360` and `320/810` whole**, including the author's landing notes on both; **the
  landing commit's message body** (`6b6110c9`, printed by a `git show --stat` before `coldsweep`
  was used) and the later commit `b74cd5ef`'s body (printed by a `git show` of its test hunk); the
  delta's non-tool hunks through `tools/coldsweep.py --commit`; `tools/namescan.py`,
  `tools/test_namescan.py`, `tools/commitmsg.py`, `.githooks/commit-msg` and `.atelier-floor.json`
  at HEAD; the helpers `allowmarker.present`, `leakscan.scan_lines` and `pdlistscan.declared_public`
  in part; `docs/method/PROPAGATION.md` § *The route* rule 2 and one bullet of § *Report without
  harming the parent*; commit subjects through `git log`; the sibling brief
  `2026-11-14-0210-attribscan-unquoted-attribution-cold.md`, its `.deferred.md`, its item and that
  brief-writer's session record (read for house form). It opened **no prior verdict**. Its harness
  also loaded user-level and repo instruction files and a memory index, which hold private context
  this brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words that commissioned the build, 2026-11-09, quoted on `320/810` (asked which of
six candidate checks to build): *"all six, warnings at first and then move to blocking action. With
a staggered turn on of each so they dont all hit at once"*. One of the six is this one, "private
names in branch names and commit titles". Those words fix three things only: the check is built, it
warns first, and it then blocks on a turn-on date staggered from the other five. **The date itself,
2027-05-03, is the run's choice, not his**, and the delta says so.

The finding the check answers is `NP2` of an earlier doctrine cold pass, summarised on its board
item as: *the precedence is prose-only on all four published surfaces — no hook or scanner reads a
branch name, commit subject or PR title*. The precedence is `docs/method/PROPAGATION.md` § *The
route* rule 2, which says, in part:

> **This rule governs every surface the filing creates, not just the item's prose, and it outranks
> any rule about how to name one** … **Branch names, PR titles, commit subjects and PR bodies are
> all published the moment the filing is pushed** … it was found because a public pull-request
> list already carried a private child's name in a head ref and a title, and **that cannot be
> retracted**.

Judge the work against that harm: a private repo's name, host or client reaching a public repo's
head refs, titles or pull-request list. Whether the build reads the surfaces the harm took, and at
the moment it can still be prevented, is yours to attack. No ruling of his fixes the design beyond
the words above.

## What the work is

One landing commit on `main`, and two later commits that touch the scanner. First confirm your tree
has them:

```
for c in 6b6110c9 b74cd5ef ba55be27; do git merge-base --is-ancestor $c HEAD || echo "MISSING $c"; done
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read each commit body-free:

```
python3 tools/coldsweep.py --root . --commit 6b6110c9 \
  --path tools/namescan.py --path tools/test_namescan.py --path tools/floor.py \
  --path tools/test_floor.py --path tools/test_precommit.py --path tools/README.md \
  --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit b74cd5ef --path tools/test_namescan.py
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`: `6b6110c9` also adds `tools/commitmsg.py` and its tests and edits
two board items, and `b74cd5ef` adds a different scanner. For `ba55be27`, read only the `namescan`
entry's `declares=` block in `tools/floor.py` at HEAD (it states the scanner's rule, grounding,
purpose gap, window and posture as reported-only declarations).

Review `tools/namescan.py` and `tools/test_namescan.py` at HEAD too, and read what it calls as far
as namescan depends on it: `tools/commitmsg.py` (`read_message`, `clean`, `subject`, `branch`,
`commits`, `pushed_range`), `leakscan.scan_lines`, `leakscan.resolve_terms_path`,
`leakscan.load_local_terms`, `allowmarker.present`, `pdlistscan.declared_public`, `report.safe_text`
and `report.guarded_main`, and `.githooks/commit-msg`. On 2026-11-14 UTC no commit after
`b74cd5ef` had touched either namescan file or `tools/commitmsg.py`. Confirm what has landed since:

```
git log --oneline b74cd5ef..HEAD -- tools/namescan.py tools/test_namescan.py tools/commitmsg.py .githooks/commit-msg
```

## What the delta claims (extracted, not evaluated)

- **What it reads:** on the message plane, this commit's title (the first non-blank line after
  comment lines and a verbose scissors section are removed) and the current branch name; on the CI
  plane, every title in the pushed range and the pushed ref name. Message bodies are not read
  (`leakscan --messages` is named as the sweep for those).
- **What counts as a private name:** exactly what leakscan treats as one, through leakscan's own
  term sources (`--terms`, `$ATELIER_LEAKSCAN_TERMS`, `~/.claude/leakscan-terms.txt`) and engine,
  structural shapes included, keeping only findings whose response is `block`. No new list is made.
- **It never prints a term:** a finding names the rule and a redacted excerpt, cut to 60 characters
  and passed through `report.safe_text`.
- **Scope:** only a repo whose `.atelier-floor.json` declares `"visibility": "public"`; a private
  repo naming itself and its clients in its own titles is out of scope.
- **The date cannot be moved:** `NAME_WARN_UNTIL` is compared with the UTC clock, and no flag,
  environment variable or config key moves it. Before it a message-plane finding exits 0; on and
  after it, exit 1 unless `--warn`. The CI plane only reports, at any date.
- **Exempt only with a reason:** a line `namescan:allow: <reason>` in the message body; a bare
  marker exempts nothing, and **a subject cannot exempt itself**. A leakscan allow marker in the
  title does not exempt (`honour_markers=False`).
- **A broken scan is not a pass:** `--require-terms` with no list, a set-but-broken term path and
  an unreadable range each exit 2. The message-plane template carries
  `--require-terms`; the CI template does not.
- **Measured and probed at landing:** 0 of 2,285 titles and 0 of 41 refs in atelier; a fleet probe
  by exit code, date patched, 21 of 21 exit 0 on the landing date (2026-11-10) and on the flip
  date, atelier the only repo in scope. "Tests: 14".
- **The registry tells the truth:** no hook template (it runs one hook later, from `commit-msg`),
  `--warn` on CI only, an advisory form a child may declare, and the advisory-count line printed on
  every run, zero included.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine. The lenses organise it; they do not bound it. Anything not named a
non-goal is in scope.

**Non-goals:** the commit-message plane itself (`.githooks/commit-msg`, `floor.py --plane msg`,
`tools/commitmsg.py` as a design), which is `160/1390`'s own pass; `quotescan` and
`leakscan --messages`, which are `160/1420`'s; the other four checks of `320/810`; and the
floor-wide declarations work of `ba55be27` beyond the namescan entry. Each is read here only as far
as namescan depends on it. A defect in a shared helper that changes namescan's result is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **NA1.** Reading the title and branch **at commit time** prevents the harm. Probe the routes
     by which a private name reaches a public repo's refs or titles without passing a commit-msg
     hook that can see it: a ref named only at push (`git push origin HEAD:<name>`), a commit on a
     detached HEAD, a branch renamed after its commits, a clone that never installed the hook, a
     `--no-verify` commit, a merge or rebase that writes titles, a pull-request title.
   - **NA2.** The CI plane is meaningful cover. A hosted runner has no local term list, and the CI
     template omits `--require-terms`. Establish what the CI run can and cannot see there, and
     whether its green line says so.
   - **NA3.** leakscan's term sources and engine are the right definition of "a private name" for
     titles and refs: block-response findings only, structural shapes included, the term list's own
     matching (word boundaries, case, separators such as `-`, `_` and `/` in ref names).
   - **NA4.** The check cannot leak what it guards (the item's first question): no term, nor a
     slice of one long enough to identify it, reaches stdout, stderr, `--json`, the unparseable-
     marker note, an error message, or a public CI log.
   - **NA5.** Scope by declaration is correct (the item's second question): a private repo's own
     name in its own history is rightly out of scope, and nothing is lost when a repo is public on
     the forge but has not declared it, or declares it wrongly.
   - **NA6.** The exemption is narrow: a reasoned body marker is the only way out, a subject cannot
     exempt itself, and one marker exempts no more than the author meant.
   - **NA7.** The date flips cleanly and alone, and every repo in scope is safe on the day.
   Ask too whether a commit-time scanner is the right altitude for a push-time, forge-side harm,
   against the next rung `PROPAGATION.md` names ("a branch-name and title lint at the reporter's
   push, or a `handupscan` run at merge").
2. **Correctness & quality.** Diff each commit; drive the tool on both planes against scratch repos
   you build, with a synthetic term list of your own, and with the date patched across the flip.
   Record each overclaim against the text that makes it: the module docstring, the help text, the
   README section, the floor entry's comment, `why` and `declares=` block, and the `CHANGELOG.md`
   entry. Check the tests would fail on a broken change: mutate a scratch copy, never the worktree.
3. **Completeness / harvest.** Every surface that states the same fact (V3): does any doctrine or
   README text still say no lint reads branch names or titles, or describe namescan's cover more
   widely than it is? One home (V4); no contradiction between docstring, README, floor comment and
   code (V5). Compare with its siblings' conventions (allow-marker grammar, advisory-count line,
   broken-scan exits, warn-first date constants) and with `pdlistscan`, which shares its scope key.
4. **Security & privacy** — mandatory. Its input is the most sensitive list on the machine. Check
   NA4 by probe on every output channel. Check terminal-control and bidi sanitising on every printed
   field (excerpt, `where`, the note, the branch name). Check option injection through `--range`
   (a spec beginning with `-` is handed to `git log`), and what a hostile message file, branch name
   or huge title does to the regexes and the run. Check the `GITHUB_*` environment reads on the CI
   plane. Check against OWASP ASVS input-handling, output-encoding and logging items, checked, not
   recalled. `/security-review` reads the session's pending diff, not this delta: aim it only at a
   scratch clone holding the delta as pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root unless it says otherwise, in the foreground, under a load average near 5 on 12 cores; its
results are held in the sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 and git
is 2.50.1 on this machine.

- `cd tools && python3 -m unittest test_namescan; echo $?`
- `cd tools && python3 -m unittest test_commitmsg; echo $?`
- `cd tools && python3 -m unittest test_floor.MsgPlaneTest; echo $?`
- `cd tools && python3 -m unittest test_precommit.CommitMsgHookTest; echo $?`
- `python3 tools/namescan.py --selftest; echo $?`
- `python3 tools/namescan.py --range pushed --root . --warn; echo $?`
- `python3 tools/namescan.py --range HEAD --root . --warn | head -2` (every title in history: the
  landing's "0 of 2,285 titles" claim, re-measured)
- `python3 tools/namescan.py --range nosuch..HEAD --root . --warn; echo $?`
- `python3 tools/floor.py --plane msg --list --root . | grep namescan`
- The changelog's fleet claim: a probe by exit code over every local child checkout, on your run
  date and with the date patched to 2027-05-03. Read-only; report counts only.

Use `cd tools && python3 -m unittest test_<name>`, never the dotted `tools.test_<name>` form, which
raises `ModuleNotFoundError` here. Run the tool from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** read-only. The runs over this repo's history, a read of this repo's open and
closed pull-request titles and head refs (`gh pr list --state all --json number,title,headRefName`),
and the fleet probe over local child checkouts are reads, and all are in scope. Any probe that
would write to a real repo or forge (staging, committing, pushing a ref, opening a PR, installing a
hook, editing a board) is **NOT RUN**: build the case in your scratchpad (scratch repos, a synthetic
term list, a scratch copy of the tool with the date patched) and say which probes you could not
build.

- **The machine's term list is private.** Run the tool with it where a probe needs real coverage,
  but never open, print, quote or count-by-term it, and never write a term anywhere. Probes of NA4
  use a synthetic list you write in your scratchpad. If a real run's output shows anything that
  looks like a term, stop, record the finding by shape only, and do not paste the output.
- Never print a secret, and quote no line from a child repo. This repo is PUBLIC: report child
  results by count only, and name no child, host, client or private path.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos and fixtures when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/` (the earlier pass that raised `NP2` included), the queue pointer above,
this brief's sibling
`docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.deferred.md` (since
folded below the verdict and the file removed), the three
delta commits' message bodies, and the two intent records whole:
`docs/roadmap/160-doctrine-review-owed/360-rule-4-cold-pass-queued-the-naming-precedence.md` and
`docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`.
Both carry the author's landing account under the finding and the proposal, and reading is atomic,
so neither can be read in part. What you need from them is quoted in *The acceptance test* above.

The delta's own text carries the author's account of why (the docstring, the README section and
the floor entry's comment above all); it is the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1410-rule-4-cold-pass-queued-namescan.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/360-rule-4-cold-pass-queued-the-naming-precedence.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions NA1–NA7 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (`6b6110c9`,
`b74cd5ef`, `ba55be27`: read body-free yes/no, findings by id), findings with stable IDs (prefix
`NS`: `NS1`, `NS2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `namescan` is self-authored guard code that will block commits in every
public child on its date, so it is doctrine by function (rule 3): **the author applies nothing on
its own**. Record all findings; they are the principal's to decide, after a plain-language account.
Counsel per finding is welcome, labelled as counsel and kept beneath it, and a finding that bears
on whether the 2027-05-03 flip should happen as built says so in its first line.

---

## Verdict — act 1

**Overall: FAIL** — 2 MAJOR · 4 MODERATE · 4 minor · 2 note (12 findings, `NS1`–`NS12`). The
check is honest at runtime and its tests, selftest and measurements all reproduce, but two
load-bearing assumptions are false: the engine as wired cannot see a private name in the shapes a
ref name actually takes (`NS1`), and the surfaces the originating harm took on the forge are read
either nowhere or only where the term list is absent, and the delta's own text does not say so
(`NS2`). Both bear on the 2027-05-03 flip, each in its first line.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection, in a fresh session
  started for this pass alone. Run on 2026-11-15 UTC from the review worktree
  `/Users/mike/worktrees/fable/atelier-160-1410-1926/atelier` at `4a219254` (the board claim),
  which carries `6b6110c9`, `b74cd5ef` and `ba55be27` (`merge-base --is-ancestor` printed
  nothing). Nothing after `b74cd5ef` touched `tools/namescan.py`, `tools/test_namescan.py`,
  `tools/commitmsg.py` or `.githooks/commit-msg`.
- **Spawn:** by a headless orchestrator session (Opus 5.5) that drain session `21a271a5`
  (Opus 5.5) started. Both are rule-4 off-tier orchestrators disclosed here: they hold the context
  partition, form no finding and write no severity; the orchestrator committed the claim and
  commits this act. Neither wrote the brief or any of the delta. Not started or instructed by the
  barred sessions `51ccf0f9`, `58027096` or `d0ca5d24` (nor anything `d0ca5d24` started). Run under
  the principal's weekly Fable drain order of 2026-11-15 17:53 UTC.
- **Read:** this brief whole; `docs/method/REVIEW.md` §§ *What a review actually checks*,
  *Re-run*, *The standing checklist*; `tools/namescan.py`, `tools/test_namescan.py`,
  `tools/commitmsg.py`, `.githooks/commit-msg` at HEAD; `tools/floor.py` (the `namescan`,
  `quotescan`, `sweepscan`, `pdlistscan` and `leakscan` entries, `MSG_CHECKS`, `FORBIDDEN_FLAGS`,
  `_render`, `commit_msg_hook_note`, the TA4 comment); `leakscan.scan_lines`, `redact`,
  `derived_form_regex`, `load_local_terms`, `resolve_terms_path`; `allowmarker.marker_rx`,
  `present`, `_note_unparseable`; `pdlistscan.declared_public`; `report.safe_text`,
  `guarded_main`, `advisory_count_line`, `quiet_selftest`; the three commits body-free through
  `coldsweep --commit … --path …`; `tools/README.md` and `CHANGELOG.md` through those diffs and
  grep; `.github/workflows/*.yml` by grep (`fetch-depth`, `floor.py`); `docs/method/PROPAGATION.md`
  § *The route* rule 2 and the bullet at lines 786–802, § *Enforcement propagates too* in part;
  `docs/method/GUARDS.md` by grep only; this repo's pull-request list (`gh pr list --state all
  --json number,title,headRefName`, 136 rows); OWASP ASVS 5.0 chapters V1, V2 and V16, fetched,
  not recalled. One `coldsweep` tree sweep with the brief's four excludes (the sibling exclude
  matched no file: it is removed from this worktree on purpose).
- **Not opened:** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, every prior verdict
  in `docs/reviews/`, the queue pointer, items `160/360`, `320/810` and `260/050`, the three commit
  bodies, the `.deferred.md` sibling. No `--include-barred`. The machine's term list was loaded by
  the tool for two real-cover measurements (`NS11`) and never opened, printed, quoted or counted.
- **Exposure, disclosed:** the pull-request listing put 136 public titles and head refs of this
  repo into the reviewer's context; none is repeated here. Fleet results below are counts only.
  The harness loaded user-level instruction files and a memory index that hold private context;
  nothing from them is used or carried here.
- **Interpreter:** the re-run lines were run with `python3` on `PATH` (3.14.6), as the brief did;
  `/usr/bin/python3` (3.9.6) was used only for `coldsweep` and the gate tools. git 2.50.1.
  Every suite ran under `nice -n 10`, one at a time, foreground, with `uptime` read first (load
  5.9–18.2 on 12 cores while other passes ran).

### Lens 1 — approach and assumptions

The load-bearing assumptions, named and probed. Every probe ran in a scratch repo under the
scratchpad with a synthetic three-term list (one plain word, one plain two-word term, one `forms:`
term), against a scratch copy of `tools/`; the worktree's `tools/` was never mutated, and every
scratch artefact was deleted afterwards.

- **NA1 — reading the title and branch at commit time prevents the harm.** DAMAGED (`NS2`). With
  the real `.githooks/commit-msg` installed in the scratch repo: a plain commit with a listed term
  in its title warns and lands (hook ran); `--no-verify` is silent; a `git rebase` replaying a
  title and a `git cherry-pick` replaying a title run no `commit-msg` hook (both confirmed, exit 0,
  no scanner line), while `git merge --no-ff -m` does run it; `git branch -m <name>` after the
  commits, `git branch <name> HEAD` after a detached-HEAD commit, and `git push <remote>
  HEAD:<name>` each publish a ref name that no local plane ever reads; a detached-HEAD commit
  scans the subject only (clean line, branch empty, as the docstring says). On the CI plane the
  pushed ref name is read from `GITHUB_HEAD_REF` / `GITHUB_REF_NAME` and, given a term list, a
  listed term in it is found; without a list (a hosted runner) the same ref is invisible. A
  pull-request title is read by neither plane: with a synthetic `GITHUB_EVENT_PATH` whose
  `pull_request.title` carried a term, the run printed a clean line. Across the 21 local child
  checkouts, 13 carry an executable `commit-msg` hook and 8 do not, including 1 of the 3 that
  declare themselves public: in that clone the message plane never runs.
- **NA2 — the CI plane is meaningful cover.** DAMAGED for terms, CONFIRMED for shapes (`NS3`).
  With `HOME` pointed at an empty directory and no `--terms`, a title carrying a listed term
  printed `✓ namescan clean — … (no local term list found — scanned STRUCTURAL patterns only. …)`,
  exit 0, and the `--json` `cover` field says the same. So the green line is honest at runtime.
  The README section, module docstring, changelog entry and floor comment say CI "reads the pushed
  range and only reports" and never that CI holds no list, so a reader of those takes the CI plane
  as cover for names; it is cover for hostnames, addresses and the other structural shapes only.
  Both workflows check out with `fetch-depth: 0`, so `pushed_range` resolves the event's `before`
  or a pull request's base in CI; on a shallow clone it falls to `HEAD^..HEAD` with a note, which
  the head line prints.
- **NA3 — leakscan's engine is the right definition of a private name for refs and titles.**
  DAMAGED (`NS1`). A plain term compiles to `\b<term>(?:s)?\b`, and `\b` treats `_`, letters and
  digits as word characters. Probed on branch names with the synthetic plain term:
  `report-<term>-1`, `report/<term>/x` and the upper-cased term are found; `fix_<term>_thing`,
  `fix<Term>Thing` and `<term>2` are missed. A plain two-word term can never match a ref name
  (refs carry no spaces):
  `report-<word>-<word>-1` and `<word>_<word>` both missed, and the same two-word term in a title
  is found spaced and missed hyphenated or underscored. Only a `forms:` term matches the slug,
  snake and camel spellings (`derived_form_regex`), and `forms:` is opt-in, held opt-in by
  leakscan for a reason that belongs to prose (compound-word false positives), not to ref names.
  Plurals and possessives in titles are caught; a term with a combining-mark spelling is matched
  through NFC as leakscan does.
- **NA4 — the check cannot leak what it guards.** CONFIRMED for findings, DAMAGED for one note
  (`NS8`). A finding's `excerpt` is `term:<2 chars>…` for a listed term and leakscan's `redact`
  for a structural shape (`10.….3 (8 chars)` shape); `where` is a literal or a 12-hex commit id;
  `rule` is a rule name; `--json` carries the same three fields; a title and a branch name carrying
  ESC, CSI and a bidi override produced no raw control character in any output; the branch name
  itself is never printed, only its redacted excerpt. The error paths print a term-list *path* or a
  floor-file path, never a term. The one channel that echoes message text is `allowmarker`'s
  "present but unparseable" note: `namescan:allow:(<term>-fixture)` and `namescan:allow::<term>`
  each printed the glued tail, term included, to stderr.
- **NA5 — scope by declaration is correct.** DAMAGED (`NS6`). Of 21 local child checkouts with an
  `.atelier-floor.json`, 3 declare `"visibility": "public"`; `gh repo view --json visibility`
  (read-only) says 5 are public on the forge, so **2 public repos are outside the check's scope**
  and get `✓ namescan clean — not declared public: out of scope.` A declaration of `"Public"`
  (capitalised) is read as not public, the same comparison `pdlistscan.declared_public` makes. A
  malformed floor file exits 2 with the shared `cannot read` line, no traceback. A private repo's
  own name in its own titles is rightly out of scope, as the docstring says.
- **NA6 — the exemption is narrow.** DAMAGED (`NS4`). `scan_message` tests
  `allowmarker.present(ALLOW_RX, message)` over the **whole** message before reading the subject,
  so a subject `tools: <term> fix namescan:allow: because` exempts itself (0 findings), against the
  docstring, README, changelog and the brief's extracted claim that "a subject cannot exempt
  itself". The separator is `SEP_ANY_SPACE` (`\s*`), which spans newlines, so a bare
  `namescan:allow:` at the end of the subject followed by a body paragraph takes the body's first
  word as its reason and exempts (0 findings). A marker inside an inline code span is a mention;
  a leakscan marker in the body or the title exempts nothing; one body marker exempts the subject
  and the branch together, which is the author's stated intent.
- **NA7 — the date flips cleanly and alone.** CONFIRMED. With `_utc_today` patched: 2027-05-02
  exits 0 with `advisory: 1 finding(s)`; 2027-05-03 and 2027-05-04 exit 1 with `commit blocked`
  and `advisory: 0`; `--warn` holds exit 0 on the flip; `--json` reports `clean: false,
  blocking: true, until: 2027-05-03`; moving the constant one day turns the suite red (`MUT4`),
  so the date is pinned by test. The range plane exits 0 after the date with or without `--warn`.
  On the day: 4 repos are in scope (this one and 3 children); over this repo's 2,336 titles and
  the children's 13,321, 0 findings on the run date and with the date patched to 2027-05-03.
  `--require-terms` on the message template means a public-declared repo on a machine with no
  term list exits 2 and blocks from the landing date, not from the flip; that matches leakscan's
  hook template and is a convention, not a defect (`NS12`).
- **Altitude.** A commit-time hook is the right *first* rung: it is the only moment the term list
  and the chance to prevent coincide. It is not the altitude of the harm, which is forge-side.
  The routes in NA1 that bypass it are closed by a pre-push hook reading the ref names being
  pushed with the same local list, and a pull-request title read in CI (structural shapes only,
  as CI must be). `PROPAGATION.md` names that rung and says it is not built; the delta neither
  points the reader there nor says what it leaves to it (`NS10`).

### Lens 2 — correctness and quality

Each commit diffed body-free; the tool driven on both planes against scratch repos across the
flip; tests mutated on a scratch copy. Overclaims recorded against the text that makes them:

- *"a subject cannot exempt itself"* — module docstring (EXEMPTION paragraph), README section,
  changelog entry: false (`NS4`).
- *"no private name in a branch name or commit title"* — README heading, floor `why`, help text:
  stronger than the engine's reach on ref names (`NS1`) and silent on pull-request titles and on
  push-time ref names (`NS2`).
- *"CI reads the pushed range and only reports"* — README, docstring, changelog, floor comment:
  true, and silent on CI's structural-only cover (`NS3`).
- *"A finding names the rule and a redacted excerpt, never the term"* — docstring, README: true of
  findings; the unparseable-marker note is not a finding and can carry the term (`NS8`).
- *"Fleet probe … 21 of 21 exit 0 … atelier is the only repo in scope"* — changelog: the exit codes
  reproduce; the scope claim is stale (3 children declare public at HEAD) and 2 more are public
  undeclared (`NS6`, `NS11`).
- *"Tests: 14"* — reproduces, and two of the fourteen cannot fail on the surface they name
  (`NS5`).

A 2 MB title scanned in 0.28 s and a title of 200,000 address-shaped tokens in 2.3 s with the
printed list capped at 40, so the regexes do not blow up on a hostile line. Mutation `MUT3`
(a reordering with identical semantics) kept the suite green, so the suite is not merely brittle.

### Lens 3 — completeness and harvest

- Mirror sites (V3): `PROPAGATION.md` lines 797–799 still read "A branch-name and title lint at
  the reporter's push, or a `handupscan` run at merge, is the next rung (`GUARDS.md`); it is not
  built". A commit-time lint is built and the sentence does not point at it, and `GUARDS.md` holds
  no text about that rung (`NS10`). `CHANGELOG.md:650` says the same as history; left as history.
- One home (V4): `NAME_WARN_UNTIL` is the date's home; the README heading and body, the changelog
  and one test carry copies at the point of use, the shape `pdlistscan` uses for 2027-03-08.
  Discharged. The scope key is one function, `pdlistscan.declared_public`, shared. Discharged.
- Siblings: marker grammar matches `quotescan` and `attribscan` (`SEP_ANY_SPACE`, unnamed
  reason); the advisory-count line, the broken-scan exits and the warn-first constant follow the
  house shapes; `MSG_CHECKS` and the `test_floor` registry test were extended for it. The `ci`
  template omits `--require-terms` as leakscan's does, by the same design.
- Not harvested: `commitmsg.commits` hard-codes `#` when cleaning history, so a historical title
  that begins with `#` is dropped and the body's first line is scanned as the subject (`NS9`).

### Lens 4 — security and privacy (V6)

Input is the most sensitive list on the machine; threats enumerated and checked against ASVS 5.0:
- **Argument injection (ASVS 1.2.5, 1.3.3).** `--range=--output=<path>` is handed to `git log`
  as an option and **wrote a file** in the scratch repo (exit 0, clean line); `--range=--all`
  widens the read to every ref. argparse refuses the space-separated spelling, and
  `FORBIDDEN_FLAGS` refuses `--range` and `--message-file` from a child's `flags`, so the surface
  is the command line only (`NS7`). `pushed_range` validates the event's SHA by regex before
  building the spec; a `GITHUB_HEAD_REF` carrying control characters reached no raw output.
- **Log injection and control characters (16.4.1).** `safe_text` on every excerpt; `where` and
  `rule` are internal; `broken` strips controls from error text. Confirmed by probe.
- **Sensitive data in output (16.2.5).** Findings redact; the unparseable-marker note does not
  (`NS8`). Where that note lands: on the message plane, the author's terminal; on the CI plane, a
  log, but the text it echoes is a commit message already pushed to a public repo. No term reaches
  a public log by the check's own hand in either; the finding is the broken claim and the channel.
- **Error messages (16.5.1).** Error text names the term-list path or the floor-file path, never a
  term. An unexpected exception prints a traceback and exits 2, which is the RT4 design.
- **`/security-review`:** discharged with grounds. It reads the session's pending diff, not a path;
  this worktree is not clean while the review runs (the deliberately removed sibling and this
  file), and several passes are live on this machine, so the batch-shape caution in `REVIEW.md`
  applies. Aimed at a scratch clone it would see the delta as landed code, which its exclusions
  cover thinly. Not run.

### Standing checklist V1–V7

- **V1** no claim stronger than its evidence: breached (`NS2`, `NS3`, `NS4`, `NS11`).
- **V2** re-run every live-proven claim: all ten lines re-run (ledger below); each reproduces.
- **V3** changed rule swept to every mirror: breached at `PROPAGATION.md:797–799` (`NS10`).
- **V4** one fact, one home: discharged (lens 3).
- **V5** no internal contradiction: breached between the EXEMPTION docstring and
  `scan_message` (`NS4`); the cross-reference `PROPAGATION.md:798 → GUARDS.md` reaches a file
  that does not hold the rung (`NS10`). The floor's `declares.rule` is `Unmet("… no passage of a
  rule")` while `PROPAGATION.md` § *The route* rule 2 is that passage (`NS10`). The docstring's
  `260/050` reference was not opened; its claim (the visibility key) is confirmed by
  `declared_public`.
- **V6** security and privacy on every review: run (lens 4); `/security-review` discharged.
- **V7** provenance stated: above.

### Findings

- **NS1 — MAJOR.** *Bears on the flip: a gate blind to slugged ref names should not turn
  blocking as built.* The engine as wired cannot see a listed name in the shapes a ref name takes:
  `_`, digit-glued and camel-case spellings of a one-word term are missed (`\b` treats `_` and
  digits as word characters), and a plain multi-word term can match no ref name at all, nor a
  hyphenated or underscored title. Only `forms:` terms reach those spellings, and `forms:` is
  opt-in for a prose reason that does not apply to refs. The headline surface gets a false clear
  in its most common shape. *Counsel:* on the ref surface (and arguably the title surface) compile
  every literal through `derived_form_regex`, or at least treat `_`, digits and case changes as
  boundaries; keep `forms:` opt-in for file text. Test the `_` case.
- **NS2 — MAJOR.** *Bears on the flip: the green it prints after the flip must not be read as
  cover for the forge.* The harm the brief says to judge by is a private name in a public repo's
  head refs, titles or pull-request list. The build reads the branch name and commit title at
  commit time only; a pull-request title is read nowhere; a ref named at push, renamed after its
  commits, or created after a detached-HEAD commit passes no plane that holds the list; rebase
  and cherry-pick replays run no `commit-msg` hook; 8 of 21 local clones (1 of 3 public-declared)
  have no `commit-msg` hook. None of this is stated in the docstring, README, changelog or floor
  comment, whose heading is "no private name in a branch name or commit title". The build matches
  the principal's commissioning words; the gap is against the harm, and it is undisclosed.
  *Counsel:* state the unread surfaces where the claim is made; read `pull_request.title` from the
  event on the CI plane (structural shapes, like the rest of CI); queue the pre-push rung with
  the local list for ref names.
- **NS3 — MODERATE.** The CI plane holds no term list by design, so its cover is structural
  shapes only; the runtime line and `--json` say so, the README section, docstring, changelog and
  floor comment do not, and "CI reads the pushed range and only reports" reads as cover for
  names. *Counsel:* one sentence at each of the four sites.
- **NS4 — MODERATE.** "A subject cannot exempt itself" is false: the exemption is tested over the
  whole message, so a reasoned marker in the title exempts the title; and because the separator
  spans newlines, a bare `namescan:allow:` ending the subject takes the body's first word as its
  reason. Neither shape is tested. *Counsel:* test the marker against `message` with the subject
  line removed, and against the body only with `SEP_SAME_LINE`; add both cases to the tests and
  the selftest.
- **NS5 — MODERATE.** Two tests cannot fail on the surface they name:
  `test_a_term_in_the_branch_warns` asserts `"branch" in out`, and the clean line reads "no
  private name in a branch or title"; `test_range_reports_and_never_blocks` asserts `"private
  name" in out`, and the clean line contains "private name". With the branch scan removed, and
  separately with the range scan reading no commits, both stayed green (`MUT1`, `MUT2`). The
  branch surface, the item's headline, has no failing test. *Counsel:* assert the finding line
  (`branch: [local-term]`) and the advisory count.
- **NS6 — MODERATE.** Scope by declaration loses repos: 2 of 21 local children are public on the
  forge and not declared, and the check prints a clean "out of scope" line in each; a capitalised
  `"Public"` is out of scope the same way. The changelog's "atelier is the only repo in scope" is
  stale at HEAD (3 children declare public). The comparison is `pdlistscan`'s and shared, so the
  defect is the floor's scope key, surfaced here. *Counsel:* a one-read reconciliation of the
  declaration against `gh repo view --json visibility`, warn-first, in `floor.py` or
  `floorfleet`; case-fold the value.
- **NS7 — minor.** `--range=<spec>` beginning with `-` is passed to `git log` as an option:
  `--output=<file>` wrote a file, `--all` widened the read. Command line only (`FORBIDDEN_FLAGS`
  and argparse bound it). Shared `commitmsg.commits`, so `quotescan` inherits it. *Counsel:*
  `git log --end-of-options <spec>` or refuse a spec with a leading `-`.
- **NS8 — minor.** The unparseable-marker note echoes up to 40 glued characters after
  `namescan:allow`, a listed term included, to stderr. On the message plane that is the author's
  terminal; on CI it is text already public. The claim "never the term" is true of findings and
  not of this channel. Shared `allowmarker` (110/010). *Counsel:* cut the note's head at the first
  separator after the marker word.
- **NS9 — minor.** On the range plane `commits()` cleans history with a hard-coded `#`, so a title
  beginning with `#` is dropped and the body's first line is scanned as the subject; a term in
  such a title was missed. `commitmsg` is `160/1390`'s design; the effect on namescan's result is
  this pass's. *Counsel:* clean only the message-file plane; history is already cleaned by git.
- **NS10 — minor.** `PROPAGATION.md:797–799` still says the branch-name and title lint "is not
  built" and cites `GUARDS.md`, which holds no such text; the floor's `declares.rule` says no rule
  passage exists while § *The route* rule 2 is one. *Counsel:* point the sentence at namescan and
  name what it leaves to the next rung; cite rule 2 in `declares`.
- **NS11 — note.** Measurements re-run with the real list, counts only: 0 of 2,336 titles in this
  repo (was 0 of 2,285); 0 of 8 refs in the shared ref store (was 0 of 41, before branch
  clean-up); 0 of 136 pull-request titles and 0 of 136 head refs; fleet 21 of 21 exit 0 on both
  dates, 0 findings. The ref figures are hand measurements over `for-each-ref`, not a surface the
  scanner reads: it reads one branch name per run. The fleet figure proves scope more than titles:
  18 of 21 are out of scope and exit 0 before reading anything.
- **NS12 — note.** `--require-terms` on the message template blocks from the landing date on any
  machine without a term list in a public-declared repo, before the flip; this is leakscan's hook
  convention and is right, stated so the flip-day reading is not that blocking began that day.

### Per-commit ledger

| commit | read body-free | findings |
| --- | --- | --- |
| `6b6110c9` | yes (`coldsweep --commit`, 7 paths) | NS1–NS9, NS11, NS12 |
| `b74cd5ef` | yes (`coldsweep --commit`, 1 path) | none; the 3-line hunk is sound |
| `ba55be27` | `declares=` block at HEAD only, as directed | none; its `Unmet` rule is NS10's |

### Re-run ledger (2026-11-15 UTC, worktree root, `python3 tools/…` with 3.14.6, `nice -n 10`)

| line | result |
| --- | --- |
| `cd tools && python3 -m unittest test_namescan` | 14 tests OK, exit 0 |
| `cd tools && python3 -m unittest test_commitmsg` | 12 tests OK, exit 0 |
| `cd tools && python3 -m unittest test_floor.MsgPlaneTest` | 10 tests OK, exit 0 |
| `cd tools && python3 -m unittest test_precommit.CommitMsgHookTest` | 7 tests OK, exit 0 |
| `namescan.py --selftest` | `selftest OK — namescan`, exit 0 |
| `namescan.py --range pushed --root . --warn` | clean, note "no pushed range known", exit 0 |
| `namescan.py --range HEAD --root . --warn \| head -2` | clean, advisory 0; 2,336 titles |
| `namescan.py --range nosuch..HEAD --root . --warn` | `git log … failed`, exit 2 |
| `floor.py --plane msg --list --root . \| grep namescan` | `enforced fleet decl 0/5` |
| fleet probe by exit code, run date and 2027-05-03 | 21/21 and 21/21 exit 0, counts only |

Probes NOT RUN because they would write to a real repo or forge: a real push of a privately
named ref, a real pull request, installing the hook in a real clone. Each was built in a scratch
repo with a scratch bare remote instead (lens 1, NA1).

### Follow-up checklist (the principal's to decide; rule 3, the author applies nothing)

- [ ] `NS1` ref-surface matching (slug, `_`, digit, case) — before the flip, or hold the flip.
- [ ] `NS2` state the unread surfaces; read the pull-request title in CI; queue the pre-push rung.
- [ ] `NS3` four sentences: CI holds no list, structural shapes only.
- [ ] `NS4` subject self-exemption and the newline-spanning separator; two tests.
- [ ] `NS5` make the branch and range tests able to fail.
- [ ] `NS6` reconcile declared visibility with the forge; on 2026-11-15 UTC two undeclared
      public repos sit outside every declaration-scoped check.
- [ ] `NS7` `--end-of-options` in `commitmsg.commits`.
- [ ] `NS8` cut the unparseable-marker note's head.
- [ ] `NS9` do not clean history with `#`.
- [ ] `NS10` PROPAGATION.md rung sentence; `declares.rule`.
- [ ] Act 2: reconcile against the sibling and the barred records.

### Reconcile

Act 2, 2026-11-15 UTC, after act 1 was committed unrevised as `6b4bbedd`. Opened: the held
sibling (one file, read in place, not copied); the queue pointer `160/1410`; `160/360` and
`320/810` whole; the three commit bodies (`git log -1 --format=%b`); the prior verdict
`2026-09-25-0715-naming-precedence-cold.md` at its `NP2` paragraph only. Nothing else barred was
opened. Act-1 text above is untouched.

**The sibling.** It is a floor and says so; it records no probe past the re-run lines, which
match mine (its 2,325 titles on 2026-11-14 became my 2,336). Its twelve questions, each against
the act-1 probe that answers it:

- Q1 push-time refs → `NS2`: no surface holding the list reads a ref named at push; CI reads the
  name without the list. Its note that this estate's own worktree sessions push from a detached
  HEAD sharpens `NS2`'s weight: the message plane reads no branch at all on that path.
- Q2 CI with no list → `NS3`: the stdout cover note and `--json` say so; the floor's `--list`
  line, the README, docstring, changelog and floor comment do not.
- Q3 PR titles and the stale sentence → `NS2` and `NS10`: nothing reads a pull-request title;
  `PROPAGATION.md:797–799` is stale for the commit-time rung and still true for the push-time
  one, and its `GUARDS.md` citation reaches nothing.
- Q4 self-exemption → `NS4`, confirmed in both shapes it asks about; one body marker does exempt
  the branch as well, which the author's EXEMPTION paragraph intends and which stands as design.
- Q5 separators → `NS1`: `-` and `/` bound; `_`, digits and case changes do not; multi-word terms
  never match a ref.
- Q6 leak through the check → NA4 confirmed for findings and `--json` (the excerpt is two
  characters of the term, or leakscan's `redact` of a structural span); the `allowmarker` note is
  `NS8`.
- Q7 option injection → `NS7`, confirmed as a write (`--output`), bounded to the command line by
  `FORBIDDEN_FLAGS` and argparse; a one-line hardening, recorded as minor.
- Q8 comment-char stripping on CI → `NS9`, confirmed: a `#`-led title escapes the range plane.
- Q9 scope key → `NS6`: nothing checks the declaration against the forge; 2 of 21 local children
  are public there and undeclared.
- Q10 malformed floor config → confirmed: `pdlistscan.ConfigError` is a `RuntimeError`,
  `guarded_main` turns it into the shared `cannot read` line and exit 2, with the path and the
  JSON error the user can clear. That the hook then blocks is read from `.githooks/commit-msg`
  (`|| status=1`), not probed.
- Q11 the clean head's wording → **`NS13`, note, formed at reconcile.** `render` says "on the
  pushed range" for every `--range` spec: my own re-run of `--range HEAD` over the whole history
  printed "no private name in a branch or title on the pushed range" for 2,336 titles that were
  never a pushed range. The sibling asked; act 1 printed the evidence and did not read it. One
  word: say "the range" unless the spec was `pushed`.
- Q12 test gaps → `NS5` covers the two that cannot fail; **`NS14`, note, formed at reconcile:**
  no test covers a structural shape in a title, the `GITHUB_HEAD_REF` / `GITHUB_REF_NAME` read
  on the CI plane, `--json`, or the stderr channel. Each was probed in act 1 and behaved; none
  is pinned.

**The author's account.** Three things it adds, none of which moves a severity:

- `160/360`'s landing note records that "the counsel's pre-push shape was not built: the
  commit-msg hook reads the branch at commit time, so a branch renamed afterwards is seen only by
  CI's pushed-range report". So the rung gap in `NS2` was known and disclosed on the board item,
  not on the delta's own surfaces, and the pull-request title is named nowhere in the account.
  The disclosure's second half is `NS3`'s overclaim in another home: CI's pushed-range report
  holds no term list, so it does not see a renamed branch's private *name*. `320/810` repeats it
  ("until then their CI report is the only cover"). `NS2` stays MAJOR: a board note the principal
  does not read, which itself overstates the fallback, does not stand in for the claim sites.
- The prior pass's `NP2` counsel was precisely the pre-push rung on the machine that holds the
  list, "failing that, state … that the four surfaces are unwatched". The build took neither
  branch of that counsel in its own text. `NS2`'s counsel restates `NP2`'s, which is to say the
  class has recurred once in doctrine and once in code.
- The changelog's "atelier the only repo in scope" and the body's "21 of 21 exit 0" were true at
  the landing commit (`320/810`: "atelier in scope, the other 20 out", 2026-11-10); 3 children
  declare public at HEAD. `NS6`'s stale-claim clause is a change since landing, not an error at
  it; the 2 undeclared public repos are the finding. `320/810` also says each flip "needs a fresh
  fleet probe before its date", which is where `NS1`'s "before the flip" belongs.
- `ba55be27`'s body explains the `Unmet` rule declaration: "a citation that does not resolve
  would be worse than Unmet, so every stated one is pinned to resolve". `NS10`'s counsel is
  therefore a *resolving* citation of `PROPAGATION.md` § *The route* rule 2, not a loosening.
- The brief's acceptance test holds as written: the principal's words fix "built, warns first,
  blocks on a staggered date", and the delta meets all three. Every finding here is against the
  harm the brief says to judge by and against the delta's own claims, not against his words.

**Overall, restated: FAIL** — 2 MAJOR (`NS1`, `NS2`) · 4 MODERATE (`NS3`–`NS6`) · 4 minor
(`NS7`–`NS10`) · 4 note (`NS11`–`NS14`; `NS13` and `NS14` formed at reconcile). The fold of the
sibling below this line is the orchestrator's.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Held out of the review worktree by the orchestrator until the reviewer's act-1 findings
were committed (`6b4bbedd`), then released to the reviewer for act 2; folded here verbatim
(headings demoted two levels) and the sibling file removed, per the brief. Act 1 was
committed locally as `52a3b0c4` and landed on `main` as `6b4bbedd` after a rebase, content
unchanged; the orchestrator corrected that one hash in the reconcile's first line (form only).
The orchestrator, a headless Claude Opus 5.5 session started by drain session `21a271a5`,
formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.md`
(`REVIEW.md` rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session
`51ccf0f9`), which authored none of the delta. Open this only after act 1 is committed. Everything
here is a floor, never a fence, and none of it is a finding: the brief-writer read the code once
and probed none of these past what is recorded below.

#### What the barred intent records say, in brief

- `160/360` carries, under the earlier pass's summary, the author's landing note for this check:
  `NP2` built 2026-11-10 as `tools/namescan.py`, and **the counsel's pre-push shape was not
  built**: the commit-msg hook reads the branch at commit time, so a branch renamed afterwards is
  seen only by CI's pushed-range report. The same item carries a 2026-11-09 note that `NP5` is
  still the principal's.
- `320/810` records the slice-5 landing with the same measurement and fleet probe the changelog
  states, "Tests: 14 … plus `tools/test_commitmsg.py` (12)", that the date is the run's choice
  (four weeks after the three already set, in the order built), and that existing clones need
  `tools/commit-msg.sample` installed for the message-plane checks to run, with `floorfleet` not
  yet checking for that hook.
- The landing commit's body says the failure "had recurred in head refs", and gives the same
  measurement and probe.

#### The brief-writer's own questions

1. **Push-time refs.** The harm in the doctrine was a head ref and a title in a public PR list. A
   ref named only at push (`git push origin HEAD:<name>`, the form this estate's own worktree
   sessions use from a detached HEAD) never passes a commit-msg hook that can see it, and
   `commitmsg.branch` returns empty on a detached HEAD, so the message plane reads no branch at
   all there. Which surface, if any, reads such a ref before it is public?
2. **CI with no term list.** The CI template has no `--require-terms`, and a hosted runner has no
   `~/.claude/leakscan-terms.txt`. So on CI the check reads structural shapes only, which do not
   include a repo or client name. The cover note says so on stdout; does anything a reader of the
   board or the floor list sees say so? Is CI's "clean" for the pushed ref name meaningful?
3. **PR titles and bodies.** `NP2` and `PROPAGATION.md` rule 2 name PR titles; nothing here reads
   one. `PROPAGATION.md` § *Report without harming the parent* still says a branch-name and title
   lint "is not built". Stale now, or still true for the push-time rung? Either way, V3.
4. **A subject cannot exempt itself.** `scan_message` calls `allowmarker.present` on the whole
   message, subject included. Does a title of the form `x: <name> namescan:allow: y` exempt itself?
   And does one body marker also exempt the branch name, which the author may not have looked at?
5. **Ref-name separators.** Branch names use `-`, `_` and `/` where a term list holds words. Does a
   term bound by `\b` still match `report-<name>-1`? (The test says yes for `-`.) What of
   `report_<name>`, `<name>/x`, a camel-cased or squashed form?
6. **Leak through the check.** The excerpt is leakscan's redacted excerpt cut to 60 characters.
   Is that excerpt redaction of the term, or of the span around it? What does `--json` carry, and
   the stderr note `allowmarker` prints for an unparseable marker ("the head of the marker, up to
   forty glued characters")? A public repo's CI log is public.
7. **Option injection.** `--range` is passed straight to `git log` after the format argument. A
   spec beginning with `-` (for example `--output=<path>`) is read as an option. Only a local user
   or a template sets it, so is this a finding or a one-line hardening?
8. **Comment-char stripping on CI.** `commits()` cleans each pushed message with `#` as the comment
   character, so a title starting with `#` is dropped and the next non-blank line read as the
   subject. Does a title like `#123: <name>` escape the CI report?
9. **Scope key.** A repo public on the forge but not declaring `"visibility": "public"` is silently
   out of scope (`not declared public: out of scope.`, exit 0). Is the declaration checked against
   the forge anywhere?
10. **Malformed floor config.** `pdlistscan.declared_public` raises its own `ConfigError`, a
    `RuntimeError` subclass, so `guarded_main` turns it into exit 2. Confirm, and confirm the
    message-plane hook then blocks the commit (fail-closed) for a reason the user can clear.
11. **The clean head on a whole-history run** says "on the pushed range" for any `--range`, not only
    `pushed`.
12. **Tests.** No test covers a structural shape in a title, the CI plane's `GITHUB_HEAD_REF` /
    `GITHUB_REF_NAME` read, `--json`, or the NA4 property on stderr. The 14 tests count matches
    HEAD.

#### What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC unless stated, foreground, load average 4 to 6 on 12
cores, at `origin/main` `461fdf92`, on a detached HEAD.

- `merge-base --is-ancestor` on `6b6110c9`, `b74cd5ef` and `ba55be27`: all ancestors.
- `cd tools && python3 -m unittest test_namescan`: 14 tests, OK, about 3 s.
- `cd tools && python3 -m unittest test_commitmsg`: 12 tests, OK, exit 0.
- `cd tools && python3 -m unittest test_floor.MsgPlaneTest`: 10 tests, OK, exit 0.
- `cd tools && python3 -m unittest test_precommit.CommitMsgHookTest`: 7 tests, OK, exit 0.
- `python3 tools/namescan.py --selftest`: `selftest OK — namescan`, exit 0.
- `python3 tools/namescan.py --range pushed --root . --warn`: exit 0, clean, with the note "no
  pushed range known: reading HEAD only"; advisory count 0.
- `python3 tools/namescan.py --range HEAD --root . --warn`: clean over 2,325 commits (the landing
  measured 2,285), with this machine's term list present; about 0.5 s.
- `python3 tools/namescan.py --range nosuch..HEAD --root . --warn`: exit 2, git's own error text.
- `python3 tools/floor.py --plane msg --list --root .`: `namescan enforced fleet decl 0/5`.
- The `coldsweep --commit 6b6110c9` line in the brief, with the five non-tool paths: exit 0, no body
  printed, the two board-store files left out by default.
- `git status --short` after the test runs: empty.
- **Not run:** the fleet probe over child checkouts, a read of the forge's PR titles and head refs,
  and any probe of the questions above. All are left whole to the pass.

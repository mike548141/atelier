# Cold pass — `namescan`, no private name in a branch name or commit title

**Board:** `docs/roadmap/160-doctrine-review-owed/1410-rule-4-cold-pass-queued-namescan.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `51ccf0f9`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
`docs/reviews/2026-11-14-0239-namescan-private-names-branches-titles-cold.deferred.md`, the three
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

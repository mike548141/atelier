# Cold pass — a loose end makes the close "not ready until you decide", a refused call is an ask and never routed around, and ccclose's scratch-folder check and refused-delete re-route flag

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is
doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-22 UTC: PASS-WITH-FINDINGS, 1 MAJOR · 1 MODERATE · 5 minor ·
1 note, by a Fable 5.1 reviewer under off-tier orchestrator `7dbb6565` (drain session `eca14b23`,
the principal's drain order of 2026-11-23 NZDT). Act 2 (reconcile against the sibling) pending its
release. Brief written 2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/996-rule-4-cold-pass-queued-close-loose-ends-and-routed-refusals.md`.
**Size of this pass:** medium: about 100 lines of code and 45 of doctrine in one commit, with four
instruments' docs.
**Why it earns a review:** This is standing close and autonomy doctrine every session reads, and the
instrument that checks it. The worst failure is a close that reads as verified when it is not, or an
instrument that names a session for a workaround it did not make.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Opus worker it dispatched, which wrote the text and code (per the queue
  pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d4a0fcf3` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `d4a0fcf3` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and the author session named above with everything
  it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  item numbers, the rules of the run, and the statement that it built none of these subjects. It
  carried no framing of the work. The brief-writer had no contact with the author session or its
  workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the board
  item whole; the intent records' opening part and every line naming the principal or a landing
  account; the design note hunks in the delta, every delta commit body-free through
  `tools/coldsweep.py --commit`; commit subjects through `git log`;
  `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole, **including that pass's
  verdict and folded sibling** (a different subject, read for house form), the acceptance-test
  section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words, printed by the span command below (one quoted sentence in `180/170`). The
rule they sit under is `docs/method/RECORD.md`'s invariant on the all-clear, and the harness's rule
that a denied call means adjust. `180/180`'s quoted sentence is a session's words, and is that
session's report, not the principal's.

Print only the quoted spans, before phase 1:

```
python3 -c 'import re, sys
for p in sys.argv[1:]:
    t = " ".join(l.strip() for l in open(p, encoding="utf-8"))
    for m in re.findall(r"\*\"(.+?)\"\*", t): print("-", m)' \
  docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md
```

## What the work is

- **`1569e64`** — `close: a loose end is an ask, a refusal is never routed around (180/170,
  180/180)`.

Delta paths, read at each commit and at HEAD:

- `docs/method/RECORD.md`, `docs/method/AUTONOMY.md`, `docs/method/CONCURRENCY.md`,
  `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/man/ccclose.1`,
  `instruments/ccclose.design.md`, `instruments/README.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 1569e64 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path docs/method/RECORD.md --path \
  docs/method/AUTONOMY.md --path docs/method/CONCURRENCY.md --path instruments/ccclose --path \
  instruments/ccclose.test.js --path instruments/man/ccclose.1 --path instruments/ccclose.design.md \
  --path instruments/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 1569e64..HEAD -- docs/method/RECORD.md
docs/method/AUTONOMY.md docs/method/CONCURRENCY.md instruments/ccclose instruments/ccclose.test.js
instruments/man/ccclose.1 instruments/ccclose.design.md instruments/README.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "A loose end is something the close owes and has not put away; open work recorded on the board is
  not one."
- A refused tool call "is a standing decision about what the agent may do", and the agent "does not
  reach the effect it blocked through another tool".
- "From inside a session the agent cannot know that a rule is a mistake."
- The refused-delete flag lists a later delete only when every route it uses is unrefused; a retry
  by a refused route is not listed; the flag does not expire.
- `REFUSAL` matches the harness's wording, from a "census of the live store", and a failed command
  does not match.
- The design note's figures: across 1119 transcripts, 73 hold a refused delete and 9 are listed; on
  the grounding session the form lists the two Python deletes and not the later `rm`.
- Check 13 reads the folder the harness records in the transcript, "never derived"; a cut walk says
  "at least".
- The design note says what the flag misses: a delete in a script file, other routes, a subagent's
  own transcript, other refused effects.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the worktree-variable work (pass `160/993`); the dispatch doctrine (pass `160/995`);
ccclose checks 1 to 12 as reviewed earlier.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states this behaviour (V3); one home (V4); no
   contradiction (V5). Find tests that would stay green on a broken delta by mutating a scratch
   copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design; at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only from a
   clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
in the foreground or under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH`.

```
node --test instruments/ccclose.test.js
nice -n 10 python3 -m unittest discover -s tools
```

Any figure the delta records from a measurement over repositories or transcripts on the machine is a
recorded proof (V2): re-run it read-only and by count. The brief-writer did not re-run those.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0207-close-loose-ends-refusals-cold.deferred.md` (a held-back file; by
count: 7 questions, 1 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/180-a-denied-delete-was-worked-around-with-python.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/170-declared-ready-to-close-with-loose-ends.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/180-a-denied-delete-was-worked-around-with-python.md \
  'DELETE_ROUTES|isRefusal|REFUSAL|checkScratch|A refused call|loose end'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`LE`: `LE1`, `LE2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, written 2026-11-22 UTC

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, tier checked at
  selection. It read the delta, answered the lenses, formed every finding and set every severity.
- **How spawned:** by headless orchestrator session `7dbb6565` (Opus 5.5), itself started by drain
  session `eca14b23` (Opus 5.5) under the principal's drain order of 2026-11-23 NZDT, verbatim:
  *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT
  todat"*. Both are off-tier orchestrators holding the context partition: they formed no finding
  and wrote no severity. The orchestrator's direction was process only (paths, the barred set, the
  two files I may write, the log, the load rules, how to finish). It carried no question about the
  delta and no pointer to where the risk lives. The sibling `.deferred.md` was removed from my tree
  before I started (`git status` shows its `D`); I did not seek it anywhere.
- **Barred sessions:** `d4a0fcf3` (brief-writer), `74f2b8cd` (its coordinator) and author session
  `4c65083c` with everything it started. None started or instructed me; no contact with any of them.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-996-2234/atelier`, HEAD `7d9ba367`,
  read-only to me except this file. Delta `1569e64` is an ancestor of HEAD (exit 0).
- **What I read:** this brief whole; `docs/method/REVIEW.md` lines 8–302 and 394–608; the delta's
  eight paths body-free through `tools/coldsweep.py --commit 1569e64 --path …` (four calls, board
  files left out, message body not printed); those regions at HEAD and `git diff 1569e64 HEAD` on
  them; `COMMUNICATION.md` heading list; `CONCURRENCY.md` 1017–1024; the first line only of the two
  intent records; the acceptance-test span (one quoted sentence). No session log, no prior verdict,
  no commit body, no board item beyond its title. The tree sweep ran through `coldsweep` with the
  brief's excludes (35 hits over 748 files, 1005 excluded); `--include-barred` was not used.
- **Live reads:** read-only counts over the transcript store on this machine
  (`~/.claude/projects/*/*.jsonl`, 1617–1618 top-level transcripts, 9.9 GB); no content printed,
  only counts and masked wording templates. No live write of any kind.
- **Work log:** `~/.claude/fable-drain/notes/atelier-160-996-2234.md`, every command and read, in
  order.
- **Load:** `uptime` 14.8 at start, 30.2 at the first suite, 8.8 by the second. Suites ran under
  `nice -n 10`, one at a time, foreground.

### Lens 1 — approach and assumptions

Named before further reading (log, step 2): A1 the acceptance test is the principal's one
sentence and the right fix is doctrine plus an instrument; A2 the refused-delete flag is only as
good as `REFUSAL`'s match on live wording; A3 check 13 depends on the harness writing
`snapshot.scratchpadDirectory`; A4 the flag keys on route label, never on the target; A5 the
verdict line with a check-13 warn must not say "ready"; A6 the 1119/73/9 figures are V2 claims;
A7 the route regexes may double-label, miss or over-match; A8 some paths look untested.

**Right problem, right altitude.** The delta answers all three clauses of the principal's
sentence: a close with an open PR or files left behind may no longer say "ready" (RECORD.md
181–196), a refused call is an ask (AUTONOMY.md 169–187, CONCURRENCY.md 1292–1294), and ccclose
makes the two misses visible at close. The shape is sound: a never-fail "look" for the scratch
folder, because the remedy may be the principal's, and a listed-not-judged shape for the re-route.
What is at the wrong altitude is one design choice inside the instrument: the refusal detector is a
**closed list of wordings** with no bucket for an error on a delete it cannot classify, so any
wording outside the list fails silent (LE1). A closed list is the right tool only with a drift
guard; the delta has none, and the live store already held four wordings outside it.

- **A1 altitude — confirmed.** Doctrine and instrument map onto the three clauses (above).
- **A2 wording list — damaged.** Four live refusal wordings unmatched, all predating the census
  (LE1).
- **A3 environment record — confirmed.** 894 of 1617 transcripts record `scratchpadDirectory`;
  911 hold an environment attachment.
- **A4 route-only key — confirmed as a limit.** Code 884–887 compares labels only (LE5).
- **A5 verdict wording — confirmed sound.** ccclose 2904–2905: a warn gives "no check fails; some
  need a look", never "ready".
- **A6 figures — re-run.** 1618 / 89 / 12 on 2026-11-22; the dated 1119 / 73 / 9 reproduce in
  method and are superseded by growth.
- **A7 regexes — damaged.** `/bin/rm` and a trailing `xargs rm` missed; Node `fs.unlink(`
  double-labelled (LE3, LE4).
- **A8 untested paths — damaged.** The "at least" cut path has no test; mutation M1 stays green
  (LE6).

### Lens 2 — correctness and quality: the claims re-driven

- "A loose end is something the close owes …; open work recorded on the board is not one." Holds;
  the wording at HEAD is unchanged and agrees with the all-clear invariant above it.
- A refused call "is a standing decision" and the agent "does not reach the effect it blocked
  through another tool". Holds as a rule; its enumeration of who refuses is narrower than the live
  store (LE2).
- "From inside a session the agent cannot know that a rule is a mistake." Holds; the grounding
  (a parallel session asked, the rule was fixed at source) is the right reading.
- The flag lists a later delete only when every route is unrefused; a retry is not listed; the
  flag does not expire. Holds, by code (884–889) and by the tests (t4, t5, the parallel case).
- `REFUSAL` matches the harness's wording "from a census of the live store"; a failed command does
  not match. **Half holds:** every match in the store carries `is_error` (233 of 233) and "Exit
  code N" never matches; but the census missed four wordings present on 2026-11-03 (LE1).
- The design note's figures. Re-run by count: 1618 transcripts, 89 with a refused delete, 12 with
  a listing (18 hits). Consistent with 1119 / 73 / 9 grown with the store; not contradicted. The
  grounding-session figures (two Python deletes, not the later `rm`) need that session's id, which
  is in a barred record: **NOT RUN in act 1**, for act 2.
- Check 13 reads the recorded folder, "never derived"; a cut walk says "at least". Holds by code
  (835–838, 1475–1503); the "at least" branch is untested (LE6).
- The design note says what the flag misses. Holds for what it lists; it does not list the same
  tool reached by path (`/bin/rm`), which the deny-rule case makes the likeliest re-route (LE3).

### Lens 3 — completeness and harvest

- **V3 mirrors:** README, ccclose header, design note, man page, CHANGELOG all carry the new check
  and the flag; the check count was swept (no "twelve/thirteen checks" left outside records). Skills
  and templates do not restate the close wording (one skill mentions scratch in another sense).
- **V4 one home:** the route list and the refusal wordings are written out in four places (code,
  design note 171–192, man page, CHANGELOG) with no stamp (note N1).
- **V5 contradiction:** none between RECORD, AUTONOMY, CONCURRENCY and ccclose's verdict line.
  The design note's reason for warn-not-fail contradicts the doctrine's own account of the scratch
  folder (LE7).
- **Mutation:** M2 (flag when any route is fresh) and M3 (drop the compound-approval wording) go
  red as expected (one test each); M1 (drop "at least") stays green, 8 of 8 (LE6). Run on a
  scratch copy of `instruments/` with `--test-name-pattern` selecting the delta's eight tests.

### Lens 4 — security and privacy (V6)

Design altitude: check 13 lists up to `CAP` file names from a path the transcript supplies, to the
session's own terminal; read-only, symlinks not followed (`Dirent.isDirectory()` is false for a
link), walk bounded at 10000. The refusal regex runs over untrusted tool output but is
start-anchored with lazy spans, so cost is linear in leading whitespace times length: no
catastrophic case. Nothing is written, nothing leaves the machine. Over-collection: none; the
check reads a folder the session already owns. `/security-review` **not run**: it reads the
session's pending diff, which here is this brief and the removed sibling; the code-altitude read
was done by hand against the ASVS classes that apply to a local read-only CLI (input handling,
resource bounds, information disclosure): nothing found. A clean pass over markdown would weigh
nothing anyway.

### Standing checklist V1–V7

- **V1** no claim past evidence: breached by the "census of the live store" claim (LE1) and by
  "a file left there harms nothing" (LE7).
- **V2** re-run: both suites green (ledger below); census re-run by count (above); the
  grounding-session figures NOT RUN (barred record) and the scratch-folder figures (50, 98) are the
  intent record's, NOT RUN until act 2.
- **V3** swept: yes (above).
- **V4** one home: unstamped copies (N1).
- **V5** contradiction: LE7; every cross-reference reaches the rule it names (`COMMUNICATION.md`
  § *Asking for a ruling* at line 214 holds the device rule; ccclose's check labels match the
  doctrine's italics).
- **V6** done by hand, grounds above.
- **V7** provenance stated in the brief and here.

### Per-commit ledger

- `1569e64` *close: a loose end is an ask, a refusal is never routed around* — read body-free: yes
  (`coldsweep --commit`, four calls, board files left out) — findings LE1–LE7, N1.

Later commits on the delta's paths (about 60, `git log --oneline 1569e64..HEAD`) were read only as
`git diff 1569e64 HEAD` on the delta's regions: they change the check count and `module.exports`
and leave the delta's code and doctrine text unchanged. Not reviewed beyond that; they are other
items' deltas.

### Findings

Every finding is the principal's to decide (rule 3): recorded, nothing applied. Counsel is
labelled and kept beneath.

**LE1 — MAJOR. The refusal detector is a closed wording list that already misses four live
refusal wordings, so a re-routed delete after any of them is invisible; the recorded "census of
the live store" was incomplete on its own date.** `instruments/ccclose` 214–220 and the design
note 171–192 claim `REFUSAL` covers "a deny rule, the auto-mode classifier, the principal's
rejection, a block for safety, and a compound command". Re-run over the store (log, steps 3–4):
of 215 error results on delete commands, 116 match; about 53 are refusals that do not, in four
shapes (masked templates, counts are results): *"Dangerous rm operation detected in `rm …`"* (31;
the harness's own `rm` guard, the nearest class to the grounding case), *"Permission for this
command was denied by a built-in Claude Code safety check, not by the user"* (20; the regex says
"action", the harness says "command"), *"This session is isolated in the worktree … too complex to
verify"* (134 in all results, 3 on deletes), and *"PreToolUse:… hook error: … call blocked"* (12,
the principal's own hooks). Dated by their own timestamps, all four existed before 2026-11-03
(worktree 142, dangerous-rm 7, safety-check 2, hook 2; earliest 2026-08-09). So about one delete
refusal in three is unseen, and a session that re-routes after one is not listed: the close reads
clean when it is not, the brief's named worst failure. Rule broken: V1/V2 (a recorded proof false
at its recording), `00-APEX` (claim past evidence).
*Counsel:* add an open bucket, not more wordings: an `is_error` result on a delete whose text is
not an `Exit code N` failure is listed as *"delete refused or blocked (unclassified)"* and treated
as a refusal for the flag; keep the named wordings for the label. Re-run the census by count in
the test suite's fixtures so the list has a drift guard. Pin the four wordings above as fixtures.

**LE2 — minor. `AUTONOMY.md` 171–172 defines a refusal as one "by a permission rule, by the
harness's classifier or by the principal"; the live store shows two more refusers the rule is
silent on: the harness's built-in safety blocks (the `rm` guard, the worktree-isolation check) and
the principal's own hooks.** The principle ("a standing decision about what the agent may do")
covers them; the enumeration reads as the definition and does not. A session meeting a hook block
can read the rule as not applying. Rule: V5 with the live harness; `DOCUMENTATION.md`'s vendor seam
says not to restate the vendor's list, so the fix is to widen the principle, not the list.
*Counsel:* "refused by anything that stands between the call and its effect: a permission rule, a
hook, the harness's own checks, or the principal".

**LE3 — MODERATE. The `rm` route misses the same tool reached by path or at the end of a
pipeline.** `deleteRoutes('/bin/rm -rf x')` → `[]` and `deleteRoutes('xargs rm')` → `[]` (log,
step 4): the lookbehind `(?<![\w./-])` rejects a `/` before `rm`, and `rm\s` needs trailing
whitespace. A deny rule on `rm` is matched by command prefix, so `/bin/rm` is the textbook
evasion of exactly the rule in the grounding case, and after a refused `rm` it is neither a
"retry" (not detected as `rm`) nor a listed re-route (no route at all). The man page's miss list
("a delete by any other tool or language") does not cover the same tool by path. Rule: V1 (the
documented reach overstates).
*Counsel:* allow an optional path prefix (`(?:\S*/)?rm`) and `rm` at end of command; add both to
the look-alike test.

**LE4 — minor. Node's `fs.unlink(` and `fs.rmdir(` are labelled both "node fs delete" and
"python pathlib delete".** The pathlib regex `(?<!\bos)\.(?:unlink|rmdir)\s*\(` matches any
`.unlink(`. Effect: after a refused pathlib delete, a Node `fs.unlink(` is read as a retry (one
label refused) and not listed; and the label misnames the route. The test covers `fs.rmSync` only.
*Counsel:* exclude `fs` and `fs.promises` in the lookbehind, or test for `\bfs` first.

**LE5 — minor. The label "refused delete re-routed" asserts a conclusion the check does not
test: it compares route labels only, never the target, so any later delete by a new route after
any refused delete is listed as a re-route.** Code 884–887. `npm rm`, `docker rm` count as `rm`;
a compound command refused for a non-delete part (`rm -f x && git push`, "parts require approval:
git push") marks `rm` refused. The check's summary ("listed, not judged; answer each") and the
design note ("A later delete is listed when every route it uses is unrefused") are honest about
the mechanism; the label is not. The brief names "an instrument that names a session for a
workaround it did not make" as a worst failure, which is why this is recorded though the harm is a
line of answer.
*Counsel:* word the label as what it saw: "delete by a route no refused delete used (refused: …)";
compare literal target paths where both commands carry one and say "same target" when they match.

**LE6 — minor. The "at least" cut-walk branch (ccclose 1484, 1500–1501) has no test.**
Mutation M1 (`const least = ''`) leaves all eight delta tests green; the design note and man page
both state the "at least" behaviour, so a stated behaviour has no check.
Rule: lens 3's mutation test; `TESTING` discipline that every stated behaviour has a check.
*Counsel:* a test with `SCRATCH_WALK` lowered through an exported setter, or a fixture of
`SCRATCH_WALK + 1` entries, asserting "at least".

**LE7 — minor. The design note (201) justifies warn-not-fail with "a file left there harms
nothing", which the doctrine itself contradicts.** `REVIEW.md` 98–103 (held-back review bytes in a
scratchpad are "one read away", SK1) and `CONCURRENCY.md` 1017–1024 ("the shared scratch is a read
surface too", the principal's answer 2026-11-09) say a scratch leftover can be a leak. The second
reason given, that the remedy may be the principal's, carries the design on its own. Rule: V1, V5.
*Counsel:* drop the first clause; keep the second.

**N1 — note (V4).** The route list and refusal wordings are copied into the design note, the man
page and the CHANGELOG with no stamp; LE1's fix moves four places. A stamp or a "see the code's
`DELETE_ROUTES`/`REFUSAL`" would hold it to one home.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR (LE1) · 1 MODERATE (LE3) · 5 minor (LE2, LE4, LE5, LE6, LE7) ·
1 note (N1).** The doctrine is right and lands where the principal's sentence pointed; the
instrument's two additions work as built and as tested; the refusal detector's closed list is the
one defect that makes a close read clean when it is not. All findings are the principal's to
decide; nothing applied.

### Re-run ledger

- `node --test instruments/ccclose.test.js` (worktree root, `nice -n 10`): exit 0; 153 pass,
  0 fail; 511 506 ms at load 30.
- `nice -n 10 python3 -m unittest discover -s tools` (worktree root): exit 0; 3382 tests, OK, in
  1595 s. A first run was killed by the harness's background time limit at about 20 minutes with
  no failure in its partial log (load 8–30, two other sessions' suites live); the second run is
  the one recorded.
- Acceptance-test span command (worktree root): exit 0; one quoted span printed.
- `git merge-base --is-ancestor 1569e64 HEAD`: exit 0.
- Census 1119 / 73 / 9 (V2), read-only over the store: 1618 / 89 / 12 (18 hits); the method
  reproduces.
- Grounding-session figures (two deletes; 50 and 98 files): NOT RUN in act 1, they sit in a barred
  record.
- `/security-review`: NOT RUN (the pending diff is this brief and the removed sibling); the
  code-altitude read was done by hand.

### Follow-up checklist (for the principal's ruling, then an applier who is not me)

- [ ] LE1: open "unclassified" bucket on delete errors; four live wordings pinned as fixtures;
      census re-run as a test, by count.
- [ ] LE2: widen AUTONOMY's definition of who refuses.
- [ ] LE3: `rm` by path and at end of command; look-alike tests.
- [ ] LE4: Node `fs.unlink`/`fs.rmdir` single-labelled.
- [ ] LE5: label says what was seen; optional same-target comparison.
- [ ] LE6: a test for the "at least" branch.
- [ ] LE7: drop "harms nothing".
- [ ] N1: one home for the route and wording lists.
- [ ] Act 2: open the sibling and the barred records; re-run the grounding-session figures.

# Top-up cold pass — paragraph projection and grace, the checks the API pass could not run

**Pass type:** top-up to a code cold pass, doctrine by function, per `docs/method/REVIEW.md`
rule 4. It covers ONLY the checks the first pass could not run, plus one verdict on whether a
top-up is enough.
**Tier:** Fable, on the principal's laptop through Claude Code, checked at selection by whoever
takes the pass. Fable work runs only with the principal's explicit permission; the dispatch
that launched this brief-writer wrongly recorded that he approved these top-ups; he asked
for the briefs and, on 2026-10-29 local date, chose to hold running them (corrected by session
f7b25adb). The taker confirms permission is on record at claim and stops if it is not.
**Status:** pass RAN 2026-11-01 UTC, act 1 written below — TOP-UP SUFFICES; overall
PASS-WITH-FINDINGS, 0 MAJOR · 2 MODERATE · 5 minor · 7 notes (PP1–PP11 plus PQ1–PQ3);
act 2 (reconcile) written 2026-11-01 UTC after the sibling's release;
sibling folded below the verdict by the orchestrator, 2026-11-01 UTC. Run on Fable 5.1 on the
laptop under the principal's 2026-11-02 drain approval, orchestrated off-tier by sessions
`f8e61647` and `c87c4ee0`.
**Original pass:** `docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.md` (the
original brief, both acts of the API verdict, and the folded sibling, in one file).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/970-rule-4-cold-pass-queued-paragraph-projection-and-grace.md`.

## Why a top-up is owed

The first pass ran on Fable 5.1 through a Claude Platform API harness, not on the laptop. Its
tools ran on this machine but sandboxed: no network, no `gh`, no keychain, no MCP connectors,
no Claude Code skills or subagents, a 300 s command limit, head-only output truncation, no
loopback bind, a global git config whose signing key was unreachable, and no repo virtualenv.
The verdict names its own limits, and its own follow-up checklist ends: *"the full suite and
`leakscan` need a run outside this sandbox before close"*. The ones that sit under a finding or
the verdict:

- the full suite was killed at the 300 s limit and never completed;
- the CI-plane floor exited 1 because `leakscan` could not read the local term list, so the
  floor at HEAD was never seen green or red for a repo reason;
- `test_board.py` ran green only with commit signing switched off by override (PP9);
- PP5 (the grace notice does not reach where a child looks) was reasoned from `floor.py`'s
  code; no real CI log could be read without `gh`;
- `/security-review` was unreachable.

The principal's ask, 2026-10-28, verbatim: *"If the API based fable review can't do the job
properly, for example because it is remote vs running on this laptop, then please tell me so
and don't send briefs that the API can't do properly. By properly I mean of a comparable
quality outcome as if we ran the fable review on this laptop as we usually do otherwise"*.
And: *"as a one off we will do the short live-only top-up covering just the missing checks,
but I would generally choose full laptop re-run to be safe. Include in each one an ask of the
cold reviewer to decide if the "top-up" is good enough or I should be doing a "full
re-run""*. And, 2026-10-29: *"I want you to write "top up briefs" for these ones that are not
as good as a reviewier on this laptop"*.

## Spawn provenance

- **Author of the delta:** session `8e498ef1` (a principal-opened Opus 5.5 queue run,
  2026-10-18) and the Opus worker it dispatched, as the original brief lists them.
- **Original brief-writer:** an Opus 5.5 subagent of session `5070f22b`, 2026-10-26.
- **Original pass:** Fable 5.1 through the API harness, orchestrated by session `f7b25adb`
  (Opus 5.5), which claimed the pass, wrote the act headers and the fold-in, and formed no
  finding.
- **Who wrote this brief:** session `29af7e91`, a headless Opus 5.5 brief-writing session
  started on the principal's instruction of 2026-10-29 (local date) to write top-up briefs.
  It authored none of the delta, the original brief or the API harness. It is **off-tier for
  review, disclosed: it forms no finding and writes no severity**, and it stops after this
  brief and its sibling.
- **Ruling on session `f7b25adb`, applying rule 4:** barred from taking, orchestrating or
  instructing this top-up. Rule 4's one criterion is that the review comes from a session the
  author neither started nor instructed. This top-up judges the API pass's limits and asks
  whether a top-up is enough; `f7b25adb` built the harness, judged those limits, and wrote the
  verdict's limits text through its orchestration. An orchestrator writes the reviewer's
  prompt and releases the sibling, which is instructing. So on this subject it is an author,
  and it fails the criterion. This agrees with an earlier brief-writer's ruling for other
  top-ups.
- **Barred from taking this pass:** session `8e498ef1` and every worker it dispatched; session
  `5070f22b` and every subagent it dispatched; session `f7b25adb` and anything it dispatched;
  session `29af7e91` (this brief-writer).
- **Who takes the review:** a further cold Fable session on the laptop that passes rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own
  provenance in its verdict.
- ⚠️ **Exposure, disclosed.** This brief-writer read the original pass file whole, including
  both API acts and the folded sibling; the two queue pointers whole; the first lines of
  `010/190`; `REVIEW.md` rule 4 and `skills/review-brief/SKILL.md` whole. It ran PQ-a, PQ-b,
  PQ-c and the count and `gh` halves of PQ-d once, reading `board`'s exit and notice per child
  and run metadata, never child content; it did not run PQ-e or PQ-d's hook fallback (results
  and gaps held in the sibling). It did not open `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other verdict or any child repo's content. Its
  harness loaded user-level and repo instruction files and a memory index, which hold private
  context this brief does not carry.

## Read first

Read the original pass file whole before you run anything: the original brief is your scope,
the API verdict is the subject of your per-finding answers, and its folded sibling is already
open material. Then read `docs/method/REVIEW.md` rule 4. The code under review is unchanged
since the API pass's HEAD: `git log --oneline 0a2b7a7..HEAD -- tools/ .githooks/ .github/`
should print nothing. If `010/190` (the grace's removal) has landed by the day you run, review
the grace at `28ef94a` from an extracted copy as the original brief says, and record what HEAD
now does. If you run on or after 2026-11-18 UTC, the live grace result is now a check you can
make and the API pass could not: make it.

## The missing checks — run only these

Each says what to run and which claim it tests. Run from your review worktree root, in the
foreground. Read exit codes explicitly. Check `uptime` before each heavy step; one heavy process
at a time, under `nice -n 10`.

- **PQ-a. `test_board.py` as given, no override.**
  `python3 -m unittest discover -s tools -p test_board.py -v`, with the machine's normal git
  config (signing on). Tests PP9's framing: on a host whose signing key is reachable, does the
  `StagedPlane` class pass as given, so that PP9 is a portability note only?
- **PQ-b. The full suite, once.** `nice -n 10 python3 -m unittest discover -s tools`, with its
  output written to a file in your scratchpad so the summary line survives; read the tail.
  Tests V2 for the suite, which the API pass could not complete.
- **PQ-c. The floor at HEAD with the real term list.** `nice -n 10 python3 tools/floor.py
  --plane ci --root .` and `python3 tools/floor.py --plane hook --root .`. Tests the API
  ledger's floor row (exit 1, `leakscan` only, for an environment reason). If a check reds,
  name the scanner and the file, and never quote a term.
- **PQ-d. The grace notice in a real CI log, read-only, by count.** Of the children the API
  pass found still on the old index form (it counted 2; count them again with `board` in check
  mode, read-only, as the original brief allows), read each one's latest `floor` workflow run
  with `gh run list` and `gh run view --log`. Report by count only: how many runs are green;
  in how many the ⚠️ grace line appears; whether it sits inside a collapsed group; whether any
  `::warning::` annotation carries it; and what the summary line says for `board`. Tests PP5
  ("the only signal that survives a green summary is the CHANGELOG") against live CI rather
  than the code. Count also, from the run list, how many of those children's recent `floor`
  runs started a job at all, and say whether the CI plane assumed in lens 1 (C) is running for
  them. If no such child exists any more, or no run of theirs carries a log, say so by count
  and test the same with a real `git commit` through the tracked hook in a scratch copy of a
  synthetic old-form board under your scratchpad, which the sandbox could not do.
- **PQ-e. `/security-review`.** From a scratch clone whose only pending change is the code
  diff of `28ef94a` (`tools/board.py`, `tools/test_board.py`; no brief, no sibling), aim
  `/security-review` at it, or discharge it in one line with grounds. Tests lens 4, which the
  API pass discharged because the command was unreachable.

Not owed, with grounds: the projection census, the legacy byte-identity comparison, the
boundary table and the mutations (local process runs the sandbox did not limit once signing
was switched off, and each is disclosed as run that way); the child counts (they reached all 11
split boards the brief-writer's laptop run found). Run any again only if a missing check above
gives you cause, and say why.

## Live access: read-only

No apply, no config change, no writes to devices, providers or mailboxes. `gh` read verbs only.
Child repos: `board` in check mode only, never `--rebuild`, no other scanner pointed at them,
nothing written there, and no child named, quoted or pathed: counts only. Every scratch repo,
extracted tree and copy lives under your scratchpad, named by your prefix, and is deleted when
you finish; never mutate the worktree's `tools/`, and never run an installed tool by bare name
from `PATH`.

## The verdict items

1. **Per API finding, PP1 to PP11:** does the new evidence CONFIRM, CHANGE (say how, including
   severity) or REFUTE it? A finding no missing check touches is marked "untouched".
2. **New findings** from the missing checks, prefix `PQ` (`PQ1`, `PQ2`, …), with severities
   (MAJOR / MODERATE / minor / note) and counsel kept beneath each.
3. **The overall line for the pass**, original plus top-up: PASS / PASS-WITH-FINDINGS / FAIL
   with counts.
4. **TOP-UP SUFFICES or FULL RE-RUN** — the principal's 2026-10-28 ask, in his words: *"decide
   if the "top-up" is good enough or I should be doing a "full re-run""*. Answer with reasons,
   against his bar of *"a comparable quality outcome as if we ran the fable review on this
   laptop"*: did the API pass's limits reach any judgement beyond the checks above, such as
   what the reviewer chose to probe, what it could not see, or what truncation cut off?

## House rules for this run

- Name your review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo
  is PUBLIC: never quote a secret, a placeholder token, an email address, a private repo's
  name, a local term or a personal detail.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: this brief's sibling (now folded at the end of this file), the queue
pointer, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, and every verdict in
`docs/reviews/` other than the original pass file named above. The original pass file is open
to you from the start.

## Process

**Phase 1.** Read first, then run the missing checks. Append your verdict below a `---` divider
in THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC date
you ran), the per-check results, the four verdict items, the standing checklist V1–V7 where a
missing check bears on it (discharge the rest in one line), a re-run ledger (commands and
results) and a follow-up checklist. Then STOP and commit phase 1 unrevised before opening the
sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: notes against its
hypotheses and re-run results, any finding formed at reconcile marked as such, and the overall
line and the TOP-UP / FULL RE-RUN answer restated. Never revise phase-1 text. Then fold the
sibling in below the reconcile and delete it.

`board` is doctrine by function (rule 3): record all findings and apply nothing; the principal
decides.

---

## Verdict — act 1 (phase 1), run 2026-11-01 UTC

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), on the principal's laptop through Claude Code;
  tier checked at selection. Permission on record: the principal's 2026-11-02 drain approval
  for Fable work, under which he also lifted his 2026-10-29 hold on running these top-ups.
- **Orchestrators, off-tier and disclosed:** I was spawned by session `f8e61647`, a headless
  Opus 5.5 orchestrator, itself started by session `c87c4ee0` (Opus 5.5). Both hold the
  context partition, form no finding and write no severity; neither authored the delta, the
  original brief, the API harness or this brief.
- **Independence:** not started or instructed by session `8e498ef1` or its workers,
  `5070f22b` or its subagents, `f7b25adb` or anything it dispatched, or `29af7e91`.
- **Worktree:** `atelier-160-970-1321`, HEAD `36b9e68`, read-only to me except this file.
  `git log --oneline 0a2b7a7..HEAD -- tools/ .githooks/ .github/` prints nothing: the code is
  the API pass's. `010/190` has not landed; the grace is at HEAD.
- **Run date:** 2026-11-01, 13:23–13:57 UTC, 17 days before the grace end.
- **Partition:** the sibling was removed from the worktree before I started (`git status`
  shows it deleted); I did not look for it elsewhere, and ran no unscoped `git diff` in the
  worktree, which would have printed the deleted file.

### Disclosure — what I read before writing

This brief; the original pass file whole (brief, both API acts, folded sibling);
`docs/method/REVIEW.md` rules 1–4, the lenses, the checklist and the lifecycle; the first 12
lines of `010/190`; `tools/board.py` lines 380–445 and 642–830 and the code diff of `28ef94a`
(`tools/board.py`, `tools/test_board.py`); `tools/floor.py` lines 1850–1930 and its `--list`;
`.githooks/pre-commit`; `.github/workflows/floor.yml` lines 120–150; the `--help` of `board`,
`pins`, `floorfleet` and the five prose gates; item `160/195` whole, because it bears on
PQ-e. Not opened: the queue pointer, `docs/SESSIONS.md`, `docs/sessions/`,
`docs/ROADMAP-DONE.md`, any other verdict. Incidental: the `git log` subjects of the five
commits above the API pass's HEAD at onramp (claim commits and one other pass's act-1 commit;
nothing opened); child repository slugs and run metadata passed through my context for PQ-d
and are not written here. The harness loaded user-level and repo instruction files and a
memory index that hold private context this verdict does not carry.

### Interpreters, stated first

`/usr/bin/python3` on this machine is Python 3.9.6; the `python3` on PATH is
`/usr/local/bin/python3`, 3.14.6; CI pins 3.12. PQ-a and PQ-c ran clean under 3.9. PQ-b under
3.9 reports 18 errors in four modules (`X | None` in a class body, `write_text(newline=)`,
`contextlib.chdir`), all interpreter age and none the delta's; under 3.14 it is green. Both
runs are in the ledger; the gap is PQ2.

### Per-check results

**PQ-a — `test_board.py` as given, no override.** Exit 0, 59 tests OK, with the machine's
normal git config (`commit.gpgsign=true`, ssh format, key reachable). PP9 is the portability
note it framed itself as.

**PQ-b — the full suite, once.** Under `nice -n 10`, in two foreground pieces by module-name
pattern (`test_[a-l]*`, `test_[m-z]*`) so each fitted the harness timeout: 1028 OK in 189 s
and 1004 OK in 276 s, exit 0 both — 2032 tests, the count the sibling reported on 2026-10-26.
V2 for the suite is discharged by a run, not a read.

**PQ-c — the floor at HEAD with the real term list.** Hook plane exit 0; CI plane exit 0.
`leakscan` reads "structural + local" on both planes: `✅ enforced` on the hook plane, `🟡
enforced (cover not guaranteed)` on the CI plane by wiring, since that plane does not pass
`--require-terms`; `board` `✅ enforced` on both, index current; `secretscan` 25 advisory on
the CI plane, 0 blocking; the four warn-only guards unchanged. The API ledger's floor row
(exit 1, `leakscan` only) was the sandbox, not the repo.

**PQ-d — the grace notice in real CI logs, by count.**

- Split boards under the repositories directory on 2026-11-01: **12** children, each with a
  first `docs/ROADMAP.md` commit before 2026-10-28. The API pass's 11 was its reach, not the
  fleet; its own limits section said checkouts elsewhere were unreachable.
- `board` check mode, both planes, no date injected: **11** current, **1** accepted only under
  the grace (⚠️ line, exit 0 on both planes), **0** stale. The API pass counted 2 under the
  grace on 2026-10-28; one has rebuilt since.
- The remaining old-form child's `floor` runs: 15 listed; **7** started a job (all on
  2026-10-17, before the delta: 2 green, 5 red); **8** started no job (1 on 2026-10-21, 7 on
  2026-10-26, each with 0 steps and no log; the latest carries an account-billing annotation
  from GitHub). Its last green log (2026-10-17) shows `board` inside a collapsed
  `##[group]board (enforced)` group under `✅ board enforced`; no run of its own after the
  delta has a log. So **the CI plane assumed in lens 1 (C) is not running for this child**:
  both planes flip together in the code, but only its hook can say so on 2026-11-18.
- Every post-delta green `floor` log readable across the fleet: **115** runs over **10**
  children (of the other 2, one has no GitHub origin resolvable from its checkout; one is the
  child above). **10** of the 115, in **3** children, carry the ⚠️ grace line — so at least 4
  children passed through the grace, 3 of which have rebuilt. In all 10 the line sits
  **inside the collapsed `board` group**; **0** `::warning::` annotations (`##[warning]` in
  the rendered log) carry it; the summary line reads `✅ board enforced`. Two further
  children's latest runs are red on `secretscan`, with `board` current.
- The hook plane, the brief's fallback, run as well: a synthetic two-item board (one wrapped
  bold title with a line-two claim) with its index rendered by `_index_entry_v1`, committed
  through a copy of the tracked `.githooks/pre-commit` with `ATELIER_TOOLS` at the
  worktree's `tools/`. Commit exit 0; the ⚠️ line is line 15 of 54 lines of hook output, the
  summary `✅ board enforced` is line 46, no annotation. A first attempt without the board
  preamble reproduced the "old form plus a problem" case: `✗` problem first, then the ⚠️
  "accepted" line, then `BLOCKED by: board` — PP8's last point, live on the hook plane.
- Which tool each hook runs: **11** of 12 children set `hooks.atelierTools` to a `tools/`
  whose `board.py` is byte-identical to HEAD's; **1** leaves it unset, so its hook, where
  installed, fails closed on "floor.py not found". All 12 set `core.hooksPath`; a rough test
  (relative paths only, not verified further, outside this brief) found an executable
  `pre-commit` at that path in **5**.

**PQ-e — `/security-review`.** Not invoked, with grounds: its prompt, read from the installed
Claude Code build, runs `git status`, `git diff --name-only origin/HEAD...`, `git log
origin/HEAD...` and `git diff origin/HEAD...` in the *session's* cwd — this worktree, whose
commits above `origin/main` are claims and another pass's act-1 verdict, and whose pending
change is the partition's deletion (`160/195` records the same mechanism). Instead I ran the
prompt's four commands verbatim over a scratch clone, on a branch at `28ef94a^` carrying the
delta as its one commit: status clean, files `tools/board.py` and `tools/test_board.py`, one
commit, and the diff byte-identical to `git diff 28ef94a^ 28ef94a` on those paths. Read
against the prompt's categories and exclusions (test files and documentation excluded;
confidence below 0.7 unreported): the delta adds no subprocess, file open, eval,
deserialiser, shell string or new argument; the new regexes run over already-committed item
text; `today` is injectable only from Python and `_today_utc()` reads the clock. **No
finding at any confidence.** Lens 4 as the API pass discharged it stands.

### The verdict items

**1. Per API finding, PP1 to PP11.**

- **PP1, PP2, PP3, PP4, PP6, PP7, PP10, PP11 — untouched.** No missing check bears on them;
  PQ-b shows the suite green, which PP3 never doubted.
- **PP5 — CONFIRMED live, severity unchanged (minor).** 10 CI logs in 3 children carry the
  line inside a collapsed group, with no annotation and a green summary; the hook plane
  prints it under the same green summary. The counsel stands and the counts give it weight.
- **PP8 — CONFIRMED on its last point** (the ⚠️ "accepted" line beside exit 1, live on the
  hook plane); the rest untouched.
- **PP9 — CONFIRMED as framed.** On a host whose signing key is reachable the class passes
  as given (59/59): a portability note, not a defect of the delta.

Nothing REFUTED; no severity CHANGED.

**2. New findings.**

**PQ1 — note (an estate fact, not the delta's).** The one child still on the old form on
2026-11-01 has had no CI job start since 2026-10-21 (an account-billing annotation), and its
last green floor run predates the delta. For it the grace's CI-plane notice (PP5) has never
run and cannot run; on 2026-11-18 its hook reds, where installed, and its CI stays unstarted,
so the red the notice was meant to pre-empt arrives from a plane that never showed the
notice.
*Counsel (not applied):* at `010/190`'s "which children have not yet rebuilt" step, take the
list from `board` check mode on each checkout, not from `fleet-pins` and "each child's latest
floor run" alone: a child with no running CI is the one that step would miss.

**PQ2 — note (pre-existing, outside the delta).** The suite needs Python 3.11 or later
(`contextlib.chdir` in `test_leakscan.py`; `X | None` in class bodies in `test_floor.py` and
`test_floorfleet.py`; `write_text(newline=)` in `test_allowmarker.py`) while `floor.py`,
`board.py` and `test_board.py` run on 3.9, and no file states the floor: `tools/README.md`
and `README.md` name no version, the hook's remedy text says "Python 3, stdlib only", CI
pins 3.12. A contributor on the macOS system interpreter meets 18 errors that read as broken
tests.
*Counsel (not applied):* one line in `tools/README.md` naming the version floor, and a
`sys.version_info` guard with a plain message at the top of the test modules that need it.

**3. The overall line, original plus top-up.** **PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE
(PP1, PP2) · 5 minor (PP3–PP6, PP11) · 6 notes (PP7–PP10, PQ1, PQ2). `board` is doctrine by
function (rule 3): nothing applied; the principal decides.

**4. TOP-UP SUFFICES.** Against the principal's bar — a comparable quality outcome to a
laptop run — the API pass holds. Reasons:

- Each of its five stated limits was environmental and is closed by a run: the suite is
  green, the floor is green with the real term list, the signing class passes as given, the
  grace line is seen in 10 real CI logs and one real hook run, and the security prompt was
  run by hand over the exact delta. None of the five changed a severity or refuted a finding.
- Did the limits reach a judgement beyond the five? Three places to look. *What it chose to
  probe:* its probe set exceeded the brief's re-run list (eight assumptions, ten mutations, a
  2,305-item census, a 20-shape matrix, both planes on four dates, two reconcile probes) and
  agrees with the sibling's independent results where they overlap. *What it could not see:*
  one child — it counted 11 of the 12 that existed; by count and by class the missed child
  adds nothing (current on both planes; no grace line in its 45 green runs). *What truncation
  cut:* its census figures (300/278 lines, 12/12 identity, 9/2 under the grace) agree with
  the author's, the sibling's and my 11/1 after a fleet that moved; no figure reads as a
  head-only artefact.
- The one new fact (PQ1) came from the `gh` check the brief listed as missing, not from a
  judgement the sandbox formed wrongly; it is a note on the estate, not on the delta.
- Residual, stated: a top-up cannot re-choose what the first reviewer chose to probe; I
  re-drove none of the projection census and formed no view of the children's item shapes
  beyond `board`'s exit and notice. Were a MAJOR in play I would say full re-run; on 0 MAJOR
  and 2 MODERATE, both formed from live probes the sandbox did not limit, a full re-run buys a
  second opinion, not a missing one.

### Standing checklist, where a missing check bears

- **V1** — the hook's "Python 3, stdlib only" is weaker than what the suite needs (PQ2);
  nothing else new.
- **V2** — the suite, the floor on both planes, the signing class and the grace line in CI
  all re-run live; the author's "1963 Python tests green" and the sibling's 2032 reconcile as
  2032 at HEAD.
- **V3, V4, V5** — discharged: no missing check touches a mirror, a second home or a
  contradiction beyond what the API pass recorded.
- **V6** — PQ-e above.
- **V7** — provenance above and in the brief.

### Re-run ledger (worktree root; exit codes read explicitly; `uptime` before each heavy step)

| command | result |
|---|---|
| `git log --oneline 0a2b7a7..HEAD -- tools/ .githooks/ .github/` | nothing |
| `/usr/bin/python3 -m unittest discover -s tools -p test_board.py -v` (3.9, signing on) | 0; 59 OK |
| `nice -n 10 /usr/bin/python3 -m unittest discover -s tools -p 'test_[a-l]*.py'` (3.9) | 1; 762 run, 18 errors, interpreter age |
| `nice -n 10 /usr/local/bin/python3 -m unittest discover -s tools -p 'test_[a-l]*.py'` (3.14) | 0; 1028 OK, 189 s |
| `nice -n 10 /usr/local/bin/python3 -m unittest discover -s tools -p 'test_[m-z]*.py'` (3.14) | 0; 1004 OK, 276 s |
| `/usr/bin/python3 tools/floor.py --plane hook --root .` | 0; every enforced check ✅; `leakscan` structural + local |
| `nice -n 10 /usr/bin/python3 tools/floor.py --plane ci --root .` | 0; `secretscan` 🟡 25 advisory; `leakscan` 🟡 by wiring; `board` ✅ |
| `board --check` and `--check --staged` per child, 12 children, HEAD's `board.py` by path | 11 current, 1 grace, 0 stale, both planes |
| `gh run list` / `gh run view --json jobs`, the old-form child, 15 runs | 7 started (pre-delta), 8 not started (0 steps) |
| `gh run view --log`, 115 post-delta green runs, 10 children | 10 logs in 3 children carry ⚠️; all in-group; 0 annotations; ✅ summary |
| synthetic old-form board through a copy of the tracked hook, `git commit` | 0; ⚠️ at line 15 of 54, ✅ board at line 46; without the preamble: ✗, ⚠️, BLOCKED |
| `hooks.atelierTools` per child, `cmp` against HEAD's `board.py` | 11 identical, 1 unset |
| the skill prompt's four git commands over the scratch clone branch | clean; 2 files; 1 commit; diff identical to the delta; 0 findings |

Scratch (the clone, the hook repository, the hook copy, logs and outputs) lived under my
scratchpad with the prefix `pq` and was deleted at the end of the act; no live capture kept.

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] PP1–PP11 — as the API pass listed them; unchanged.
- [ ] PQ1 — take `010/190`'s not-yet-rebuilt list from `board` on each checkout, not from CI.
- [ ] PQ2 — state the Python floor in `tools/README.md`; guard the three test modules.
- [ ] Orchestrator — the API verdict's closing line ("the full suite and `leakscan` need a run
      outside this sandbox before close") is discharged by PQ-b and PQ-c.

ACT 1 SAVED

### Reconcile (act 2, 2026-11-01 UTC)

Opened for this act, after act 1 was committed unrevised at `d230cc0` by session `f8e61647`:
the sibling, released from the orchestrator's hold. The other phase-2 bars lifted with it; I
opened none of them, since nothing in the sibling needed them. Three small read-only probes
were run to answer it (the timing bound in `test_pins.py`, the identity and birth dates of
the 12 child checkouts, and the pin of the remaining old-form child); nothing in act 1 is
revised.

#### Against the sibling's five re-run results (2026-10-28, load 14–53)

1. *PQ-a: 59 OK, signing on.* Agrees with act 1.
2. *PQ-b: 2032 tests, exit 1, one failure in `test_pins.BoundedMemory`, "scan did not finish
   in time".* Act 1 ran the same 2032 green at load 5–10 in 465 s against the sibling's
   1197 s. The test runs `pins` as a subprocess with a 60 s wall-clock timeout over 200
   synthetic siblings (`test_pins.py` lines 306–309), so at the sibling's load it timed out
   and at mine it did not. The sibling's reading — timing-bound, outside the delta — holds,
   and the un-checked half ("whether it reproduces at normal load") is answered: it does
   not. Recorded as **PQ3 (note, formed at reconcile)** below.
3. *PQ-c: both planes exit 0; `pathscan` 3 warn-only findings outside the delta.* Agrees on
   every exit and state; act 1 did not count `pathscan`'s findings and does not now.
4. *PQ-d: 11 split boards, 2 under the grace, both with their last ten runs failing without
   a job starting.* Partly superseded by three days: act 1 counts 12 boards, 1 under the
   grace. The 12 are 12 distinct repositories (no linked worktree, no shared git directory),
   each with a first `docs/ROADMAP.md` commit and a checkout directory older than
   2026-10-28 — so the API pass and the brief-writer both missed the same one, for a reason I
   cannot see from here; by class it adds nothing (current on both planes, no grace line in
   45 green runs). Of the sibling's 2, one has rebuilt; the remaining one's unstarted CI is
   what act 1 saw (8 runs, 0 steps). The sibling could read no grace line in CI because it
   looked only at those 2; act 1 widened the read to every post-delta green run and found the
   line in 10 logs across 3 other children, which had been on the old form with CI running
   and have since rebuilt. So the grace reached at least 5 children: 3 told by CI inside a
   collapsed group, 2 whose CI never started.
5. *PQ-e not run.* Act 1's hand-run of the prompt over the exact delta: 0 findings.

#### Against the sibling's six hypotheses

1. *PP9 is a portability note only.* Confirmed (PQ-a).
2. *The floor and suite gaps hide nothing about the delta.* Confirmed; the one suite failure
   is load-bound and did not reproduce (PQ3).
3. *Lens 1 (C) needs a qualification the API pass could not see; PP5 sharpens.* Confirmed
   and formed independently in act 1 as PQ1, before reading this. Two refinements from act
   1's wider read: the qualification bites on 1 child on 2026-11-01, not 2; and the "CHANGELOG
   at a pin bump is the only channel" clause has been exercised — the remaining old-form
   child's pin is at or past the delta (`pins`, read-only, by count), so by the house's own
   channel it has been told, and is still on the old form 17 days before the cut-off. That
   is a fact for `010/190`'s list, not a new finding against the delta.
4. *The fallback hook run confirms the notice wording.* Confirmed: ⚠️ line, exit 0, the
   staged remedy carrying `--from-index`, printed under a green summary (act 1, PQ-d).
5. *`/security-review` finds nothing.* Confirmed by the hand-run.
6. *TOP-UP SUFFICES.* Agrees with act 1's reasoning and adds nothing it did not weigh; the
   live-CI fact (its hypothesis 3) is the PQ1 act 1 carried.

#### Findings formed at reconcile

- **PQ3 — note (pre-existing, outside the delta).** `test_pins.BoundedMemory` bounds its
  subprocess at 60 s of wall clock, so the full suite reds under machine load (the sibling's
  run, load 14–53) and is green at normal load (act 1, load 5–10). A suite whose exit depends
  on the host's load is the class board section `120` already names for another test.
  *Counsel (not applied):* scale the timeout by a measured baseline, or mark the memory
  bound as the assertion and the timeout as a skip with reason.

#### Overall, restated

**PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE (PP1, PP2) · 5 minor (PP3–PP6, PP11) · 7 notes
(PP7–PP10, PQ1–PQ3). Act 1's text and severities are unchanged; the reconcile added one note.
**TOP-UP SUFFICES**, restated: the sibling's own laptop results and act 1's agree on every
check, and the only divergence (one load-bound test) is answered. `board` is doctrine by
function (rule 3): nothing applied; the principal decides. The sibling is not folded here;
the orchestrator folds it.

ACT 2 SAVED

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-01)

*Released to the reviewer only after its act-1 findings were committed; folded here
verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (session `f8e61647`, Claude Opus 5.5, started by session `c87c4ee0`) formed no
finding and wrote no severity.*

### Sibling to the paragraph-projection and grace top-up — held under rule 1's split

Sibling of `docs/reviews/2026-10-28-1255-paragraph-projection-grace-topup-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the top-up's phase-1 findings are
committed.** Written 2026-10-28 UTC by session `29af7e91`, the brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

#### Re-run results held back from the brief

Run once each by the brief-writer, 2026-10-28 between 12:54 and 13:45 UTC, from its worktree
root at `16c6511` (code identical to the API pass's `0a2b7a7`), on the principal's laptop.
Load averages were between about 14 and 53; other sessions were live.

- **PQ-a.** `test_board.py -v` as given, with signing on and reachable: 59 tests OK, exit 0.
- **PQ-b.** Full suite under `nice -n 10`: 2032 tests in 1197 s, **exit 1, one failure**:
  `test_pins.BoundedMemory.test_peak_memory_does_not_scale_with_sibling_count`, "scan did not
  finish in time". It is outside the delta and timing-bound, at very high load; whether it
  reproduces at normal load was not checked.
- **PQ-c.** Floor at HEAD with the real term list: ci plane exit 0 (`board` ✅; `leakscan` 🟡,
  no `--require-terms` on the ci plane; `pathscan` 3 warn-only missing-path findings outside
  the delta); hook plane exit 0.
- **PQ-d.** Children by count, `board --check` from the worktree's copy, read-only: 11 split
  boards; 11 exit 0; **2** pass only under the grace, which agrees with the API pass. For both
  of those 2, the latest ten GitHub runs ended `failure` **without a job starting**: the CI
  provider refused to start them for an account-level reason outside the repos. No log exists
  to read, and the grace line could not be observed in CI. Atelier's own floor runs, a public
  repo, are green. The hook-plane fallback (a real `git commit` over a synthetic old-form
  board) was **not run** by the brief-writer.
- **PQ-e.** Not run (a headless brief-writer cannot aim `/security-review` usefully).

#### Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. **PP9 is a portability note only.** On a host whose key is reachable, `StagedPlane` passes
   as given; the note stands as written.
2. **The API pass's floor and suite gaps hide nothing about the delta.** The floor is green and
   the one suite failure is a load-bound test elsewhere.
3. **Lens 1 (C) needs a qualification the API pass could not see.** It counted "CI →
   `floor.yml@main`, 11/11" from the committed workflows. For the 2 children still on the old
   form, the CI plane is not running at all at present. So "both planes flip together" on
   2026-11-18 is true of the code and false of what those children will see: until their CI
   jobs start again, only the hook will red. The same fact sharpens PP5. For those 2, the
   CHANGELOG at a pin bump is the only channel. The ⚠️ line cannot reach a CI log that is
   never written, and one of the two has not bumped its pin.
4. **The fallback hook run confirms the notice wording.** Through a real `git commit`, the
   hook should print the ⚠️ line and exit 0 before 2026-11-18, with the staged remedy carrying
   `--from-index`, as the API pass saw through the CLI.
5. **`/security-review` finds nothing.** The delta adds no subprocess and no new input path.
6. **Top-up or full re-run.** Every judgement-forming probe the API pass ran (the census, the
   identity check, the boundary table, the mutations with signing switched off) was local and
   disclosed, and the missing checks so far confirm it. That points to TOP-UP SUFFICES. The
   live-CI fact in hypothesis 3 is new evidence the API pass could not reach, but a top-up
   carries it without a full re-run.

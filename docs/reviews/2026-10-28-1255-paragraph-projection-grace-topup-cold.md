# Top-up cold pass — paragraph projection and grace, the checks the API pass could not run

**Pass type:** top-up to a code cold pass, doctrine by function, per `docs/method/REVIEW.md`
rule 4. It covers ONLY the checks the first pass could not run, plus one verdict on whether a
top-up is enough.
**Tier:** Fable, on the principal's laptop through Claude Code, checked at selection by whoever
takes the pass. Fable work runs only with the principal's explicit permission; this brief's
dispatch records that he approved these top-ups (2026-10-29 local date). The taker confirms
that permission is on record at claim and stops if it is not.
**Status:** BRIEF WRITTEN 2026-10-28 UTC; pass NOT run.
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

Rule 2 bars until phase 2: this brief's sibling
`docs/reviews/2026-10-28-1255-paragraph-projection-grace-topup-cold.deferred.md`, the queue
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

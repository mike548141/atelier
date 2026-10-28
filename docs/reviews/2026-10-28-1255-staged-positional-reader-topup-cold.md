# Top-up cold pass — the staged-positional reader, the checks the API pass could not run

**Pass type:** top-up to a code cold pass, doctrine by function, per `docs/method/REVIEW.md`
rule 4. It covers ONLY the checks the first pass could not run, plus one verdict on whether a
top-up is enough.
**Tier:** Fable, on the principal's laptop through Claude Code, checked at selection by whoever
takes the pass. Fable work runs only with the principal's explicit permission; this brief's
dispatch records that he approved these top-ups (2026-10-29 local date). The taker confirms
that permission is on record at claim and stops if it is not.
**Status:** BRIEF WRITTEN 2026-10-28 UTC; pass NOT run.
**Original pass:** `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md` (the
original brief, both acts of the API verdict, and the folded sibling, in one file).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/950-rule-4-cold-pass-queued-staged-positional-reader.md`.

## Why a top-up is owed

The first pass ran on Fable 5.1 through a Claude Platform API harness, not on the laptop. Its
tools ran on this machine but sandboxed: no network, no `gh`, no keychain, no MCP connectors,
no Claude Code skills or subagents, a 300 s command limit, head-only output truncation, no
loopback bind, a global git config whose signing key was unreachable, and no repo virtualenv.
The verdict names its own limits (*Limits of this pass* and the re-run ledger). Several of
them sit under a finding or the verdict:

- every test that commits in a scratch repo errored (exit 128), so the four delta test files
  never ran green, and QS4's mutation baseline carried those errors;
- the full suite's summary line was lost to truncation and was not re-run;
- `leakscan` and `floorfleet` ran with the local term list replaced by an empty file;
- QS1 (MAJOR) was driven through `floor.py --plane hook`, never through a real `git commit`;
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

- **Author of the work under review:** session `8e498ef1` (a principal-opened Opus 5.5 queue
  run, 2026-10-18) and the Sonnet worker it dispatched, as the original brief lists them.
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
- ⚠️ **Exposure, disclosed.** This brief-writer read the original brief file whole, including
  both API acts and the folded sibling; the two queue pointers whole; `REVIEW.md` rule 4 and
  `skills/review-brief/SKILL.md` whole; `tools/report.py` lines 145–190 and the class names of
  the delta's test files; `.githooks/pre-commit` by grep. It ran QU-a, QU-b, QU-c, QU-f, QU-h
  and the M7 half of QU-d once; it did not run QU-e, QU-g or the other eight mutations
  (results and gaps held in the sibling). It did not open `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md` or any other verdict. Its harness loaded user-level
  and repo instruction files and a memory index, which hold private context this brief does
  not carry.

## Read first

Read the original pass file whole before you run anything: the original brief is your scope,
the API verdict is the subject of your per-finding answers, and its folded sibling is already
open material. Then read `docs/method/REVIEW.md` rule 4. The code under review is unchanged
since the API pass's HEAD: `git log --oneline 0a2b7a7..HEAD -- tools/ .githooks/ .github/`
should print nothing; if it prints a commit, weigh it before you continue.

## The missing checks — run only these

Each says what to run and which claim it tests. Run from your review worktree root, in the
foreground. Read exit codes explicitly. Check `uptime` before each heavy step; one heavy process
at a time, under `nice -n 10`.

- **QU-a. The environment the hook really has.** `command -v python3`, `python3 --version`,
  `/usr/bin/python3 --version`; the interpreter line `.githooks/pre-commit` uses; one throwaway
  commit in a scratch repo under your scratchpad to prove signing works. Tests QS9 (the suite
  "not runnable on the system Python 3.9") against what the hook and the suite actually run
  under here, and confirms the signing limit is absent.
- **QU-b. The four delta test files, as given, no environment override.**
  `python3 -m unittest discover -s tools -p test_report.py`, and the same for
  `test_leakscan.py`, `test_secretscan.py`, `test_conflictscan.py`, with the machine's local
  term list where it normally lives. Tests the API ledger's attribution of every error and
  failure to the sandbox (signing, the denied `stat`, `contextlib.chdir` on 3.9), and the
  second half of QS9.
- **QU-c. The full suite, once.** `nice -n 10 python3 -m unittest discover -s tools`, with its
  output written to a file in your scratchpad so the summary line survives; read the tail.
  Tests V2 for the suite, which the API pass could not read.
- **QU-d. The mutations, against an all-green baseline.** Clone your worktree into your
  scratchpad (`git clone -q <worktree> <scratch>/clone`) and mutate the clone's `tools/`. A
  bare `git archive` extract is not a git repo, and in it the `StagedAbsolutePathTest`
  classes fail unmutated for that reason alone. First run the four delta test files in the
  clone unmutated and confirm they are green. Then apply mutation M7 (in `scope_staged`,
  `prefixes = tuple(norm)` in place of `tuple(n + "/" for n in norm)`) and run the four files
  **whole**, not filtered by `-k`. The API baseline had errors in the git-backed classes
  (`StagedRealGitRepo`, `StagedSpacedPathAndMultiHunkTest`, `ParseAddedLinesTest`) and ran
  with `-k Staged -k scope_staged`. Tests QS4: does any test that could not run there red M7?
  Re-run the other eight mutations the verdict names the same way, as far as your judgement
  says they need it.
- **QU-e. QS1 through a real commit.** In a scratch repo under your scratchpad, wire the hook
  as an adopter would: copy the worktree's `.githooks/` in, set `core.hooksPath` and
  `hooks.atelierTools` in that scratch repo's own config (pointing at your extracted or
  worktree `tools/`, never at an installed copy), commit an `.atelier-floor.json` whose
  `scope` names `Docs` for `secretscan` and `conflictscan`, then stage a live-shaped (synthetic,
  concatenated) private-key header under `docs/` and run `git commit`. Repeat for the NFD
  spelling. Tests QS1's claim that the hook, the only gate before the remote, lets it through,
  at the real gate rather than at `floor.py --plane hook`. Say also, from `floor.py` and the
  workflows, what the CI plane on a case-sensitive runner would do with the same config, and
  whether that changes QS1's severity.
- **QU-f. The floor at HEAD with the real term list.** `nice -n 10 python3 tools/floor.py
  --plane ci --root .` and `python3 tools/floor.py --plane hook --root .`. Tests the API
  ledger's floor rows, which ran `leakscan` over an empty term list. If a check reds, name the
  scanner and the file, and never quote a term.
- **QU-g. `/security-review`.** From a scratch clone whose only pending change is the code diff
  of `692c04a` (no brief, no sibling, no markdown), aim `/security-review` at it, or discharge
  it in one line with grounds. Tests lens 4, which the API pass discharged because the command
  was unreachable.
- **QU-h. CI, read-only.** `gh run list --repo mike548141/atelier -L 5` and the job's Python
  version from a recent floor run. Tests QS9's "CI pins 3.12, so CI is unaffected" against a
  live run rather than the workflow text.

Not owed, with grounds: the child probe (its counts agree with the brief-writer's laptop run
in the folded sibling, and the reconcile accounts for the one difference); the 45-spelling
table and the cwd probes (pure local process runs the sandbox did not limit). Run either
again only if a missing check above gives you cause, and say why.

## Live access: read-only

No apply, no config change, no writes to devices, providers or mailboxes. `gh` read verbs only.
No scanner pointed at a child repo, nothing written to one, and no child named: counts only.
Every scratch repo, extracted tree and mutated copy lives under your scratchpad, named by your
prefix, and is deleted when you finish; never mutate the worktree's `tools/`, and never run an
installed tool by bare name from `PATH`.

## The verdict items

1. **Per API finding, QS1 to QS11:** does the new evidence CONFIRM, CHANGE (say how, including
   severity) or REFUTE it? A finding no missing check touches is marked "untouched".
2. **New findings** from the missing checks, prefix `QU` (`QU1`, `QU2`, …), with severities
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
`docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.deferred.md`, the queue
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

The guards are doctrine by function: record all findings and apply nothing (rule 3); the
principal decides.

# Top-up cold pass — the staged-positional reader, the checks the API pass could not run

**Pass type:** top-up to a code cold pass, doctrine by function, per `docs/method/REVIEW.md`
rule 4. It covers ONLY the checks the first pass could not run, plus one verdict on whether a
top-up is enough.
**Tier:** Fable, on the principal's laptop through Claude Code, checked at selection by whoever
takes the pass. Fable work runs only with the principal's explicit permission; the dispatch
that launched this brief-writer wrongly recorded that he approved these top-ups; he asked
for the briefs and, on 2026-10-29 local date, chose to hold running them (corrected by session
f7b25adb). The taker confirms permission is on record at claim and stops if it is not.
**Status:** BRIEF WRITTEN 2026-10-28 UTC; act 1 written 2026-11-01 UTC — top-up ran on the
laptop (Fable 5.1), PASS-WITH-FINDINGS, 1 MAJOR · 2 MODERATE · 3 minor · 7 notes (QS1–QS11 plus
QU1–QU2), TOP-UP SUFFICES; act 2 (reconcile) pending.
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

---

*Act 1 run by Fable 5.1 (`claude-fable-5-1`) on the principal's laptop through Claude Code, as a
subagent of orchestrator session `4610c607`, 2026-11-01 UTC.*

## Verdict — top-up, phase 1 (cold pass, 2026-11-01 UTC)

### Provenance, repeated

- **Reviewer:** Fable 5.1, tier checked at selection. The pass runs as reviewer-plus-orchestrator
  under rule 4: I was spawned by session `4610c607` (Opus 5.5), a headless orchestrator started
  by session `c87c4ee0` (Opus 5.5). Both are off-tier orchestrators, disclosed here before the
  findings: they hold the context partition, formed no finding and wrote no severity. Neither
  authored the delta, the original brief, the API harness or this top-up brief.
- **Spawn test:** I was neither started nor instructed by any barred session: `8e498ef1` (the
  author) or its workers, `5070f22b` or its subagents, `f7b25adb` or anything it dispatched, or
  `29af7e91` (this brief's writer).
- **Permission:** the principal's 2026-11-02 (local date) drain approval for Fable work, which
  lifted his 2026-10-29 hold on these top-ups; the board claim cites it.
- **Worktree:** `atelier-160-950-1335`, detached at `2b55622`, read-only to me except this file.
  The brief's sibling was removed from the worktree by the orchestrator before I started (it
  shows as a deleted file in `git status`); I did not look for it in history, other checkouts
  or scratch. Scratch work ran under a `rv950-` directory in my session scratchpad: a scratch
  clone of the worktree (the sibling deleted from it unread, straight after cloning), a
  signing-probe repo and a hook-probe repo. All are deleted at the end of act 2.
- **What I read:** this brief whole; the original pass file whole (brief, both API acts, the
  folded sibling); `docs/method/REVIEW.md` lines 25–445; `.githooks/pre-commit` whole;
  `tools/report.py` `scope_staged` and `broken`; `tools/floor.py` lines 1580–1600, 1790–1850,
  `_reject_escaping_scope` and the registry entries for the three guards; `.atelier-floor.json`
  at HEAD; `.github/workflows/floor.yml` by grep; the `scope_staged` call sites in the three
  guards; the code diff of `692c04a` body-free (`git diff 692c04a^ 692c04a -- tools/`, never
  `git show`). Not opened: the sibling, the queue pointer, `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other verdict.
- **Exposure, disclosed:** the ci-plane floor output printed two warn-only `pointerscan` lines
  naming the `950` and `970` queue-pointer files with a one-line state message each; I saw the
  filenames and that message, not the files. A count of `.deferred.md` files in the clone's
  `docs/reviews/` showed two other siblings exist; I saw a count, not a name. The signing probe
  printed the committer identity; not written here. My harness loaded user-level and repo
  instruction files and a memory index, which hold private context this verdict does not carry.

### Read first

`git log --oneline 0a2b7a7..HEAD -- tools/ .githooks/ .github/` printed nothing: the code is
unchanged since the API pass's HEAD. Load averages at each heavy step are in the ledger; the
machine was shared (load 3.4–7.8 on 12 CPUs) and each heavy step ran alone under `nice -n 10`.

### The missing checks — results

- **QU-a.** `command -v python3` resolves to a python.org 3.14.6 on this machine, for my shell
  and for a login shell (`zsh -l`); `/usr/bin/python3` is 3.9.6. `.githooks/pre-commit` is
  `#!/bin/sh` and calls bare `python3` from the committing shell's PATH, so the hook and the
  suite run on 3.14 here, not 3.9. The API pass ran everything on 3.9 because the sandbox's
  PATH did. A throwaway commit in a scratch repo signed (good SSH signature, one `gpgsig`
  header): the signing limit is absent on the laptop. Under `/usr/bin/python3` (3.9) in the
  clone: `test_report.py` 71 OK; `test_leakscan.py` 219 run, 7 errors, all
  `contextlib.chdir`; `test_allowmarker.py` 31 run, 9 errors, all `write_text(newline=)`.
  QS9's two incompatibilities reproduce exactly, and only on 3.9.
- **QU-b.** From the worktree root, bare `python3`, no environment override, the machine's term
  list where it lives: `test_report.py` 71 OK · `test_leakscan.py` 219 OK ·
  `test_secretscan.py` 174 OK · `test_conflictscan.py` 56 OK, each exit 0. Every error and
  failure the API ledger attributed to the sandbox is absent on the laptop, so the attribution
  holds for all of them: signing (`ParseAddedLinesTest`, `StagedRealGitRepo`,
  `StagedSpacedPathAndMultiHunkTest`), the denied `stat` (leakscan's 2 failures + 1 error) and
  3.9 (the 7 `contextlib.chdir` errors).
- **QU-c.** Full suite, once, `nice -n 10 python3 -m unittest discover -s tools`, output to a
  scratch file: **`Ran 2032 tests in 442.217s` — `OK`**, exit 0. The summary line the API pass
  lost is read; it matches the count the folded sibling records for 2026-10-26.
- **QU-d.** Clone of the worktree (a real git repo at `2b55622`), four delta files unmutated:
  71 / 219 / 174 / 56, all OK — an all-green baseline, including the git-backed classes the API
  baseline carried as errors. Then each mutation applied to the clone's `tools/` and the four
  files run **whole** (no `-k`), restored from git between mutations:

  | mutation | result on the four files run whole |
  |---|---|
  | M7 prefix boundary (`tuple(norm)`) | **all four green** (71/219/174/56 OK) — QS4 confirmed |
  | M1 old match restored (`norm = list(paths)`) | red in all four (1 + 4 + 4 + 4) |
  | M2 escaping refusal dropped | red in all four (1 + 4 + 4 + 4) |
  | M3 `.` case dropped | red in all four (1 + 1 + 1 + 1) |
  | M4 filter ignored | red in all four (1 + 1 + 1 + 1, `test_empty_by_scope_is_not_refused`) |
  | M5 refuse on empty | red in all four (1 + 1 + 1 + 1, the same test) |
  | M6 exact-file match dropped | red in `test_report.py` only (1); the three guard files green |
  | M8 refusal demoted to a print | red in all four (1 + 4 + 4 + 4) |
  | M9 first leakscan caller discards its code | red in `test_leakscan.py` (5, now including `StagedAbsolutePathTest`, which the sandbox could not run) |

  No test that could not run in the sandbox reds M7. M6's spread is new evidence (QU1 below).
- **QU-e.** A scratch repo wired as an adopter would: the worktree's `.githooks/` copied in,
  `core.hooksPath .githooks`, `hooks.atelierTools` pointed at the clone's `tools/`, a
  `.atelier-floor.json` committed first (that commit ran the hook and passed). Then real
  `git commit`s, each with the planted content built by concatenation at run time:

  | scope in the committed config | staged under `docs/` | `git commit` |
  |---|---|---|
  | `secretscan`, `conflictscan` → `Docs` (the brief's shape) | private-key header | exit 1, **blocked by leakscan** (unscoped; it has its own key-header rule); secretscan and conflictscan printed clean |
  | same | AWS-shaped access-key token | exit 1, blocked by leakscan again (own credential rule); secretscan clean |
  | same | a conflict marker | **exit 0, committed** — only conflictscan knows the class, and it was scoped away |
  | all three → `Docs` | private-key header | **exit 0, committed**; all three printed clean, leakscan as "structural + local" |
  | all three → the NFD spelling of a directory git stores NFC (`core.precomposeunicode=true`, set by git at init; index entry verified NFC with `core.quotePath=false`) | private-key header | **exit 0, committed** |
  | no scope (controls) | the same token; the same marker | exit 1 each, blocked by the right guard |

  QS1 holds at the real gate, for both spellings, on the house platform. The brief's exact
  shape is masked for secrets by the guards' overlapping rules and open for the class only one
  guard knows; scoping every guard that knows the class opens it for secrets too.
  **The CI plane.** `floor.py`'s ci arguments for the three guards carry no `--staged`
  (registry lines 447–480), so `_render` resolves the scope through the filesystem, and the run
  guard at 1797 blocks a declared path that does not exist for any scanner with
  `advisory=None` — all three guards. On a case-sensitive runner (`ubuntu-latest`, QU-h) `Docs`
  does not exist, so CI blocks the config itself: demonstrated here with the typo `Dcos` on
  both planes ("scope resolves to nothing — BLOCKING", exit 1). On this folding filesystem the
  ci plane resolves `Docs` to the real directory and secretscan reads it in tree mode: exit 1,
  one `private-key-header` finding. So CI reds after the push either way, with an honest
  message on Linux and a true finding on macOS. **Severity unchanged:** the hook is the only
  gate before the remote, and on a public repo the push is the publication; CI detects a burned
  secret, it does not prevent one. The narrower true statement for `floor.py` 1809–1819: the
  class is shut on the ci plane and on case-sensitive filesystems, and open on the hook plane
  wherever the filesystem folds case or normalisation.
- **QU-f.** From the worktree root, the real term list present at its home: `--plane ci` exit 0
  in 25 s; `--plane hook` exit 0 (staged set empty). leakscan reported "clean (structural +
  local)", so the local term plane ran. The ci plane's only reds are warn-only: `pathscan` 1
  missing-path finding in `docs/decisions/2026-10-03-0641-the-exception-register.md`, and
  `pointerscan` 2 queue-state findings on the `160/950` and `160/970` queue pointers (a pass
  recorded as run while the state line still says queued). None is this delta's (QU2).
- **QU-g.** `/security-review` was not run. Grounds: it reads the session's pending diff, and
  this session's pending diff is the worktree's, whose one pending change is the deleted
  sibling — running it there would feed barred material into this verdict (the SL2 class
  REVIEW.md names); a subagent cannot re-aim it at the scratch clone. Discharged with my own
  code-altitude read of the `692c04a` diff: the positionals are compared against git's output
  and never reach a subprocess argument, a pathspec or the filesystem; `os.path.normpath` is
  lexical; absolute and `..` forms are refused before any match; a leading `-` is consumed by
  argparse upstream; the three callers are identical; the fixtures are synthetic. Nothing
  reachable under OWASP A01 or A03; the API pass's lens-4 read stands.
- **QU-h.** `gh run list -L 5`: the floor workflow on `main`, latest success `41310941147`
  (4 m 38 s); the two cancelled rows are concurrency cancel-in-progress on back-to-back pushes.
  Its log: `actions/setup-python` with `python-version: 3.12`, "Successfully set up CPython
  (3.12.15)", on `ubuntu-latest`. QS9's "CI pins 3.12" is live-true, and the runner is
  case-sensitive, which QU-e's CI-plane answer relies on.

### Per API finding

- **QS1 — CONFIRMED, MAJOR unchanged.** Reproduced through a real `git commit` at the real
  gate, case-folded and NFD, with the content committed (QU-e). Sharpened: the brief's
  two-guard shape lets through only the class the scoped guard alone knows; scoping all three
  lets secrets through; CI reds after the push on both filesystem kinds.
- **QS2 — CONFIRMED.** M5 (refuse on empty) reds `test_empty_by_scope_is_not_refused` in all
  three guard files and `test_report.py`: the pin is real. The hook plane with scope `Dcos`
  blocked before any guard ran ("scope resolves to nothing"), which is QS2's premise that the
  floor never hands the reader a missing directory.
- **QS3 — untouched.**
- **QS4 — CONFIRMED, minor unchanged.** M7 green on all four files run whole against an
  all-green baseline and a 2032-green suite; no test the sandbox could not run catches it.
- **QS5, QS6 — untouched.**
- **QS7 — CONFIRMED as a note.** M9 reds five tests in `test_leakscan.py`, including the
  absolute-path pin the sandbox could not run; the first caller's code is pinned, the two
  discards remain unpinned, as the finding says.
- **QS8 — untouched.**
- **QS9 — CONFIRMED, grounds changed, note unchanged.** The 3.9 incompatibilities reproduce
  under `/usr/bin/python3` (7 + 9 errors) and vanish under the `python3` the hook actually
  resolves here (3.14.6). "Every scanner ran on 3.9 in this pass" was the sandbox, not the
  hook. CI's 3.12 is live-verified. The signing half is moot on the laptop (QU-a) and stands
  as a portability point for a host with a different signing config.
- **QS10, QS11 — untouched.**

### New findings

**QU1 — note.** The three per-guard `StagedPositionalScope` classes do not pin the exact-file
positional: dropping `or path in norm` (M6) reds only `test_report.py`'s unit test and leaves
`test_leakscan.py`, `test_secretscan.py` and `test_conflictscan.py` green. With QS4 (the prefix
boundary pinned nowhere), each guard copy pins five rows of the reader's contract and not the
two that distinguish a file from a directory prefix. The suite still reds, so a break is caught;
the copies overclaim by their near-identity. *Counsel:* either a file-positional row and a
`docs-extra` row in each copy (with QS4's fixture), or shrink the copies to one wiring smoke per
guard and let `test_report.py` be the one home.

**QU2 — note, outside the delta.** The ci plane at HEAD carries three warn-only findings, none
on a delta path: one `pathscan` missing-path in
`docs/decisions/2026-10-03-0641-the-exception-register.md` and two `pointerscan` queue-state
findings on the `160/950` and `160/970` pointers. The `950`
one is this pass's own pointer; when the top-up lands, its state glyph comes off per the
scanner's message, or the pass is recorded under the pointer's own rule. Recorded so the
orchestrator meets it before the fold, not as a defect in the reader.

### Standing checklist

- **V1** — The API ledger's attributions (signing, the denied `stat`, 3.9) were each re-driven
  and hold; the one claim stronger than its evidence is "each caught" for M6, which is caught in
  one file (QU1).
- **V2** — Re-ran: the four delta files, the full suite (summary read), both floor planes with
  the real term list, nine mutations whole, QS1 at a real `git commit`, CI's Python live.
- **V3, V4** — No mirror-site or one-home question among the missing checks; discharged.
- **V5** — QS2's contradiction re-driven (M5; the `Dcos` block). No new contradiction.
- **V6** — `/security-review` discharged with grounds (QU-g); hand read done; nothing planted
  reads as live (the floor at HEAD is green over the test files with the real term list).
- **V7** — Provenance stated in the brief and repeated above.

### Overall line (original plus top-up)

**PASS-WITH-FINDINGS** — 1 MAJOR · 2 MODERATE · 3 minor · 7 notes (QS1–QS11, QU1–QU2). No
severity changed; no API finding refuted; QS1 now stands on a real commit at the real gate.

### TOP-UP SUFFICES or FULL RE-RUN

**TOP-UP SUFFICES.** Against the principal's bar — a comparable quality outcome to a laptop
run — the reasons:

1. Every sandbox limit that sat under a finding or the verdict has been re-driven on the
   laptop, and each attribution held: the four files are green, the suite is 2032 OK, the floor
   is green with the real term list, signing works, and the 3.9 errors are 3.9's.
2. The limits reached no judgement beyond the listed checks. The 45-spelling table, the lens
   work and the child probe were local process runs the sandbox did not constrain, and the two
   findings that rest on the table (QS1, QS3) reproduce here — QS1 at the real gate, which is
   stronger than the API pass could reach. The one place a limit shaped a judgement is QS4's
   `-k`-narrowed mutation baseline; run whole, the answer is the same, plus one note (QU1).
3. Truncation cut only the suite summary, now read. The empty term list changed nothing the
   verdict rests on: the floor rows are the same both ways.
4. What remains unrun, `/security-review`, is unreachable from both harness shapes for the same
   structural reason (it reads the session's pending diff), so a full re-run would not add it.

Residual, stated: a laptop re-run would re-derive the same findings from unchanged code; its
one advantage, a reviewer that saw a green baseline while choosing what to probe, is the
judgement the API pass made with its limits named rather than hidden, and the probes it chose
are the ones a green baseline would have led to.

### Re-run ledger

| command | result |
|---|---|
| `git log --oneline 0a2b7a7..HEAD -- tools/ .githooks/ .github/` | nothing: code unchanged |
| `command -v python3` · `python3 --version` · `/usr/bin/python3 --version` · `zsh -l -c` | 3.14.6 (python.org, shell and login shell); system 3.9.6 |
| throwaway commit, scratch repo, host signing config | exit 0, good SSH signature, 1 `gpgsig` |
| `/usr/bin/python3 -m unittest … test_report/test_leakscan/test_allowmarker` (clone) | 71 OK; 219 run 7 errors (`contextlib.chdir`); 31 run 9 errors (`write_text(newline=)`) |
| `python3 -m unittest discover -s tools -p test_<x>.py` × 4, worktree root | 71 / 219 / 174 / 56, all OK, exit 0 (load 6.3) |
| `nice -n 10 python3 -m unittest discover -s tools` → file | `Ran 2032 tests in 442.217s`, OK, exit 0 (load 5.7 → 4.8) |
| `git clone -q <worktree> <scratch>/clone`; sibling removed unread; four files | 71 / 219 / 174 / 56, all OK |
| nine mutations on the clone, four files whole, `nice -n 10` | table under QU-d (load 4.1 → 4.8) |
| hook-probe repo: six real `git commit`s + controls | table under QU-e; probe commits B, C and the conflict-marker commit landed with exit 0 |
| `floor.py --plane ci` / `--plane hook` on the probe, scope `Docs` then `Dcos` | ci `Docs`: exit 1, secretscan 1 finding in tree mode; ci and hook `Dcos`: exit 1, "scope resolves to nothing" |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` (worktree) | exit 0, 25 s; warn-only: pathscan 1, pointerscan 2 (QU2) |
| `python3 tools/floor.py --plane hook --root .` (worktree) | exit 0; staged set empty |
| `gh run list --repo mike548141/atelier -L 5`; `gh run view 41310941147 --log` | floor on `main`; CPython 3.12.15 on `ubuntu-latest` |
| `/security-review` | not run; discharged with grounds (QU-g) |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] QS1 — unchanged ask; add the narrower true statement for `floor.py` 1809–1819 (shut on
      ci and case-sensitive filesystems; open on the hook plane where the filesystem folds).
- [ ] QS4 + QU1 — one fixture set pinning the prefix boundary and the exact-file match in the
      per-guard copies, or shrink the copies to a wiring smoke each.
- [ ] QS9 — the hook promises "Python 3, stdlib only" with no floor; either state 3.11+ for the
      suite or restore 3.9 in the two tests; the signing-config point stands for other hosts.
- [ ] QU2 — orchestrator: the `950` pointer's state glyph when this top-up lands; the `970`
      pointer and the 2026-10-03 decision record's stale path are other items'.

Tally: original 11 findings (QS1–QS11) plus 2 top-up notes (QU1–QU2) — 1 MAJOR, 2 MODERATE,
3 minor, 7 notes. Overall PASS-WITH-FINDINGS. TOP-UP SUFFICES.

ACT 1 SAVED

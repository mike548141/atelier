# Cold pass — the `pre-merge-commit` hook, the repo-local seam documentation, and the five content scanners reading the staged index

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is
doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RUN, act 1 appended 2026-11-15 UTC by a Fable 5.1 reviewer spawned by a headless
Opus 5.5 orchestrator of drain session `21a271a5`, under the principal's weekly Fable drain order.
PASS-WITH-FINDINGS, 0 MAJOR · 3 MODERATE · 3 minor · 4 notes; act 1 committed `8df76523`. Act 2
(reconcile against the sibling, the intent records and the commit bodies) appended 2026-11-15 UTC;
the overall line is unchanged. The sibling is folded in below the reconcile by
the orchestrator, 2026-11-15 UTC. Brief written 2026-11-09 UTC by session `d4a0fcf3`, a headless
Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/998-rule-4-cold-pass-queued-merge-hook-and-staged-content-scanners.md`.
**Size of this pass:** large: four commits across the hook plane, five scanners and `GUARDS.md`,
about 1,500 lines with tests, reaching every child.
**Why it earns a review:** The merge hook and the five scanners reach every child's hook plane and
next CI run, and `GUARDS.md` gained a section. The worst failure is a commit the hook plane is
believed to have read that it did not, or a blocking scan that now passes content it used to stop.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Sonnet worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
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
  account; every delta commit body-free through `tools/coldsweep.py --commit`; commit subjects
  through `git log`; `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole,
  **including that pass's verdict and folded sibling** (a different subject, read for house form),
  the acceptance-test section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

No record the brief-writer read carries a ruling of the principal's on these designs. Judge them
against `docs/method/GUARDS.md` § *Which commits the hook plane reaches* (in the delta, so also a
claim) and the floor's `board` rationale for the staged read (`010/020`, cited in `tools/floor.py`).

## What the work is

- **`b5e6ead`** — `hooks: ship a pre-merge-commit hook so a clean merge runs the hook plane
  (115/340)`.
- **`625f29a`** — `docs: document the repo-local check seam in the README and the hook sample
  (320/560)`.
- **`7673da1`** — `spellscan, wrapscan: read the staged index at the hook, not the disk (320/600
  slice 1)`.
- **`38bdcb1`** — `datescan, reviewscan, sizescan: read the staged index at the hook (320/600 slice
  2)`.

Delta paths, read at each commit and at HEAD:

- `tools/pre-merge-commit.sample`, `.githooks/pre-merge-commit`, `.githooks/pre-commit`,
  `tools/pre-commit.sample`, `tools/test_precommit.py`, `tools/report.py`, `tools/spellscan.py`,
  `tools/test_spellscan.py`, `tools/wrapscan.py`, `tools/test_wrapscan.py`, `tools/datescan.py`,
  `tools/test_datescan.py`, `tools/reviewscan.py`, `tools/test_reviewscan.py`, `tools/sizescan.py`,
  `tools/test_sizescan.py`, `tools/floor.py`, `tools/README.md`, `docs/method/GUARDS.md`,
  `commands/install-hook.md`, `skills/create-repo/SKILL.md`, `CHANGELOG.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 38bdcb1 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path tools/pre-merge-commit.sample --path \
  .githooks/pre-merge-commit --path .githooks/pre-commit --path tools/pre-commit.sample --path \
  tools/test_precommit.py --path tools/report.py --path tools/spellscan.py --path \
  tools/test_spellscan.py --path tools/wrapscan.py --path tools/test_wrapscan.py --path \
  tools/datescan.py --path tools/test_datescan.py --path tools/reviewscan.py --path \
  tools/test_reviewscan.py --path tools/sizescan.py --path tools/test_sizescan.py --path \
  tools/floor.py --path tools/README.md --path docs/method/GUARDS.md --path commands/install-hook.md \
  --path skills/create-repo/SKILL.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 38bdcb1..HEAD -- tools/pre-merge-commit.sample
.githooks/pre-merge-commit .githooks/pre-commit tools/pre-commit.sample tools/test_precommit.py
tools/report.py tools/spellscan.py tools/test_spellscan.py tools/wrapscan.py tools/test_wrapscan.py
tools/datescan.py tools/test_datescan.py tools/reviewscan.py tools/test_reviewscan.py
tools/sizescan.py tools/test_sizescan.py tools/floor.py tools/README.md docs/method/GUARDS.md
commands/install-hook.md skills/create-repo/SKILL.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "A clean `git merge --no-ff` makes the merge commit without ever calling" `pre-commit`; git calls
  `pre-merge-commit` there "with the merged result staged" (measured on git 2.50.1).
- "Run it by `sh` so a lost execute bit on the sibling cannot turn into a skip"; the hook fails
  closed when `pre-commit` is absent.
- Cherry-pick, revert and rebase "have no client-side hook that can refuse the commits they write";
  those are "checked by CI only".
- `staged_blob` "inherits the environment on purpose" and a failed read "is a broken scan (exit 2)",
  "never an empty and therefore clean one".
- `reviewscan` and `sizescan` judge the file whole, including "a deletion-only edit"; `spellscan`,
  `wrapscan` and `datescan` report only added lines.
- The advisory form stays whole-tree; CI keeps the whole-tree read.
- `tools/README.md` and the hook samples now name the `local` seam.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** `board`, `secretscan`, `leakscan`, `conflictscan`, `publishscan` and `harvestscan`'s
staged reads, reviewed earlier; the later staged-reader work `6467729` (`160/950`) and `ea8de0f`,
except as they bear on HEAD.

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
cd tools && python3 -m unittest test_precommit
python3 -m unittest discover -s tools -p test_spellscan.py
python3 -m unittest discover -s tools -p test_wrapscan.py
python3 -m unittest discover -s tools -p test_datescan.py
python3 -m unittest discover -s tools -p test_reviewscan.py
python3 -m unittest discover -s tools -p test_sizescan.py
python3 tools/floor.py --plane hook --root .
nice -n 10 python3 -m unittest discover -s tools
```

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
`docs/reviews/2026-11-09-0207-merge-hook-staged-scanners-cold.deferred.md` (a held-back file; by
count: 8 questions, 2 facts; now folded in below the verdict and removed), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/340-merges-cherry-picks-and-rebases-skip-the-hook-plane.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/560-the-repo-local-check-seam-is-absent-from-the-readme-and-method-docs.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/600-the-hook-plane-content-scanners-read-the-working-tree-not-the-staged-index.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/340-merges-cherry-picks-and-rebases-skip-the-hook-plane.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/560-the-repo-local-check-seam-is-absent-from-the-readme-and-method-docs.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/600-the-hook-plane-content-scanners-read-the-working-tree-not-the-staged-index.md \
  'pre-merge-commit|staged_blob|staged_added_by_path|staged_paths|--staged'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`HS`: `HS1`, `HS2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict (act 1) — 2026-11-15 UTC

### Provenance

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. A fresh session started for this pass alone.
- **How spawned:** by a headless Opus 5.5 orchestrator session, itself started by drain session
  `21a271a5` (Opus 5.5) under the principal's weekly Fable drain order (`/fable-drain`,
  2026-11-15T17:53Z). Both are rule-4 off-tier orchestrators, disclosed: they hold the context
  partition, commit the records, form no finding and write no severity. Neither wrote the brief or
  any of the delta. I was not started or instructed by `d4a0fcf3`, `74f2b8cd` or author session
  `4c65083c`.
- **Orchestrator direction, process only** (condensed from the spawn prompt; it carried no question
  about the delta, no pointer to where risk lives, and no request to revise a finding): the item
  and brief paths; my worktree; the finding prefix `HS`; "read the brief in full first and follow
  it exactly"; the partition ("the `.deferred.md` sibling has been removed from the worktree on
  purpose ... do not look for it in git history, other checkouts, scratchpads or tmp. It will be
  released to you by message after act 1 is committed"); what I may write (this file and a review
  log outside the repo); no commit, push or `git add`; read-only live systems; load rules (`nice`,
  one suite at a time); public-repo wording rules; "do not ask questions; take sensible defaults
  and record them"; and the act-1 / act-2 shape with the orchestrator doing the fold.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-998-1937/atelier`, HEAD
  `41c29978`; `git merge-base --is-ancestor 38bdcb1 HEAD` exit 0. The only working-tree change
  is the sibling's deletion (the partition). Read-only to me except this file.
- **Review log (open by design):** `~/.claude/fable-drain/notes/atelier-160-998-1937.md`, every
  check, probe and mutation with its evidence.
- **What I read:** this brief whole; `docs/method/REVIEW.md` whole; the four delta commits
  body-free through `tools/coldsweep.py --commit` with the brief's `--path` list (exit 0 each;
  board files left out); the per-file history since `38bdcb1` and the HEAD text of `tools/report.py`
  (staged helpers), the five scanners' staged branches, `tools/floor.py` (Scanner, `_load_local`,
  the runner, the hook entries), both hooks and samples, `tools/filewalk.py` lines 95–110,
  `docs/method/GUARDS.md` § *Which commits the hook plane reaches*, `tools/README.md` (`local`,
  the five scanners' sections), `docs/build/REPO-STANDARD.md` (grep), `CHANGELOG.md` lines
  1665–1790, `.atelier-floor.json`, `tools/test_floor.py` lines 1487–1491; the brief's `coldsweep`
  sweep (343 hits over 678 files, 742 barred files excluded) — its single-line hits included lines
  of non-barred board items (`010/020`, `010/110`, `020/160`, `115/080`, `115/350`, `115/360`,
  `260/110`, `320/050`, `320/060`, `320/290`, `320/340`, `320/440`, `320/630`, `320/790`), read no
  further and none an account of this delta; the hook-plane floor run's output (no barred path
  named). **Not opened:** `docs/SESSIONS.md`, `docs/sessions/`, any prior verdict, the sibling, the
  barred board items, any delta commit's message body. The harness loaded user-level and repo
  instruction files and a memory index that hold private context this verdict does not carry.
  Tool versions: git 2.50.1 (Apple Git-155); `python3` first on `PATH` = CPython 3.14.6.
- **`/security-review`:** NOT RUN, discharged by grounds: the delta is landed (nothing pending),
  and the tree carries the sibling's deletion by design, so the scanner would read this brief.
  The code-altitude read was done by hand (lens 4).

### Load-bearing assumptions, named first and tested

- **A1 — git runs a hook from the worktree root with the index the commit will carry in its
  environment, and the scanners read that.** Confirmed. Probe G in a scratch child with the tracked
  hooks and `hooks.atelierTools` pointing at this worktree's tools: `git commit -a` with a US
  spelling only on disk (`GIT_INDEX_FILE=…/index.lock`) BLOCKED; `git commit -o docs/a.md`
  (`next-index-*.lock`) BLOCKED; an unstaged draft beside a clean commit did NOT block. Probe I:
  under a temporary index holding the defect, the shipped `spellscan --staged` exits 1.
- **A2 — at `pre-merge-commit` the index is the merged result and `diff --cached` against HEAD
  yields the other branch's lines.** Confirmed: a `--no-ff` merge of a `--no-verify` side branch
  carrying a US spelling under `docs/` was BLOCKED by spellscan through the merge hook; HEAD
  unmoved (probe G4). With the sibling `pre-commit` at mode 644 the merge was still scanned and
  blocked (G5a); a plain `git commit` with a 644 `pre-commit` is skipped by git with a hint (X).
- **A3 — the GUARDS table is a fact about git, measured.** Partly false: see HS1 (probe A).
- **A4 — added-line filtering over a whole-file fence read is the right unit for the three line
  scanners; the whole staged file is the right unit for `reviewscan` and `sizescan`.** Confirmed
  by the delta's tests re-run and by the live probes; one edge noted (HS9).
- **A5 — "what this commit is about to make true" is the index.** True for content, false for
  policy: ignore globs are read from the working tree (probe E) — HS4.
- **A6 — the five staged readers share the hardened plumbing the earlier-reviewed staged guards
  have at HEAD.** False: HS2, HS3.
- **A7 — the merge hook reaches every child.** It reaches new installs (`create-repo`,
  `/atelier:install-hook`); an existing child copies it by hand and nothing reports one that has
  not. The CHANGELOG says so plainly, so this is a follow-up, not a finding (see checklist).

### Per-lens answers

1. **Approach and assumptions.** Right problem, right altitude. A transport-only merge hook that
   fails closed and hands over to the registry is the smallest shape that closes the clean-merge
   gap; a `post-merge` warning could not refuse. Reading the index at the hook follows the `board`
   rationale (`010/020`) and the brief's acceptance test. The non-goals fence off no risk. The
   claims are mostly true; the one stamped "measured" is wrong in two cells (HS1).
2. **Correctness and quality.** Every re-run line green (ledger). The staged read is correct on
   the hook plane, including partial and `-a` commits. Two hand-run paths fail open (HS2, HS3);
   neither reaches the hook, where git fixes the cwd and `--root`.
3. **Completeness and harvest.** Mirror sites swept (V3). The hook-reach fact is restated in four
   places (HS1). `filewalk.py` is stale (HS6). Four mutations of a scratch copy left the delta's
   tests green (HS5). `floorfleet` does not report a child without the merge hook (disclosed).
4. **Security and privacy.** Design altitude: the staged read narrows what the hook reads to the
   commit's own content, a privacy gain; the merge hook adds no new trust (same `hooks.atelierTools`
   class, trust note present). The one design weakness is policy read from disk (HS4). Code
   altitude, by hand against the OWASP ASVS classes for a local tool: no shell anywhere (`argv`
   lists in the hook's runner, `staged_blob`, `staged_paths`); paths come from git's `-z` output and
   are used only as index specs and dict keys, and the `:0:` prefix neutralises a dash-leading
   name; `local.run` is checked inside the repo lexically and resolved; reads are streamed and
   bounded; the hook output prints offending lines as before (no new exposure); no personal data
   handled. `/security-review` discharged above.

### Standing checklist

- **V1** — HS1 (a "measured" table wrong in two cells), HS4 (the index claim does not cover the
  rules applied). "Fail closed" claims confirmed (G, X). "Net effect on a green child: none can
  turn red" holds: what blocks now was CI-red before.
- **V2** — re-run ledger below; every line reproduced.
- **V3** — swept: CHANGELOG (three entries present and candid), `create-repo` SKILL, `install-hook`,
  README, hook samples, GUARDS, REPO-STANDARD (`local` bullet at line 132). Stale: `filewalk.py`
  (HS6).
- **V4** — the hook-reach fact has four homes (HS1, counsel).
- **V5** — HS2 and HS3 (the staged readers disagree at HEAD on cwd and pins); HS6. Cross-references
  checked for the rule reached: README `local` → `floor.py` docstring § *The repo-local seam*
  (holds it) and REPO-STANDARD (holds it); sample and README → GUARDS § (holds it).
- **V6** — lens 4 above; `/security-review` discharged with grounds.
- **V7** — provenance in the brief and repeated here.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `b5e6ead` hooks: pre-merge-commit | yes | HS1 (sample header restates), HS5 (M3) |
| `625f29a` docs: local seam | yes | none; claims re-driven: no shell, collision, missing, planes |
| `7673da1` spellscan, wrapscan staged | yes | HS2, HS4, HS5 (M1) |
| `38bdcb1` datescan, reviewscan, sizescan staged | yes | HS2, HS3, HS5 (M2, M4), HS6 (made stale) |

### Findings

**HS1 — MODERATE.** `GUARDS.md` § *Which commits the hook plane reaches*, stamped "Measured on git
2.50.1", is wrong in two cells and silent on the route that most often lands unread commits. On
git 2.50.1 (probe A, marker hooks, each re-verified with visible output): `git cherry-pick
--continue` after a hand-resolved conflict RUNS `pre-commit` and can be refused; `git rebase -i`
with `reword` RUNS `pre-commit`; `git rebase --continue` after a hand-resolved conflict does not
(the table is right there); plain `cherry-pick`, `cherry-pick -e`, `revert` (with and without the
editor) and a clean `rebase` do not. Not in the table at all: `git merge --ff-only` (and so
`git pull`) and `git am` make or move onto commits no local plane read; `am` has `pre-applypatch`,
which can refuse and which atelier does not ship. The section's purpose is to tell a designer
where a hook-only check does not reach; the fast-forward omission is the material one. The same
fact is restated in `tools/pre-merge-commit.sample`, `tools/README.md` § *Merges* and the
CHANGELOG (V4). *Counsel:* correct the table from the probe (split the last row into
`cherry-pick` / `revert` / `rebase` with the `--continue` and `reword` cells stated), add rows for
`merge --ff` / `pull` and `am`, and make the sample and README point at the section instead of
restating it.

**HS2 — MODERATE.** The five `--staged` readers do not call `report.refuse_other_repo` (the QS3
guard, `160/950`), which `secretscan`, `leakscan`, `conflictscan` and `attribscan` call at HEAD.
Probe F, cwd in this worktree, `--root` a scratch repo with a staged US spelling / a record with no
review line / a roadmap with a completed item: `spellscan`, `wrapscan`, `datescan`, `reviewscan`
and `sizescan --check` all exit 0 "clean" (they read this cwd's empty index under the other
repo's rules); `secretscan --staged --root <same>` exits 2 with the refusal. The hook plane is
unaffected: git runs hooks from the top level and `--root` is that same directory. The brief's
non-goal names `160/950` "except as it bears on HEAD"; this is that bearing (V5). *Counsel:* the
one-line call the other four make, in each `--staged` branch, plus a test.

**HS3 — MODERATE.** `report.staged_paths` (new in `38bdcb1`) lacks the pins `STAGED_DIFF_CMD`
gained in `160/800` (`--no-relative`; `_diff_env()`), and filters `ACMR` where the diff reader
filters `ACMRT`. Probe D with `diff.relative=true`: from the repo root both whole-file scanners
block as they should; from a subdirectory, `reviewscan --staged` exits 0 ("not in scope … scanned
nothing") over a staged record with NO review line, because git listed `decisions/…` relative to
the cwd and `staged_kind` saw no `docs/` parent; `sizescan` exits 2 (`cat-file :0:ROADMAP.md`
fails: fail closed); `spellscan`, whose reader is pinned, exits 1. The delta's own claim is "a
failed read is a broken scan (exit 2), never an empty and therefore clean one"; reviewscan's path
here is the empty-and-clean case. Hook plane unaffected (root cwd). *Counsel:* give `staged_paths`
the same pins and env as `STAGED_DIFF_CMD` (one shared tuple), decide `T` deliberately, and add
the subdirectory case to `test_reviewscan`.

**HS4 — minor.** In `--staged` mode content comes from the index but exemption policy comes from
the working tree: `load_ignore_globs(root)` reads `.spellscanignore` (and the siblings) from disk,
and `.atelier-floor.json` is read from disk by the floor. Probe E: a staged US spelling under
`docs/frozen/` exits 1 with no ignore file (E1); exits 0 with a reasoned `.spellscanignore` written
on disk and left untracked (E2, "1 file(s) by .spellscanignore"), so the hook passes a commit that
will not carry the file that exempted it and CI reds; with the ignore file staged but deleted from
disk it exits 1 (E3). Class-wide (the earlier-reviewed guards read their ignore files from disk
too) and recoverable at CI, but unstated: the delta's docstrings and README say the hook judges
"what this commit is about to make true". *Counsel:* one sentence in `tools/README.md` naming the
residual, or read the ignore file from the index when `--staged`.

**HS5 — minor.** Four tests that stay green on a broken delta (scratch copies of `tools/`; each
mutation shown live): **M1** `staged_blob` drops `GIT_INDEX_FILE` from its environment — the five
`StagedPlane` classes (58 tests) pass, while under a temporary index holding the defect the mutant
exits 0 and the original 1 (probe I); the delta's "inherits the environment on purpose" is
load-bearing and untested, though probe G shows the hook path is right. **M2** `staged_paths`
filters `ACM` (renames dropped) — `reviewscan`/`sizescan` `StagedPlane` pass; a `git mv` of a
record with no review line into `docs/decisions/` (R100) passes the mutant, blocks the original.
**M3** the merge hook `exec`s the sibling directly — `MergeHookTest` passes; live, a 644 sibling is
refused either way (exit 1, HEAD unmoved), the shipped `sh` form with a scanner verdict and the
mutant with a bare refusal, so the sample's rationale holds in direction and is untested. **M4**
staged `sizescan` skips the `.sizescanignore` check for archive stores — `StagedPlane` passes; a
staged `ROADMAP-DONE.md` with a live marker under a reasoned ignore glob: original 0 (suppressed
1), tree mode 0, mutant 1. *Counsel:* one test per mutation; M1 is the one that guards a claim the
delta makes.

**HS6 — minor.** `tools/filewalk.py` lines 101–102: "The three boundary guards avoid this with
`--staged`; the others do not." Stale at HEAD: the five content scanners (this delta), `attribscan`
and `board` read the index too. A stated residual that is now wrong in its second half (V5).
*Counsel:* "the hook-plane scanners that take `--staged` avoid this; `linkscan`, `pointerscan`,
`pathscan`, `indexscan`, `pdlistscan` and `licenscan` read the tree."

**HS7 — note.** In `--staged` mode the default scope is every staged Markdown file; in tree mode it
is `docs/` when present. The floor passes `{scope}` so the planes agree at the hook; by hand they
differ, as `--help` says. Recorded, not raised.

**HS8 — note.** `sizescan` takes directory parts relative to the repo root in staged mode and to
the walk base in tree mode, so under a narrow scope such as `docs/sessions` a `ROADMAP.md` there is
skipped at the hook and judged on CI. The docstring names it. Recorded, not raised.

**HS9 — note.** A file renamed into scope with small edits shows only its edited lines as added, so
a defect it already carried passes the three line scanners at the hook and is CI's. Consistent
with the delta's stated rule; recorded for the reader deciding what the hook covers.

**HS10 — note.** The hook-plane floor run printed a `pathscan` warning on
`docs/method/EVIDENCE.md:431` (a missing `docs/PRINCIPLES.md`), unrelated to this delta, and the
coverage line "0 line(s) read — scanned nothing" for a header-only `sizescan` read appears in tree
mode too (the `115/130` coverage line, out of scope). Neither is this delta's.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 3 MODERATE (HS1, HS2, HS3) · 3 minor (HS4, HS5, HS6) · 4 notes
(HS7–HS10). No finding touches the hook plane's live behaviour, which the probes confirm end to
end; the MODERATE findings are a doctrine table stamped "measured" that is partly wrong, and two
hand-run fail-open paths where the five readers lag the hardening the other staged guards received
after this delta landed. All findings are the principal's to decide (rule 3); nothing applied.

### Re-run ledger

All from the worktree root unless stated, with the `python3` first on `PATH` (CPython 3.14.6),
under `nice -n 10`, one at a time, exit codes read explicitly. `uptime` load 14.1 at start,
4.4–10 during the runs.

1. `cd tools && python3 -m unittest test_precommit` — Ran 30, OK, exit 0 (99.8 s).
2. `python3 -m unittest discover -s tools -p test_spellscan.py` — OK, exit 0.
3. `… -p test_wrapscan.py` — Ran 71, OK, exit 0.
4. `… -p test_datescan.py` — Ran 100, OK, exit 0.
5. `… -p test_reviewscan.py` — Ran 70, OK, exit 0.
6. `… -p test_sizescan.py` — Ran 117, OK, exit 0.
7. `python3 tools/floor.py --plane hook --root .` — exit 0; every check clean or not in scope,
   one `pathscan` warning (HS10); no barred path named in its output.
8. `nice -n 10 python3 -m unittest discover -s tools` — Ran 3134, OK, exit 0 (1148.9 s, two
   other sessions' suites running alongside).

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] HS1: correct the GUARDS table from the probe; add the fast-forward / `pull` / `am` rows;
      make the sample and README point at it.
- [ ] HS2: `refuse_other_repo` in the five `--staged` branches, with a test.
- [ ] HS3: pin `staged_paths` as `STAGED_DIFF_CMD` is pinned; decide `T`; subdirectory test.
- [ ] HS4: state the disk-policy residual, or read ignore files from the index when staged.
- [ ] HS5: four tests (M1 first).
- [ ] HS6: one sentence in `filewalk.py`.
- [ ] Follow-up, not a finding: `floorfleet` reporting a child whose hook plane lacks
      `pre-merge-commit` (the CHANGELOG already names the gap).
- [ ] Owed ask: none. Default taken: findings recorded only, per rule 3.

### Reconcile (act 2) — 2026-11-15 UTC

Act 1 was committed unrevised as `8df76523` before anything below was opened. Opened for act 2:
the sibling (released by the orchestrator's message naming its held path), the three intent
records and the `160/998` item whole, the four commit bodies, the bearing lines of the two prior
verdicts the sibling names (`2026-10-26-0912` and `2026-10-28-1255`, the staged-positional-reader
passes) and the session-store lines on the three items. No act-1 text is revised. No finding was
formed at reconcile.

**Against the sibling's eight questions.**

1. *`$0` through a symlink, a worktree `core.hooksPath`, a relative path; the tracked hook's mode.*
   Git invokes a hook by the path it resolved, so `dirname "$0"` is the hooks directory whether
   `core.hooksPath` is relative (`MergeHookTest`, `.githooks`) or absolute (probe G, which used
   an absolute path); `create-repo` absolutises it for worktrees. Both tracked hooks are mode 755
   and byte-equal to their samples (checked). A hook reached through a symlink was NOT probed.
2. *Installation reach and the population.* A7 and the follow-up checklist: new installs get it,
   an existing child copies it by hand, nothing reports one without it. The intent record's close
   says step 3 was "deliberately left" and why (a new `floorfleet` column reds every green child).
   The population was not measured: child repos are read-only to this pass and reported by count
   only, and I opened none.
3. *Fast-forward, `--no-commit`, octopus.* Fast-forward probed: nothing runs, and HS1 asks for the
   row. `--no-commit` and an octopus merge were NOT probed; by git's own hook contract
   `pre-merge-commit` does not run under `--no-commit` (the later `git commit` runs `pre-commit`),
   which the table could state alongside the fast-forward row.
4. *Fence state from the index; `git add -p`.* The whole index blob is read (`staged_blob`), so the
   fence state is the index copy's; `test_fence_context_comes_from_the_whole_staged_file` pins it
   and I re-ran it. `git add -p` produces an index that differs from both HEAD and the disk, and
   `--cached` line numbers are the index copy's by construction; the probe-I temporary index is the
   same shape. Not separately driven with `-p`.
5. *`ACMR`.* A rename with no content change is listed as `R` and judged (the M2 mutant shows the
   rule is live and untested, HS5). A mode-only change lists as `M` under `--name-only` and is
   judged whole. `T` is excluded where the diff reader includes it (HS3). A deleted record (`D`) is
   not judged on either plane: its absence is not a missing review line, and CI's tree read cannot
   see it either; consistent with the design, recorded.
6. *Hook-time growth.* Not measured. The cost is one `git cat-file` per staged file that is in a
   scanner's scope and class (Markdown under `docs/` for three; records, briefs, roadmaps and
   archive stores for two), not five per commit; untouched files are no longer read at all, which
   is a saving over the tree read. Probe G's whole-floor hook runs took seconds under load 10.
7. *A narrowing, ruled, CI-covered.* It is a narrowing: a defect already in a touched file no
   longer blocks at the hook. The intent record left the remedy to atelier and the author decided
   it (the body calls it a judged choice); no principal's ruling is recorded, and none was
   required by the record. CI covers it: the five `ci=` registry forms are whole-tree and
   unchanged (read in `floor.py`). HS9 records the one edge (a rename into scope). Nothing to add.
8. *`staged_blob`'s `finally` on an early stop.* Probe B and the finalisation check: a 2.4 MB
   header-only read exits 0 with empty stderr, and `gc.collect()` under `-X dev` printed nothing.
   `reviewscan` drains its stream explicitly. The author's body says the header-only read "closes
   it cleanly"; my reading of the generator-close path had expected a swallowed
   `CalledProcessError`, and the live result shows none. Consistent with the account; the
   mechanism is not stated in the code and I did not pin it further.

**Against the sibling's facts.** The system Python 3.9.6 import failure (`str | None` at module
level) was not re-driven: the brief fixes the interpreter to the first `python3` on `PATH`, 3.14.6,
and the hook's own guard requires only that some `python3` exist. Recorded as a residual outside
this delta. `staged_blob`'s reuse by `secretscan`'s body exemption (`160/1030`) is consistent
with "one shared helper, not a third private copy" in the `7673da1` body; HS2 and HS3 sit in the
callers and in `staged_paths`, not in `staged_blob`.

**Against the brief-writer's re-run results.** Every line it ran passed then and passes at HEAD;
the counts grew with the later landings (`test_precommit` 23 → 30, the full suite 2,643 → 3,134).

**Against the author's account (the four bodies and the intent records).**

- HS1: the intent record's own measurements (2026-10-16 and the 2026-10-17 addendum) covered plain
  `cherry-pick`, `rebase`, `revert` and `rebase --continue`, and the GUARDS row generalised from
  them to "including `rebase --continue`" and to every form of `cherry-pick`; `cherry-pick
  --continue` and `reword` were never measured. The addendum's point that a hand-resolved rebase
  lands unhooked stands and is the row's true cell. HS1 stands as written.
- HS2 and HS3: both are gaps in a later application, not errors of this author. QS3 (`--root` does
  not govern the staged diff) was found on 2026-10-26, before this delta; its remedy
  `refuse_other_repo` landed 2026-11-09 (`6467729`), and the `160/800` pins the same day
  (`ea8de0f`), both after the delta and both reaching the readers those passes named, not the
  five added here. The counsel stands; the record should say the sweep missed these callers.
- HS4: the bodies say the hook now answers "what is this commit about to make true"; the policy
  plane is unmentioned in bodies, records and docs. Stands.
- HS5: the `7673da1` body states `staged_blob` "inherits `GIT_INDEX_FILE`" as a design point; the
  tests pin neither it nor the three other mutated lines. Stands.
- HS6: the stale sentence is in a file the delta did not touch; the delta made it stale. Stands.
- The bodies' "proven through the real hook in a throwaway repo" claims reproduce (probe G), and
  "no child that was green can turn red" holds (V1 above).

**Overall line, restated:** PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (HS1, HS2, HS3) · 3 minor
(HS4, HS5, HS6) · 4 notes (HS7–HS10). Unchanged by reconcile. The sibling is folded in below by
the orchestrator.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`8df76523`); folded here
verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (a headless Claude Opus 5.5 session started by drain session `21a271a5`) formed no
finding and wrote no severity.*

### Sibling to the merge-hook-staged-scanners cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-merge-hook-staged-scanners-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `cd tools && python3 -m unittest test_precommit`: 23 tests, OK, exit 0 (Python 3.14.6).
- `python3 -m unittest discover -s tools -p test_spellscan.py`: exit 0 (Ran 87 tests).
- `python3 -m unittest discover -s tools -p test_wrapscan.py`: exit 0 (Ran 67 tests).
- `python3 -m unittest discover -s tools -p test_datescan.py`: exit 0 (Ran 96 tests).
- `python3 -m unittest discover -s tools -p test_reviewscan.py`: exit 0 (Ran 49 tests).
- `python3 -m unittest discover -s tools -p test_sizescan.py`: exit 0 (Ran 106 tests).
- `python3 tools/floor.py --plane hook --root .`: exit 0 (✅ licenscan enforced).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

#### Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`
- `docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.md`

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `exec sh "$hook_dir/pre-commit"`: `$0` when a hook is invoked through a symlink, a worktree's
   `core.hooksPath` or a relative path. Does `dirname "$0"` find the sibling? Does the shipped
   `.githooks/pre-merge-commit` have its mode set?
2. Installation reach: `commands/install-hook.md` copies it, but a child whose `.githooks` is
   already stamped? `floorfleet` or `create-repo`'s stamp: what is the population that has it, and
   does anything report a child without it?
3. `git merge` when the merge is fast-forward, or with `--no-commit`, or an octopus: what runs? The
   table measured one git version.
4. Added-line filter plus whole-file context for fences: does `spellscan` read the fence state from
   the index copy or the disk? Partial staging with `git add -p`: which lines are "added" and do the
   numbers map to the index copy?
5. `reviewscan` and `sizescan` whole-file on the index: `staged_paths` filter is `ACMR`. A rename
   with no content change, a mode-only change, a deletion of a file whose absence is the defect (a
   deleted ADR's review line)? `D` is excluded.
6. Hook plane runtime: five more `git cat-file` readers per commit. On a big child's hook, the
   hook-time growth?
7. A blocking scan that used to read the disk and now reads only added lines: a defect already in a
   touched file no longer blocks. Is that a narrowing, was it ruled, and does CI cover it on every
   push in every child?
8. `staged_blob`'s `finally`: `proc.stdout.close()` before `proc.wait()` on a large blob; a consumer
   that stops reading early gets a SIGPIPE rc from git, and raises for a clean read?

#### Facts held back from the brief

- `tools/test_precommit.py` fails to import on the system Python 3.9.6 here; passes on 3.14.
- `staged_blob` is the reader `secretscan`'s `--staged` body exemption later reuses (pass
  `160/1030`, whose verdict the brief-writer read).

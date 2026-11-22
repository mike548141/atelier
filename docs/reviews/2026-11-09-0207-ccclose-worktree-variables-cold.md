# Cold pass — `ccclose` resolves a shell variable in a worktree add's path, drops one it cannot, and pins the committer-date window

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine by
function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-22 UTC by a Fable 5.1 reviewer under orchestrator session
`a8755ef4` (drain session `eca14b23`, the principal's drain order of 2026-11-23 NZDT):
PASS-WITH-FINDINGS, 1 MAJOR · 1 MODERATE · 3 minor · 2 notes. Act 2 (reconcile against the
sibling) pending. Brief written 2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5
brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/993-rule-4-cold-pass-queued-ccclose-worktree-variables.md`.
**Size of this pass:** small: about 50 lines of code across two commits.
**Why it earns a review:** `ccclose`'s identifiers block is pasted into records as fact. The worst
failure is a made-up worktree path reported as evidence, or a session's real worktree dropped from
the close check with nothing saying so.

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

No record the brief-writer read carries a ruling of the principal's on this design. Judge it against
`instruments/ccclose.design.md` and `docs/method/RECORD.md` on the close evidence.

## What the work is

- **`a6dd65a`** — `ccclose: pin committer-date window membership against backdated author dates
  (210/320)`.
- **`1550874`** — `ccclose: resolve a shell variable in a worktree add's path, drop one it cannot
  (210/330)`.

Delta paths, read at each commit and at HEAD:

- `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
  `instruments/man/ccclose.1`, `CHANGELOG.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 1550874 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path instruments/ccclose --path \
  instruments/ccclose.test.js --path instruments/ccclose.design.md --path instruments/man/ccclose.1
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 1550874..HEAD -- instruments/ccclose
instruments/ccclose.test.js instruments/ccclose.design.md instruments/man/ccclose.1`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "A variable with no such assignment, or any other expansion ($(...), backticks), leaves the path
  unknown, and the add is DROPPED: a made-up path would be pasted as fact."
- An assignment that only prefixes the git command itself "is not seen by that command's own
  expansion, so it does not count either".
- Variables are read from "a literal assignment made earlier in the same command, or before it in
  the transcript".
- A commit is dated by its committer date, and "an author date set back by a history import plays no
  part".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** `03d8503` (`210/360`, pass `160/1010`) and `5f7c2b0` (`210/370`, pass `160/1020`),
except as they bear on HEAD; the scratch-folder check and the refused-delete flag (pass `160/996`).

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
`docs/reviews/2026-11-09-0207-ccclose-worktree-variables-cold.deferred.md` (a held-back file; by
count: 5 questions, 1 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/210-instruments-open-features/330-ccclose-lists-a-worktree-path-with-an-unexpanded-variable.md`
- `docs/roadmap/210-instruments-open-features/320-ccclose-misses-author-backdated-commits.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/330-ccclose-lists-a-worktree-path-with-an-unexpanded-variable.md \
  --also-exclude docs/roadmap/210-instruments-open-features/320-ccclose-misses-author-backdated-commits.md \
  'worktreeAdds|expandVars|varsBefore|inWindow'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`WT`: `WT1`, `WT2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (cold, before the sibling)

**Overall: PASS-WITH-FINDINGS** — 1 MAJOR (WT1), 1 MODERATE (WT2), 3 minor (WT3, WT4, WT5),
2 notes (WT6, WT7). The drop-not-guess half of `210/330` and the whole of `210/320` hold; the
"earlier in the transcript" half of `210/330` re-creates the made-up path it set out to remove,
on the harness this review ran on. The verdict is PASS-WITH-FINDINGS and not FAIL because the
tree at HEAD is still strictly safer than the tree before the delta (which pasted `<cwd>/$W`),
and the MAJOR is a narrowing, not a redesign. Every finding is the principal's to decide (rule
3): nothing is applied here.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Spawned by orchestrator session `a8755ef4` (Opus 5.5), itself started by drain
  session `eca14b23` (Opus 5.5), under the principal's drain order of 2026-11-23 NZDT. Both are
  off-tier orchestrators: they hold the context partition, formed no finding and wrote no
  severity; neither wrote the brief or any of the delta. The brief's barred sessions
  (`d4a0fcf3`, `74f2b8cd`, the author `4c65083c` and what it started) neither started nor
  instructed this reviewer.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-993-2223/atelier` at HEAD
  `5c8bc4399deddd2bd699cbd357f0dff9ee10d1a9`, read-only but for this file. The sibling
  `.deferred.md` was removed from the worktree by the orchestrator (the partition) and was not
  opened, searched for or recovered.
- **Day:** 2026-11-22 UTC (the machine's local day was 2026-11-23 NZDT).
- **What was read:** this brief whole; `docs/method/REVIEW.md` (rules 1–4, V1–V7, lifecycle);
  both delta commits body-free through `tools/coldsweep.py --commit … --path ×5`; the since-line
  (16 commits on the delta paths, read only where they bear on HEAD: `03d8503d`, `4e3b3984`);
  `instruments/ccclose` at HEAD lines 116, 236–292, 300–405, 520–600, 648–683, 725–765,
  860–885, 955–975, 2200–2290, 2412–2440, 2540–2562; `instruments/ccclose.test.js`
  1–175, 1140–1162, 1322–1452, 1595, 1752–1780; `instruments/ccclose.design.md` 59–64,
  668–680, 776–786; `instruments/man/ccclose.1` 60–61, 545–552, 755–768; `CHANGELOG.md`
  2213–2240;
  `instruments/README.md` 23–25; the `210/330` and `210/320` item titles only. Barred records
  stayed barred. The brief's `coldsweep` sweep was run as written (58 hits, 1005 files
  excluded; hits only in `ccclose`, its test and `CHANGELOG.md`). The orchestrator's prompt
  and the harness's own instruction files were loaded by the harness, as every session's are.
- **Work log:** kept throughout at the drain's notes path for this pass (commands, lines read,
  probe outputs); the orchestrator appends it to this file at the fold.

### Lens 1 — approach and assumptions (named first, then tested)

| # | Load-bearing assumption | Result |
|---|---|---|
| A1 | A shell variable assigned in one Bash tool call is still set in a later call, so an assignment "earlier in the transcript" is the value a later `git worktree add $W` ran with. | **Damaged → WT1.** On the harness this review ran on, a variable set and exported in one call is unset in the next; only the working directory persists. |
| A2 | The last *literal* assignment seen is the variable's value when the add runs. | **Damaged → WT2.** A later `W=$(…)`, `W=$OTHER` or `unset W` is not recorded, so the earlier literal stays in force. |
| A3 | A command's text is one flat scope: every `NAME=value` in it is a live assignment. | **Damaged → WT3** (minor). Heredoc bodies and subshells count. |
| A4 | A `tool_result` that is not an error means the add ran as parsed. | Not re-driven: inherent to a transcript reader with no git record of a put-away worktree. Noted: the integration fixtures fabricate `Preparing worktree`, which git prints whatever path it got. |
| A5 | Committer date is when the session made the commit. | Confirmed for the author-backdated case the item names (`%ct` everywhere, `--since` is committer-dated, mutation d bites). Overclaims for a command that sets `GIT_COMMITTER_DATE` → WT7 (note). |
| A6 | `210/320` is a pin, not a behaviour change. | **Confirmed.** The code diff is a three-line comment; the test is new and red on an author-date reading (mutation d). |

Right problem, right altitude: yes for the drop rule (a reader that cannot resolve a path must say
so, and `210/360` later made it count what it dropped). The cross-command rule solves a problem
the shell does not pose on this harness, and does it at the cost the brief names as the worst
failure.

### Lens 2 — correctness and quality (claims re-driven)

Probe inputs, `cc.worktreeAdds(cmd, '/r', vars)` on the worktree's own module:

| Claim (from the delta) | Probe | Result |
|---|---|---|
| "$(...), backticks … the add is DROPPED" | `W=/w/a; W=$(mktemp -d); git worktree add --detach $W` | `[{path:/w/a}]` — not dropped; the stale literal is used (WT2). Same for `W=$OTHER` and `unset W`. |
| same, across the transcript | vars `{W:/w/old}`, `W=$(mktemp -d); git worktree add --detach $W` | `[{path:/w/old}]` (WT2). |
| a prefix assignment "does not count" | `W=/w/prefix git worktree add --detach $W` | `[]` — holds. `W="a\|b" git worktree add --detach $W` → `[{path:/r/a\|b}]` (WT3, contrived). |
| "a literal assignment made earlier in the same command" | `W=/w/one && git worktree add --detach $W origin/main` | `[{path:/w/one}]` — holds. An assignment after the add is ignored — holds. |
| "or before it in the transcript" | harness: call 1 `X=v; export X; echo "[$X]"` → `[v]`; call 2 `echo "[${X:-unset}]"` → `[unset]` | The value the rule reads is not the value the shell had (WT1). |
| `cd` / `-C` with a variable | `R=/repo && git -C $R worktree add -b b rel`; `W=rel && cd /other && git worktree add -b b $W` | `/repo/rel`, `/other/rel` — both as a shell would. |
| committer date, not author date | mutation d (`%ct` → `%at` in `windowCommits`) | the new `210/320` test goes red — the claim is tested. |

Quality: the `varsBefore` snapshot (line 872) is right and its reason is stated in the comment;
`expandVars` refuses any residual `$` or backtick, so a half-expanded word never escapes; the
other adds in a command survive a dropped one. The `210/320` change is an honest pin: the
`CHANGELOG` says "pinned, not changed", and that is what the diff shows.

### Lens 3 — completeness and harvest

- **V3, mirrors:** the rule is stated in the code comment (300–312), the design note (59–64,
  668–680), the man page (60–61, 755–761) and `CHANGELOG.md`; all four say the same thing, so
  the sweep finds no drift, and WT1/WT2 apply to every one of them. `instruments/README.md`
  describes `ccclose` at summary level with nothing to mirror. `ccopen` has no worktree-add
  reader; `ccfleet`'s one `worktree add` is a command it runs, not a parse.
- **V4, one home:** the design note is the home; the man page is the user surface; the code
  comment and `CHANGELOG` are the usual copies. Discharged.
- **V5, contradiction:** WT4 (the subagent caller at 2269 does not apply the stated rule and
  discards its count), WT6 (the "same reading as message files" is not the same), WT7 (the
  design note's parenthetical says more than the man page). Cross-references: the design note's
  `210/330`, `210/320` and `210/310` point at board items whose titles state the rule reached;
  checked by title only (barred beyond it).
- **Tests that would stay green on a broken delta** (mutations on a scratch copy of
  `instruments/{ccclose,cctranscript,cclive,ccclose.test.js}`, each one edit confirmed by diff,
  run with `--test-name-pattern`):
  - a. `const varsBefore = t.msg.vars;` (a live reference, not a snapshot) → **16/16 green**.
    End to end on that copy, a transcript command `git worktree add --detach $W …; W=<p>` lists
    `<p>` as a worktree (the pristine copy drops it and counts 1 unresolved). → WT5.
  - b. drop the `[;&|\n]` prefix-assignment guard → 15/16, red where expected.
  - c. `expandVars` returns `''` for an unknown name → 12/16, four red.
  - d. `%ct` → `%at` in `windowCommits` → the `210/320` test red.

### Lens 4 — security and privacy (V6)

- **Design altitude.** The reader consumes the session's own `tool_use` command text (never a
  tool result's text, never another user's input) and emits paths into a record. Nothing new is
  collected. What it exposes is unchanged by the delta: absolute worktree paths, printed
  home-relative by `tildePath`, into a session record whose repo may be public; that is the
  record-writer's existing duty, not a new weakness here. The one design-level risk is the one
  the brief names and WT1/WT2 find: a wrong path *asserted as evidence*.
- **Code altitude** (ASVS V5 input handling, V12 files; checked by hand): expansion is string
  substitution with no `eval`, no shell; `git()` is `execFile` with `-C root` and an argument
  array; a resolved path reaches `fs.statSync`, `fs.realpathSync` and string formatting only. A
  value with shell metacharacters (probe E) is a wrong path, not an injection. `~` expands via
  `os.homedir()`. No vector found in the delta's class.
- **`/security-review`:** discharged by grounds. It reads the session's pending diff, and this
  tree is dirty with the partition's deletion and this brief, so a run would have read the
  review surface, not the delta; the code-altitude read above stands in, as the brief allows.

### V1–V7

- **V1** — WT1 and WT2 are claims stronger than their evidence (the code comment and design
  note state an unconditional rule the shell on this harness does not honour, and a DROPPED
  outcome the code does not deliver on a reassignment). WT6, WT7 are small instances.
- **V2** — both re-run lines were re-run, not read (ledger below).
- **V3** — swept; mirrors agree with each other (so they share WT1/WT2). No drift.
- **V4** — discharged: one home, the design note; copies at the usual surfaces.
- **V5** — WT4, WT6, WT7; cross-references reach the rule they cite (titles).
- **V6** — lens 4 above; no injection vector; `/security-review` discharged by grounds.
- **V7** — stated above and in the brief's own spawn-provenance section.

### Findings

**WT1 — MAJOR — The "earlier in the transcript" rule reads a variable the shell no longer
had, and lists the worktree at that value.** `readTranscript` snapshots `t.msg.vars` (872),
which `noteMessageSources` fills with every literal assignment the session ever ran (681), and
`worktreeAdds` seeds its environment from it (365). On the harness this review ran on, shell
state does not survive a Bash tool call: a variable set and exported in one call read back as
unset in the next (probe, lens 2), and the tool's own description says the same. So a session
that ran `W=/w/a` in one call and `git worktree add --detach $W origin/main` in a later one ran
git with an empty `$W` (git then adds a worktree at `<cwd>/origin/main`), while `ccclose` lists
`/w/a`, a worktree that was never made, as fact. That is the brief's named worst failure, and
the integration fixture `sess-id-13` (test file 1375–1390, records `v2`/`v3`) asserts it as
the wanted behaviour, with a fabricated non-error result. Whether an earlier harness kept a
persistent shell this review cannot say; the design note states the rule unconditionally for
every transcript. *Counsel:* honour only assignments in the same command; count a
cross-command variable as unresolved (the `210/360` line already exists to say so), unless the
harness is shown, per transcript or per version, to persist shell state. The message-file
reader (`210/310`, design note 779–782) rests on the same assumption and is outside this pass:
a follow-up item, not a finding here.

**WT2 — MODERATE — A non-literal reassignment, or `unset`, leaves the earlier literal in
force.** `assignmentsIn` records literal assignments only (`LITERAL_ASSIGN`, 544), and nothing
removes a name on `W=$(mktemp -d)`, `W=$OTHER` or `unset W`, so `W=/w/a; W=$(mktemp -d); git
worktree add --detach $W` lists `/w/a` (probes A, B, C, G). The code comment (304–306) says any
other expansion "leaves the path unknown, and the add is DROPPED"; the design note (781–782)
says the same of `S=$(mktemp -d)` for message files, which shares the machinery. The result is
an invented path (a duplicate of a real earlier worktree, or a path from an earlier call) with
no count. *Counsel:* have the assignment reader also record `NAME=<anything else>` and
`unset NAME` as *unknown* (delete the name), so the later add drops and counts.

**WT3 — minor — The assignment reader has no notion of scope.** A `NAME=value` line inside a
heredoc body (probe D: `cat > f.sh <<'EOF' … W=/evil … EOF; git worktree add --detach $W` →
`/evil`), inside a subshell (probe H), or a quoted prefix value holding `;`, `&` or `|` (probe
E) is read as a live assignment. Each needs an unusual shape, so minor; the heredoc case is the
realistic one in this estate, where scripts are written by heredoc routinely. Context, not a
delta finding: `WT_ADD` has always matched an add written *inside* a heredoc body too.
*Counsel:* blank heredoc bodies (`heredocWritesIn` already finds their bounds) and `( … )`
groups before scanning for assignments.

**WT4 — minor — The subagent caller does not apply the stated rule, and drops its count.**
`commitEvidence` (2269) calls `worktreeAdds(cmd, cwd, new Map(), { unresolved: 0 })`: the
per-subagent `ev.vars` built two lines above is not passed, and the stats object is thrown
away. So the design note's rule is applied to the parent transcript and not to its subagents'
(V5), and an add a subagent could not resolve is counted nowhere. Given WT1 the empty map is
the *safer* reading, which makes this an inconsistency to resolve in WT1's direction rather
than a hole to fill; either way, the count should not be discarded silently. The line landed
with `4e3b3984` (`160/960`), after the delta, and bears on the delta's claim at HEAD.

**WT5 — minor — The `varsBefore` snapshot is untested.** Mutation a (a live reference in
place of the snapshot) left all 16 worktree tests green, and end to end the mutated copy lists
`git worktree add --detach $W …; W=<p>` at `<p>` while the pristine copy drops and counts it.
The comment at 870–871 states the reason; no test holds it. *Counsel:* one integration case
with the assignment after the add in the same command, expecting no item and `unresolved: 1`.

**WT6 — note — "The same reading as message files" is not the same.** The message-file reader
resolves a relative literal at assignment time against the command's cwd (`envAt`, 667–671);
`worktreeAdds` carries the literal and resolves it at the add against any `cd`/`-C` (probe K:
`W=rel && cd /other && git worktree add -b b $W` → `/other/rel`), which is what a shell does.
The worktree reading is the right one; the claim of sameness (design note 672–673, code comment
302–303) overstates. *Counsel:* "a reading like the message files'", or align the other reader.

**WT7 — note — `210/320`: the design note's parenthetical says more than the code does.**
"a commit being dated by its committer date (when the session made it; …)" (design note
62–63) equates committer date with wall-clock time. A commit command that sets
`GIT_COMMITTER_DATE` (a history replay with true dates, which this repo's own practice
includes) falls outside the window silently. The man page's sentence (60–61) is exact: author
date never counts; a backdated *author* date still counts. Code and test are sound. *Counsel:*
trim the parenthetical to "the committer date, which the author date never changes".

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `a6dd65a` (`210/320`) | yes, `coldsweep --commit --path ×5` | WT7 (note); test confirmed to bite (mutation d) |
| `1550874` (`210/330`) | yes, `coldsweep --commit --path ×5` | WT1, WT2, WT3, WT5, WT6 |
| HEAD, since-line | `4e3b3984` read body-free for line 2269 only | WT4 |

### Re-run ledger

| Line | Run | Exit | Result |
|---|---|---|---|
| `node --test instruments/ccclose.test.js` | 2026-11-22T22:30Z, `nice -n 10`, foreground, load 14.70 at start | 0 | 153 tests, 153 pass, 0 fail, 365 s |
| `nice -n 10 python3 -m unittest discover -s tools` | attempt 1 at 2026-11-22T22:30Z (load 16.59) was stopped by the harness's background time limit at about 23:05Z before its summary, no failure printed; re-run whole from 23:06Z (load 7.64), background, single process; `python3` = 3.14.6, first on PATH | 0 | `Ran 3382 tests in 1260.839s` · `OK` |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] WT1: decide the cross-command rule — same-command only, or persistence proven per
      harness; the fixture `sess-id-13` changes with it. Open a follow-up for the message-file
      reader (`210/310`), which shares the assumption.
- [ ] WT2: non-literal reassignment and `unset` make a name unknown.
- [ ] WT3: scope heredoc bodies and subshells out of the assignment scan.
- [ ] WT4: one reading for parent and subagent transcripts; keep the subagent count.
- [ ] WT5: a test for the snapshot (assignment after the add, same command).
- [ ] WT6, WT7: wording in the design note and code comment.
- [ ] Reconcile (act 2) against the sibling and the commit bodies; restate the overall line.

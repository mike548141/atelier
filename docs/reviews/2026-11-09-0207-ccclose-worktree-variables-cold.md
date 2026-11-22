# Cold pass — `ccclose` resolves a shell variable in a worktree add's path, drops one it cannot, and pins the committer-date window

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine by
function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN, acts 1 and 2 written 2026-11-22 UTC by a Fable 5.1 reviewer under orchestrator
session `a8755ef4` (drain session `eca14b23`, the principal's drain order of 2026-11-23 NZDT): act 1
committed as `0129890d`, act 2 (reconcile) written 2026-11-22 UTC by the same reviewer:
PASS-WITH-FINDINGS, 1 MAJOR · 1 MODERATE · 3 minor · 3 notes (WT1–WT8). The sibling is folded below
the verdict. Brief written 2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer.
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
`docs/reviews/2026-11-09-0207-ccclose-worktree-variables-cold.deferred.md` (now folded below;
by count: 5 questions, 1 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
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

### Reconcile (act 2, 2026-11-22 UTC, after act 1 was committed as `0129890d`)

Opened at act 2: the sibling (5 questions, 1 fact, the brief-writer's re-run results), the two
intent records whole, board item `160/993` whole, both delta commit bodies, and the prior
verdicts named by the sibling or found by grep (`2026-10-17-1010`, `2026-10-26-0917`,
`2026-10-18-0506`, `2026-11-09-0126` on `210/360`, `2026-11-09-0153` on `160/960`), read for
overlap only. No act-1 text is revised. Four more unit probes were run for the sibling's
questions 3 and 4 (listed under question 3 below); one note was formed at reconcile (WT8).

**The brief-writer's re-runs against mine.** Node suite exit 0 both times (brief-writer 215 s at
`b1f9499`; this pass 365 s at HEAD, 153 tests). Python suite OK both times (brief-writer 2,643
tests in 1,167 s on 3.14.6; this pass 3,382 tests in 1,261 s on the same interpreter, after a
first attempt the harness stopped). The growth is the tree's, not a discrepancy. The 3.9.6 import
errors the sibling names were not met: `python3` first on PATH here is 3.14.6, as the brief asks.

**Per question.**

1. *A dropped add leaves the close check blind; at these two commits, does anything say so?*
   Agreed, and act 1 reads it the same way: at `1550874` a drop was silent (`worktreeAdds`
   returned `[]` and nothing counted it); `03d8503` (`210/360`, pass `160/1010`) added the count
   and the "N worktree adds not resolved" line, so at HEAD a silence is no longer possible for
   the parent transcript. No finding here at HEAD. The silence that remains is the subagent
   caller's (WT4): its count is still discarded, which the `210/360` verdict also observed in
   passing (its lens-2 text, not a numbered finding) and which act 1 numbers.
2. *The transcript-wide map is stale across a fresh shell; is a path then confidently wrong?*
   Yes: this is WT1, formed at act 1 from a live probe before the sibling was read, and the
   brief-writer's own premise ("the Bash tool does not persist env") is the same observation
   from the other side of the partition. Two independent arrivals at one defect. The commit body
   and the intent record both present the cross-command reading as the fix's design ("the
   `210/310` reading"), which confirms the flaw is shared with the message-file reader; act 1's
   follow-up on `210/310` stands. Severity unchanged: MAJOR.
3. *Subshell, `if`, `for`, pipeline, reassignment after use, `export`, quoting.* Probed at act 2,
   same harness as act 1 (`cc.worktreeAdds(cmd, '/r')`): `if false; then W=/w/if; fi; git
   worktree add --detach $W` → `/w/if` (the branch never ran); `echo x | W=/w/pipe cat; git
   worktree add --detach $W` → `/w/pipe` (a pipeline-stage prefix assignment, counted because the
   `;` after it satisfies the separator test); `export W=/w/exp && …` → `/w/exp` (correct);
   `W=/w/a && git worktree add --detach $W && W=/w/b && git worktree add --detach $W` →
   `/w/a`, `/w/b` (correct: each add sees the assignment before it). `for` is `210/360`'s and
   was reviewed there (CW1–CW8). The `if` and pipeline shapes join WT3's list (heredoc body,
   subshell, quoted prefix value); they do not change its severity: each needs the variable to
   be unset in the real shell at the add, which the same-command shapes rarely are. Where the
   brief-writer's reassignment question meets WT2 is the non-literal reassignment, which act 1
   found and the author's "last assignment wins" test does not cover (it tests two literals).
4. *`$HOME`, `~`, `${VAR:-default}`: literal or guess?* Probed: `${W:-/w/dflt}` → dropped (the
   `${NAME}` form admits a bare name only, so the residual `$` fails `expandVars`); `$HOME/wt` →
   dropped unless the transcript assigned `HOME` a literal (then that literal is used, which is
   what a shell would do too); `~/wt` → resolved through `os.homedir()` of the process running
   `ccclose`, the same user as the session on this machine. None guesses; `$HOME` is dropped
   where it could nearly always be resolved, which costs a count line, never a wrong path. No
   finding; recorded as WT8 (note, formed at reconcile).
5. *A rebase's committer date credits a rebasing session with others' commits; is that named
   beside the heuristic?* Partly. The code comment (`ccclose` 960–962) names "a rebase" beside
   the import; the design note (62–63) names only the import, and the man page (60–61) neither.
   Since `160/960`, a commit in the window is credited only on a command of the session naming
   its subject, and a rebase's recommits are otherwise printed as unconfirmed, so the heuristic
   is bounded in code; the prose understates it. This belongs with WT7 (note): its counsel widens
   to "name the rebase case on the three prose surfaces, as the code comment does".

**Against the author's account (commit bodies, intent records).**

- `1550874` body: "the way `210/310`'s message-file reader does" — WT6 stands: the two readers
  differ on a relative literal (resolve-at-assignment against the cwd versus resolve-at-use
  against `cd`/`-C`); the worktree reading is the shell's.
- `1550874` body: "last assignment wins" — true among literals only; WT2 stands.
- `1550874` body: "The transcript reader snapshots its variables before folding in each command,
  so the command's own assignments are read in order" — true, and untested; WT5 stands.
- `1550874` body and `210/330`: "A prefix assignment … is not counted: bash expands `$W` before
  the assignment applies" — correct and tested (mutation b); the quoted-value exception (WT3,
  probe E) is contrived.
- `210/330` records that on the day the real worktree still existed and was listed from `git
  worktree list`, "so nothing was lost": that is why the pre-delta defect was a wrong entry
  beside a right one. After the delta, the WT1 path has no right entry beside it once the
  worktree is put away, which is the usual state at close.
- `a6dd65a` body and `210/320`: "No behaviour change", "the premise did not hold" — confirmed by
  the diff (a comment) and by mutation d. The item's closing diagnosis (script-made commits print
  as unconfirmed) is what the new test pins. WT7 is wording only.

**Overlap with prior verdicts.** `2026-11-09-0126` (`210/360`, CW1–CW8) reviewed `loopsAround`
and the count line, and mentioned the subagent caller's discarded `stats` in its lens-2 text;
WT4 numbers that and adds the empty variable map. No CW finding covers WT1, WT2, WT3, WT5 or WT6.
`2026-11-09-0153` (`160/960`) covers the evidence tier WT4's line belongs to, not the worktree
reading. `2026-10-17-1010`, `2026-10-26-0917` and `2026-10-18-0506` predate the delta and do not
touch it. No finding-prefix collision: `WT` is unused elsewhere in `docs/reviews/`.

**Formed at reconcile.**

**WT8 — note (formed at reconcile) — `$HOME` and `${VAR:-default}` are dropped, never guessed.**
`expandVars` admits `$NAME` and `${NAME}` only, so a parameter expansion with an operator and an
environment variable the transcript never assigned both leave the add unresolved and counted.
That is the conservative side, and it is the right side; it is noted because `$HOME` is common
in this estate's commands and a session reading the "N not resolved" line should know this is
one cause. *Counsel:* none needed; a one-line mention beside the count line's explanation would
save a reader a search.

**Overall line restated: PASS-WITH-FINDINGS — 1 MAJOR (WT1), 1 MODERATE (WT2), 3 minor (WT3,
WT4, WT5), 3 notes (WT6, WT7, WT8).** The sibling's questions confirmed WT1 independently, widened
WT3 and WT7 without changing a severity, and added one note. Every finding is the principal's to
decide (rule 3); nothing is applied. The sibling is left in place for the orchestrator to fold.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `0129890d`, the hash
the reviewer's text cites; it lands on `main` under a new hash when rebased with this fold); folded
here verbatim (headings demoted two levels, no word changed; one heading line is over 100 columns as
the sibling wrote it) and the sibling file removed, per the brief. The orchestrator, headless Opus
5.5 session `a8755ef4` started by drain session `eca14b23`, held the partition, formed no finding
and wrote no severity; drain session `eca14b23` wrote no brief and no delta and started no
brief-writer for this pass.*

### Sibling to the ccclose-worktree-variables cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-ccclose-worktree-variables-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `node --test instruments/ccclose.test.js`: exit 0 (ℹ duration_ms 214628.846232).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

#### Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`
- `docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md`

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. A dropped add leaves the close check blind to a real worktree. Later `03d8503` counts the
   unresolved. At these two commits, does anything say an add was dropped? A guess is prevented, a
   silence is not.
2. The transcript-wide variable map: a variable assigned in one shell command and reused in a later
   one that ran in a fresh shell (the Bash tool does not persist env). Is the map then stale, so a
   path is confidently wrong?
3. `a.at < m.index` and the `[;&|\n]` test: an assignment inside a subshell, an `if`, a `for`, or a
   pipeline; one reassigned after use; `export`; quoting. Does any give a path that was not the one
   used?
4. `$HOME`, `~` and `${VAR:-default}` in `expandVars`: which are literal, and which guess?
5. The window: the committer date of a rebase is the rebase's. A session that only rebases others'
   commits is credited with them. Is that named beside the heuristic?

#### Facts held back from the brief

- Later commits touch the same file (`1569e64`, `3de818b`, `03d8503`, `5f7c2b0`, `457f374`,
  `4e3b398`); three are under their own passes.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels. No public-repo gate blocked a token, so no
placeholder was substituted.*

### Review log — atelier 160/993, ccclose worktree variables cold pass

Reviewer: Fable 5.1 (claude-fable-5-1). Spawned by orchestrator session a8755ef4 (Opus 5.5),
started by drain session eca14b23 (Opus 5.5). Review worktree:
/Users/mike/worktrees/fable/atelier-160-993-2223/atelier. Brief:
docs/reviews/2026-11-09-0207-ccclose-worktree-variables-cold.md.

#### Act 1

- 2026-11-22T22:24Z `uptime`: load 8.62 7.72 15.09 (several passes running). `date -u`:
  Sun Nov 22 22:24:43 UTC 2026. `git status --short`: only ` D` of the brief's `.deferred.md`
  sibling (expected partition). HEAD 5c8bc4399deddd2bd699cbd357f0dff9ee10d1a9.
- Read the brief in full (203 lines). Pass prefix WT; lenses 1–4; V1–V7; re-run lines:
  `node --test instruments/ccclose.test.js`, `nice -n 10 python3 -m unittest discover -s tools`.
  Barred until act 2: ROADMAP-DONE, SESSIONS, sessions/, prior verdicts, sibling, 160/* beyond
  title, commit bodies, 210/330 and 210/320 beyond first line.
- Read `docs/method/REVIEW.md` §§ Independence (rules 1–4), standing checklist V1–V7, lifecycle
  (verdict shape, method record).
- `git merge-base --is-ancestor 1550874 HEAD` → 0; same for a6dd65a → 0. Delta is in the tree.
- Since-line `git log --oneline 1550874..HEAD -- <4 delta paths>`: 16 commits, among them
  03d8503d (210/360 for-loops, non-goal), 5f7c2b0c (210/370), 4e3b3984 (160/960 credits a commit
  only on evidence), 457f374d, 1bc89816, e4d572d1, 20fd0f09, 54f91ad3, 1568acce (ccopen twin).
- `coldsweep --commit a6dd65a --path ×5`: body-free. 47+/2−. Code change = a 3-line comment
  on `inWindow` only (no logic change); test adds `commitBackdated` + one test (author date 90d
  back, committer in window; a scripted backdated commit prints unconfirmed); man page +2 lines;
  design note +2 lines; CHANGELOG entry says "pinned, not changed".
- `coldsweep --commit 1550874 --path ×5`: body-free. 114+/10−. `worktreeAdds(command, cwd,
  vars=new Map())`: `assignmentsIn(command)` for same-command assigns, env = transcript vars
  overlaid by assigns whose text before the add contains `[;&|\n]` (prefix-assignment exclusion);
  `expand()` only when word has `$` or backtick; null/'' target → `continue` (drop); cd/-C dirs
  expanded, unknown dir only drops a relative target; branch `pos[1]` expanded.
  `notePending(..., vars)`; `readTranscript` snapshots `varsBefore = new Map(t.msg.vars)` BEFORE
  `noteMessageSources` folds the command's own assignments in. 5 unit tests + 1 integration test.
  Design note, man page, CHANGELOG each gain one statement.
- grep at HEAD: `worktreeAdds` defined 347 (now takes `stats`), callers at 735 (`notePending`)
  and 2269 (passes `new Map()` — an empty vars map — candidate to probe). `expandVars` 567.
  `inWindow` 963, used 972, 1051, 1090, 1304, 1314, 2435.
- Read at HEAD: `instruments/ccclose` 300–405 (worktreeAdds + loopsAround), 520–600
  (commitCommandsIn tail, LITERAL_ASSIGN, assignmentsIn, expandVars, resolvePath), 648–683
  (MsgEvidence, noteMessageSources: `ev.vars.set` for every literal assign; a NON-literal
  assignment is not recorded and does not unset), 725–740 (notePending), 748–765
  (resolvePending: adds → t.worktrees, unresolved counted), 860–885 (readTranscript varsBefore
  snapshot), 955–975 (inWindow, sinceArg, windowCommits: `%ct`, `--since` with one day slack),
  2200–2290 (commitEvidence: subagent transcripts; line 2269 calls `worktreeAdds(cmd, cwd,
  new Map(), {unresolved:0})` — empty vars, stats discarded), 2412–2440 (worktree check),
  257–292 (shellWords, unquote, resolveFrom). `git()` = execFile with `-C root`, no shell.
- Read at HEAD: man page 60–61, 545–552, 755–768; design note 59–64, 668–680, 776–786;
  CHANGELOG 2213–2240. Test file 1–175 (fixtures), 1140–1162 and 1595 (helpers), 1322–1452.
- Mirror sweep: `grep -rln "worktreeAdds|WT_ADD|worktree add" instruments/` → ccclose,
  ccclose.design.md, man/ccclose.1, ccfleet, man/ccfleet.1 (ccfleet: to check whether it parses
  adds or only runs them). `ccopen` has no worktree-add parser. `instruments/README.md` 23 and
  25 describe ccclose/ccopen at summary level only (no variable statement to mirror).
- Brief's coldsweep sweep ('worktreeAdds|expandVars|varsBefore|inWindow'): 58 hits over 748
  files, 1005 excluded as barred; hits only in instruments/ccclose (19), ccclose.test.js (38),
  CHANGELOG.md (1). No second implementation outside ccclose.
- PROBE (harness, live, read-only): Bash call 1 `PROBE_WT_993=probe_value_from_call_one; export
  PROBE_WT_993; echo "[$PROBE_WT_993]"; pwd` → `[probe_value_from_call_one]`, pwd = worktree.
  Bash call 2 `echo "[${PROBE_WT_993:-unset}]"; pwd` → `[unset]`, pwd = worktree. So on this
  harness the cwd persists between tool calls and a shell variable does NOT (the tool's own
  description says the same: "Shell state (env vars, functions) does not persist"). Bears on the
  delta's claim that a variable is read "from a literal assignment ... before it in the
  transcript": an earlier call's `W=/p` is not set when a later call runs `git worktree add $W`.
  Candidate WT1.
- RE-RUN 1 (2026-11-22T22:30Z, load 14.70 at start): `nice -n 10 node --test
  instruments/ccclose.test.js` from the worktree root → exit 0; tests 153, pass 153, fail 0;
  365 s. Output kept in scratch (rerun-node.txt), not in the record.
- PROBE (unit, `node -e` requiring the worktree's instruments/ccclose, cwd '/r', no transcript
  vars unless stated) `cc.worktreeAdds(cmd, '/r', vars)`:
  A `W=/w/a; W=$(mktemp -d); git worktree add --detach $W` → [{path:/w/a}]  (stale literal kept;
    claim says a `$(...)` leaves the path unknown and the add DROPPED)
  B `W=/w/a; W=$OTHER; git worktree add --detach $W` → [{path:/w/a}]  (same)
  C `W=/w/a; unset W; git worktree add --detach $W` → [{path:/w/a}]  (same)
  D `cat > f.sh <<'EOF'\nW=/evil\nEOF\ngit worktree add --detach $W` → [{path:/evil}]
    (an assignment inside a heredoc body is read as live)
  E `W="a|b" git worktree add --detach $W` → [{path:/r/a|b}]  (prefix assignment counted because
    the quoted value holds a separator char; contrived)
  F `git worktree add --detach $W; W=/w/late` → []  (correct: assignment after the add ignored)
  G vars {W:/w/old}; `W=$(mktemp -d); git worktree add --detach $W` → [{path:/w/old}]  (stale
    transcript literal survives a non-literal reassignment)
  H `( W=/w/sub ); git worktree add --detach $W` → [{path:/w/sub}]  (subshell scope not seen)
  I `W='$X'; git worktree add --detach $W` → []  (correct, conservative)
  J `R=/repo && git -C $R worktree add -b b rel` → [{path:/repo/rel, branch:b}]  (correct)
  K `W=rel && cd /other && git worktree add -b b $W` → [{path:/other/rel}]  (correct for a shell;
    NOTE the message-file reader's `envAt` resolves a relative literal at assignment against the
    command's cwd instead, so "the same reading as message files" is not exact)
  L control `W=/w/one && git worktree add --detach $W origin/main` → [{path:/w/one}]
- MUTATIONS on a scratch copy of instruments/{ccclose,cctranscript,cclive,ccclose.test.js}
  (scratchpad mut-*/; `perl -0pi` one edit each, confirmed by diff; `nice -n 10 node --test
  --test-name-pattern=<p> ccclose.test.js`):
  a `const varsBefore = t.msg.vars;` (live reference, not a snapshot), p='worktree|210/330|210/360'
    → exit 0, 16/16 PASS. The snapshot's reason is untested. Candidate WT (test gap).
  b drop the `/[;&|\n]/.test(...)` prefix-assignment guard → exit 1, 15/16; red: "worktreeAdds
    drops a path it cannot resolve rather than invent one". Guard is tested.
  c `expandVars` returns '' for an unknown name → exit 1, 12/16, 4 red. Drop rule is tested.
  d `windowCommits` format `%ct` → `%at`, p='210/320|committer' → exit 1, 0/1; red: the 210/320
    test. The committer-date test bites on an author-date reading.
- Line 2269 (`commitEvidence`, subagent transcripts): `worktreeAdds(cmd, cwd, new Map(),
  {unresolved:0})` — the per-subagent `ev.vars` (built two lines above by noteMessageSources) is
  not passed and the stats object is discarded. Evidence is the line itself; no fixture probe run.
- V3/V4 mirrors: code comment (ccclose 300–312), design note 59–64 and 668–680, man page 60–61
  and 755–761, CHANGELOG 2224–2240 all state the same rule; README 23/25 summary-level only;
  ccfleet 549 and man/ccfleet.1 730 are unrelated mentions. No contradiction among mirrors.
- Rendering (ccclose 2553–2562): a worktree prints as `~/path (branch x) — worktree still
  present|put away; branch ...`; `via` is not printed, so a path reads as fact.
- `git()` (line 116) = execFile `git --no-optional-locks -C root ...`, no shell; resolved paths
  reach `isDir` (statSync), `safeReal` (realpathSync) and `tildePath` only.
- `which python3` → /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 (3.14.6).
- PROBE (end to end, scratch `probe-varsbefore.js`: a throwaway git repo, a fake HOME with one
  synthetic transcript whose single Bash command is `git worktree add --detach $W origin/main;
  W=<base>/wt-late` with a non-error "Preparing worktree" result; `node <copy>/ccclose --session
  sess-pv --identifiers --json`): pristine copy → `worktrees.items = []`, `unresolved = 1`
  (correct); mutation a (live reference instead of the `varsBefore` snapshot) → items =
  [`<base>/wt-late`], unresolved = 0: an invented path, and the suite stayed green on it
  (mutation a above). Candidate WT5 (test gap) confirmed with its consequence.
- RE-RUN 2 started 2026-11-22T22:30Z (load 16.59): `nice -n 10 python3 -m unittest discover -s
  tools` from the worktree root, output to scratch rerun-py.txt; moved to the background by the
  harness at the 600 s mark and still running at 22:52Z (load 20.70); result recorded below when
  it ends.
- Act-1 verdict appended to the brief below a `---` divider; Status line updated (ACT 1 WRITTEN,
  PASS-WITH-FINDINGS, 1 MAJOR · 1 MODERATE · 3 minor · 2 notes; act 2 pending).
- Gates on the brief (`python3 tools/<x>.py --root <worktree> <brief>`): datescan exit 0, clean
  (428 lines read); spellscan exit 0 but scanned nothing (docs/reviews is in .spellscanignore);
  wrapscan exit 0 but scanned nothing (.wrapscanignore); linkscan exit 0, clean (no internal
  links). Hand check `awk 'length > 100'`: pre-existing long lines 1, 41, 161, 169, 180, 181 are
  the brief-writer's; mine over 100 are table rows (250–255, 268–274, 407, 415–416) and one
  prose line (236) to be rewrapped.
- Scratch cleaned: mutation copies, probe scripts and fixture dirs removed; only the two re-run
  output files remain until the pass ends.
- RE-RUN 2, attempt 1: started 2026-11-22T22:30Z, moved to the background by the harness at
  600 s, then STOPPED by the harness's background time limit at about 23:05Z without reaching
  the summary line (load 14–24 throughout; other passes running). Output kept as
  rerun-py-attempt1-killed.txt in scratch (dots only, no failures printed up to the stop).
  Restarted 2026-11-22T23:06Z as a background run with the longest allowed limit (2 h), same
  command, same cwd, load 7.64 at restart.
- RE-RUN 2, attempt 2 (2026-11-22T23:06Z → 23:26Z): `nice -n 10 python3 -m unittest discover -s
  tools` from the worktree root → exit 0; `Ran 3382 tests in 1260.839s` · `OK`. Another pass's
  identical suite ran at the same time from its own worktree (seen by `lsof -d cwd`), left alone.
  Re-run ledger in the brief filled; the stopped attempt is recorded there too.
- Final checks: datescan exit 0 clean (428 lines), linkscan exit 0 clean; no placeholder left;
  every prose line of the verdict ≤ 100 columns after rewrapping (table rows run longer, as the
  brief-writer's own lines 1, 41, 161, 169, 180, 181 do). `git status --short`: only the brief
  modified (+229/−3 at the Status line) and the orchestrator's partition deletion of the sibling.
  Scratch: my files removed; the three `*.log` files there are the orchestrator's, untouched.
- ACT 1 complete 2026-11-22T23:3xZ. Verdict: PASS-WITH-FINDINGS — WT1 MAJOR, WT2 MODERATE,
  WT3–WT5 minor, WT6–WT7 notes. Not opened: the sibling, any barred record, any commit body.

#### Act 2

- 2026-11-22T23:3xZ: orchestrator confirms act 1 committed (0129890d) and releases the sibling at
  the held path. Opening now: the sibling, intent records 210/330 and 210/320 whole, board item
  160/993 whole, both delta commit bodies (`git log -1 --format=%B`).
- Read the sibling whole (5 questions, 1 fact, brief-writer's re-runs: node exit 0 215 s; python
  2,643 OK 1,167 s on 3.14.6). Read 210/330 and 210/320 whole, 160/993 whole, both commit bodies.
- Prior-verdict overlap: `grep -ln "worktreeAdds|expandVars|persist"` over docs/reviews → three
  files: 2026-11-09-0126 (210/360, CW1–CW8; its lens-2 text at 361–362 notes the subagent
  caller's discarded stats, no numbered finding; none covers WT1/2/3/5/6), 2026-11-09-0153
  (160/960; evidence tier, not the worktree reading), 2026-10-18-0506 (predates). The sibling's
  two named priors (2026-10-17-1010, 2026-10-26-0917) grep'd: no variable-expansion content.
  No `WT` prefix elsewhere in docs/reviews.
- PROBES for sibling Q3/Q4 (`cc.worktreeAdds(cmd,'/r')`): `if false; then W=/w/if; fi; git
  worktree add --detach $W` → /w/if; `echo x | W=/w/pipe cat; git worktree add --detach $W` →
  /w/pipe; `export W=/w/exp && …` → /w/exp (correct); `W=/w/a && add $W && W=/w/b && add $W` →
  /w/a, /w/b (correct); `${W:-/w/dflt}` → []; `$HOME/wt` → []; `~/wt` → <homedir>/wt;
  `HOME=/h && … $HOME/wt` → /h/wt.
- Reconcile appended beneath the verdict: per-question notes, author's account checked, overlap
  recorded, WT8 (note) formed at reconcile, overall line restated (1 MAJOR · 1 MODERATE · 3 minor
  · 3 notes). Status line updated to act 2 written; sibling not folded, not deleted.
- Final gates after act 2: datescan exit 0 clean, linkscan exit 0 clean (spellscan/wrapscan skip
  docs/reviews by ignore file); no prose line of the verdict over 100 columns; no private path,
  email or estate fact in the added text. `git status --short`: only the brief modified (+102
  against the act-1 commit) and the orchestrator's partition deletion; the held sibling is in
  place, unfolded. No scratch files of mine remain.
- ACT 2 complete 2026-11-22T23:4xZ. Overall restated: PASS-WITH-FINDINGS — WT1 MAJOR, WT2
  MODERATE, WT3–WT5 minor, WT6–WT8 notes (WT8 formed at reconcile).

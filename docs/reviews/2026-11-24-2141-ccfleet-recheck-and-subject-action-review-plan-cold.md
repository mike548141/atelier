# Cold pass — the `ccfleet` re-check (`160/1450`) and subject, space, action with `review plan`, `ccfleet plan` and `work plan` (`160/1790`), with `/atelier:session close` (`450/030`)

**Board:** `docs/roadmap/160-doctrine-review-owed/1450-rule-4-cold-pass-queued-ccfleet-fleet-sweep-review-drain-modelguard.md`
(the re-check of its FAIL) and
`docs/roadmap/160-doctrine-review-owed/1790-rule-4-cold-pass-queued-subject-action-review-plan-ccfleet-plan.md`:
one pass, one verdict, both items, as the principal chose. The same verdict also closes
`docs/roadmap/160-doctrine-review-owed/1740-rule-4-cold-pass-queued-ccfleet-whole-grant-and-unlanded.md`
(his pick, recorded there) and is the review of
`docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/030-a-close-command-so-the-close-text-is-not-pasted.md`
(Part C below).
**Status:** BRIEF ONLY, not run. Written 2026-11-24 UTC by a brief-writer worker of queue run
`0b4f93ef` (Opus 5.5), pinned at `26a4fe7e` (`origin/main` when written). **Widened** 2026-11-25 UTC
by queue run `9a08702f` (`atelier-56`, Opus 5.5, principal-opened) to take in `/atelier:session
close` (Part C), and **repinned at `5696f91a`** (`origin/main` when widened).
**Approval:** one Fable pass, on the laptop's weekly budget, by a fresh session. The principal's
pick, 2026-11-24 ~21:30 UTC, recorded on `160/1790` (an answer, not a ruling), verbatim:
*"Fresh session, this week (Recommended)"*; the option text he picked: *"Confirms the one approved
Fable review covers both: the fixes and the new commands. A separate session runs it as soon as
the brief lands, on this week's budget. Benefit: if it's clean, /fable-drain can retire before <!-- datescan:allow: the principal's picked option text, quoted verbatim -->
Monday 30 Nov's drain. Cost: one Fable review from this week's budget (roughly a large pass)."*
It stands on two earlier picks recorded on `210/470`: *"Approve one pass (Recommended)"*
(2026-11-23, the re-check) and *"Wait, review the new build (Recommended)"* (2026-11-24, one pass
over the fixes and the new commands together). The widening is his route: asked whether to land
the close command now or after the pass started, he asked instead, verbatim, *"Is the review
underway or can we expand its brief to cover this as well?"* (2026-11-24 ~23:05 UTC, recorded on
`450/030`); it had not started, so the brief takes the command in and the one pass covers it. Run
only once the delta has stopped moving:
re-check the since-line under *What the work is* before you start, and stop if it is not empty.

**Pass type:** a re-check and a cold pass in one, per `docs/method/REVIEW.md` rule 4: code,
design and doctrine. The skills, their prompt templates, the routers and a hook that denies tool
calls are doctrine by function (rule 3); the instrument that runs them is reviewed with them as
one commitment.
**Tier:** Fable, the principal-named review tier, checked at selection by whoever takes the pass.
A session that cannot run on it stops (rule 4).
**Size of this pass:** very large. Fourteen commits in scope, three more read for context. At
`26a4fe7e`: `instruments/ccfleet` 2,186 lines of standard-library Python, its tests 1,557 lines
(103 tests, about four minutes each run), a 1,582-line manual page, `tools/modelguard.py` 510
lines with a 191-line test, about 2,000 lines of skill text over six subjects, the menu script
(184 lines) and two guard tests, and the live-reference sweep across the doctrine; Part C adds a
76-line action, its router row and a 158-line guard test. Budget the
time; never thin the pass to fit it (`REVIEW.md`, *Budget decides how many reviews run and when,
never how a review is run*).

**The question this pass answers for the principal.** Once it is clean, his weekly drain moves
off a user-level command outside this repo and onto `/atelier:review plan` and
`/atelier:review run`, driven by `ccfleet`. His words, 2026-11-24 ~06:20 UTC, recorded on
`180/210`, verbatim: *"we fable review the new code/design/wahtever before we use it for a review
drain session"*. So the verdict must say plainly whether a paid drain can safely start from
these commands as they stand.

**Why it earns a review.** `ccfleet` starts unattended headless Claude Code sessions in a
worktree of every repo an estate lists, with the user's credentials, and decides from their
output whether a paid review's claim is released and its worktree removed. `review plan` is now
the one place that decides which paid reviews run, in what order and on which budget; `review run`
seals that and drains it; `review brief` and `fleet sweep` take their work from it. Every
`/atelier:` command every plugin user types was renamed, with no forwarder. `/atelier:session
close` runs the principal's own close text in any session, in any repo or none, from one word.
`modelguard` sits in
front of every `Agent` and `Bash` call where it is wired. The worst failures:

- **Paid review work lost, silently redone, or misread.** A pass cut off by a usage cap, a crash,
  a reboot or a closed terminal whose claim, worktree, session id or review log cannot be
  recovered; a finished pass read as unfinished, or the reverse. This is what failed last time,
  and what the drain switch waits on.
- **The wrong reviews bought, or quality traded for price.** A plan that ranks or routes against
  the principal's words, sends a review to a route that cannot match a local pass, or estimates
  a spend that is not measured; a seal or gate that a drain can pass without a plan.
- **A command that does something other than what was typed.** A bare or mistyped subject that
  starts work, or reads toward it, instead of showing its menu; an action word that is a near-miss
  of another; a live reference that still names a command that no longer exists.
- **Blast radius.** One config mistake (a grant, a repo list, a private name left off the list,
  a prompt variable) reaches every repo in one run; a public repo's prompt or record carrying a
  private name is a publication that cannot be retracted.
- **A false allow, or a false deny that stops routine work, from the hook.** A launch with no
  model that `modelguard` passes is the silent failure; a refusal of an ordinary command blocks
  every session that runs it.
- **A skill that stamps a wrong rule** into every adopter's sessions: the widest blast radius in
  the operating model (rule 4).
- **A close that is not the principal's close.** A command that runs a stale, uncommitted or
  partial copy of his text, drifts from it, or reads as a proper close when it ran something
  else, in sessions he then shuts on its word.

## Spawn provenance

- **Authors of the work under review**, by commit (from the board's records and the commits'
  subjects; no message body was used to find them):
  - The original delta reviewed by the first pass: sessions `559edaec` (headless, started by an
    estate health sweep, orchestrator `58027096`), `78ca9153`, `84b7932e`, `64f984ac`, `19378351`.
  - The fixes to the first pass's findings, the hook fix after them and the canary: queue run
    `c7a1e36e` and its workers (`b99fa4be`, `e75fe749`, `e9916406`, `36e9ef0e`, `c2d4e628`,
    `5d99a2cc`).
  - The config-as-the-whole-grant change, the review-log hash change and the shipped-skill lists:
    queue run `608d8123` and its workers (`9ba5c6b6`, `b95db160`, `7a8a2305`).
  - The `work-run` rename the subject sweep built on: session `b95c0d98` (`dae1786d`,
    `ee6f384f`).
  - The plan-mode and command-form commissions recorded on the board: session `edf25bd3`.
  - Subject, space, action, `review plan`, `ccfleet plan`, `work plan` and the live-reference
    sweep: session `523be3be` (`atelier-e8`) and its workers (`0c67dc0f`, `bfa38582`,
    `10b32435`, `f354e542`, `6a98df21`).
  - The `/atelier` menu the subject menus build on: session `f50448ca`.
  - `/atelier:session close` (Part C): queue run `0b4f93ef` (`atelier-86`) and its Sonnet worker
    (`e917a98b`); the item's build spec and his pick were recorded by session `33d3cde8`. Session
    `9a08702f` rebased the commit onto `main` with no content change (it became `3620c908`) and
    pushed it; it authored no line of it.
- **Who wrote earlier briefs and ran the first pass:** queue run `08cd3b95` and its workers wrote
  the first brief; session `5106cf48` orchestrated the first pass, and its Fable reviewer formed
  the first verdict.
- **Who wrote this brief:** a brief-writer worker (Opus 5.5) of queue run `0b4f93ef` (`atelier-86`,
  principal-opened, 2026-11-24). Neither the worker nor its orchestrator authored, started or
  instructed any part of the delta. **Off-tier for review, disclosed: the brief-writer forms no
  finding and writes no severity**, and stops after writing. It ran no review and used no Fable
  model. Queue run `0b4f93ef` will not start the pass.
- **Who widened this brief:** queue run `9a08702f` (`atelier-56`, Opus 5.5, principal-opened,
  started 2026-11-24 UTC, widened 2026-11-25 UTC), inline, no worker. It authored, started and instructed no part of the delta or
  of the original brief; it rebased and pushed Part C's commit unchanged and ran the full suite on
  it. **Off-tier for review, disclosed: it forms no finding and writes no severity**, ran no
  review, used no Fable model, and will not start the pass.
- **Barred from running or orchestrating this pass:** `0b4f93ef` and every worker it started
  (whoever writes a brief does not run it); `559edaec`, `58027096`, `78ca9153`, `84b7932e`,
  `64f984ac`, `19378351`, `08cd3b95`, `5106cf48`, `c7a1e36e`, `608d8123`, `b95c0d98`,
  `edf25bd3`, `523be3be`, `f50448ca`, `33d3cde8`, `9a08702f`, and everything each of them started
  or instructed.
- **Contact, disclosed (rule 4).** The brief-writer's only instruction came from its orchestrator
  `0b4f93ef`: the two items, the approval, the delta commits named on `160/1790`, the old-to-new
  skill paths, the principal's purpose (the drain switch, so judge whether `review plan` and
  `review run` are safe to run a paid drain from), the barred sessions, the house form, and to
  pick a new finding prefix. No author session contacted the brief-writer. The widening's only
  instruction was the principal's own run brief to `9a08702f`: land `e917a98b`, widen this brief to
  take in the close action, its router row and its test, repin it, add matching held-back
  questions, record it on `160/1790`, and not run the pass. No author session contacted it.
- **Who reviews:** a fresh Fable session started for this pass alone, by a session that passes rule
  4's criterion. An orchestrator may hold the context partition and commit the records off-tier,
  only if it forms no finding, writes no severity, and is disclosed in the claim, the pointer and
  the verdict, with its spawn prompt and release message in the verdict's provenance.
- ⚠️ **Brief-writer's exposure, disclosed** (author-account material met before writing): its
  launch prompt; `REVIEW.md` whole; `skills/review/brief.md` whole; the held-back-material
  paragraph of `CONCURRENCY.md`; items `160/1450`, `160/1790`, `160/1740`, `210/470`, `210/570`
  and `450/020` whole and `180/210` whole, the heads of `160/1770`, `160/1780`, `210/560`
  (**all carry authors' accounts**); **the first pass's brief and the opening of its verdict**
  (scope, provenance, section headings), read as the house's shape model, so this writer has met
  the first verdict's framing; the heads of six session records, read only to find which session
  wrote which commit; the delta at HEAD in part (`skills/review/` whole, the six routers,
  `skills/work/plan.md`'s head, `ccfleet`'s docstring and usage text, the menu's and the subject
  test's docstrings, the example config); commit subjects and file stats; one body-free
  `coldsweep --commit` read; the results of the re-run lines below. It opened no delta commit's
  message body. Its harness also loaded user-level and repo instruction files and a memory index,
  which hold private context this brief does not carry. Everything evaluative it formed is in the
  held-back sibling.
- ⚠️ **Widener's exposure, disclosed:** its launch prompt; items `450/030` and `160/1790` whole
  (**author's accounts**), the newest session record (`0b4f93ef`'s, **author's account**), this
  brief and its held-back sibling whole; Part C's commit with its message body (read before
  widening, to land it), `skills/session/close.md`, the router diff, the test's head and test
  names, the `README.md` and `CHANGELOG.md` hunks; the full suite's results on the landed commit;
  the re-run lines below. Its harness loaded the same user-level and repo instruction files and a
  memory index. Everything evaluative it formed is in the held-back sibling.

## The acceptance test

Judge the work against what it claims (its docstrings, manual, skills, routers, menu, tests and
changelog) and against the doctrine it must keep:

- **The principal's words.** The command form, his ruling of 2026-11-24, verbatim, as the delta
  itself quotes it (`tools/test_subject_skills.py`, the routers): *"I think a space and for the
  default it could have a menu or help screen a little like what /atelier does by itself. We
  should make all the atelier command like this so its consistent"* · *"So something like
  /atelier:review by itself would be a help screen, not run a command by default"*. The plan's
  commission, the one-home instruction and the `review brief` link are quoted verbatim in
  `skills/review/plan.md`; judge the plan, the run and the brief against those words and against
  his rule on review quality, quoted in `REVIEW.md` § *When to review*: *"Quality is more
  important than cost. If we run out of budget then we will resume the work when the budget
  replenishes"*. A drain that cannot resume what a spent budget cut off fails that sentence. The
  old names: his pick *"Nothing"* (no forwarder, no signpost), as the delta's own test records.
  The close command: his rule against drift, as `skills/session/close.md` quotes it verbatim
  (*"You need to ensure the there is no drift between the command and the text file unless I
  authorise the drift"*), and his reason for asking, 2026-11-24, verbatim: *"I regularly copy and
  paste the ending session text into sessions when I want them to wrap it up properly. Often these
  are sessions that I did not start with a /atelier:work run command"*. Judge the action against
  the section it claims to run, word for word.
- **The rules the drain enforces on others.** `REVIEW.md` rule 1 (the deferred split and the
  context partition), rule 2 (barred reading), rule 4 (spawn criterion, tier at selection, the
  off-tier orchestrator's two conditions), *The lifecycle* (method record); `CONCURRENCY.md`
  § *Orchestrated queue runs* (where held-back material lives); `ECONOMICS.md` (tier set by risk;
  the model named on purpose).
- **The public-repo rule.** `docs/PERSONAL-DATA.md` and the repo-craft purpose rule: a generic
  tool in a public repo carries no estate's names, and its config example is fictional.
- **The first pass's findings**, in phase 2 only (*Process* below): each is to be fixed as that
  verdict counselled, by the principal's answer recorded on `160/1450`. That verdict is
  [`2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md`](2026-11-20-0813-ccfleet-fleet-sweep-review-drain-modelguard-cold.md),
  pinned at `f767033a`, barred until your act 1 is committed (rule 2). This brief neither quotes
  nor summarises it.

## What the work is

**Part A, the re-check (`160/1450`).** Every commit on the first pass's paths since its pinned
head `f767033a`, those paths followed to where they now live (`skills/fleet-sweep/` is now <!-- pathscan:allow: the old path, named to say where it moved -->
`skills/fleet/sweep.md` and its prompts; `skills/review-drain/` is now `skills/review/run.md` <!-- pathscan:allow: the old path, named to say where it moved -->
and its prompts):

- **`b99fa4be`** — `modelguard: find claude in command position, and pass a lookup of it`
  (2026-11-23)
- **`e75fe749`** — `skills: scope fleet-sweep adoption, keep cut-off worktrees, unique labels`
  (2026-11-23)
- **`e9916406`** — `skills: review-drain reads a cut-off pass as cut off, and keeps its log`
  (2026-11-23)
- **`36e9ef0e`** — `ccfleet: never read a cut-off pass as done; fix the 160/1450 code findings`
  (2026-11-23)
- **`c2d4e628`** — `ccfleet: make the review-drain and fleet-sweep skills say what the code does`
  (2026-11-23)
- **`5d99a2cc`** — `modelguard: pass ssh as a user named claude (210/570)` (2026-11-23)
- **`9ba5c6b6`** — `ccfleet: make the config the whole grant; read a clean end that leaves
  unlanded work as UNLANDED` (2026-11-23; queued for its own pass as `160/1740`, below)
- **`b95db160`** — `ccfleet: hash the review-log name with SHA-256, still finding SHA-1 names`
  (2026-11-23; widened into `160/1740`)

**Part B, the new build (`160/1790`):**

- **`0c67dc0f`** — `skills: every /atelier: command becomes subject, space, action (450/020)`
  (2026-11-24)
- **`bfa38582`** — `session-open: the prompt names /atelier:work run (450/020)` (2026-11-24)
- **`10b32435`** — `review plan, ccfleet plan, and the live-reference sweep (450/020, 180/210,
  180/240)` (2026-11-24)
- **`f354e542`** — `skills: a subject's first word must match an action exactly` (2026-11-24)
- **`6a98df21`** — `skills: routers name the harness placeholders in words` (2026-11-24)

**Part C, the close command (`450/030`, reviewed under `160/1790`):**

- **`3620c908`** — `skills: /atelier:session close runs the prompt's close (450/030)` (2026-11-24;
  the same change as `e917a98b`, rebased onto `main` unchanged)

**Read for context only** (on the paths, with their own queued passes): `dae1786d` and
`ee6f384f` (the `queue-run` to `work-run` rename and its retired alias, `160/1780`), and
`7a8a2305` (the plugin manifest's skill lists, `160/1770`). They are in scope only as far as the
code and skills at HEAD carry them; their own subjects (the session-open prompt's start gates,
the parked mark, decision-record statuses) are those passes'.

`160/1740` is the queued pass for `9ba5c6b6` and `b95db160`. Those commits change the code the
drain runs, so this pass reviews them as part of `ccfleet` at HEAD; the principal has since
picked that this verdict also closes `160/1740` (recorded there).

Every other commit on these paths since `f767033a` touches only another tool's row in
`tools/README.md` or `instruments/README.md` (`ccclose`, `ccopen`, `idhook`, `leakscan`,
`archivecut`, the floor, `pathscan`), and is out of scope.

Delta paths, read at HEAD and commit by commit:

- `instruments/ccfleet`, `instruments/ccfleet.example.json`, `instruments/test_ccfleet.py`,
  `instruments/man/ccfleet.1`, `instruments/README.md` (the `ccfleet` and menu rows and the
  requirements paragraph)
- `skills/` whole: six subjects (`fleet`, `repo`, `review`, `session`, `work`, `worktree`), each a
  router `SKILL.md` and one file per action, with their prompt templates
- `instruments/atelier-menu/` and `instruments/test_atelier_menu.py`
- `tools/modelguard.py`, `tools/test_modelguard.py`, `tools/test_subject_skills.py`,
  `tools/README.md` (§ *`modelguard.py`* and the lines `10b32435` changed)
- Part C: `skills/session/close.md`, the `close` row, description, `argument-hint` and
  `allowed-tools` in `skills/session/SKILL.md`, `tools/test_session_close_single_source.py` (and
  the helpers it imports from `tools/test_work_run_single_source.py`), the `close` lines in
  `README.md`, and the *Ending the session* section of
  `docs/method/session-open/session-open-prompt.md` as the text the action runs (judged for
  whether the action runs it faithfully, not for its wording)
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- the live-reference sweep in `10b32435` and `bfa38582`: every line it changed in `CLAUDE.md`,
  `README.md`, `.githooks/pre-commit`, `tools/pre-commit.sample`, `docs/method/`, `docs/build/`,
  `docs/decisions/` (two lines), and the tools and tests it touched (`deadhook`, `floorfleet`,
  `quotescan`, `stampscan`, `test_deadhook`, `test_precommit`, `test_templates`,
  `test_work_run_single_source`); judged for whether each reference now names what exists, not
  for the doctrine around it
- `CHANGELOG.md`: the entries that name any of the above since 2026-11-22, the `450/030` entry
  included

First confirm the tree holds the whole delta, then read each commit body-free:

```
git merge-base --is-ancestor 3620c908 HEAD; echo "exit=$?"
python3 tools/coldsweep.py --root . --commit 36e9ef0e --path instruments --path skills \
  --path tools --path .claude-plugin --path CHANGELOG.md
```

Repeat the `--commit` line for each of the other thirteen commits in Parts A, B and C, and the
three read for context. For `10b32435` and `bfa38582` add `--path docs/method --path docs/build
--path docs/decisions --path CLAUDE.md --path README.md --path .githooks`; for `3620c908` add
`--path README.md`. Plain `git show` is
barred: it prints the message body before the diff, and reading is atomic (rule 1). Several of
these commits also touch board items and session records; those are barred until phase 2, so
always pass `--path`.

Then check what has landed on the delta paths since this brief was pinned:

```
git log --oneline 5696f91a..HEAD -- instruments/ccfleet instruments/ccfleet.example.json \
  instruments/test_ccfleet.py instruments/man/ccfleet.1 instruments/README.md \
  instruments/atelier-menu instruments/test_atelier_menu.py skills tools/modelguard.py \
  tools/test_modelguard.py tools/test_subject_skills.py tools/README.md .claude-plugin \
  tools/test_session_close_single_source.py tools/test_work_run_single_source.py \
  docs/method/session-open/session-open-prompt.md
```

It was empty at `5696f91a`, the head this brief was repinned at (first pinned at `26a4fe7e`).
A commit that only touches another tool's row in one of the two READMEs does not count (read
its diff body-free to tell). Any other commit means the delta moved: stop and hand back for the
brief to be updated. Otherwise review the work as it stands at your HEAD, and pin that SHA in
your verdict's scope.

**Machine-local surfaces no other review will catch** (read-only; report them in public-safe
terms, never a home path or a private name):

- The user-level settings wire `modelguard` as a `PreToolUse` hook on `Agent|Task|Bash`, run as
  `/usr/bin/python3 -I <the primary checkout>/tools/modelguard.py`. That interpreter is Python
  3.9.6; the `python3` on `PATH` is 3.14.6. The hook runs the primary checkout's copy, which was
  at `26a4fe7e` when this brief was written.
- `~/.local/bin/ccfleet` is a link to the primary checkout's `instruments/ccfleet`.
- The plugin is installed in place from the primary checkout (a local-path marketplace), so the
  skills a session loads are the primary checkout's. A plugin user installing from the remote
  marketplace gets a copy instead; the routers' relative path to the menu script is worth
  judging under both.
- `ccfleet check` on this machine reports which user-level hooks a launched session keeps and
  which it drops, and that the user-level instruction file is appended to every launched
  session's system prompt. Read it with a synthetic config only (below); quote no path or
  content from it.
- Free disk sat below the gate's default floor (20 GB) when this brief was written, so `gate` may
  answer "hold" on this machine for reasons unrelated to the code.
- The in-place install also means `/atelier:session close` reads the prompt from the primary
  checkout's `HEAD` and checks that checkout's working tree for a pending edit, whichever repo
  the session runs in. The section names `ccclose`, which here is a link on `PATH`; the router's
  `allowed-tools` names it by bare name.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the authors' claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1); these are a floor, never a fence.

**`ccfleet` (from its docstring, usage text and manual at HEAD)**

1. "An end is clean only when the session exited 0 and its JSON flags no error; anything else
   reads as ERROR (TIMEOUT at the time limit) whatever its text says, so a cut-off pass is never
   read as DONE."
2. "A worktree is removed only after a clean RESULT, never by force, and never while it holds
   uncommitted files or commits on no remote branch."
3. "A new session is given its id up front (`--session-id`), so a session killed before it prints
   still has one on its START line and its claim."
4. "A dry drain writes its own launched list and calls no `queue.ranked`, so a rehearsal never
   makes the real drain read a full queue as empty. A pick that ends before its session starts is
   taken back off the list."
5. "The config is the whole grant": every launch passes `--setting-sources project,local` and a
   `--settings` file ccfleet writes (the user-level settings less their allow rules, default mode,
   extra directories and any hook that prints an allow decision; deny and ask rules, guard hooks,
   plugins and env kept); the user-level instruction file is appended to the system prompt; "a
   launch prints a WIDENED line for each grant" a repo's own settings add.
6. "A clean RESULT that leaves unlanded work is not clean: it reads as UNLANDED, the claim stays
   and the worktree is kept for a resume."
7. A session still running at `session_timeout_minutes` (default 480) is ended; a stopping driver
   reports a hung child instead of waiting forever.
8. The transcript fallback takes, on a clean end only, "the newest text that has a RESULT line
   and an ITEM: or REPO: line (the final-output shape), never a line of narration".
9. The review log is `<kit_dir>/review-logs/<repo>-<item>-<hash>.md`, the same path for a pass,
   its resume and its fold; a log an earlier pass left there is moved, dated, to
   `review-logs/withdrawn/` first; the hash is SHA-256, and older SHA-1 names are still found.
10. `drain` refuses a config without `next`, `ranked`, `take` and `release` (exit 64); calls
    `ranked` once before the first pick, after the reset check, never on a dry drain; any other
    exit prints `DRAIN EXIT: not ranked` and exits 1.
11. **`ccfleet plan`** "reads and never judges": it calls `queue.evidence` (and `queue.owed`),
    reads its own past pass logs for cost, and calls none of `ranked`, `take`, `next`, `release`
    or `ended`, and writes no launched list, claim, worktree or session; `drain --dry-run` prints
    the same reading prefixed `DRY plan:`; a failing queue command, or output other than the JSON
    shape, exits 1; no `queue.evidence` exits 64.
12. Cost history counts only passes that ended clean, from `<kit_dir>/logs/pass-*.out` and the
    JSON logs they name (count, median, max of cost, duration, turns); only the `local` route is
    measured; any other route, or local with no logs, reads "no measurement"; "Nothing is
    estimated."
13. A pass run by hand (`ccfleet pass`) "meets the same gate as a drain" (the run skill) and
    "leaves no .out and is not counted" (the plan's history).
14. Every earlier claim the first brief listed for `ccfleet` that the code at HEAD still makes
    (per-repo billing by worktree basename, the private-name guard, the headroom gate, stdin from
    `/dev/null`, the wait-ceiling variable, one driver per `kit_dir`, the live ceiling, the stop
    file's age rule, children in their own session, the exit codes, "Python 3.8 or later,
    standard library only").

**`modelguard`**

15. It denies every `Agent` call with no `model` (a fork exempt) and every Bash command that
    starts or resumes a `claude` session with no `--model`, finding `claude` in command position;
    a lookup of `claude` (and, since `5d99a2cc`, `ssh`, `scp`, `sftp` and `rsync` to a user named
    `claude`) passes, while `ssh host claude -p …` is still refused; after a command head it does
    not know, it fails closed. A malformed payload never blocks.
16. It passes its tests on both interpreters, including the 3.9 the hook runs under.

**The command form (`0c67dc0f`, `f354e542`, `6a98df21`)**

17. Every `/atelier:` command is one skill per subject with the action as its first argument; each
    action's text lives in its own file, so a use loads only its own.
18. A router checks the first word before anything else: it must be exactly one of its table's
    actions, "not a synonym (for example `drain` for `run`), not a word later in the sentence";
    "Read no action file and run nothing until this check passes." A bare subject or an unknown
    word shows the subject's menu, says which words were typed, and stops.
19. The routers name the harness's placeholders in words (the arguments placeholder, the
    plugin-root placeholder), and the plugin root is "the folder two levels above this skill's
    base directory".
20. Each router's description carries the trigger words of every action it holds; the menu is
    read at run time from front matter, so a new command appears with no edit.
21. The retired hyphen names are gone from every live surface; records keep them.
    `tools/test_subject_skills.py` guards this, the router tables and the descriptions.

**`review plan`, `review run`, `review brief`, `work plan` (`10b32435`)**

22. `skills/review/plan.md` is "the one home of the method": nothing else ranks, routes or finds
    owed reviews. Three callers: `review run` (the briefed rows, sealed), `review brief` (the
    owed-but-unbriefed list), `ccfleet drain --dry-run` (`ccfleet plan`'s reading).
23. The plan is read-only: no claim, worktree, session, commit or seal; "a plan is never a seal".
24. "A review is owed when its item's own text, or the principal's words on it, says one is
    required. A bare `⏳`, REVIEW.md's triggers, or a writer's view that it deserves one do not
    count."
25. The ranking and routing rules of steps 2 and 3 (the principal's direction first; lapse-first
    when a lapse is near, else cheapest capable route, cost breaking a tie; no fixed threshold for
    "near", the plan saying why per budget; "Unsure means the local route"); estimates only from
    measurement, else "no measurement"; the table form he picked.
26. `review run` runs the plan every run, prints it with no question, then seals it through the
    adopter's queue with his words; the seal's own rules (refuses while any ready review is
    missing, unreasoned, on a closed route, on a later route than its best without why, or while
    two budgets are open and either lapse time is unknown; lasts one run); the spill rule and the
    open question it leaves to the principal.
27. `review run`'s Mode 1, Mode 2, the variables table and the close, as they now read after
    the fixes, including that the review tier's approval is "the adopter's setting".
28. `review brief` with no subject takes its work from the plan's unbriefed list; `fleet sweep`
    takes the owed-not-briefed list from it too.
29. `work plan` holds no rule of the run, reads the run's brief as the run does, and claims,
    changes and starts nothing.
30. `menu.py` lists every subject and action; `menu.py SUBJECT` prints one subject's menu; its
    selftest proves a fixture plugin and stays quiet on junk.

**`/atelier:session close` (`3620c908`, Part C)**

31. The action "holds no rule of its own": it reads the prompt's *Ending the session* section,
    from its heading "to the next heading that starts with `## `, or to the end of the file", and
    follows it "as his own brief, word for word", doing "nothing the rest of the prompt says".
32. It reads the committed copy, never the working file (`git show HEAD:` when the plugin root is
    a checkout), warns in its first lines when an edit to the prompt is pending, and says which
    of the two reads applied when the plugin is not a checkout.
33. "If the heading is not there, stop": it says so in its first line and closes nothing from
    memory, another section or any other text.
34. Words typed after `close` are "this session's extra close brief", carried out alongside the
    section; where they add to or narrow a step, it says so.
35. It "works in any repo, because the plugin is installed for the user and the prompt is read
    from the plugin", and in a session with no repo `ccclose` runs without `--root` and "reports
    on that directory and the session's own transcript".
36. `tools/test_session_close_single_source.py` (14 tests) "fails if the action stops pointing at
    the file and the section heading, starts copying the section's lines, or grows an instruction
    the delivery job does not need"; by its own docstring it "cannot catch a paraphrase".
37. The router lists `close`, its description carries the close's trigger words, its
    `argument-hint` reads `onramp | close`, and the prompt itself is unchanged by the commit.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:**

- Any estate's private ccfleet config, rulings file, queue tool (its `evidence`, `owed`,
  `ranked`, `seal`, `next`, `take`), lane records and run results. Grounds: private by design,
  this repo is public, and the delta's claim is that the code and skills are generic. Judge the
  contract they must meet through the example config and a synthetic queue. Do not open a real
  config.
- The user-level drain command the estate still runs, outside this repo; it retires at the
  switch this pass gates.
- The subjects of `160/1770` and `160/1780` beyond what the skills at HEAD carry (decision-record
  statuses; the session-open prompt's start gates, parked mark and asks backlog), and of the other
  tools whose README rows changed. They have their own passes.
- Private children's own sweeps of their live references; they are their sessions' work. The
  claim that children's copies refresh at their next pin bump is in scope, judged by class.
- The wording of the session-open prompt, the *Ending the session* section included: it is the
  principal's own text. Whether `close` runs that section faithfully, completely and only it is
  in scope; so is `ccclose`'s behaviour only as far as claim 35 relies on it.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else.
   Is a router's instruction to check the first word a control a model reliably follows, and what
   stands behind it if not? Is one file of prose, read by an agent each run, the right home for
   a ranking that decides paid spend, with code that only reads? Is "owed" defined so the plan
   finds what the doctrine says is owed? Is a cost estimate from local-only history a sound basis
   for the spend the principal asked to see? Is "no forwarder" for the old names sound for every
   plugin user and for children whose hooks and stamped onramps still name them until a pin bump?
   And the re-check's own question: is the first pass's counsel, as applied, the right fix, or
   did a fix move the risk somewhere the counsel did not look? For the close: is "read the
   committed copy at the plugin root's `HEAD`" the principal's current close in every install
   shape, and is a test that pins pointers and forbids copied lines enough to hold "no drift"?
2. **Correctness & quality.** Re-drive the claims above against the code and the skills, by probe,
   not by reading. Trace what survives, and where, when a pass is interrupted at each point of its
   life: before the claim, after the claim and before `START`, mid-session (a usage cap; a
   `SIGKILL`; a reboot; the driver's terminal closed; the driver itself killed), after the session
   and before the release, and during a fold. For each, say whether the claim, worktree, session
   id, review log and verdict can be recovered with what the tool and the skills record, and
   whether `resume` can take it from there. Walk a drain from `/atelier:review run` through
   `review plan`, the seal, `ccfleet drain` and the close, as an adopter with only this repo
   would, and say where it can start a paid pass without a plan or a seal. Drive each router with
   a bare subject, every action, a near-miss word and a word later in the sentence, in a headless
   session on the cheapest model if you can spend on it (below). Drive the close the same way:
   the section finder against a prompt whose heading is gone, moved, duplicated or followed by a
   fenced `## ` line; a pending edit; a plugin root that is not a checkout; a session with no
   repo. Record each overclaim against the text that makes it, including any claim no test pins.
3. **Completeness / harvest.** Every surface that states the queue contract, the plan's
   interface, the exit codes, the template variables, the stop conditions, the command names or
   the drain's rules agrees (docstring, `--help`, manual, READMEs, skills, routers, prompts, menu,
   manifest, changelog: V3 and V5). One home per fact (V4): the plan claims to be the only home of
   the method, so look for a second copy, in this repo and in what the delta says it folded.
   Find tests that would stay green on a broken delta by mutating scratch copies of `ccfleet`,
   `modelguard`, a router and the menu. What the delta duplicated or ignored that atelier already
   holds (`cclive`, `ccrepo`, `pins.py`, the work-run skill's single-source guard).
4. **Security & privacy**, mandatory. Design altitude: an unattended session in every repo (what
   a wrong config, a repo's own settings or instruction file, or a hostile pull request can make
   it do now that the config is the whole grant; what the kept hooks and the appended user-level
   instruction file bring into a session working in a public repo), the private-name guard's
   reach, what the review log, result files, settings files and plan output collect and where they
   sit. Code altitude: the likely vectors for the class, checked against an open catalogue (OWASP
   ASVS or the domain's equivalent), not recalled: values from the config, the jobs file, the
   queue's output (now JSON from `evidence` and `owed`) and session transcripts flowing into paths,
   argv, prompts, tables and git commands; for `modelguard`, every way a launch with no model can
   pass, and every ordinary command it now refuses. Aim `/security-review` at the code only from
   a clean tree; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once, on 2026-11-24 UTC, at
`26a4fe7e`, from the places named. At `5696f91a` the widener re-ran every line except the two
`test_ccfleet` runs, the two `test_modelguard` runs and the synthetic dry runs (no file those
cover changed between the two pins: only Part C did), plus the lines Part C added. Both sets of
results are held in the sibling. Read exit codes
explicitly. Check `uptime` first; one heavy process at a time, under `nice -n 10`, foreground
with a long timeout (the `ccfleet` suite takes about four minutes per interpreter).

From the worktree root:

```
git merge-base --is-ancestor 6a98df21 HEAD; echo "exit=$?"
mandoc -T lint -W style instruments/man/ccfleet.1; echo "exit=$?"
python3 instruments/ccfleet --help; echo "exit=$?"
python3 instruments/atelier-menu/menu.py --selftest; echo "exit=$?"
python3 instruments/atelier-menu/menu.py review; echo "exit=$?"
python3 instruments/atelier-menu/menu.py session; echo "exit=$?"
```

From `instruments/` (the tests load their subjects by path; run `ccfleet`'s on both
interpreters, since the runtime claim is 3.8 or later):

```
nice -n 10 python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 10 /usr/bin/python3 -m unittest -q test_ccfleet; echo "exit=$?"
nice -n 10 python3 -m unittest -q test_atelier_menu; echo "exit=$?"
```

From `tools/` (the second line is the interpreter the user-level hook runs under):

```
nice -n 10 python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 10 /usr/bin/python3 -m unittest -q test_modelguard; echo "exit=$?"
nice -n 10 python3 -m unittest -q test_subject_skills test_templates test_work_run_single_source; echo "exit=$?"
nice -n 10 python3 -m unittest -q test_session_close_single_source; echo "exit=$?"
nice -n 10 /usr/bin/python3 -m unittest -q test_session_close_single_source; echo "exit=$?"
```

**A dry run on a synthetic config**, in your scratchpad only. Make two throwaway git repos with no
remote under a scratch `repos_root` (one marked public, one private, the public one holding a
dummy brief); a config whose `kit_dir`, `repos_root` and `worktrees_root` are scratch
directories, `claude_bin` set to `/usr/bin/false` (so nothing can start a real session), one
invented private name, a pass template, a plain run template with no `{ITEM}`, and a `queue`
whose `next`/`ranked`/`take`/`release`/`evidence`/`owed` are a small scratch script that logs
every call it receives, offers one pick until it is in `{LAUNCHED}`, prints one evidence row and
one owed row as JSON, and whose `ranked` exit code you can set; a copy with no `queue.ranked`
and its own `kit_dir`; a copy with no `queue.evidence` and its own `kit_dir`. Then, with
`--config` on each:

```
python3 instruments/ccfleet --config <cfg> check; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> check --prompt <pass template>; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> gate; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> plan; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> plan --json; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> --by <your id> drain --dry-run; echo "exit=$?"
RANKED_RC=1 python3 instruments/ccfleet --config <cfg> --by <your id> drain; echo "exit=$?"
python3 instruments/ccfleet --config <cfg without ranked> --by <your id> drain --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg without ranked> run <public repo> \
  --prompt <plain run template> --dry-run; echo "exit=$?"
python3 instruments/ccfleet --config <cfg without evidence> plan; echo "exit=$?"
python3 instruments/ccfleet --config <cfg> run <public repo> \
  --prompt <template naming the private name> --dry-run; echo "exit=$?"
```

(`RANKED_RC` is how the brief-writer's scratch queue read the exit code to give `ranked`; use
your own mechanism.) Read `<kit_dir>` afterwards: `driver.log`, every file the runs left (and
any they should have left and did not), and the scratch queue's own log of the calls it
received, in order. How the brief-writer built its config, and what it saw, is in the sibling.

**Live behaviour.** The claims about real `claude -p` (stdin, the JSON log, the wait ceiling,
`--session-id`, `--setting-sources`, `--settings`, `--append-system-prompt-file`, the transcript
store's layout and timestamps, the billing label) rest on a stand-in binary in the tests, and the
routers' behaviour rests on a model following prose. Re-drive what you can read-only: the
transcript store's layout and an entry's `timestamp` and `type`, read through a scratch script
that prints keys and counts, never content; `ccrepo`'s labelling rule from its source. At most
a few real launches, and only if the session running you may spend on them, all on the cheapest
model, in a throwaway repo under your scratchpad, with no permission-mode argument: one `ccfleet
run` whose prompt only prints a `RESULT:` line; and headless `claude -p` sessions started in a
scratch directory with the plugin loaded from your worktree, sending a bare `/atelier:review`,
`/atelier:review drain` and one other near-miss, each told to report what it read and ran; and,
in a scratch directory that is not a repo, a bare `/atelier:session`, `/atelier:session closing`
and `/atelier:session close`, each told to report what it read and ran and to make no write
outside that directory.
Otherwise mark them NOT RUN with grounds. Never run `ccfleet` against a real repo, never `drive`
or `drain` for real, and never with a real config. The brief-writer ran none of these launches.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. A check that needs a write is
  marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Other sessions' transcripts are read only through
  a script that prints keys and counts; quote none of their content. `ccfleet check` prints the
  user-level hooks and instruction-file path: quote neither. Probes use scratch copies and
  synthetic fixtures under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad, and
  never touch the primary checkout (the hook, the installed `ccfleet` and the in-place plugin run
  from it). Child repos are read-only and reported by count only, never by name or path.
- Never run an installed tool by bare name from `PATH`: use `instruments/ccfleet` or
  `python3 tools/<x>.py` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief dirty.
- This pass is pending while you run it: anything you write to a pointer or a commit subject before
  phase 2 names the held-back sibling by count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at about 100 columns; NZ English. This repo
  is PUBLIC: quote no secret, email address, home path, private repo name or estate fact.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

**Reviewer's start-up reading:** skip the session-log step of the repo's read order; the log is on
rule 2's barred list.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material is held outside the repo under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/sessions/`, every
prior verdict in `docs/reviews/` (the first pass's above included), every item under
`docs/roadmap/160-doctrine-review-owed/` beyond its title, the delta commits' message bodies,
`docs/method/census/`, and beyond their first line:

- `docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md`
- `docs/roadmap/210-instruments-open-features/470-fix-ccfleet-and-its-two-skills-fl1-fl25.md`
  (the fix record; it summarises the first verdict)
- `docs/roadmap/210-instruments-open-features/500-modelguard-reads-a-lookup-of-claude-as-a-launch.md`
- `docs/roadmap/210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md`
- `docs/roadmap/210-instruments-open-features/570-modelguard-refuses-ssh-as-the-claude-user.md`
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md`
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/020-every-command-is-subject-then-action.md`
- `docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/030-a-close-command-so-the-close-text-is-not-pasted.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md`
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md`

All of these carry an author's account of the work, and two carry the first verdict's findings.

**This brief's held-back sibling is not in the tree.** Whoever orchestrates the pass holds it
outside the repo and every worktree, and releases it to you only after your act 1 is committed;
by count it holds 34 questions and 19 facts. Never look for it in git history, other checkouts,
scratchpads or temporary directories. Run by hand with no orchestrator, you open it yourself, as a
deliberate second act, after act 1 is committed, and disclose when.

The delta's own comments, docstrings, manual, skills, prompts, tests and `CHANGELOG.md` entries
carry the authors' account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/210-instruments-open-features/440-ccfleet-per-repo-billed-headless-sessions-and-two-skills.md \
  --also-exclude docs/roadmap/210-instruments-open-features/470-fix-ccfleet-and-its-two-skills-fl1-fl25.md \
  --also-exclude docs/roadmap/210-instruments-open-features/500-modelguard-reads-a-lookup-of-claude-as-a-launch.md \
  --also-exclude docs/roadmap/210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md \
  --also-exclude docs/roadmap/210-instruments-open-features/570-modelguard-refuses-ssh-as-the-claude-user.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/020-every-command-is-subject-then-action.md \
  --also-exclude docs/roadmap/450-one-home-and-one-command-prefix-mike-commissioned/030-a-close-command-so-the-close-text-is-not-pasted.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/210-a-plan-mode-that-shows-the-drain-before-it-runs.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/240-a-work-plan-mode-for-work-run.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/410-evidence-17-says-nothing-inspects-shell-commands-modelguard-does.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/500-census-slice-4-doctrine-defects.md \
  --also-exclude docs/method/census \
  "ccfleet|modelguard|review plan|review run|subject|session close"
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the
re-run list, over the whole delta as it stands at your HEAD, cold: you have not read the first
verdict, so judge the code and skills on their own terms, not as fixes. Append your verdict below
a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, any
orchestrator with its spawn prompt, what you read, the UTC day, the HEAD you pinned), per-lens
answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption damaged or
confirmed with its probe, a per-commit ledger (read body-free yes/no, findings by id), findings
with stable IDs (prefix `RK`: `RK1`, `RK2`, …) and severities (MAJOR / MODERATE / minor / note),
an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, the method record
`REVIEW.md` § *The lifecycle* requires, and a follow-up checklist. Give the plan-and-run path its
own line in the per-lens answers. Then STOP: act 1 is committed, unrevised, **before** the sibling
or the first verdict is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling, the first verdict and the barred records; screen the delta
commits' bodies. Append `### Reconcile` beneath your verdict, with:

- **The FL ledger, one row per finding FL1–FL25 of the first verdict:** what it counselled (by
  pointer, not restated at length), the commit and file:line that answers it, how you re-drove it
  at your HEAD (the command and its result, or the first verdict's own reproduction re-run), and
  its state: *fixed as counselled* · *fixed another way* (and whether that way meets the finding)
  · *partly fixed* · *not fixed* · *regressed*. Reading a fix is not re-driving it (V2). Where a
  fix went beyond or against the counsel, say so and judge it.
- Per-finding notes on your act-1 findings against the sibling's questions and the authors'
  account; any finding formed at reconcile, marked as such, with an `RK` id after your last.
- The residual risk, named: act 2 reads the first verdict, so the FL ledger is anchored on it by
  design; act 1 is the cold half.
- The overall line restated.

Never revise act-1 text. Then fold the sibling in below the reconcile.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per
finding is welcome, labelled as counsel and kept beneath it. Under the overall verdict, say
plainly in three lines: whether anything you found loses or misreads paid review work; whether
`/atelier:review plan` and `/atelier:review run`, with `ccfleet` as it stands, are safe to run
the principal's paid weekly drain from, and if not, what must change first; and whether
`/atelier:session close` runs his close and only his close. Name `160/1450`, `160/1790` and
`160/1740` in your scope line, so all three can close on this verdict, and `450/030` as the item
Part C answers to.

---

# Verdict, act 1 (cold): `ccfleet`, the subject commands, plan and run, `modelguard`, the close

**Scope:** board items `160/1450` (the re-check), `160/1790` (the new build) and `160/1740` (the
whole-grant and unlanded changes), all three closing on this verdict, with `450/030` as the item
Part C answers to. Reviewed as it stands at `2111e260` (`origin/main` when the pass started,
2026-11-25 UTC). The since-line from `5696f91a` to that head is empty on the delta paths, so the
delta had not moved.

**Overall: PASS-WITH-FINDINGS. 0 MAJOR, 10 MODERATE, 14 minor, 4 notes (28 findings, `RK1` to
`RK28`).** Act 1 only: the first verdict, the held-back sibling and every barred record are
unread.

Three plain lines, as the brief asks:

- **Does anything found lose or misread paid review work?** Not on the ordinary paths: under a
  stand-in session binary, an error end, a nonzero exit, a killed driver and a clean end with
  unlanded work each kept the claim, the worktree and the review log, and `resume` finished the
  two I resumed. Three narrower paths do misread or lose: a final report that mentions `RESULT:
  DONE` after its real result line reads as DONE (`RK3`); a launcher killed by a signal other than
  an interrupt leaves its session running unwatched, and a `resume` started meanwhile removed the
  worktree under it (`RK4`); and a pass finished by `resume` leaves no result file, so a close that
  counts from the result files still reads it as cut off (`RK6`).
- **Are `/atelier:review plan` and `/atelier:review run`, with `ccfleet` as it stands, safe to run
  the paid weekly drain from?** The runner's own handling of claims, worktrees and verdicts is
  sound enough to drain from, and I found no MAJOR. Two things sit on the drain's own path and are
  cheap to settle first, or to accept knowingly: the per-pass orchestrator prompt now points at its
  reviewer-prompt template by a path that does not exist in the repo it runs in (`RK2`, new with
  the rename, not driven live), and a fold after the reset is refused until the config's reset
  time is moved, which the skill does not say (`RK5`). Then one canary pass on the real config
  before the full drain, because three things could not be seen from here: the private queue tool
  that holds the seal (a non-goal), a real usage-limit end, and whether the real config still
  grants its sessions enough now that user-level grants no longer load (`RK12`).
- **Does `/atelier:session close` run his close and only his close?** By its text, yes: it points
  at the one section, copies none of it, reads the committed copy and stops when the heading is
  gone. Live, it did not run at all in the one launch the brief allowed: a headless session outside
  the plugin's directory was refused the read of the action file (`RK1`), so "and only his close"
  is judged from the text and the guard test, not from a session that ran it.

## Provenance (rule 4, V7)

- **Reviewer:** one fresh session on **Fable 5.2** (`claude-fable-5-2`), the principal-named review
  tier, started for this pass alone as a subagent of the orchestrator below. It read the delta,
  answered the lenses, formed every finding and wrote every severity here.
- **Orchestrator, off-tier, disclosed:** session `4a34637a` (`atelier-a9`), Opus 5.5, opened by the
  principal to run this pass. By its own account in the spawn prompt it holds the context
  partition, commits the records and releases the held-back sibling after act 1 is committed; it
  forms no finding and writes no severity; it authored, started and instructed no part of the delta
  or the brief. Its direction to me was process only. The barred-set choice: exactly the brief's.
- **Spawn prompt, verbatim**, with three form-only substitutions made by me because this repo is
  public and the prompt holds absolute paths under a home directory: `<WT>` stands for the review
  worktree's absolute path, `<SCRATCH>` for the orchestrating session's scratch directory and
  `<PRIMARY>` for the primary checkout's path. Nothing else is changed; the orchestrator holds the
  original file.

````text
You are the reviewer for one rule-4 cold pass in the atelier repo. You run on Fable, the
principal-named review tier. State your model in your verdict's provenance.

**The brief:** `<WT>/docs/reviews/2026-11-24-2141-ccfleet-recheck-and-subject-action-review-plan-cold.md`.
Read it whole first, then follow it and `docs/method/REVIEW.md` exactly. It defines the scope,
the barred reading, the re-run list, the deliverable and the two acts. Nothing here changes it.

**Your worktree:** `<WT>` (branch `atelier-a9-rk-pass`, HEAD
`2111e260`, which is `origin/main`; the only commit after the brief's repin chain is my claim,
touching two board items under `docs/roadmap/160-doctrine-review-owed/` and `docs/ROADMAP.md`,
which are on your barred list). Run every command from it, with absolute paths. It is read-only to
you except the brief file, where you append your verdict.

**Your scratch directory:** `<SCRATCH>/rk/`
(create it). All probes, scratch clones, synthetic configs, fixtures and working notes go there.
Delete your fixtures when you finish act 2.

**Who I am, disclosed (rule 4):** session `4a34637a` (`atelier-a9`), Opus 5.5, opened by the
principal with the instruction to run this pass. I am an off-tier orchestrator: I hold the context
partition, commit the records and release the held-back sibling after your act 1 is committed. I
form no finding and write no severity. I authored, started and instructed no part of the delta or
the brief. My exposure before spawning you: the brief whole; `REVIEW.md` rule 4 and *The
lifecycle*; board items `160/1790` (most of it), `160/1450` and `160/1740` (heads and tails,
which carry authors' accounts); recent commit subjects; one earlier claim commit as a format
model. I have not opened the held-back sibling or any prior verdict. Record this prompt verbatim
in your provenance; it is saved at
`<SCRATCH>/rk-spawn-prompt.md`.
The barred set is exactly the brief's; I add nothing and remove nothing.

**Process rules:**

1. **No git writes.** No commit, add, checkout, switch, stash, reset, push or worktree command in
   `<WT>` or anywhere else. Read-only git (log, diff, show via
   `coldsweep`, merge-base, ls-files, grep) is fine. I commit. A scratch clone under your scratch
   directory is yours to do as you like with.
2. **Never touch the primary checkout** `<PRIMARY>`: the live hook, the installed
   `ccfleet` and the in-place plugin run from it. Read nothing there either; your worktree is at
   the same commit. Never run an installed tool by bare name from `PATH`.
3. **Machine load.** Other sessions are live on this machine (load about 14 on 12 cores when I
   spawned you). Check `uptime` before each heavy step, run one heavy process at a time under
   `nice -n 10`, in the foreground with a long timeout (the `ccfleet` suite takes about four
   minutes per interpreter; use a 600000 ms timeout). Never background a test run.
4. **Real launches:** you may spend on the few real launches the brief's *Live behaviour*
   paragraph lists (at most one `ccfleet run` and six headless `claude -p` sessions), all on the
   cheapest model (`--model haiku`), in throwaway directories under your scratch directory, with no
   permission-mode argument, exactly as the brief bounds them. Nothing more. No real config, no
   real repo, no `drive`, no real `drain`.
5. **Subagents:** if you start any, give each an explicit `model`, keep it read-only, and have it
   write its report to a file in your scratch directory and return three lines. Any subagent that
   reads the delta and forms judgement must be Fable; the findings and severities are yours.
6. **Public repo.** Quote no secret, email address, home path, private repo name, estate fact or
   other session's transcript content. Absolute ISO 8601 dates from `date -u`; NZ English; prose
   wrapped at about 100 columns. Finding prefix `RK`.
7. **Act 1:** append your verdict below a `---` divider at the end of the brief file, complete per
   the brief's *Process*, then STOP and reply to me in at most five lines: that act 1 is written,
   the overall line with counts, and anything I must know to commit it (for example a floor
   marker you needed). Do not open the held-back sibling or the first verdict. The sibling is not
   in the tree; I release its path to you by message after I commit act 1.
8. **Act 2** starts only on my release message. Do it as the brief's *Phase 2* says, then reply in
   at most five lines.
9. **If a usage limit or error stops you,** stop where you are; your transcript persists and I
   will resume you by message. Keep working notes in your scratch directory so a resume loses
   nothing.

Budget the time this very large pass needs; never thin it to fit.
````

- **The wrapper message that carried it, verbatim** (same substitution): "Your full instructions
  are in this file; read it first and follow it exactly. It is also the text you record verbatim in
  your verdict's provenance: `<SCRATCH>/rk-spawn-prompt.md` (This wrapper message is the only text
  sent besides that file; record it too.)"
- **Release message:** none yet; act 2 has not started.
- **Contact:** none from any author session.
- **Review worktree:** the orchestrator's worktree of this repo on branch `atelier-a9-rk-pass`,
  read-only to me but for this file. Scratch: a `rk/` folder in the orchestrator's scratch
  directory, holding every probe, fixture, scratch clone and working note.
- **What I read:** the spawn prompt; this brief whole; `docs/method/REVIEW.md` whole; at HEAD and
  in full: `instruments/ccfleet`, `tools/modelguard.py`, `instruments/atelier-menu/menu.py` and its
  `SKILL.md`, `instruments/ccfleet.example.json`, the six routers (one whole, five by diff against
  it), `skills/review/` (`plan.md`, `run.md` and the three prompts whole; `brief.md` by search),
  `skills/session/close.md`, `skills/work/plan.md` and `run.md`, `skills/fleet/sweep.md`,
  `tools/test_session_close_single_source.py`, the *Ending the session* section of the session-open
  prompt, the manual's `pass`, queue-interface and THREATS text, `tools/README.md` on
  `modelguard.py`, both plugin manifests. By search or in part: the rest of the manual,
  `instruments/test_ccfleet.py` (its 103 test names, and through 22 mutations),
  `tools/test_modelguard.py` (through 12 mutations), `tools/test_subject_skills.py`, the fleet
  prompts, the moved `repo`, `worktree` and `fleet pins` action files, `README.md`, `CHANGELOG.md`,
  `ccclose`'s usage text and `ccopen` (one search each). The 17 commits body-free (ledger below).
- **Exposure to disclose.** My harness loaded the user-level and repo instruction files and a
  memory index before the brief; they hold private context this verdict does not carry, and the
  index's one-line titles include a few that read as an author's account of earlier `ccfleet` and
  review-batch work. None steered a finding that I can trace. I skipped the session-log step, read
  no file under `docs/sessions/`, `docs/roadmap/` or `docs/method/census/`, no prior verdict, and
  no commit message body. `docs/ROADMAP.md` was not opened.
- **Two Fable helpers, read-only, disclosed** (spawn prompt rule 5; each given an explicit model
  and the barred list, each wrote a report to scratch): one cross-checked every surface that
  states a `ccfleet` fact against the code; one swept the live references after the rename. Their
  own disclosures: the second ran `git show --stat --format=%s` on six commits (subject and stat,
  no body), ran one `--include-barred` sweep piped straight into a counter with no line displayed,
  and read old trees' file content with `git cat-file`; the first read one `grep` of
  `tools/pins.py`. Every helper item that became a finding here I re-drove myself or name as
  read-only. Severities are mine.
- **Process departures, disclosed.** (1) The spawn prompt said never to background a test run; the
  harness moves any command past 180 seconds to the background on its own, so both four-minute
  `ccfleet` suites and the mutation run finished there, one at a time, under `nice -n 10`. (2) I
  read file content from two old commits with `git show <sha>:<path>` (a blob, no message body) to
  compare one prompt line before and after the rename. (3) I ran the worktree's `ccclose` once, in a
  scratch directory that is no repo, to re-drive claim 35; its output named this session's own
  transcript and stayed in scratch.

## Method

In this order: the floor and the since-line; `REVIEW.md`; `ccfleet` read whole, noting candidate
defects before any probe; the review skills and prompts; `modelguard`; the close action, its test
and the section it runs; the routers and the menu. Then probes, all in scratch: the brief's
synthetic config and its eleven command lines; a stand-in session binary driven through ten end
states, a killed launcher, a killed driver, folds and resumes around a reset; 124 `modelguard`
commands and nine payload shapes on the interpreter the hook runs under; 22 mutations of
`ccfleet`, 12 of `modelguard` and 20 of the routers, the close action, the prompt, the plan, the
run, the menu and a manifest, each against its tests; the close action's own git commands across
three install shapes; the transcript store read by keys and counts only; six real headless
sessions and one real `ccfleet run`, all on the cheapest model, as the brief bounds them. Lens
4's catalogue was read, not recalled: the chapter index of OWASP ASVS 4.0.3 (V1 to V14), fetched
on the day.

**Left out, with grounds.** Any real config, queue tool, rulings file or run result (non-goals).
A real usage-limit end, a real resume of a real subagent across a process restart, and a real
per-pass orchestrator reading its template: each needs a paid pass beyond the launches the brief
allows, so each is NOT RUN and named where it bears. The close action beyond its refusal (`RK1`):
the brief's six-session bound was spent. Python 3.8: no such interpreter on this machine. Child
repos: none read. `/security-review`: discharged, because it reads this session's pending diff,
which on a clean tree at the delta's end is empty, and aiming it at the landed delta would mean
dirtying a worktree that is read-only to me; the code-altitude read was done by hand against the
ASVS chapters (lens 4).

## Load-bearing assumptions (lens 1), named before the brief's

| # | The assumption the work rests on | State | The probe |
|---|---|---|---|
| A1 | A session's end can be told clean from unclean by exit code and the JSON error flag | **Confirmed** for the stand-in; **not run** for a real limit | ten end states, below |
| A2 | The last `RESULT:` in a final message is the verdict | **Damaged** | `RK3` |
| A3 | A session dies with its launcher, or the launcher outlives it | **Damaged** | `RK4` |
| A4 | A model follows "check the first word" | **Confirmed**, five of five on the cheapest model | live launches 1 to 5 |
| A5 | An action's text can live in a file the model reads | **Damaged**: that read needs a permission the router does not carry | live launch 6, `RK1` |
| A6 | A headless orchestrator in a child's worktree can reach the review action's text | **Damaged** by reading; not run live | `RK2` |
| A7 | The adopter's queue enforces the plan and the seal | **Unverifiable here** (non-goal); nothing in this repo defines the seal | `RK7` |
| A8 | Past passes' logged cost predicts a review's cost | **Damaged** | `RK8` |
| A9 | Leaving out the user-level setting source leaves out its grants | **Confirmed** live for the default mode | the one real run |
| A10 | The private-name guard covers what a public repo's session is told | **Damaged** | `RK10` |
| A11 | "Committed" means hooked, tested and reviewed | **Damaged** (it means hooked) | `RK20` |
| A12 | No forwarder for the old names is safe | **Confirmed** for this repo's live surfaces; children judged by class | helper sweep, `RK22` |

## Per-lens answers

**Lens 1, approach.** The runner's central idea holds: the verdict is the launcher's reading of an
exit code, an error flag and one line, and anything unclean keeps everything. The first-word check
is a control a model followed every time it was tried, and behind it the tests pin its sentences.
Three assumptions do not hold as built: that action text can be loaded by an ordinary file read
(`RK1`, `RK2`), that a session's life is tied to its launcher's (`RK4`), and that a pooled cost
figure answers the question the principal asked of the plan (`RK8`). On the question the brief
puts: prose is a defensible home for a ranking **only because** a seal in code is meant to stand
behind it, and that seal is not in this repo, by design; what is in this repo neither defines its
interface nor tests the prose (`RK7`, `RK19`). "Owed" is defined more narrowly than `REVIEW.md`
defines what earns a review, and says so; the leftover list it promises the principal has no place
in the plan's output (`RK13`). The re-check's own question (did a fix move the risk) is act 2's;
cold, the place the risk now sits is the launcher's death and the result line, not the error end.

**Lens 2, correctness.** Claims 1, 2, 4 to 7, 9 to 12 and 14 held under probe, with the limits in
the claims ledger. Claims 3, 8, 13, 17, 21, 35 and 36 are overstated (`RK21`, `RK3`, `RK7`, `RK1`,
`RK22`, `RK1`, `RK19`). The interruption table below traces each point of a pass's life.

**The plan-and-run path, on its own line.** Walked as an adopter holding only this repo:
`/atelier:review run` loads the router, then `run.md`; that needs a private config and a rulings
file; `review plan` needs `queue.evidence`, a command this repo does not ship; the seal goes
"through the adopter's queue" with no key, command or input shape given anywhere; then `ccfleet
drain` calls `queue.ranked` once and trusts its exit code. So with only this repo nothing can
start, and with a queue built from the manual a paid pass can start with no plan and no seal in
three ways: `ccfleet pass` by hand (it calls `take` and never `ranked`; probed on a config with no
`ranked` at all); `ccfleet drain` against a `ranked` that always exits 0; and `ccfleet run` or
`drive` with the orchestrator prompt and three `--set` values. `resume` and a fold start sessions
without either by design. The gate is real only where the adopter's `take` and `next` refuse an
unsealed run, and only `run.md` says they must (`RK7`). For the principal's estate that tool is
private and outside this pass.

**Lens 3, completeness.** One home per fact mostly holds: the routers, the menu and the two
single-source actions are well pinned. The misses are mirrors: the manifests and the onramp's
companion list lack `session close`; the changelog has no entry for the rename, the plan, the
whole-grant change or UNLANDED; the manual, `--doc` and the skills disagree in a dozen small
places (`RK22`, `RK23`). The plan's claim to be the only home of the method is true of this repo's
prose, and by construction untrue of the whole: the adopter's `owed` and seal commands must
implement the same definitions, unseen. What the delta reused rather than duplicated: `pins.py`
for the pin, the work-run guard's helpers for the close guard. Mutation found the `ccfleet` suite
strong (19 of 22 broken copies caught) and the prose guards thin (`RK19`).

**Lens 4, security and privacy.** Design altitude: the manual's THREATS section is a real
enumeration (who can steer a session, what bounds it, what widens the grant), which is the
build-time step this lens asks for. Held: every queue, git and session command is an argument
list, never a shell string (ASVS V5); a repo name is refused as a path; labels and log names are
folded to safe characters with a hash; the per-session settings file is written mode 0600 (V12,
V14); the user-level default mode and allow rules did not reach a real session (V4, live). Not
held: the private-name guard reads the rendered prompt only, while the same launch appends the
operator's user-level instruction file to the system prompt of a session in a public repo (`RK10`);
the copies of that file and of the settings are never removed (`RK11`); the "whole grant" has more
exceptions than the three the manual lists (`RK12`); a repo's own non-approving hooks run code at
session start with no WIDENED line (said in THREATS, not at launch). `modelguard`: nine shapes
that start a session with no model pass (`RK15`), and a class of ordinary commands is refused
(`RK9`). No finding here is a vulnerability in tooling others adopt that needs the private
disclosure route: each is a limit of a guard that the documents already call a net.

## The standing checklist

- **V1, no claim stronger than its evidence:** run; findings `RK1`, `RK3`, `RK8`, `RK12`, `RK19`,
  `RK20`, `RK21`.
- **V2, re-run every recorded proof:** run; the whole re-run list reproduced (ledger below), and
  the two live claims that rest on a real session (`--session-id` honoured, user-level default
  mode not inherited) were re-driven once for real.
- **V3, a changed rule swept to every mirror:** run; `RK2`, `RK22`.
- **V4, one fact, one home:** run; `RK13`, `RK7`; the single-source guards for `work run` and
  `session close` hold (their copy checks pass, and a copied line fails them).
- **V5, no internal contradiction:** run; `RK5`, `RK13`, `RK23`. Cross-references checked for the
  rule reached: `run.md` to `plan.md` (reaches the ranking rules); `sweep.md` item 4 to `plan.md`
  step 1 (reaches the definition of owed); `fold-prompt.md` to `orchestrator-prompt.md` step 7
  (reaches the fold); `orchestrator-prompt.md` to `skills/review/run.md` (the rule is there, the
  path does not reach it from where the reader runs: `RK2`).
- **V6, security and privacy:** run by hand against ASVS 4.0.3; `/security-review` discharged with
  grounds (Method).
- **V7, spawn provenance:** stated in the brief and repeated above, with the spawn prompt.

## The claims, re-driven

| Claim | Result | Evidence |
|---|---|---|
| 1 error end never DONE | **Holds** | stand-in: error flag with `RESULT: DONE` text, and exit 1 with the same text, both read ERROR, no release; exit 1 with the stop phrase read BUDGET EXHAUSTED |
| 2 worktree removed only when clean and landed | **Holds**; "never by force" is pinned by no test | uncommitted file and unmerged commit both read UNLANDED and were kept; mutant m6 (adds `--force`) survived the suite |
| 3 id up front, on START and the claim | START and result head: **holds**, live. "And its claim": only where `take` records `{SESSION}`; the example's does not | `RK21` |
| 4 dry drain | **Holds** | dry drain called `evidence`, `owed`, `next` only; its launched list was gone at exit |
| 5 config is the whole grant | **Holds in the main**; exceptions wider than stated | live session ran in the default mode; `RK12` |
| 6 UNLANDED | **Holds** | as claim 2; `ended` called with UNLANDED, `release` not called |
| 7 time limit, hung child | Not driven by me; pinned by two tests that pass | suite |
| 8 transcript fallback shape | **Holds** for the fallback; the primary path has no shape test | `RK3` |
| 9 review log path, withdrawn move, hash | **Holds** by suite and by the paths seen in probes | suite; probe output |
| 10 drain refuses without the four commands; ranked once | **Holds** | exit 64; `RANKED_RC=1`: one `ranked` call with the id, `DRAIN EXIT: not ranked`, exit 1 |
| 11 plan reads only | **Holds** | queue log: `evidence`, `owed`; no kit directory created |
| 12 cost history, nothing estimated | **Holds as stated**; what it measures is `RK8` | code; mutant m7 killed |
| 13 a hand pass meets the same gate | **Not in this repo** | `RK7` |
| 14 earlier claims still made | Spot-checked: billing basename (live), private-name guard (exit 5), gate (hold at the default floor on this machine: 12 GB free against 20), one driver per kit directory, live ceiling file, children in their own session (killed driver: both passes ran on) | probes |
| 15 modelguard | **Partly** | `RK9`, `RK15` |
| 16 both interpreters | **Holds** | 6 tests OK on 3.14.6 and on 3.9.6 |
| 17 one file per action, a use loads only its own | True of the layout; the load itself can be refused | `RK1` |
| 18 first-word check | **Holds** live, five of five | launches 1 to 5 |
| 19 placeholders named in words | Holds in the routers; the action files still carry the literal placeholders, which nothing substitutes | `RK20` |
| 20 descriptions carry triggers; menu read at run time | **Holds** | menu mutants killed |
| 21 retired names gone from every live surface | **Overstated**: no dead command remains, but the names survive in live files as quotation and narration | `RK22` |
| 22 to 29 plan, run, brief, work plan | Text reviewed; no test pins any of it | `RK7`, `RK13`, `RK14`, `RK19`, `RK27` |
| 30 menu | **Holds** | selftest, 4 tests, mutants |
| 31 to 34 close: one section, committed copy, stop, typed words | **Holds by text**; not run | `RK1`, `RK19`, `RK20` |
| 35 works in any repo or none | `ccclose` half **holds** (run in a non-repo directory: every repo check reads "not a git repository"); the command half failed live | `RK1` |
| 36 the 14 tests | Pass; weaker than the docstring says | `RK19` |
| 37 router row, hint, prompt unchanged | **Holds** | diff of the routers; the commit's stat touches no prompt file |

## A pass interrupted at each point of its life

Stand-in binary, scratch repos with no remote. "Kept" means still there afterwards.

| Interrupted | Claim | Worktree | Session id | Review log | What `resume` or the next step finds |
|---|---|---|---|---|---|
| Before the claim (launcher killed after the worktree is made; by reading) | none taken | left behind, unowned | none | none | a leftover worktree for a sweep to clear; the drain takes the pick back off its list |
| After the claim, before START (by reading) | held | kept | given to `take` only | none | the drain logs "ended before its session started" though a claim is held; a narrow window |
| Mid-session: error end, nonzero exit | held | kept | START line, result file, `ended` | kept at its path | `resume` ran, released on a clean end, removed the worktree |
| Mid-session: the session prints the stop phrase | held | kept | as above | kept | the drain stopped at once |
| Mid-session: real usage limit | NOT RUN (needs a real limit) | | | | rests on the CLI ending with an error or printing no result line; either reads as not clean |
| Mid-session: reboot | held | kept (on disk) | START line in the pass's `.out`; on the claim only if `take` records it | kept (outside the repo) | not driven; by code nothing is released, and `resume` needs only those |
| Driver killed with SIGKILL | handled by each pass itself at its own end (here: kept, both read UNLANDED) | kept, as UNLANDED says | as above | as above | both passes ran on to their END lines and called `ended`; the next driver counted them as holding slots |
| Driver's terminal closed | not driven; the passes are in their own sessions, as the killed driver showed | | | | |
| **The pass's own launcher killed with SIGTERM** | held | kept | START line only | kept | **the session ran on, unwatched; no END, no result file, no `ended` call; a `resume` started then was accepted** (`RK4`) |
| After the session, before the release (by reading) | held | kept | all three | kept | not driven; the END line says DONE while the claim stays, and a `resume` would release it |
| During a fold (by reading) | held | kept | as above | whatever the fold left | a second fold; the fold prompt has no "already folded" clause (`RK6`) |
| After the reset | | | | | **`resume` runs; a fold is refused with exit 3** (`RK5`) |

## Findings

Each is the principal's to decide (rule 3); nothing here is applied. Counsel, where given, is
labelled and sits beneath the finding.

### MODERATE

**RK1. An action's text is loaded by a file read that the router does not carry permission for;
`/atelier:session close` could not run in the one live launch.** Claims 17 and 35. Probe: a
headless session on the cheapest model, in a scratch directory that is no repo, the plugin loaded
from the review worktree, no permission-mode argument and no user-level settings, sent
`/atelier:session close`. Its only tool call was a read of `skills/session/close.md`; the harness
answered that permission to read that path had not been granted; the session stopped and said so
(it did not close from memory, which is the right failure). The five router launches before it
worked because the menu is a `python3` call the router's `allowed-tools` covers. The cause is the
shape, so it is not special to `close`: every one of the sixteen actions now reaches its text
through a read of a path outside the session's own directory, where the old one-skill-per-command
form had the harness load the text itself. Effect by reader: an interactive user without a
standing grant is asked once per action file; a headless session without one (a `ccfleet` session
most of all, since `9ba5c6b6` strips the user-level allow rules) is refused. On the principal's
own machine a standing grant probably hides this; I did not open his settings to check. Criterion:
the brief's worst failure "a command that does something other than what was typed", and claim 35's
"works in any repo ... or none". Not driven: whether adding the read to the router's
`allowed-tools` clears it.
*Counsel:* try `Read` in each router's `allowed-tools` and re-run this one launch; if the harness
does not honour it for a path outside the directory, the action text has to come back inside what
the harness loads.

**RK2. The per-pass orchestrator and the fold are told to read `skills/review/run.md`, a path that
exists only in atelier, from inside another repo's worktree.**
`skills/review/orchestrator-prompt.md`
line 17 ("the atelier `/atelier:review run` action (`skills/review/run.md`; its reviewer prompt
section is your template)") and line 23 ("Fill in the skill's reviewer prompt");
`skills/review/fold-prompt.md` line 7. Neither prompt has an `{ATELIER}` variable, though the same
sweep gave the fleet prompts `{ATELIER}/skills/...`. Before the rename the line read "the atelier
`review-drain` skill", which a session loads by name with no file read (`git show
0c67dc0f~1:skills/review-drain/orchestrator-prompt.md`, line 17). Now the three routes left to the
orchestrator each fail or mislead: the relative path is absent from its worktree; the absolute one
is unknown to it and, by `RK1`, needs a read permission a narrowed config does not give; and the
skill by name is a router that says to follow `run.md` "as written", which is a drain, not a
reference. Step 4 of the prompt repeats most of the reviewer prompt's duties inline, so the likely
result is a thinner reviewer prompt, not a lost pass. NOT RUN live: it needs a real orchestrator.
Criterion: V3, and the brief's "a skill that stamps a wrong rule"; this is the template every paid
review's prompt is built from, and the rename changed it from working to unresolved.

**RK3. The verdict is the last `RESULT:` anywhere in the final message, so a failure report that
mentions `RESULT: DONE` reads as DONE.** `instruments/ccfleet` `RESULT_RX` (line 233, not anchored
to a line start) and `result_word` (lines 706 to 717, last match). Probes: `result_word("RESULT:
FAILED\nITEM: a:b\nVERDICT: n/a\nNOTES: the fold never reached RESULT: DONE", ...)` returns
`DONE`; a stand-in session that exited 0 with the one sentence "I could not finish act 2. The
prompt said to end with RESULT: DONE once landed, but nothing landed." was read `result=DONE`, its
claim released and its worktree removed. The prompts forbid a *line beginning* `RESULT:` outside
the final output; a mention inside NOTES is not a line beginning it. The shape test (`ITEM:` or
`REPO:` line) guards only the transcript fallback, never this primary path. The UNLANDED check
bounds the harm: where the reviewer's text or an unpushed commit is in the worktree, the pass
still reads UNLANDED and everything is kept. So the loss case is a pass that ended with nothing
unlanded, read as done. A second door of the same kind: a log that is not JSON at all but holds
`RESULT: DONE` in its last 4,000 characters read DONE at exit 0, where the manual says unreadable
output reads UNKNOWN. Criterion: claim 1's own sentence, "a cut-off pass is never read as DONE",
and claim 8.
*Counsel:* take the first `RESULT:` that begins a line of the final output, and require the shape
line on the primary path too.

**RK4. A launcher that dies by any signal but an interrupt leaves its session running, unwatched,
and `resume` does not notice.** `launch()` ends the session's process group only on an exception
(`instruments/ccfleet` lines 871 to 873); SIGTERM, SIGHUP and SIGKILL end the launcher with no
exception, and the session, in its own process session by design, runs on. Probe: `ccfleet pass`
with a stand-in that sleeps; `kill -TERM` to the pass process; the pass was gone, the stand-in
alive; the `.out` held START and no END; no result file; `ended` never called. A drain driver
watching that pass would log "its session was cut off", which is untrue while it runs. Then
`ccfleet resume` of that same session id, started while the first still ran, was accepted, ended
DONE, released the claim and removed the worktree; the original, still running, had its directory
taken from under it and its late write was lost. The resume lock stops two resumes; nothing stops
a resume beside the original. How it happens in practice: stopping a drain with a process kill
aimed at `ccfleet` (it reaches every pass launcher and no session), or closing the terminal of a
`pass`, `resume` or fold run by hand. Harm: budget spent by sessions nothing harvests, and the
narrow case of a resume racing a live original. Criterion: the brief's "a pass ... whose claim,
worktree, session id or review log cannot be recovered; a finished pass read as unfinished".
*Counsel:* record the session's process id beside the claim and have `resume`, and the drain's
"cut off" line, check it is gone first.

**RK5. After the reset, the cheap fold is refused and the review-tier resume is not; Mode 2 does
not say why or what to change.** `run_one` checks `reset_reached` first (line 1029), and a fold is
`run --in WT --item ITEM`; `resume()` has no such check. Probe on a config whose `reset_utc` had
passed: the fold printed `RESET reached; not starting` and exited 3; `resume` of the same pass ran
and released. `skills/review/run.md` Mode 2 is headed "after the reset" and sends passes whose act
2 is written to exactly that fold; its Close removes "one-off entries" and names `vars.HOLDS`, not
`reset_utc`. The manual says of `reset_utc` "No session starts at or after it", which `resume`
contradicts. A session following the skill meets a refusal on the one step that costs no review
budget. Criterion: V5, and the principal's sentence the brief holds the drain to: "we will resume
the work when the budget replenishes".

**RK6. What a resume and a fold leave behind does not match what the skill reads afterwards.**
Three linked gaps, each probed. (a) `resume` writes no result file and its END line names the JSON
log; the result file of the pass it finished still says ERROR, and `run.md` step 4 and Close step
5 count verdicts "from the rows: the result files ... and the launched list". A pass finished by
resume is counted as cut off. (b) The fold and resume commands as `run.md` prints them carry no
`--by`, so `release` and `ended` are called with `unknown` (seen in the queue log) and the fold
prompt renders "Drain session unknown started you"; an adopter's `release` that checks the holder
would refuse, exit 2. (c) A fold's result file is `results/<day>/<repo>.md` unless `--label` is
given, and `run.md` gives none: two folds in one repo on one day overwrite each other's result,
which the skill tells the drain session to read before deleting the held copy. Also here: the fold
prompt has no clause for a fold that was itself cut off after appending.

**RK7. The seal has no interface in this repo, and the gate on a pass started by hand exists only
as a sentence in `run.md`.** `run.md` lines 71 to 77: "the adopter's queue makes `ranked`, `next`
and `take` refuse until this run's ranking is sealed, so a pass started by hand (`ccfleet pass`)
meets the same gate as a drain". The manual's contract for `take` says only "Any nonzero exit
means another session holds it"; for `next`, nothing about a seal; no `seal` key, command or input
shape appears in the manual, `--doc`, the example config or any README (`grep -n -i seal`: five
hits, each "the seal is the adopter's queue's" or "must ... seal ... nothing"). Probe: `ccfleet
pass` on a config with no `queue.ranked` at all started its session after one `take` call. The
seal's five refusal rules (`run.md` lines 79 to 84) are requirements on software this repo neither
ships nor specifies nor tests. For the principal's estate the tool exists and is out of scope; for
any other adopter, and for a reader asking what in the public repo stops an unplanned paid pass,
the answer is `queue.ranked`'s exit code and nothing else. Criterion: claim 13; the brief's "a
seal or gate that a drain can pass without a plan".
*Counsel:* state the seal's contract where the other queue commands are stated, with what `take`
and `next` must refuse, and ship a small reference queue the tests can drive.

**RK8. The plan's cost estimate is one pooled figure that cannot answer "for a review of that
size", leaves out the costliest passes, and may leave out the review itself.** `plan.md` step 4:
"from measured past passes on that route, for a review of that size (`ccfleet plan`'s history
...)". `pass_history` returns one count, median and maximum over every clean drain pass
(`instruments/ccfleet` lines 1707 to 1748): no size, repo or item, so every row of the plan gets
the same number or "no measurement". It counts only passes that ended clean in one session: a pass
cut off and finished by `resume` or a fold has no row, and neither has a pass run by hand, so the
long passes most likely to hit a limit are the ones excluded. And the figure is the orchestrator
session's `total_cost_usd`; the function's own docstring says the reviewer subagent's share is
"whatever the CLI folds in". The reviewer is the review tier and the bulk of the spend. My one
real run had no subagent, so I could not settle it; the log does carry `modelUsage` and
`subagent_stats` keys. "Nothing is estimated" is true; what is measured is not shown to be the
thing asked for. Criterion: V1, and the principal's commission quoted in `plan.md`: "estimated
budget/API spend".

**RK9. `modelguard` refuses a class of ordinary commands: any command it does not know, holding
the word `claude` with a word after it.** Sixty ordinary commands were driven on the hook's own
interpreter (`/usr/bin/python3 -I`). Refused, though none starts a session:

````text
su - claude -c 'ls'                      docker exec -u claude box ls
runuser -u claude -- ls                  psql -U claude -d db -c 'select 1'
mysql -u claude -p                       journalctl -u claude -n 50
systemctl status claude --no-pager       tmux new -s claude -d
docker logs claude --tail 5              fd claude src
zgrep claude log.gz                      python3 -m pytest -k claude tests
ccrepo claude --json                     useradd -m claude -s /bin/zsh
ssh host 'su - claude -c ls'             smbclient -U claude //host/share -c ls
````

Passed, as claim 15 says: `ssh claude@host ls`, `ssh -l claude host 'ls /mnt'`, `scp`, `rsync` and
`sudo -u claude ls`. So the four transports and `sudo -u` pass, and the same class stays open for
every other way of naming a user, a unit, a container or a search term `claude`. The docstring
states the rule ("fails closed"); it does not state the cost, and the refusal's text tells the
session to add `--model`, which is wrong advice for every one of these. Criterion: the brief's "a
false deny that stops routine work".
*Counsel:* after an unknown head, count a later `claude` word only when a session flag or a prompt
follows it, and have the refusal say how to rephrase when no launch was meant.

**RK10. The private-name guard reads the rendered prompt only; the same launch appends the
operator's user-level instruction file, unscanned, to the system prompt of a session in a public
repo.** `build_prompt` runs `private_hits` on the template's rendered text; `session_files` writes
the user-level instruction file to `<kit_dir>/settings/<id>-user-instructions.md` and
`session_argv` passes it with `--append-system-prompt-file` for every repo, whatever its
visibility. The docstring's lesson reads as absolute: "A public repo's prompt never names a
private repo." On this machine that file names private repositories (known from this reviewer's
own harness context, not opened for the pass, and not quoted). An interactive session in a public
repo loads the same file, so the exposure is not new; what is new since `9ba5c6b6` is that the
runner does the appending itself, beside a guard whose stated purpose is to keep those names out
of an unattended session's instructions. `check` says the file is appended; THREATS does not list
it among what the guard misses. Security finding: severity MODERATE (a publication cannot be
retracted; it needs a session to repeat a name it was only told). Recurrence prevention: run the
same guard over the instruction file for a public or unknown repo and either refuse, or print a
line per name at launch as WIDENED does for grants.

### minor

**RK11. Per-session copies of the user-level settings and instruction file are never removed.**
Twenty files after ten stand-in passes in `<kit_dir>/settings/`, each 0600 in a 0755 directory;
nothing in the code deletes them and the manual's FILES section gives them no lifetime. They hold
whatever the user-level `env` block and instruction file hold.

**RK12. "The config is the whole grant" has more exceptions than the three the manual lists, and
`check` is silent when the config grants nothing.** The session settings on this machine kept
sixteen top-level keys beside permissions and hooks, among them the enabled plugins (which bring
their own hooks and skills), `env`, and the key that skips the bypass-mode confirmation; `check`
prints their names, the manual's list of what widens the grant names only repo settings, an
approving hook script and managed settings. `PERMISSION_FLAGS` does not include `--mcp-config`,
`--plugin-dir`, `--tools` or `--permission-prompt-tool`, so `check` does not name them. And the
reverse: a config with no permission mode and no allow rule now launches sessions that cannot do
anything that asks (the live run's transcript shows the default mode), and `check` prints nothing
to say so. For an estate whose sessions used to inherit user-level grants, that is the first thing
to confirm before a paid drain, and it reaches the fleet prompts too: they tell a worker to read
`{ATELIER}/skills/...`, a path outside its worktree.

**RK13. `plan.md`'s "owed" is narrower than the doctrine's, and the list it promises has no place
in its output.** Step 1: "A bare `⏳`, REVIEW.md's triggers, or a writer's view that it deserves
one do not count; those go to the principal as a list, never into a brief." `REVIEW.md` rule 4
makes the `⏳` pointer the queue entry any passing spawner may take and brief. A pointer whose
title says a pass is queued does count by "its item's own text", so the two rarely collide, but
"bare" is undefined. Step 5's output has the ranked table, the per-budget lines and the unbriefed
list, and no slot for the list step 1 sends to the principal. The definition also has a second
home by construction: `queue.owed`, the adopter's code, is what actually finds them.

**RK14. `run.md` gives the words typed after `/atelier:review run` no home.** The router says the
words after the action are its arguments "where the action's file names its arguments
placeholder"; `run.md` names none, and tells the session to quote the approval "from there [the
rulings file], never from memory". `work/run.md` and `session/close.md` each say where typed words
go. A principal who types his approval or a pacing target after the command has, by the text,
typed it nowhere.

**RK15. Nine shapes that start a session with no model pass `modelguard`, and none is in its deny
table.** Passed: `function f { claude -p hi; }; f` (the `f() { ... }` form is caught); `command
claude -p update` (the code strips `-p` after `command`, then reads the one-word prompt as a
management subcommand); `echo 'claude -p hi' | sudo sh` and `| env bash`; `python3 -c` with a
`subprocess` call; `at now <<EOF`; `git -c alias.x='!claude -p hi' x`; `set -- claude -p hi;
"$@"`; and the documented `${c}aude`. The docstring says each bypass found joins the table; these
are for it. Also unguarded, not probed: the harness's `Workflow` tool, a third route that starts
agents, passes the hook (the module says "Two routes start a model").

**RK16. A `pass` on a config with no `queue` dies in a traceback after making its worktree.**
`queue_call` reads `cfg["queue"][name]` with no check; probe: `KeyError: 'queue'`, exit 1, one
worktree left behind. The manual gives exit 64 for "pass ... without the config they need", and
the function's docstring says "never a traceback". By reading, `resume --item` with a `queue` that
lacks `release` does the same after the session has run.

**RK17. In a repo with no remote, a resume and a fold render a landing line naming branch `None`,
and leave the pass's branch behind.** Probe: the resume prompt's `{LANDING}` read "`merge
--ff-only None`"; after a fold removed the worktree, `fleet/<label>-<time>` was still in `git
branch`. The fleet prompts also say the worktree is "detached at the mainline", untrue with no
remote.

**RK18. `check --prompt` files `{BRIEF}` and `{ITEM}` under "filled only by pass or resume" for
prompts neither will fill.** `check --prompt skills/review/fold-prompt.md` lists `{BRIEF}` there;
a fold never fills it, and the fold launched as `run.md` prints it was refused with exit 5 for
`{BRIEF}`, `{FINISH_WORDS}` and `{HELD}`. `run.md` and `sweep.md` say `check --prompt` "names any"
unfilled placeholder first.

**RK19. The prose guards catch less than their docstrings say, and the plan, the run and the
manifests are pinned by nothing.** Mutations that stayed green: in `close.md`, a new rule added
inside an anchored paragraph ("Skip the section's step 2 when the principal seems busy"), "read
that section and the two before it, and follow all three", a fallback section named for when the
heading is missing, and a weakened missing-heading stop
(`test_session_close_single_source`, 14 tests OK each time; its docstring says it fails if the
action "grows an instruction the delivery job does not need"); in a router, `allowed-tools`
widened to all of Bash, an added line telling the session to start a drain, and the plugin root
said to be one level up; in `plan.md`, the read-only rule replaced by "seal it and start the
drain"; in `run.md`, "every run" made optional; in `plugin.json`, an action that does not exist.
Killed, to the tests' credit: a copied section line, the committed-copy read swapped for the
working file, the exact-first-word sentences, "menu and nothing else", the menu's wiring, and both
menu defects (8 of 20 killed, 12 survived). The test's own section finder also stops at a fenced
`## ` line with no failure. The single-source claim that matters (no copied line) is pinned and
holds.

**RK20. The close action's delivery text overstates what "committed" buys, and leaves a
plugin-only user without `ccclose`.** "Only text that has been committed has met the pre-commit
hook, the tests and review": it has met the hook. With the plugin installed in place, `HEAD` is
whatever the primary checkout has checked out, landed or not, pulled or not; with an install from
the remote, it is the installed copy until the plugin is updated, so a change to the principal's
close reaches such sessions later, silently. Both are defensible readings of "no drift between the
command and the text file"; neither is said. The section's first step is `ccclose` by bare name;
the plugin puts no such command on a user's path, and the action gives no path to it. The action
files also still carry the literal placeholders the routers explain in words (37 lines across nine
action files), so the commands in `close.md` and `work/run.md` rest on the model substituting
them by hand; run literally in a
shell with the variable unset, `git -C ""` reads the session's own repo (probed). The checkout
test is also a string comparison that a link defeats: reached through a symbolic link,
`rev-parse --show-toplevel` prints the resolved path, not "that same path" (probed), so by the
text the action falls back to the working file, pending edit included, though it must say so.

**RK21. The example config's `take` records no session id.** Claim 3 and `run.md` both say a
killed pass's id is on its claim; the example passes `take` the item, the holder and the brief
only, and leaves the id to `ended`, which a killed pass never reaches. The START line still has
it for a drain's pass; a pass run by hand prints it only to its terminal.

**RK22. The rename's mirrors: `session close` is missing from three lists, and the changelog has
no entry for the rename or the plan.** `.claude-plugin/plugin.json` and `marketplace.json` say
"sixteen actions" and list fifteen; `skills/session/onramp.md`'s companion list omits the close.
`CHANGELOG.md` has no entry for subject-space-action, `review plan`, `ccfleet plan`, `work plan`,
the whole-grant change, UNLANDED or the SHA-256 log names; its newest words on the commands other
than `close` are the retired names. Claim 21 as worded is overstated: no live surface tells a
reader to type a retired name (helper sweep, 137 hits classified), but the names stand in live
files as verbatim quotation and dated narration. The guard test cannot see a bare old name with no
`/atelier:` or `skills/` prefix, the `.githooks/` and workflow folders, or an invalid new-form
command. For children, by class: an old hand-held copy of the session-open prompt names a command
that no longer exists, and a runner config copied from the old example points `pass_prompt` at a
path that is gone.

**RK23. Surfaces that state a `ccfleet` fact disagree in small ways.** From the helper's
cross-check, each read against the code by it and spot-checked by me where a probe touched it:
both skills say `ccfleet --doc` tells who can steer a session, which only the manual does; the
manual says "only check, gate and `--dry-run`" start nothing, omitting `plan`; "a drain that
started a pass exits 0" is untrue after a failed `next`; `repos.<name>.branch` is read only with
no remote though the example sets it beside a remote-style note; the example's `~` paths in `vars`
and `env` are passed unexpanded into prompts that then double-quote them; the docstring's blanket
list of queue placeholders overstates what `ranked`, `next`, `evidence` and `owed` receive; the
manual mentions one earlier review-log name where the code reads two; `run.md`'s always-filled
list omits `{PIN}`; the manual's date predates the `plan` it documents.

**RK24. The fleet prompts' own verdicts `PARTIAL` and `BLOCKED` are not clean, so such a job keeps
its worktree and is run again by every re-run.** Probe: a stand-in ending `RESULT: PARTIAL` with a
clean tree, driven twice: two starts, two worktrees left. `adopt-prompt.md` has a BLOCKED that
"writes nothing" for a repo that is not the adopter's; that job re-runs each time. `sweep.md`'s
list of what keeps a worktree names a cut-off and uncommitted work only.

### notes

**RK25.** A refused claim counts toward the three-unclean stop, and a pick taken back off the
launched list can be offered again at once: a queue whose `next` does not skip claimed items ends
a drain as "failures" after three refusals, which reads as a spent budget. `drive` never reads
`reset_utc` itself (helper, by reading).

**RK26.** What the code suites do not pin. `ccfleet`, 22 broken copies, 19 caught (the error flag
ignored, an unranked drain allowed, UNLANDED switched off, user allow rules kept, the shape test
dropped, stale logs inherited, the wait ceiling dropped, an approving hook kept, release on any
result, no un-launch, a dry drain calling `ranked`, no session id, no appended instructions, the
guard skipping an unknown repo, the time limit read as an error, the user source loaded, the
resume lock off, unclean passes counted in the history, a resume that skips the unlanded check).
Three stayed green: `git worktree remove --force` with the removal-time check off (the earlier
UNLANDED reading still protects the work, so "never by force" is true today and pinned by
nothing); a session started in its launcher's process group; and a pass launcher not detached
from the driver, which is the claim "closing the driver's terminal does not end the sessions it
started" (a test's name says "detaches its passes"; it passes either way). `modelguard`, 12
broken copies, 10 caught; green with the parse-failure deny switched off, and with `--resume`
removed from the session flags.

**RK27.** `work plan` says it changes nothing; its first read, `ccopen`, runs a `git fetch`. The
router tells the session to say "none of them is an action" even when a later word is one (launch
3 said so of a sentence holding `run`). `MECHANISMS.md`'s table still says a slash command fires
"only when deliberately invoked" though every action now sits behind a skill whose description
carries trigger phrases.

**RK28.** "Python 3.8 or later" is tested on 3.9.6 and 3.14.6 only; the tool also needs `nice`,
`ps` and, on macOS, `memory_pressure`, which "standard library only; git on PATH" does not say.
On this machine free disk (12 GB) is under the gate's default floor (20 GB), so a drain with the
default gate would hold every start: a fact for the first paid drain, not a defect.

## Per-commit ledger

Every commit was read with `coldsweep --commit` and the brief's `--path` list (exit 0 each), never
with plain `git show`. "Whole" means I read the diff's stat and its files at HEAD in full; "stat
and HEAD" means the stat, the files at HEAD, and the diff by search, not line by line.

| Commit | Body-free | How read | Findings |
|---|---|---|---|
| `b99fa4be` | yes | stat and HEAD (`modelguard` whole at HEAD) | `RK9`, `RK15` |
| `e75fe749` | yes | stat and HEAD | `RK24` |
| `e9916406` | yes | stat and HEAD | `RK5`, `RK6` |
| `36e9ef0e` | yes | stat and HEAD (`ccfleet` whole at HEAD) | `RK3`, `RK4`, `RK16`, `RK17`, `RK25` |
| `c2d4e628` | yes | stat and HEAD | `RK6`, `RK18`, `RK23` |
| `5d99a2cc` | yes | stat and HEAD | `RK9` |
| `9ba5c6b6` | yes | stat and HEAD | `RK10`, `RK11`, `RK12` |
| `b95db160` | yes | stat and HEAD | none |
| `0c67dc0f` | yes | stat and HEAD (routers, menu, `review/` whole) | `RK1`, `RK2`, `RK19` |
| `bfa38582` | yes | whole | none |
| `10b32435` | yes | stat and HEAD; its added command references read line by line | `RK2`, `RK7`, `RK8`, `RK13`, `RK14`, `RK22`, `RK23` |
| `f354e542` | yes | stat and HEAD | none (the check it adds held live) |
| `6a98df21` | yes | stat and HEAD | `RK20` |
| `3620c908` | yes | whole | `RK1`, `RK19`, `RK20`, `RK22` |
| `dae1786d` (context) | yes | stat only | none |
| `ee6f384f` (context) | yes | stat only | none |
| `7a8a2305` (context) | yes | stat and the manifests at HEAD | `RK22` |

## Re-run ledger

All on 2026-11-25 UTC at `2111e260`, from the places the brief names. `python3` is 3.14.6,
`/usr/bin/python3` is 3.9.6.

| Line | Exit | Result |
|---|---|---|
| `git merge-base --is-ancestor 3620c908 HEAD` and `... 6a98df21 HEAD` | 0, 0 | both ancestors |
| the since-line (`git log --oneline 5696f91a..HEAD -- <delta paths>`) | 0 | empty |
| `mandoc -T lint -W style instruments/man/ccfleet.1` | 0 | no output |
| `python3 instruments/ccfleet --help` | 0 | 30 lines |
| `menu.py --selftest`, `menu.py review`, `menu.py session` | 0, 0, 0 | three and two rows |
| `python3 -m unittest -q test_ccfleet` | 0 | 103 tests, 236 s, OK |
| `/usr/bin/python3 -m unittest -q test_ccfleet` | 0 | 103 tests, 201 s, OK |
| `python3 -m unittest -q test_atelier_menu` | 0 | 4 tests OK |
| `test_modelguard`, both interpreters | 0, 0 | 6 tests OK each |
| `test_subject_skills test_templates test_work_run_single_source` | 0 | 79 tests OK |
| `test_session_close_single_source`, both interpreters | 0, 0 | 14 tests OK each |
| synthetic `check`; `check --prompt` | 0, 0 | the pass template's three names listed as pass-only |
| synthetic `gate` | 0 on a relaxed gate; 1 ("hold") on the default gate | 12 GB free disk |
| `plan`; `plan --json` | 0, 0 | one evidence row, one owed row, "no measurement"; queue log: `evidence`, `owed` |
| `drain --dry-run` | 0 | `DRY plan:` lines, `DRY queue.ranked not called`; queue log: `evidence`, `owed`, `next` ×3; dry launched list gone |
| real `drain` with `ranked` exiting 1 | 1 | `DRAIN EXIT: not ranked`; one `ranked` call carrying the id |
| `drain --dry-run`, no `queue.ranked` | 64 | refused |
| `run <public repo> --dry-run`, no `queue.ranked` | 0 | DRY lines, END `result=DRY` |
| `plan`, no `queue.evidence` | 64 | refused |
| `run <public repo>` with a template naming the private name | 5 | refused, the name printed |

Afterwards the kit directory held `driver.log`, `driver.pid` (emptied), `children.tsv`, one
`logs/pass-*.out` from the dry drain and an empty dated launched list from the refused real drain;
`plan` alone created nothing.

**Live, all on the cheapest model, 2026-11-25 UTC.** One `ccfleet run` in a throwaway repo, prompt
"reply with a RESULT line and a REPO line": exit 0, `result=DONE`, 1 turn; the JSON log parsed with
empty stderr; the id on the START line equalled the log's `session_id` and the transcript's file
name; the transcript sat under the project folder named for the worktree's path; every entry's
working directory had the repo's name as its basename (the billing key); the session's permission
mode was `default`; the worktree was removed. A kept user-level session-start hook visibly shaped
the reply (it added a line the prompt had not asked for), which is what "a kept hook runs with its
full power" means in practice. Six headless sessions, the plugin loaded from the review worktree:
`/atelier:review`, `/atelier:review drain`, `/atelier:review please run the drain of the briefed
reviews now`, and outside any repo `/atelier:session` and `/atelier:session closing`, each ran the
menu script and nothing else and read no action file (checked in each reply; the sixth also in its
transcript's tool calls); `/atelier:session close` is `RK1`. Total spend about 0.035 USD.

**NOT RUN, with grounds:** a real usage-limit end; a real orchestrator pass; a real resume of a
subagent across a restart; `drive` and `drain` for real; any real config (all barred or beyond the
brief's bound); the close action past its refusal (bound spent); Python 3.8 (absent).

## Follow-up checklist

- [ ] Rule each finding (rule 3). The two that bear on the first paid drain are `RK2` and `RK5`;
      `RK12`'s check of the real config's grant and one canary pass come before the full drain.
- [ ] `RK1`: decide how an action's text is loaded, then re-run the one refused launch.
- [ ] `RK3`, `RK4`: decide the result line's grammar and whether a session's process id is
      recorded; both want a test.
- [ ] `RK6`, `RK14`, `RK18`, `RK23`: one wording round on `run.md` and the manual.
- [ ] `RK7`: decide whether the seal's contract and a reference queue belong in this repo.
- [ ] `RK8`: decide what the plan's cost column should mean; settle the reviewer's share from one
      real pass log.
- [ ] `RK9`, `RK15`: the deny table and the unknown-head rule.
- [ ] `RK10`, `RK11`: the instruction file and the settings copies.
- [ ] `RK22`: the three lists and the changelog entries.
- [ ] Act 2: the FL ledger, the sibling's questions, the commit bodies and the barred records.
- [ ] Scratch fixtures deleted after act 2.

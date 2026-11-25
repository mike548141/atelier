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

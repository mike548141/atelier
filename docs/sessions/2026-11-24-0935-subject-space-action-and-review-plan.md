# 2026-11-24 09:35 UTC — Every command is subject, space, action; `review plan`

**Session:** `523be3be` (messaging name `atelier-e8`), Claude Opus 5.5,
principal-opened in the VS Code extension with `/atelier:work-run` and a typed
brief. Orchestrator in worktrees `atelier-e8-subject-action` and
`atelier-e8-no-old-questions`; three Sonnet workers (the live-reference sweep,
`ccfleet plan`, the `ccclose` check removal), no git writes by any worker. No
other atelier session was live; five ran in the estate root throughout.

## What was asked

His brief, verbatim: *"Build board 450/020 together with 180/210 and 180/240:
every /atelier: command becomes subject, space, action, a bare subject shows a
help menu, review plan holds the ranking logic that review run, review brief
and ccfleet's dry run all call, and work plan joins. Read all three items in
full first; my words in them govern. Confirm the rename table with me in one
line before moving anything. Don't wait for the 160/1450 re-check. Old names
stop existing, so sweep every live reference first; private repos' references
go to their own sessions."*

Mid-session, verbatim: *"No more asking me old questions from the repo like
you started doing tonight. Its not helpful"*. <!-- datescan:allow: his words, verbatim, 2026-11-24 -->

## What happened

- **Rename table confirmed** in one line, his pick: *"Go, as written
  (Recommended)"*, with one addition put to him: a bare `/atelier:worktree`
  shows its menu instead of running `list`.
- **Six subjects, sixteen actions** (`0c67dc0f`): `review` (plan, run,
  brief), `work` (run, plan), `fleet` (sweep, pins), `worktree` (start, list,
  land, remove), `repo` (create, scan, hook), `session` (onramp). One router
  `SKILL.md` per subject; each action its own file, so a use loads only its
  own. `commands/` is gone. The menu instrument lists subject and action from
  the action files' front matter and takes a subject for the bare menu.
- **`review plan`** (`skills/review/plan.md`) is the one home of finding,
  ranking, routing and estimating. Design call, written in the file: the
  code half reads and never judges (`ccfleet plan`), the judgement half is
  the file, the adopter's queue holds the seal. `review run` plans then
  seals; `review brief` and `fleet sweep` take the owed-not-briefed list;
  `drain --dry-run` prints `ccfleet plan`. Three copies folded.
- **`ccfleet plan`** (worker): read-only, `queue.evidence` and optional
  `queue.owed`, cost history only from ccfleet's own clean pass logs, "no
  measurement" otherwise; 14 new tests.
- **`work plan`** (`skills/work/plan.md`): the run's opening reads and triage,
  stopping before the first act.
- **Live-reference sweep** (worker, 45 files) and the one-line change to his
  prompt, committed with his words (`bfa38582`). Records keep their names;
  four record links that moved take allow-markers.
- **Full suite before landing:** tools 3452 OK, node 746/746, instruments
  234 OK. Landed `10b32435`.
- **Exercised headless after landing.** Bare `/atelier:review` and bare
  `/atelier` printed their menus. `/atelier:review drain the reviews now`
  did not: the session took *drain* for *run* and read the drain's files and
  the estate's queue (reads only; nothing claimed, sealed or started). Fixed
  within the hour (`f354e542`: the first word is exact and gates every read),
  re-run, menu only.
- **Private repos** (four, by class here: the estate root, two service
  repos, a client engagement): one hand-down item each on their own boards,
  listing their live files; their hook and stamped `CLAUDE.md` copies refresh
  at the next pin bump.
- **No more old questions at close** (`180/250`, `85da9586`): a child's
  hand-up relayed his rejection first; his own words then came here. The
  prompt's close puts this session's questions only; `COMMUNICATION.md` says
  so with both his quotes; `ccclose` check 16 is withdrawn (number retired);
  `ccopen` drops its pointer. ccclose 160/160, ccopen 48/48.
- **Residue:** a local `pr140` branch, its content landed as `210/540` and
  `210/550`, deleted.

## Misses, owned

- **The router let a synonym through.** I wrote "a word not in the table
  shows the menu" and landed it on a unit test; only the headless run showed a
  cheaper model treating *drain* as *run*. The rule needed to say the word is
  exact and that it gates reads too. Caught by exercising before close, not
  by the principal.
- **The private-repo count on `180/210` was low.** It said nine files in two
  repos; the sweep found 24 in four, plus every child's floor copies.

## Left open

- The `160/1450` re-check (via `210/470`) of the new build, by a session that
  wrote none of it; no drain uses the new commands until it is clean (his
  words on `180/210`); then the drain switch (`450/010` row 2).
- `180/250` (a): a different plan for stale asks, an idea until he says it is
  a priority.
- Rule-4 review of this build's doctrine and skill text: covered by the same
  re-check, which his pick named (*"Wait, review the new build"*).

## After the close

- A bare `/atelier:session` from the principal showed its menu as built, and
  showed a defect: Claude Code fills the arguments and plugin-root
  placeholders in a `SKILL.md` as it loads it, so the routers' sentences
  explaining them loaded garbled. Fixed (`6a98df21`): the routers name them
  in words, and a test bars the literal tokens. Exercised headless:
  `/atelier:session onramp` routed to `onramp.md`. `160/1790` takes the
  commit.

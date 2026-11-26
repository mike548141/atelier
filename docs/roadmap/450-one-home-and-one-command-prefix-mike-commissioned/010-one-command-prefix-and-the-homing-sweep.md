- [ ] 🎯 **Every slash command under `/atelier:`, and every
      collaboration tool homed in atelier** `[L][instruments][skills]`.
      Mike commissioned this, 2026-11-18 (his words in this section's
      README). Assessed 2026-11-18 by session 84b7932e (Opus 5.5,
      principal-opened); nothing moved yet. **Tell Mike before each move
      into atelier**: his condition, verbatim, *"tell me before you make
      changes like pulling a tool from another repo into atelier"*.

      **What the assessment found.**
      - The prefix is mostly there already. Every skill and command the
        atelier plugin ships is `/atelier:<name>` (six skills, four
        commands). Only two of Mike's commands sit outside it, both
        user-level skills: `/estate-health` and `/fable-drain`. The
        claude.ai-synced skills are Anthropic's, not his, and stay out.
      - **The catch is visibility.** `/atelier:` comes from this plugin,
        and this repo is public. Both stragglers quote the principal's
        rulings and name every estate repo, which is why they were kept
        out on 2026-11-13 (`210/440`: the general parts here, the estate
        parts in a private config). So the route is not to move them in:
        it is to switch the estate onto the general skills that already
        exist here (`/atelier:fleet-sweep`, `/atelier:review-drain`,
        `instruments/ccfleet`) with the private config held privately,
        then retire the two old commands. `210/440` already names that
        switch as the principal's to choose.
      - **Colon, not space.** The plugin system namespaces a plugin's
        skills `/<plugin>:<skill>`, and typing `/atelier` lists them all
        together, which is the grouping asked for. A single `/atelier`
        router taking a word (`/atelier estate-health`) would hide each
        command's description from the picker. Recommendation: the colon
        form; the principal's to confirm.
      - **Things outside atelier that help the collaboration** (scan of
        every repo under the estate root, 2026-11-18; named here by class,
        since this repo is public and the holders are mostly private):

        | # | What it is | Where now | Size | Waits on |
        |---|---|---|---|---|
        | 1 | `/estate-health` → `/atelier:fleet-sweep` + ccfleet + private config | estate-root kit | M, 1–2 sessions | principal's pick to switch; `160/1450` |
        | 2 | `/fable-drain` → `/atelier:review-drain`; re-add the API-credit lane `210/440` dropped | estate-root kit | L, 2–4 | as 1, plus the lane's own pass |
        | 3 | Rule + guard: a new skill or command is born `/atelier:<name>` | none | S | nothing |
        | 4 | Model-required hook: wire `tools/modelguard.py`, retire the estate copy | estate-root kit | S | `160/1450` |
        | 5 | Status-line badge when the model is not the build model | `~/.claude`, in no repo | XS | nothing |
        | 6 | Hook refusing a command that would print a secret file | one service-estate child | M (path list → config) | nothing |
        | 7 | Guard: the stash stack is shared across worktrees, so an old stash is a peer's | one app child | S–M | nothing |
        | 8 | Check: a dead `.git/hooks/` copy shadowing the live `.githooks/` | one service-estate child | S | nothing |
        | 9 | "Which tree did this gate read" second line for every check | one app child | S | nothing |
        | 10 | Two children's own floor-verbatim verifiers → `stampscan`, once its two recorded blockers are fixed | two children | M | nothing |
        | 11 | Four separate "review on the API" runners (SDK lane, split reviewer, batch trial, a client batch reader) → one atelier lane | estate root + a private child | L, 3–5 | the principal's 2026-11-16 batch conditions (runner built, own cold pass, `030/420` MAJORs fixed) |
        | 12 | The review-queue reader (reads `docs/reviews/*.deferred.md`, atelier's own shape) → ccfleet's default queue | estate root | M | after 2 |
        | 13 | Private-pointer guard for an export tree: check overlap with `pointerscan` first | one infra child | S to judge | nothing |
        | 14 | A bare `/atelier` that prints the menu of every `/atelier:` command | new | S | nothing |

        💬 Row 14 was offered after the principal pressed Enter on `/atelier`
        and `/atelier:` expecting the list (the picker shows it only while
        typing). Asked whether to add it, his answer, 2026-11-18, verbatim:
        *"yes"*. How: a plugin skill is always `/atelier:<name>`, so a bare
        `/atelier` has to be a user-level skill named `atelier`. Version its
        definition here and link it into `~/.claude/skills/`, the way the
        estate kits are linked. Build the menu at run time from the plugin's
        `skills/` and `commands/` front matter, never from a typed list, so a
        new command appears without an edit.

        Stays where it is: business connectors (an accounting MCP),
        service and infrastructure tools, and each estate's repo list,
        rulings and run results (private by the 2026-11-13 split). The
        children's `.githooks/` are floor copies at several pins: pin
        drift for a health sweep, not a homing question.
      - **Total, roughly:** 12–18 build sessions on the build tier, plus
        one owed cold pass per strand under rule 4, about 5–7 review-tier
        passes, each waiting for the principal's approval of review-tier
        time.

      **The principal's answers, 2026-11-18, verbatim, each to one
      question the session put** (answers, not rulings):
      - Colon form: *"that is fine"*.
      - Switch the two estate kits to the general skills now, retiring
        the old names: *"yes"*.
      - The homing rows: *"I will accept your recommendation on these"*.
        This is also the telling his condition asked for, so the moves the
        table lists are cleared, in the session's recommended order:
        14, 3, 5, 4 (atelier only, small); then 1, 2, 12 (the switch);
        then 6–9 and 13 (guards, each child dropping its copy after); then
        10; last 11, which still waits on his 2026-11-16 batch conditions.
      - Review-tier time: *"during the drain as usual, a lower priority
        for these vs other work"*. So each strand's cold pass is briefed
        as normal and runs in his weekly drain, after the drain's other
        work. The drain config has no per-item priority yet; until it
        does, each brief's item carries the words "drain priority: low
        (principal, 2026-11-18)" for the drain's picker to read.

      **Progress, 2026-11-18 (session 84b7932e):**
      - ✅ Row 14, `/atelier` menu: `instruments/atelier-menu`, linked by
        the installer; a headless run of `/atelier` printed the table.
      - ✅ Row 5, `instruments/ccstatusline`, wired as the user-level
        status line; the unversioned copy removed.
      - ✅ Row 3, the rule in `MECHANISMS.md` and `tools/prefixhook.py`,
        wired at session open. It names the two estate commands until they
        retire: that is the true state, not noise to silence.
      - ✅ Row 4, the user-level model hook now runs `tools/modelguard.py`
        (`/usr/bin/python3 -I`); a read-only gap analysis found its logic
        identical to the estate copy, and four probes behaved. The estate
        copy is left as history for its own repo to retire.
      - ✅ Rows 1–2 prerequisite: `ccfleet`'s generic gaps closed
        (`17f158d2`, `d9d1589e`, `a025636e`), among them the background
        wait ceiling, whose absence kills a reviewer mid-pass.
      - Cold passes queued: `160/1610` (rows 14, 5, 3; low) and `160/1450`
        widened to the gap fixes (normal; it gates row 2).
      - 💬 Asked when the drain should switch, given the gap analysis found
        faults that lose paid review work, his pick: *"After its review
        (Recommended)"*. So row 2 waits for a clean `160/1450` and then
        switches at a gap between drains, never mid-drain; his drain command
        keeps working until then. Row 1, the sweep, switches now.
      - ✅ Row 1, the sweep: switched. The estate root holds the private
        config and rulings file, the user-level settings point the skill at
        it, one real `run` on a small repo ended `DONE` and billed to that
        repo, and the old `/estate-health` link is removed. The run found
        three `ccfleet` faults (fresh `kit_dir` crash; a failing queue read
        as empty; dry passes logged as ended early), fixed in `1eb42f54`.
        🚩 The machine had 20–22 GB free against the sweep's 20 GB gate, so
        a full sweep will hold until disk is freed.
      - ✅ Row 2 prep (no switch): the estate's queue tool gained the tab
        `next` and `take --set`, and a base drain config exists, unused.
      - ✅ Row 6 `tools/secretguard.py` and row 8 `tools/deadhook.py`
        (`cdfadc75`). `deadhook --status` is now `/atelier:install-hook`'s
        proof step. secretguard wired user-level on the principal's pick,
        *"Switch it on (Recommended)"*.
      - ✅ Row 7 `tools/stashscan.py` (wired at session open) and row 9
        `tools/treeline.py`, which the floor now prints under its coverage
        line, so every child's next floor run shows one more line
        (`ef4972e6`; informational, never an exit code).
      - ✅ Row 10: `tools/pins.py --floor --child .` gives a child its own
        offline floor-copy verdict (`262658e0`); both children's copies
        read `identical` under it. `320/160` closed.
      - ✅ Row 13 judged, not built: one instance, tied to one repo's export
        script and naming the estate root; generalising it would invent a
        pattern, not ground one. It stays in its repo.
      - 2026-11-24 (session edf25bd3): row 2's target moves. `180/210`
        splits the drain into a plan step and a run step, and `450/020`
        (his ruling, a space form for every command) names them
        `/atelier:review plan` and `/atelier:review run`; the old drain
        command's own *Rank and route* section is one of the copies
        `180/210` folds into the plan. So row 2 retires the old command onto
        those, in the same build or after it; it still waits on a clean
        `160/1450` re-check and switches between drains, never mid-drain.
        Later the same day, his words, verbatim: *"Also I want you to carry on with design and build in a fresh session, not wait until the fable review is done"*. So the
        build of `review plan` and `review run` does not wait; the cutover
        of his live drain is asked separately (see `180/210`).
        Asked at that close, his pick: *"Wait, review the new build (Recommended)"*: the re-check waits for the
        build and covers it, and the switch follows a clean result (`210/470`).
        His words after, verbatim: *"we fable review the new code/design/wahtever before we use it for a review drain session"*.
      - Still open: row 2 (done 2026-11-26, step D below), row 11 (waits on the
        batch conditions), row 12 (the generic half of the estate's queue
        reader as atelier's reference queue; optional, after row 2).
      - **Child follow-ups**, for each child's own session or the next
        sweep (queue, never deliver): the service-estate child moves its
        secret paths into secretguard's config and drops its own hook, and
        drops its dead-hook check for `deadhook.py`; the app child drops its
        stash check for `stashscan.py` and its tree line for `treeline.py`;
        the two children with their own floor verifiers switch to `pins.py
        --floor`; the estate root retires its model-hook copy (no longer
        wired). Exact steps are in the session record.
      - Cold passes: `160/1620` (rows 6–10, low); `160/1450` widened again
        to `1eb42f54` (normal).

      **How to re-run the scan**: list each repo's tracked
      `tools/ scripts/ bin/ hooks/ .claude/` files, keep those dense in
      collaboration terms (claude, fable, transcript, subagent, worktree,
      session log, board, cold pass), and drop floor copies; plus
      `~/.claude/{skills,hooks,settings.json}` and `~/.claude.json`'s MCP
      servers.
      **Row 2, the route to the switch, as of 2026-11-25 ~08:45 UTC** (queue run
      0b4f93ef, `atelier-86`, from the principal's picks on `160/1790`, `210/600`
      and `210/620`). Each step is its own session; independence decides who may
      take which. Deadline for all of it: the drain's start, 2026-11-29 23:00 UTC.
      - **A.** `210/620`: a build session applies `DV1`–`DV11` and `PK1`–`PK21`,
        MODERATEs first, and queues the re-check pointer in `160` in its landing
        commit. It neither briefs nor runs the re-check.
      - **B.** shed `020/1040` (shed's own session, alongside A): above all its
        drain config's `pass_prompt` moves to
        `skills/review/orchestrator-prompt.md`, since the retired
        `skills/review-drain/` path makes every pass refused at launch; and the
        session id joins its claim step.
      - **C.** After A lands: the one Fable re-check the principal approved on
        `210/620`, briefed by a session that wrote none of the fixes and run by
        one fresh Fable reviewer.
      - **D.** Only when C has no MAJOR and B is done: this row. The drain moves
        onto `/atelier:review plan` and `/atelier:review run` and the user-level
        `/fable-drain` retires, between drains, never mid-drain.
      - ✅ **A done 2026-11-25 UTC** (session b04df0da, `atelier-f9`): `210/620` closed, all
        32 findings applied; the re-check pointer is `160/1820`. B (shed's own) and C remain.
      - ✅ **C done 2026-11-25 UTC** (session 01c055e5, `atelier-4c`): `160/1820` came back
        PASS-WITH-FINDINGS with **0 MAJOR** (5 MODERATE, 11 minor, 5 notes, `DP1`–`DP21`), so C's
        condition for D is met. D still waits on B (shed's `020/1040`). The `DP` findings are the
        principal's to rule; none is a precondition for D unless he says so.
      - ⚖️ **His ruling 2026-11-25 ~21:45 UTC (session 01c055e5), verbatim:** *"Given the low
        severity of the findings I am ruling that * This code is ready to use for the drain so we
        can continue to switch over to it * That we will fix the findings we know about * If those
        fixes cause work that then requires another review we can decide if that review is run in
        the interim or waits until the next drain, but I wont decide that until we have completed
        the fixes"*. So D is open and goes ahead; the `DP` fixes are `210/630`, built now, and
        their review, if any, is his to time once they are done. 🚩 Fixes landing on the drain's
        paths before the drain would run unreviewed in it: `210/630` says to land them before
        D's first-use dry run or after the drain, never during it.
      - **The step D prompt, as handed to the principal 2026-11-25 (session 01c055e5)**, to run
        after `210/630` lands. The `210/630` session's close hands it to him, adapted to
        whatever has changed (his ask, 2026-11-26, verbatim: *"instrust the parallel session to
        give me the prompt once its finished (or an adapted version of the prompt if things
        change - essentially whatever needs to happen next)"*):
        ```
        /atelier:work run Step D of board 450/010 row 2, between drains and before the drain starts 2026-11-29 23:00 UTC, never mid-drain: move the weekly drain onto /atelier:review plan and /atelier:review run, and retire the user-level /fable-drain. Step B (shed 020/1040) and step C (160/1820: PASS-WITH-FINDINGS, 0 MAJOR) are both done, and my ruling recorded on 450/010 says this code is ready for the drain. Check that 210/630's fixes have landed first; if they haven't, go ahead on the reviewed code and leave them until after the drain. Make the adopter actions in the changelog and the private-config points that the 160/1800 and 160/1820 verdicts name, in the estate root's drain config and queue (work that belongs in the estate root goes to its own session if the doctrine says so). Then do the first-use check from shed 020/1050: a dry run, the reset time checked against the weekly meter, and ccfleet check clean. If D can't finish before the drain starts, Monday runs on /fable-drain. At close, give me the exact prompt for the next step from that row.
        ```
      - ✅ **`210/630` landed 2026-11-26 UTC** (session 5e236e34, `atelier-cd`): all of
        `DP1`–`DP21` are on `main`, before step D's first-use dry run, so that dry run exercises
        the fixed code. Their review is `160/1870`, approved by him to run before the drain, and
        his answer on the leftovers added `210/640` (`b3e17296`, inside that review). The step D
        prompt adapted to this, as handed to him, is in
        `docs/sessions/2026-11-26-0156-dp-fixes.md` § *The adapted prompts handed to him*; it
        supersedes the one below.
      🔒 **CLAIMED 2026-11-26T04:44Z (wt: atelier-51-step-d) by principal-opened session a2aeebc8
      (`atelier-51`, Opus 5.5), for step D only**: the adopter actions and private-config points
      (the estate root's share by a session working there), the first-use check, the switch and
      `/fable-drain`'s retirement. No Fable work here; `160/1870` runs in its own session.
      ✅ **D done 2026-11-26 UTC** (session a2aeebc8, `atelier-51`, Opus 5.5; no Fable work).
      - **The estate root's share**, by a headless Opus session started inside it (its `020/1070`,
        RESULT DONE, its CI green): its queue now refuses `ranked`, `next` and `take` with exit 3
        while unsealed (`210/640`), `take` applies `next`'s checks and takes `--route` (`DP8`),
        `seal` refuses `unknown` (`PK10`), an `unseal` ends a run's seal; its base config passes
        `--route local` on `next` and `take` (`PK3`/`DP7`), keeps the review tier's alias and no
        standing `FINISH_WORDS` (`DV2`), and its `pass_prompt` stays the review skill's (step B);
        its rulings file gained the estate's drain section, carrying the old command's rules
        verbatim. The old kit still runs, as the fallback. Its own cold pass is queued there,
        unbriefed, for the principal to time. The new `END` fields (`review_model=`,
        `result_line=`) are read by `/atelier:review run`, not by a config: no estate change.
      - **First-use check** (on `b3e17296`'s code, the estate root's generator writing to a
        scratch copy, no approval in it): the generator's reset, Mon 2026-11-30 12:00 NZDT =
        2026-11-29T23:00 UTC, matches the weekly meter's "Resets Monday 12:00 PM"; `ccfleet check
        --prompt` exit 0 with no `QUEUE ROUTE` line (the base printed one before); `ccfleet plan`
        exit 0, 15 briefed reviews; `ccfleet drain --dry-run` exit 0, its `next` refused with exit 3
        and read as "not sealed: no launches rehearsed".
      - **Switched:** the user-level `/fable-drain` link is removed (its kit stays in the estate
        root, relinkable in one command if `160/1870` sends Monday back to it); the user-level
        instructions now name `/atelier:review plan` and `run`; `prefixhook` reports no command
        outside `/atelier:`.
      - 🚩 **For the drain session:** the gate's disk floor was not met at the check (11 GB free
        against 20); the drain holds every start until it is, so free disk or set the floor
        (the generator's `--min-disk`) at the drain's start. `160/1870` runs inside the drain
        (his answer, quoted there); it does not gate it.
      🔓 2026-11-26T05:20Z: session a2aeebc8 releases its claim on step D.
      🎯 **Owed ask, the disk floor:** put to him at the close (session a2aeebc8, AskUserQuestion:
      free disk to above 20 GB, lower the floor to 12 GB for this drain, or decide on Monday), his
      typed answer, verbatim: *"Ask me again from tomorrow evening"*. So ask again from the evening
      of Fri 2026-11-27 NZDT (about 05:00 UTC that day), before the drain starts.
      ✅ **Settled by the measurement, 2026-11-26T11:50Z** (session a2aeebc8, at its second close):
      the drain config's gate now reads 87 GB free against the 20 GB floor, so it opens with no
      change and there is nothing to ask. If the drain session finds the gate holding on disk,
      it puts the question to him then.
      If C or B misses the drain's start, D is skipped: that drain runs on
      `/fable-drain` and D waits for the gap after it. Each session's close hands
      the principal the prompt for the next step it is not barred from naming.


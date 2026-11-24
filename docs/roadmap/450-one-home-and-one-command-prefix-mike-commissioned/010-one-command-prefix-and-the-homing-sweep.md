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
      - Still open: row 2 (waits on `160/1450`), row 11 (waits on the
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

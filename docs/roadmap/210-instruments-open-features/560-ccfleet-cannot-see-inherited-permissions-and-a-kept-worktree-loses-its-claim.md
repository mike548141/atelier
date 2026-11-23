- [x] **`ccfleet`'s permission line cannot see what a session inherits,
      and a kept worktree can outlive its claim.** Found 2026-11-23 by the
      `210/470` FL20 canary (queue run c7a1e36e), two findings:
      1. **Narrowing a headless session's permissions in the config did
         nothing.** The canary set `acceptEdits` and an `--allowedTools`
         list without `python3`; the session ran `python3` anyway, because
         the operator's user-level settings allow bare `Bash`, and a
         headless session inherits user-level allow rules and hooks.
         `ccfleet check` prints its PERMISSIONS line from `claude_args`
         only, so it reports a narrowing the session does not get. This is
         FL10's threat surface (who can steer an unattended session): the
         man page's THREATS section and `check` should say that user- and
         project-level settings widen what the config sets, or `ccfleet`
         should launch with a settings source it controls
         (`--setting-sources` or an explicit settings file) so the config
         is the whole grant. Which is a design choice.
      2. **A clean DONE that leaves uncommitted work releases its claim and
         keeps its worktree**, so the unlanded work is tied to no claim and
         no queue item; only the KEPT line in the driver log points at it.
         The design as written (release on a clean RESULT, removal only
         when nothing is unlanded) allows it. Options: keep the claim while
         the worktree is kept, or have a clean RESULT with unlanded work
         read as not clean. A choice about what "clean" means.
      Also seen, not a defect: a headless session inherits the operator's
      PreToolUse hooks, so a canary prompt has to avoid commands those
      hooks refuse (the first canary session ended BLOCKED on one).
      💬 **Answered 2026-11-23 ~12:35 UTC (session c7a1e36e, AskUserQuestion), his pick:** part 1, *"Config is the whole grant
      (Recommended)"*: ccfleet launches sessions so that only its config's
      permissions apply, not user-level allow rules, with tests and the
      THREATS section and `check` saying so. Part 2, *"Treat as not clean
      (Recommended)"*: a clean RESULT that leaves unlanded work is not
      clean, so the claim stays and the pass can be resumed. Both are now
      build work, owed here; the build earns its own cold pass.
      ✅ **Built 2026-11-23 (queue run 608d8123, commit `ccfleet: make the
      config the whole grant…`).** Part 1: every launch passes
      `--setting-sources project,local` and a per-session `--settings` file
      ccfleet writes (user-level settings less their allow rules,
      `defaultMode` and `additionalDirectories`, less any hook that prints
      an allow decision, plus a config `settings` key; `drop_hooks` drops
      more); guard hooks are kept, so nothing widens; the user-level
      `CLAUDE.md` is passed by `--append-system-prompt-file`, because the
      setting sources also decide which `CLAUDE.md` files load (measured on
      the real CLI). `check` prints GRANT, HOOK, INSTRUCTIONS and REPO
      SETTINGS lines; THREATS names what still widens (repo settings, a kept
      hook whose script answers allow, managed settings), and a launch
      prints WIDENED for repo grants. Part 2: a clean RESULT with
      uncommitted, untracked or unpushed work reads UNLANDED, keeps the
      claim and the worktree, and `resume` finishes it. 87 `ccfleet` tests
      pass. Trade-offs recorded in the man page: user-level skills, agents
      and commands no longer reach fleet sessions (plugin skills still do),
      and user-level settings now outrank a repo's own on a shared key.
      Cold pass queued as `160/1740`.

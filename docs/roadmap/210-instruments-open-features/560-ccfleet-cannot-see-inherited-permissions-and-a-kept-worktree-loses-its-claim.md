- [ ] 🔎 **`ccfleet`'s permission line cannot see what a session inherits,
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

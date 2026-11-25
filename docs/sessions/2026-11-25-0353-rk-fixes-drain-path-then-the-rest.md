# 2026-11-25 03:53 UTC — the RK fixes: the drain path, a canary, then the rest (`210/600`)

**Session:** `0ee74059` (messaging name `atelier-c3`), Claude Opus 5.5, principal-opened in the
VS Code extension by `/atelier:work run`, as orchestrator. Worktree `atelier-c3`, then one per
worker (`-modelguard`, `-skills`, `-lifecycle`, `-grant`), each removed once landed.

## What was asked

The principal, verbatim (the run's brief): *"Work board 210/600 in its stated order: (1) the
drain-path fixes RK2 and RK5, then RK12's read-only check of the real drain config, then ONE
canary pass on the real config; queue the small Fable pass's pointer over those fixes in the
landing commit, and do not brief or run it; (2) then the remaining RK findings, as the reviewer
advised. The drain-path part must land before 2026-11-29 23:00 UTC."*

## What was done

- **Claim** on `210/600`, pushed first (`e6ae2b82`). `ccopen`: one other live session (the RK
  pass's own, closing); machine quiet at the start.
- **Part 1, the drain path** (`a1cc5f2d`, landed 2026-11-25, four days inside the deadline).
  `RK2`: the reviewer-prompt template's one home is now `orchestrator-prompt.md`, so a pass in
  another repo reads nothing outside its worktree. `RK5`: a fold runs after `reset_utc`, as a
  resume does; new work is still refused. `RK12`, read-only: the real config's sessions run in the
  bypass permission mode, so they have what they need; its `pass_prompt` names the retired path
  (already queued in the estate root's own board). **Canary:** one pass on a copy of the real
  config, grant fields verbatim, the cheapest model for orchestrator and reviewer, a throwaway repo
  with a local origin and a stand-in queue: `DONE`, claim taken with the session id and released,
  worktree removed, act 1 and fold landed, and the orchestrator read nothing outside its worktree.
  It found one more drain-path defect, fixed in the same commit: `REVIEW_MODEL` must be the Agent
  tool's tier alias, not a full model id. The small Fable pass is queued as `160/1800`; this
  session neither briefed nor ran it.
- **Part 3, the rest**, by four Opus workers in their own worktrees, merged and re-tested here:
  `modelguard` `RK9`, `RK15` (`fc922383`); the skills `RK1`, `RK12` (fleet prompts), `RK13`,
  `RK14`, `RK19`, `RK20`, `RK22`, `RK27`, `RK29` (`4a9318b7`, `9b4a8f8f`); the `ccfleet` pass
  lifecycle `RK3`, `RK4`, `RK6`, `RK16`, `RK17`, `RK24`–`RK26` (`53203833`, `2d8e05e3`); the
  `ccfleet` grant and contract `RK7`, `RK8`, `RK10`, `RK11`, `RK12`, `RK18`, `RK21`, `RK23`,
  `RK28` (the commit after them). Every new test was checked to fail on the old code. Live probes
  were all on the cheapest model: the canary and three router launches (`RK1`).
- **Board:** `210/600` closed; `160/1800` (drain-path pass, the one he picked) and `160/1810`
  (part-3 pass, waits for his permission for Fable work) queued.

## Decisions taken without him (mechanical or the reviewer's way)

- The canary is a stand-in on a copy of the real config, not the real queue: a real pass would
  have claimed a real review and spent Fable, which nothing approved.
- `RK10`'s guard refuses a public repo's launch by default when the operator's instruction file
  names a private name; `instructions_guard: warn` goes on with a line per name. Fail-closed, as
  a publication cannot be retracted; it means the estate root's config must choose before a
  public repo's next pass.
- `RK12`'s fleet prompts keep their reads of the atelier checkout (long, changing texts) and stop
  BLOCKED on a refused read, rather than inlining them.

## Left open

- `160/1800`: the small Fable pass, before Monday 2026-11-30's drain; by a fresh session.
- `160/1810`: the part-3 pass, waiting on his permission for Fable work.
- Hand-down to the estate root (its own board already holds the path fix): the drain config's
  `pass_prompt`, and the `instructions_guard` choice.

## After the close: his answers, and `210/610`

- `RK10`, his pick *"Keep refusing as per your recommend option but what do we do to fix this?"*,
  then, to a separate public-safe file, *"Build it now as recommended but would it be better to
  have two instructions files? one with just hte private info in it and the other with everything
  else so that there cant be drift rather than needing a drift checker?"* (answers, not rulings).
  Done his way: the user-level file is now a shared part that imports a private part, and
  `ccfleet` follows the import for private repos only (`210/610`, `f4360a79`). Public-repo passes
  are no longer refused, and need no config change.
- `160/1810`: his pick *"Approve one pass now"*: one Fable pass by a fresh session, recorded on
  the item. With `160/1800`, both wait for a fresh session he opens; 0ee74059 may run neither.

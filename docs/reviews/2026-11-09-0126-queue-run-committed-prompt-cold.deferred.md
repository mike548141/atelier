# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-queue-run-committed-prompt-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

## The queue pointer's questions (author-written, verbatim)

> whether an agent following the skill can still end up running uncommitted prompt text (a checkout
that is not the plugin root, a detached head, a stale clone); whether the three-leg teardown rule is
followable by a separate-session worker.

## The brief-writer's own questions

1. Step 3's fallback reads the working file when `git show` fails. What can make `git show` fail on
demand, and is that a fail-open route to the very text the rule refuses?
2. "Prints that same path": a path compared as text, on a machine with symlinks and a case-folding
disk. What happens with a symlinked plugin root?
3. `HEAD` is whichever branch the checkout is on: a feature branch, a detached head, an unpushed
commit. Does "committed" deliver what the skill says it delivers?
4. `git status` and `git show` in the plugin root run under that repo's config. Does the threat note
account for it?
5. The test pins text in a skill an agent then interprets. What checks that a session actually read
HEAD?
6. The away-cadence inference: is it what the prompt says, and did the principal say so for every
run started by the command?
7. Three-leg teardown: `lsof +D` cost and reliability on a large worktree; a worker still pushing
while the orchestrator merges; worktrees left forever when the marker never comes.
8. A later series of commits touched these doctrine files after `663b978a`. Check the delta's text
still stands at HEAD.

## What the brief-writer ran, and what it got

- `qr`: python3 3.14: 56 tests OK, exit 0.
- `skillcmds`: the first prints the worktree root; the prompt is 161 lines at HEAD; 0 lines pending.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

---
name: queue-run
description: Orchestrate a queue run — drain the shared roadmap queue as an orchestrator, executing items yourself or via worker sessions in worktrees, closing records per item so a session cap loses at most the item in flight. Use when the principal points a session at the queue ("progress any work you can", "drain the queue", "keep the plan busy"), or asks to run atelier's orchestrated-queue-run pattern, optionally with this run's brief after the invocation.
---

<!--
  ONE TEXT, NOT TWO — and a STAMPED COPY, NOT A SECOND SOURCE: this skill
  holds no rule of its own. It runs the principal's session-open prompt, and
  the prompt file below is the single source, so the command and the copy he
  pastes by hand cannot drift (Mike, 2026-10-18, 180/090: "You need to
  ensure the there is no drift between the command and the text file unless
  I authorise the drift"). The prompt is principal-owned text: change it
  only on his say-so, quoted in the commit. Do not restate any of it here;
  tools/test_queue_run_single_source.py fails if this file stops pointing at
  the prompt or starts copying its lines. What the skill does add is only
  delivery, and each addition is pinned by that test: how to fetch the prompt
  (the committed copy, never the working file, with a warning when an edit to
  it is pending: Mike, 2026-11-08, 160/900 QK1, "Keep edit; read committed
  only"), the bundled path of the doctrine (QK3), and where the typed text
  goes. A change to the prompt takes effect when it is committed, and not
  before. The doctrine the prompt anchors to
  is `docs/method/CONCURRENCY.md` § Orchestrated queue runs and
  `docs/method/ECONOMICS.md` § The orchestrated-run tier split, bundled with
  this plugin. Doctrine's four safety pins live in the prompt itself, on
  Mike's ruling (2026-10-18, 180/100: "Move them into my prompt");
  tools/test_templates.py checks them in the command as loaded, skill plus
  prompt.
-->

# Atelier — orchestrating a queue run

Read the principal's session-open prompt and follow it as his own brief, word
for word. The file is:

`${CLAUDE_PLUGIN_ROOT}/docs/method/session-open/session-open-prompt.md`

(The same file, from this skill's base directory:
`../../docs/method/session-open/session-open-prompt.md`.)

**Read the committed copy, never the working file.** Only text that has been
committed has met the pre-commit hook, the tests and review, so an edit in the
working tree is not run. Do this before anything else:

1. If `${CLAUDE_PLUGIN_ROOT}` is the top of a git checkout (`git -C
   "${CLAUDE_PLUGIN_ROOT}" rev-parse --show-toplevel` prints that same
   path), read the prompt with `git -C "${CLAUDE_PLUGIN_ROOT}" show
   HEAD:docs/method/session-open/session-open-prompt.md`, and do not open the
   working file.
2. Then run `git -C "${CLAUDE_PLUGIN_ROOT}" status --porcelain --
   docs/method/session-open/session-open-prompt.md`. If it prints anything,
   edits to the prompt are pending: say so in the first lines of your opening
   report (the file, and that you ran the committed copy, not the pending
   edit). Committing the edit, on the principal's say-so, is what makes it
   run; you do not commit it.
3. If the plugin is not a git checkout (an install from GitHub is a copy of
   one commit, so there is no pending edit to run), or `git show` fails, read
   the file at the path above and say which of the two applied.

The doctrine the prompt anchors to is bundled with this plugin at
`${CLAUDE_PLUGIN_ROOT}/docs/method/CONCURRENCY.md`. Where the path the prompt
gives does not resolve from the repo you are in, read that copy instead and say
so.

The text the principal typed after the invocation is that prompt's *This run*
section. With nothing after it, the run takes the prompt's default order.

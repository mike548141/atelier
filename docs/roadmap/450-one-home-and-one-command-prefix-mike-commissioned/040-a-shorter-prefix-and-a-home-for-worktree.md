- [ ] 🤔 **A shorter prefix (`/a:` for `/atelier:`), and whether
      `/atelier:worktree` belongs under another subject** `[M][skills]`.
      The principal, 2026-11-28 (session a78630a6, `atelier-e6`), verbatim:
      *"Put this on the board. I am considering renaming all the /atelier:
      commands to be /a: instead so its quicker to type. I am also looking
      at commands like /atelier:worktree to decide if they have a better
      home e.g. perhaps it should be /atelier:work tree or /atelier:session
      worktree"*. **He is still considering both; nothing is built or
      renamed until he rules.**

      **What a build would have to know (grounded 2026-11-28):**
      - **The prefix is the plugin's name.** `/atelier:` comes from
        `"name": "atelier"` in `.claude-plugin/plugin.json`, so `/a:` means
        renaming the plugin itself, and its marketplace entry and install
        follow. Whether a one-letter plugin name is accepted, and whether it
        clashes with another installed plugin, is unchecked.
      - **The sweep is large.** 113 tracked files outside the records name
        `/atelier:`. Old names stop existing with no forwarder (his pick,
        2026-11-24, recorded in `020` and `180/210`), so every live
        reference moves in the same landing; records stay as written.
      - **The bare `/atelier` menu** (`010` row 14) is a user-level skill
        named `atelier`; it would become `/a`, or both would be kept.
      - **Repo name and plugin name would part.** The repo, the README and
        the doctrine stay "atelier"; only the typed prefix shortens.
      - **`worktree` today is its own subject** with four actions (`start`,
        `list`, `land`, `remove`). Under `work` or `session` it becomes a
        second level (`/atelier:session worktree start <branch>`), which the
        one-level subject-then-action form (`020`) and the menu builder
        (`instruments/atelier-menu/menu.py`) do not handle yet. `030`
        recorded that `work` means queue runs and `session` holds a
        session's own steps (`onramp`, `close`); a worktree is a step of a
        line of work inside a session, so the fit is arguable both ways.
      - 13 tracked lines name `/atelier:worktree` by itself.

      💬 **His answers, 2026-11-27 ~23:35 UTC (same session, AskUserQuestion,
      typed in place of the options), verbatim:** on `/a:`, *"Its work for
      the baord not now"*; on worktree, *"/atelier:work tree <branch> makes
      more sense to me. I dont see why we need a "start" in there as well.
      But this is work on the board for later"*. So both are later work;
      his leaning for worktree is `work tree <branch>`, with no `start`.
      Owed by that build: how `list`, `land` and `remove` read under it,
      how a branch name is told from an action word (a branch called
      `list`), and the second action level in the menu and tests; put the
      shape to him in one line before moving anything.

      **To do when he rules:** confirm the prefix and the worktree home with
      him in one line, then rename in one landing (plugin name, skills,
      tests, menu, every live reference), full suite green before it lands.

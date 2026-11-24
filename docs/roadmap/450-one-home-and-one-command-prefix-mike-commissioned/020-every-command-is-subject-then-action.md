- [ ] 💡 **Every `/atelier:` command takes the form *subject, space,
      action*, and a bare subject shows its menu.** His ruling, 2026-11-24
      (session edf25bd3, AskUserQuestion, his own words, verbatim): *"I
      think a space and for the default it could have a menu or help screen
      a little like what /atelier does by itself. We should make all the
      atelier command like this so its consistent"*. Asked whether the
      review commands should be `/atelier:review-plan` (hyphen, recommended
      to him) or `/atelier:review plan`. It fits his commission above
      (*"/atelier estate-health"*), and `/atelier:worktree start|list|land|
      remove` already works this way.
      **What it means.** One skill per subject, the action as its first
      argument: `/atelier:review plan`, `/atelier:review run`,
      `/atelier:review brief`. A bare `/atelier:review`, or an action it
      does not know, shows that subject's menu and does nothing else, so a
      dropped or misread word can never start spending (the risk the hyphen
      form was recommended for).
      **Shape to consider, for him to confirm before the build moves
      anything:**

      | Today | Becomes |
      |---|---|
      | `review-brief`, `review-drain`, (new, 180/210) | `review brief`, `review run`, `review plan` |
      | `queue-run` | `queue run` (a `queue plan` later if wanted) |
      | `fleet-sweep`, `fleet-pins` | `fleet sweep`, `fleet pins` |
      | `worktree` | unchanged |
      | `scan`, `install-hook`, `create-repo`, `session-onramp` | single-action commands; grouping (e.g. `repo scan`, `repo hook`, `repo create`, `session onramp`) is open |

      **Owed by the build:** each subject's skill description must carry the
      trigger words of every action it holds (one description now does the
      work of several), and each action's text lives in its own file behind
      the skill so a use loads only its own. The `/atelier` menu lists
      subjects and their actions. Old names get no aliases (180/210's
      reasoning). Live references are swept here; private children's by
      their own sessions; records stay as written. Lands with or before
      180/210, which then builds `review plan` and `review run` under this
      form.

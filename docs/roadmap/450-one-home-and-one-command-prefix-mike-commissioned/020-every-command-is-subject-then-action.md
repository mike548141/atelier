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
      This updates `010`'s 2026-11-18 point *Colon, not space*: the colon
      stays (the plugin namespace), and the space now carries the action.
      The trade-off `010` named, that actions do not show in the picker, is
      the one he accepted; the bare-subject menu answers it. `010` row 2
      (retiring the user-level drain command) now lands on `review run`.
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
      | `work-run` (renamed from `queue-run`, 180/230) | `work run` (and `work plan`, 180/240) |
      | `fleet-sweep`, `fleet-pins` | `fleet sweep`, `fleet pins` |
      | `worktree` | unchanged |
      | `scan`, `install-hook`, `create-repo`, `session-onramp` | `repo scan`, `repo hook`, `repo create`, `session onramp` |

      **His answers, 2026-11-24 (AskUserQuestion; answers, not rulings):**
      the four single-action commands, *"Group them (Recommended)"*, as the
      last row reads. The rest of the table was shown to him in the same
      turn with no objection; the build confirms it with him in one line
      before moving anything.
      **Owed by the build:** each subject's skill description must carry the
      trigger words of every action it holds (one description now does the
      work of several), and each action's text lives in its own file behind
      the skill so a use loads only its own. The `/atelier` menu lists
      subjects and their actions. Old names simply stop existing, with
      no forwarder and no signpost (his pick, 2026-11-24, *"Nothing"*,
      recorded in 180/210), so the sweep of live references must be
      complete before the rename lands. Live references are swept here; private children's by
      their own sessions; records stay as written. Lands with or before
      180/210, which then builds `review plan` and `review run` under this
      form.

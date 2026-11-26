- [ ] 🔧 **Look for a measurably safer way for `modelguard` to catch a model-less `claude`
      started inside tmux or screen, without refusing harmless commands (the `DP1` leftover of
      `210/630`).** `210/630` kept tmux's options from swallowing the command and denied the
      seven reviewed shapes again, but did not build the counsel's "any `claude` word after a
      tmux run or send subcommand is a launch", since that refuses `tmux new -d docker logs
      claude` and `tmux send-keys 'cd claude' Enter`. What passes: a bare `claude` word after a
      runner the hook does not know. The risk is a session started on the default model rather
      than a named one (cost and tier), not data loss. Assess first, then build only an option
      that is measurably safer and still lets the job get done; report the measure.
      💬 **His answer, 2026-11-26 ~03:20 UTC (session 5e236e34, `atelier-cd`, AskUserQuestion;
      an answer, not a ruling)**, verbatim: *"With (1) I'm ok with these commands and I
      understand that they carry a risk of data loss etc if the wrong commands are used. If
      there are ways to do this in a way that is measurably safer whilst still be effective
      (i.e. the job gets done well) then I am interested in making those changes. But I am not
      blocking these kinds of commands if there is not a better option."*
      Not on the drain's path: after the 2026-11-29 drain, normal priority.

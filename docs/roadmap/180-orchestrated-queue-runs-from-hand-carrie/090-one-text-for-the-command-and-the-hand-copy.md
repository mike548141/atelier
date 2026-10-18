- [~] (claimed 2026-10-18-0450, wt: atelier-qr-180-090)
      **One text for `/atelier:queue-run` and the hand copy, with no drift.**
      Mike, 2026-10-18: *"I would like the latest version of the prompt that
      "/atelier:queue-run <this run's brief>" uses to be in a text file
      somewhere that is easy for me to access in vscode so that I can use it
      by hand and review its contents when I want too. You need to ensure the
      there is no drift between the command and the text file unless I
      authorise the drift. I expect there is already a text file with exactly
      that in the repo which has that git history of prompts attached to
      it"*. Measured: not exactly. `session-open-prompt.md` holds his prompt,
      and the `queue-run` skill is a separate text that carries the same
      clauses in other words, with nothing to stop the two drifting. Owed:
      make the prompt file the single source that the command loads, guard
      that by test, and make the file principal-owned text. Then delete the
      loose copy, as he authorised.

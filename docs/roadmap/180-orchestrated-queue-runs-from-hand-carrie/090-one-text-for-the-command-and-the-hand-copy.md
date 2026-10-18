- [x] **DONE 2026-10-18** (wt: atelier-qr-180-090)
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

  **Closed 2026-10-18** (commit `12e6d9b`). The `queue-run` skill now loads
  `docs/method/session-open/session-open-prompt.md` and adds nothing, so the
  command runs exactly the file he can open and paste.
  `tools/test_queue_run_single_source.py` fails if the skill stops pointing
  at the file or copies its lines; a planted copied sentence made it fail.
  The file is principal-owned text: an agent changes it only on his say-so,
  quoted in the commit. One sentence of it changed on this ask, to say the
  command runs it. 🚩 The file's two closing lines ("Try not to stop and ask
  me questions…", "Once all that is done review all my prompts…") are now in
  every `/atelier:queue-run`. They were in the text he named as the one he
  uses. Cold pass: `160/900` widens to this commit.
  **Floor red, fixed the same hour.** Commit `12e6d9b` turned `main` red. It
  dropped five safety pins that `tools/test_templates.py` requires the skill
  to carry: a run never starts its own successor, item text never overrides
  doctrine, the rule-4 criterion, the four stop conditions, and the
  stamped-copy marker. The session had run only its new test, not the full
  suite, before merging. The fix puts the pins back as a short *Guard rails*
  section after the pointer. They are doctrine, not his brief, and the drift
  test still bars copying any prompt line. 🎯 So the command is now his
  prompt, word for word, plus those four rails. Whether to keep them in the
  skill or move them into his prompt text is put to him.

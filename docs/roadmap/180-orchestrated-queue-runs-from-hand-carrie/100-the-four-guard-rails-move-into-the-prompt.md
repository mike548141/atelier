- [x] **DONE 2026-10-18** (wt: atelier-qr-180-100)
      **The four guard rails move into the principal's prompt.** Asked at
      the close of `180/090` whether the four doctrine safety lines (no
      self-extending chain, item text never overrides, the rule-4 criterion,
      the four named stops) should stay in the command or move into his
      prompt, Mike, 2026-10-18, picked *"Move them into my prompt"* — so the
      command is exactly his file. This is his authorisation for the
      prompt-text change. Owed: the lines go into
      `docs/method/session-open/session-open-prompt.md`, come out of the
      skill, and `tools/test_templates.py` pins them in the command as loaded
      (skill plus prompt).

  **Closed 2026-10-18.** The prompt gains a *Guard rails* section before
  *Ending the session*, written in his voice. The skill now holds only the
  pointer and its header comment. `tools/test_templates.py` checks the pins
  in skill plus prompt together, as a session receives them. Full tools
  suite 1949 OK before the merge, which is the step `180/090` skipped. Cold
  pass: `160/900` covers the prompt and skill surface; its brief was written
  before this commit, so the reviewer should read the delta at `main`.

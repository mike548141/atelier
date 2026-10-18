- [x] **DONE 2026-10-18** (wt: atelier-qr-180-070)
      **Print the session id at open; drop the date-and-time line.** Mike,
      2026-10-18, mid-run: *"When a session opens it should print the session
      ID at the top of the transcript so that I can use as a reference for
      other claude code sessions to find it, or to use with cctranscript."*
      And: *"The date and time are appearing in the vscode session transcript
      now, it looks to be like Anthropic have added it as a feature in the
      claude plugin. Not something that we are causing with my prompt. That
      means we don't need to ask for the date or time in my templated prompt
      anymore since its a fature of claude code in vscode."* Owed: the prompt,
      `CONCURRENCY.md` and the `queue-run` skill gain the session id as the
      first line of the opening report, and lose the date-at-open line that
      `180/040` restored hours earlier.

  **Closed 2026-10-18.** In the prompt, `CONCURRENCY.md` and the `queue-run`
  skill, the session id is the first line, and the date line is gone.
  Mike's observation that the harness now stamps each turn is taken as he
  gave it; the agent did not test other surfaces such as the terminal or
  cloud sessions. Cold pass: `160/900` widens to this commit.

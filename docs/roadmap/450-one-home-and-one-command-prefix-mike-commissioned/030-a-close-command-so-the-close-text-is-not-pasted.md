- [ ] **`/atelier:session close`: one command runs the session-open
      prompt's close, so the principal stops pasting it.** The principal,
      2026-11-24 (session 33d3cde8), verbatim: *"The reason I have the
      session-open-prompt.md file open in vscode all the time is I regularly
      copy and paste the ending session text into sessions when I want them to
      wrap it up properly. Often these are sessions that I did not start with a
      /atelier:work run command"* · *"I am wondering if I would be better off
      with a command like /atelier:work close to save me copying and pasting
      the text from the prompt template file. Or should it be embedded in
      ccclose or some other way?"*
      **His pick** (AskUserQuestion, options and recommendation Claude's):
      *"/atelier:session close (Recommended)"*, over `/atelier:work close` and
      folding the text into `ccclose`. The reasons put to him:
      - **Not in `ccclose`.** It is a read-only checker a session may run
        several times mid-work; instructions in its output would set off the
        wrap-up on every check. The summary, the walk-through and the
        record check are judgement, which `210/480` kept in the prompt.
      - **`session`, not `work`.** `work` means queue runs; most sessions he
        closes this way were never one. `session` already holds `onramp`.
      - **One source.** The action reads the committed *Ending the session*
        section of `docs/method/session-open/session-open-prompt.md`, the
        way `work run` reads the whole file (`180/090`, no drift without his
        say-so). It restates none of the text.
      **To build:**
      - `skills/session/close.md`, and its row in `skills/session/SKILL.md`
        (the description and `argument-hint` too); `tools/test_subject_skills.py`
        and the `atelier-menu` output follow.
      - Read the section from the committed copy, never the working file, with
        the same pending-edit warning as `work run`. Find it by its heading;
        fail loudly if the heading is gone rather than run nothing.
      - A single-source test like `tools/test_work_run_single_source.py`: the
        action must point at the section and must not copy its lines.
      - Words typed after `close` are that session's extra close brief.
      - Works in any repo (the plugin is installed for the user) and in a
        session with no repo, where `ccclose` runs without `--root`.
      The prompt's text does not change; it is his, so any later trim of the
      close section is shown to him first. Whether a cold pass is owed on the
      skill text is the builder's call under `REVIEW.md`; a Fable pass needs
      his approval.

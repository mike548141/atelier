- [~] **Every session opens by showing its messaging name and its transcript
      id.** The principal, 2026-11-22, verbatim: *"Also when a new session
      opens it must print the session ID (what other sessions would use to
      communicate with that session) and session transcript ID to the
      transcript so that I see both from the time I first start a new
      session"*. Two different identifiers, measured the same day (Claude Code
      2.1.330): the name other sessions message (`SendMessage` to, e.g.,
      `atelier-df`) is the `name` field of `~/.claude/sessions/<pid>.json`;
      the transcript id is the session UUID, the transcript file's name, which
      `cctranscript` and `ccclose --session` take. The prompt's "print the
      session ID first" line asks the model for the second only, and only
      when the prompt is used. Build: a `SessionStart` hook,
      `tools/idhook.py`, wired user-level beside the other three, that shows
      both as a `systemMessage` and asks the model to print both as the first
      line of its first reply.
      *(claimed 2026-11-22 UTC, session 12a41aa2, inline, primary checkout)*

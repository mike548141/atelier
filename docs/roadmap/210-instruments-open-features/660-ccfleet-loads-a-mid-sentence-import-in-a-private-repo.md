- [ ] 🔧 **`ccfleet` loads a file a private repo's instructions name mid-sentence ("see
      @file"), as Claude Code does (the `DP18` leftover of `210/630`).** Low priority: work on
      it once it is evidenced as an issue. Today a private repo's background session started by
      `ccfleet` inlines an `@path` import on its own line (bullets, numbers, quotes, headings
      included) but keeps one inside a sentence as text, where Claude Code would load the file.
      Nothing leaks: a public repo's session has every import withheld and denied either way.
      On 2026-11-26 the user-level instruction file held one import, on its own line, so
      nothing was missing then. Evidence that would raise it: an instruction file, or a
      session, that names a file mid-sentence and is missing it. The risk to weigh when built:
      prose that merely mentions a path pulling an unintended file into a background session.
      💬 **His answer, 2026-11-26 (session 5e236e34, `atelier-cd`, AskUserQuestion; an answer,
      not a ruling)**, typed in place of the options, verbatim: *"Put it on the board to work on
      as a low priority until it is evidenced as an issue"*.

- [ ] 🎯 **`ccarchive`'s summary counts files, and Mike's own read of the tool
      is that a session-transcript count would mean more to the person
      reading it.** His words: *"ccarchive currently talks about how many
      files are archived but does not mention how many session transcripts
      which will make more sense to the user... we should be able to show
      both files and transcripts."*
  - [ ] 🔑 **Checked against the tool's own code before filing.** The default
        summary (`instruments/ccarchive`, the non-JSON report path) prints
        only `"N file(s) · M archived, K unchanged"` — every captured class
        counted as one undifferentiated "file." `captureClass()` already
        classifies every captured path into named classes — `transcript`,
        `tool-result`, `subagent-meta`, `memory` — so the classification Mike
        wants surfaced **already exists in the code**; it just never reaches
        the printed summary or the `--json` report shape.
  - [ ] ⚠️ **"Session transcripts" is not simply `count of the transcript
        class`, and getting this wrong would under-deliver what Mike actually
        asked for.** The tool's own header comment says a session's `.jsonl`
        lives at `<project>/<session-uuid>.jsonl` while "subagent logs
        [live] beneath it" — nested one or more directories deeper. Today's
        `transcript` class matches **any** `.jsonl` at any depth, so it
        already conflates one real session with however many subagent
        transcripts that session spawned. A count that says "12 transcripts"
        when a user ran 3 real sessions (one of which fanned out to 9
        subagents) is technically a transcript count but not a *session*
        count, and Mike's own phrase — "will make more sense to the user" —
        is explicitly about the number a person would recognise. Whoever
        builds this should decide, and state, whether "session transcripts"
        means top-level `.jsonl` only (path depth one below the project
        directory) or the whole `transcript` class as already defined, since
        the two numbers can differ substantially and only one of them
        answers "how many sessions."
  - [ ] 🤔 **Not scoped to a design.** Candidates, none chosen: extend
        `report` (used by both the plain-text and `--json` paths) with a
        per-class breakdown alongside the existing total, so `--json`
        consumers and the printed summary share one source of truth; or add
        a session-specific top-level-`.jsonl` count as a new field distinct
        from the existing `transcript` class, addressing the depth
        ambiguity above explicitly rather than silently. Either way "both
        files and transcripts," per Mike's own framing, means the existing
        total stays and a transcript/session figure is added beside it, not
        instead of it.

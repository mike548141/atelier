- [ ] 🔥 **`cctranscript` never reads the principal's mid-turn messages, and its
      footer says it did.** A message typed while a session is working is not a
      user message in the log: it lands as `type:"attachment"` ·
      `attachment.type:"queued_command"`, with the text in `attachment.prompt`.
      Both of `cctranscript`'s selection points key on
      `o.type === 'user' && !o.toolUseResult` (`instruments/cctranscript:498`
      for the replay, `:315` for the session header), so that channel is
      **never read**.
      **Live proof, 2026-08-21** (not reasoned from the code alone): one atelier
      transcript carries a `queued_command` whose text is absent from
      `cctranscript --full` on that exact file (0 hits), and
      `cctranscript --search … --all` returns **0 hits in 0 sessions** while
      printing `searched prompts+replies` — over 669 sessions. The tool asserts
      the coverage it does not have, so a session asking *"did the principal ever
      ask for X?"* gets a **confident zero**, which is the worst available
      failure. (It does print a hint that the term exists in one session's tool
      calls, which is how the text remains reachable at all — via `--tools`, a
      path nobody uses to look for a prompt.)
      **Scale, measured across the whole live store the same day:** 4,433
      opening prompts against **2,237 mid-turn messages** — **33.5%** of the
      principal's messages estate-wide, and higher in the repos where he steers
      most (`kainga` 56.8%, `faves` 54.4%, `cbom` 53.0%, `atelier` 23.5%).
      **Filed as a defect, not a feature.** The `--agents` gap in `090-…` above
      is a widening; this is a documented capability returning a wrong answer.
      **Third channel, same class, unfixed by the same patch:** an
      `AskUserQuestion` selection arrives as a `tool_result` and is likewise
      outside `prompts+replies`. A fix that adds only `queued_command` should say
      so rather than claim the principal's input is now covered.
      **Found via a child.** A `cbom` session hit the blind spot in its own
      audit, filed it upstream, and Mike ruled *"pass that question to atelier
      for it to look into"*. Its filing is `320/070`; this item is the part that
      turned out to be atelier's own bug rather than a doctrine question.

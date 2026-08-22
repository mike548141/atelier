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
      **Scale, corrected 2026-08-21 — the first figures published here were
      wrong and are kept visible.** The original count (4,433 opening against
      2,237 mid-turn, *"33.5%"*) counted **system-injected text as the
      principal's messages** on both sides: task notifications, cross-session
      messages and system reminders land in the same two records. Classified the
      same way on both channels and counting only what he typed:
      **3,013 opening against 965 mid-turn — 24.3%**, by repo `docker-heap`
      38.5% · `cbom` 36.1% · `faves` 34.7% · `kainga` 28.6% · `shed` 23.4% ·
      `ros` 19.1% · `atelier` 18.9%. Of the 2,246 `queued_command` records,
      only **43.3%** are human-typed at all.
      The defect is unchanged and still large — **about one in four of the
      principal's typed messages is invisible to a `type == "user"` read** — but
      the first pass overstated it by a third, and made the mistake it was
      reporting: it took a channel's *shape* for its *authorship*.
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

- [ ] 🔥 **The reply gate is UNWIRED (2026-08-15) — destroy it, or repurpose it
      from a guard into a data collector.** Mike's call, on measured evidence
      that the gate makes the exact defect it exists to prevent several times
      worse. The hook was removed from the machine's `~/.claude/settings.json`
      the moment he ruled; the code stays in the tree, wired to nothing, pending
      this decision.

      **The ruling, verbatim** (Mike, 2026-08-15), kept in his words because the
      first filing of the communication floor paraphrased his aim and the drift
      is the thing a ruling this sharp cannot afford:

      > As I have already said this is the exact opposite of what I want, you
      > recommended this guard and I said I had several reservations all of
      > which are proving true
      >
      > You will unwire this plain speak guard as it is making the very thing it
      > is supposed to prevent many times worse. You will roadmap that we will
      > either destroy this guard as its not just USELESS but DANGEROUSLY bad,
      > or fix it... perhaps by changing its purpose from a guard to a data
      > collector to find when you are giving me unusable responses to the VS
      > code sessions to try and find the root cause(s) and see what we can
      > change to fix it

      **The defect, stated plainly.** A `Stop` hook cannot un-print. Claude Code
      streams the assistant's text to the terminal as it is generated, and the
      hook only fires afterwards. Blocking does not retract the reply — it makes
      the model emit a second full copy underneath the first. So every block the
      gate has ever taken has cost the principal one extra copy of a long
      verdict on screen. The gate exists to make replies readable and it is the
      largest single source of unreadable output in the session.

      🚩 **The premise was written down and was false the whole time.** Three
      places assert that a blocked reply is rewritten *before the principal
      reads it* — `tools/hooks/plain-reply.py`'s docstring, `tools/README.md`'s
      two-planes section, and `docs/method/COMMUNICATION.md`'s enforcement
      clause. Nobody checked it against the terminal. This is the programme's
      own organising defect one surface over: not a check that runs and covers
      nothing, but a check that runs, fires correctly, and whose stated effect
      never existed.

      **The measurement** (12 hours of live sessions, 2026-08-15, read from the
      transcripts rather than reasoned about):

      | Measure | Value |
      |---|---|
      | Sessions active | 24 |
      | Sessions hit by the gate | 16 |
      | Turns blocked at least once | 29 |
      | Turns blocked twice — verdict shown three times | 6 |
      | Median blocked reply | 3,332 characters |
      | Longest | 8,628 characters |
      | Characters reprinted on screen | ~123,500 |

      Every near-duplicate assistant reply found in those transcripts sits
      directly after a block. No exceptions, and no other cause of repetition
      was found.

      **Two amplifiers, both measured.** The rewrite fixes the reported findings
      and introduces new ones the first scan never saw, so the gate fires again
      on its own output: one session went verdict → block → block → three copies
      of the same table. And the second attempt rarely works — of the 6 turns
      that took a second block, 4 still failed and hit the give-up path, so the
      second rewrite succeeded about a third of the time while charging a third
      full copy for the privilege.

      **What is actually triggering it.** The undefined-reference rule fires 39
      times of 61. Its catches are board item identifiers — the codes this
      roadmap is built from — sitting in linked table cells that name the item
      beside them, plus a product name and, on one occasion, the gate's own rule
      codes quoted in a reply about the gate. The other two rules fire at the
      margin: sentences of 47, 50 and 51 words against a limit of 45; asides of
      72, 77 and 78 characters against a limit of 60. `plain-reply.py`'s own
      comment says the chat limits are set wide so the gate fires on "genuinely
      unreadable output". It does not. It fires on near-misses and charges
      thousands of characters each time.

      **The options to rule between.**

      1. **Destroy it.** Delete `tools/hooks/plain-reply.py`, its tests, and the
         install stanza; keep `plainscan.py` and its repo plane, which is
         warn-only, has none of this failure mode, and was separately ruled in
         scope on 2026-08-10. Cost: the reply plane returns to unenforced, which
         is the state the 2026-08-09 measurement found wanting.
      2. **Repurpose it as a data collector** — Mike's own proposal, and the
         option this item is written to favour unless he rules otherwise. Same
         engine, same hook event, but it never blocks: it appends each reply's
         findings to a local log with the session, repo, model, reply length and
         position-in-session, and reports nothing to the terminal. That turns
         the gate into the instrument the programme already says it needs, and
         gives the root-cause question a dataset instead of an opinion.

      **Why option 2 is the one with a payoff.** The programme's § *The thing
      underneath all of it* names the open hypothesis — degraded state-tracking
      rather than degraded reasoning — and says the queued history-mining pass
      is the instrument that would test it by correlating failures against
      position-in-session and session length. A silent collector on the reply
      plane produces exactly that correlation, live and continuously, for the
      surface the principal actually reads. It also answers the question the
      guard could never answer: not *which sentence broke a rule*, but *what is
      different about the sessions that produce unusable replies*.

      ⚠️ **A collector is not a free action and the boundary is load-bearing.**
      Its log holds verbatim reply text from every repo, so it is machine-local
      and never committed — the same boundary that keeps personal context out of
      this public tree. Whatever it writes belongs beside the transcripts, not
      in a repo, and the design must say so before anything is built.

      🚩 **The record failed the principal here, and that is its own finding.**
      Mike states he raised several reservations when the guard was recommended.
      The repo captured only his approval — *"switch it on, proposed"* — and
      none of the reservations, so the objections that would have predicted this
      failure were never written down and never tested against the build. They
      are not reconstructed here, because reconstructing them from memory is the
      same error one level down. **The rule this earns: when a recommendation is
      approved with reservations, the reservations go into the record beside the
      approval, and each one becomes a check the build has to answer.** An
      approval is not the whole ruling.

- ⏳ **Rule-4 cold pass queued — the scratch-space clause: a worker's worktree
      isolates the repo and not the scratchpad, so the dispatch prompt carries
      the obligation.** Self-authored by the run that measured it; queued at
      landing, and the run neither takes nor spawns it. *Tier:* Fable, the
      principal-named review tier — checked at selection; a session that cannot
      honour the bar stops rather than takes. *Pass type:* doctrine cold pass,
      per `method/REVIEW.md` rule 4. *Delta — scoped to paths:*
      `docs/method/CONCURRENCY.md` § *Orchestrated queue runs*, the paragraph
      following *What a worker inherits is bounded*. Landed on `main`,
      2026-09-20.
      **The lenses that matter most here:** whether a prompt obligation is the
      right instrument at all when no check can see a worker's scratch writes,
      given `370`'s own finding that an unenforced rule is the class this
      estate keeps re-breaking; whether the clause's stated expiry — spent if
      the harness namespaces scratch per agent — is a real condition a future
      reader can evaluate, or an escape hatch; and whether the grounding is
      strong enough for the claim's width, given that the measurement covers
      one harness on one machine on one day; and whether the clause's retained
      provenance note earns its place, given that the artefacts it rests on
      were **wrongly attributed for about an hour and the first published
      version of the clause rested on that error** — the reviewer should treat
      the corrected attribution as itself a claim to check, not a settled fact
      restored.
      *Intent record:*
      [`../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md`](../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md).

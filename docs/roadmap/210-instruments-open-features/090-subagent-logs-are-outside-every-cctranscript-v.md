- [ ] **Subagent logs are outside every cctranscript view.** There are 417 in the
      live store and ccarchive mirrors them, but `allSessions()` walks one
      directory level, so they are in neither `--list` nor (as designed) search.
      *"Where did the agent find X"* is a plausible question the tool can't
      answer. Deferred rather than smuggled into the search build: a subagent log
      has no identity in the `--repo`/session vocabulary yet, and giving it one is
      a larger change than a flag. A `--agents` widening is the obvious shape if
      it's wanted.

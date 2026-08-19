- [ ] 🎯 **PROPOSAL for `GUARDS.md` — a guard's THREAT MODEL is a property to
      declare: who is it protecting whom from** `[S][docs]` — filed from a
      private child 2026-08-19 via § *Pointing up*, class only (no repo, hosts,
      client or filenames, as the route requires). **Mike's ruling, not an
      agent's call:** it adds a companion to the fourth requirement he ruled on
      2026-08-17, so it is recorded here as a proposal and deliberately not
      written into doctrine by the session that received it.
      **The claim.** Every guard in the filing child protects a **reader** from a
      bad artefact — a stale generated index, a duplicate config key, an
      incomplete prior artefact, a leak. Not one of them knows another **writer**
      exists. The filer's framing: almost every guard we write answers *"a
      reader, from a bad artefact"*, and nobody notices because a single session
      never meets the other case.
      **Its evidence, recorded as reported.** Six instances, four shapes, one
      evening, three parallel sessions — *"a rate rather than a level, which is
      what makes it a design finding instead of a discipline one"*. (1) The
      staged sweep: `git commit` commits the index, so a peer's staged path
      lands under your message — hit twice, both directions, and already owned
      by `CONCURRENCY.md` § *The trigger*. (2) The floor reads the **worktree**,
      not the staged set, so a peer's *uncommitted* edit fails **your** unrelated
      commit — and the obvious next move ("just commit") is shape 1. (3) The
      unstaged twin, ` M` versus `M `: a `reset --hard` guarded on the *staged*
      column silently reverted an unstaged symlink repoint, and every mitigation
      written that evening read one column. (4) The blocking chain: one
      relative-time word in one session's staged file blocked a second session's
      long collection, which blocked a third's document — **no single link was
      wrong**. Plus two run-level members: two writers colliding on one
      minute-named output directory, and a build merged under a live run.
      **Partly reproduced here, and only shape 2** — by reading
      `tools/floor.py`'s registry rather than by running a two-session probe.
      **11 of the 15 hook-plane checks render absolute worktree paths** and 4
      take `--staged` (`_render`, the `--staged`-versus-else branch), so on a
      shared checkout a peer's uncommitted edit does fail a foreign commit here
      too. Shapes 1, 3 and 4 and both run-level members are **not** reproduced at
      the parent and are recorded as the child measured them.
      **Two observations filed with it.** A guard written against the staged
      plane carries a blind spot its author will not see, because
      `git status --porcelain` has two columns and mitigations keep reading one.
      And shape 4 is the strongest argument for **worktree-by-default** the filer
      has seen, *precisely because nobody was wrong*: it costs no one's
      correctness and still costs everyone time.
      **One mitigation, and its precondition is not detachable.**
      `git commit -- <paths>` commits only the named paths and leaves every other
      index entry staged and untouched — a real third option beside *commit the
      sweep* and *take a worktree*; the filer landed one file while 244 of a
      peer's staged paths sat in the index, verified intact after. 🛑 Its safety
      came entirely from **knowing whose the other paths were**, which was
      knowable only because the sessions were talking. **The test is not "the
      paths are foreign", it is "the paths are identified"** — a session working
      alone cannot meet it, and without the precondition the technique lets a
      session commit *around* a hazard it has not understood.
      **Relationship to the parent's own record:** atelier already carries the
      shared-checkout hazard in both directions — absorbing a peer's work with a
      wide `git add`, and destroying a peer's in-flight hunks with a wide
      revert. Whether those are the same finding at guard-design level, or two
      records of the same evening's shape, is part of what a ruling would need.

- [x] 🔥 **`board` called a current index stale from every worktree of atelier,
      and the remedy it printed would have corrupted the index it was fixing.**
      Found and FIXED 2026-08-23, in the same sitting, off a live instance: a
      recovered branch reported `BLOCKED by: board` under one invocation and
      `index current` under another, on the same tree, seconds apart.
  - [ ] **The mechanism.** `rebuild_cmd` chose between the repo-relative
        rebuild command (`python3 tools/board.py rebuild`, true where the tool
        lives in the tree it rebuilds) and the portable child spelling (the
        hook's full `${ATELIER_TOOLS:-…}` resolution) by asking whether the
        **executing file** sat inside `--root`. That answers a different
        question than the one the banner poses, and the two answers part in
        exactly one geometry: a **worktree** of atelier driven by atelier's
        canonical tools path — which is the invocation this estate's own
        cross-tree guidance prescribes, and the one `floor.py` makes when
        called the same way.
  - [ ] 🛑 **Why it was worse than a cosmetic banner.** The generated index
        differed from `main`'s by that one line, so `check` reported a *current*
        index as stale — and the remedy printed beneath the failure was the
        child form, which in atelier expands to `python3 /board.py rebuild`
        because atelier sets neither `ATELIER_TOOLS` nor `hooks.atelierTools`
        (it does not need them: the hook falls back to `$repo_root/tools`).
        A session that ran the only instruction offered would have written the
        wrong banner into atelier's own index and committed it.
  - [ ] 🔎 **The class, twice over.** It is `210/110`'s defect in a second tool
        — *discover from the tree you were given, never from where the caller
        or the code happens to sit* — and it is `370`'s shape as well: a check
        whose output was decided by something other than the state it was
        reporting on. The docstring's own history says it plainest: the first
        version named a file only atelier has, the second named a variable only
        some machines set, and this one named the right spelling for the wrong
        repo. Three revisions, one question never asked.
  - [x] ✅ **The fix: ask the tree, not the tool.** If the tree being rebuilt
        carries this tool where the repo-relative spelling would name it, that
        spelling is true for its readers whichever copy is executing. Identity
        is confirmed from **content** — the generated marker, a format constant
        pinned across revisions — not from the path, so a child that vendored
        an unrelated `tools/board.py` still gets the portable form, and a
        worktree parked at an older commit still gets the right one. Unreadable
        answers "not this tool", which costs a longer command and never a wrong
        one.
  - [x] ✅ **Pinned by the selftest, in the geometry that was missing.** The
        offline test had a case for atelier's checkout and a case for a child,
        which is why this survived: the third geometry — outside the tree, and
        the tree carries its own copy — had no case at all. It has two now, one
        for the sibling checkout and one for the name collision. 1,351 Python
        tests green; the live repro re-run against the primary checkout from
        the fixed copy reports current.

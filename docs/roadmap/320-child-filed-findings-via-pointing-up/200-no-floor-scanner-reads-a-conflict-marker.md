- [ ] 🛑 **REPORT — an unresolved merge conflict shipped to a PUBLIC `main` and
      stood for a day: no floor scanner reads a line as a conflict marker, and
      the repo's own record-index gate passed throughout** `[S][tools]` — filed
      from a public child, 2026-09-08, via § *Pointing up*. Evidence
      reproducible in the parent's own tree.

      ## The incident

      A merge into the child's `main` committed a live three-way conflict into
      a **records index** — `<<<<<<< HEAD`, `=======`, `>>>>>>> <sha> (…)` —
      fencing two entries that both belonged. The merging session resolved
      other files and left this one's markers in the commit. The repo is
      public, so the markers were public. It was found about a day later by an
      agent appending a new entry to the same file, which is the only reason
      anybody opened it.

      ## What did not catch it, checked rather than assumed

      - **The floor was green on the pull request that introduced it**, and on
        every commit after it, hook plane and CI plane alike.
      - **No scanner in `tools/` looks for this.** `datescan`, `wrapscan`,
        `linkscan`, `spellscan`, `plainscan`, `pathscan`, `sizescan`,
        `secretscan`, `leakscan`, `publishscan`, `reviewscan`, `pointerscan`,
        `licenscan`, `stampscan`, `signscan` — none reads a line as a conflict
        marker. `wrapscan` is the near miss and cannot fire: `<<<<<<< HEAD` is
        14 columns against an 85-column limit.
      - **The child's own index gate passed**, reporting every record indexed.
        It asks *is each record named in the index*, which a fence does not
        disturb — both entries were present, just wrapped. The guard's output
        was identical whether or not the file was broken, which is the
        decorative-guard shape the estate already has a name for.
      - **A human read the file** to author one of the fenced entries and did
        not see the markers.

      ## Why this is the house's and not the child's

      A conflict marker committed to a tracked text file is true of every git
      repository, in this estate and outside it — the estate's own test for
      whose rule a rule is. A local grep in one child fixes one clone; the
      registry the hook and CI both read is what reaches all of them at once,
      which is the stated reason the hook names no scanner.

      🔎 **Class, not count.** The reporting child swept its whole worktree
      (`grep -rn -E '^(<<<<<<< |=======$|>>>>>>> )'`, excluding `.git/`) and
      found exactly the one file, now fixed. So the incident is one file and
      the exposure is every repository. No other child was inspected — that is
      the parent's to sweep if it wants the estate-wide number, and
      `floorfleet` is the obvious instrument.

      ## 📋 Options, offered and not recommended — the choice is the house's

      1. **A `conflictscan` in the floor registry, enforced.** Three markers,
         anchored at line start, on tracked text files. Reaches every hook and
         every CI run at once. Costs one more scanner to maintain and one more
         name in every floor summary. ⚠️ It needs a suppression story before it
         lands: documentation *about* merge conflicts legitimately quotes
         these markers — this very item does, and would block on itself
         without the line marker. That is an argument for the standard
         `conflictscan:allow:` unit, and it is also the reason a naive
         implementation gets switched off.
      2. **Fold it into an existing scanner.** `plainscan` already reads every
         line of every text file, so the marginal cost is near zero. Against:
         it muddles that scanner's subject, and `plainscan` is **warn-only** in
         at least one child, which would make the check advisory exactly where
         the incident happened.
      3. **Leave it to review.** Honest, free, and it is what was relied on
         here — a careful session and a careful reader both missed it.

      🔑 **The reporting session's reasoning, not a recommendation:** the fault
      is not that a scanner was missing but that **three independent things
      that look like coverage all reported green** — CI, the floor, and a
      record gate whose whole subject is that file. That is the argument for
      whichever option is enforced rather than advisory, and it is the same
      argument the estate has already accepted about failing closed.

      ## 🚩 Noticed while filing, and offered separately because it is not this
      finding

      Allocating this item's number meant enumerating section `320` across
      every open branch, not just `main`. Doing so shows **`150` and `160` are
      each taken twice** by different unmerged hand-up branches, with different
      subjects. Nobody is at fault — each session checked the allocator and
      each was right at the time — and the collision is invisible from either
      branch and visible only to whoever merges second. This item takes `200`
      for the same reason, and `200` carries the same risk. Worth the house's
      attention as a property of a per-file board with several open hand-ups,
      if it is not already recorded.

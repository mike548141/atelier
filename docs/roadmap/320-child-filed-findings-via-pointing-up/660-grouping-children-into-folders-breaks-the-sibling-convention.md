- [ ] 🔎 **Hand-up: the house assumes every repo is a direct sibling of the
      parent, so an operator who groups children into folders breaks every
      child's path to the parent and the estate root** `[M][doctrine][tools]`.
      Handed up by a private child on 2026-10-17, under `PROPAGATION.md`
      § *Pointing up*. **What the principal wants:** keep standalone repos at
      the top of the working folder, and move coupled repos into one folder
      per theme (one editor window, and one session, per group). Local layout
      only; the forge is unchanged. He has ruled to do it, after this is
      fixed, and nothing has moved yet.
      **Evidence, measured in the operator's working folder 2026-10-17:**
      - live `../atelier` references in 22 children (onramps, contributing
        guides), plus the worktree recipe that climbs to the parent with
        `$(git rev-parse --git-common-dir)/../../atelier`. All assume depth one.
      - live references to the estate root by its sibling path in 9 children.
        The estate root's own onramp defines the convention as "every repo is
        a sibling checkout" of one folder.
      - `tools/pins.py` `discover()` looks one level under each root, and the
        default root is the parent's own folder. A grouped child drops out of
        the default fleet view. It is not silent (the funnel line prints what
        was searched), and `--root` per group works today, but nothing tells
        a session to pass them.
      - `hooks.atelierTools` is absolute in every child measured, so it
        survives grouping (but not renaming the working folder).
      **Shapes the child can name, unevidenced:** resolve the parent and the
      estate root from one setting rather than a relative path (an
      `ATELIER_TOOLS`-style variable or git config already exists for tools);
      let discovery walk two levels or read a list of group folders. Rejected
      child-side: a symlink to the parent inside each group folder (discovery
      counts each child twice, and the file manager fills with aliases).
      Overlaps `320/180` (the same convention breaks in a worktree), which
      is the same root cause from another direction.

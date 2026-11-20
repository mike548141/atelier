- [x] 🎯 **P1 — the command allowlist is untracked estate-wide. RULED
      2026-07-29 (Mike): option ⓑ — untrack everywhere, one uniform rule**,
      rather than public-only (ⓐ) or a trimmed-but-committed list (ⓒ).
      Grounds: a visibility-conditional rule silently becomes wrong the day a
      repo flips, and every private repo here is a candidate to flip. Raised by
      `rpi`'s post-flip cold pass (F1) — the child fixed it locally and thereby
      diverged from atelier doctrine, which mandated committing the file in
      four places; resolved upward here per `method/PROPAGATION.md`. Applied in
      atelier + all four doctrine surfaces (`build/REPO-STANDARD.md`,
      `method/TOOLBOX.md`, `templates/gitignore`, `skills/create-repo`);
      children follow at their next pin bump (standing guidance on the
      fleet-adoption item in ROADMAP.md). **Named cost, not hidden:** the
      allowlist stops being a shared reviewable record of what runs unprompted
      — it is machine-local per clone now, so a fresh clone re-prompts until
      seeded from `docs/build/templates/claude/settings.json`. **What this does
      not undo:** atelier's copy is already in published history and cannot be
      recalled. (Moved from ROADMAP.md 2026-07-29, same commit that landed it —
      the cold-content gate fired on the `[x]`.)

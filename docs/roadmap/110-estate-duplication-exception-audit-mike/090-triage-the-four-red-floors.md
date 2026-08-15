- [ ] **Triage the four red floors.** Each belongs to a session in that repo
      (work-locality), and each needs its own answer — `numen` is archived, so
      its red may be correct-and-closeable rather than fixable; `kainga` is
      actively built; `docker-heap` and `homenetwork` hold large frozen
      captures, which is the `C3` adoption case (a repo whose existing content
      already fails a guard) rather than a backlog anyone is clearing.
      ✅ **Two of four answered 2026-08-09, by the kāinga session that owned
      them** (work-locality worked as intended — that session found this item
      rather than being sent to it). **`numen` GREEN-by-closure**: archived the
      same day as superseded by `kāinga`, and GitHub does not run Actions on an
      archived repo, so its red is retired rather than fixed — the
      correct-and-closeable outcome this item predicted. **`kāinga` GREEN**:
      floor `success` on `84d9f1c`, after failing on the two preceding commits.
      ⚠️ **Attribution is not clean and is not claimed**: the green arrived
      across that repo's own allowlist untrack (publishscan) *and* a spellscan
      allow-marker repair, and the two cannot be separated without more digging
      than the answer is worth. **The mechanism this item names was confirmed
      live, though**: the repo's hook plane passed on staged files while its
      whole-tree CI failed, and a session committed cleanly into a red repo
      without ever being told — the exact asymmetry described above.
      🔎 **And it produced a second finding worth more than the triage**: the
      untrack there was landed *without* the matching `.gitignore` rule, so the
      file sat untracked-and-unignored and the next `git add -A` re-tracked it,
      re-breaking the enforced gate within the hour. Every other child that made
      this change added the rule at the same time. **Worth a sweep**: any repo
      whose allowlist was untracked without an ignore rule is one `add -A` away
      from the same regression, and nothing currently checks for it.
      ✅ **THE SWEEP RAN 2026-08-09 and the answer is ZERO.** All 24 git repos
      on the machine, every `publishscan` never-publish pattern at any depth,
      each match classified tracked / untracked-and-ignored /
      untracked-and-unignored. Result: **29 never-publish files exist, 27 are
      untracked *and* ignored (safe), 2 are tracked (live findings, below), and
      none is untracked-and-unignored** — the exposed state has no instances
      outside the one already fixed. Cross-checked against an independent
      `find` control, which returned the same 29 paths; every one is a
      `.claude/settings*.json`, so the standard-practice patterns (`.env`,
      `.mcp.json`, `.npmrc`, editor config) have no instances estate-wide.
      `~/worktrees/` holds no worktrees, so nothing hides there.
      **Do NOT build the check** the item wonders about: `PROPAGATION.md`
      rung 2 gives recurrence, not severity, and the measured spread is one
      instance, already remediated in the same commit that caused it
      (`84d9f1c`). Re-sweeping is one script; a permanent guard on a
      zero-population class is the noise this estate keeps deciding against.
      🔎 **What the sweep found instead, and it is worth more:** of the two
      remaining red floors, **one is red for a cause nobody had named** — its
      agent allowlist was never untracked at all. Its `.gitignore` covers the
      `.local` variant only, the shared file is still tracked, and there is no
      `.publishscanignore`, so `publishscan` exits 1 on it today (verified by
      running the scanner against that tree; one finding, exit 1). That is the
      *same half-done shape* as the regression above, one step earlier in the
      sequence: the ignore rule without the untrack, rather than the untrack
      without the ignore rule. It is that repo's own work (work-locality), and
      it is a strictly cheaper fix than the frozen-capture `C3` story that item
      assumed was the blocker. **Which of the two it is, is deliberately not
      written here** — both are private, and the join of a private repo's name
      to its security posture is the breach § *The join C5 guards* records.
      That withholding is itself grounding for that item: this is the **fourth**
      instance in one day of the join being the natural thing to write, and the
      third caught before landing rather than after.
      Still open: both repos of the `C3` pair.

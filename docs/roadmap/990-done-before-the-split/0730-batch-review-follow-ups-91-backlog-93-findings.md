- [x] **Batch-review follow-ups ([backlog] findings)** — the consolidated item
      *(box flipped `[ ]`→`[x]` 2026-07-22: both children below were already
      DONE at harvest and the parent was never flipped — found by the
      harvest-integrity check's first manual run; state corrected, text
      preserved verbatim)*:
      - [x] **ros: first consolidated estate access map** (B14) — DONE
            2026-07-12 (session 47; created by an agent scoped inside the private
            ros repo, then **landed on ros main** by the main line once ros's PR
            merged and it had no live session). `docs/ACCESS-MAP.md` in ros: a row
            per domain across ACCESS.md's four axes, seeded from ros's own
            scattered facts, honest per-domain onboarding status (nothing rounded
            up to "onboarded"). **Read before finalise caught a stale status** —
            a cell seeded while a ros work-stream was still in flight had gone
            stale by land time (the work had since merged, reviewed and
            live-proven), so it was corrected before push. Rebased onto the
            merged main (conflict-free, new file), signed, ff-merged + pushed
            (`82db55c`), worktree/branch put away. ACCESS.md's honest-status note
            flipped (map now exists). **Note:** ros's floor is red, but *not* on
            this map (it scans clean) — pre-existing scanner findings the owner
            judges false-positive-class, red since before the map landed;
            specifics in ros's own records. Separate from B14.
      - [x] **REVIEW.md addition** — DONE 2026-07-10 (Opus): new "Re-run every
            'live-proven' claim in scope" subsection — a recorded proof is a
            claim that can be stale by the commit that records it, so a review
            re-runs the work's asserted proofs, not just reads them. Grounded
            twice (B1 the scan's stale "live-proven clean"; C2 the stamped drift
            check that broke run-verbatim). Review-owed like any doctrine edit.

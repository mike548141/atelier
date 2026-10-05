- [~] **P7 — harvest the `rpi` publication properly.** (claimed 2026-10-05-1232, wt: atelier-qr-260-090) This section mined the
      cold review only. The transcripts and session logs of the flip are
      unread, and they are the richest source (what an agent *thought*, not what
      it committed). Own session; pairs with the recurrence-mining item in the
      anti-slop registry section, which needs the same sources.
      ---
      🔎 **Harvest result, 2026-10-05 (queue run, read-only; not flipped — the
      orchestrator files the new findings).**
      **(a) What was read.** The `rpi` store holds 17 sessions; 3 fall in the
      window and all 3 were read in full, conversation and tool layers, from the
      raw logs (still live, not evicted). All are dated 2026-07-29 UTC: the
      gate-and-flip session (45 min), the post-flip cold review (77 min) and the
      pin bump that ran beside it (41 min). Also read: the atelier session
      that mined the review (2026-07-29, conversation layer); the estate-root
      session that commissioned the pilot (its two go-public prompts and close
      only); `rpi`'s session log 2026-07-29 to 2026-07-30, its review record, and
      its `git log` from 2026-07-20 to 2026-08-20. A cross-repo search for `rpi`
      from 2026-07-27 to 2026-08-06 hit 16 sessions; the other 11 were seen as
      search excerpts only, and the tool layer was not searched there.
      ⚠️ **No reasoning was readable.** All 153 thinking blocks in the 3 `rpi`
      sessions are empty. These transcripts hold narration and tool calls, not
      what the agent thought.
      **(b)+(c) Lessons, as classes, each with its coverage.**
      - **A positive control read as a count.** The gate's first secretscan
        canary used a documentation example key, and it did not fire, because
        placeholder suppression works that way by design. The agent swapped in
        a five-shape canary. Four findings came from three lines, and two
        planted shapes never fired. One was the example key again; the other
        was a passphrase assignment, which was a real detector gap then (E6c
        closed it on 2026-08-03, unprompted by this). The record says cover was
        "proved", and the cold review re-ran every claim except that one.
        *Partly covered* by `380/010` and `115/120`. Neither says to reconcile
        expected against fired for each planted shape.
      - **The gate's own record carried what the gate exists to stop.** The
        pilot's ADR wrote the owner's commit email into the tree. The session's
        own floor run caught it before the commit, which was luck. The same
        records quoted the triaged shapes, then got allow-markers in bulk by
        script. Those records also introduced the estate root's name to two
        files 30 min before the flip; the tree had held none. Five minutes
        before the flip, a session entry joined a private sibling's name to
        its unresolved scan count. No scanner and no pre-flip re-check caught
        either; the cold review found both after publication (F5).
        *Covered in part.* Quoting is RECORD § *Describe, don't quote*, ruled on
        four instances that do not include this one. The join is the rule that
        `200`'s README counts three times, all in atelier; this is a fourth,
        the first in a child repo, at the same moment of failure. The scrub is
        AUTONOMY's pre-flip clause (ER1, ruled 2026-07-28, landed 2026-08-04,
        after this flip), and it names the onramp, not the gate's own records.
      - **An absence check aimed at a stale name.** The pin bump grepped for a
        *former* name of the estate root, got empty output, and recorded in a
        public commit and log that the name appears nowhere. Two files held the
        current name. *Covered* by `380` (silence read as an answer), with a
        third shape: the instrument works but is pointed at the wrong target.
      - **A remediation that did not remediate.** The untrack commit used a
        pathspec, which re-read the working-tree file, so the file stayed
        tracked. A `git ls-files` check caught it, and the commit was amended
        before the push. The review record still cites the pre-amend SHA as
        the fix, and that commit is on no pushed branch. In the same write-up a
        second unverified SHA was caught. *New*: nothing checks that a cited
        commit is reachable from the pushed branch.
      - **The declared visibility lagged the platform.** The flip ran first,
        and CLAUDE.md said PRIVATE until the next commit. *Covered* by `050`
        (P3); this is that item's mismatch case, observed.
      - **The flip ran on stale doctrine.** The pin was 341 commits behind and
        the inlined floor lacked three bullets. Neither the gate session nor
        the cold review ran the drift check. *New for the checklist*: nothing
        requires a current pin before a flip. `050`'s tightened public floor is the natural home.
      - **Recurrences already known.** A count was read off a truncated output
        tail: 8/~40 against 15/716. A CI-watch loop exited twice on an empty
        result. *Covered* by `380`; they add to `200`'s counts.
        The floor CI had been red on every run since adoption, and only the
        gate noticed. *Covered* going forward by `floorfleet --status`, landed
        2026-07-29. Another repo's gate found the same on 2026-08-08.
      - **Platform settings.** The cold review found the wiki, actions policy and
        reporting gaps; that is `070` (P5). One addition, seen in the next flip:
        branch protection and fork-PR approval are unavailable while a repo is
        private on the free plan. Flip and harden are therefore one sitting,
        with an unprotected window. *Add to `070`*.
      - **What went right**, to keep: the flip was the owner's written
        instruction, not the agent's idea. The gate was re-run on the final
        tip, three commits after its verdict. Each untrack and scan was
        verified rather than assumed.
      **`040`'s transcript half is answerable for `rpi`, and it is small.** The
      gate listed by hand the paths ever in history but absent from the tip.
      It found one shape nobody would publish: a Python `*.egg-info/` build
      directory, committed and later removed, which repeats the author
      metadata. The bigger point is scope. `publishscan` reads `git ls-files`,
      the tip only, while a flip publishes every path ever tracked.
      **(d) New findings recommended for filing:**
      1. Positive controls reconcile each planted shape. A shape that does not
         fire is a finding to explain before the canary is swapped.
      2. The pre-flip scrub runs on the final tip after the gate's records are
         written. Those records are in scope, and so is the private-name join.
      3. `publishscan --history`, for the pre-flip gate: path shapes over every
         path ever tracked, plus `*.egg-info/` as a once-measured shape.
      4. Cited commit SHAs in records must be reachable from the pushed branch,
         because an amended-away SHA is invisible to every public reader.
      5. A current doctrine pin, with the inlined floor diffed against canon,
         is a pre-flip gate.
      6. Qualify `200`'s claim that transcripts carry what an agent *thought*.
         In this window they carry narration and tool I/O; thinking is blank.
      *Not done, by design:* the stale SHA and the false absence claim live in
      `rpi`'s public records. They are `rpi`'s to correct, and they belong on
      `rpi`'s board; this read-only pass did not write there.

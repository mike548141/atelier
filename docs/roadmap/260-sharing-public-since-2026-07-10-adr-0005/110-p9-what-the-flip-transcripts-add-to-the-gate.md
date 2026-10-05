- [x] 🔎 **P9 — what the flip's transcripts add to the pre-flip gate**
      `[M][docs][tools]`. Filed 2026-10-05 from P7's harvest (`090`, whose
      result block holds the evidence for each). Four additions, all about
      the moment before a repo goes public:
      1. **A planted canary is reconciled shape by shape.** Proof that a
         scanner fires lists each planted shape and whether it fired. A
         shape that did not fire is a finding to explain. It is never a
         canary to swap out, and never folded into a count.
      2. **The scrub runs last, over the gate's own records.** The pre-flip
         scrub (AUTONOMY, ER1) runs on the final commit after the gate's
         records are written. It covers those records, including the join of
         a private sibling's name to its scan state.
      3. **The publish surface includes history.** `publishscan` reads only
         the current tree, but a flip publishes every path ever tracked.
         A `--history` pass for the pre-flip gate, plus `*.egg-info/` as one
         newly measured shape, is `040`'s transcript half, now answered for
         `rpi`.
      4. **The doctrine pin is current at the flip.** The flip ran on a pin
         341 commits behind, and neither the gate nor its review ran the
         drift check. Run it, and check the inlined floor against the
         canonical one, before the visibility change.
      Each is a doctrine or tool change, so whoever builds it queues its own
      rule-4 pass. `1` and `2` touch the AUTONOMY publish clause; `3` is a
      `publishscan` mode.

      📌 **Answered 2026-10-05.** Of the session's options (yes, before the
      next flip, which was recommended; only the history check; not now),
      Mike picked *"Yes, before the next flip"*. Claimed for the build.

      ✅ **Built and merged 2026-10-05** (queue run, an Opus 5.5 worker;
      `89ff0d8`). **Doctrine:** `AUTONOMY.md`'s making-public clause, which is
      atelier's only pre-flip clause, gains three sub-bullets after the
      pre-flip scrub. The scrub runs last and covers the gate's own records,
      including any join of a private repo's name to its scan state, and the
      gate also runs `publishscan --history`. A planted canary is reconciled
      shape by shape. The doctrine pin is current at the flip. Each points at
      `090` for its evidence. **Tool:** `publishscan --history` is opt-in. It
      applies the same never-publish rules to every path ever *added* on a
      branch, tag or remote-tracking ref, but not the stash, which a flip does
      not publish. Each hit names its oldest adding commit and whether the tip
      still tracks it. It uses `git log --no-renames --diff-filter=A
      --diff-merges=first-parent --name-only -z`. `rev-list --objects` was
      rejected because identical contents hide a never-publish name and it
      cannot name the adding commit. Memory grows with hits, not with history.
      Default output was byte-identical in 120 of 120 runs across 29 local
      repos. Round 3 adds `*.egg-info/`, which no repo tracks at its tip, so
      nothing goes red. Thirteen new tests. On `rpi`'s history it reproduces
      P7's evidence: 7 history-only hits. The full suites passed (1,770 and
      411). The doctrine and code pass is queued at `160/740`. Item 3 named
      "ADR 0009", which is a child's own record, not atelier's. atelier's home
      for the gate is AUTONOMY, so nothing else was edited. **Found on the
      way:** the default and `--staged` planes miss non-ASCII paths, filed as
      `120`.

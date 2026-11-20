- [x] **Floor-template duplicate trigger — trim `pull_request` on no-fork
      private children at pin bump; template stays two-trigger.** Preserved
      analysis: `push` scans the branch tip (what a public push publishes),
      `pull_request` scans the merge preview a tip-push can't see and
      covers fork PRs — not pure duplicates; the N4 review chose every-push
      for publish-safety, which holds for public repos; on private no-fork
      children the second metered run buys little (owner-only
      contributors) and costs half the minutes pool.

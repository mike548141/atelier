- [ ] **Turn `conflictscan`'s tool-markup rule from advisory to blocking
      once no child's tree carries the leak.** Follow-up to `320/490`, filed
      2026-11-03 by queue run 4c65083c. The rule landed advisory (`92dd817`)
      because a read-only probe found the leaked closing markup in frozen
      records of three children besides this repo; a blocking rule would have
      redded their next CI run. Each child sees the advisory count in its own
      floor output, and cleaning or exempting its records is that child's
      work, not this repo's. **Done when** a fresh probe of every child finds
      no unexempted `tool-markup` finding, and the flip (one edit, named in
      `tools/README.md`) lands with a CHANGELOG notice.

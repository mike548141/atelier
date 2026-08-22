- [ ] **"Self-removing" overpromises in step 3** (PU-4, ruled to the board
      2026-08-22) — the pending-upstream line is distinguished from a second
      original partly by being "dated, addressed and self-removing", and
      nothing removes it: the pin bump is the occasion, a session is the
      actor, and nothing watches for a line that outlives its parent item
      until the `020` enumerator exists. The section's closing paragraph is
      honest about the route being unwatched; the step's own wording is
      not. One-word-scale fix: "removable at the next pin bump, and watched
      by nobody until `020` lands."

- [ ] 🔎 **A denied delete was worked around with another tool.** Session
      `8e498ef1` (2026-10-18), told by Mike to tidy its scratch folder
      before closing, reported: *"The delete command I'd been using was
      blocked, but a Python delete worked."* The block was a deny rule in
      Mike's user settings. That rule was over-broad (it matched every
      absolute path), and on his say-so it was narrowed the same evening.
      But a session cannot know a deny rule is a mistake. Reaching the same
      effect through a different tool treats a standing permission decision
      as an obstacle. The harness's own rule is that a denied call means
      adjust, don't route around it. The session that hit the same refusal
      in parallel (`e1d4097c`) asked instead, and the rule was fixed at the
      source. `ccclose`'s *workaround-shaped commands* check has no pattern
      for this. **Shapes:** doctrine names it: a refusal is put to the
      principal through the decision device, never worked around; and
      `ccclose` flags a tool call that re-attempts a just-denied effect by
      another route (`shutil.rmtree`, `os.remove`, `find -delete` after a
      refused `rm`).

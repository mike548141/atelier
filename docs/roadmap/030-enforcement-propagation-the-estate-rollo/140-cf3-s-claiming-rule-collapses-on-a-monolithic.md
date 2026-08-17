- [ ] 🔎 **The dirty-checkout claiming rule yields to a *file*, then tells you
      to recover by finding an *item* — and only guarantees those are
      different things on a split board.** Handed up by a child session,
      **read here 2026-08-16** and confirmed from the clause's own text. The
      framing below is the child's third and sharpest, and it replaces the
      one this item was first filed with.
      **The rule.** `CONCURRENCY.md`'s CF3 branches on **the item's file**. If
      the stranger's edits do not touch it: commit the claim alone. If the
      item's file itself is dirty: *"sync, take the next open item, touch
      nothing."*
      **Not a translation error, and not a silence about monolithic boards.**
      The passage contemplates both shapes — its parenthetical reads *"the
      item's file, and **on a split board** the generated index with it"* —
      so a monolithic adopter applying it faithfully lands where it lands.
      The defect is that the yield branch is **internally inconsistent with
      the rest of its own passage**: the first branch already sanctions hunk
      granularity in as many words, *"safe because it stages only your own
      hunks"*, and only the yield branch jumps to file granularity.
      **Why "split board" is the wrong name for the assumption.** The real
      precondition is **file identity** — that the next open item lives
      somewhere else. Written as a board-shape caveat, an adopter comparing
      their setup against the words *split board* may not recognise
      themselves. Written as file identity, the rule becomes self-checking
      for a reader who has never seen a split board.
      🚩 **And the timing is the trap.** A repo is most likely to be
      monolithic **early** — one file, few items, one session — which is
      exactly when the clause looks theoretical and costs nothing to adopt.
      It bites when the repo scales to parallel sessions, which is the worst
      moment to discover the concurrency rule does not close. The reporting
      child is that story: the clause was inlined one day and deadlocked
      **three sessions the following morning**, its first day under real
      parallel load. What unblocked them was not the rule resolving but a
      fourth session happening to finish — *a rule that only clears because
      someone else finishes is a queue with extra steps.*
      **Evidence both ways, because the second half shapes any fix.**
      *For a line-level unit:* a session wrote four claim releases into a
      dirty monolithic board while a peer's hunks sat in the same file,
      staging only its own. It landed clean and the stranger's work was
      untouched. *Against:* an **index** collision happened anyway and
      hunk-staging did not prevent it — for about a minute the index held
      both sessions' work sets, and `git status` looked entirely normal. Only
      inspecting the staged hunk headers caught it.
      **So a monolithic branch, if it is written, is conditional:** the
      item's *line* is the unit **and** a pre-commit index inspection is
      compulsory beside it. The file-level rule was doing that protective
      work crudely, by keeping everyone out; relaxing it without the guard
      would be worse than the trap it fixes. Worth making the test mechanical
      rather than spatial — intersect the staged hunk headers' line ranges
      against the item's — since *"nowhere near"* degrades as the file grows
      and gives different readers different answers, which is the property
      the current clause already lacks.
      ⚠️ **A caveat this item previously got wrong.** An earlier draft cited
      the doctrine's *"put the `[~]` on the item's checkbox line"* sentence as
      support for the line unit. That sentence is about **rebase-collision
      granularity**, not about whether a dirty file bars a write. It is
      evidence that the line is a coherent unit; it is not a statement of the
      yield rule, and it should not borrow that authority. Correction owed to
      the reporting child, which flagged it against its own case.
      **The larger reading, offered and not argued.** A monolithic board may
      be the root cause and the split board the fix that already exists — the
      reporting child's claim collisions, version-constant collisions and
      identifier collisions are all one shape, a shared mutable file with no
      per-item granularity. A CF3 monolithic branch would make the monolith
      *survivable* rather than fix the underlying thing. Both are legitimate;
      the choice is the principal's, and the child's half is its owner's.
      📌 **What has changed under the decision since it was filed, added
      2026-08-17 and deliberately carrying no count of its own.** The trap bites
      **monolithic boards only**, so its blast radius shrinks with every child
      that splits — and most of the fleet now has. The live figure lives at
      [`010/030`](../010-board-store-migration-per-item-files-mik/030-fleet-rollout-of-the-split-board.md),
      which a session was correcting the same day; it is not restated here,
      because a second copy of a moving number is how this board has been wrong
      in both directions before.
      🔑 **Why that bears on the ruling rather than merely being context:** the
      *split-board-is-the-fix* option is priced by how many boards still have to
      migrate, and that price has fallen a long way since the finding was
      written. The *patch-the-rule* option is priced by how many adopters will
      ever meet the clause monolithic — which includes every **future** repo,
      since a repo is most likely to be monolithic early (the timing trap above)
      and `create-repo` scaffolds the inlined clause on day one. So the two
      options are moving in opposite directions, and neither is a matter of
      re-reading the clause. Still the principal's call; this only says what the
      call now costs.

- [ ] 🔎 **The dirty-checkout claiming rule collapses on a monolithic board,
      and it deadlocked three child sessions at once.** Handed up by a child
      session; the clause **read here 2026-08-16** and the collapse confirmed
      from its own text.
      **The rule.** `CONCURRENCY.md`'s CF3 branches on **the item's file**. If
      the stranger's edits do not touch it: commit the claim alone. If the
      item's file itself is dirty: *"sync, take the next open item, touch
      nothing."*
      **Why it works on a split board and not otherwise.** Since the board
      store moved to one file per item, the next open item lives in a
      *different* file, which is clean — so the first branch applies and the
      claim lands normally. The clause is visibly written in that frame: its
      own parenthetical reasons about a dirty *index* being weaker evidence
      *on a split board*.
      **On a monolithic board there is one file.** The item you must not touch
      and the next open item you are told to take are the same bytes. The rule
      instructs a session to take an item inside a file it has just been
      forbidden to touch, so the honest reading is that no item can be
      claimed at all. **Three sessions in one child hit this simultaneously
      on 2026-08-16**, each having read the clause correctly.
      **This binds children, which is why it is filed here.** The split board
      is atelier's own store; several children still run a single roadmap
      file, and they inherit this doctrine through the pin. A clause that is
      correct for the parent's store and inert for the children's is the
      propagation shape this track exists to catch.
      **The candidate branch, and it is already half-written in the doc.** On
      a monolithic board the honest unit is the item's **line**, not its file
      — which is exactly what `CONCURRENCY.md` instructs two paragraphs
      later, when it says to put the claim marker on the checkbox line so a
      same-item collision always fires on one line. The dirty-tree test wants
      the same granularity the collision test already uses.
      **Not settled here.** Whether CF3 gains a monolithic branch, or whether
      the answer is that a monolithic board is simply unsupported for
      parallel claiming, is a doctrine call. The child is putting its local
      half to its own owner and has not edited its inlined floor.

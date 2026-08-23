- [~] 🔥 **The unseen duplicate number** (claimed 2026-08-23-1259, wt: board-dup-numbers-0823)
      — `board.py` cannot see a duplicate SECTION number, and rebuilt a clean
      index over one `[S][tools]` — found live 2026-08-17, not reasoned about.
      Two sessions independently minted section **`290`** within the same hour —
      `290-posture-…` and `290-ruling-round-…` — and **no git conflict fired**,
      because two new directories are not a shared line. `rebuild` then produced
      a perfectly well-formed index containing both, and the `board` floor check
      passed it. The index sorts them adjacently and reads as intentional.
      **Why the existing machinery cannot catch it.** The board's own
      coordination-free naming argument (`CONCURRENCY.md` § Integration hygiene)
      retired next-N counters for *records* precisely because two sessions
      allocating from stale views collide silently — but a board **section**
      number is still a next-N counter, allocated by reading the directory. It is
      the one surviving counter in a store built to abolish them.
      **The mechanical fix, and it is cheap:** `board.py` already enumerates the
      section directories to build the index; duplicate leading numbers are a
      one-line check on that same list, and the `board` gate is already enforced
      on every commit. That turns a silent collision into the trivial-conflict
      class the rest of the store lives in.
      🔑 **The tell that generalises:** the generator's verdict was *honest and
      carried no information about this class at all* — a **latent** guard in the
      sense already filed against this estate. Nothing asserted that section
      numbers are unique, so nothing could report that they were not.
      **This instance is repaired**, by the colliding party with the cheaper
      repair moving to `300` (`PRINCIPLES.md` §10's tie-break: fewest inbound
      references moves, and the other section carried two hand-authored
      cross-references including a rule-4 intent-record citation). The repair is
      not the fix; this item is.

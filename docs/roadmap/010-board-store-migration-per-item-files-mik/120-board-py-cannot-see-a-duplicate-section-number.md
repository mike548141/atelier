- [x] 🔥 **The unseen duplicate number — FIXED 2026-08-23** (wt: board-dup-numbers-0823)
      — `board.py` could not see a duplicate SECTION number, and rebuilt a clean
      index over one `[S][tools]` — found live 2026-08-17, not reasoned about.
      ✅ **What landed.** `number_collisions()` asserts uniqueness on the same
      enumeration the index is already built from, and its problems red `check`
      **and `rebuild` both** — papering over a collision with a well-formed
      index is precisely how the last one survived six days. The message names
      the colliding files, not just the number, because "10 is used twice"
      names nothing to fix.
      ⚖️ **The scope was WIDENED, and the reason is a finding rather than a
      preference.** This item asks for sections. Enumerating the board to check
      that premise turned up a **live duplicate one grain down**: `160/190` was
      two files — `190-review-md-gap-…` and `190-security-review-reads-…` —
      both rendered in the index, adjacent, reading as intentional, and
      unnoticed since 2026-08-17. Shipping the section half alone would have
      meant landing a check that ran clean over a real collision sitting in the
      same tree, which is this item's own complaint restated. Items are
      allocated by the same next-N read of the same directory, so the check is
      the same call with a different list. **The instance is repaired here**
      (the security-review pointer moved to `195`; neither file had an inbound
      reference, so the `PRINCIPLES.md` §10 tie-break was free).
      🧪 **Proven against the known-bad input** (`370/030`): the new tests fail
      **4 + 1 error** against the unfixed tool and pass on the fix. Two of them
      first passed for the *wrong reason* — a new file makes the index stale, so
      `check` reds whether or not the collision is seen — and were rewritten to
      rebuild first, which is the vacuous-test shape this estate keeps finding.
      Two more are negatives that must pass either way: the same number in two
      different sections is normal, and a section's `README.md` is not an item.
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

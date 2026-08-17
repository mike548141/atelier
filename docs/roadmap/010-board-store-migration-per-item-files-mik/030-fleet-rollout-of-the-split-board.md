- [ ] 🎯 **Fleet rollout of the split board** — nine children split on
      2026-08-17, two monolithic boards left; order and timing Mike's.
      atelier is the worked example (board-store ADR 2026-08-15) and its own
      split landed then. The rollout itself did not run from here: Mike sent
      one standing prompt to one session per repo, and each child cut its own
      board in its own session, which is what **PROPAGATION § The problem**
      already required. This item is therefore the fleet's *record*, not its
      plan — and it has been wrong in both directions before, so every figure
      below names what it counted.
      **Measured 2026-08-17 1057 UTC**, one pattern applied to every repo
      under the estate root: a `docs/roadmap/` directory ⇒ split; `wc -l
      docs/ROADMAP.md` at the split commit and at its parent for the two index
      figures. A peer atelier session re-ran the same count independently and
      agreed; `cbom` split *between* two reads twenty minutes apart in this
      session, so the state below is a timestamp, not a standing fact.

      | child | split commit | monolith → index | note |
      |---|---|---|---|
      | `faves` | `672ad17` | 6,274 → 268 | first child; proved the playbook |
      | `ros` | `98ec234` | 5,513 → 384 | regenerated `5cff027` on the fixed generator |
      | `shed` | `8755a62` | 3,465 → 136 | bumped its pin twice the same day |
      | `cbom` | `8d4975f` | 1,367 → 118 | **local `main` only — no remote** |
      | `kainga` | `c6e4479` | 323 → 103 | |
      | `tuhura` | `78e31b1` | 173 → 58 | |
      | `stewart-drive` | `a3c1c4a` | 98 → 66 | |
      | `derry-hill` | `4c67be9` | 74 → 69 | |
      | `rpi` | `4bd429c` | — → 69 | **born split** — no prior `ROADMAP.md` |

      **Still monolithic:** `docker-heap` 302 lines (tree not clean at the
      reading, last commit 2026-08-15) and `nova` 274 lines (clean, last
      commit 2026-08-09). `numen` 24 lines is **archived and never pushed**,
      so it is out of scope rather than outstanding. Per repo the work is
      unchanged: run the migration split, adopt the board floor check (already
      reaches every child via the registry — it passes as out-of-scope until
      the directory exists), and carry that repo's own conventions across.
      🚩 **Two readings the table does not make on its own.** `cbom` has no
      remote and no remote-tracking branch, so "pushed" is not a category
      there — its split exists on a local `main` and is *not* equivalent to
      the others for anything that depends on origin. And `rpi` never
      migrated: it had no `ROADMAP.md` before `4bd429c`, so its board was
      *written* in the store form from nothing. That is the stronger evidence
      for the form — it is adoptable without a monolith to convert, which no
      migration could have shown.
      ⚠️ *One figure is not a correction.* `faves`' index reads 268 lines at
      `672ad17` under the definition above; this item previously recorded 271
      under a definition it did not state. Three lines, and which point in
      that session was counted is the likely difference — so it is flagged,
      not overwritten as an error. The three figures this item *did* get wrong
      (5,213 / 3,125 / 1,853, all low, `faves` alone out by 4,421) were
      corrected 2026-08-17 and are named here because the failure mode
      recurs: a rollout record adjusted by intuition rather than swept.
      *What `faves` proved, so no later child rediscovers it:* the cut needs
      no judgement — an item is a column-0 checkbox plus its indented
      continuations, which is the grammar the monolith was already written in;
      verify losslessness as a **multiset over every non-heading source
      line**, not by eye; **the links are the real work** — every
      `ROADMAP.md` link is relative to `docs/` and breaks two directories
      down, and a repointer that tests only one side of `](` silently
      repointed 40 of 102 and reported success (`linkscan` caught it); and
      `tools/board.py` in a child is a **shim, not a copy** (ADR 0008) — and
      since the generator was fixed 2026-08-17 to resolve its rebuild
      instruction per root, not even a shim: `ros`, `shed` and `cbom` all
      carry none. The `.wrapscanignore` + `.pathscanignore` entries `faves`
      needed for the generated index are also **no longer required** — the
      same fix took the banner to 69 columns and stopped the index repeating
      section paths as link text, so `faves` deleted the pair it opened.
      *Gate note:* this item read "gated on this cycle's review closing" and
      `faves` shipped with the cycle still open on BS1 — so both of BS1's
      probed slips (a rebuilt-but-unstaged index passing the hook; a sibling
      session's dirty state line absorbed by `rebuild`) ride in nine children
      now, not one, and the two remaining boards inherit them until BS1 is
      ruled.
      *Handed up by children mid-rollout and open here:* `100` (`ros`' 38
      items using `[~]` for *partially delivered*, Mike's to rule) and `110`
      (a relative path argument scanned against cwd while `--root`'s rules
      apply — 🔥, four tools).

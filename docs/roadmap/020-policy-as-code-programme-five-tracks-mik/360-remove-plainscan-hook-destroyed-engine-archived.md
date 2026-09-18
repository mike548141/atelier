- [x] 🎯→✅ **Remove
      plainscan: the reply hook destroyed, the engine archived** — Mike's
      mid-session ask and ruling, 2026-09-18.
      Mike, verbatim: *"What is the impact of completly removing plainscan? I
      had so much trouble with it prior I ordered it be "unwired""* and *"I
      think as a guard its possibly more dangerous than it is beneficial"*.
      Impact measured before the ask: the reply hook was already unwired
      (machine settings carry no reference to it) with a Fable DESTROY verdict
      awaiting his ruling (`290/070`); the floor scanner is warn-only in every
      repo, no child promotes it, and it prints ~6,050 findings on every
      commit — noise that buries a genuinely new red.
      **Ruled via the question device**, in his own words over the offered
      options: *"Remove the hook and archive the engine in case we ever want
      the code again"*.
      Delivery: delete `tools/hooks/plain-reply.py`; take `plainscan` off the
      floor registry; remove the engine and its tests from the live tree,
      archived under the git tag `archive/plainscan-2026-09-18` (the last
      commit carrying both), named in `tools/README.md` so it can be found;
      rewrite the `COMMUNICATION.md` passage that says `plainscan` checks the
      committed prose plane. Settles `290/070` (destroy) and `020/310`.

      ✅ **DELIVERED 2026-09-18** (`1568228`, merged from
      `plainscan-removal-0918`): hook, engine and tests deleted; registry
      entry, mixed-root list and a stale `pathscan` comment removed;
      `tools/README.md` names the archive tag. Tag
      `archive/plainscan-2026-09-18` → `3a6ae81`, pushed. Four links in two
      review records now point at deleted files and carry scoped
      `linkscan:allow:missing-file` markers naming this ruling — annotation,
      not a rewrite of the records. `COMMUNICATION.md`'s passage now says the
      scanner was removed and why (*checkable is not worth a guard*). Review
      rides `160/310`, widened in the same commit. Settles `290/070` and
      `020/310`; `120/010` is moot (its flaky tests were the hook's own).

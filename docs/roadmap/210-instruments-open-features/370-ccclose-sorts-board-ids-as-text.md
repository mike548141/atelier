- [x] 🔎 **`ccclose --identifiers` lists board items in text order, so
      `160/1000` prints before `160/986`.** Found 2026-11-03 on queue run
      deeac927's own close, the first close to cite a four-digit pointer.
      The same class `010/200` fixed in `board.py`: the board lists sort
      their ids as strings. Display only, nothing is lost or miscounted.
      **Shape:** sort each list with numeric collation, so every digit run
      compares as a number.
      **DONE 2026-11-03** (queue run deeac927): `instruments/ccclose` sorts
      the board lists with `boardOrder`, numeric collation, pinned in
      `instruments/ccclose.test.js`. Cold pass queued as `160/1020`.

- [x] 🔎 **A four-digit item number sorts out of order, and the review
      section has one three-digit number left.** Found 2026-11-03 by queue
      run deeac927 while numbering a cold-pass pointer. Section `160` holds
      pointers up to `999`; the only free numbers below it are `986` (taken
      by this run) and `987`. `tools/board.py` orders items and sections by
      sorting their file names as text, so a `1000-…` item would sort before
      `130-…` and land near the top of the section in the index. Nothing
      breaks yet, because no item is numbered past `999` in this repo. The
      next session that queues a pointer will hit it. **Shape:** sort by the
      leading number first, then the name, for both sections and items;
      no existing index changes, because every current number has the same
      width within its directory.
      **DONE 2026-11-03** (queue run deeac927): `tools/board.py` sorts by
      `board_order`, the leading number then the name, on both planes, and
      `tools/test_board.py` pins it. This repo's index rebuilt byte for byte
      the same. Cold pass queued with this landing as `160/987`.

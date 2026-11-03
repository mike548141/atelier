- [~] (claimed 2026-11-03-1130, wt: atelier-qr-deea-ccapple)
      🔎 **`ccapple` looks for the store before it checks that a filter was
      given, so a no-filter run on a Mac without that store exits 1, not 2.**
      Found 2026-11-01 while writing the process-level tests. For `messages`,
      `calendar`, `notes`, `photos` and `home`, the command resolves the one
      store file first (`_one`) and only then does the search function reject an
      empty filter set; `contacts` and `reminders` check the filter first. The
      "search, never dump" gate still holds, since nothing is read either way,
      but the exit status is the wrong one for a caller that branches on it
      (1 = "store unreadable", 2 = "bad invocation"), and the message names a
      missing store when the real fault is the missing filter. **The likely
      fix:** validate the filter set in `main()` before any store is resolved,
      sharing the check the search functions already carry, with a test that
      runs the script under an empty `HOME`. Left as built in the first
      version of the instrument; the fix is its own change.

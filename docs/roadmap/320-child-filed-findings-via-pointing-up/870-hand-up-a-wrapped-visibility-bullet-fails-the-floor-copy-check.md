- [~] 🔎 **Hand-up: under the new visibility slot (`320/370`), a child whose
      visibility fact wraps before "Verify:" fails the floor-copy check as
      unfilled.** Handed up 2026-11-16 UTC by a private child's live session,
      by cross-session message to queue run 78ca9153, class only. The
      canonical bullet put both slots on one line,
      `<visibility fact>. Verify: <visibility check>.`, and `pins.py`'s
      `fill_placeholders` matches a line's literal text exactly, so a child that
      breaks the line at the space before "Verify:" (the natural break for a
      long fact) fills neither slot and reds as drift. Joining it onto one line
      passes, but runs past 85 columns, and got through only because the floor
      region is not wrap-scanned in that child. Reproduced here the same hour:
      a wrap inside the fact or inside the check fills; a wrap before
      "Verify:" does not. The child reported several others with multi-line
      visibility bullets, so they would fail at their next bump.
      **Owed:** put "Verify: <visibility check>." on its own line in the
      canonical floor, so a long fact wraps inside its own slot; a test for the
      wrapped case.
      🔒 CLAIMED 2026-11-16 (wt: none) by queue-run session 78ca9153 (Opus 5.5,
      principal-opened).

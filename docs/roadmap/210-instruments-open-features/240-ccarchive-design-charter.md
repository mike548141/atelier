- [ ] 🔎 **ccarchive's design charter, in Mike's words, checked against the
      tool** (Mike, 2026-10-05, mid-run)

      *"Following my earlier thinking, * We sign the data in the archive for
      integrity * We encrypt the archive data for confidentially, especially
      since all sorts of things can end up in the transcripts content *
      Compressed to save storage * Writes limited to reduce IO work where it is
      sensible to do so * Storage types handled like iCloud that may take data
      off the device and leave a file stub * We write a manifest so its easy to
      manage and consume from the archive * We do it all in a way that makes it
      efficient and effective to use the archive with other tools like ccrepo
      and cctranscript"*.

      **Checked against the tool after `210/210` (merge `8540a1d`):**
      - ✅ **Signed.** HMAC-signed manifest, checked before any write.
      - ⏳ **Encrypted.** Not built. The crypto source is answered (C′,
        `210/030`), and the build waits on the `⏳ 160/670` review, by Mike's
        choice. His reason here, that anything can end up in a transcript, is
        the case for doing it next.
      - ✅ **Compressed.** gzip per file.
      - ⚠️ **Writes limited.** Only changed files are written. But a growing
        transcript is re-compressed and rewritten whole on every change, not
        appended. Not yet weighed: appending a gzip member would write only the
        new bytes, but it cuts across atomic replace and the planned
        encryption.
      - ✅ **Offloading storage.** Offloaded mirrors are never read on a run.
        They are renamed rather than opened, and reported as "not checked".
      - ✅ **Manifest.** It now also carries each mirror's size and time, so a
        run trusts a mirror from a stat alone.
      - ✅ **Sibling tools.** ccrepo and cctranscript skip `_untrusted/`,
        `_anomalies/` and `_versions/`. cctranscript's skip of the last two
        landed with this item's filing. Its archive pool still gunzips every
        mirror for one column (`210/180`).

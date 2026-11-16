- [x] 🔎 **Hand-up: a child's own visibility fact sits inside its verbatim floor copy, so when the fact changes the child cannot keep it true** `[S][doctrine]`. Handed up by a child's session on 2026-10-17, for atelier to consider. A suspicion of a wrong rule, with one measured instance; no fix proposed. <!-- wrapscan:allow: a state line carries the whole state in one line so the index reads true -->

      **What was measured.** The floor's visibility bullet is copied into each
      child's onramp verbatim, and the 2026-09-19 *floor copy verbatim* ruling
      forbids a child narrowing or editing that copy. But the bullet carries a
      per-repo fact: whether the repo is private, public, or private now with
      intent to publish later. In one child that fact changed when its tool
      half moved to a separate public repo: the stamped line still says
      "private now, with intent to publish the *tool* later", which is no
      longer true of that child (it is private for good). The child can only
      add a local bullet below the stamp explaining how to read the stale line,
      so the floor copy, the one part every session is told binds, is the part
      that reads wrong.

      **The question for atelier:** should a per-repo fact live inside a
      verbatim floor copy at all, or be a slot the child fills (the floor text
      saying only "state this repo's visibility here, and how to verify it")?

      **Smaller, same family:** `310`'s README and item `310/040` name a child
      by the repository name it had before a rename; that child's sessions now
      open under its new name.
      🔎 **Verified at HEAD 2026-10-16** (1501 UTC queue run, a read-only
      Sonnet worker): ⚠️ partly. The visibility fact already is a slot,
      `<visibility fact>` (`PROPAGATION.md:78,198`), which a child fills and
      may re-fill; `320/360` records exactly that. The real residue: stampscan
      has no placeholder handling (a filled `<SHA>` reds), and nothing says
      a fill is re-editable. The 310 rename remark holds. Overlaps `320/370`.
      ✅ **Resolved 2026-11-16 — the house's choice, not the principal's**
      (queue run 78ca, with `320/370`). **Taken:** both per-repo facts in the
      visibility bullet are slots (`<visibility fact>`, and now
      `<visibility check>` for the verify), and `PROPAGATION.md` says a child
      re-fills either in place when its fact changes. `tools/pins.py` reads
      each fill out of the copy, so a re-fill is not drift (a test covers
      it); the stampscan residue noted above is that tool's job, since
      stampscan cannot resolve a child's source. **Not taken:** moving the
      visibility bullet out of the floor, which would drop a safety statement
      from the one text that binds where nothing else is read. **The 310
      rename remark** is already carried by `310/040`'s 🚩 note; the 310
      README names the old checkout only inside the principal's quoted
      words, which stay as he said them.
      🔒 CLAIMED 2026-11-16T12:07Z (claimed 2026-11-16-1207, wt: qr-78ca-floorb) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).

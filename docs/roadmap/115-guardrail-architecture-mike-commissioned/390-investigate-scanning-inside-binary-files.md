- [x] 🤔 **Investigate scanning inside binary files.** No guard reads a
      binary's contents beyond image metadata: not pixels, not the insides of
      other formats, and `secretscan` reads no binary at all. So an exemption
      over a binary can only cover the whole file, and a secret or personal
      detail inside one is unseen. Filed 2026-11-09 by queue run 722ac2e2 on
      Mike's answer to the exception-register redraft's Q4 (*"Separate
      investigation"*, an answer to options offered), kept out of that design
      (`160/650`). Scope: which binary kinds the estate actually tracks, what
      each could hide, and what reading them would cost; ranked by value like
      any other work (`020/240`).
      🔒 CLAIMED 2026-11-16T11:55Z (claimed 2026-11-16-1155, wt: qr-78ca-binary) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      📝 **INVESTIGATED 2026-11-16** by a worker of queue run 78ca: the census and
      ranking are in
      [`2026-11-16-1206-binary-kinds-investigation.md`](../../method/census/2026-11-16-1206-binary-kinds-investigation.md).
      Estate-wide the siblings track 633 binary files (204.7 MB) and atelier
      none; images are two thirds of them and the only kind any guard reads.
      🎯 **Recommendation, awaiting the principal's ruling:** build the Office
      (OOXML, zip plus XML) read first, then the PDF metadata slice, as one
      small stdlib reader under `leakscan`'s G3 gate (39 files, text and
      author fields no guard sees today); archive descent and a printable-string
      pass follow; OCR is out under the zero-dependency rule. Accepting the gap
      is the stated alternative.
      💬 2026-11-16 UTC, the principal's answer to options offered (an answer,
      not a ruling), told that all 37 tracked Office/PDF files sit in 3 private
      repos and the orchestrator recommended holding behind a pre-flip gate
      line: *"Build the reader"*. The option read: a ~300–450 line
      standard-library reader for Office then PDF metadata under leakscan's
      binary-file check, plus one Fable cold review.
      🔒 CLAIMED 2026-11-16T19:25Z (claimed 2026-11-16-1925, wt: qr-78ca-docreader) by
      queue-run session 78ca9153 (Opus 5.5, principal-opened).
      ✅ **BUILT 2026-11-16** by a worker of queue run 78ca: the Office (OOXML)
      then PDF metadata reader, inside `leakscan`'s G3 gate (`tools/leakscan.py`,
      the "G3 documents" block; `tools/README.md` § *Binary files (G3)*). New
      sets `office-props` (creator, lastModifiedBy, Company, Manager),
      `office-custom`, `office-comments` and `pdf-info` (Author and non-standard
      keys), plus a PDF's XMP as the existing `xmp` set; every value read goes
      through the ordinary rules and term list. Standard library only, every
      read capped (zip directory, member count, declared size, per-part
      inflation, PDF windows and inflation budget), expat with DOCTYPE and
      entities refused, and a bounded-memory regression test in the `020/380`
      shape. **Rollout:** everything the reader adds warns until
      `DOCUMENT_UNTIL` = **2027-01-18** (UTC) and blocks from it; the file
      gate's own dates are unchanged. Estate probe (this worktree's leakscan,
      read-only, over 29 sibling repos): 0 change to any repo's blocking
      findings or exit code; 53 new warnings in 3 repos, by class 41
      `binary-metadata` (office-props 12, office-custom 9, pdf-info 6, xmp 14)
      and 12 text-rule hits (ipv4 5, local-term 5, nz-phone 2). The 5 ipv4 hits
      are a browser user-agent version (`Chrome/x.0.0.0`) in a PDF `Creator`,
      the rule's noise rather than the reader's; PDF dates were dropped from
      the text scan after they produced 7 card-checksum false positives.
      *review: Fable cold pass to be queued by the orchestrator.*

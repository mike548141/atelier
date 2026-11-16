- [ ] 🤔 **Investigate scanning inside binary files.** No guard reads a
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

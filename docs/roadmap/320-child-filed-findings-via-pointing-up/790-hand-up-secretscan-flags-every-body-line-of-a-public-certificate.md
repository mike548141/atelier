- [x] (claimed 2026-11-06-0527, wt: atelier-qr-722a-secretscan)
      🔎 **Hand-up: `secretscan` flags every body line of a PEM public
      certificate, so a child that must commit one is pushed to a path-level
      exemption that blinds the scanner to the whole file** `[tool]`.
      Handed up from a private child on 2026-11-03 under `PROPAGATION.md`
      § *Pointing up*, found by a queue-run worker (Opus 5.5, no reviewer)
      and reproduced before filing with this repo's `tools/secretscan.py`
      at `8220032`. Stated class-only. Consideration and remediation are
      atelier's; the filer stops here.
      **The gap.** `PUBLIC_KEY_RX` (`tools/secretscan.py`, the public-key
      suppression) is per line: it exempts the `-----BEGIN CERTIFICATE-----`
      line and nothing below it. A PEM body is base64 lines with no keyword,
      so each one trips the entropy net. Reproduced: a fresh 14-line
      self-signed P-256 certificate, staged alone in a scratch repo, gives
      `secretscan: 8 finding(s) — commit blocked`, all `[medium/entropy]`
      on body lines. An inline allow-marker cannot be added, because a
      comment inside a PEM block breaks the decode the consumer relies on.
      **What it costs a child.** The only route left is a `.secretscanignore`
      path entry, which exempts the whole file from every rule, so a private
      key pasted into that file later passes the scanner unseen. The child
      that hit this added its own check that the exempted folder holds
      certificates only; every child that pins a certificate would need to
      repeat that.
      **A possible shape, for atelier to judge:** suppress entropy across a
      `BEGIN CERTIFICATE` … `END CERTIFICATE` block (and the `PUBLIC KEY`
      block), counted like the existing public-key spans, and never across a
      `PRIVATE KEY` block; optionally confirm the block decodes as X.509.
      ✅ **DONE 2026-11-06:** `tools/secretscan.py` treats a
      `CERTIFICATE` or `PUBLIC KEY` PEM block as a unit and exempts its body
      from the entropy rule only, counted in the existing `by public-key
      line` field. Fail-closed: exact public labels only; the matching END
      within 2048 body lines; every body line pure base64 of at most 76
      characters on consecutive lines; the decoded body one DER SEQUENCE
      whose first element is a SEQUENCE (a certificate's and a public key's
      shape, absent from every private-key form); one stray line voids the
      whole block; each certificate in a chain stands alone. `--staged`
      judges added body lines against the index copy of the file.
      `tools/test_secretscan.py` (`PublicPemBody*`) pins each condition; its
      private-key fixtures are synthetic DER, no real key material. The
      repro certificate now scans clean and its private key still blocks.
      Cold pass queued as `160/1030`.

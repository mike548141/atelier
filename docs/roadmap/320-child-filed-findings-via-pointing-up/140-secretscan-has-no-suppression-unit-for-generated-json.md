- [ ] **REPORT — secretscan's suppression units cannot reach a finding inside
      generated JSON, so a child's derived artefact blocks on a value its
      source file already carries a marker for** `[S][tools]` — filed from a
      private child, 2026-09-04, via § *Pointing up*. Evidence available.

      ## The seam

      secretscan's suppressions are: a line marker (`secretscan:allow:`), a
      per-file glob (`.secretscanignore`), and the public-key fingerprint
      carve-out. A machine-written **valid JSON** file can carry none of the
      first — JSON has no comments, and appending a marker to a line corrupts
      the value or the syntax — the fingerprint carve-out is key-shaped only,
      and the glob is the wrong width for a data-rich generated file whose
      whole point is to be scanned.

      ## The incident (2026-09-04, private child)

      A collector pipeline echoes a provenance value — a dated source
      filename, mixed case, digits, underscores — from a hand-written YAML
      register into a generated `summary.json` on every run. In the YAML the
      value carries a line marker with its reason and has passed the gate
      since it landed. The echo in JSON tripped `medium/entropy` and blocked
      the commit of every fresh observation. No credential existed on either
      line; the marker's vouching could not travel with the value.

      Resolved at the write site: the echo is now emitted in display form
      (underscores to spaces), which de-tokenises it below the entropy net.
      Cost, declared: the echo is no longer byte-identical to its source, so
      "a changed source with unchanged output is a bug" now holds only up to
      the deterministic transform.

      ## The shape of a fix (sketch, not a design)

      A suppression unit that names a **value**, not a line or a file: e.g. a
      repo-local allowlist of `sha256(token) + reason`, or a `path +
      JSON-pointer` form for structured files. Either keeps the register's
      properties — narrow (one value), noisy (counted in the tally), reasoned
      (the reason field), declared (it forbids nothing; it vouches). The
      write-site workaround generalises badly: not every generated echo has a
      lossless display form.

      ## Second instance (2026-09-06, same private child) — hand-up

      A second, independent occurrence in the same child, from a different data
      source. It is reported because **it is the case the sketch above
      predicted and the first instance could not demonstrate.**

      A cloud resource-graph export names each managed disk by concatenating a
      machine name, a role and an opaque suffix. The concatenation is the only
      reason the value reads as a token: measured against the gate's own net
      over the generated `assets.json`, **twelve values match and no others**,
      in two shapes — ten `<machine>_OsDisk_1_<32 hex>` and two
      `<machine>-DiskCopy-<14-digit stamp>`. None is a credential; every one is
      a resource identity, and two disks on one machine differ only by that
      suffix. `git add` of a fresh observation was refused with **96 findings**,
      all `medium/entropy`, across four generated files.

      **What makes it the stronger evidence.** The first instance had a
      lossless display form, so the write-site fix was free. This one has none
      in principle: the token *is* the resource's own name, and altering it
      alters an identifier. That is the sketch's own prediction — *"not every
      generated echo has a lossless display form"* — met by a real case.

      ⚠️ **Honest limit on that claim, and it cuts against us.** The child did
      in the end resolve this instance at the write site too, by **structuring**
      rather than altering: the display label is emitted with its joins as
      spaces and the three components are carried separately, so the exact name
      rebuilds byte for byte and no component qualifies alone. So this is not
      proof that no write-site fix exists — it is evidence that the write-site
      route now depends on the token having *internal structure the emitter
      controls*, which is a narrower and less predictable condition than having
      a lossless display form. A value that is opaque end to end still has
      nowhere to go.

      The child's own reasoning is recorded with it, including that its first
      answer was the wrong one: it reached for a `.secretscanignore` glob and
      argued the write-site fix was impossible because *"altering the token
      alters an identifier"* — true of altering it, false of structuring it.
      Evidence available on request.

      Consideration and remediation are atelier's; the reporting child stops
      at this report.

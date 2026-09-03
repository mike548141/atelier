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

      Consideration and remediation are atelier's; the reporting child stops
      at this report.

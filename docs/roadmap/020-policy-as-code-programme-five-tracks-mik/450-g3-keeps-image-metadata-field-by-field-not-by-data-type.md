- [ ] **G3 keeps image metadata field by field, not by data type.** Mike,
      2026-10-19, correcting how `020/440` read his word "fields": *"I did
      mean fields as in GPS versus the camera model. Things like exif, iptc,
      xmp are data types, nto fields. Put it on the board to do in a future
      session"*. His rule, from `020/440`: *"I am fine with one reason
      applying to multiple fields of metadata, but it should be specific
      e.g. fields A, B, and C allowed because of X"*.
      **What exists now.** leakscan's G3 gate (`020/150`, `020/440`) sorts
      PNG, JPEG and WebP metadata into data types (`exif`, `iptc`, `xmp`,
      `icc`, `png-text`, `jpeg-comment`, `unknown`). An entry keeps a whole
      type under a reason. Exif, IPTC and ICC contents are detected by
      presence and never read, so a reason that keeps `exif` for the camera
      model also keeps the GPS block beside it.
      **Owed.**
      - Read the fields inside each type: Exif and GPS IFD tags, IPTC
        datasets, XMP properties, PNG text keywords. Use stdlib only, with
        bounded reads, as the walker does now.
      - An entry names the fields it keeps (`exif:Model,LensModel`, say)
        under one specific reason, and any field present and not named
        blocks, naming it.
      - Decide how fields are named (tag names or numbers), what a field the
        parser cannot decode counts as (blocks, as `unknown` does now), and
        whether a few groups need a shorthand. GPS is the obvious one, but
        any shorthand must still name what it covers.
      - Update `--binary-entries` to print per-field lines, and update the
        tests, README and CHANGELOG.
      **Timing.** The G3 grace ends 2026-11-18 (`010/190`). If this lands
      after children have listed their binaries by type, their type-level
      lines need a migration path. Weigh landing before the cut-off, or
      accepting type-level lines with a warning for one more grace.

- [x] (done 2026-11-03: Exif and GPS in part 1, IPTC, XMP and PNG text in part 2; the G3 field-level reader is complete) **G3 keeps image metadata field by field, not by data type.** Mike,
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

      **Part 1 landed 2026-11-03: Exif and GPS fields.** Remaining: IPTC,
      XMP and PNG text, so the item stays open.
      - *Decisions.* Fields are named by the TAG NAMES of the Exif / TIFF /
        GPS specifications, in the manifest as `exif:Make` and `gps:GPSLatitude`
        (a bare name after a `set:Field` continues that set, so
        `exif:Make,Model` is the item's `exif:Model,LensModel` form). A tag
        the table does not name is written by number, `exif:0x9999`. An
        undecodable Exif block is the field `exif:unknown`, which blocks
        until named, as `unknown` does at the type level. No wildcard and no
        shorthand: `gps` alone is refused because it would keep every GPS
        tag under a reason that names none of them, and a 4-tag line is
        cheap to write. A set and its own fields cannot both be named.
        MakerNote is one field, with the cost stated in the README.
      - *Reader.* Tag numbers only (never values), walking IFD0, the Exif,
        GPS and Interoperability IFDs and IFD1 within the 1 MiB segment cap,
        at most 16 IFDs and 1,024 entries each; PNG eXIf, JPEG APP1, WebP
        EXIF and ImageMagick raw exif profiles are read alike.
      - *Migration.* Type-level `exif` lines stay accepted, with a warning
        naming the fields the file carries, until `TYPE_LEVEL_UNTIL`
        (2026-12-18, a month after the G3 grace ends 2026-11-18); then the
        set blocks until fields are named. `--binary-entries` lists the field
        lines that replace a type-level line. Other sets are unaffected.
      - *Not done.* IPTC datasets, XMP properties, PNG text keywords, and the
        type-level cut-off for those sets (they have none yet). Done in part 2
        below.

      **Part 2 landed 2026-11-03: IPTC, XMP and PNG text. The item is done.**
      - *Decisions.* Same design as part 1, same helpers. IPTC fields are the
        IIM dataset names (`iptc:By-line`), `iptc:<record>:<number>` for one
        the table lacks, `iptc:8BIM-0x03ED` for another Photoshop resource in
        the APP13. XMP fields are `xmp:<prefix:property>`, the top-level
        properties of the packet's `rdf:Description` (attribute or element
        form), written in full each time because a prefix can equal a set's
        name; a property's value, structure included, is one field. PNG text
        fields are the chunk keyword with `%XX` for bytes outside
        `A-Za-z0-9_.-`, so each is one manifest token. `<set>:unknown` is what
        cannot be read, and blocks until named. Names only, never values.
      - *Reader.* IPTC by lengths, XMP by stdlib expat as a start-tag stream
        with no DOCTYPE or entity accepted, both inside the 1 MiB segment cap,
        with caps on datasets, resources and properties; JPEG extended XMP is
        joined first.
      - *Migration.* The same `TYPE_LEVEL_UNTIL` (2026-12-18) now covers
        `iptc`, `xmp` and `png-text`: type-level lines warn, naming the
        fields, until then. `icc` and `jpeg-comment` have no fields to name.
      - *Left over.* A JPEG comment is one text field with no name, and an ICC
        profile is read by presence; neither is a data type holding fields, so
        both stay by set. The type-level warning path is deleted after
        2026-12-18 (a later cleanup, not owed here).

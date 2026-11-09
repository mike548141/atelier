- [ ] **Hand-up from a private child: leakscan's `nz-phone` rule fires on
      bracketed hex-byte strings.** Filed 2026-11-09 by a child session, as a
      finding only; the fix is the house's.

      **The shape.** macOS `ioreg` dumps print a device property's raw bytes
      between angle brackets. A little-endian small integer is eight hex digits
      with a leading zero and a tail of zeros, all of them decimal digits, so
      the run inside the brackets matches `nz-phone`. (This item describes the
      shape rather than quoting one, because a quoted one is refused by the
      rule it reports.) The child measured 64 such hits across three captured
      fixtures, each now carrying a per-line allow marker that exists only to
      answer this rule.

      **Why the existing guard misses it.** `_phone_inside_hex_digest` skips a
      separator-free digit run only when the unbroken run of hex characters
      around it is 16 or more long, for digests. These runs are 8 to 16 hex
      characters, so they fall under that floor.

      **A possible rule, the house's to judge.** A digit match wholly inside
      `<` and `>`, where the bracketed text is an even-length run of hex
      digits and nothing else, is a bounded byte field and not a phone number.
      A bracketed phone with a separator, or a `<+64 …>`-style contact, keeps
      full reach. A test wants both directions: the byte field passes and a
      bracketed real-shaped number is still caught.

      **Done means** the rule no longer matches that shape, with tests in
      both directions. The child then removes its 64 markers on a later pin.

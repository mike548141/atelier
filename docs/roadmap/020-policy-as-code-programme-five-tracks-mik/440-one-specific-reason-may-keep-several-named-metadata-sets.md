- [x] **DONE 2026-10-18** (wt: atelier-qr-020-440)
      **G3: one specific reason may keep several named metadata sets.**
      `020/150` landed with one metadata set per manifest line, and refused
      a reason one set line shared with another. Mike, 2026-10-19, on that
      design: *"I am fine with one reason applying to multiple fields of
      metadata, but it should be specific e.g. fields A, B, and C allowed
      because of X"*. Read as: a line may name several metadata sets
      (`<digest>:icc,xmp  <path>`) under one reason, so long as each set is
      named explicitly. No wildcard. A set not named still blocks, and the
      metadata reason still may not just repeat the file's own reason.
      "Fields" is read at the granularity the scanner can see, its named
      sets (`exif`, `iptc`, `xmp`, `icc`, `png-text`, `jpeg-comment`,
      `unknown`). Individual Exif tags are not read, so a tag-level rule
      would be a separate, larger build.
      ✅ **Built 2026-10-19, `34dc0f0`.** A set line may name several sets
      under one reason (`<digest>:icc,exif  path  # why`). Each set is named
      once, from the known list, with no wildcard. Any set present and not
      named still blocks, by name. A set line that repeats the file line's
      own reason is still refused, as the blanket form. Two set lines may
      now share a reason. Existing one-set-per-line manifests load
      unchanged. 219 leakscan and 2,032 Python tests green. Reviewed under
      `160/980`, widened to this commit.

- [ ] 🔎 **leakscan's `ipv4` rule reads a browser version string
      (`Chrome/x.0.0.0`) as an address.** Found 2026-11-16 UTC by the
      `115/390` reader's estate probe: 5 of the 53 new warnings it added were
      a PDF's Creator field carrying a browser user-agent version. They warn
      until 2027-01-18 (`DOCUMENT_UNTIL`) and block after it unless the rule
      or the files change. **Owed:** decide whether `ipv4` should skip a
      dotted quad preceded by a product token and slash (`Name/a.b.c.d`), the
      user-agent shape, and test it against the estate before 2027-01-18.

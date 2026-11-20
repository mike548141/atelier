- [x] 🔎 **leakscan's `ipv4` rule reads a browser version string
      (`Chrome/x.0.0.0`) as an address.** Found 2026-11-16 UTC by the
      `115/390` reader's estate probe: 5 of the 53 new warnings it added were
      a PDF's Creator field carrying a browser user-agent version. They warn
      until 2027-01-18 (`DOCUMENT_UNTIL`) and block after it unless the rule
      or the files change. **Owed:** decide whether `ipv4` should skip a
      dotted quad preceded by a product token and slash (`Name/a.b.c.d`), the
      user-agent shape, and test it against the estate before 2027-01-18.
      🔒 CLAIMED 2026-11-20T07:40Z (claimed 2026-11-20-0740, wt: atelier-qr-08cd-graces) by queue-run
      session 08cd3b95 (Opus 5.5, principal-opened). Scope: the ipv4 user-agent shape, tested on the estate.
      ✅ **Done 2026-11-20 UTC (queue run 08cd, worker):** `ipv4` skips a dotted
      quad directly after ONE capitalised alphanumeric token and a slash, that
      starts its word and ends the token (`Chrome/120.0.0.0`, `Version/…`),
      in `_ipv4_is_ua_version` beside `_ipv4_is_safe`. A URL
      (`http://addr/`), `key=value`, a bare address, a lowercase directory
      (`src/addr`, `logs/addr.txt`), `a/Chrome/addr`, `Server/addr.txt`,
      `Server/addr/path` and a five-part number all still report; tests both
      ways in `IPv4UserAgentVersion`. Accepted cost, pinned by a test: a
      capitalised word, a slash and an address followed by a space in prose
      reads as a version. Estate probe (every sibling repo, one snapshot):
      14 findings removed, 0 of them an address: 2 in text, 7 four-part
      clause numbers after a capitalised folder in an archive manifest, and the
      5 PDF Info `Chrome/…` Creator versions the `115/390` probe found. The
      scan before and after the change otherwise matches.

- [ ] 🎯 **The exception audit above checked reason-presence and
      effectiveness — never narrowness. Mike commissioned, 2026-09-12.** His
      words: *"I am concerned that guards like secretscan and leakscan have
      exceptions granted in various repos that are too broad... To clarify I
      mean just the specific characters in a text file, not the file, not
      the line/row. Same for non-text files."* He also restated the standing
      rule this isn't relitigating: a secret you find and can't be bothered
      rotating is never a legitimate exception — this item is only about
      exceptions that are otherwise legitimate but scoped wider than they
      need to be.
  - [ ] 📎 **Checked against this repo's own files first, per the reporting
        duty.** The 2026-08-09 audit above swept ~120 line markers and 11
        ignore-file globs estate-wide and found every one reasoned — then
        corrected itself before close: *"an exception review that reads the
        reasons has checked rule (c) and nothing else. Whether an allowance
        actually suppresses is a separate question."* Neither pass asked
        the question Mike is asking now: **is the granted scope the
        narrowest one available**, as `GUARDS.md` § *Granularity* itself
        already requires ("use the narrowest level that covers the case, and
        the narrowest scope within that level"). Nobody has swept for that.
  - [ ] 🔑 **For text, the narrowest level the tooling has IS the line —
        there is no finer rung.** `GUARDS.md`'s own granularity table stops
        at Line ("one line, in the file it concerns"), optionally rule-scoped
        (`secretscan.py`/`leakscan.py` line ~99/65: a bare marker exempts
        every rule on the line, `:allow:<rule>:` exempts one). Mike's ask —
        "just the specific characters" — is a rung this table does not name
        at all. Concretely: a line carrying one real secret plus other
        legitimate content, or **two distinct matches of the same rule on one
        line** (one real, one a false positive), has no way today to exempt
        only the offending span — the choice is exempt the whole line
        (over-broad, the other match on the line goes unguarded silently) or
        rewrite the line (not always possible — see C5's unrewordable
        ordinary-English/quotation cases, `020/030`).
  - [ ] 🔥 **For non-text files, there is no exception to narrow, because
        there is no coverage to narrow it from.** Read directly:
        `tools/secretscan.py` `scan_paths` and `tools/leakscan.py`
        `scan_paths` both call `_looks_binary(data)` and `continue` —
        binary file **contents** are never scanned by either guard, full
        stop. (`leakscan.py` scans a binary's **path/name** via
        `scan_path_name` — G2 — but never its bytes; `secretscan.py` skips
        the file entirely.) So a credential embedded in a binary (a keystore,
        a compiled asset, image metadata, a PDF) passes both guards with no
        finding, no marker, no record, and no reason — which is a wider and
        less visible gap than any over-broad *declared* exception, because
        nothing declares it. This is worse than what Mike described, not
        milder: he assumed an exception exists and asked whether it's scoped
        too wide; for binaries the honest answer is there's no exception
        because there's no guard.
  - [ ] 🤔 **Not scoped to a mechanism.** For text, a character-span/offset
        marker is the shape that would answer this (e.g. a scanner-readable
        redaction annotation naming a column range, or a companion sidecar
        the size of a diff hunk) — real cost, since `scan_text`'s finding
        model and every marker parser would need a span concept added, not
        just a new marker string. For binaries, the prior question is
        whether either guard should attempt content detection at all (entropy
        scanning binary bytes is a different false-positive profile
        entirely) — that is a bigger, separate design question this item
        does not answer, only surfaces.
  - [ ] 📎 Filed beside the 2026-08-09 audit rather than as a fresh audit,
        because the finding is precisely that audit's own blind spot named
        by its closing self-correction — a second question the first sweep
        didn't know to ask, not a new sweep of different ground.

- [~] (claimed 2026-10-03-0416, wt: qr-exceptions; parts 2–3: the exception record and its migration) 🎯 **The exception audit above checked reason-presence and
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
  - [ ] 🔥 **RESTATED and widened by Mike, 2026-10-03. He says he has had to
        repeat it "many many times", so it is now a build, not a question.**
        Verbatim:
        > I want to be clear that I am seeing too larger gaps in the
        > exceptions used for things like leakscan, secretscan and the other
        > guards. I've said many many times (I've had to repeat myself to you
        > alot on this) that I want any exception to be
        > * Specified and recorded so that its clear that the exception
        > exists, why it is necessary, who created it (e.g. session transcript
        > ID, did I rule or did you do it automatically etc), when the
        > exception was granted, and any other relevant and useful info
        > * As narrow an exception as possible. I gave the example of a
        > particular position in the file or string of characters rather than
        > a whole line in a file, or the whole file, or a folder of files.
        > For example if every line in a file is secrets then an exception for
        > the file makes sense, but if it were one string in the file then
        > only that string should be excluded.
        > This should be true of binaries, files large and small etc
        >
        > And the guards need to work efficently and effecitvely. For example
        > we have had situations were the guards ran for hours and took GBs of
        > memory that stalled the laptop and had to be killed. It should not
        > try and load a whole file or all results into memory, it needs to
        > continually close work as it opens new work so it can deal with big
        > repos (GB or number of files), big files etc
        **Three requirements:**
        - (1) every exception RECORDS why, who (session transcript ID, and
          whether he ruled it or an agent added it), when, and other useful
          detail;
        - (2) every exception is as NARROW as possible, down to a character
          span, for text and binaries alike;
        - (3) every guard STREAMS, so a large repo or file never exhausts
          memory or time.
        **Plan, in landable parts:**
        - Part 1, now: an audit of every exception mechanism against (1) and
          (2), and an estate-scale time and memory measurement of every
          guard against (3). Both are read-only.
        - Part 2: one exception record format, shared through
          `allowmarker.py`, with span-level scope.
        - Part 3: migrate the guards and existing exceptions to it.
        - Part 4: fix whatever part 1 measures as unbounded.
        G3 (PR #97) is held until it meets (1) and (2).
  - [x] 📊 **PART 1 DONE 2026-10-03: what the guards accept at `1685fd8`, measured
        against requirements (1) and (2)** (read-only, atelier's tree at
        `1685fd8`). **26 exception mechanisms.** Only one, the floor
        `advisory`, has an expiry. **None records the session or whether
        Mike ruled it**, and git cannot recover either, because every commit
        has the same single author. Live in atelier:
        - **91 line allow-markers, all whole-line.** No span form exists:
          the median marked line is 135 characters, and only about 3 lines
          hold more than one finding. 84 of the 91 (92%) are unscoped,
          although nearly all cover a single rule.
        - **33 ignore-file globs.** About 14 mask a file or folder where only
          a few lines are findings, for example 1–3 lines in files of 21–1,451
          lines, or a 357-file records tree for 43 spelling findings. About 5
          are genuinely whole-file.
        - **Who, when, session:** 0 of 130 exceptions carry a session ID, 4
          carry a date, 6 a who-ish word, and all of it is prose.
        - **Three exemptions need no reason and are not counted:** the
          reviewscan deferral substring (6 live), wrapscan silencing any
          line that carries a *sibling's* marker (11 lines), and
          `sizescan:budget`.
        🔴 **A doctrine line contradicts Mike's standard and goes in part 2.**
        `GUARDS.md` § *Who, why, when* says who and when "come from version
        control", and that demanding an author field asks someone to retype
        what `git blame` knows. `git blame` cannot name a session, or tell a
        ruling from an agent's choice.
  - [x] 📏 **PART 1 DONE: scale.** Every guard × the 3 largest repos, under a
        hard 300 s cap. **Memory held:** every finished real-repo run peaked
        under 120 MB. **Time did not.** The content scanners walk the whole
        *filesystem*, untracked trees included. In one private repo 93% of
        the files walked, 15.7 GB of 15.8 GB, are untracked, so secretscan,
        leakscan and conflictscan hit the cap there. That is the cause of
        the hours-long runs. Split out as `110/110`. Two guards **are**
        unbounded on one huge file: pathscan reads files whole (RSS past
        1 GB) and linkscan keeps every finding (past 500 MB). Split out as
        `110/120`.
  - [ ] 📐 **PART 2 DESIGN DRAFTED 2026-10-03: ADR
        `docs/decisions/2026-10-03-0641-the-exception-register.md`** (draft,
        so Mike rules). It proposes:
        - **One per-repo register** that every guard reads.
        - **Required fields:** why, who (the session transcript ID, and
          whether he *ruled* it with his words quoted, *answered* a
          session's options, or an *agent* chose it), when, and review-by
          for deferments.
        - **A narrowness ladder** whose finest rung exempts one exact
          string by its hash, never storing the string.
        - **Stale and over-wide entries reported** on every run.
        - **A helper** that fills in session and time automatically.
        The design cold pass is queued at `160/650`, before acceptance.
        The build (part 3) waits on both.

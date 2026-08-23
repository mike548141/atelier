- [x] 🔥 **The mixed-root scan — BUILT 2026-08-23** (wt: mixed-root-eleven-0823)
      — a scanner given `--root X` and a *relative* path scanned your cwd's
      file while applying X's rules: a mixed-root run that reported
      confidently and meant nothing. Handed up by the `ros` session on
      2026-08-17, which had lost a round of readings to a mixed root and
      suspected this. **`ros` later withdrew that attribution and the
      withdrawal is accepted** — its readings came from a stuck `cd`, not from
      this defect (the full account is in the ⚖️ note below; Mike ruled the
      lead sentence corrected rather than annotated, 2026-08-23). What the
      item rests on instead is what was proven here: the mechanism, the
      eleven-tool sweep at HEAD, and the `floor.py` finding — all reproduced
      by probe, none of them dependent on that first report being right.
      ✅ **What landed**, exactly as specified below and nothing more: the
      `pointerscan` line copied into the eleven, each site carrying a
      three-line note so the next hand knows why it is not `Path(p)`; and
      **one** parametrised test (`tools/test_mixed_root.py`), run over twelve
      mains — the eleven plus `pointerscan` itself, so the tool the fix was
      copied from cannot drift out of the family unnoticed.
      🧪 **Proven against the known-bad input before it was believed**, per
      `370/030`: the same test file run with `PYTHONPATH` pointed at the
      unfixed tools fails **12 times**, and passes on the fix. A test that
      passes either way would have proven nothing.
      ⚖️ **The absolute-path judgement, taken and stated:** `root / p` still
      lets an *absolute* path outside `root` be scanned under `root`'s rules,
      and that is left as it is — an absolute target is an explicit act by the
      caller, not a silent mis-resolution, and `--staged` mode in `leakscan`
      and `secretscan` already refuses absolutes for its own reason. A test
      pins it (`test_absolute_target_is_still_taken_as_given`) so the
      permissive half is deliberate rather than untested.
      ✅ **Ruled 2026-08-23 (Mike):** the lead sentence is CORRECTED, not
      annotated — a skim reader only ever reads the first line, and it was the
      half that read wrong. The severity half of the 2026-08-17 question was
      already moot by then, the defect being fixed.
      🔎 **The mechanism.** A relative argument becomes `Path(p)`, which
      resolves against **cwd**, never against `--root`. But `root` is used
      separately for everything else the run depends on — the `.<tool>ignore`
      lookup, the repo-relative anchors, the `docs/` default. So the run reads
      **one repo's file under another repo's rules**. That is worse than
      simply using the wrong root, because neither half of the output is
      attributable and nothing in it says so.
      🔎 **The blast radius, swept at HEAD 2026-08-17 rather than estimated.**
      This item previously said "at least four tools". The sweep says
      **eleven**, and names them so the next sweep can disagree with something
      specific — `datescan:686`, `leakscan:855`, `linkscan:598`,
      `pathscan:849`, `plainscan:586`, `reviewscan:412`, `secretscan:989`,
      `sizescan:643`, `spellscan:639`, `stampscan:851`, `wrapscan:546`. That
      is every scanner taking both `--root` and a path list, minus one.
      `reviewscan` spells it `Path(p).resolve()`, which is the same defect in
      different words. `board`, `publishscan` and `harvestscan` accept a path
      list and **ignore** it (their unit is the repo), and `coldsweep` walks
      from `root`; all four are unaffected.
      🔑 **Why it survived, and why that is the frightening part.**
      `floor.py:1485` pre-resolves before it calls anything —
      `scoped = [str((root / p).resolve()) for p in paths] or [str(root)]` —
      so the hook plane and CI hand every scanner an **absolute** path and
      have never once exercised the defect. The guard is correct wherever a
      machine calls it and wrong wherever a human does. That inverts the usual
      risk story: the plane with no test coverage is the plane whose output a
      session reads, believes, and reports from.
      🔑 **It needs a path collision to bite, and this estate guarantees one.**
      Every tool exits 2 on a target that does not exist, so a relative
      argument only *silently* mis-resolves when the same relative path exists
      in both trees. `docs/ROADMAP.md`, `docs/method/`, `docs/SESSIONS.md` —
      every child has them under the same names by design. The propagation
      model is what turns a latent bug into a reliable one.
      🎯 **The fix, chosen: adopt the line `pointerscan` already uses.**
      `pointerscan:456` and `:676` carry
      `p = (root / raw) if not Path(raw).is_absolute() else Path(raw)` and are
      the one scanner in the family that gets this right. Copy it into the
      eleven. Not the louder alternative (refuse a target outside `root`,
      exit 2) as the primary fix — an in-tree reference implementation beats a
      new convention, and `root / p` makes `--root` mean exactly one thing.
      ⚖️ **The one judgement left, and it is small.** `root / p` still lets an
      *absolute* path outside `root` be scanned under `root`'s rules. That is
      an explicit act by the caller rather than a silent mis-resolution, so it
      is a separate decision, not a blocker: take it as a second commit, or
      rule it acceptable and say so. Do not let it hold the eleven.
      🤔 **The shared-layer question, and why it does not gate this.**
      Eleven copies of one line is the argument `115/080` already makes for a
      single scanner harness — and eleven is a better argument than four.
      But the harness is a programme and this is a false clean in the hand of
      every session today. Fix in place, and record the count as evidence for
      `115/080` rather than waiting on it.
      🧪 **The test that must exist**, and one test, not eleven: build two
      temporary trees carrying the *same* relative path with different
      content and different ignore files, `chdir` into the second, call each
      tool's `main(["--root", str(first), "docs/<file>"])`, and assert the
      finding names the first tree's file. Parametrised over the eleven mains
      it is the regression guard for the harness later; written eleven times
      it is eleven things to forget. A green run must be impossible while any
      tool reads the cwd.
      🔁 **`ros` re-measured unprompted and withdrew its claim — the withdrawal
      does not land, and the defect is unaffected (2026-08-17).** Over the
      channel, `ros` withdrew "the flag is silently ignored", saying it never
      tested it and that a persisted `cd` explained its readings. Its
      re-measurement is sound and its **conclusion — "there is no tool
      defect" — is falsified**: it re-ran `wrapscan --root <probe>` and
      `--root .`, neither of which passes a *relative* path with a foreign
      root, so neither can exercise this. Confirmed here by probe rather than
      argument — two trees carrying the same `docs/bad.md`, one 199 columns and
      one clean, `--root` at the clean tree: the finding names the **cwd** tree's
      line, and with an ignore file added to the root tree the same run reports
      clean and says `1 file(s) suppressed`. Both halves, one command. So the
      claim was wrong in one direction and the withdrawal is wrong in the other;
      the truth is the mechanism above, and this item already held it.
      ⚖️ **What the withdrawal cost this item: its grounding story — since
      PAID, 2026-08-23.** The lead used to say `ros` lost a round of readings
      *to this defect*. `ros` says the cause was a stuck `cd` with `--root .` —
      root and target both atelier, so **not a mixed root, and not an instance
      of this**. `ros` is the only witness to its own invocation, so that
      account outranks the inference, and **Mike ruled the lead sentence
      corrected rather than annotated** (2026-08-23): a skim reader only ever
      reads the first line. The lead above now says so, and the item holds 🔥 on
      the eleven-tool proof plus the `floor.py` finding alone. The exposure
      argument never depended on the withdrawn instance — the estate's own
      guidance already records that a shell's cwd can silently revert, and the
      2026-08-17 session re-demonstrated exactly that while verifying `120`.
      *Source: the `ros` session's hand-up, 2026-08-17, after its board split.
      `ros` reported it as "the flag is silently ignored" and as
      `linkscan`/`sizescan` behaving correctly; both are slightly off — the
      flag is honoured for rules and not for targets, and those two carry the
      identical line, differing only in their default when no path is given.
      Mechanism and the eleven-tool count re-derived here at HEAD. `ros` was not
      asked to re-measure and then did so on its own; see the withdrawal note
      above, which changes the grounding and not the defect.*

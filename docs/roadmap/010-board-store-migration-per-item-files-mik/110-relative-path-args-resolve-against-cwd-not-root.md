- [ ] 🔥 **A scanner given `--root X` and a *relative* path scans your cwd's
      file while applying X's rules** — a mixed-root run that reports
      confidently and means nothing. Handed up by the `ros` session on
      2026-08-17, which lost a full round of "ros is clean" readings that were
      actually atelier's tree, including a floor result it nearly reported
      from. It was caught only by recognising atelier section names in
      supposed `ros` output. **READY TO TAKE** — the fix is chosen, the
      reference implementation is already in this tree, and the test is
      specified below. Nothing here is built.
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
      ⚖️ **What the withdrawal DOES cost this item: its grounding story.** The
      lead still says `ros` lost a round of readings *to this defect*. `ros` now
      says the cause was a stuck `cd` with `--root .` — root and target both
      atelier, so **not a mixed root, and not an instance of this**. `ros` is
      the only witness to its own invocation, so that account outranks the
      inference. 🎯 **Mike's to rule:** retire the grounding sentence and hold
      🔥 on the eleven-tool proof plus the `floor.py` finding alone, or step the
      severity down now that no confirmed real-world instance stands. The
      exposure argument survives either way — the estate's own guidance already
      records that a shell's cwd can silently revert, and this session
      re-demonstrated exactly that while verifying `120`.
      *Source: the `ros` session's hand-up, 2026-08-17, after its board split.
      `ros` reported it as "the flag is silently ignored" and as
      `linkscan`/`sizescan` behaving correctly; both are slightly off — the
      flag is honoured for rules and not for targets, and those two carry the
      identical line, differing only in their default when no path is given.
      Mechanism and the eleven-tool count re-derived here at HEAD. `ros` was not
      asked to re-measure and then did so on its own; see the withdrawal note
      above, which changes the grounding and not the defect.*

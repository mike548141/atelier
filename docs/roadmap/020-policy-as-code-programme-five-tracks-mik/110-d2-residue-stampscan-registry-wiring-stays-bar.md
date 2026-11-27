- [x] **D2 residue — stampscan registry wiring stays barred on ST3.** The
      advisory wiring landed 2026-08-05 (atelier `ci.yml` only, the
      reviewer's bar step 1); registry wiring — which reaches every child
      (ADR 0008) — waits on the child-side `source=` resolution story:
      pin-aware (a child at `atelier@<SHA>` may lawfully differ from
      atelier@main), and `create-repo` taught that the markers are
      load-bearing scaffold content. Any blocking flip is a separate later
      ruling after an advisory soak (the wrapscan/datescan precedent).

      ✅ **Done 2026-11-27** (session 9c5fa72c's queue run, a worker, Opus
      5.5). **What ST3 barred, confirmed against the review:** the template's
      stamp names `source=docs/method/PROPAGATION.md`, which exists only in
      atelier, so a child running `stampscan` exits 2, and registry wiring
      would make every child run it; the review's sharpening made pin-awareness
      part of the precondition. Measured before the change over the estate's
      children: 25 stamped floors, every one `missing-source`, exit 2.
      - **The resolution** (`tools/stampscan.py`, § THE CHILD'S PIN). When
        `source=` is not in the scanned tree, the tree is a git repository and
        it is not atelier (same git common dir, so an atelier worktree counts
        as atelier), the source is read from the atelier checkout at the
        child's own pin, `git show <pin>:<source>`, the pin read by
        `pins.read_pin`, with the child's placeholder fills put back by
        `pins.fill_placeholders`. Never atelier's HEAD. The atelier checkout is
        the one the scanner ships in, or `--atelier <path>`. Source confinement
        (ST4) is unchanged. A question the run cannot answer (no pin, a pin the
        checkout lacks, a pin from before the region was marked) is a new
        `unverified` finding: never clean, exit 2 without `--warn`, 0 with it,
        never enough for either cover switch. A source absent from the child
        and from atelier at a pin it holds still points nowhere: config error.
      - **Measured after:** the same 25 read `identical` at their pins; every
        child exits 0 under `--warn`. One drift remains, a raw marker quoted in
        one child's decision record, reported and not blocking. `pins.py
        --floor` agrees on every child both tools judged.
      - **Wired** warn-only in `tools/floor.py`, ci plane only (`CI_ONLY`,
        beside `HOOK_ONLY`: the whole-tree walk took up to 14 s on the largest
        children, against 5 to 6 s for linkscan's). The bespoke `ci.yml` step
        is retired, pathscan's promotion precedent. The precondition `320/130`
        named (`--require-stamps`, and `--require-floor-stamp`) exists; the
        wiring passes neither, because a warn-only line demands no cover.
      - **`/atelier:repo create`** now says the marker lines are load-bearing
        and proves the copy with `stampscan --require-floor-stamp --root .
        CLAUDE.md` (checked on a synthetic scaffold: `identical`, exit 0).
      - **Tests:** 14 in `ChildPinResolution` (`tools/test_stampscan.py`),
        including a stale pin (clean against its pin, drift with HEAD's text),
        no pin, a pin the checkout lacks, a pre-region pin, an unfilled
        placeholder, and atelier itself; 139 in the module. `test_floor.py`
        (433, one new: the CI-only check lists as skipped on the hook) and the
        floor's selftest pass.
      - **Left, and not this item's:** the blocking flip (drop `--warn`, and add
        `--require-floor-stamp` if an unstamped floor should fail) is the
        principal's later ruling after the soak; a hook-plane line is one more
        template once the walk is cheaper. `320/130`'s shapes (a)–(c) stay
        unruled on that item.
      - Commitment: a check every child's CI runs, telling the child its
        inlined safety floor matches atelier's text at the child's own pin.
      - Worst failure: not holding — it reads `identical` for a copy that
        differs (a placeholder fill absorbing a real reword, or the wrong
        reference read), or a no-answer is filed `unverified` and the floor's
        warn-only line shows exit 0. Too tight — a faithful child reds or exits
        2 and blocks its CI; that way is loud, on every child's next push and
        in the 25-child probe.
      - Why the floor misses it: a false `identical` is silent. The tests pin
        chosen fixtures, and 25 of 25 `identical` is also what a too-lenient
        comparison would print; the floor renders the check `👁️ warn-only`,
        exit 0, whether every stamp was verified or none was.

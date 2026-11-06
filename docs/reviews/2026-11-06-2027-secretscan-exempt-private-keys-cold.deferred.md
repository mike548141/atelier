# Sibling to the secretscan exempt-private-keys cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** The orchestrator, drain session `850e2a78`, holds it and hands it over on receipt
of the committed act 1. Written 2026-11-06 UTC by the brief-writer, session `782f8a66` (Opus
5.5), named in the brief's provenance; it forms no finding and assigns no severity. Fold this
file in below the reconcile and delete it at phase 2.

## Intent record and author's account

- `115/380` (`docs/roadmap/115-guardrail-architecture-mike-commissioned/`) — read in full by the
  brief-writer. Found 2026-11-06 by queue run `722ac2e2` at its own landing of `320/790`: the
  worker's fix had added four real throwaway private keys (EC and RSA PKCS#8, SEC1, PKCS#1) to
  `tools/test_secretscan.py`; every check passed and only the orchestrator's read caught them
  before the push; the branch was amended to synthetic DER and the record says nothing reached
  `main`. Its "possible shape, to judge" is the landed design. It says the finding run took the
  work itself, advisory first, because the change alters what a guard reads inside its own
  exemptions and children float at `main`.
- Its `DONE 2026-11-06` paragraph is the author's landing account and carries a **live-proven
  claim** to re-run (V2): a probe over every child with a `.secretscanignore`, with a count of
  such children, blocking results unchanged, run times within noise, and the rule's only hits
  in one child, described there as true positives held as recorded debt.
- No principal ruling on the design was found in either record. The principal's pick quoted in
  the pointer approves running the pass, not the design or the advisory tier.
- No commit message body was read.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-06 UTC, from the worktree root at `b2851e9`, in the
foreground unless stated:

- `test_secretscan.py`: 239 tests, OK, exit 0 (about 10 s). `secretscan --selftest`: exit 0.
- Full suite under `nice -n 10`: 2358 tests, OK, exit 0 (536.5 s, load average 2.5 to 4.8).
- `floor.py --plane ci --root .`: exit 0. `--plane hook`: exit 0, with nothing staged. Both ran
  with this brief's four files untracked and the two pointer lines unstaged in the tree.
- The tree: exit 0; 0 blocking; 28 advisory, all `low-variety-entropy`; 0
  `exempt-private-key`; `files_by_ignore_glob` 3.
- The test-file loop: 0 hits in `tools/test_secretscan.py` at each of `c5f6202`, `3d53b67` and
  `0d8db9c`.
- The exempt file, scratch repo: staged, exit 0, 1 advisory finding, `exempt-private-key` at
  line 2, excerpt naming a base64 run of 1216 decoded bytes in a PKCS#8 outline,
  `files_by_ignore_glob` 1; whole tree, the same finding, exit 0; with `--disable
  exempt-private-key`, 0 advisory, exit 0. Control, the pre-delta tool from `815dce6` on the same
  staging: 0 advisory, exit 0. A first attempt with a glob carrying no stated reason exited 2
  on every plane (existing behaviour, not this delta's), so the recipe states a reason.
- Children, read-only, count only: `floorfleet` found 23 rows, 22 `wired` and 1 `absent`; 21
  wired children other than the parent, **11 of them carrying a `.secretscanignore`**. Pre-delta
  tool (`815dce6`) against HEAD: exit codes and `counts.blocking` identical in all 21.
  `exempt-private-key` hits in exactly **one** child: 6, all `PEM PRIVATE KEY` blocks, across 3
  files; that child's advisory count goes from 2 to 8. Run time: the largest child 74.0 s
  before and 78.0 s at HEAD (one run each, under load); every other child within 0.1 s. The
  intent record states a different count of children with a `.secretscanignore`; reconcile the
  two.

## Prior records on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/050-a-real-credential-in-an-exempt-fixture-file-is.md`
  — by its file name, an earlier instance of the same class; surfaced by the brief's reconcile
  sweep. Not opened.
- `docs/reviews/2026-07-28-1204-c1-advisory-cold.md`,
  `2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md`,
  `2026-10-17-1010-advisory-count-per-scanner-cold.md` — the advisory tier and its count line,
  which this delta adds a second rule to.
- `docs/reviews/2026-07-28-1220-secretscan-fragment-cold.md` — by its name, earlier work on
  fragments in `secretscan`.
- `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md` and its top-up — the
  `--staged` reader (`115/360`); the brief-writer read only `160/950`'s summary of it.
- `docs/method/GUARDS.md`, `commands/scan.md`, `docs/build/templates/workflows/floor.yml`,
  `tools/publishscan.py`: hits of the reconcile sweep, not read.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **Tier.** `SECRETS.md`'s posture is over-flag, and a working private key in a public repo is
   the clearest leak there is. The check is advisory, so the exit code does not move. Whose
   decision was advisory, is it recorded where the doctrine says narrowing decisions go, and is
   there a board item for the flip to blocking that the README and comment promise ("a later
   item may")?
2. **Who reads it.** The floor board carries the `secretscan advisory:` count. On atelier's own
   tree that count is 28 low-variety findings. Does a real key in an exempt file show as 29 on
   the board, indistinguishable from noise, and is that "an advisory finding nobody reads is
   cover, not coverage" (EI1)?
3. **Off switch.** `--help` lists the rules `--disable` takes and does not name
   `exempt-private-key`. Can a child disable it through the floor's `flags`, and would
   `floorfleet` or the summary line show that it did?
4. **Shapes missed.** Traditional encrypted PEM (`Proc-Type: 4,ENCRYPTED`) is stated as not a
   hit, while `ENCRYPTED PRIVATE KEY` is checked; is the difference principled? A bare OpenSSH
   body (no PEM lines), a PuTTY `.ppk`, a JWK with a `d` member (base64url), a PKCS#12 or DER
   key file the reader treats as binary, a key in a JSON string with `\n` escapes, a key split
   over comma-separated literals or `+` concatenation, a key whose first fragment shares a line
   with other text: which are caught, which are stated gaps, and which are silent gaps?
5. **Outline false positives.** `private_key_outline` matches PKCS#1 as a `SEQUENCE` of an
   `INTEGER` 0 or 1 then five or more `INTEGER`s and optional trailing `SEQUENCE`s. What else has
   that shape (DSA or DH parameters, some signature formats, an ASN.1 test vector in a crypto
   library's fixtures)? Does the advisory text ("holds text that decodes as a real private
   key") overclaim when the test is an outline, not a parse?
6. **Cost.** `_FRAG_RX` and `_TAIL_AFTER_RX` carry `\s*` and optional groups; `_LONG_FRAG_RX`
   and `_RUN_RX` run `finditer` over every line of up to 4096 characters, and the reader windows
   longer lines. Is there an input that makes any of them super-linear, and what does the check
   cost on the largest exempt file in the children (the brief's probe times it)?
7. **State machine edges.** `covered` remembers one PEM block; `flush` drops a run whose start
   line falls in it. Two keys in one file, a PEM block followed by its own body as a quoted
   literal, a padded `=` mid-run, an `acc_len` cap flush in the middle of a 4096-bit key: does
   each report once, twice, or never?
8. **Staged plane.** Only added lines are read. A key added across two commits, or a commit
   that adds the key lines to an existing exempt file whose earlier half was committed earlier,
   is missed at the hook; the README says CI "prints anything the hook missed", but CI does not
   block on it either. Is "the CI run reads the whole file" a claim the floor's CI plane makes
   good for every child (scope, `flags`)?
9. **Record dates.** The changelog heading is dated 2026-11-07; the commit landed 2026-11-06
   UTC (2026-11-07 in the committer's zone). `CONVENTIONS.md` keeps UTC at rest.
10. **Public record of a near miss.** The README, comment and changelog say a worker put four
    working private keys in the test file. Is that statement accurate against history (the
    brief's test-file loop), and is it the right content for a public tool README?
11. **Exempt binary files.** `.secretscanignore` can name a binary file; does the exempt check
    read it, skip it as binary, or fail?

## Facts held back from the brief

- The intent record's child-probe claim (above) is what the brief's children line re-runs; the
  brief does not state the claim or its numbers.
- `115/050` exists (above); the brief does not name it.

# Sibling to the G3 grace and metadata-sets cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer subagent of session 5070f22b
named in the brief's provenance; it forms no finding and assigns no severity. Fold this file in
below the reconcile and delete it at phase 2.

## Intent records

- `020/150` (`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/`) — read in full by the
  brief-writer. Lines 1–18 are the funding and the 2026-08-04 blocking ruling, paraphrased, not
  quoted. Lines 20–42 are the 2026-10-03 build's account: why it was held as a draft PR (the
  child CI reds it would cause, with counts), the two decisions put to the principal, and what
  the build found on the staged plane and in the floor's flag blocklist (filed as `020/410`).
  Lines 43–58 record his answers, and say the grace "stands against E6a's no-advisory-form
  decision" with his answer as the authority. Lines 59–76 are the landing account: the grace
  date "was the queue run's choice on '~30 days', not a ruling"; text metadata needing a line
  is called "a judgement call"; test counts; the removal at `010/190`.
- `020/440` — read in full. The author's reading of "fields" as the scanner's named sets, the
  build account, and its own flag (lines 23–26) that the reading was wrong, with the principal's
  correction and the follow-up at `020/450`.
- `020/450` lines 1–12 and `010/190` whole — read by the brief-writer. `010/190` asks that,
  before removal, the children still unlisted be counted and the list taken to the principal.
- No commit message body, PR body, PR comment or PR review was read.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-10-26 UTC (before the cut-off), from the worktree root at
`6f78d85`, in the foreground, local term list present:

- `test_leakscan.py`: 219 tests, OK. `test_floor.py`: 150, OK. `test_allowmarker.py`: 31, OK.
  `test_report.py`: 71, OK. All exit 0.
- `leakscan --selftest` exit 0; `floor --selftest` exit 0.
- Full suite: 2,032 tests, OK, exit 0 (about 8.5 minutes under load).
- `floor.py --plane ci --root .`: exit 0. `--plane hook`: exit 0, with nothing staged in the
  worktree (so it exercised no staged binary).
- `leakscan --root . --binary-entries` on atelier: 0 lines, exit 0;
  `git ls-files --eol` shows 0 tracked binaries.
- Grace boundary, one synthetic tracked PNG with one harmless text chunk: day before the
  cut-off exit 0; cut-off exit 1; a day after exit 1; real clock (2026-10-26) exit 0, with two
  G3 warnings counted in the `suppressed:` line.
- Children, read-only, count only: `floorfleet` found 22 rows, 21 `wired` and 1 `absent`; 20
  wired children other than the parent. `--binary-entries` exited 0 in all 20; 5 of them would
  be asked for lines, 179 file lines and 111 set lines in total; 1 already has a
  `.leakscanbinaries`. 1 child passes leakscan `flags` and 2 pass leakscan `scope` through the
  floor. `floor.py --list` exited 0 on both planes for all 20.
- `exiftool`: not on `PATH` or in the usual install places; nothing run.

## Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- `2026-07-29-1243-e6-intent-cold.md`, `2026-08-05-1253-e6-application-cold.md` — names suggest
  E6, the posture this delta excepts.
- `2026-08-09-0826-e7-leakscan-build-cold.md` — the build G3 was the residue of.
- `2026-08-17-1321-posture-cold.md`, `2026-10-04-2215-exception-register-design-cold.md`.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `tools/README.md` presents the decision device's option text ("unlisted files print a
   warning naming a cut-off date (~30 days) … each lists its files when convenient") as the
   principal's quoted words; the intent record calls it the option text he picked. Is that an
   attribution overclaim?
2. E6a's doctrine home, `SECRETS.md` § *The boundary's posture*, still says leakscan "gains no
   advisory form". The exception is stated in `tools/README.md`, code comments and the
   changelog only. Is that one home, or a doctrine edit made at tool altitude, the failure
   shape `020/140` itself names?
3. ADR `2026-10-03-0641` (the exception register) says G3 (PR #97) "is reworked onto this
   register as `file` entries", and `110/100` says PR #97 "is held until it meets (1) and (2)".
   The landed gate uses its own `.leakscanbinaries`. Was that decision superseded on the record,
   or contradicted silently?
4. `forbidden_flags` refuses mode flags, but a reasoned `flags` entry may still carry other
   arguments. Can `--root <elsewhere>`, `--terms`, a positional path, or `--` followed by a
   dash-led argument turn the CI plane into a pass that never runs the gate, without the grace
   being "moved"?
5. `.leakscanignore` runs before the gate. Is a reasoned glob over a child's images a sanctioned
   route around G3, and does the principal's blocking ruling admit it?
6. The blanket-reason refusal compares reasons. Is it string equality, defeated by one changed
   character, and after `34dc0f0` does anything stop one generic reason being copied onto every
   set line of every file?
7. 34dc0f0's README text still quotes "fields A, B, and C" as satisfied by data-type sets after
   the principal said that reading was wrong. Does any landed text claim more than the set-level
   design delivers?
8. The walker decompresses `zTXt`/`iTXt` and walks length-prefixed segments. Is decompressed
   size capped, and do zero-length or self-referencing lengths terminate?
9. Before the cut-off the warnings print but exit 0. In a child's CI, who reads them? If nobody,
   the cut-off reds the 5 children above with no prior signal, which `010/190` assumes away.
10. The required reasons are committed in each child, often public. Does the gate push children
    to describe private images in public text?
11. The staged hook reads the index copy. Does a partially staged binary, a binary with
    `-diff`/`binary` attributes that is really text, or a submodule change slip through?
12. The README's example digests in its sample manifest — are they real digests of any file, and
    do any fixtures in `test_report.py` or the selftest carry metadata strings beyond the
    `example.com` address the brief-writer saw?

# Sibling to the secretscan public PEM spans cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** The orchestrator, drain session `850e2a78`, holds it and hands it over on receipt
of the committed act 1. Written 2026-11-06 UTC by the brief-writer, session `782f8a66` (Opus
5.5), named in the brief's provenance; it forms no finding and assigns no severity. Fold this
file in below the reconcile and delete it at phase 2.

## Intent record and author's account

- `320/790` (`docs/roadmap/320-child-filed-findings-via-pointing-up/`) — read in full by the
  brief-writer. It is a hand-up from a private child, filed 2026-11-03 under `PROPAGATION.md`
  § *Pointing up* by a queue-run worker with no reviewer, stated class-only. It names the gap
  (per-line `PUBLIC_KEY_RX`, a 14-line P-256 certificate giving 8 entropy findings staged
  alone), the cost to a child (a whole-file `.secretscanignore` entry, so a private key pasted in
  later passes unseen; the filing child added its own certificates-only check), and "a possible
  shape, for atelier to judge" which the landed design follows, including the optional X.509
  decode. Its `DONE 2026-11-06` paragraph is the author's landing account; it says the repro
  certificate now scans clean and its private key still blocks.
- The queue pointer `160/1030` records that the authoring session sent the worker back twice:
  once to require the nested `SEQUENCE`, once to replace real throwaway private keys in the
  fixtures with synthetic DER. `115/380` records the second as the finding that led to
  `160/1040`'s delta, and says nothing reached `main`.
- No principal ruling on the design was found in either record. The principal's words in the
  pointer approve running the pass, not the design.
- No commit message body was read.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-06 UTC, from the worktree root at `b2851e9`, in the
foreground unless stated:

- `test_secretscan.py`: 239 tests, OK, exit 0 (about 10 s). `secretscan --selftest`: exit 0.
- Full suite under `nice -n 10`: 2358 tests, OK, exit 0 (536.5 s, load average 2.5 to 4.8).
- `floor.py --plane ci --root .`: exit 0. `--plane hook`: exit 0, with nothing staged (so it
  exercised no staged certificate). Both ran with this brief's four files untracked and the two
  pointer lines unstaged in the tree.
- The tree: exit 0; 0 blocking; 28 advisory, all `low-variety-entropy`;
  `by_public_key_line` 3; `files_by_ignore_glob` 3.
- `--staged`, scratch repo: a new certificate-shaped file staged whole, exit 0, 10 by
  public-key line; re-keyed in place (the staged diff adds and removes 10 body lines, no BEGIN
  or END), exit 0, 10 by public-key line. Control, the pre-delta tool from `0518906` on the same
  body-only staging: 10 findings, commit blocked, exit 1.
- Children, read-only, count only: `floorfleet` found 23 rows, 22 `wired` and 1 `absent`; 21
  wired children other than the parent. Run with the pre-delta tool (`0518906`), the post-delta
  tool (`815dce6`, whose `secretscan.py` is `3d53b67`'s) and HEAD: exit codes and
  `counts.blocking` identical in all 21 (3 children exit 1 at every version). **`by public-key
  line` was identical before and after the delta in all 21**: the exemption suppressed nothing
  in any child on this machine (the count is non-zero in 4 children, the same at each version).
  The largest child took 73 to 78 s a run at every version.
- Not run: the fail-closed `--staged` case, an encrypted-PKCS#8 body under a certificate header,
  and the real-world shapes in question 6 below.

## Prior records on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md` and its top-up
  `2026-10-28-1255-staged-positional-reader-topup-cold.md` — the `--staged` reader this delta's
  staged path sits on (`115/360`). The brief-writer read the queue pointer `160/950`, which
  summarises that verdict; it did not open the verdict.
- `docs/roadmap/320-child-filed-findings-via-pointing-up/290-secretscan-reads-published-urls-as-credentials-and-mis-locates-findings-in-paths-with-spaces.md`
  — cited as `320/290` in `scan_lines`' docstring for the real-line-number shape.
- `docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md` (the public-key
  fingerprint carve-out beside this one), `2026-07-28-1220-secretscan-fragment-cold.md`,
  `2026-09-25-0715-secretscan-stream-pathscan-roots-cold.md` (the streaming reader
  `_scan_file` uses).
- `docs/method/GUARDS.md`, `commands/scan.md`, `SECURITY.md`: possible mirror sites
  (question 11), not read.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `SECRETS.md` § *The boundary's posture* says narrowing coverage is the principal's decision,
   recorded in the roadmap or an ADR, never settled at tool altitude. This delta narrows the
   entropy rule's coverage; its record is a child's hand-up, a queue run's DONE line, the
   README, the changelog and a code comment. Is there a principal decision behind the narrowing,
   and if not, is that the failure shape the doctrine names?
2. The nested-`SEQUENCE` test separates a certificate from PKCS#8, PKCS#1 and SEC1. An
   `EncryptedPrivateKeyInfo` (`SEQUENCE { SEQUENCE, OCTET STRING }`) has a `SEQUENCE` first.
   Is an encrypted PKCS#8 body under a `CERTIFICATE` header exempt? What other secret-bearing
   DER (PKCS#12, PKCS#7/CMS with embedded keys, a CSR) has the same outline?
3. The README says "a random secret wrapped in forged headers" is still flagged. That holds for
   a wrapper made by accident; anyone who builds the outline on purpose passes. Is the threat
   model (accidental, not adversarial) stated, and is the README's claim stronger than its
   evidence (V1)?
4. `_der_element` accepts a long-form length with leading zero octets and the inner element need
   not fill the outer. Is "one DER `SEQUENCE`" an overclaim for a BER-tolerant check, and does
   it matter?
5. `scan_lines` counts exempt body lines in `by public-key line`. Does the count mean lines or
   entropy spans, and does a reader of the summary line now read the same field differently?
6. Whole-block voiding: certificate bundles in real repos are often indented YAML block
   scalars, carry CRLF endings, sit after `openssl x509 -text` output, or sit inside a Python
   triple-quoted string that opens on the BEGIN line (`CERT = """-----BEGIN ...`). Which of
   those void the block, and is the cost a child pays for that pushed back to a whole-file
   exemption, the outcome the hand-up was about?
7. `--staged`: does `report.staged_blob` read the index copy for a partially staged file, a
   rename, a mode change, a submodule, a file deleted from the worktree but still staged? What
   exit code does a blob read failure give, and is it ever 0?
8. `_scan_file` feeds `pem_exempt_stream` from `_iter_numbered_lines`, which windows an
   overlong line under the same line number (020/370). Can a window boundary inside a BEGIN or
   END line, or a repeated line number, open or close a block wrongly?
9. `tools/test_secretscan.py` now carries a real self-signed certificate (`REAL_PEM_BODIES`,
   added in `3d53b67`) and its public key. Decode them: do the subject, issuer, serial,
   validity or extensions carry anything beyond `example.test`, such as a machine name, user,
   path or organisation? Is a real certificate the right fixture when `der_blob` exists?
10. 2048 lines and 76 characters: is the SLH-DSA size claim in the README and comment right, and
    is a certificate chain file (several blocks) bounded per block or in total?
11. Does any mirror site state the old per-line carve-out as the whole story: `commands/scan.md`,
    `docs/method/GUARDS.md`, the floor template, `SECURITY.md` (V3)?

## Facts held back from the brief

- A real self-signed certificate is in the test module (question 9); the brief says only that
  fixtures are a privacy surface.
- The brief-writer did not try the fail-closed `--staged` case (git unable to give the blob),
  the encrypted-PKCS#8 case (question 2) or any of the shapes in question 6.

# 2026-07-12 · session 40 — the two owed cold reviews cleared (Fable)

Mike: "Do any review work needed." The standing doctrine debt held two items:
the RECORD "keep private repos generic" section (incident-born, never cold-read)
and the signing doctrine (SIGNING.md + ADR 0007, decided-but-dormant). Both got
the full lifecycle — brief written, cold fresh-context agent run, verdict
appended to the brief, findings dispositioned, fixes applied — in parallel
(the session-36 pattern).

## Review 1 — RECORD "keep private repos generic": PASS-WITH-FINDINGS, 7/7 [fixed]

Verdict: `reviews/2026-07-12-record-private-repos-generic.md`. The central
clause (prose describing secrets is the leak class a scanner can't catch) held
and was re-proven live. The naming clause was **mis-drawn**: incident-born
doctrine over-fitted — it banned the harmless thing (names: the record
legitimately names children everywhere, and the incident scrub itself *kept*
every name) while the harmful thing — the **join** of a name to secret-posture
prose — survived that scrub in four places, one precise enough to serve as
targeting data (three named repos → "carrying secrets/client content").

Fixes: section redrafted — the join is the regulated class (name × which
secrets / where / exposure history / publication intent / client content);
name-only sanctioned behind a load-bearing-name test (e.g. ros, faves, numen);
enforcement stated honestly (write-time discipline + review sweeps — no
mechanical floor exists, by the rule's own premise); scrub-of-HEAD-is-not-
remediation now opens the section. The four surviving joins scrubbed at HEAD,
resolved the strict way (coarse joins genericised too) so doctrine and record
agree. Residual, stated: pre-scrub prose stays reachable in public history —
write-time is the only moment the rule can bind.

## Review 2 — signing doctrine: PASS-WITH-FINDINGS, 10/10 addressed

Verdict: `reviews/2026-07-12-signing-doctrine.md`. The reviewer live-drove
every mechanical claim in a scratch repo (throwaway keys; sign → backdate →
bound → retire → re-verify) and grounded the GitHub claims in current docs.
The core design **proved out**: config block verbatim-correct, and the
crown-jewel claim — append-only `allowed_signers` with bounded retirement
keeps old signatures verifiable — is true (git passes the committer timestamp
as verify-time). The perimeter failed: three blocking, all text-edit-cheap
because nothing is wired — exactly what review-before-activation was for.

- **G1** the CI design failed on atelier's own history: GitHub's server-side
  merge commits (`a0ef731`, `4b2cf6f`) are GPG-signed by the web-flow key and
  would have red-flagged the repo on first activation. Verification is now
  **two-plane**: `git verify-commit` for machine-key commits; the `gh api`
  verification check for `GitHub <noreply@github.com>` commits (spoof-safe, <!-- leakscan:allow: GitHub's public web-flow committer address, not personal data -->
  live-proven).
- **G2** the badge claim was **inverted**: GitHub verification is persistent —
  removing a key does *not* un-verify history. Corrected in SIGNING.md; ADR
  0007 corrected by **addendum** (no-edit rule). The durable-plane argument
  survives on its real grounds (self-hosted + reviewed vs GitHub-controlled).
- **G3** the man page's unquoted `valid-after=` syntax fails to parse on the
  estate's own ssh-keygen and silently fails the entry — quoted timestamps
  now mandated, with a known-signed-fixture selftest specced into step 5.
- G4–G10: principal convention + membership-not-binding honesty; custody at
  true strength (vault holds the durable copy; committing machines hold a
  working copy — standing machine credential); ladder steps 4–5 marked stub
  with the mechanics named (`fetch-depth: 0`, `git rev-list <boundary>..HEAD`);
  **trust list resolved at the child's pin, never floating `main`** (floating
  distributes fixes; here it would distribute *trust* — defeats the
  blast-radius argument); GPG rejection reworded to true strength;
  verified-email condition in step 1; bounding is retirement hygiene, not
  revocation.

Decision unchanged; **activation still gates on Mike registering a signing
key** (his act, AUTONOMY floor).

## Meta

Both reviews were doctrine-correcting, neither doctrine-reversing — the
review-before-activation sequencing earned its keep twice (every signing fix
was a text edit; a post-activation G1 would have been a fleet retrofit). The
fixes are doctrine text implementing the verdicts' own wording — judged
covered by the reviews themselves, not fresh unreviewed doctrine. The standing
review debt is now **clear**; ROADMAP's review-owed section holds no open item.
Fleet note: real method/ changes landed (RECORD, SIGNING), so children read
behind again at their next session — normal, the pin bump carries it.

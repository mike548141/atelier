# 2026-07-12 · session 40 — the two owed cold reviews cleared (Fable)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 63+1 -->
- [2026-07-12 · the two owed cold reviews cleared (Fable)](2026-07-12-40-two-cold-reviews-cleared.md) — "do any review work needed": the standing doctrine debt's two items run as parallel cold fresh-context agents (the session-36 pattern), full lifecycle each (brief → cold run → verdict in the brief file → disposition). **RECORD "keep private repos generic": PASS-WITH-FINDINGS, R1–R7 all [fixed]** — the central clause held (re-proven live), but the naming clause was mis-drawn: the harmful class is the **join** (a private repo's name × its sensitive posture), not the name — the rule as written outlawed the repo's own records while the actual join survived the incident scrub in four places. Section redrafted (join regulated; name-only sanctioned behind a load-bearing-name test, e.g. ros/faves/numen; enforcement stated honestly — write-time + review sweeps, no mechanical floor; scrub-of-HEAD-is-not-remediation); the four surviving joins scrubbed at HEAD the strict way so doctrine and record agree. **Signing doctrine (SIGNING.md + ADR 0007): PASS-WITH-FINDINGS, G1–G10 all addressed** — every mechanical claim live-driven in a scratch repo; the core design proved out (bounded retirement genuinely keeps old signatures verifiable). Three blocking, all text-edit-cheap pre-activation: CI verification made **two-plane** (GitHub's web-flow-signed merge commits — two already on `main` — would have red-flagged the repo; `gh api` check closes it spoof-safe), the badge-persistence claim was **inverted** vs current GitHub behaviour (corrected; ADR 0007 addendum per the no-edit rule), quoted `valid-after` timestamps mandated (unquoted man-page syntax fails on the estate's ssh-keygen). Plus trust-list-at-the-child's-pin (never floating `main` — floating distributes fixes, this would distribute *trust*), custody/boundary/backdating honesty. Decision unchanged; activation still gates on Mike registering a key. **The review-owed section is now clear.**


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

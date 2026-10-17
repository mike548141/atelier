# Sibling to the ccmail auth-advice cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-1010-ccmail-auth-advice-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record:
  `docs/roadmap/210-instruments-open-features/270-ccmail-sent-the-operator-to-a-setup-he-did-not-need.md`
  (the filing session's account; the child's own record stays private) — **not opened
  by the brief-writer**. It was added by the landing commit itself.
- The landing commit's message body (read by the brief-writer), in summary: with
  delegation configured a lapsed login needs only `gcloud auth login`, but `--status`
  printed the empty keychain route as a failure with the `--auth` fix, "and sessions
  relayed that as a step"; now an optional route's absence prints neutrally, plain
  `--auth` checks delegation first and prompts for nothing, and the fallback stays
  reachable "deliberately" with `--auth --fallback`; "four tests added (30 pass); man
  page and help updated". Trailer: an Opus model.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-09-25-0715-ccmail-build-cold.md` — the only verdict whose text
  names ccmail

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

None found: no other pass in this batch names `instruments/ccmail`. Two earlier commits
on the same file (`fd345ff`, which adopted the existing estate identity and added
ccpdf, and `5b0acf5`) are not this delta; their subjects only were seen.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The end-to-end test sets `CCMAIL_GCLOUD` to a missing path and `PATH` to nothing, but
   `gcloudBin` falls through to fixed install locations under the user's home (now the
   temporary one) and two system prefixes. On a machine with the CLI at one of those
   prefixes, does the test run the real CLI, read the real login and attempt a real
   signing call for a synthetic service account?
2. `--auth` with delegation configured now dies with "Delegation failed (…) — try gcloud
   auth login" for every non-expired failure, including a missing CLI, a refused
   signing call and a network error. Is "try a fresh login" the right instruction for
   each, or a new version of the misdirection the change removes?
3. When both routes fail, `resolveToken` lists the keychain route as "not set up — not
   needed, the delegation route is configured" directly under a delegation failure. Does
   that read as reassurance at the moment there is no way in?
4. `--fallback` is accepted by the parser in every mode. Is `ccmail --status --fallback`
   silent, and should an unknown pairing be a usage error as other flags are?
5. The man page's grounding note and the code comment cite what happened in a private
   child ("relayed to the operator, twice", "he did not need"). Is a gendered reference
   to the operator, and a count of incidents from a private repo, the narrowest form for
   a public repo?
6. The README's flag vocabulary and its ccmail sections still describe `--auth` as the
   one-time setup. The delta did not touch the README.
7. A hand-up landed code into atelier's instruments with its rule-4 review queued
   rather than run. Does `PROPAGATION.md` § *Pointing up* describe a child delivering a
   code change, or only a finding that atelier then acts on?
8. The lander is the orchestrator of the session that dispatched this brief-writer. Does
   rule 4's criterion, read strictly, need anything more for the taker than "not started
   or instructed by the author"?

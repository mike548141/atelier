# Enforcement census — REACH, SECRETS, SIGNING, STORAGE, TOOLBOX, session-open/

Board item `020/220`, slice 5 of the census, the last slice over `docs/method/`.
Run 2026-11-23 (UTC) by a worker of queue run 608d. This is a measurement
record, not doctrine: it changes no rule, and it builds no guard. It uses
slice 1's method, states and row format
(`docs/method/census/2026-11-16-1142-record-review-concurrency.md`) and the
fold conventions of slices 2 to 4
(`docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md`,
`docs/method/census/2026-11-16-1220-evidence-economics-communication-data.md`,
`docs/method/census/2026-11-23-1559-access-conventions-documentation-glossary-mechanisms-principles.md`),
so the five slices add up.

## What this asks

For each rule in five governing documents and the session-open directory: if it
is broken, what sees it? Each rule gets one state, defined as in slice 1.

- **enforced**: a mechanical check reads the breach. The row names the check,
  the plane it runs on (the pre-commit hook, the commit-message hook, CI, a
  harness hook, a session-open hook, or a tool's own guard at the call) and
  whether it **blocks** or **warns**. *partial* means the check covers some of
  the rule and the rest is unguarded.
- **directive-only**: nothing mechanical sees a breach. Where a self-run
  instrument would report it if a session chose to run it, the row says
  *instrument* and the state stays directive-only: nothing invokes those
  tools, so nothing sees the breach unless the breaker looks.
- **unenforceable, accepted**: the fact that would license or condemn the act
  is outside any check's evidence window (`GUARDS.md` § *Before building a
  check: the evidence window*), or the house has recorded a decision not to
  build the check, and the reason is stated. None of the 73 rules here is
  accepted on either ground (see *Doubts*).

A directive-only rule also gets the place its breach could be seen, as in
slices 1 to 4: **diff** (the committed change itself), **record** (only by
joining records outside one diff) or **invisible** (nothing in the tree or the
repo's records).

## Method, and what it did not do

1. Read `REACH.md`, `SECRETS.md`, `SIGNING.md`, `STORAGE.md` and `TOOLBOX.md`
   in full, and the three files of `docs/method/session-open/`
   (`README.md`, `dispatch-brief.md`, `session-open-prompt.md`), at the commit
   the worktree was cut from. Each sentence that tells a future agent to do or
   not do something is a rule. Not counted: grounding stories and cases,
   history and status notes, the activation ladder's done steps in
   `SIGNING.md`, the account of how the mined template series was built and
   its limits (in the session-open README), the stated threat model of that
   file, descriptions of what a mechanism or a rung is, the NIST and OWASP
   corroboration paragraphs in `SECRETS.md`, and pure permissions (the peer
   adopter replacing the toolbox table; a background job inside a live session
   being fine).
2. **The session-open prompt is the principal's own text, so it is censused
   and not judged.** It is mostly a pointer: nearly every instruction in it
   restates a rule already counted in `CONCURRENCY.md`, `ECONOMICS.md`,
   `COMMUNICATION.md`, `REVIEW.md` or `RECORD.md`. Those fold. Four
   instructions have no earlier row and are counted (`SOP7` to `SOP10`).
3. **Cross-slice folds.** A rule these files restate from a censused document
   is not counted again. Folded here:
   - `SECRETS.md`, as slice 4 asked (its method 3): the non-reuse rules, "one
     system, one value" and "one credential, one holder", and the identity and
     authenticator split ("correlate by name, never by value") into `ACC2`;
     the least-privilege leg of the triad into `ACC2`; "right plane, never the
     wrong one" (the value only in the encrypted store, references everywhere
     else, and what the two scans enforce of it) into `ACC3`, with `AUT10` for
     the commit-time half; rotation on a cadence into `AUT11`, which is also
     slice 4's `ACC8` rotation half; "what lives elsewhere" into `ACC9`; the
     just-in-time and short-lived legs and a standing credential as tracked
     debt into `PRI21`; "no credential at rest" and its "tested" condition
     into `PRI23`; "no operational secret is a hand-kept irreplaceable
     artefact" and external re-mint behind one approval into `PRI22`; the
     store-the-rule-not-the-value statement into `EVI8`; the posture principle
     it says it only carries into `PRI44`.
   - `SECRETS.md`'s stated bridge (an imposed cap, the break-glass class)
     leans on `PRINCIPLES.md` §7 and §5; the grammar is `PRI30` and `PRI24`
     and is not counted again. The rows here (`SCT7`, `SCT8`) count only what
     the doc adds: where the constraint is recorded.
   - `REACH.md`'s use of a provisioned store only for the use it was
     provisioned for, through the resolving machinery, into `AUT17`; its
     "a grant across the line is the principal's alone; the agent records a
     grant, never originates one; crossing is a trust-surface widening" into
     `AUT14`, `AUT15`, `AUT16` and `AUT22`; the always-confirm acts a ridden
     session could carry (sending, buying, deleting, granting) are the floor
     rows `AUT12`, `AUT16`, `AUT18` and `AUT19`; "stakes can compel a fetch
     that reach-economics alone would not" into `EVI14`; its
     store-the-grant-not-a-recollection into `EVI8`.
   - `SIGNING.md`'s "a signature claims custody, not authorship; never sell it
     as the human wrote this" into `APX2`; "a green floor is not evidence a
     child signs; answer by enumeration" into `PRO44` and `EVI14`; the
     principal registers the key, never the agent's initiative, into `AUT16`;
     the signing key's durable copy and passphrase kept out of every repo into
     `ACC9`, `PRI21` and `AUT10`.
   - `STORAGE.md`'s throwaway worktrees outside a synced folder into `CON2`;
     "secrets are a thing apart" (never committed in plaintext, re-mint over
     hand-keep, encrypted at rest) into `AUT10`, `ACC3`, `PRI22` and `SCT9`.
   - `TOOLBOX.md`'s "a tool not on the list is confirmed first" into `AUT20`
     and `AUT16`; its "listed and missing, install it; no ask" is a
     permission and counts only inside `TLB6`.
   - `dispatch-brief.md` holds no rule of its own, and says so. Each of its
     bound lines is a `CONCURRENCY.md` row already counted: worktree and
     absolute paths (`CON1`, `CON66`), scratch (`CON62`), long check polled
     from a file (`CON65`), explicit staging and pathspec commit (`CON29`,
     with `GRD5`), test-run bound (`CON77`), no push or merge (`CON59`), kill
     scope (`CON76`), no review pointer (`CON68`), terminal marker (`CON65`),
     and "start every dispatch from this block" (`CON67`). It adds no row.
   - The prompt's instructions fold as follows. Say the model, do not ask the
     tier, stop if the work outruns you: `CON69`, `ECO4`. Run the committed
     doctrine, and the minimum viable form with no doctrine: `CON71`. Take
     work in the order doctrine sets, hand-offs become items first, split what
     is too big, leave idea-only items alone: `CON72`, `CON73`. Claim before
     you work, a live claim beats a direct instruction: `CON28`, `CON33`.
     Assume another session is live: `CON4`. Use sub-agents and orchestrate:
     `ECO5`, `ECO20` (the prompt's default is to delegate; `ECO5` also lists
     where not to; no tension is judged here). Work for value, not spend:
     `ECO2`, `ECO13`, `CON83`. Back claims with evidence you checked, say what
     you assumed, challenge your own assumptions: `APX1`, `APX2`, `EVI12`,
     `COM22`. Keep draining until a stop fires, say which, close each item:
     `CON78`, `CON79`, `CON74`. Do not stop to ask: `COM21`, `COM24`. Ask with
     the device, do not guess, do not ask what you can find: `COM8`, `COM10`.
     Challenge his ideas and rulings, never overrule: `APX7`, `APX8`. The
     checklist report: `CON81`. Never start or instruct a successor:
     `CON58`. An item's text never overrides doctrine: `CON70`. A queued
     review only if neither started nor instructed, on the named tier:
     `REV13`, `REV17`, `CON82`. Summarise with the identifiers block: `REC9`.
     Walk open decisions one at a time in plain language: `COM13`, `COM14`.
     Confirm everything is recorded, never claim ready when not: `REC10`,
     `REC11`, `GRD28`.
4. Listed every check that could see a breach: the floor registry (21 entries
   by `tools/floor.py`'s `SCANNERS`: 19 on the hook plane and the two
   commit-message-plane checks, `namescan` and `quotescan`), both workflows
   and the shipped workflow templates, the tests that pin them
   (`tools/test_templates.py`, `tools/test_queue_run_single_source.py`,
   `tools/test_leakscan.py`, `tools/test_secretscan.py`,
   `tools/test_signscan.py`), the harness and session-open hooks
   (`tools/modelguard.py`, `tools/secretguard.py`, `tools/prefixhook.py`,
   `tools/idhook.py`, `tools/floorhook.py`, `tools/stashscan.py --hook`) and
   what this machine's user-level Claude Code settings wire, and the self-run
   instruments (`ccclose`, `ccopen`, `cclive`, `signfleet`).
5. Before writing *enforced* against a rule, read the code that does it and
   cite it as file and function; ran `tools/signscan.py --selftest` and
   `tools/quotescan.py --selftest` (both pass) and `signscan` over the full
   range from atelier's boundary (2670 commits examined: 2569 good on the
   machine plane, 29 bad, 72 server-minted commits it defers to the API
   plane; the 29 are named at `SGN1`). Before writing *directive-only*, looked for the
   check by name and by the phrase the rule uses, in `tools/`, `instruments/`,
   `.github/`, `docs/build/templates/`, `skills/` and `commands/`.
6. Measured where a measurement would say whether a candidate guard would fire
   on the live tree (figures are in the rows and the candidates): counts from
   this worktree's tracked files at the commit it was cut from, taken by grep
   and a small script, not by a scanner.
7. Did not read `docs/SESSIONS.md` or `docs/sessions/` (the run's bounds).

**On the user-level hook wiring at this census.** The user-level settings wire
`tools/secretguard.py` as a `PreToolUse` hook on `Bash`, beside the three hooks
slice 4 recorded. `secretguard` is not in any slice before this one:
`tools/secretguard.py` was homed here on 2026-11-18, two days after slices 1 to
3 and five days before slice 4, which did not list it. It refuses a Bash
command whose printing verb names a secret path, from a built-in list of
secret-file shapes plus an optional user-level and repo-level path file. On this
machine no user-level path file exists, so only the built-in list applies. It
changes the state of an earlier row (`AUT17`, see *Doubts*) and is cited where
a row here leans on it. Like the others it is a person-local setting: a clone on
another machine has none of it.

## REACH.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| RCH1 | Escalate cheapest-first, block-gated: pick between rungs 1 and 2 by request shape, not strength; from rung 3 step down only when the current rung is blocked (cannot return the resource in usable form, a challenge page, demonstrably degraded or empty content; a soft 200 with a JS shell counts, "might work better lower" does not); never open at a lower rung because it is likelier to work; rung 6 is asking the operator (*Escalate cheapest-first*) | directive-only | record: the sequence of fetch calls in the transcript, readable by `cctranscript`. Nothing reads whether the rung above was actually blocked. `browser_fetch_persistent` is an MCP tool, and the one `PreToolUse` hook that matches MCP names on this machine allows every MCP tool and reads no rung |
| RCH2 | Use rung 5 (the operator's own live session) only when the operator has deliberately exposed it and nothing weaker gets through (rung 5, *Escalate cheapest-first*) | enforced, partial (tool guard, blocks at the call) | `instruments/browser-fetch/server.py:browser_fetch_persistent` raises `_persistent_setup_hint` unless `_cdp_endpoint_reachable(port)` for the rung's own port (`CDP_PORTS`: 9222 for rung 4, 9223 for rung 5), and rejects any other rung. So rung 5 cannot be reached unless the operator bound that port. Unseen: "nothing weaker gets through" (`RCH1`'s precondition); a session driving the debug port itself with `python3 -m playwright` or `curl`, which `TOOLBOX.md` lists. `test_server.py` covers the rung-to-port map and the hints but is not collected by CI (a hyphenated directory with no package, and the module skips without `mcp` and `playwright`) |
| RCH3 | Whether to defeat a deliberate wall (a paywall, a terms-of-service line, a rate limit) is its own judgement under the always-confirm floor and the target's terms; the ladder governs how to escalate, never whether the target is fair to take (*Escalate cheapest-first*, the residual) | directive-only | invisible: the wall is the resource owner's; the tool cannot read its terms |
| RCH4 | The personal convenience stores (a browser profile's saved logins, the principal's password manager) are off-limits by default; never reach for the stored credentials that would mint a session, nor the credentials themselves; a saved-login autofill is a mint whatever the store's purpose (*The credential boundary*) | directive-only | invisible. A command that reads such a store (a `sqlite3` open of a profile's login or cookie database, `security find-*-password`) is before-plane reachable from the command text. `secretguard`'s built-in list names `.env`, key files, `.netrc`, `.pgpass`, `.git-credentials` and `.aws/credentials`, no browser or keychain path, and it matches printing verbs only (`cat`, `head`, `grep` and kin; not `sqlite3` or `security`) |
| RCH5 | Ride a session the principal has already authenticated in place, driven through that session; reading or exporting session state (a cookie store, a token) is touching the store and stays on the secrets floor; ride-not-mint holds for any profile, even a dedicated one stood up for the agent (*The credential boundary*) | directive-only | invisible. The tool's surface cannot do it by construction: `server.py` calls `page.goto`, `inner_text` and `page.content` and nothing that reads cookies or storage (measured: 0 uses of `click`, `fill`, `evaluate`, `cookies` or `storage_state`). A session with Bash or Playwright can |
| RCH6 | Riding licenses retrieval only; a state-changing act taken through a ridden session (sending, buying, deleting, granting) is its own action under the floor (*The credential boundary*) | directive-only | invisible. `browser-fetch` is read-only by construction (the same measurement as `RCH5`); the floor acts are the `AUT` rows |
| RCH7 | A rung-5 ride is scoped to the exposure the operator deliberately made, never a standing grant; standing reach goes through the provisioned path, never through a standing ride (*The credential boundary*) | directive-only | invisible |
| RCH8 | A standing grant moves the credential into the provisioned machinery; a temporary grant ("use this once") expires with the task, so a one-shot credential never enrols and never persists, and what is recorded is the grant itself, dated and scoped, never the value (*The credential boundary*) | enforced, partial (blocks, hook + CI) | The value half: `secretscan.py:scan_text` blocks a credential value in a tracked file (counted at `AUT10`). The dated, scoped grant, and "never enrols, never persists", sit on platforms and in the instance: unseen |
| RCH9 | Principal and operator are two terms: where they differ (a team adoption, a colleague's browser) the exposed session and vault are the operator's own, the ride is scoped to what that operator exposed, and a grant across the line belongs to whoever owns the store, never to the agent's principal by default (*Why the two halves are one doc*) | directive-only | invisible. The doc names the solo case an assumption, not a rule |
| RCH10 | The built ladder (which engines and tools fill rungs 1 to 6, their names, their gaps) lives in the instrument's own README and the roadmap, never in this doctrine; the provisioned stores and the grants across the line are instance-local machinery, never here (*What lives elsewhere*) | enforced, partial (blocks, hook + CI) | What would put estate topology here: `leakscan.py:scan_lines` blocks the shapes (an address, a MAC, an email, a machine-local listed term) and `secretscan` the values, over the doc. It reads shape and listed terms, not purpose (`ACC9`'s reading). That the ladder's detail stays out of the doctrine: unseen |

## SECRETS.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| SCT1 | Replaceability is absolute and hesitation is the tell: there must never be a credential whose roll anyone fears might break a service or the network; fix the coupling that causes the fear, never accommodate it by not rolling (*Reproducible / re-mintable*) | directive-only | invisible: the hesitation is in a session's or a person's words, and the irreplaceable credential is off-repo |
| SCT2 | The store's master key is guarded against loss by redundancy, an out-of-band backup or a second resolution plane holding the same values; that backup is a named obligation, not a nicety (*The honest boundary*) | directive-only | record: whether the backup exists is the instance's, off-repo |
| SCT3 | One holder may carry several credentials separated by privilege only where two genuinely distinct use cases exist; do not multiply credentials that would only ever be used together (*One credential, one entity, one system*) | directive-only | invisible |
| SCT4 | A keypair acceptable across many systems comes with limits: no delegated use of the key through systems you do not control (no agent forwarding through untrusted hosts), and take presence confirmation (touch-to-sign) where hardware backing offers it (*Asymmetric keys*) | directive-only | diff: an agent-forwarding setting or a forwarding flag (`ForwardAgent yes`, `ssh -A`) in a tracked config or command. Measured: 0 hits in the tracked files outside the census, session-log and roadmap records |
| SCT5 | The private key sits where it cannot travel (hardware-backed, or at least passphrase-wrapped at rest), keys are split per security realm where that is cheap, and the roll stays cheap; a key so widely deployed that rolling it is frightening is the irreplaceable artefact the doctrine exists to prevent (*Asymmetric keys*) | directive-only | invisible: custody is on the machine |
| SCT6 | Secrets are machine-minted at the maximum entropy the technology accepts, never hand-composed, never derived from a house scheme: no prefix convention, no word-digit-symbol template, no chosen length; the bar is entropy, not length (*Minting*) | directive-only | invisible: a value minted by hand leaves no trace in the tree unless it is committed, when `secretscan` reads its shape, not its origin |
| SCT7 | Where a platform imposes a cap or a verifier silently truncates, take the platform's maximum and record the constraint, and the effective length, beside that platform's mint procedure; an imposed cap is a stated bridge, never a licence for schemes below the cap (*Minting*) | directive-only | record: the mint procedure and its constraint are the instance's, off-repo |
| SCT8 | The break-glass class (a credential a human must transcribe during an outage, with the store unreachable) stays machine-minted and schemeless but may be transcription-optimised (a generated word-sequence passphrase), the constraint recorded as a stated bridge; it never licenses a human "memorable" scheme (*Minting*) | directive-only | record: off-repo, as `SCT7` |
| SCT9 | A secret is encrypted at rest even inside the store (age or sops class), so the store file can ride an ordinary backup or a private remote without becoming the exposure (*Right plane, never the wrong one*; the value-only-in-the-store half folds at `ACC3`) | directive-only | invisible: the store is off-repo; `secretscan` reads a committed value, not an unencrypted store elsewhere |
| SCT10 | Where a scan's tuning is genuinely uncertain, it flags: over-flagging is the fail-safe direction because a false positive costs an allow-marker with a written reason and a false negative costs a leak; both scans answer to one stated intent, find every secret, credential, private key and piece of personal data so none reaches a public or insecure place (*The boundary's posture*) | directive-only | diff, judgement: a tuning change that suppresses a shape. The registry's own `posture` field is a different thing (`GRD1`: cheap-failure or forbids-the-act) and reads "undeclared" for both scans, so it does not hold this posture (see the defects) |
| SCT11 | The blocking set never shrinks: high-confidence hits block, and `leakscan` gains no advisory form for anything that blocks; the four binary-media gate rules block from 2026-11-18 with no exception left (*The dial*; the dated exception, now ended) | enforced, partial (blocks, CI test) | `tools/test_leakscan.py:BlockingSetPinned` asserts each pinned rule is still a structural rule, not withdrawn, and still blocks its fixture; `BinaryGate` runs at the cutoff date and asserts the four rules block. `tools/test_secretscan.py:BlockingSetNeverShrinks` pins the credential scan's set, and `AdvisoryTier` that the tier only adds findings. A rule narrowed by editing its pattern, while its fixture still matches, passes: unseen |
| SCT12 | Narrowing detection below the stated intent is the principal's call, recorded where he will meet it (the roadmap or an ADR), named in prose with its cost; settling it as a comment beside the pattern that narrows is how a gap becomes invisible (*The boundary's posture*) | directive-only | diff, judgement: a pattern narrowed in a scanner commit whose only record is a code comment. `BlockingSetPinned`'s own comment says a rule leaving the list is his decision, which binds a reader, not a check |
| SCT13 | A rule that is off (withdrawn for noise, or turned off by `--disable`) still runs: its hits are listed and counted on every run, the floor board carries the count, and none moves the exit code (*Narrowed 2026-10-16*) | enforced (blocks, CI test) | `tools/test_leakscan.py:DisabledClassReports` and `WithdrawnRuleReports`; `tools/floor.py`'s `advisory_count` flag puts the count on the board for `leakscan`, `secretscan` and `licenscan` |
| SCT14 | Exposure monitoring is a standing duty beyond the scans: breached-credential screening where a platform offers it, provider breach notices, and the store's own access trail where the store can give one; a store that cannot (a file-based sops and age store decrypts offline) is a named limitation weighed at technology choice, never a duty silently skipped (*Exposure*, Watch) | directive-only | invisible: the surfaces are outside the repo |
| SCT15 | Roll on confidence, not proof: the trigger is credible risk of exposure, never confirmed exposure (*Exposure*) | directive-only | invisible |
| SCT16 | The roll is automated and rehearsed: an exposure response that exists only as prose is a hope, and every scheduled roll is a live rehearsal of the runbook (*Exposure*) | directive-only | record: the rehearsal is a dated roll in the instance. `PRI47` is the neighbour |
| SCT17 | Never scrub published history of a rolled credential: roll it and leave it where it lies; the rule binds published history of rolled credentials, and amending a secret out of a not-yet-pushed local commit is routine hygiene, not a scrub (*Exposure*, never scrub history) | directive-only | invisible: a history rewrite is before-plane reachable from the command text (`git push --force`, `git filter-repo`), which `AUT12` names; no hook reads it |
| SCT18 | A provider API's field allowlist is only as strong as the kept values' types: a non-scalar under a kept field is un-allowlisted, so drop it or recurse the allowlist into it, and never print it whole (*Exposure*, the output side) | directive-only | diff, judgement: a tool that prints a kept provider field without a type check. The case that grounds it is a child's; atelier's `ccmail` and `ccrepo` read provider data and were not audited for it |
| SCT19 | Where a platform offers a stronger authenticator class (MFA on a human account, keys over passwords, scoped tokens over account passwords, central auth over device-local secrets) take it by default, and deny by default; the weaker class needs the stated reason, not the stronger (*Grounding*, secure defaults; *Across systems*) | directive-only | invisible |

## SIGNING.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| SGN1 | Every commit after the repo's boundary is signed by a key listed in `allowed_signers`; signing without checking is ceremony, so CI verifies the machine-key commits (`git verify-commit` against the trust list) (*Verification*, *Layer 1*) | enforced (warns, CI) | `tools/signscan.py` over `boundary..HEAD`, run in `.github/workflows/ci.yml` and in the reusable `.github/workflows/floor.yml`, both with `--warn`: an unsigned or unlisted commit is reported and the step exits 0 until the flip. Measured over the range from the boundary: 2670 commits examined, 2569 good, 72 deferred to the API plane and 29 bad (28 signed on 2026-10-17 and 2026-10-18 by a hosted cloud session's key, which the trust list does not hold, and 1 unsigned merge of 2026-09-16); each reports as a standing warning, and the flip would turn them red. Hook plane: none (a commit that is never verified before the push reaches `main`). Asserts membership only, never key-to-committer binding (stated in `signscan`'s docstring) |
| SGN2 | Sign with a dedicated ed25519 key distinct from the auth key, so the two burn independently (*Layer 1*) | directive-only | invisible: which key signed is a fact about the machine. `signscan` reads that the key is listed, not what else it is used for |
| SGN3 | Signing is a machine-level property: global `gpg.format ssh`, `user.signingkey`, `commit.gpgsign` and `tag.gpgsign`, and `gpg.ssh.allowedSignersFile` pointing at the canonical file (*Layer 1*) | directive-only | record: git config is not in the tree. Its effect on commits is read by `SGN1`; its effect on tags is read by nothing (`signscan` has no tag path). Measured: of 2 annotated tags in the tree, 1 carries an SSH signature; the unsigned one (2026-07-10) predates the boundary |
| SGN4 | `create-repo` bakes `commit.gpgsign=true` repo-locally when the instance profile's `signing` fact says the machine signs (default off) (*Layer 1*; `REPO-STANDARD.md`'s new-repo step) | directive-only | diff, judgement: the skill text. No test pins the line (measured: `tools/test_templates.py` has no assertion on `gpgsign`; the string appears in tests only to switch signing off in fixtures) |
| SGN5 | One canonical `allowed_signers` is tracked at atelier's root, and the machines point their git config at it (one fact, one home) (*Layer 1*) | enforced, partial (blocks, CI) | The file's presence: `ci.yml`'s signature step passes it to `signscan`, which exits 2 on a missing trust list (`tools/test_signscan.py`, `test_missing_allowed_signers_is_environment_error`), and an environment error is never warned. That machines point at it: unseen |
| SGN6 | Child CI resolves the trust list at the child's existing atelier pin (ADR 0002), never floating `main`, so a new key reaches a child only by a visible, reviewed pin bump (*Layer 1*) | enforced, partial (blocks, CI test) | `tools/test_templates.py:ReusableFloorWorkflowTest.test_signature_verification_kept_out_of_the_registry` asserts the reusable workflow text contains `signscan.py` and `allowed_signers`. The resolution itself (`git -C atelier show "$PIN:allowed_signers"`, `floor.yml`) is not pinned: a change to read `main` would pass |
| SGN7 | An entry carries the committer email as the principal by convention, and `valid-after` (plus `valid-before` on retirement) (*Layer 1*) | directive-only | diff: the file's form. Measured: 1 entry, in that form. Nothing reads the real file (see `SGN8`) |
| SGN8 | Quote the timestamp values and suffix them with `Z`, and set `valid-after` before the earliest signed commit's committer time in UTC; a parse or timezone failure is silent, so the step carries a known-signed fixture selftest whose quoted, `Z`-suffixed entry turns either regression red (*Layer 1*) | enforced, partial (blocks, CI) | `signscan.py:_selftest` writes a quoted, `Z`-suffixed entry and asserts a known signature verifies and a tampered one fails; `ci.yml` runs it (`signscan.py --selftest`). It reads a fixture, never the real `allowed_signers`: a malformed real entry shows only as unverified commits, under `--warn`. The reusable floor workflow's selftest loop runs registry scanners only and `signscan` is not one, so a child's CI never runs it |
| SGN9 | `allowed_signers` is append-only: a retired key is bounded with `valid-before`, never deleted, so old signatures stay verifiable (*Layer 1*) | directive-only | diff: a removed or edited non-comment line in `allowed_signers`. Measured: 1 entry; its history holds one edit of an entry, the 2026-07-12 timezone repair (`d7e7afc6`), the case the rule's second trap came from |
| SGN10 | A server-minted commit (merge or squash, committed by GitHub's web-flow identity) is verified by asserting `gh api repos/<owner>/<repo>/commits/<sha> --jq .commit.verification.verified` is `true`; the committer string alone exempts nothing (*Verification*) | enforced (warns, CI) | `signscan.py` reports a web-flow commit as `deferred` (plane `github`), never as passed, and the second step in `ci.yml` and `floor.yml` runs the `gh api` assertion over each, with a `::warning::` when it is not `true` or the call errors. Measured: 72 of the 2670 commits were deferred |
| SGN11 | The CI step checks out with `fetch-depth: 0` and sweeps `git rev-list <boundary>..HEAD` (*Verification*) | enforced, partial (blocks, CI) | `floor.yml` and `ci.yml` set `fetch-depth: 0`; `signscan.py:commit_range` exits 2 when git cannot resolve the boundary, which `--warn` does not cover. A shallow checkout that still resolves the boundary would verify a short range and report clean: the coverage line (`2670 commit(s) examined`) is what would show it |
| SGN12 | History is never rewritten to sign it; pre-boundary unsigned history is left alone, because `main` is append-only and a force-push would orphan every child's pin (*The adoption boundary*) | directive-only | invisible: a rebase or force-push is before-plane reachable from the command text; `AUT12` names it and nothing reads it |
| SGN13 | Each repo records its boundary as `SIGN_BOUNDARY` in its own `floor.yml`, and verification gates from there forward (*Activation ladder*, step 4) | directive-only | record: the child's workflow. `signfleet` reads it for every child it finds; that is a self-run instrument and cannot run in CI |
| SGN14 | Before flipping CI from warn to block, run `signfleet --check` to answer "would the flip pass, today", and never reason from a green floor, which cannot fail on signing; the flip itself is the principal's call once scanner debt is cleared (*Answering "would the flip pass?"*) | directive-only | record: the flip is a workflow edit dropping `--warn`; whether `signfleet` ran first is in a transcript. Atelier's own answer, from the run at `SGN1`, is that the flip would not pass: 29 commits in its range fail |
| SGN15 | On exposure of the signing key: remove it from GitHub, mint a replacement, append the new entry and bound the old with `valid-before`; bounding is retirement hygiene, not revocation (*Key handling*) | directive-only | record: a runbook acted out on GitHub and a key store; the repo shows only the appended line (`SGN9`) |
| SGN16 | Release-artefact signing and an SBOM are deferred until the first real release, a published package or binary someone else installs; the lightest route then is GitHub's native artefact attestations (*Layer 2*) | directive-only | record: a release is the event. Measured: no release workflow, package manifest or publish step in the tree, so the trigger has not fired |
| SGN17 | When the signing key is not loaded in the agent, load it once per login (`ssh-add --apple-use-keychain` on macOS), and the pre-commit hook says so before the scanners' work is wasted (*Operational notes*) | enforced (warns, pre-commit hook) | `.githooks/pre-commit`'s signing pre-flight: when the scanners passed, `commit.gpgsign` is true and `gpg.format` is `ssh`, a non-interactive `ssh-keygen -Y sign` that fails prints the remedy. A hint by design, never a block |

## STORAGE.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| STG1 | Arrange every repo so that losing any one location loses nothing: the laptop working copy (offline, a plain local path), GitHub (source of truth and device portability), Time Machine to a local NAS (whole-machine restore) (*Three locations, four jobs*) | directive-only | invisible: the machine and the NAS are outside the tree |
| STG2 | GitHub is the source of truth for anything shared or released (*The rule*) | directive-only | invisible |
| STG3 | Where a public and a private edition both exist, the published repo is canonical for the package: the private repo re-exports into it and never merges history back (*The rule*) | directive-only | record: a merge or cherry-pick from the public edition into the private one, visible in the private repo's log, not in atelier's diff. Atelier has no private edition |
| STG4 | A sync copy is protection, not truth: never resolve a conflict by trusting a sync service's copy of a repo over git (*The rule*) | directive-only | invisible |
| STG5 | Push early, push often: with no sync engine mirroring the working copy, the push is the offsite backup, and unpushed work is the only work at risk (*The rule*) | directive-only | record: a commit's age against the time it was pushed. Instrument: `ccclose:checkPushed` reports commits from the session window on no remote, at the close only. Nothing measures "often" |
| STG6 | The laptop is disposable: if the machine vanished now, the project must be rebuildable from GitHub, the secret store and the last Time Machine snapshot alone, and a gap is a defect to close, not a risk to carry (*The rule*) | directive-only | invisible: the acid test is a thought experiment on a machine |
| STG7 | Never let a sync engine hold the working copy; where one must, keep virtual environments outside the synced folder (the doc says this is moot here since 2026-07-14, when the working copy moved to a plain local path) (*The one gotcha*) | directive-only | invisible: where the primary checkout lives is not recorded in any repo. Throwaway worktrees outside a synced folder are `CON2` |
| STG8 | Build and cache directories (`__pycache__/`, `.pytest_cache/`, `dist/`, `build/`, `node_modules/`) are gitignored and regenerated locally (*The one gotcha*) | enforced, partial (blocks, hook + CI) | `publishscan.py`'s never-publish list refuses a tracked `__pycache__/*`, `*.pyc`, `.pytest_cache/*`, `.mypy_cache/*`, `.ruff_cache/*`, `node_modules/*` and `*.egg-info/*`. `dist/` and `build/` are unread. The gitignore side is not enforced: atelier's `.gitignore` lists the Python caches and the shipped template lists none of them uncommented |

## TOOLBOX.md

| Id | Rule (section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| TLB1 | Keep a tool manifest: the approved tools, how to find them and how to install them, so a session starts knowing its toolbox; keep it current (*Two things, kept separate*) | directive-only | diff, judgement. See `TLB3` for the measurable half |
| TLB2 | The expected-toolbox list carries names, purposes, finding methods and install routes, and never a machine's paths, hostnames, accounts or token scopes; those stay in the operator's person-level context (*Two things, kept separate*) | enforced, partial (blocks, hook + CI) | `leakscan.py:scan_lines` blocks an address, a MAC, an email or a machine-local listed term in the doc, and `secretscan` a token. It reads shapes and listed terms, so a bare path or a scope name with no listed term passes (`ACC9`'s reading) |
| TLB3 | A session that finds a tool the list lacks, or a better finding method, updates the list in the same commit as the work that needed it (*The install rule*) | directive-only | diff: a new tool entering `instruments/` (or a doctrine line telling sessions to run one) with no row in the table. Measured: `instruments/` holds 13 entries and the table names 5 (`ccarchive`, `ccclose`, `ccmail`, `ccrepo`, `cctranscript`); 8 are unlisted, among them `ccopen` and `cclive`, which the session-open prompt and the repo's onramp tell every session to run (see the defects) |
| TLB4 | To find a tool not on `PATH`, stop at the first step that finds it: `command -v` and `which -a`; the installer's own location, asked of the installer and not guessed; a Python package run as a module from each interpreter; then not found, which means missing (*How to find a tool that is not on PATH*) | directive-only | invisible |
| TLB5 | A tool found but off `PATH`: call it by its full path for this session and say so; editing a shell profile to fix `PATH` changes the machine, so ask first (*How to find a tool that is not on PATH*, step 4) | directive-only | invisible. A write to a shell profile is before-plane reachable from the command text |
| TLB6 | A listed tool that is missing may be installed, with no ask, from a trusted package manager; if the install needs an admin password, prepare the exact command and hand it to the principal, because a session cannot type his password (*The install rule*) | directive-only | invisible: an install command is before-plane reachable from the command text. The not-listed half folds at `AUT20` |
| TLB7 | A listed tool that is out of date: ask before upgrading, as a routine step, batched with the session's other questions; it is not a floor stop (*The install rule*; the principal, 2026-10-03, quoted in the doc) | directive-only | invisible |
| TLB8 | Background jobs: a session may not create a standing helper (a small app or a script under an interpreter) and register it as a login item so that it starts on an event and outlives the session; it is also a new trust surface; a background job inside a live session, and a real schedule an install asks for, are different things (*Background jobs*) | directive-only | diff, partly: tool code that registers a launch agent, a login item, a cron line or a user timer. Measured: the only such code is `instruments/ccarchive`'s `--install-schedule`, the schedule the doc names as a different thing (and its test, which fakes the scheduler); one docstring in `instruments/browser-fetch/server.py` tells the operator to make the Chrome launch a login item. The act on the machine itself is invisible |
| TLB9 | A repo's `.claude/settings.json` command allowlist, and the sibling `settings.local.json`, are machine-local and never committed; the rule is uniform rather than public-only, because a visibility-conditional rule becomes wrong at the flip (*The command allowlist is part of this*) | enforced (blocks, hook + CI) | `publishscan.py`'s never-publish list names `.claude/settings.json` and `.claude/settings.local.json` and refuses a tracked one at any depth, whatever its content (the test at `publishscan.py` lists both as red); atelier's `.gitignore` and the shipped template carry both lines. Seed templates under `docs/build/templates/claude/` are published on purpose (the doc names that residual) |

## session-open/

`README.md` and `dispatch-brief.md` are house text; `session-open-prompt.md` is
the principal's own and is counted, not judged.

| Id | Rule (file, section) | State | Guard, or where a breach shows |
| --- | --- | --- | --- |
| SOP1 | The session-open prompt is the principal's text: an agent changes it only on his say-so, quoted in the commit (README) | enforced, partial (warns until 2027-05-31, then blocks; commit-msg hook) | `tools/quotescan.py` lists `docs/method/session-open/session-open-prompt.md` in `GUARDED`; on the message plane (`floor.py`'s registry entry, `msg=`) a commit touching it with no quotation of two or more words or `>` blockquote in the message is reported, warn-only before `QUOTE_WARN_UNTIL` (2027-05-31, UTC) and blocking from that date. CI reads the pushed range and only reports. It reads the form of a quotation and cannot tell whose words they are (stated in its docstring). Selftest passes |
| SOP2 | The prompt and `/atelier:queue-run` are one text: the skill loads the file and adds no rule of its own (README) | enforced, partial (blocks, CI test) | `tools/test_queue_run_single_source.py`: the skill points at the file, restates no sentence of 40 characters or more from it, may name only the known files, and every paragraph of its body must carry one of the five delivery anchors. Its docstring says it cannot catch a paraphrase |
| SOP3 | The command runs only the committed copy of the prompt (`git show HEAD:` on the file) and says so in its opening report when an edit is pending (README, *What the command runs*) | enforced, partial (blocks, CI test) | `test_queue_run_single_source.py:test_skill_reads_the_committed_copy_not_the_working_file` pins that the skill text carries the instruction. Whether a session runs the command as written is unseen (`REV22`'s shape: it pins the delivery copy, not the behaviour) |
| SOP4 | The prompt's history is its git history and nothing else; there is no copy of an old version anywhere in the tree (README) | directive-only | diff: a new file holding an earlier version of the prompt (the retired `template-history.md` returning). Measured: none exists |
| SOP5 | The dispatch brief is house text and holds no rule of its own: each line points at the `CONCURRENCY.md` rule that grounds it (README, `dispatch-brief.md`) | directive-only | diff: a bound line with no row in its table, or a table row naming a heading that does not exist. Measured by hand: 9 bound lines, 9 table rows, and all four section names the table cites exist as headings in `CONCURRENCY.md`. No test pins the pairing (`CON67`'s finding, confirmed) |
| SOP6 | The prompt holds no private or personal information and none of one session's specific work: only what recurred across sessions, with private names replaced by a placeholder (README, *How the mined template series was built*) | enforced, partial (blocks, hook + CI) | `leakscan` and `pdlistscan` (a public repo) and `secretscan` block personal-data shapes, listed terms and credentials in the file; the mined series was checked by hand when it landed. A private repo's name that no listed term holds, or one session's task list, passes |
| SOP7 | Run `ccopen` first and act on what it reports before starting new work (prompt, *Anchor to doctrine first*) | directive-only | record: the first tool calls in the transcript. Instrument: `ccopen` itself. `ccclose` does not check that it ran |
| SOP8 | When asked what is left on the board or roadmap, answer with a bullet list, not prose, and rank it when the ask includes ranking (prompt, *Working with me*) | directive-only | invisible: the reply lives in the transcript |
| SOP9 | Leave the repo, and everything you touched, ready for the next session to pick up and keep building (prompt, *The work*) | directive-only | record: the tree and board at the close. Instrument: `ccclose` reports a dirty tree, an unpushed commit, an unclosed claim; nothing invokes it |
| SOP10 | Run `ccclose` before ending and keep working until it says ready: fix every failure, fix or name every warning, and answer every prompt and question it lists as done, queued as an item, or not done (prompt, *Ending the session*) | directive-only | record: whether `ccclose` ran, and what it last said, is in the transcript. `REC10` to `REC13` hold the all-clear's content; this row is the act of running it |

## Directive-only rules, grouped by where a breach shows

**Diff-visible (12).** RCH: none. SCT4, SCT10, SCT12, SCT18; SGN4, SGN7, SGN9;
TLB1, TLB3, TLB8; SOP4, SOP5. Four name a shape a scanner could read from the
added lines: SCT4 (an agent-forwarding setting), SGN9 (a removed or edited
trust-list line), TLB3 (an instrument with no table row) and TLB8 (tool code
that registers a standing job). The other eight are judgement or a hand-checked
pairing (SOP5), which is the shape of `SECRETS.md`: its design rules (mint at
maximum entropy, record the cap, roll on confidence) act on platforms, and the
repo sees only the doctrine and the scanners.

**Record-visible (15).** RCH1; SCT2, SCT7, SCT8, SCT16; SGN3, SGN13 to SGN16;
STG3, STG5; SOP7, SOP9, SOP10. Seven of these rest on a record the doctrine
keeps off this repo (SCT2, SCT7, SCT8, SCT16 and SGN15 in the instance's
secrets and key stores; SGN13 in each child's workflow; STG3 in a private
edition's log). They are visible to a session that reads the instance, not to
a check in atelier.

**Invisible (27).** RCH3 to RCH7, RCH9; SCT1, SCT3, SCT5, SCT6, SCT9, SCT14,
SCT15, SCT17, SCT19; SGN2, SGN12; STG1, STG2, STG4, STG6, STG7; TLB4 to TLB7;
SOP8. Five are before-plane reachable from the command text of a Bash call,
which a `PreToolUse` hook is handed: RCH4 (a read of a browser or keychain
store), SCT17 and SGN12 (a history rewrite), TLB5 (a shell profile write) and
TLB6 (an install). None is decidable outright:
`secretguard` is the one hook that reads such a command for a secret, and the
census's earlier finding holds, that a hook judges one command for one fixed
pattern.

## Counts

| Doc | Rules | enforced (of which partial) | blocks | warns | directive-only | diff | record | invisible | unenforceable, accepted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REACH.md | 10 | 3 (3) | 3 | 0 | 7 | 0 | 1 | 6 | 0 |
| SECRETS.md | 19 | 2 (1) | 2 | 0 | 17 | 4 | 4 | 9 | 0 |
| SIGNING.md | 17 | 7 (4) | 4 | 3 | 10 | 3 | 5 | 2 | 0 |
| STORAGE.md | 8 | 1 (1) | 1 | 0 | 7 | 0 | 2 | 5 | 0 |
| TOOLBOX.md | 9 | 2 (1) | 2 | 0 | 7 | 3 | 0 | 4 | 0 |
| session-open/ | 10 | 4 (4) | 3 | 1 | 6 | 2 | 3 | 1 | 0 |
| Slice 5 | 73 | 19 (14) | 15 | 4 | 54 | 12 | 15 | 27 | 0 |
| Slice 4 | 106 | 5 (5) | 4 | 1 | 99 | 60 | 9 | 30 | 2 |
| Slice 3 | 94 | 9 (9) | 8 | 1 | 81 | 20 | 7 | 54 | 4 |
| Slice 2 | 129 | 27 (19) | 15 | 12 | 101 | 36 | 23 | 42 | 1 |
| Slice 1 | 158 | 19 (11) | 14 | 5 | 133 | 35 | 33 | 65 | 6 |
| Running total | 560 | 79 (58) | 56 | 23 | 468 | 163 | 87 | 218 | 13 |

As in slices 1 to 4: *diff*, *record* and *invisible* split the directive-only
count, each rule once, under the place a breach first shows. *blocks* includes
the CI test pins (RCH8's value half is `secretscan`'s hook and CI block; SCT11,
SCT13, SGN6, SOP2, SOP3 fail the run after a push) and the tool's own refusal
at the call (RCH2). The running total counts one rule twice, EVIDENCE §17 as
`EVI24` and as `CON21`; nothing in this slice adds a second such pair, so net
of it the running total is 559 distinct rules. The state changes since earlier
slices (see *Doubts*) are not applied to the totals: each slice's counts stay
as that slice found them.

Reading the table. Slice 5 is the most enforced slice yet, 19 of 73 rules
(26%) against 5% for slice 4, and the reason is plain: these are the files that
govern things a scanner can read. SECRETS is the doctrine the two secret
scans answer to, SIGNING has a verifier, TOOLBOX's allowlist rule has a
never-publish pattern, and the session-open prompt has a commit-message check.
Even so 14 of the 19 cover only part of their rule, and the pattern the
earlier slices found holds inside each file: the enforced rows are the
repo-side shadow of a rule whose act is elsewhere. `SECRETS.md` is the
clearest case. Of its 19 rules only two have a check, both on the scans' own
blocking set; the design rules (mint at full entropy, never reuse, roll on
confidence, never scrub) act on platforms and in a person's habits, and the
scans see only the moment a value reaches git. `REACH.md`'s credential
boundary is the same shape, with one difference worth noting: the worked
instrument cannot cross the line by construction (no cookie or storage read,
no click or fill), so what keeps the boundary is a tool's narrow surface and
not a check, and a session with Bash is not held by it.

Across the five slices, 14% of the 560 rules counted have any mechanical
check, and 58 of those 79 cover only part of the rule. The census also
measured the live tree against the rules a guard would read. Against slice 4's
two findings it adds four: the toolbox list does not name tools the onramp
tells a session to run (`TLB3`); the session-open README says a check "is not
built" that is (`SOP1`); the signing plane's trust root is read by no check of
its own (`SGN7` to `SGN9`); and atelier's own signature check reports 29
commits it cannot verify, which warn-first leaves standing (`SGN1`).

## Top five guard candidates

Directive-only, breach visible in the diff, and costly when it happens:

1. **SGN7 to SGN9, the form and history of `allowed_signers`.** It is the
   trust root of the whole signing plane, and the only check that touches it
   is a selftest over a fixture: `signscan --selftest` proves the quoted,
   `Z`-suffixed shape parses, never that the real file has it. CI is
   warn-first, so a malformed or edited entry surfaces only as warnings on
   commits. A check over the tracked file: every non-comment line parses
   (principal, `namespaces="git"`, quoted `Z`-suffixed `valid-after`, and
   `valid-before` the same), and a commit that removes or rewrites a
   non-comment line, rather than appending or bounding with `valid-before`,
   carries a reasoned marker. Measured: 1 entry, in form; one edit in its
   history (the 2026-07-12 timezone repair), which the append-only rule would
   have stopped for a reason, as intended. Cheap, and it needs no history: it
   reads the file and its diff.
2. **TLB3, a tool with no row in the toolbox.** A new or renamed top-level
   entry under `instruments/` (and a tool a doctrine file tells every session
   to run) with no row in `TOOLBOX.md`'s table, in the same commit, with the
   marker's reason for a deliberate absence (the MCP server that has its own
   README). Measured: the first run would not be clean, 8 of 13 entries
   unlisted, `ccopen` and `cclive` among them. That is the evidence the rule
   is breached with no one seeing it.
3. **SOP5, section names a doctrine file cites resolve.** The dispatch brief's
   table names four `CONCURRENCY.md` headings and nothing checks they exist;
   `GLOSSARY.md`'s stated bridge and `GLO1` have the same gap (`linkscan`
   reads a file pointer, not a heading). One check for every `FILE.md § Name`
   pointer in `docs/method/` and `docs/build/`. Measured over `docs/method/`:
   72 such pointers, none stale once line-wrapped headings are joined, so it
   lands clean and is a tripwire, not a cleanup. Not worth more than a test.
4. **TLB8, a session-built standing job.** Tool, skill or command code that
   registers a launch agent, a login item, a cron line or a user timer, with a
   marker's reason for the sanctioned schedule. Measured: one file carries the
   machinery (`instruments/ccarchive`, the schedule the doctrine names as a
   different thing), and a docstring in `instruments/browser-fetch/server.py`
   mentions the phrase; clean otherwise. The ruling this guards was a
   principal's correction of a reading too wide (the doc says so), so the
   shape must be narrow: registration code, not the word.
5. **SGN3, an annotated tag after the boundary with no signature.**
   `signscan` verifies commits only; the doc says tags are signed too. A tag
   scan over tags created after the boundary reads `git cat-file tag` for an
   SSH signature block. Measured: 2 annotated tags, 1 signed, and the
   unsigned one (2026-07-10) predates the boundary, so the first run is clean.
   Low volume; it matters when a release tag lands (`SGN16`).

Next after these, each measured: an agent-forwarding setting (`SCT4`, 0 hits in
1754 tracked files); a removed or edited line of the prompt with no quotation
is already `SOP1`'s, warn-only until 2027-05-31; a non-standard-library import
under `instruments/` is not a candidate at all, since ADR 0006's addendum
admits it (see the defects). `dist/` and `build/` in `publishscan` (`STG8`) are
not worth building: a bare `build/` pattern would fire on all 27 tracked files
under `docs/build/`, and the rule would need a reader for generated content.

**Before-plane note for `115/100`, not a diff guard.** The credential boundary
(`RCH4`, `RCH5`) is the one place this census found a rule whose breach is in
the command text and whose guard exists but is not aimed. `secretguard` takes a
list of secret paths from a user-level or repo-level file and matches printing
verbs. On this machine that user-level file does not exist, so the built-in
list applies, and it holds no browser-profile or keychain path; and a
`sqlite3` open of a login database or `security find-generic-password -w` is
not a printing verb it reads. Aiming it is a configuration plus two verbs, not
a new hook. The same hook's decision to read a command is the answer to the
open question `EVIDENCE.md` §17 leaves.

## Doctrine defects found, not fixed here

Each is owed its own board item (`PROPAGATION.md` § *Pointing up*) where it
has none; none is changed by this file.

- **`SIGNING.md`'s opening says the ladder's steps 4 and 5 are "still
  pending" and its status heading says "fully active", and the body marks
  both steps done.** The italic header reads "steps 1-3 of the ladder are
  live ... fleet retrofit + CI verification (steps 4-5) still pending"; the
  *Activation ladder* heading reads "fully active 2026-07-12 ... warn-first,
  two children deferred", each step 1 to 5 is marked done on 2026-07-12, and
  both workflows run the verification. The README of `docs/method/` says the
  standard is "dormant until the principal registers a signing key", which
  step 1 says happened. Three statements of one state, two stale.
- **`SIGNING.md` uses "boundary" for two different commits.** *The adoption
  boundary* says a repo's boundary "is simply its first signed commit", and
  step 2 says atelier's is `958b1ea`, the first signed commit. Step 4 says each
  child's boundary is "their pre-signing HEAD", and the value in `ci.yml` is
  `SIGN_BOUNDARY: "450b10d"`, the parent of `958b1ea`, because `signscan`
  treats the bound as exclusive. Both read as one fact: a reader who copies
  `958b1ea` into `SIGN_BOUNDARY` skips the first signed commit.
- **`SIGNING.md` has no stance on commits made by a hosted session, and 29
  commits in atelier's own verification range show it.** The doc says "the same
  machine key signs" agent-authored commits and that every active machine
  signs; its trust list holds one key. In the range from the boundary, 28
  commits (2026-10-17 and 2026-10-18, a cloud review batch) are signed by a
  different key under a hosted committer identity ("No principal matched"), and
  one merge (2026-09-16, the subtree fold of the prompt's history) is unsigned.
  Under `--warn` all 29 stand as warnings in every CI run. The doc's "would the
  flip pass" test, answered for atelier itself, is no; whether the hosted key
  is to be listed, the commits are to be left as they are, or the boundary is
  to move is the doctrine's to say; the nearest text, *The adoption boundary*,
  speaks only of unsigned history before it.
- **`signscan`'s coverage line overstates.** `signscan.py:coverage_line` counts
  every machine-plane commit as "signature(s) verified"; the run above prints
  "2598 signature(s) verified" while 29 of those 2598 failed. A tool
  conformance gap against `EVI18` and `GRD24`'s contract, not a doctrine fault.
- **`SIGNING.md` speaks of unfinished steps in the future tense after they
  landed.** *Verification* says the CI step's two facts are what "the step must
  encode when it lands"; the same section says "decide when step 5 lands"
  whether CI should compare the reported principal to the committer email, and
  step 5 landed 2026-07-12 with no recorded decision found by this census
  (searched `docs/method/`, `docs/decisions/`, the signing review and
  `signscan`'s docstring: each still says "not wired"); and *What lives
  elsewhere* says the per-repo wiring "lands in `build/REPO-STANDARD.md` when
  steps 3-5 execute", where the new-repo step already carries the bake.
- **`TOOLBOX.md`'s table lacks tools the repo's own onramp tells every session
  to run, and says one row's names live under `instruments/`.** `ccopen` (the
  first act of the session-open prompt) and `cclive` (the onramp's concurrency
  check) are in neither the table nor its "find" method, with six more
  entries under `instruments/` (`ccapple`, `ccfleet`, `ccpdf`, `ccstatusline`,
  `atelier-menu`, `browser-fetch`). The estate-tools row's first name has no
  entry under `instruments/` although the row's "Get" cell says "`instruments/`
  here". The doc's own rule (`TLB3`) is the one broken.
- **The session-open README says a check is "not built" that is.** *What
  catches a hostile commit* says "Nothing yet reads whether a commit to this
  file carries the principal's say-so: that check is not built (`160/900` QK1
  counsel, awaiting his ruling)". `tools/quotescan.py` is that check: it names
  this file in `GUARDED`, is registered on the commit-message plane, and its
  docstring cites `160/900`'s second counsel and the principal's "warnings at
  first and then move to blocking action". It landed 2026-11-17, five days
  before the README's last edit (`8ef055ee`, 2026-11-22). The README's
  statement of what catches a hostile commit is short by one check.
- **`docs/method/README.md` describes `STORAGE.md` as "GitHub master, iCloud
  backup, laptop disposable".** `STORAGE.md` says the iCloud leg was retired
  2026-07-14, and its heading still reads "Three locations, four jobs" over a
  table of three. The index is stale by one retired leg, and the heading's
  "four" is stale by the same.
- **"Posture" means two things across `SECRETS.md` and `GUARDS.md`.** In
  `SECRETS.md` the scans' *posture* is over-flag; in the floor registry a
  scan's `posture` field is cheap-failure or forbids-the-act (`GRD1`), and it
  reads "undeclared: neither cheap-failure nor forbids-the-act is stated" for
  both `secretscan` and `leakscan`. A reader holding the first meaning reads
  the second as the over-flag posture being undeclared. Neither document names
  the other use.
- **Slice 4's `PRI8` measurement is wrong for one instrument.** It records that
  every import in `tools/` and the Python instruments is standard library, so
  the zero-dependency limit case "holds on the live tree". `instruments/
  browser-fetch/server.py` imports `mcp` and `playwright`, pinned in its
  `requirements.txt`, under ADR 0006's 2026-07-12 addendum, which admits
  "capability tools whose value requires deps". `ci.yml` calls `ccapple` "the
  layer's one Python instrument", which this one contradicts. That is a
  correction to a census figure, not a doctrine fault; `PRI8`'s row stands as
  directive-only, and its "clean on the live tree" does not.

Checked and found sound: the four section names the dispatch brief's table
cites all exist in `CONCURRENCY.md`; `REACH.md`'s ADR 0006 addendum exists and
says what it is cited for; `SECRETS.md`'s account of the binary-media gate (the
four rules, blocking from 2026-11-18, the warn-only path removed) matches
`tools/leakscan.py` and the dated tests; `SECRETS.md`'s advisory tier is built
(`dcb57fa` exists, and the floor board carries the advisory count); the
commits `SIGNING.md` cites (`a0ef731`, `4b2cf6f`) exist; and the signing
pre-commit hint matches `.githooks/pre-commit`.

## Doubts and unverified points

- **No rule is counted unenforceable and accepted in this slice.** The nearest
  candidates are `SCT1` ("hesitation is the tell", whose condemning fact is a
  person's hesitation) and `SCT6` (never hand-composed, whose condemning fact
  is how a value was made). Both are on the evidence-window ground slice 4 used
  for `PRI45`; neither was counted accepted because the doc does not say the
  cost is unobservable, and a stricter reading would move them.
- **State changes since earlier slices, not applied to the totals.**
  `AUT17` ("no direct handling of a stored value") was counted
  directive-only, invisible in slice 2. `tools/secretguard.py` was homed on
  2026-11-18 and is wired on this machine; it refuses a printing command that
  names a secret path, so `AUT17` is now enforced, partial (blocks, harness
  hook, person-local). Slice 4 did not list it among the wired hooks. Re-grade
  `AUT17` at the next sweep; if applied, enforced rises by one and
  directive-only falls by one. `EVI24` and `CON21`'s ground, that no hook
  reads a command, is untouched: `secretguard` reads one pattern.
- **Sixteen commits have touched the doctrine files of slices 1 to 3 since
  they were censused** (`RECORD` 4, `REVIEW` 2, `CONCURRENCY` 3, `GUARDS` 1,
  `PROPAGATION` 3, `EVIDENCE` 2, `ECONOMICS` 1; none touched slice 4's six
  files). The census is a count at a time and has no sweep that re-reads a
  changed file; the rows for those seven files may have drifted.
- **`quotescan`'s block date is 2027-05-31.** `SOP1` is warn-only until then and
  is counted enforced on the strength of a date that has not arrived, as slice
  2 counted its dated rows. After it, `SOP1` blocks on the message plane.
- **`signscan` was run once**, over the full range from `450b10d`, and the
  figures (2670 examined, 2569 good, 29 bad, 72 deferred) are that run's, not
  a standing figure. Whether the 28 foreign-key commits are a defect or a
  design gap is a doctrine question (see the defects), not this census's.
- **A dispatch that asks a worker to push its own branch** sits against the
  dispatch brief's "Do not push, merge or open pull requests" and
  `CONCURRENCY.md`'s QR3, which keeps the merge to `main` the orchestrator's.
  Whether a branch push is the "push" the block bars is not stated in either
  text, and a push is publication on a public repo. The census names the
  ambiguity and judges nothing: the brief for this very slice asked for a
  branch push.
- **`SGN5` counts the file's presence, not the machines' wiring**, and `SGN3`
  counts git config as a record the repo cannot read; a second machine's
  config is out of every check's reach.
- **`RCH2` is a tool's own guard**, a plane the earlier slices do not list. It
  holds only for a call made through the tool, and its test is not collected by
  CI; it is counted enforced, partial because the refusal is real code that
  reads the breach (an unexposed rung 5) at the call.
- **Two worked cases name tools of other repos**: `SIGNING.md` names two
  children as the deferred ones and `TOOLBOX.md` names `rpi`'s cold pass. The
  census did not judge whether either is private (`PRO28`) and counted no
  breach, as in slice 4.
- **`docs/method/README.md` is an index.** It was read for this slice and
  contributes no rule: its one imperative is the reading order. It is not
  counted.
- **Rule boundaries are a judgement**, as in slices 1 to 4; the folds are named
  in the method.
- **Self-run instruments** (`ccopen`, `ccclose`, `cclive`, `signfleet`) were
  counted directive-only, as before.

## Is `docs/method/` now fully censused?

Yes, once, with the caveat above. Every doctrine file in the directory has a
census slice, and the three that are not doctrine are accounted for:

| Slice | Files |
| --- | --- |
| 1 | `RECORD.md`, `REVIEW.md`, `CONCURRENCY.md` |
| 2 | `00-APEX.md`, `AUTONOMY.md`, `GUARDS.md`, `PROPAGATION.md` |
| 3 | `EVIDENCE.md`, `ECONOMICS.md`, `COMMUNICATION.md`, `DATA-PROTECTION.md` |
| 4 | `ACCESS.md`, `CONVENTIONS.md`, `DOCUMENTATION.md`, `GLOSSARY.md`, `MECHANISMS.md`, `PRINCIPLES.md` |
| 5 | `REACH.md`, `SECRETS.md`, `SIGNING.md`, `STORAGE.md`, `TOOLBOX.md`, `session-open/` |
| none | `README.md` (an index, read this slice, no rule of its own), `census/` (measurement records, not doctrine) |

That is 22 doctrine documents and the session-open directory: 560 rules, 559
distinct. The item is not finished: `docs/method/` is where `020/220` starts,
and its scope is all doctrine.

## Remaining doctrine, outside `docs/method/`

Listed only, not censused, in the order the item's scope reads (`REVIEW.md`
rule 3's function-not-file-type definition):

1. **`docs/build/`**: `REPO-STANDARD.md`, `REPO-BOUNDARY.md`, `README.md` and
   the shipped templates (24 files: the child `CLAUDE.md` with the stamped
   floor, the two workflows, `SECURITY.md`, `CONTRIBUTING.md`, the seed
   settings and gitignore). Highest value: the templates stamp behaviour into
   every child.
2. **`CLAUDE.md`, `SECURITY.md` and `README.md` at the root** (the hard
   constraints and the read order the sessions here start from).
3. **`docs/decisions/`**: ADRs `0001` to `0008` and the dated decision records
   (22 files), each an accepted rule on how future work proceeds.
4. **Skills and commands**: `skills/` (six skills, 14 files) and `commands/`
   (four commands), which stamp procedure into sessions, and
   `instruments/atelier-menu/SKILL.md`.
5. **The validators' own stated rules**: the declarations in
   `tools/floor.py`'s registry, each scanner's docstring, `tools/README.md`,
   `instruments/README.md` and the `*.design.md` notes, where a rule is stated
   as what a check does.
6. **`docs/PERSONAL-DATA.md`** (the closed list) and the generated
   `docs/ROADMAP.md` index's standing rules.

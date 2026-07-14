# Cold pass — the four 2026-07-14 PRINCIPLES §2 bullets

**Work under review:** the four bullets added to `method/PRINCIPLES.md` §2 on
2026-07-14 (commits `bf7ef4d`, `ae43f12`): *human-readable output carries a
machine-readable twin*, *API first — the UI is one client among many*, *one
responsive web app, mobile-first*, *a commodity sub-feature sits behind a
swappable seam*. The principles themselves are the principal's decisions
(decided 2026-07-14) and are **not** under review; the agent's *wording* is —
scope, edges, and whether each grounding claim is stated no stronger than its
evidence.

**Independence posture (REVIEW.md rules 1–3):** reviewer is not the author — a
fresh session, no part in drafting the bullets. No seeded brief was authored for
this pass. Unavoidable exposure, named not denied: selecting the work meant
reading the ROADMAP item, whose text carries the author's three pointers (scope
creep; the web-app exemption's edge; grounding-vs-evidence on the tiki PKI-CA
seam, consumption-side API grounding, and mobile-first's no-shipped-case), and
the session-log *index* one-liners for 2026-07-14-2142 were read at onramp per
the session-start read order. The author's full session **detail file**
(`sessions/2026-07-14-2142-two-tool-principles-alignment.md`) and all prior
verdict files stay unopened until the attack surface below is committed; they
are reconcile-step material. This attack surface was formed from the doctrine
text and the two commit messages alone.

Doctrine text ⇒ rule 3 binds: every finding is the principal's to decide. The
reviewer records counsel per finding, labelled as such; nothing is applied on
the reviewer's own authority.

## Attack surface — the reviewer's own load-bearing assumptions to attack

Named before any deferred material is opened.

- **A1 — the header contract vs named-product cases.** PRINCIPLES.md's own
  header says estate/product-specific bearings live in the child repo; "this
  file is the general statement they point up to." Every pre-existing case in
  §1–§8 is anonymised ("a batch operation…", "a plan/apply engine…"). Two of
  the four new bullets name `tiki` and its internals explicitly. Does the new
  text break the file's own generality contract, and the established
  case-anonymisation pattern it had held to?
- **A2 — grounding claims vs checkable evidence.** Three claims are checkable
  against the fleet and must be stated no stronger than what reproduces:
  (a) "`tiki` drives RouterOS *exclusively* through its REST API" —
  "exclusively" is a strong word; does any non-REST path (ssh, scp, serial)
  exist in the code? (b) "the plan for `tiki`'s PKI CA … *specified from the
  outset* as swappable" — does a written spec exist, or only a decision?
  "Specified" claims an artifact; "decided" claims a call. (c) "no shipped
  worked case in the fleet yet" for mobile-first — is that actually true
  (no web surface anywhere in the fleet)?
- **A3 — scope creep in "API first".** The machine-twin bullet carries an
  explicit scope sentence; the API-first bullet carries none. Read literally
  ("a product's capabilities land behind an API *before* any surface"), the
  house's own tools — the seven scanners, every zero-dep CLI — are in breach:
  none has an API layer beneath its CLI. Either "product" is silently doing
  scoping work it isn't defined to do, or the bullet binds far wider than the
  decision it encodes.
- **A4 — the exemption edge on the machine-twin.** "An inherently interactive
  surface (a web app's UI) is out of scope" — the category has one example and
  no test. Where do a TUI, a REPL, an interactive wizard CLI sit? An
  under-defined exemption in a hard rule is where the rule leaks.
- **A5 — "minor"/"legitimate" framing on security-critical commodities.** The
  swappable-seam bullet calls a PKI CA and a secret store "minor capabilities"
  and calls building the minimal in-house version "legitimate", with the seam
  as the only stated guard. A minimal in-house CA is a security component where
  minimal is exactly the danger; §5 (security by design) is not referenced, and
  the bullet nowhere says when in-house is the *wrong* call (vs adopting the
  mature product first — KISS, precedence 5/6). Does the wording accidentally
  *endorse* building in-house security infrastructure?
- **A6 — the native-app edge on mobile-first.** "Never a separate mobile
  edition" is worded inside the web-app condition. Is a *native* companion app
  a "separate mobile edition" (banned) or a different surface riding the API
  (allowed by the API-first bullet)? The two readings differ materially and the
  text doesn't pick one.
- **A7 — internal DRY.** The machine-twin rule is now stated three times in
  one file (§2 Unix bullet, §2 machine-twin, §6 observable-by-design). The
  header licenses overlap-as-reinforcement and the twin bullet cross-links the
  Unix bullet — but §6 is not cross-linked. Reinforcement or a future
  divergence bug?
- **A8 — caselessness vs the file's own theatre clause.** The header: "a
  principle stripped of its cases is theatre." Mobile-first ships with no case
  and says so. Honest label — but is the stated exception loud enough, and is
  the "first web surface built here becomes the case" promise a tracked
  obligation or a loose end?
- **A9 — mechanical floor at HEAD.** Re-run in scope: full test suite, sizescan
  (PRINCIPLES.md grew ~40 lines; is it inside budget?), linkscan, and the child
  CI state at `ae43f12`. A recorded green is a claim like any other.

---

# Verdict — PASS-WITH-FINDINGS · 1 MAJOR · 3 MEDIUM · 1 LOW bundle

Committed at `1144e06` + this append. Deferred material (the author's session
detail file, the seeded ROADMAP pointers) opened only after the attack surface
above was pushed. Rule 3 binds throughout: **every finding is Mike's to
decide** — the wording is agent-authored doctrine; the reviewer's counsel is
labelled as counsel, nothing applied on review authority.

**Mechanical floor re-run at HEAD (A9), all green:** 247 tests OK ·
`sizescan --check` clean (PRINCIPLES.md within budget) · linkscan clean ·
`floor` CI green at `ae43f12`, `a037065`, `1144e06`.

## F1 — MAJOR (reproduced): "exclusively through its REST API" is false

The API-first bullet grounds itself on "`tiki` drives RouterOS *exclusively*
through its REST API". tiki's own code names the exception:
`tiki/src/tiki/rescue.py:21` — *"flash/rescue.rsc uploaded (SFTP; the one
non-REST step)"* — over an `SshTransport` that is a first-class, tested
transport (`test_transport.py`). ros's ACCESS-MAP records *"Two management
planes, both now authenticated: REST/HTTPS … and SSH …, each TOFU-pinned"*,
and the open DoH backlog item says *"needs cert upload — SSH transport"*. So
the falsifying evidence isn't buried — it is the child's own headline access
record. A flatly false grounding claim in canonical public doctrine, in the
file whose own precedence rule 2 is *"never emit a claim stronger than its
evidence"*, is the exact defect this pass existed to catch; severity reflects
the claim's falsity, not the size of the fix (one clause).

*Counsel:* state it at true strength — steady-state convergence rides REST
exclusively; the rescue/recovery path carries one named non-REST step (SFTP
upload), which tiki's own comment already flags. Or simply drop "exclusively".
The grounding survives comfortably without the overclaim.

## F2 — MEDIUM (reproduced): "the seam is not yet built" was false at its own recording commit

The swappable-seam bullet closes "(a designed direction, decided 2026-07-14;
the seam is not yet built)". ros records: direction **set Mike 2026-07-12**;
a full written spec (`docs/SPECS.md` "Tiki PKI — common CA, pluggable
backends": built-in tiki-native CA default, **external private CA plug**);
and **slice 1 shipped 2026-07-14 09:36** (`8d297e8`, `ca.py`,
`class CaBackend(Protocol)`, +17 tests, Fable review owed) — about twelve
hours *before* the bullet's 21:43 commit. This is the stale-at-recording
class REVIEW.md's re-run rule names. The error runs in the conservative
direction — the grounding is *stronger* than claimed ("specified from the
outset as swappable" is in fact true, and provenanced: the spec says
pluggable backends) — but a false fact in doctrine is a false fact, and
"decided 2026-07-14" inside the tiki parenthetical reads as the tiki decision
date, which ros gives as 2026-07-12 (expanded 2026-07-14).

*Counsel:* restate at true strength — spec'd pluggable from the outset
(external-CA plug named in the spec), seam's first slice shipped 2026-07-14
(review owed), direction set 2026-07-12. If "decided 2026-07-14" meant the
*atelier principle's* adoption, move it out of the tiki parenthetical.

## F3 — MEDIUM: API-first binds wider than the decision — the house's own tools breach it as worded

The machine-twin bullet carries an explicit scope sentence; API-first carries
none. Read literally — "a product's capabilities land behind an API *before*
any surface is built on them, and every surface — web app, CLI, automation …
— rides that same contract" — every zero-dep house CLI is in breach: none of
the seven scanners has an API beneath its CLI surface, and nothing defines
"product" to exclude them. The undefined word "product" is silently doing all
the scoping work.

*Counsel:* give it the scope line its sibling has — e.g. binds where a
capability serves (or will serve) more than one surface, or is a service; for
a single-surface CLI tool the machine twin (`--json` + exit codes) *is* its
API, which the twin bullet already mandates. That keeps the two bullets a
matched pair instead of one scoped rule and one unbounded one.

## F4 — MEDIUM: "minor"/"legitimate" framing under-warns on security-critical commodities

The swappable-seam bullet opens "Many *minor* capabilities … — a PKI CA, a
secret store, a web server, a hypervisor" — its own examples contradict
"minor" (the title's word, *commodity*, is the right one), and two of the
four are security-critical. "Building the minimal in-house version is
legitimate" reads as endorsement with the seam as the only stated guard: no
pointer to §5 (security by design) for the CA/secret-store class, and no
sentence saying when in-house is the *wrong* call (when nothing needs it,
adopting the mature product outright is the KISS / precedence-5/6 default).
Notably the real decided practice is more nuanced than the bullet: the tiki
PKI spec requires "works-out-of-box AND plugs-into-anything both", with four
custody modes including external org CA and YubiKey — the doctrine wording is
*looser* than the practice it generalises.

*Counsel:* "minor" → "commodity"; add one sentence naming the other exit
(adopt the product outright when the in-house default earns nothing) and a §5
pointer for security-critical commodities.

## F5 — LOW bundle: under-defined edges and style drift

- **The machine-twin exemption has one example and no test.** "An inherently
  interactive surface (a web app's UI)" — where do a TUI, a REPL, an
  interactive wizard sit? An undefined category inside a hard rule is where
  the rule leaks. *Counsel:* a one-line test, e.g. "if a human reads it, twin
  it; if a human operates it, the layer beneath earns the API."
- **Mobile-first's native-app edge is unpicked.** "Never a separate mobile
  edition" — is a *native* companion app a banned "mobile edition" or a
  legitimate second client riding the API-first contract? The two readings
  differ materially. *Counsel:* one clause picking a side (the API-first
  bullet suggests: another client, allowed — the ban is on forking the *web*
  surface).
- **Named-product cases diverge from the file's own style.** Every §1–§8 case
  is anonymised ("a batch operation…", "a plan/apply engine…"); the new
  bullets name `tiki` twice. Sibling method docs name tiki freely, so this is
  within-file consistency, not a repo contract break — but the header does
  say product bearings live in the child and "this file is the general
  statement". *Counsel:* either anonymise to match ("a network-automation
  tool's planned CA…") or accept named cases as the new pattern — Mike's
  call; consistency either way.
- **The twin rule now appears three ways** (§2 Unix bullet, §2 machine-twin,
  §6 observable-by-design). The header licenses overlap-as-reinforcement and
  the twin bullet cross-links the Unix bullet; §6 isn't cross-linked.
  *Counsel:* one "(see §6)" so the three statements can't drift apart
  unnoticed.

## Reconciled clean — for the record

- **Mobile-first's "no shipped worked case in the fleet yet" — verified
  true.** No web surface exists in any fleet repo (the HTML files in the
  wider Pet Projects tree are saved reference pages, not products).
- **Caselessness is honestly handled** (A8): the bullet names its own gap and
  the stub-don't-fabricate rule covers it; the "first web surface becomes the
  case" promise is loose but harmless.
- **"Specified from the outset as swappable" — true** (see F2; the ros spec
  names pluggable backends and the external-CA plug).
- **Seeded pointers reconciled** (opened post-commit): the author's three
  pointers (scope creep, exemption edge, grounding-vs-evidence) aimed at the
  right areas; this pass's concrete findings (F1's falsity, F2's
  stale-at-recording, F3's undefined "product") are what the pointers only
  gestured at. The author's session detail repeats both false claims
  ("exclusively", "not a shipped seam") — the pass ran blind to ros's
  same-day state.
- **Section placement, precedence fit, §N stability** — all four bullets sit
  correctly in §2, no ladder conflicts, no section renumbering.

## Disposition

PASS-WITH-FINDINGS. The four principles are sound as decisions and the
wording is mostly honest — the two reproduced falsities (F1, F2) are both
one-clause fixes, and F2's error is conservative. **All findings are Mike's
to decide** (rule 3: agent-authored doctrine). Per the cycle rule, the pass
carries a MAJOR, so the applied batch — once Mike rules — earns its own cold
pass before the cycle closes.

*Decision stamps (Mike) go below, per finding.*

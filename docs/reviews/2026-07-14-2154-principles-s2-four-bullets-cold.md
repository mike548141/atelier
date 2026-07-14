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

*Attack surface committed before the deferred material is opened. Verdict
follows below.*

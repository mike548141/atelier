# Cold pass — the E6b secretscan advisory tier + the E3 fingerprint carve-out

**Pass type:** code cold pass (rule-4 queued — an application of ruled
decisions; the applier's judgement produced the delta).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06 (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring session, and wrote
  this brief as the non-author taker. Rule 4's single criterion is met, and the
  tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code landed 2026-08-06, reviewed at HEAD:

1. [`tools/secretscan.py`](../../tools/secretscan.py) and
   [`tools/test_secretscan.py`](../../tools/test_secretscan.py) — the advisory
   tier (E6b) and the fingerprint carve-out (E3); that suite grew 89 → 122.
2. [`tools/floor.py`](../../tools/floor.py) and
   [`tools/test_floor.py`](../../tools/test_floor.py) — the advisory-count
   contract; that suite grew 98 → 108.
3. The consumer note in
   [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).
4. The corrected check row in [`tools/README.md`](../../tools/README.md).
5. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits: the intent of a two-tier (blocking / advisory) secret
scanner, the carve-out's design, the code, the tests, the consumer contract in
CI and the floor, and live behaviour. **Non-goals:** none narrows the delta.
The reviewer does not decide findings' dispositions; residue joins the
principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. An advisory tier is a deliberate softening: does the design keep the
   blocking floor intact, and is the boundary between tiers principled or
   convenient? Does a fingerprint carve-out create a class of secret that can
   never red the floor?
2. **Correctness & quality** — run the suites; run the scanner live against
   scratch fixtures in the scratchpad (never leave the repo dirty); verify the
   advisory-count contract between `secretscan.py` and `floor.py` behaves as
   documented, including exit codes.
3. **Completeness / harvest** — what secret classes does the carve-out
   accidentally widen to; does the README row match actual behaviour; do CI
   and the hook consume the tiers consistently?
4. **Security & privacy** — mandatory and central: this delta *is* a security
   control. Check for bypasses — a real secret shaped to land in the advisory
   tier, a fingerprint-lookalike that is actually live material, ordering or
   precedence defects between allowlists, carve-outs, and tiers. atelier is
   PUBLIC — your verdict must not quote any live-looking token or join a
   private repo's name to its posture; describe classes, never contents. The
   house security scanner reads pending diffs; this is a landed-delta review,
   so state the reach case that applied.

## Re-run obligation

Re-run, do not read, at least: both suite-count claims (89 → 122, 98 → 108) at
the landing commits and the full suites at HEAD (house invocations in
[`.githooks/pre-commit`](../../.githooks/pre-commit)), the advisory tier's
exit-code behaviour, and the fingerprint carve-out against both a genuine
fingerprint shape and a near-miss.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/`. The intent record (the prior intent pass and the rulings
the delta applies) is held by the orchestrator and will be provided on receipt
of your committed findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `AB`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — cold rule-4 pass, phase 1 (pre-reconcile)

**Provenance (repeated):** reviewed by a cold session on Fable (the
principal-named review tier, ruling 2026-08-04), spawned by the principal via an
orchestrator holding the context partition; the reviewer authored no part of the
delta, was neither started nor instructed by the authoring session, and read no
intent record, session log, prior verdict, `ROADMAP.md` or `ROADMAP-DONE.md`
before this verdict was written. Greps and reads were confined to the delta's
files, `CHANGELOG.md`, `.githooks/pre-commit`, `.atelier-floor.json` and
`docs/method/REVIEW.md` — no records surface was opened, so no author-account
exposure to disclose.

**Delta reviewed at HEAD** (6887118): `tools/secretscan.py`,
`tools/test_secretscan.py` (landed dcb57fa), `tools/floor.py`,
`tools/test_floor.py`, the `ci.yml` consumer note (landed 59190da), the
`tools/README.md` residual row, and the `CHANGELOG.md` entry (534313f/ac9fddd,
merged e3b94c1).

**Assumptions named first** (before any deferred material): (a) the blocking set
never shrinks; (b) the fingerprint regex admits only whole genuine fingerprint
shapes and near-misses still flag; (c) the carve-out reaches only the
context-free entropy net, never named or assigned context; (d) advisory means
exit 0 with consumers that actually surface the findings; (e) the board count is
read off the live run and drift is loud; (f) the suite-count claims; (g) the
allowance mechanisms compose without precedence defects. (a), (b) and (c) each
partly fail — findings AB1 and AB2.

## Re-run evidence (all re-run, none taken on trust)

| Claim | Result |
|---|---|
| `test_secretscan` 89 → 122 at dcb57fa | ✅ 89 at parent 5d083b3, 122 at dcb57fa (two failures in the scratch tree were the missing-`.git` environment; both green re-run inside a scratch git repo) |
| `test_floor` 98 → 108 at 59190da | ✅ 98 at parent dcb57fa, 108 at 59190da |
| Full suites at HEAD | ✅ 1210 Python (`unittest discover -s tools`), 207 node, `secretscan --selftest` OK |
| Advisory exit code | ✅ advisory-only fixture exits 0 with `advisory: 2 finding(s)`; blocking fixture exits 1 and keeps blocking/advisory blocks separable |
| Genuine fingerprint shape | ✅ base64 digest form suppressed and counted (`1 public-key fingerprint(s)`), exit 0; legacy colon-hex form recognised, nothing to suppress, as documented |
| Near-miss shapes | ✅ four lookalikes (body too long, too short, prefix without separator, base64url body) all BLOCK as `high-entropy` |
| Board leg live | ✅ `floor.py --plane ci --root .` at HEAD exits 0, board carries `🟡 secretscan enforced (🟡 22 advisory finding(s) — reported, not blocking)` |
| JSON contract | ✅ `clean` / `blocked` two-field shape with split counts, as documented |
| CI tree-wide guarantee | ✅ no `scope.secretscan` in `.atelier-floor.json` at HEAD; the guarantee's pin (`test_the_ci_plane_re_prints_the_whole_tree`) re-run green |

## The four lenses

**1 — Approach & assumptions.** Sound in the main. The response/detection split
is principled (a `Finding.response` field, defaulting into the gate so a rule
that forgets to declare fails safe), the tier introduces no new thresholds
(length from the E6c ruling, class split from the existing net), and the
consumers shipped with the tier rather than after it — the EI1 objection is
genuinely answered, not gestured at. To the brief's lens-1 question — *does a
fingerprint carve-out create a class of secret that can never red the floor?* —
the honest answer is YES by construction: a fingerprint is indistinguishable
from any random 256-bit value in the same encoding, so any such secret spelled
behind the algorithm prefix is inside the carve-out. The design knows this
(whole-shape matching, counted suppression, canaries both directions). What the
design did not anticipate is that the class extends into credential-keyed lines
its own tests declare unreachable — AB1.

**2 — Correctness & quality.** Both suite-count claims reproduce exactly; all
suites green at HEAD; live behaviour matches every documented claim I probed
(table above). The one changed contract (`test_context_free_path_is_unchanged`
→ `test_context_free_blocking_set_is_unchanged`) is renamed, re-scoped and
argued on the record — the honest shape for a deliberate contract change. The
module docstring carries one overclaim (AB2).

**3 — Completeness / harvest.** The README residual row matches measured
behaviour (a hex token outside an assignment is reported, not blocking — the
residual is now response, not blindness). Hook, CI and board consume the tier
consistently; the count seam is pinned from both sides and its drift state is
loud (−1 renders 🔴, never 0). Deliberate narrowness that is coherent rather
than defective: other public-digest spellings are not carved out (a
container-image digest lands in the advisory tier; a certificate-pin body still
blocks). Known softening channels adjacent to the delta are on the record, not
new (AB6).

**4 — Security & privacy** (central: the delta is a security control).
Precedence between the mechanisms is otherwise clean: the carve-out suppresses
only the context-free entropy net (a vendor token beside a fingerprint still
blocks — probed); allow-markers demand reasons and scoped typos fail closed;
`--disable` self-reports; blocking outranks advisory in dedupe, in render and
on the board; a missing count line is louder than any number. The hunted bypass
exists and is AB1 below. House scanner: `/security-review` reads pending diffs;
this is a landed-delta review of a clean tree, so there is nothing it can be
aimed at — discharged on those grounds (and it was never run over this brief).
No live token appears in this verdict; all fixture material was synthetic and
is described by class only.

## Findings

**AB1 — MODERATE (security, lens 4): the fingerprint carve-out reaches
credential-keyed assignments, and the delta's own tests claim it cannot.**
A line assigning a credential-named key a value of the form *algorithm prefix +
separator + 43-character base64 body* exited 1 before the delta (the body is a
mixed-class high-entropy hit) and scans fully CLEAN at HEAD — no finding of any
tier, only an anonymous `+1` in the fingerprint tally. Live-probed both
directions: the parent-commit scanner blocks the fixture, HEAD passes it.
Mechanism: the assigned-secret value class stops at the separator character, so
key-name context only ever sees the short algorithm token (rejected as an
identifier) and never the body; the entropy net then finds the body, and the
carve-out — which checks only span containment, not context — eats it. The
suite's `test_a_credential_under_a_key_name_still_blocks` ("a value a key name
has already called a credential is never reached by it") is true only for
values the key regex can capture whole; the composite shape refutes the general
claim. Net effect: a 256-bit secret can now sit *under a credential-named key*
and never red the floor, visible only as an aggregate count with no location
(AB3 compounds this). Graded MODERATE, borderline: the 16 canary families,
mixed-class net and capturable assigned context are all intact, the spelling is
rare in accidental leaks, and the suppression is at least counted — but it is
the exact shape the brief asked to hunt, and it regressed from blocking.
Disposition is the principal's; the options I see: exclude lines where the
credential-key regex matched from the carve-out; or demote carved-out spans to
the advisory tier instead of silence; or accept the residual explicitly and pin
the composite shape as a decided canary.

**AB2 — minor (honesty, lens 2): the module docstring's unqualified
never-shrinks claim is false at HEAD.** "The blocking set never shrinks. Every
input that exited non-zero before this tier existed still exits non-zero, with
the same finding" — E3, landed in the same commit, subtracts the fingerprint
shape (and AB1's composite) from the blocking set. The test class states the
truth precisely ("E3 is the ONE ruled subtraction"); the module contract
statement should carry the same exception rather than leave the reader a claim
the same file's own carve-out breaks.

**AB3 — minor (auditability, lens 4): fingerprint suppressions are counted but
never located.** Allow-markers are per-line, reasoned and diff-visible; ignore
globs live in a reviewable file; `--disable` prints its own scope. The
fingerprint carve-out — the one allowance that admits attacker-shapeable input —
reports only an aggregate count, in both human and JSON output. A reader who
sees the count grow (the growth-visibility the tally comment claims as its
purpose) cannot audit which lines grew it without hand-searching the tree, and
under AB1 a shaped secret is indistinguishable inside the aggregate from a
benign keygen line.

**AB4 — note: the fingerprint tally counts suppressed spans, not prevented
findings.** It increments before the placeholder gate and before dedupe, so it
can count a span that would never have become a finding (acknowledged in-code
as "counted once either way"). Semantics are honest if read as "spans"; worth a
word in the summary line if it ever confuses.

**AB5 — note: floor's count regex is anchored looser than the contract line.**
`ADVISORY_COUNT_RX` matches `advisory: N finding(s)` anywhere in captured
stdout, first match wins, and in a blocking run finding lines (which embed file
paths) print before the count line — a hostile filename could spoof the parsed
count. No impact today: such a run already exits 1 and ❌ outranks the count on
the board. Cheap hardening when next touched: match the full
`ADVISORY_COUNT_PREFIX` (already exported for exactly this purpose — the
scanner-side comment says floor matches "this prefix", which floor does not
quite do) or anchor to line start.

**AB6 — note (harvest, lens 3): the adjacent softening channels are on the
record but board-silent.** A reasoned `scope.secretscan` ends the tree-wide
re-print guarantee (named in the ci.yml comment; the pin tests only the
template default) and renders ✅ enforced with no note; `flags` may carry
`--disable` of blocking rules with a stated `why` (EP1(b) requires the reason;
the scanner's own tally then reports the disable, but the board line does not).
Both are declared-config, estate-visible channels, listed here so the ruling
round weighs them beside AB1 rather than discovering them later — not new
defects of this delta.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE (AB1) · 2 minor (AB2, AB3) ·
3 notes (AB4, AB5, AB6).** The tier and its consumers do what they claim,
every re-run claim reproduced, and the blocking core is intact; the one real
defect is the carve-out's reach into credential-keyed lines, which contradicts
the delta's own stated invariant and is the principal's to disposition.

## Follow-up checklist

- [ ] AB1 — principal's ruling: exclude credential-keyed lines from the
      carve-out, demote carved-out spans to advisory, or accept and canary the
      composite shape as decided residual.
- [ ] AB2 — qualify the module docstring's never-shrinks claim with the E3
      exception.
- [ ] AB3 — consider locating fingerprint suppressions (path:line, human and
      JSON) so a growing count is auditable.
- [ ] AB4/AB5/AB6 — notes for the ruling round; no action mandated by the
      reviewer.

*Reviewer decides no disposition; residue joins the principal's ruling round.
Reconcile section to follow on receipt of the deferred references.*

## Reconcile (written after the verdict above was durably committed)

Opened on the orchestrator's phase-2 handover, and only these two surfaces: the
prior intent verdict (`docs/reviews/2026-07-29-1243-e6-intent-cold.md`, EI1–EI6
with Mike's rulings of 2026-07-29) and `docs/ROADMAP-DONE.md` § "E6b built"
(carrying the 2026-08-04 consumer and E3 rulings as harvested). Nothing else in
the barred set was opened. Phase-1 text above is unrevised.

**Agreements — the prior cycle's decisions verify at HEAD.**

- **EI1's ruled build precondition was honoured.** E6b was barred until the
  design named where advisory findings surface durably; the delta shipped all
  three consumer legs with the tier, and every leg re-verified live in phase 1
  (hook argv pinned; CI tree-wide note plus its pin test; board `🟡 22` off the
  live run at HEAD, drift state loud). The MAJOR the intent pass raised is
  genuinely discharged, not gestured at.
- **EI4's corrected narrowing site is where the build aimed.** The
  `low-variety-entropy` rule opens exactly the mixed-class-requirement gap the
  intent pass located, not the slug suppressor the item first named.
- **EI6(a)'s per-plane semantics** are stated (ci.yml comment) and pinned
  (the tree-wide re-print test) as ruled.
- **E3's ruled mechanics are delivered as ruled** for the shapes the ruling
  named: whole-shape matching, both spellings, canaries both directions,
  counted never silent. The recorded first measurement (21 tree-wide at the
  landing commit) reproduces exactly on the landing tree — post-reconcile
  re-run; HEAD's 22 is tree movement since, not contract drift.
- **Convergent residue, independently reached:** the harvest's stated-limits
  list (container-image digests land advisory, unruled and unsuppressed;
  `PUBLIC_KEY_RX` still subtracts silently, queued as its own item) matches my
  lens-3 observations, so neither is re-raised as new.

**Divergences.**

- **AB1 is genuinely new — not priced by the E3 ruling.** The ruling's evidence
  base and scope were fingerprint tokens in prose context (keygen-style output;
  "two of eight findings in one child were this shape"), and its both-directions
  canary ask was met for the shapes it named: wrong length, missing separator,
  bare prefix. Neither the ruling, the intent verdict, nor the harvested
  stated-limits residue mentions the composite shape — a fingerprint-spelled
  value *assigned to a credential-named key* — and the build's own test asserts
  that context is unreachable, which phase 1 falsified live. So the carve-out's
  reach exceeds what was ruled ("stop blocking on public fingerprints", not
  "suppress fingerprint-spelled values under credential keys"), and the
  stated-limits paragraph — the delta's honest-residue surface — omits it,
  confirming missed rather than accepted. AB1 stands at MODERATE; the ruling
  context sharpens its framing (scope-exceedance, not just a bypass) without
  changing its grade. The nearby harvested residue line ("a non-alphanumeric
  token carrying separators still passes both tiers") is a different, standing
  limitation — separator-broken spans the net never matched — not this
  regression of a span it did block.
- **AB2 stands, narrowed to one surface.** The harvest and CHANGELOG scope the
  never-shrinks claim to the blocking families and name E3 as the ruled
  subtraction beside it; only the module docstring carries the unqualified
  sentence. The finding is confirmed as a single-file wording fix, not a
  record-wide honesty defect.
- **AB3 stands as a refinement of the ruling, not a conflict.** The ruling
  asked counted-never-silent and got it; location-less counting is a gap the
  ruling did not speak to. Disposition remains the principal's.

**Post-reconcile additions (clearly marked, found only via the deferred
surfaces):** none rising to a finding. Two verifications performed
post-reconcile and recorded here for completeness: the 21-at-landing
measurement reproduced (above), and the harvest's "interpretation flagged"
note — the board count read as `floor.py`'s per-repo board, `floorfleet`
deliberately given none — matches what the code does; that interpretation was
already put to the principal at the build's close and needs nothing from this
pass. The harvest's suite claim (1060 → 1103 on the branch) was not re-run as a
whole; its two named components (89 → 122, 98 → 108) both reproduced in
phase 1.

**Status after reconcile:** overall line unchanged — **PASS-WITH-FINDINGS,
0 MAJOR · 1 MODERATE · 2 minor · 3 notes**. No finding's severity moved; AB1
gains the scope-exceedance framing for the ruling round. Verdict finalised.

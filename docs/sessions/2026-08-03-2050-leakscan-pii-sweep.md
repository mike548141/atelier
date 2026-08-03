# leakscan PII-half sweep — 2026-08-03

The companion sweep the E6 intent record flagged and the intent cold pass
endorsed as real open work, carried four sessions and discharged here: **does
`leakscan` reach the personal-data half of the stated boundary intent as
`secretscan` (post-E6) reaches the credential half?** Run by an analysis
worker of the 2026-08-03 Fable-orchestrated queue run; probes were synthetic,
run in a discarded worktree, and none touched `SESSIONS.md`/`docs/sessions/`
(author-account records are out of sweep scope by standing rule). Every probe
shape below is **described, never quoted** — most of the literal forms would
trip the scanners this record discusses, which is the describe-don't-quote
rule (E5) doing exactly its job.

## Verdict

**Partially — materially behind the credential half.** `secretscan` covers
credentials three ways: named vendor shapes, a credential-key context rule
(key name plus value), and a context-free entropy net, with placeholder and
indirection suppression. `leakscan` covers personal data two ways: twelve
structural rules (of which five are personal data proper — email, NZ street
address, NZ phone, coordinates, NZ IRD shape; three are estate topology;
three duplicate secretscan's ground) and the machine-local literal term list.
It has **no label/assignment context layer and no placeholder suppression**,
and since personal data has no entropy signature, label context is the only
available analogue of the generic net. Probed: a block of values sitting
under explicit personal-data key names (date-of-birth, patient name, bank
account, medication, passport number, NHI, vehicle plate) passed completely
clean. Where the tool *is* aimed it is genuinely good — nine of ten NZ phone
formats, email, NZ street addresses, high-precision coordinates all caught.
The failure is reach, not craft.

## Coverage map (class level)

Covered structurally and probe-confirmed: personal email · NZ street
addresses (three common forms) · NZ phone (nine of ten common formats; the
bracketed area-code form is the miss) · hyphenated IRD shape ·
high-precision coordinates · home IP shapes, MAC, IPv6/ULA.

Covered only by the machine-local term list (exact literal, whole word):
person names · health terms · SSIDs and internal hostnames · social handles.
Probed: slug, camel-case, snake-case, double-space, line-split and initial
forms of a listed name all pass clean — the list matches the canonical
spelling only.

Covered by nothing (all probe-confirmed clean): date of birth in any form ·
NZ bank account (hyphenated or compact) · payment card numbers · bare-digit
IRD/tax numbers · IBAN · passport / driver licence / NHI numbers · vehicle
plates · international non-NZ phone numbers · email localparts without a
domain · low-precision coordinates · children's school/age/year details ·
calendar and routine patterns · **file paths** (a file whose *name* carries
an address never has that name scanned) · **binary media** (a synthetic
image carrying GPS metadata, a name, an email and an address scanned clean —
binaries are skipped silently).

## Ranked gaps

- **G1 — the missing third kind: a personal-data key-context rule.** The
  highest-value fix by a wide margin: one rule (a PII key vocabulary
  mirroring the credential-key rule, firing on a non-placeholder value)
  closes DOB, bank account, passport, licence, NHI, plate, bare IRD, health
  and next-of-kin at once — and it is the move E6's own reasoning blesses:
  key context has already done the filtering. Cry-wolf LOW, lower still if
  it reuses secretscan's placeholder/indirection suppression, which leakscan
  currently lacks entirely.
- **G2 — scan the path, not just the contents.** Run the relative path
  through the same rule set, report at line zero. Cry-wolf LOW and
  *measured*: the full structural set over this repo's 390 real tracked
  paths produced zero findings.
- **G3 — binary media are unscannable, and silently so.** Honest fix is a
  *notice*, not a parse: committed image/media types get an
  unscannable-content line (or an image-metadata check). Cry-wolf MEDIUM as
  a block, LOW as a notice. Recorded tension, not resolved here: an
  unscannable-content notice is advisory-shaped, and `SECRETS.md` (E6a) has
  just recorded "leakscan gains no advisory form" as decided — this is the
  honest counter-case for Mike to weigh.
- **G4 — financial identifiers as a class.** Card numbers with a Luhn check
  (self-validating, LOW); IBAN by country-plus-checksum shape (LOW); NZ bank
  account by its hyphenated field shape (LOW-MEDIUM; the compact digit form
  must stay key-context-only). Bare-digit IRD: key-context only, never
  standalone.
- **G5 — international phone** by the E.164 shape (leading plus, eight to
  fifteen digits). Cry-wolf MEDIUM: semver build metadata and other
  plus-prefixed numerics are the FP class; require a plausible country code
  and exclude version contexts.
- **G6 — term-list form fragility.** Names leak as slugs, localparts and
  identifiers far more often than as the canonical spaced literal. Fix is
  cheap: teach the regex form for derived shapes in the example terms file
  (today it teaches it only for hostnames and subnets), or opt-in
  auto-derivation of separator variants per term. Cry-wolf LOW-MEDIUM;
  derivation stays opt-in.
- **G7 — the bracketed NZ phone form.** One-character regex widening;
  cry-wolf negligible.

## What should NOT be added (part of the finding)

A bare date rule for DOB (every record in the estate is date-stamped; it
would fire on essentially every file) · standalone ID-shape rules for
passport/licence/NHI/plate (letters-plus-digits is the shape of SKUs, enum
values and ticket refs — the E4 class waiting to happen) · bare eight/nine
digit number rules · name detection by dictionary or NER (unbounded FP
surface, and it would put a name corpus in a public repo — the machine-local
term list is the correct home, that split is the design working) ·
calendar-pattern detection (prose, not a shape; its control is E5's
describe-don't-quote rule) · low-precision coordinate rules (collide with
every ordinary decimal pair).

## Defects found in existing rules

- **D1 (the real one) — an allow-marker silences the term list too.** The
  scanner skips the whole line on an allow-marker *before* any rule runs, so
  a marker written for a low-confidence structural FP also disables the
  highest-confidence layer — the estate's own literals — on that line, and
  the repo already carries allow-markered lines. Probed: a line holding a
  term-list-matching name plus an unrelated allow-marker scanned clean. Fix
  shape: exempt structural rules only, or make markers rule-scoped.
- **D2 — the E4 class is live and wider than the roadmap states.** The IPv6
  rule fires on any three-plus colon-separated hex-ish groups: time
  triplets, port mappings, ratio notation, hex colour triplets — not just
  "two clock times side by side".
- **D3 — the IPv4 rule flags non-findings**: the common netmask literals,
  loopback, broadcast, and public resolvers — guaranteed allow-marker
  generators in networking prose. Fix: widen the safe set.
- **D4 — the NZ address rule FPs on short and bare-word suffix forms** (a
  low street number plus an abbreviated or single-word suffix with no
  preceding capitalised word). Fix: require at least one capitalised word
  before those suffixes.
- **D5 (cosmetic) — MAC addresses double-report**, once as MAC and once as
  IPv6 on the same span.
- **D6 (nit) — the IPv4 safe-set check uses a prefix match** for the
  all-zeroes address, so longer octet strings beginning with those
  characters are exempted too; the exact-match clause beside it is redundant.

## Worth stating, not a defect

The hook/CI plane split means the term list — the only cover for names,
health, finance and topology literals — never runs tree-wide. That is
decided design (the floor documents it, and the require-terms flag plus the
partial-cover rendering are the honesty controls), but its consequence is
worth holding: a personal-data leak that reaches history via a bypassed
hook, a machine without the list, or a host that never had one, is never
detected again by anything.

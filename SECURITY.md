# Security policy

atelier is a **public, solo-maintained** doctrine repository that also ships
working tooling other repositories adopt — the `tools/` scanners and the
`docs/build/templates/` a child repo copies. This policy covers vulnerabilities
in *that* surface. It is deliberately short: the repo runs no service, holds no
secrets, and takes no third-party dependencies (zero-dep stdlib Python and Node
— see `tools/README.md`, "Supply chain"), so the realistic vulnerability classes
are narrow.

## Scope

**In scope** — a flaw in what this repo ships:

- a scanner in `tools/` that fails to catch what it claims to catch (a
  false-negative in a security control — e.g. a secret shape `secretscan` should
  flag and does not), or that can be induced to pass unsafe content;
- a template in `docs/build/templates/` that ships an insecure default into
  every repo that copies it (an over-permissive workflow permission, an unpinned
  action, a leaky `.gitignore`);
- doctrine that, followed as written, leads an adopter into an unsafe practice.

**Out of scope:**

- an adopter's own estate, private repositories, or how they wired the tooling —
  that is the adopter's boundary, not this repo's;
- third-party GitHub Actions, the Python/Node toolchain, or the CI runner image
  — report those to their own maintainers (this repo pins the actions it uses;
  see `tools/README.md`, "Supply chain", on the toolchain residual);
- the **documented** limits of the scanners — each tool states in
  `tools/README.md` what it structurally cannot see. A report that a scanner
  misses a class it already declares out of reach is a documentation pointer,
  not a vulnerability.

## Reporting

Report privately through **GitHub's security advisories** — the "Report a
vulnerability" button under this repository's *Security* tab (GitHub Private
Vulnerability Reporting). That keeps the report confidential until a fix exists.
Please do **not** open a public issue for a security flaw.

Include what you would want to receive: the affected file or tool, what an
attacker gains, and the smallest steps to reproduce.

## What to expect

This is a one-person project maintained around other work, so there is **no
guaranteed response time and no service-level commitment** — realistically,
acknowledgement in days-to-weeks, not hours. There is **no bug bounty**; reports
are handled on a best-effort basis because the tooling is worth keeping sound,
not for a reward.

When a report is confirmed, the fix carries a **severity** and a
**recurrence-prevention step** — the same way an internally-found security
finding does (`docs/method/REVIEW.md`, the security lens). Because a fix
publishes on push (the repo is public) and children pin atelier by commit SHA,
adopters pick it up by bumping their pin.

#!/usr/bin/env python3
"""signscan — verify git commit signatures over a range against a trust list.

The CI + hook half of SIGNING.md (ADR 0007): a signature nobody verifies
enforces nothing (the same read-≠-complied logic as PROPAGATION). Verification
is **two-plane by necessity**, split by committer (2026-07-12 review, G1):

  - MACHINE-KEY commits — everything NOT committed by GitHub's web-flow identity
    (its public no-reply committer, see WEB_FLOW_EMAIL below). Verified locally
    with ssh-keygen against the canonical `allowed_signers`: the durable,
    self-hosted, auditable plane. This tool does exactly this.
  - GITHUB-SERVER commits — merge/squash commits GitHub itself mints, committed
    by the web-flow identity and signed by GitHub's web-flow GPG key. Verifying
    them needs a GPG keyring this estate does not run, so they go through
    `gh api …commit.verification.verified` instead — NOT here. This tool REPORTS
    them as `deferred` so the CI gh-api step (or a human) covers them. Silently
    passing them would be a hole; silently failing them would red-flag every PR
    merge (two such commits already sit on atelier's own main).

TRUST LIST RESOLUTION IS THE CALLER'S JOB. Pass --allowed-signers pointing at
atelier's file **at the child's pin** (ADR 0002), never floating main — a floated
trust root lets anyone with write to atelier's main mint trust for every child
silently, the exact auth-plane compromise the dedicated signing key exists to
survive.

WHAT VERIFICATION ASSERTS, HONESTLY: git checks the signing key is a *member* of
allowed_signers; it does not bind key to committer identity (any listed key
verifies any committer). The assurance is machine-level custody, not personal
authorship — stating it stronger would over-claim (SIGNING.md).

Zero third-party deps: stdlib + git + ssh-keygen, already present wherever git
signs. `gh` is only for the separate GitHub-server plane, never invoked here.

    signscan --allowed-signers <path> --boundary <sha>   # verify <sha>..HEAD
    signscan --allowed-signers <path> --rev <sha>        # verify one commit
    signscan --selftest                                  # prove the engine
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

# GitHub's web-flow committer address — the marker that a commit is server-minted
# (merge/squash) and belongs to the gh-api plane, not the local one. Not personal
# data: it is GitHub's own public no-reply identity.
WEB_FLOW_EMAIL = "noreply@github.com"  # leakscan:allow: GitHub's public web-flow committer address


class SignscanError(Exception):
    """Environment failure — could not truthfully compute, so we don't pretend."""


def _git(repo: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", repo, *args],
        capture_output=True, text=True,
    )


def commit_range(repo: str, boundary: str | None, rev: str | None) -> list[str]:
    """Commits to verify. A single `rev`; or `boundary..HEAD` (boundary EXCLUSIVE
    — it is the last UNSIGNED commit, the adoption boundary, so a retrofit repo
    skips its pre-signing history); or, with neither, ALL of HEAD's history — the
    right default for a born-signed repo, where every commit should verify."""
    if rev:
        spec = ["-1", rev]
    elif boundary:
        spec = [f"{boundary}..HEAD"]
    else:
        spec = ["HEAD"]
    proc = _git(repo, "rev-list", *spec)
    if proc.returncode != 0:
        raise SignscanError(f"git rev-list failed: {proc.stderr.strip()}")
    return [line for line in proc.stdout.split() if line]


def committer_email(repo: str, sha: str) -> str:
    proc = _git(repo, "show", "-s", "--format=%ce", sha)
    if proc.returncode != 0:
        raise SignscanError(f"git show failed for {sha}: {proc.stderr.strip()}")
    return proc.stdout.strip()


def verify_machine_commit(repo: str, sha: str, allowed_signers: str) -> tuple[bool, str]:
    """Verify one machine-key commit against the given allowed_signers file.
    Returns (ok, detail). The trust file is forced on the command line so the
    caller's pinned file is used, not whatever the repo/machine config points at."""
    proc = _git(
        repo,
        "-c", "gpg.format=ssh",
        "-c", f"gpg.ssh.allowedSignersFile={allowed_signers}",
        "verify-commit", sha,
    )
    # git verify-commit reports on stderr and exits 0 only on a good signature.
    detail = (proc.stderr or proc.stdout).strip().splitlines()
    return proc.returncode == 0, (detail[-1] if detail else "")


def scan(repo: str, allowed_signers: str, boundary: str | None,
         rev: str | None, web_flow_email: str) -> dict:
    if not os.path.isfile(allowed_signers):
        raise SignscanError(f"allowed_signers not found: {allowed_signers}")
    allowed_abs = os.path.abspath(allowed_signers)
    results = []
    for sha in commit_range(repo, boundary, rev):
        email = committer_email(repo, sha)
        if email == web_flow_email:
            results.append({"sha": sha, "plane": "github", "status": "deferred",
                            "detail": "server-minted; verify via gh api"})
            continue
        ok, detail = verify_machine_commit(repo, sha, allowed_abs)
        results.append({"sha": sha, "plane": "machine",
                        "status": "good" if ok else "bad", "detail": detail})
    return {"repo": repo, "allowed_signers": allowed_abs, "results": results}


# --- selftest fixture -------------------------------------------------------
# A known ed25519 signature over known data, verifiable with ssh-keygen. Only the
# PUBLIC key and the signature are embedded (the throwaway private key was
# discarded at generation) — nothing secret. The allowed_signers line uses the
# QUOTED valid-after form: if a platform's ssh-keygen ever fails to parse it (the
# "missing start quote" trap the estate hit — SIGNING.md), the positive case goes
# red here instead of silently failing every real verification.
_FIX_DATA = b"atelier signscan selftest fixture v1\n"
_FIX_PUB = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH83ur6OGBroCHBjw+NivPdhPWyVp5SVKOhTbZkGnruT"  # secretscan:allow: throwaway selftest public key, not a credential
# Assembled from per-line literals (not one triple-quoted blob) so each
# base64 line can carry its own secretscan:allow at the source level — the
# armored SSH SIGNATURE of a throwaway key over _FIX_DATA, public and inert.
_FIX_SIG = "\n".join([
    "-----BEGIN SSH SIGNATURE-----",
    "U1NIU0lHAAAAAQAAADMAAAALc3NoLWVkMjU1MTkAAAAgfze6vo4YGugIcGPD42K892E9bJ",  # secretscan:allow: throwaway selftest signature line, not a credential
    "WnlJUo6FNtmQaeu5MAAAADZ2l0AAAAAAAAAAZzaGE1MTIAAABTAAAAC3NzaC1lZDI1NTE5",  # secretscan:allow: throwaway selftest signature line, not a credential
    "AAAAQP8+O/JClxp8l9MejSSurrHdeeY1JoY71uejS3/A9JiifbI4EJ8EMFvGafMqHJQuc5",  # secretscan:allow: throwaway selftest signature line, not a credential
    "2nhAHMEhGCm8PkG5fNYw8=",  # secretscan:allow: throwaway selftest signature line, not a credential
    "-----END SSH SIGNATURE-----",
    "",
])
_FIX_PRINCIPAL = "signscan-selftest@atelier"  # leakscan:allow: fictional selftest principal, not a real address


def _ssh_verify(allowed_signers: str, principal: str, sig_path: str,
                data: bytes) -> int:
    proc = subprocess.run(
        ["ssh-keygen", "-Y", "verify", "-f", allowed_signers,
         "-I", principal, "-n", "git", "-s", sig_path],
        input=data, capture_output=True,
    )
    return proc.returncode


def _selftest() -> int:
    """Prove the verification engine on any box: the known-good fixture MUST
    verify (guards allowed_signers parsing — the quoted-timestamp regression),
    and a tampered payload MUST fail (proves the check has teeth, not a no-op)."""
    if subprocess.run(["ssh-keygen", "--help"], capture_output=True).returncode not in (0, 1, 255):
        print("selftest FAILED — ssh-keygen not available")
        return 1
    with tempfile.TemporaryDirectory() as d:
        as_path = os.path.join(d, "allowed_signers")
        sig_path = os.path.join(d, "data.sig")
        with open(as_path, "w") as f:
            f.write(f'{_FIX_PRINCIPAL} namespaces="git",valid-after="20260101" {_FIX_PUB}\n')
        with open(sig_path, "w") as f:
            f.write(_FIX_SIG)

        good = _ssh_verify(as_path, _FIX_PRINCIPAL, sig_path, _FIX_DATA)
        tampered = _ssh_verify(as_path, _FIX_PRINCIPAL, sig_path, b"tampered\n")

    ok = good == 0 and tampered != 0
    if good != 0:
        print("selftest FAILED — known-good fixture did not verify "
              "(allowed_signers parse regression? check quoted valid-after)")
    if tampered == 0:
        print("selftest FAILED — tampered payload verified (check has no teeth)")
    if ok:
        print("selftest OK — fixture verifies, tampering rejected")
    return 0 if ok else 1


def render_human(report: dict, warn: bool) -> tuple[str, int]:
    results = report["results"]
    machine = [r for r in results if r["plane"] == "machine"]
    deferred = [r for r in results if r["plane"] == "github"]
    bad = [r for r in machine if r["status"] == "bad"]
    lines = []
    for r in bad:
        lines.append(f"  ✗ {r['sha'][:12]}  {r['detail']}")
    for r in deferred:
        lines.append(f"  ~ {r['sha'][:12]}  github-server commit → verify via gh api plane")
    good_n = len(machine) - len(bad)
    head = (f"signscan: {good_n} good, {len(bad)} bad, {len(deferred)} deferred "
            f"(github plane) over {len(results)} commit(s)")
    body = "\n".join(lines)
    if bad:
        verb = "WARN (not blocking)" if warn else "FAIL"
        out = f"✗ {head} — {verb}\n{body}"
        return out, (0 if warn else 1)
    tail = f"\n{body}" if body else ""
    return f"✓ {head}{tail}", 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="signscan",
        description="Verify git commit signatures over a range against a trust list.")
    ap.add_argument("--allowed-signers",
                    help="trust list to verify against — atelier's allowed_signers "
                         "AT THE CHILD'S PIN, never floating main")
    ap.add_argument("--boundary",
                    help="adoption boundary SHA (exclusive): verify <boundary>..HEAD")
    ap.add_argument("--rev", help="verify a single commit instead of a range")
    ap.add_argument("--repo", default=".", help="repo directory (default: .)")
    ap.add_argument("--warn", action="store_true",
                    help="report bad signatures but exit 0 (warn-first rollout)")
    ap.add_argument("--web-flow-email", default=WEB_FLOW_EMAIL,
                    help=argparse.SUPPRESS)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the engine on a known fixture, then exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()
    if not args.allowed_signers:
        ap.error("--allowed-signers is required (or use --selftest)")

    try:
        report = scan(args.repo, args.allowed_signers, args.boundary,
                      args.rev, args.web_flow_email)
    except SignscanError as e:
        print(f"signscan: environment error — {e}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2))
        bad = any(r["status"] == "bad" for r in report["results"])
        return 0 if (args.warn or not bad) else 1

    out, code = render_human(report, args.warn)
    print(out)
    return code


if __name__ == "__main__":
    sys.exit(main())

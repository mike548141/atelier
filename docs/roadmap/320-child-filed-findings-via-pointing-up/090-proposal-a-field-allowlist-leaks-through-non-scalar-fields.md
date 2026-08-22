- [ ] **Proposal: a response-field allowlist leaks through non-scalar fields —
      the output side of exposure wants a sentence in `SECRETS.md`.** Filed
      from a private child via § *Pointing up*, 2026-08-22.
      **The incident, as class:** a session reading a provider API's
      certificate listing allowlisted the fields it kept before printing — the
      discipline the child's own doctrine prescribes — and kept a field whose
      value had always been a scalar label. For objects signed by the
      provider's own internal CA, the provider embeds the *entire issuing-CA
      object* in that field, private key included, and the allowlist passed it
      whole into the session transcript. Rotation is queued under the child's
      exposure rule (retire-vs-reissue is the principal's open ruling); nothing
      reached any tree, and no key material appears in any record.
      **The guarantee that failed:** "allowlist the fields you keep" reads as a
      complete defence and is not — it is only as strong as the kept values'
      *types*. A kept field holding a dict/object is an unfiltered surface
      wearing an allowlisted name. Third instance of the
      provider-reads-hand-back-credentials class in that child's history; first
      where the allowlist itself was the hole.
      **Proposed doctrine, one sentence, likely home `SECRETS.md` (Exposure, or
      the boundary's posture):** treat any non-scalar value under a kept field
      as un-allowlisted — drop it, or recurse the allowlist into it, never
      print it. The child already carries the full rule locally in its own
      wording; what points up is the class, which is true of any repo whose
      sessions read provider APIs — a stack-independent shape, per § The test.
      **For the verifying atelier session:** the shape reproduces against any
      provider whose read APIs expand related objects in place (ORM-style
      embedding); the child can supply a redacted transcript shape over the
      cross-session channel on request.

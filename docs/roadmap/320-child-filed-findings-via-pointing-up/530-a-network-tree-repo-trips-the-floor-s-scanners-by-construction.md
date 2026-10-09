- [ ] 🔎 **Hand-up from a private child: a repo that holds one network's
      desired state and operational records trips the floor's scanners by
      construction — a create-repo type for it** `[M][doctrine][tools]` —
      filed 2026-10-09 under `PROPAGATION.md` § *Pointing up*. A report, not
      parent work: consideration and remediation are atelier's. Evidenced from
      **one** child repo only, observed 2026-10-08 and 2026-10-09.

  **The shape of the repo.** The child holds a single network's desired state
  (a layered config tree) plus the operational records that accumulate while
  that network is run: device configuration exports, encrypted secret files
  (age/sops), binary device backups that are themselves age-encrypted, packet
  captures kept as evidence, measurement directories named with UTC
  timestamps, and review files written by a reviewer who is not the repo's
  author. `REPO-STANDARD.md` sizes repos to a type (static, package, infra /
  config, docs); this is an infra / config repo whose *operational residue* is
  the unusual part, and it is the residue that collides with the scanners.

  **What happened, in order (all measured in the child, none inferred).**

  | When | Scanner | Legitimate content it tripped on | How it was resolved |
  |---|---|---|---|
  | At repo creation | `leakscan`, `secretscan` | the tree's ordinary content (addresses, hostnames, encrypted secret files) | scoped by hand, **copying the precedent of another private repo of the same kind** — there was no house starting point to copy |
  | In normal operation | `secretscan` | timestamped evidence-directory names, and a list of IPv6 DNS resolver addresses, read as high-entropy strings | reasoned marker / exemption |
  | In normal operation | `publishscan` | packet-capture evidence files | a reasoned glob exemption |
  | In normal operation | `datescan`, `wrapscan` | a reviewer's verbatim prose in a review record ("tonight", long lines) | a per-line allow-marker on **another author's words** |

  Every one of these was resolved the sanctioned way, with a reason attached.
  The cost was not the exemption; it was that each arrived as a **blocked
  commit in the middle of operating the network**, and at least once during a
  time-sensitive change window, when the commit was the point of the work.

  **The class.** A repo type whose normal, correct contents are the things the
  scanners are tuned to distrust: encrypted blobs, high-entropy-looking
  identifiers (timestamps in names, resolver address lists), binary evidence,
  and prose that is not the repo author's. The scoping was reasoned fresh each
  time, and the first scoping was copied from a sibling by hand, which is the
  `PROPAGATION.md` drift pattern one level down: the knowledge of what such a
  repo legitimately contains lives in two private repos and nowhere in the
  house.

  **Evidenced vs unevidenced.**

  - **Evidenced (one child):** the four trips above, and that each was resolved
    with a reasoned exemption or marker.
  - **Unevidenced:** that other repos of this kind exist and meet the same
    friction (one sibling is known to have been scoped first; whether it hit the
    same operational trips is not known). Whether the exemptions are the same
    set across such repos. Whether any of the `secretscan` trips is a
    detector defect rather than a content-type issue; that is not claimed.

  **Ask (offered for atelier to consider; the reporter does not decide it).**

  1. A **"network tree" type in `create-repo`** (a sub-kind of infra / config)
     that ships the exemptions it will certainly need, *each with its reason*:
     capture-file globs for `publishscan`, an evidence-directory naming
     convention that does not read as a secret, and the paths where
     encrypted backups live. The reasons matter as much as the globs, since
     the ignore files require one per line.
  2. Possibly a scanner-level notion of a **verbatim record by another
     author**, so a reviewer's prose is neither edited nor line-marked to
     satisfy `datescan` / `wrapscan`. Editing a reviewer's words defeats the
     point of a cold review; marking them line by line works but scatters
     markers through a record whose value is that it is untouched.

  **What the child did locally.** It narrowed with reasons and kept the
  incident in its own record, per step 3 and 4 of the route. It added no
  general rule. Whether (1) and (2) are one item or two is atelier's to split.

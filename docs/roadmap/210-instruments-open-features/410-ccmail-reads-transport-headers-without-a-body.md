- [~] 🔧 **`ccmail` gains a headers-only read: a message's transport headers (Received, authentication results, DKIM-Signature) fetched without its body, so a mail route can be measured from a mailbox without reading anyone's mail.** (claimed 2026-11-11-0840, wt: ccmail-headers)

      **Why.** A session measuring an outbound mail route (which hops a
      message crossed, the TLS on each, which domain signed it) needs only the
      headers a receiving server writes. The mailbox connector sessions talk
      to returns whole messages, bodies included; `ccmail` talks to the Gmail
      API directly and can ask for `format=metadata` with a named header list,
      which returns no body at all. Same grant (`gmail.readonly`), no new
      scope, no new credential.

      **Shape.** `ccmail <id> --headers` and `ccmail --search <q> --headers`
      write one private file of transport headers per message and print only
      paths; subjects are not fetched in this mode. Same work-tree refusal as
      `--get`.

## Bot Verification Methods

Cloudflare verifies bots via:

1. **Reverse DNS (IP validation):** Traditional method—bot IP resolves to expected domain
2. **Web Bot Auth:** Modern cryptographic verification—faster propagation

When `verifiedBot=true`, bot passed at least one method.

**Inactive verified bots:** IPs removed after 24h of no traffic.


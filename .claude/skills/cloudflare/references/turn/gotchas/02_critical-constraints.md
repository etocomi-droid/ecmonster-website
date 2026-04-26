## Critical Constraints

| Constraint | Value | Consequence if Violated |
|------------|-------|-------------------------|
| Max credential TTL | 48 hours (172800s) | API rejects request |
| Credential revocation delay | ~seconds | Billing stops immediately, connection drops shortly |
| IP allowlist update window | 14 days (if IPs change) | Connection fails if IPs change |
| Packet rate | 5-10k pps per allocation | Packet drops |
| Data rate | 50-100 Mbps per allocation | Packet drops |
| Unique IP rate | >5 new IPs/sec | Packet drops |


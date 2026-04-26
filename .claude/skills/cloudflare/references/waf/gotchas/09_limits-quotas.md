## Limits & Quotas

| Resource | Free | Pro | Business | Enterprise |
|----------|------|-----|----------|------------|
| Custom rules | 5 | 20 | 100 | 1000 |
| Rate limiting rules | 1 | 10 | 25 | 100 |
| Rule expression length | 4096 chars | 4096 chars | 4096 chars | 4096 chars |
| Rules per ruleset | 75 | 75 | 400 | 1000 |
| Managed rulesets | Yes | Yes | Yes | Yes |
| Rate limit characteristics | 2 | 3 | 5 | 5 |

**Important Notes:**
- Rules execute in order; first match wins (except skip rules)
- Expression evaluation stops at first `false` in AND chains
- `matches` regex operator is slower than string operators
- Rate limit counting happens before mitigation


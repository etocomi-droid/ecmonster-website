## Headers Quick Reference

| Header | Purpose | Example | Notes |
|--------|---------|---------|-------|
| `cf-aig-authorization` | Gateway auth | `Bearer {token}` | Required for authenticated gateways |
| `cf-aig-metadata` | Tracking | `{"userId":"x"}` | Max 5 entries, flat structure |
| `cf-aig-cache-ttl` | Cache duration | `3600` | Seconds, min 60, max 2592000 (30 days) |
| `cf-aig-skip-cache` | Bypass cache | `true` | - |
| `cf-aig-cache-key` | Custom cache key | `my-key` | Must be unique per response |
| `cf-aig-collect-log` | Skip logging | `false` | Default: true |
| `cf-aig-cache-status` | Cache hit/miss | Response only | `HIT` or `MISS` |


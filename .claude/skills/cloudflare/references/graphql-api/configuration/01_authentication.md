## Authentication

### API Token (Recommended)

| Permission | Scope | Use Case |
|------------|-------|----------|
| **Account Analytics: Read** | Account-wide | Workers, R2, KV, D1, DO, AI, Network Analytics |
| **Zone Analytics: Read** | Per-zone | HTTP requests, Firewall, DNS, Load Balancing |
| **All zones - Analytics: Read** | All zones | Multi-zone HTTP/Firewall/DNS queries |

Create tokens at: [dash.cloudflare.com > Account API Tokens](https://dash.cloudflare.com/?to=/:account/api-tokens)

```bash
# Verify token
curl -s https://api.cloudflare.com/client/v4/graphql \
  -H "Authorization: Bearer $CF_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"query":"{ viewer { zones(filter: {zoneTag: \"ZONE_ID\"}) { httpRequestsAdaptiveGroups(limit: 1, filter: {datetime_gt: \"2025-01-01T00:00:00Z\"}) { count } } } }"}'
```

### API Key + Email (Legacy)

Not recommended. Use `X-Auth-Email` + `X-Auth-Key` headers instead of `Authorization: Bearer`.


## Creating a Gateway

### Dashboard
AI > AI Gateway > Create Gateway > Configure (auth, caching, rate limiting, logging)

### API
```bash
curl -X POST https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways \
  -H "Authorization: Bearer $CF_API_TOKEN" -H "Content-Type: application/json" \
  -d '{"id":"my-gateway","cache_ttl":3600,"rate_limiting_interval":60,"rate_limiting_limit":100,"collect_logs":true}'
```

**Naming:** lowercase alphanumeric + hyphens (e.g., `prod-api`, `dev-chat`)


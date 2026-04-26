## Authentication

### API Token (Recommended)

**Create token**: Dashboard → My Profile → API Tokens → Create Token

```bash
export CLOUDFLARE_API_TOKEN='your-token-here'

curl "https://api.cloudflare.com/client/v4/zones" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

**Token scopes**: Always use minimal permissions (zone-specific, time-limited).

### API Key (Legacy)

```bash
curl "https://api.cloudflare.com/client/v4/zones" \
  --header "X-Auth-Email: user@example.com" \
  --header "X-Auth-Key: $CLOUDFLARE_API_KEY"
```

**Not recommended:** Full account access, cannot scope permissions.


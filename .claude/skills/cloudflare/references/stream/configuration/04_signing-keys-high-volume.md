## Signing Keys (High Volume)

Create once for self-signing tokens (thousands of daily users).

**Create key**
```bash
curl -X POST \
  "https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/keys" \
  -H "Authorization: Bearer <API_TOKEN>"

# Save `id` and `jwk` (base64) from response
```

**Store in secrets**
```bash
wrangler secret put STREAM_KEY_ID
wrangler secret put STREAM_JWK
```


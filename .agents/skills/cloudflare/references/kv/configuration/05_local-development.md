## Local Development

```bash
wrangler dev                # Local KV (isolated)
wrangler dev --remote       # Remote KV (production)

# Or in wrangler.jsonc:
# "kv_namespaces": [{ "binding": "MY_KV", "id": "...", "remote": true }]
```


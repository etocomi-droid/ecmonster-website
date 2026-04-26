## Worker Isolation Mode

Workers in a namespace run in **untrusted mode** by default for security:
- No access to `request.cf` object
- Isolated cache per Worker (no shared cache)
- `caches.default` disabled

### Enable Trusted Mode

For internal platforms where you control all code:

```bash
curl -X PUT \
  "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/dispatch/namespaces/$NAMESPACE" \
  -H "Authorization: Bearer $API_TOKEN" \
  -d '{"name": "'$NAMESPACE'", "trusted_workers": true}'
```

**Caveats:**
- Workers share cache within namespace (use cache key prefixes: `customer-${id}:${key}`)
- `request.cf` object accessible
- Redeploy existing Workers after enabling trusted mode

**When to use:** Internal platforms, A/B testing platforms, need geolocation data


### With Outbound Worker
```jsonc
{
  "dispatch_namespaces": [{
    "binding": "DISPATCHER",
    "namespace": "production",
    "outbound": {
      "service": "outbound-worker",
      "parameters": ["customer_context"]
    }
  }]
}
```


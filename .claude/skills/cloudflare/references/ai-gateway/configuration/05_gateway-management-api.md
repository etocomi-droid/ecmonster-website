## Gateway Management API

```bash
# List
curl https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways \
  -H "Authorization: Bearer $CF_API_TOKEN"

# Get
curl .../gateways/{gateway_id}

# Update
curl -X PUT .../gateways/{gateway_id} \
  -d '{"cache_ttl":7200,"rate_limiting_limit":200}'

# Delete
curl -X DELETE .../gateways/{gateway_id}
```


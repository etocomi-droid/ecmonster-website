### REST API

```bash
# Enable
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cache/cache_reserve" \
  -H "Authorization: Bearer $API_TOKEN" -H "Content-Type: application/json" \
  -d '{"value": "on"}'

# Check status
curl -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cache/cache_reserve" \
  -H "Authorization: Bearer $API_TOKEN"
```


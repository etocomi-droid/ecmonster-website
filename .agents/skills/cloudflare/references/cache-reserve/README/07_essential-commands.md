## Essential Commands

```bash
# Check Cache Reserve status
curl -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cache/cache_reserve" \
  -H "Authorization: Bearer $API_TOKEN"

# Enable Cache Reserve
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/cache/cache_reserve" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"value": "on"}'

# Check asset cache status
curl -I https://example.com/asset.jpg | grep -i cache
```


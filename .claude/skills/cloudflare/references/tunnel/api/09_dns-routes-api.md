## DNS Routes API

```bash
# Create DNS route
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}/connections" \
  -H "Authorization: Bearer ${CF_API_TOKEN}" \
  --data '{"hostname": "app.example.com"}'

# Delete route
curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}/connections/{route_id}" \
  -H "Authorization: Bearer ${CF_API_TOKEN}"
```


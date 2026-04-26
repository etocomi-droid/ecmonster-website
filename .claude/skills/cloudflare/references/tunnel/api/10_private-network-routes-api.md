## Private Network Routes API

```bash
# Add IP route
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}/routes" \
  -H "Authorization: Bearer ${CF_API_TOKEN}" \
  --data '{"ip_network": "10.0.0.0/8"}'

# List IP routes
curl -X GET "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}/routes" \
  -H "Authorization: Bearer ${CF_API_TOKEN}"
```

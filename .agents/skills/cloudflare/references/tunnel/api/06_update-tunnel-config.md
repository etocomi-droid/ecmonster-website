## Update Tunnel Config

### cURL
```bash
curl -X PUT "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}/configurations" \
  -H "Authorization: Bearer ${CF_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{
    "config": {
      "ingress": [
        {"hostname": "app.example.com", "service": "http://localhost:8000"},
        {"service": "http_status:404"}
      ]
    }
  }'
```

### TypeScript
```typescript
const config = await cf.zeroTrust.tunnels.configurations.update(
  tunnelId,
  {
    account_id: accountId,
    config: {
      ingress: [
        { hostname: 'app.example.com', service: 'http://localhost:8000' },
        { service: 'http_status:404' },
      ],
    },
  }
);
```


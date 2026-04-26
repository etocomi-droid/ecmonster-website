## Get Tunnel Info

### cURL
```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}" \
  -H "Authorization: Bearer ${CF_API_TOKEN}"
```

### TypeScript
```typescript
const tunnel = await cf.zeroTrust.tunnels.get(tunnelId, {
  account_id: accountId,
});

console.log(`Status: ${tunnel.status}`);
console.log(`Connections: ${tunnel.connections?.length || 0}`);
```


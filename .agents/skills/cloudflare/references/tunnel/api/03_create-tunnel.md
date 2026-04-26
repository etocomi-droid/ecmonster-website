## Create Tunnel

### cURL
```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels" \
  -H "Authorization: Bearer ${CF_API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{
    "name": "my-tunnel",
    "tunnel_secret": "<base64-secret>"
  }'
```

### TypeScript
```typescript
const tunnel = await cf.zeroTrust.tunnels.create({
  account_id: accountId,
  name: 'my-tunnel',
  tunnel_secret: Buffer.from(crypto.randomBytes(32)).toString('base64'),
});

console.log(`Tunnel ID: ${tunnel.id}`);
```


## List Tunnels

### cURL
```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels" \
  -H "Authorization: Bearer ${CF_API_TOKEN}"
```

### TypeScript
```typescript
const tunnels = await cf.zeroTrust.tunnels.list({
  account_id: accountId,
});

for (const tunnel of tunnels.result) {
  console.log(`${tunnel.name}: ${tunnel.id}`);
}
```


## Delete Tunnel

### cURL
```bash
curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/{account_id}/tunnels/{tunnel_id}" \
  -H "Authorization: Bearer ${CF_API_TOKEN}"
```

### TypeScript
```typescript
await cf.zeroTrust.tunnels.delete(tunnelId, {
  account_id: accountId,
});
```


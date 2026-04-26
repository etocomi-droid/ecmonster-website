## Token-Based Tunnels (Config Source: Cloudflare)

Token-based tunnels store config in Cloudflare dashboard instead of local files.

### Via Dashboard
1. **Zero Trust** > **Networks** > **Tunnels**
2. **Create a tunnel** > **Cloudflared**
3. Configure routes in dashboard
4. Copy token
5. Run on origin:
```bash
cloudflared service install <TOKEN>
```

### Via Token
```bash
# Run with token (no config file needed)
cloudflared tunnel --no-autoupdate run --token ${TUNNEL_TOKEN}

# Docker
docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token ${TUNNEL_TOKEN}
```

### Get Tunnel Token (TypeScript)
```typescript
// Get tunnel to retrieve token
const tunnel = await cf.zeroTrust.tunnels.get(tunnelId, {
  account_id: accountId,
});

// Token available in tunnel.token (only for config source: cloudflare)
const token = tunnel.token;
```


## Integration with Cloudflare Tunnel

To connect Workers to private networks, combine TCP Sockets with Cloudflare Tunnel:

```
Worker (TCP Socket) → Tunnel hostname → cloudflared → Private Network
```

### Quick Setup

1. **Install cloudflared** on a server inside your private network
2. **Create tunnel**: `cloudflared tunnel create my-private-network`
3. **Configure routing** in `config.yml`:

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /path/to/<TUNNEL_ID>.json
ingress:
  - hostname: db.internal.example.com
    service: tcp://10.0.1.50:5432
  - service: http_status:404  # Required catch-all
```

4. **Run tunnel**: `cloudflared tunnel run my-private-network`
5. **Connect from Worker**:

```typescript
const socket = connect(
  { hostname: "db.internal.example.com", port: 5432 },  // Tunnel hostname
  { secureTransport: "on" }
);
```

For detailed Tunnel setup, see [Tunnel configuration reference](../tunnel/configuration.md).


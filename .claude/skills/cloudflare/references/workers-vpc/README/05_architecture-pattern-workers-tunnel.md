## Architecture Pattern: Workers + Tunnel

Most private network connectivity combines TCP Sockets with Cloudflare Tunnel:

```
┌─────────┐     ┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Worker  │────▶│ TCP Socket  │────▶│   Tunnel     │────▶│   Private   │
│         │     │ (this API)  │     │ (cloudflared)│     │   Network   │
└─────────┘     └─────────────┘     └──────────────┘     └─────────────┘
```

1. Worker opens TCP socket to Tunnel hostname
2. Tunnel endpoint routes to private IP
3. Response flows back through Tunnel to Worker

See [configuration.md](./configuration.md) for Tunnel setup details.


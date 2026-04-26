## Protocol Selection

Cloudflared automatically selects protocol:

| Protocol | Port | Priority | Use Case |
|----------|------|----------|----------|
| QUIC | 7844 UDP | 1st (preferred) | Low latency, best performance |
| HTTP/2 | 443 TCP | 2nd (fallback) | QUIC blocked by firewall |

**Force HTTP/2 fallback:**
```bash
cloudflared tunnel --protocol http2 run my-tunnel
```

**Verify active protocol:**
```bash
cloudflared tunnel info my-tunnel
# Shows "connections" with protocol type
```


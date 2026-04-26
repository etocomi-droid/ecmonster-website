## Pre-Flight Check

Test connectivity before deploying:

```bash
# Test DNS resolution
dig edge.argotunnel.com +short

# Test port 7844 (QUIC/UDP)
nc -zvu edge.argotunnel.com 7844

# Test port 443 (HTTP/2 fallback)
nc -zv edge.argotunnel.com 443

# Test with cloudflared
cloudflared tunnel --loglevel debug run my-tunnel
# Look for "Registered tunnel connection"
```

### Common Connectivity Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "no such host" | DNS blocked | Allow port 53 UDP/TCP |
| "context deadline exceeded" | Port 7844 blocked | Allow UDP/TCP 7844 |
| "TLS handshake timeout" | Port 443 blocked | Allow TCP 443, disable SSL inspection |


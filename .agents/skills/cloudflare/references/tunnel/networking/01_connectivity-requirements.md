## Connectivity Requirements

### Outbound Ports

Cloudflared requires outbound access on:

| Port | Protocol | Purpose | Required |
|------|----------|---------|----------|
| 7844 | TCP/UDP | Primary tunnel protocol (QUIC) | Yes |
| 443 | TCP | Fallback (HTTP/2) | Yes |

**Network path:**
```
cloudflared → edge.argotunnel.com:7844 (preferred)
cloudflared → region.argotunnel.com:443 (fallback)
```

### Firewall Rules

#### Minimal (Production)
```bash
# Outbound only
ALLOW tcp/udp 7844 to *.argotunnel.com
ALLOW tcp 443 to *.argotunnel.com
```

#### Full (Recommended)
```bash
# Tunnel connectivity
ALLOW tcp/udp 7844 to *.argotunnel.com
ALLOW tcp 443 to *.argotunnel.com

# API access (for token-based tunnels)
ALLOW tcp 443 to api.cloudflare.com

# Updates (optional)
ALLOW tcp 443 to github.com
ALLOW tcp 443 to objects.githubusercontent.com
```

### IP Ranges

Cloudflare Anycast IPs (tunnel endpoints):
```
# IPv4
198.41.192.0/24
198.41.200.0/24

# IPv6
2606:4700::/32
```

**Note:** Use DNS resolution for `*.argotunnel.com` rather than hardcoding IPs. Cloudflare may add edge locations.


## Private Network Routing

### WARP Client Requirements

Users accessing private IPs via WARP need:

```bash
# Outbound (WARP client)
ALLOW udp 500,4500 to 162.159.*.* (IPsec)
ALLOW udp 2408 to 162.159.*.* (WireGuard)
ALLOW tcp 443 to *.cloudflareclient.com
```

### Split Tunnel Configuration

Route only private networks through tunnel:

```yaml
# warp-routing config
warp-routing:
  enabled: true
```

```bash
# Add specific routes
cloudflared tunnel route ip add 10.0.0.0/8 my-tunnel
cloudflared tunnel route ip add 172.16.0.0/12 my-tunnel
cloudflared tunnel route ip add 192.168.0.0/16 my-tunnel
```

WARP users can access these IPs without VPN.


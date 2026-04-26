## Migration Strategies

### From Ngrok
```yaml
# Ngrok: ngrok http 8000
# Cloudflare Tunnel:
ingress:
  - hostname: app.example.com
    service: http://localhost:8000
  - service: http_status:404
```

### From VPN
```yaml
# Replace VPN with private network routing
warp-routing:
  enabled: true
```

```bash
cloudflared tunnel route ip add 10.0.0.0/8 my-tunnel
```

Users install WARP client instead of VPN.

## Config Source Comparison

### Local Config
```yaml
# config.yml
tunnel: <UUID>
credentials-file: /path/to/<UUID>.json

ingress:
  - hostname: app.example.com
    service: http://localhost:8000
  - service: http_status:404
```

```bash
cloudflared tunnel run my-tunnel
```

**Pros:** Version control, multi-environment, offline edits
**Cons:** Requires file distribution, manual restarts

### Cloudflare Config (Token-Based)
```bash
# No config file needed
cloudflared tunnel --no-autoupdate run --token <TOKEN>
```

Configure routes in dashboard: **Zero Trust** > **Networks** > **Tunnels** > [Tunnel] > **Public Hostname**

**Pros:** Centralized updates, no file management, instant route changes
**Cons:** Requires dashboard/API access, less portable


## Common Errors

### "Error 1016 (Origin DNS Error)"

**Cause:** Tunnel not running or not connected
**Solution:**
```bash
cloudflared tunnel info my-tunnel     # Check status
ps aux | grep cloudflared             # Verify running
journalctl -u cloudflared -n 100      # Check logs
```

### "Self-signed certificate rejected"

**Cause:** Origin using self-signed certificate
**Solution:**
```yaml
originRequest:
  noTLSVerify: true      # Dev only
  caPool: /path/to/ca.pem  # Custom CA
```

### "Connection timeout"

**Cause:** Origin slow to respond or timeout settings too low
**Solution:**
```yaml
originRequest:
  connectTimeout: 60s
  tlsTimeout: 20s
  keepAliveTimeout: 120s
```

### "Tunnel not starting"

**Cause:** Invalid config, missing credentials, or tunnel doesn't exist
**Solution:**
```bash
cloudflared tunnel ingress validate  # Validate config
ls -la ~/.cloudflared/*.json         # Verify credentials
cloudflared tunnel list              # Verify tunnel exists
```

### "Connection already registered"

**Cause:** Multiple replicas with same connector ID or stale connection
**Solution:**
```bash
# Check active connections
cloudflared tunnel info my-tunnel

# Wait 60s for stale connection cleanup, or restart with new connector ID
cloudflared tunnel run my-tunnel
```

### "Tunnel credentials rotated but connections fail"

**Cause:** Old cloudflared processes using expired credentials
**Solution:**
```bash
# Stop all cloudflared processes
pkill cloudflared

# Verify stopped
ps aux | grep cloudflared

# Restart with new credentials
cloudflared tunnel run my-tunnel
```


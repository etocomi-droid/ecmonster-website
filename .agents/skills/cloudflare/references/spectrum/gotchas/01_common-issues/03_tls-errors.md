### TLS Errors

**Problem:** TLS handshake failures, 525 errors  
**Cause:** TLS mode mismatch

| Error | TLS Mode | Problem | Solution |
|-------|----------|---------|----------|
| Connection refused | `full`/`strict` | Origin not TLS | Use `tls: "off"` or enable TLS |
| 525 cert invalid | `strict` | Self-signed cert | Use `tls: "full"` or valid cert |
| Handshake timeout | `flexible` | Origin expects TLS | Use `tls: "full"` |

**Debug:**
```bash
openssl s_client -connect app.example.com:443 -showcerts
```


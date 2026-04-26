## TLS/SSL Issues

### StartTLS Timing

**Problem:** Calling `startTls()` too early

**Solution:** Send protocol-specific STARTTLS command, wait for server OK, then call `socket.startTls()`

### Certificate Validation

**Problem:** Self-signed certs fail

**Solution:** Use proper certs or Tunnel (handles TLS termination)


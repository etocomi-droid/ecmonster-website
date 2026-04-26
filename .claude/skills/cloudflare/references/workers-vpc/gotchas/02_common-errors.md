## Common Errors

### Error: "proxy request failed"

**Causes:** Blocked destination (Cloudflare IP, localhost, port 25), DNS failure, network unreachable

**Solution:** Validate destinations, use Tunnel hostnames, catch errors with try/catch

### Error: "TCP Loop detected"

**Cause:** Worker connecting to itself

**Solution:** Connect to external service, not Worker's own hostname

### Error: "Port 25 prohibited"

**Cause:** SMTP port blocked

**Solution:** Use Email Workers API for email

### Error: "socket is not open"

**Cause:** Read/write after close

**Solution:** Always use try/finally to ensure proper closure order

### Error: Connection timeout

**Cause:** No built-in timeout

**Solution:** Use `Promise.race()`:

```typescript
const socket = connect(addr, opts);
const timeout = new Promise((_, reject) => setTimeout(() => reject(new Error('Timeout')), 5000));
await Promise.race([socket.opened, timeout]);
```


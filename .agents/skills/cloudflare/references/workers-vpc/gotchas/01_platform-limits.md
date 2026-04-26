## Platform Limits

### Connection Limits

| Limit | Value |
|-------|-------|
| Max concurrent sockets per request | 6 (hard limit) |
| Socket lifetime | Request duration |
| Connection timeout | Platform-dependent, no setting |

**Problem:** Exceeding 6 connections throws error

**Solution:** Process in batches of 6

```typescript
for (let i = 0; i < hosts.length; i += 6) {
  const batch = hosts.slice(i, i + 6).map(h => connect({ hostname: h, port: 443 }));
  await Promise.all(batch.map(async s => { /* use */ await s.close(); }));
}
```

### Blocked Destinations

Cloudflare IPs (1.1.1.1), localhost (127.0.0.1), port 25 (SMTP), Worker's own URL blocked for security.

**Solution:** Use public IPs or Tunnel hostnames: `connect({ hostname: "db.internal.company.net", port: 5432 })`

### Scope Requirements

**Problem:** Sockets created in global scope fail

**Cause:** Sockets tied to request lifecycle

**Solution:** Create inside handler: `export default { async fetch() { const socket = connect(...); } }`


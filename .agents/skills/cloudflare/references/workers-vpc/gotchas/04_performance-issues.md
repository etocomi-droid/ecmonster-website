## Performance Issues

### Not Using Connection Pooling

**Problem:** New connection overhead per request

**Solution:** Use [Hyperdrive](../hyperdrive/) for databases (built-in pooling)

### Not Using Smart Placement

**Problem:** High latency to backend

**Solution:** Enable: `{ "placement": { "mode": "smart" } }` in wrangler.jsonc

### Forgetting to Close Sockets

**Problem:** Resource leaks

**Solution:** Always use try/finally:

```typescript
const socket = connect({ hostname: "api.internal", port: 443 });
try {
  // Use socket
} finally {
  await socket.close();
}
```


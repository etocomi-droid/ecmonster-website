## Execution Context

```typescript
ctx.waitUntil(logAnalytics(request));  // Background work, don't block response
ctx.passThroughOnException();  // Failover to origin on error
```

**Never** `await` background operations - use `ctx.waitUntil()`.


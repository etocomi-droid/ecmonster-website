## Rate-Limited Auto-Reply

```typescript
const rateKey = `rate:${message.from}`;
if (!await env.RATE_LIMIT.get(rateKey)) {
  // Send reply...
  ctx.waitUntil(env.RATE_LIMIT.put(rateKey, '1', { expirationTtl: 3600 }));
}
```


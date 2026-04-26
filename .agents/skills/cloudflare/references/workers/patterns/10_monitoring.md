## Monitoring

```typescript
const start = Date.now();
const response = await handleRequest(request, env);
ctx.waitUntil(env.ANALYTICS.writeDataPoint({
  doubles: [Date.now() - start], blobs: [request.url, String(response.status)]
}));
```


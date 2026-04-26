## Background Tasks (waitUntil)

Non-blocking tasks after response sent (analytics, cleanup, webhooks):

```typescript
export async function onRequest(ctx: EventContext<Env>) {
  const res = Response.json({ success: true });
  
  ctx.waitUntil(ctx.env.KV.put('last-visit', new Date().toISOString()));
  ctx.waitUntil(Promise.all([
    ctx.env.ANALYTICS.writeDataPoint({ event: 'view' }),
    fetch('https://webhook.site/...', { method: 'POST' })
  ]));
  
  return res; // Returned immediately
}
```


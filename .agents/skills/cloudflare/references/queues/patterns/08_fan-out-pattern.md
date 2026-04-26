## Fan-out Pattern

```typescript
async fetch(request: Request, env: Env): Promise<Response> {
  const event = await request.json();
  
  // Send to multiple queues for parallel processing
  await Promise.all([
    env.ANALYTICS_QUEUE.send(event),
    env.NOTIFICATIONS_QUEUE.send(event),
    env.AUDIT_LOG_QUEUE.send(event)
  ]);
  
  return Response.json({ status: 'processed' });
}
```


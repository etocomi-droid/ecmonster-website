## Buffering API Calls

```typescript
// Producer: Queue log entries
ctx.waitUntil(env.LOGS_QUEUE.send({
  method: request.method,
  url: request.url,
  timestamp: Date.now()
}));

// Consumer: Batch write to external API
async queue(batch: MessageBatch, env: Env): Promise<void> {
  const logs = batch.messages.map(m => m.body);
  await fetch(env.LOG_ENDPOINT, { method: 'POST', body: JSON.stringify({ logs }) });
  batch.ackAll();
}
```


## Idempotency Pattern

```typescript
async queue(batch: MessageBatch, env: Env): Promise<void> {
  for (const msg of batch.messages) {
    // Check if already processed
    const processed = await env.PROCESSED_KV.get(msg.id);
    if (processed) {
      msg.ack();
      continue;
    }
    
    await processMessage(msg.body);
    await env.PROCESSED_KV.put(msg.id, '1', { expirationTtl: 86400 });
    msg.ack();
  }
}
```


## Event-Driven Workflows

```typescript
// R2 event → Queue → Worker
export default {
  async queue(batch: MessageBatch, env: Env): Promise<void> {
    for (const msg of batch.messages) {
      const event = msg.body;
      if (event.action === 'PutObject') {
        await processNewFile(event.object.key, env);
      } else if (event.action === 'DeleteObject') {
        await cleanupReferences(event.object.key, env);
      }
      msg.ack();
    }
  }
};
```


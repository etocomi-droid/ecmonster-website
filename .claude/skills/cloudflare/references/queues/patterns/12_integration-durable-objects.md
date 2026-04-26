## Integration: Durable Objects

```typescript
// Queue distributes work to Durable Objects by ID
async queue(batch: MessageBatch, env: Env): Promise<void> {
  for (const msg of batch.messages) {
    const { userId, action } = msg.body;
    
    // Route to user-specific DO
    const id = env.USER_DO.idFromName(userId);
    const stub = env.USER_DO.get(id);
    
    try {
      await stub.fetch(new Request('https://do/process', {
        method: 'POST',
        body: JSON.stringify({ action, messageId: msg.id })
      }));
      msg.ack();
    } catch (error) {
      msg.retry({ delaySeconds: 60 });
    }
  }
}
```

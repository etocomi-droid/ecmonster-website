## Integration: D1 Batch Writes

```typescript
async queue(batch: MessageBatch, env: Env): Promise<void> {
  // Collect all inserts for single D1 batch
  const statements = batch.messages.map(msg => 
    env.DB.prepare('INSERT INTO events (id, data, created) VALUES (?, ?, ?)')
      .bind(msg.id, JSON.stringify(msg.body), Date.now())
  );
  
  try {
    await env.DB.batch(statements);
    batch.ackAll();
  } catch (error) {
    console.error('D1 batch failed:', error);
    batch.retryAll({ delaySeconds: 60 });
  }
}
```


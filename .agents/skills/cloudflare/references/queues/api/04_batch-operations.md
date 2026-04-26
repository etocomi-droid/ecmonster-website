## Batch Operations

```typescript
// Acknowledge entire batch
try {
  await bulkProcess(batch.messages);
  batch.ackAll();
} catch (error) {
  batch.retryAll({ delaySeconds: 300 });
}
```


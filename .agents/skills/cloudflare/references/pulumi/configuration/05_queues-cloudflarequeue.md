## Queues (cloudflare.Queue)

```typescript
const queue = new cloudflare.Queue("my-queue", {accountId, name: "my-queue"});

// Producer
const producer = new cloudflare.WorkerScript("producer", {
    accountId, name: "producer", content: code,
    queueBindings: [{name: "MY_QUEUE", queue: queue.id}],
});

// Consumer
const consumer = new cloudflare.WorkerScript("consumer", {
    accountId, name: "consumer", content: code,
    queueConsumers: [{queue: queue.name, maxBatchSize: 10, maxRetries: 3}],
});
```


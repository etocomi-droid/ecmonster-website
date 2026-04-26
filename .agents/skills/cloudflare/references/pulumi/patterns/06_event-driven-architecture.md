## Event-Driven Architecture

```typescript
const eventQueue = new cloudflare.Queue("events", {accountId, name: "event-bus"});
const producer = new cloudflare.WorkerScript("producer", {
    accountId, name: "api-producer", content: producerCode,
    queueBindings: [{name: "EVENTS", queue: eventQueue.id}],
});
const consumer = new cloudflare.WorkerScript("consumer", {
    accountId, name: "email-consumer", content: consumerCode,
    queueConsumers: [{queue: eventQueue.name, maxBatchSize: 10}],
});
```


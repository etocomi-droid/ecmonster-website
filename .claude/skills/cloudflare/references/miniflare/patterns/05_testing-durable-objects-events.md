## Testing Durable Objects & Events

```js
// Durable Objects
const ns = await mf.getDurableObjectNamespace("COUNTER");
const stub = ns.get(ns.idFromName("test-counter"));
await stub.fetch("http://localhost/increment");

// Direct storage
const storage = await mf.getDurableObjectStorage(ns.idFromName("test-counter"));
const count = await storage.get("count");

// Queue
const worker = await mf.getWorker();
await worker.queue("my-queue", [
  { id: "msg1", timestamp: new Date(), body: { userId: 123 }, attempts: 1 },
]);

// Scheduled
await worker.scheduled({ cron: "0 0 * * *" });
```


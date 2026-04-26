## Queue-Based Processing

```typescript
const queue = new cloudflare.Queue("processing-queue", {accountId, name: "image-processing"});

// Producer: API receives requests
const apiWorker = new cloudflare.WorkerScript("api", {
    accountId, name: "api-worker", content: apiCode,
    queueBindings: [{name: "PROCESSING_QUEUE", queue: queue.id}],
});

// Consumer: Process async
const processorWorker = new cloudflare.WorkerScript("processor", {
    accountId, name: "processor-worker", content: processorCode,
    queueConsumers: [{queue: queue.name, maxBatchSize: 10, maxRetries: 3, maxWaitTimeMs: 5000}],
    r2BucketBindings: [{name: "OUTPUT_BUCKET", bucketName: outputBucket.name}],
});
```


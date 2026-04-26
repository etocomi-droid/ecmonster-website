## Task Queue

```ts
await this.queue("processVideo", { videoId: "abc123" }); // Add task
const tasks = await this.dequeue(10); // Process up to 10
```


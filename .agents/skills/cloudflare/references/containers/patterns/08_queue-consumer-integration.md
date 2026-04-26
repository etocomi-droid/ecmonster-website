## Queue Consumer Integration

```typescript
export default {
  async queue(batch, env) {
    for (const msg of batch.messages) {
      try {
        const container = env.PROCESSOR.getByName(msg.body.jobId);
        await container.startAndWaitForPorts();
        
        const response = await container.fetch("/process", {
          method: "POST",
          body: JSON.stringify(msg.body)
        });
        
        response.ok ? msg.ack() : msg.retry();
      } catch (err) {
        console.error("Queue processing error:", err);
        msg.retry();
      }
    }
  }
};
```

**Use:** Asynchronous job processing, batch operations, event-driven execution.

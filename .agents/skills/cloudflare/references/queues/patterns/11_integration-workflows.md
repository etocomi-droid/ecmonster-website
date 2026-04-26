## Integration: Workflows

```typescript
// Queue triggers Workflow for long-running tasks
async queue(batch: MessageBatch, env: Env): Promise<void> {
  for (const msg of batch.messages) {
    try {
      const instance = await env.MY_WORKFLOW.create({
        id: msg.id,
        params: msg.body
      });
      console.log('Workflow started:', instance.id);
      msg.ack();
    } catch (error) {
      msg.retry({ delaySeconds: 30 });
    }
  }
}
```


## Triggering Workflows

```typescript
// From Worker
export default { async fetch(req, env) { const instance = await env.MY_WORKFLOW.create({id: crypto.randomUUID(), params: { userId: 'user123' }}); return Response.json({ id: instance.id }); }};

// From Queue
export default { async queue(batch, env) { for (const msg of batch.messages) { await env.MY_WORKFLOW.create({id: `job-${msg.id}`, params: msg.body}); } }};

// From Cron
export default { async scheduled(event, env) { await env.CLEANUP_WORKFLOW.create({id: `cleanup-${Date.now()}`, params: { timestamp: event.scheduledTime }}); }};

// From Another Workflow (non-blocking)
export class ParentWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event, step) {
    const child = await step.do('start child', async () => await this.env.CHILD_WORKFLOW.create({id: `child-${event.instanceId}`, params: {}}));
  }
}
```


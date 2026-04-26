## Orchestration Patterns

### Fan-Out (Parallel Processing)
```typescript
const files = await step.do('list', async () => this.env.BUCKET.list());
await Promise.all(files.objects.map((file, i) => step.do(`process ${i}`, async () => processFile(await (await this.env.BUCKET.get(file.key)).arrayBuffer()))));
```

### Parent-Child Workflows
```typescript
const child = await step.do('start child', async () => await this.env.CHILD_WORKFLOW.create({id: `child-${event.instanceId}`, params: { data: result.data }}));
await step.do('other work', async () => console.log(`Child started: ${child.id}`));
```

### Race Pattern
```typescript
const winner = await Promise.race([
  step.do('option A', async () => slowOperation()),
  step.do('option B', async () => fastOperation())
]);
```

### Scheduled Workflow Chain
```typescript
export default { async scheduled(event, env) { await env.DAILY_WORKFLOW.create({id: `daily-${event.scheduledTime}`, params: { timestamp: event.scheduledTime }}); }};
export class DailyWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event, step) {
    await step.do('daily task', async () => {});
    await step.sleep('wait 7 days', '7 days');
    await step.do('weekly followup', async () => {});
  }
}
```

See: [configuration.md](./configuration.md), [api.md](./api.md), [gotchas.md](./gotchas.md)

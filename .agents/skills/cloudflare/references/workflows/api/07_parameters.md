## Parameters

**Pass from Worker:**
```typescript
const instance = await env.MY_WORKFLOW.create({
  id: crypto.randomUUID(),
  params: { userId: 'user123', email: 'user@example.com' }
});
```

**Access in Workflow:**
```typescript
async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
  const userId = event.payload.userId;
  const instanceId = event.instanceId;
  const createdAt = event.timestamp;
}
```

**CLI Trigger:**
```bash
npx wrangler workflows trigger my-workflow '{"userId":"user123"}'
```


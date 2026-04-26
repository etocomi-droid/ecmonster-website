## Instance Management

```typescript
// Create single
const instance = await env.MY_WORKFLOW.create({id: crypto.randomUUID(), params: { userId: 'user123' }}); // id optional, auto-generated if omitted

// Create with custom retention (default: 3 days free, 30 days paid)
const instance = await env.MY_WORKFLOW.create({
  id: crypto.randomUUID(),
  params: { userId: 'user123' },
  retention: '30 days'  // Override default retention period
});

// Batch (max 100, idempotent: skips existing IDs)
const instances = await env.MY_WORKFLOW.createBatch([{id: 'user1', params: {name: 'John'}}, {id: 'user2', params: {name: 'Jane'}}]);

// Get & Status
const instance = await env.MY_WORKFLOW.get('instance-id');
const status = await instance.status(); // {status: 'queued' | 'running' | 'paused' | 'errored' | 'terminated' | 'complete' | 'waiting' | 'waitingForPause' | 'unknown', error?, output?}

// Control
await instance.pause(); await instance.resume(); await instance.terminate(); await instance.restart();

// Send Events
await instance.sendEvent({type: 'approval', payload: { approved: true }}); // Must match waitForEvent type
```


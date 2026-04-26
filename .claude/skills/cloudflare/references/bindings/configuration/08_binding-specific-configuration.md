## Binding-Specific Configuration

### Durable Objects with Class Export

```jsonc
{
  "durable_objects": {
    "bindings": [
      { "name": "COUNTER", "class_name": "Counter", "script_name": "my-worker" }
    ]
  }
}
```

```typescript
// In same Worker or script_name Worker
export class Counter {
  constructor(private state: DurableObjectState, private env: Env) {}
  async fetch(request: Request) { /* ... */ }
}
```

### Queue Consumers

```jsonc
{
  "queues": {
    "producers": [{ "binding": "MY_QUEUE", "queue": "my-queue" }],
    "consumers": [{ "queue": "my-queue", "max_batch_size": 10 }]
  }
}
```

Queue consumer handler: `export default { async queue(batch, env) { /* process batch.messages */ } }`


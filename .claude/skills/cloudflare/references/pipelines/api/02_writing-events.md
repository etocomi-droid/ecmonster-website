## Writing Events

### Single Event

```typescript
await env.STREAM.send([{
  user_id: "12345",
  event_type: "purchase",
  product_id: "widget-001",
  amount: 29.99
}]);
```

### Batch Events

```typescript
const events = [
  { user_id: "user1", event_type: "view" },
  { user_id: "user2", event_type: "purchase", amount: 50 }
];
await env.STREAM.send(events);
```

**Limits:**
- Max 1 MB per request
- 5 MB/s per stream

### Fire-and-Forget Pattern

```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const event = { /* ... */ };
    
    // Don't block response on send
    ctx.waitUntil(env.STREAM.send([event]));
    
    return new Response('OK');
  }
};
```

### Error Handling

```typescript
try {
  await env.STREAM.send([event]);
} catch (error) {
  console.error('Pipeline send failed:', error);
  // Log to another system, retry, or return error response
  return new Response('Failed to track event', { status: 500 });
}
```


## Service Bindings

```typescript
// Worker-to-worker RPC (zero latency, no internet round-trip)
return env.SERVICE_B.fetch(request);

// With RPC (2024+) - same as Durable Objects RPC
export class ServiceWorker {
  async getData() { return { data: 'value' }; }
}
// Usage: const data = await env.SERVICE_B.getData();
```

**Benefits**: Type-safe method calls, no HTTP overhead, share code between Workers


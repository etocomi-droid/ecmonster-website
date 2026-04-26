## Durable Objects

### RPC Pattern (Recommended 2024+)

```typescript
export class Counter {
  private value = 0;
  
  constructor(private state: DurableObjectState) {
    state.blockConcurrencyWhile(async () => {
      this.value = (await state.storage.get('value')) || 0;
    });
  }
  
  // Export methods directly - called via RPC (type-safe, zero serialization)
  async increment(): Promise<number> {
    this.value++;
    await this.state.storage.put('value', this.value);
    return this.value;
  }
  
  async getValue(): Promise<number> {
    return this.value;
  }
}

// Worker usage:
const stub = env.COUNTER.get(env.COUNTER.idFromName('global'));
const count = await stub.increment(); // Direct method call, full type safety
```

### Legacy Fetch Pattern (Pre-2024)

```typescript
async fetch(request: Request): Promise<Response> {
  const url = new URL(request.url);
  if (url.pathname === '/increment') {
    await this.state.storage.put('value', ++this.value);
  }
  return new Response(String(this.value));
}
// Usage: await stub.fetch('http://x/increment')
```

**When to use DOs**: Real-time collaboration, rate limiting, strongly consistent state


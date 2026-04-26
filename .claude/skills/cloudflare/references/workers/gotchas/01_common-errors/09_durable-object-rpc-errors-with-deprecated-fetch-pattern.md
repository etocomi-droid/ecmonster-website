### "Durable Object RPC errors with deprecated fetch pattern"

**Cause:** Using old `stub.fetch()` pattern instead of RPC (2024+)  
**Solution:** Export methods directly, call via RPC:

```typescript
// ❌ Old fetch pattern
export class MyDO {
  async fetch(request: Request) {
    const { method } = await request.json();
    if (method === 'increment') return new Response(String(await this.increment()));
  }
  async increment() { return ++this.value; }
}
const stub = env.DO.get(id);
const res = await stub.fetch('http://x', { method: 'POST', body: JSON.stringify({ method: 'increment' }) });

// ✅ RPC pattern (type-safe, no serialization overhead)
export class MyDO {
  async increment() { return ++this.value; }
}
const stub = env.DO.get(id);
const count = await stub.increment(); // Direct method call
```


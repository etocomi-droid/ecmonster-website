## Concurrency Model (CRITICAL)

Durable Objects use **input/output gates** to prevent race conditions:

### Input Gates
Block new requests during storage reads from CURRENT request:

```typescript
// SAFE: Input gate active during await
async increment() {
  const val = await this.ctx.storage.get("counter"); // Input gate blocks other requests
  await this.ctx.storage.put("counter", val + 1);
  return val;
}
```

### Output Gates
Hold response until ALL writes from current request confirm:

```typescript
// SAFE: Output gate waits for put() to confirm before returning response
async increment() {
  const val = await this.ctx.storage.get("counter");
  this.ctx.storage.put("counter", val + 1); // No await
  return new Response(String(val)); // Response delayed until write confirms
}
```

### Write Coalescing
Multiple writes to same key = atomic (last write wins):

```typescript
// SAFE: All three writes coalesce atomically
this.ctx.storage.put("key", 1);
this.ctx.storage.put("key", 2);
this.ctx.storage.put("key", 3); // Final value: 3
```

### Breaking Gates (DANGER)

**fetch() breaks input/output gates** → allows request interleaving:

```typescript
// UNSAFE: fetch() allows another request to interleave
async unsafe() {
  const val = await this.ctx.storage.get("counter");
  await fetch("https://api.example.com"); // Gate broken!
  await this.ctx.storage.put("counter", val + 1); // Race condition possible
}
```

**Solution:** Use `blockConcurrencyWhile()` or `transaction()`:

```typescript
// SAFE: Block concurrent requests explicitly
async safe() {
  return await this.ctx.blockConcurrencyWhile(async () => {
    const val = await this.ctx.storage.get("counter");
    await fetch("https://api.example.com");
    await this.ctx.storage.put("counter", val + 1);
    return val;
  });
}
```

### allowConcurrency Option

Opt out of input gate for reads that don't need protection:

```typescript
// Allow concurrent reads (no consistency guarantee)
const val = await this.ctx.storage.get("metrics", { allowConcurrency: true });
```


## Safe Counter / Optimized Write

```typescript
// Input gate blocks other requests
async getUniqueNumber(): Promise<number> {
  let val = await this.ctx.storage.get("counter");
  await this.ctx.storage.put("counter", val + 1);
  return val;
}

// No await on write - output gate delays response until write confirms
async increment(): Promise<Response> {
  let val = await this.ctx.storage.get("counter");
  this.ctx.storage.put("counter", val + 1);
  return new Response(String(val));
}
```


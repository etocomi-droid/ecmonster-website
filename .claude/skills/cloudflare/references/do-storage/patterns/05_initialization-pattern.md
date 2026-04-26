## Initialization Pattern

```typescript
export class Counter extends DurableObject {
  value: number;
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    ctx.blockConcurrencyWhile(async () => { this.value = (await ctx.storage.get("value")) || 0; });
  }
  async increment() {
    this.value++;
    this.ctx.storage.put("value", this.value); // Don't await (output gate protects)
    return this.value;
  }
}
```


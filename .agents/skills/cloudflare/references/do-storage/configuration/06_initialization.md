## Initialization

```typescript
export class Counter extends DurableObject {
  value: number;
  
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    
    // Block concurrent requests during init
    ctx.blockConcurrencyWhile(async () => {
      this.value = (await ctx.storage.get("value")) || 0;
    });
  }
}
```

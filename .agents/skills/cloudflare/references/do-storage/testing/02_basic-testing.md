## Basic Testing

```typescript
import { env, runInDurableObject } from "cloudflare:test";
import { describe, it, expect } from "vitest";

describe("Counter DO", () => {
  it("increments counter", async () => {
    const id = env.COUNTER.idFromName("test");
    const result = await runInDurableObject(env.COUNTER, id, async (instance, state) => {
      const val1 = await instance.increment();
      const val2 = await instance.increment();
      return { val1, val2 };
    });
    expect(result.val1).toBe(1);
    expect(result.val2).toBe(2);
  });
});
```


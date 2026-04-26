## getPlatformProxy

Lightweight unit testing - provides bindings without full Worker runtime.

```js
// vitest.config.js
export default { test: { environment: "node" } };
```

```js
import { env } from "cloudflare:test";
import { describe, it, expect } from "vitest";

describe("Business logic", () => {
  it("processes data with KV", async () => {
    await env.KV.put("test", "value");
    expect(await env.KV.get("test")).toBe("value");
  });
});
```

**Pros:** Fast, simple  
**Cons:** No full runtime, can't test fetch handler


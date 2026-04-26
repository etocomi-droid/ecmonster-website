## vitest-pool-workers

Full Workers runtime in Vitest. Reads `wrangler.toml`.

```bash
npm i -D @cloudflare/vitest-pool-workers
```

```js
// vitest.config.js
import { defineWorkersConfig } from "@cloudflare/vitest-pool-workers/config";

export default defineWorkersConfig({
  test: {
    poolOptions: { workers: { wrangler: { configPath: "./wrangler.toml" } } },
  },
});
```

```js
import { env, SELF } from "cloudflare:test";
import { it, expect } from "vitest";

it("handles fetch", async () => {
  const res = await SELF.fetch("http://example.com/");
  expect(res.status).toBe(200);
});
```

**Pros:** Full runtime, uses wrangler.toml  
**Cons:** Requires Wrangler config


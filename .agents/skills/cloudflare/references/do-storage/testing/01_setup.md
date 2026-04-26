## Setup

**vitest.config.ts:**
```typescript
import { defineWorkersConfig } from "@cloudflare/vitest-pool-workers/config";

export default defineWorkersConfig({
  test: {
    poolOptions: {
      workers: { wrangler: { configPath: "./wrangler.toml" } }
    }
  }
});
```

**package.json:** Add `@cloudflare/vitest-pool-workers` and `vitest` to devDependencies


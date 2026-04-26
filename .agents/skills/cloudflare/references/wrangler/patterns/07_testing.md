## Testing

### Integration Tests with Node.js Test Runner

```typescript
import { startWorker } from "wrangler";
import { describe, it, before, after } from "node:test";
import assert from "node:assert";

describe("API", () => {
  let worker;
  
  before(async () => {
    worker = await startWorker({ 
      config: "wrangler.jsonc",
      remote: "minimal"  // Fast tests with real bindings
    });
  });
  
  after(async () => await worker.dispose());
  
  it("creates user", async () => {
    const response = await worker.fetch("http://example.com/api/users", {
      method: "POST",
      body: JSON.stringify({ name: "Alice" })
    });
    assert.strictEqual(response.status, 201);
  });
});
```

### Testing with Vitest

Install: `npm install -D vitest @cloudflare/vitest-pool-workers`

**vitest.config.ts:**
```typescript
import { defineWorkersConfig } from "@cloudflare/vitest-pool-workers/config";
export default defineWorkersConfig({
  test: { poolOptions: { workers: { wrangler: { configPath: "./wrangler.jsonc" } } } }
});
```

**tests/api.test.ts:**
```typescript
import { env, SELF } from "cloudflare:test";
import { describe, it, expect } from "vitest";

it("fetches users", async () => {
  const response = await SELF.fetch("https://example.com/api/users");
  expect(response.status).toBe(200);
});

it("uses bindings", async () => {
  await env.MY_KV.put("key", "value");
  expect(await env.MY_KV.get("key")).toBe("value");
});
```

### Multi-Worker Development (Service Bindings)

```typescript
const authWorker = await startWorker({ config: "./auth/wrangler.jsonc" });
const apiWorker = await startWorker({
  config: "./api/wrangler.jsonc",
  bindings: { AUTH: authWorker }  // Service binding
});

// Test API calling AUTH
const response = await apiWorker.fetch("http://example.com/api/protected");
await authWorker.dispose();
await apiWorker.dispose();
```

### Mock External APIs

```typescript
const worker = await startWorker({ 
  config: "wrangler.jsonc",
  outboundService: (req) => {
    const url = new URL(req.url);
    if (url.hostname === "api.external.com") {
      return new Response(JSON.stringify({ mocked: true }), {
        headers: { "content-type": "application/json" }
      });
    }
    return fetch(req);  // Pass through other requests
  }
});

// Test Worker that calls external API
const response = await worker.fetch("http://example.com/proxy");
// Worker internally fetches api.external.com - gets mocked response
```


## startWorker (Testing)

Starts Worker with real local bindings for integration tests. Stable API (replaces `unstable_startWorker`).

```typescript
import { startWorker } from "wrangler";
import { describe, it, before, after } from "node:test";
import assert from "node:assert";

describe("worker", () => {
  let worker;
  
  before(async () => {
    worker = await startWorker({
      config: "wrangler.jsonc",
      environment: "development"
    });
  });
  
  after(async () => {
    await worker.dispose();
  });
  
  it("responds with 200", async () => {
    const response = await worker.fetch("http://example.com");
    assert.strictEqual(response.status, 200);
  });
});
```

### Options

| Option | Type | Description |
|--------|------|-------------|
| `config` | `string` | Path to wrangler.jsonc |
| `environment` | `string` | Environment name from config |
| `persist` | `boolean \| { path: string }` | Enable persistent state |
| `bundle` | `boolean` | Enable bundling (default: true) |
| `remote` | `false \| true \| "minimal"` | Remote mode: `false` (local), `true` (full remote), `"minimal"` (remote bindings only) |

### Remote Mode

```typescript
// Local mode (default) - fast, simulated
const worker = await startWorker({ config: "wrangler.jsonc" });

// Full remote mode - production-like, slower
const worker = await startWorker({ 
  config: "wrangler.jsonc",
  remote: true 
});

// Minimal remote mode - remote bindings, local Worker
const worker = await startWorker({ 
  config: "wrangler.jsonc",
  remote: "minimal"
});
```


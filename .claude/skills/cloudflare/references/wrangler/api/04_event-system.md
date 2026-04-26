## Event System

Listen to Worker lifecycle events for advanced workflows.

```typescript
import { startWorker } from "wrangler";

const worker = await startWorker({
  config: "wrangler.jsonc",
  bundle: true
});

// Bundle events
worker.on("bundleStart", (details) => {
  console.log("Bundling started:", details.config);
});

worker.on("bundleComplete", (details) => {
  console.log("Bundle ready:", details.duration);
});

// Reconfiguration events
worker.on("reloadStart", () => {
  console.log("Worker reloading...");
});

worker.on("reloadComplete", () => {
  console.log("Worker reloaded");
});

await worker.dispose();
```

### Dynamic Reconfiguration

```typescript
import { startWorker } from "wrangler";

const worker = await startWorker({ config: "wrangler.jsonc" });

// Replace entire config
await worker.setConfig({
  config: "wrangler.staging.jsonc",
  environment: "staging"
});

// Patch specific fields
await worker.patchConfig({
  vars: { DEBUG: "true" }
});

await worker.dispose();
```


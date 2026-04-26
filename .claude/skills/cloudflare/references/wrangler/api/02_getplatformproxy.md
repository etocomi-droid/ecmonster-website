## getPlatformProxy

Emulate bindings in Node.js without starting Worker.

```typescript
import { getPlatformProxy } from "wrangler";

const { env, dispose, caches } = await getPlatformProxy<Env>({
  configPath: "wrangler.jsonc",
  environment: "production",
  persist: { path: ".wrangler/state" }
});

// Use bindings
const value = await env.MY_KV.get("key");
await env.DB.prepare("SELECT * FROM users").all();
await env.ASSETS.put("file.txt", "content");

// Platform APIs
await caches.default.put("https://example.com", new Response("cached"));

await dispose();
```

Use for unit tests (test functions, not full Worker) or scripts that need bindings.


## Multi-Worker Registry

Test multiple Workers with service bindings.

```typescript
import { startWorker } from "wrangler";

const auth = await startWorker({ config: "./auth/wrangler.jsonc" });
const api = await startWorker({
  config: "./api/wrangler.jsonc",
  bindings: { AUTH: auth }  // Service binding
});

const response = await api.fetch("http://example.com/api/login");
// API Worker calls AUTH Worker via env.AUTH.fetch()

await api.dispose();
await auth.dispose();
```


## Migration Guides

### From Miniflare 2.x to 3+

Breaking changes in v3+:

| v2 | v3+ |
|----|-----|
| `getBindings()` sync | `getBindings()` returns Promise |
| `ready` is void | `ready` returns `Promise<URL>` |
| service-worker-mock | Built on workerd |
| Different options | Restructured constructor |

**Example migration:**
```js
// v2
const bindings = mf.getBindings();
mf.ready; // void

// v3+
const bindings = await mf.getBindings();
const url = await mf.ready; // Promise<URL>
```

### From unstable_dev to Miniflare

```js
// Old (deprecated)
import { unstable_dev } from "wrangler";
const worker = await unstable_dev("src/index.ts");

// New
import { Miniflare } from "miniflare";
const mf = new Miniflare({ scriptPath: "src/index.ts" });
```

### From Wrangler Dev

Miniflare doesn't auto-read `wrangler.toml`:

```js
// Translate manually:
new Miniflare({
  scriptPath: "dist/worker.js",
  compatibilityDate: "2026-01-01",
  kvNamespaces: ["KV"],
  bindings: { API_KEY: process.env.API_KEY },
});
```


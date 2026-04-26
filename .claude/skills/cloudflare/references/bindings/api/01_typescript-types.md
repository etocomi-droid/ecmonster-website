## TypeScript Types

Cloudflare generates binding types via `npx wrangler types`. This creates `.wrangler/types/runtime.d.ts` with your Env interface.

### Generated Env Interface

After running `wrangler types`, TypeScript knows your bindings:

```typescript
interface Env {
  // From wrangler.jsonc bindings
  MY_KV: KVNamespace;
  MY_BUCKET: R2Bucket;
  DB: D1Database;
  MY_SERVICE: Fetcher;
  AI: Ai;
  
  // From vars
  API_URL: string;
  
  // From secrets (set via wrangler secret put)
  API_KEY: string;
}
```

### Binding Types

| Config | TypeScript Type | Package |
|--------|-----------------|---------|
| `kv_namespaces` | `KVNamespace` | `@cloudflare/workers-types` |
| `r2_buckets` | `R2Bucket` | `@cloudflare/workers-types` |
| `d1_databases` | `D1Database` | `@cloudflare/workers-types` |
| `durable_objects.bindings` | `DurableObjectNamespace` | `@cloudflare/workers-types` |
| `vectorize` | `VectorizeIndex` | `@cloudflare/workers-types` |
| `queues.producers` | `Queue` | `@cloudflare/workers-types` |
| `services` | `Fetcher` | `@cloudflare/workers-types` |
| `ai` | `Ai` | `@cloudflare/workers-types` |
| `browser` | `Fetcher` | `@cloudflare/workers-types` |
| `analytics_engine_datasets` | `AnalyticsEngineDataset` | `@cloudflare/workers-types` |
| `hyperdrive` | `Hyperdrive` | `@cloudflare/workers-types` |
| `rate_limiting` | `RateLimit` | `@cloudflare/workers-types` |
| `workflows` | `Workflow` | `@cloudflare/workers-types` |
| `mtls_certificates` / `vars` / `text_blobs` / `data_blobs` | `string` | Built-in |
| `wasm_modules` | `WebAssembly.Module` | Built-in |


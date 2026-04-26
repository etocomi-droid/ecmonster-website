## Bindings Reference

| Binding Type | Interface | Config Key | Use Case |
|--------------|-----------|------------|----------|
| KV | `KVNamespace` | `kv_namespaces` | Key-value cache, sessions, config |
| D1 | `D1Database` | `d1_databases` | Relational data, SQL queries |
| R2 | `R2Bucket` | `r2_buckets` | Large files, user uploads, assets |
| Durable Objects | `DurableObjectNamespace` | `durable_objects.bindings` | Stateful coordination, websockets |
| Workers AI | `Ai` | `ai.binding` | LLM inference, embeddings |
| Vectorize | `VectorizeIndex` | `vectorize` | Vector search, embeddings |
| Service Binding | `Fetcher` | `services` | Worker-to-worker RPC |
| Analytics Engine | `AnalyticsEngineDataset` | `analytics_engine_datasets` | Event logging, metrics |
| Environment Vars | `string` | `vars` | Non-sensitive config |

See [configuration.md](./configuration.md) for wrangler.jsonc examples.


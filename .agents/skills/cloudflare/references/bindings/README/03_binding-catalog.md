## Binding Catalog

### Storage Bindings

| Binding | Use Case | Access Pattern |
|---------|----------|----------------|
| **KV** | Key-value cache, CDN-backed reads | `env.MY_KV.get(key)` |
| **R2** | Object storage (S3-compatible) | `env.MY_BUCKET.get(key)` |
| **D1** | SQL database (SQLite) | `env.DB.prepare(sql).all()` |
| **Durable Objects** | Coordination, real-time state | `env.MY_DO.get(id)` |
| **Vectorize** | Vector embeddings search | `env.VECTORIZE.query(vector)` |
| **Queues** | Async message processing | `env.MY_QUEUE.send(msg)` |

### Compute Bindings

| Binding | Use Case | Access Pattern |
|---------|----------|----------------|
| **Service** | Worker-to-Worker RPC | `env.MY_SERVICE.fetch(req)` |
| **Workers AI** | LLM inference | `env.AI.run(model, input)` |
| **Browser Rendering** | Headless Chrome | `env.BROWSER.fetch(url)` |

### Platform Bindings

| Binding | Use Case | Access Pattern |
|---------|----------|----------------|
| **Analytics Engine** | Custom metrics | `env.ANALYTICS.writeDataPoint(data)` |
| **mTLS** | Client certificates | `env.MY_CERT` (string) |
| **Hyperdrive** | Database pooling | `env.HYPERDRIVE.connectionString` |
| **Rate Limiting** | Request throttling | `env.RATE_LIMITER.limit(id)` |
| **Workflows** | Long-running workflows | `env.MY_WORKFLOW.create()` |

### Configuration Bindings

| Binding | Use Case | Access Pattern |
|---------|----------|----------------|
| **Environment Variables** | Non-sensitive config | `env.API_URL` (string) |
| **Secrets** | Sensitive values | `env.API_KEY` (string) |
| **Text/Data Blobs** | Static files | `env.MY_BLOB` (string) |
| **WASM** | WebAssembly modules | `env.MY_WASM` (WebAssembly.Module) |


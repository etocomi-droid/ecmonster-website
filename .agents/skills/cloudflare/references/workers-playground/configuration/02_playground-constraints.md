## Playground Constraints

⚠️ **Important Limitations**

| Constraint | Playground | Production Workers |
|------------|------------|-------------------|
| **Module Format** | ES modules only | ES modules or Service Worker |
| **TypeScript** | Not supported (JS only) | Supported via build step |
| **Bindings** | Not available | KV, D1, R2, Durable Objects, etc. |
| **wrangler.toml** | Not used | Required for config |
| **Environment Variables** | Not available | Full support |
| **Secrets** | Not available | Full support |
| **Custom Domains** | Not available | Full support |

**Playground is for rapid prototyping only.** For production apps, use `wrangler` CLI.


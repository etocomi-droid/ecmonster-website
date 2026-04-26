## Environment Bindings

**Type-safe pattern:**

```typescript
interface Env {
  AI?: Ai;                              // Workers AI
  MyAgent?: DurableObjectNamespace<MyAgent>;
  ChatAgent?: DurableObjectNamespace<ChatAgent>;
  DB?: D1Database;                      // D1 database
  KV?: KVNamespace;                     // KV storage
  R2?: R2Bucket;                        // R2 bucket
  OPENAI_API_KEY?: string;              // Secrets
  GITHUB_CLIENT_ID?: string;            // MCP OAuth credentials
  GITHUB_CLIENT_SECRET?: string;
  QUEUE?: Queue;                        // Queues
}
```

**Best practice:** Define all DO bindings in Env interface for type safety.


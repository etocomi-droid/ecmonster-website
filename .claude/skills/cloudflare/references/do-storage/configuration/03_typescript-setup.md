## TypeScript Setup

```typescript
export class MyDurableObject extends DurableObject {
  sql: SqlStorage;
  
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;
    
    // Initialize schema
    this.sql.exec(`
      CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
      );
    `);
  }
}

// Binding
interface Env {
  MY_DO: DurableObjectNamespace;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const id = env.MY_DO.idFromName('singleton');
    const stub = env.MY_DO.get(id);
    
    // Modern RPC: call methods directly (recommended)
    const result = await stub.someMethod();
    return Response.json(result);
    
    // Legacy: forward request (still works)
    // return stub.fetch(request);
  }
}
```


## Class Structure

```typescript
import { DurableObject } from "cloudflare:workers";

export class MyDO extends DurableObject<Env> {
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    // Runs on EVERY wake - keep light!
  }
  
  // RPC methods (called directly from worker)
  async myMethod(arg: string): Promise<string> { return arg; }
  
  // fetch handler (legacy/HTTP semantics)
  async fetch(req: Request): Promise<Response> { /* ... */ }
  
  // Lifecycle handlers
  async alarm() { /* alarm fired */ }
  async webSocketMessage(ws: WebSocket, msg: string | ArrayBuffer) { /* ... */ }
  async webSocketClose(ws: WebSocket, code: number, reason: string, wasClean: boolean) { /* ... */ }
  async webSocketError(ws: WebSocket, error: unknown) { /* ... */ }
}
```


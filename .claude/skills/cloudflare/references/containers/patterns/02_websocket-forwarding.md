## WebSocket Forwarding

```typescript
export default {
  async fetch(request: Request, env: Env) {
    if (request.headers.get("Upgrade") === "websocket") {
      const sessionId = request.headers.get("X-Session-ID") || crypto.randomUUID();
      const container = env.WS_BACKEND.getByName(sessionId);
      await container.startAndWaitForPorts();
      
      // ⚠️ MUST use fetch(), not containerFetch()
      return container.fetch(request);
    }
    return new Response("Not a WebSocket request", { status: 400 });
  }
};
```

**⚠️ Critical:** Always use `fetch()` for WebSocket.


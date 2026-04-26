## Hibernation-Aware Pattern

Preserve state across hibernation:

```typescript
async fetch(req: Request): Promise<Response> {
  const [client, server] = Object.values(new WebSocketPair());
  const userId = new URL(req.url).searchParams.get("user");
  server.serializeAttachment({ userId });  // Survives hibernation
  this.ctx.acceptWebSocket(server, ["room:lobby"]);
  server.send(JSON.stringify({ type: "init", state: this.ctx.storage.kv.get("state") }));
  return new Response(null, { status: 101, webSocket: client });
}

async webSocketMessage(ws: WebSocket, msg: string) {
  const { userId } = ws.deserializeAttachment();  // Retrieve after wake
  const state = this.ctx.storage.kv.get("state") || {};
  state[userId] = JSON.parse(msg);
  this.ctx.storage.kv.put("state", state);
  for (const c of this.ctx.getWebSockets("room:lobby")) c.send(msg);
}
```


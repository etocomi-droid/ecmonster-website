## WebSocket Hibernation

Hibernation allows DOs with open WebSocket connections to consume zero compute/memory until message arrives.

```typescript
async fetch(req: Request): Promise<Response> {
  const [client, server] = Object.values(new WebSocketPair());
  this.ctx.acceptWebSocket(server, ["room:123"]);  // Tags for filtering
  server.serializeAttachment({ userId: "abc" });    // Persisted metadata
  return new Response(null, { status: 101, webSocket: client });
}

// Called when message arrives (DO wakes from hibernation)
async webSocketMessage(ws: WebSocket, msg: string | ArrayBuffer) {
  const data = ws.deserializeAttachment();          // Retrieve metadata
  for (const c of this.ctx.getWebSockets("room:123")) c.send(msg);
}

// Called on close (optional handler)
async webSocketClose(ws: WebSocket, code: number, reason: string, wasClean: boolean) {
  // Cleanup logic, remove from lists, etc.
}

// Called on error (optional handler)
async webSocketError(ws: WebSocket, error: unknown) {
  console.error("WebSocket error:", error);
  // Handle error, close connection, etc.
}
```

**Key concepts:**
- **Auto-hibernation:** DO hibernates when no active requests/alarms
- **Zero cost:** Hibernated DOs incur no charges while preserving connections
- **Memory cleared:** All in-memory state lost on hibernation
- **Attachment persistence:** Use `serializeAttachment()` for per-connection metadata that survives hibernation
- **Tags for filtering:** Group connections by room/channel/user for targeted broadcasts

**Handler lifecycle:**
- `webSocketMessage`: DO wakes, processes message, may hibernate after
- `webSocketClose`: Called when client closes (optional - implement for cleanup)
- `webSocketError`: Called on connection error (optional - implement for error handling)

**Metadata persistence:**
```typescript
// Store connection metadata (survives hibernation)
ws.serializeAttachment({ userId: "abc", room: "lobby" })

// Retrieve after hibernation
const { userId, room } = ws.deserializeAttachment()
```


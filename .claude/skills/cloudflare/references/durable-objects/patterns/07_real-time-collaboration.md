## Real-time Collaboration

Broadcast updates to all connected clients:

```typescript
async webSocketMessage(ws: WebSocket, msg: string) {
  const data = JSON.parse(msg);
  this.ctx.storage.kv.put("doc", data.content);  // Persist
  for (const c of this.ctx.getWebSockets()) if (c !== ws) c.send(msg);  // Broadcast
}
```

### WebSocket Reconnection

**Client-side** (exponential backoff):
```typescript
class ResilientWS {
  private delay = 1000;
  connect(url: string) {
    const ws = new WebSocket(url);
    ws.onclose = () => setTimeout(() => {
      this.connect(url);
      this.delay = Math.min(this.delay * 2, 30000);
    }, this.delay);
  }
}
```

**Server-side** (cleanup on close):
```typescript
async webSocketClose(ws: WebSocket, code: number, reason: string, wasClean: boolean) {
  const { userId } = ws.deserializeAttachment();
  this.ctx.storage.sql.exec("UPDATE users SET online = false WHERE id = ?", userId);
  for (const c of this.ctx.getWebSockets()) c.send(JSON.stringify({ type: "user_left", userId }));
}
```


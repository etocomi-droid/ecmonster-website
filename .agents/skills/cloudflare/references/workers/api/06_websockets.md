## WebSockets

### Standard WebSocket

```typescript
const [client, server] = Object.values(new WebSocketPair());

server.accept();
server.addEventListener('message', event => {
  server.send(`Echo: ${event.data}`);
});

return new Response(null, { status: 101, webSocket: client });
```

### WebSocket Hibernation (Recommended for idle connections)

```typescript
// In Durable Object
export class WebSocketDO {
  async webSocketMessage(ws: WebSocket, message: string) {
    ws.send(`Echo: ${message}`);
  }
  
  async webSocketClose(ws: WebSocket, code: number, reason: string) {
    // Cleanup on close
  }
  
  async webSocketError(ws: WebSocket, error: Error) {
    console.error('WebSocket error:', error);
  }
}
```

Hibernation automatically suspends inactive connections (no CPU cost), wakes on events


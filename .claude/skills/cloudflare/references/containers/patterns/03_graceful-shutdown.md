## Graceful Shutdown

```typescript
export class GracefulContainer extends Container {
  private connections = new Set<WebSocket>();

  onStop() {
    // SIGTERM received, 15 minutes until SIGKILL
    for (const ws of this.connections) {
      ws.close(1001, "Server shutting down");
    }
    this.ctx.storage.put("shutdown-time", Date.now());
  }

  onActivityExpired(): boolean {
    return this.connections.size > 0;  // Keep alive if connections
  }
}
```


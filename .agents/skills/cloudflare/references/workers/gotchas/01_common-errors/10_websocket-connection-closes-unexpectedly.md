### "WebSocket connection closes unexpectedly"

**Cause:** Worker reaches CPU limit while maintaining WebSocket connection  
**Solution:** Use WebSocket hibernation (2024+) to offload idle connections:

```typescript
export class WebSocketDO {
  async webSocketMessage(ws: WebSocket, message: string) {
    // Handle message
  }
  async webSocketClose(ws: WebSocket, code: number) {
    // Cleanup
  }
}
```

Hibernation automatically suspends inactive connections, wakes on events


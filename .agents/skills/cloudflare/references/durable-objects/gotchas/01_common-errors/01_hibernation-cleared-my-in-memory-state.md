### "Hibernation Cleared My In-Memory State"

**Problem:** Variables lost after hibernation  
**Cause:** DO auto-hibernates when idle; in-memory state not persisted  
**Solution:** Use `ctx.storage` for critical data, `ws.serializeAttachment()` for per-connection metadata

```typescript
// ❌ Wrong - lost on hibernation
private userCount = 0;
async webSocketMessage(ws: WebSocket, msg: string) {
  this.userCount++;  // Lost!
}

// ✅ Right - persisted
async webSocketMessage(ws: WebSocket, msg: string) {
  const count = this.ctx.storage.kv.get("userCount") || 0;
  this.ctx.storage.kv.put("userCount", count + 1);
}
```


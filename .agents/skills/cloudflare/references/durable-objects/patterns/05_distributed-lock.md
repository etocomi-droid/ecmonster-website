## Distributed Lock

```typescript
private held = false;
async acquire(timeoutMs = 5000): Promise<boolean> {
  if (this.held) return false;
  this.held = true;
  await this.ctx.storage.setAlarm(Date.now() + timeoutMs);
  return true;
}
async release() { this.held = false; await this.ctx.storage.deleteAlarm(); }
async alarm() { this.held = false; }  // Auto-release on timeout
```


### "setTimeout Didn't Fire After Restart"

**Problem:** Scheduled work lost on eviction  
**Cause:** `setTimeout` in-memory only; eviction clears timers  
**Solution:** Use `ctx.storage.setAlarm()` for reliable scheduling

```typescript
// ❌ Wrong - lost on eviction
setTimeout(() => this.cleanup(), 3600000);

// ✅ Right - survives eviction
await this.ctx.storage.setAlarm(Date.now() + 3600000);
async alarm() { await this.cleanup(); }
```


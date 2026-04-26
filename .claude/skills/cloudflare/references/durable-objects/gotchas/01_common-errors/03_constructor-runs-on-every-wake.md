### "Constructor Runs on Every Wake"

**Problem:** Expensive init logic slows all requests  
**Cause:** Constructor runs on every wake (first request after eviction OR after hibernation)  
**Solution:** Lazy initialization or cache in storage

**Critical understanding:** Constructor runs in two scenarios:
1. **Cold start** - DO evicted from memory, first request creates new instance
2. **Wake from hibernation** - DO with WebSockets hibernated, message/alarm wakes it

```typescript
// ❌ Wrong - expensive on every wake
constructor(ctx: DurableObjectState, env: Env) {
  super(ctx, env);
  this.heavyData = this.loadExpensiveData();  // Slow!
}

// ✅ Right - lazy load
private heavyData?: HeavyData;
private getHeavyData() {
  if (!this.heavyData) this.heavyData = this.loadExpensiveData();
  return this.heavyData;
}
```


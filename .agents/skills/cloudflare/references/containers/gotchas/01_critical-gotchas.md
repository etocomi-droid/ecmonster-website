## Critical Gotchas

### ⚠️ WebSocket: fetch() vs containerFetch()

**Problem:** WebSocket connections fail silently

**Cause:** `containerFetch()` doesn't support WebSocket upgrades

**Fix:** Always use `fetch()` for WebSocket

```typescript
// ❌ WRONG
return container.containerFetch(request);

// ✅ CORRECT
return container.fetch(request);
```

### ⚠️ startAndWaitForPorts() vs start()

**Problem:** "connection refused" after `start()`

**Cause:** `start()` returns when process starts, NOT when ports ready

**Fix:** Use `startAndWaitForPorts()` before requests

```typescript
// ❌ WRONG
await container.start();
return container.fetch(request);

// ✅ CORRECT
await container.startAndWaitForPorts();
return container.fetch(request);
```

### ⚠️ Activity Timeout on Long Operations

**Problem:** Container stops during long work

**Cause:** `sleepAfter` based on request activity, not internal work

**Fix:** Renew timeout by touching storage

```typescript
const interval = setInterval(() => {
  this.ctx.storage.put("keepalive", Date.now());
}, 60000);

try {
  await this.doLongWork(data);
} finally {
  clearInterval(interval);
}
```

### ⚠️ blockConcurrencyWhile for Startup

**Problem:** Race conditions during initialization

**Fix:** Use `blockConcurrencyWhile` for atomic initialization

```typescript
await this.ctx.blockConcurrencyWhile(async () => {
  if (!this.initialized) {
    await this.startAndWaitForPorts();
    this.initialized = true;
  }
});
```

### ⚠️ Lifecycle Hooks Block Requests

**Problem:** Container unresponsive during `onStart()`

**Cause:** Hooks run in `blockConcurrencyWhile` - no concurrent requests

**Fix:** Keep hooks fast, avoid long operations

### ⚠️ Don't Override alarm() When Using schedule()

**Problem:** Scheduled tasks don't execute

**Cause:** `schedule()` uses `alarm()` internally

**Fix:** Implement `alarm()` to handle scheduled tasks


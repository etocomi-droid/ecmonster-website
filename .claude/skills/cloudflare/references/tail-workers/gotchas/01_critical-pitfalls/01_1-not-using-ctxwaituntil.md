### 1. Not Using `ctx.waitUntil()`

**Problem:** Async work doesn't complete or tail Worker times out  
**Cause:** Handlers exit immediately; awaiting blocks processing  
**Solution:**

```typescript
// ❌ WRONG - fire and forget
export default {
  async tail(events) {
    fetch(endpoint, { body: JSON.stringify(events) });
  }
};

// ❌ WRONG - blocking await
export default {
  async tail(events, env, ctx) {
    await fetch(endpoint, { body: JSON.stringify(events) });
  }
};

// ✅ CORRECT
export default {
  async tail(events, env, ctx) {
    ctx.waitUntil(
      (async () => {
        await fetch(endpoint, { body: JSON.stringify(events) });
        await processMore();
      })()
    );
  }
};
```


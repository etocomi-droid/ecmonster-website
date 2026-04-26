### 6. Excessive Logging Volume

**Problem:** Unexpected high costs  
**Cause:** Invoked on EVERY producer request  
**Solution:** Sample events

```typescript
export default {
  async tail(events, env, ctx) {
    if (Math.random() > 0.1) return;  // 10% sample
    ctx.waitUntil(sendToEndpoint(events));
  }
};
```


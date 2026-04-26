### 8. Missing Error Handling

**Problem:** Tail Worker silently fails  
**Cause:** No try/catch  
**Solution:**

```typescript
ctx.waitUntil((async () => {
  try {
    await fetch(env.ENDPOINT, { body: JSON.stringify(events) });
  } catch (error) {
    console.error("Tail error:", error);
    await env.FALLBACK_KV.put(`failed:${Date.now()}`, JSON.stringify(events));
  }
})());
```


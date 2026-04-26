### 7. Serialization Issues

**Problem:** `JSON.stringify()` fails  
**Cause:** `log.message` is `unknown[]` with non-serializable values  
**Solution:**

```typescript
const safePayload = events.map(e => ({
  ...e,
  logs: e.logs.map(log => ({
    ...log,
    message: log.message.map(m => {
      try { return JSON.parse(JSON.stringify(m)); }
      catch { return String(m); }
    })
  }))
}));
```


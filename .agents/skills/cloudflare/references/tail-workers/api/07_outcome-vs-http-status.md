## Outcome vs HTTP Status

**IMPORTANT:** `outcome` is script execution status, NOT HTTP status.

- Worker returns 500 → `outcome='ok'` if script completed successfully
- Uncaught exception → `outcome='exception'` regardless of HTTP status
- CPU limit exceeded → `outcome='exceededCpu'`

```typescript
// ✅ Check outcome for script execution status
if (event.outcome === 'exception') {
  // Script threw uncaught exception
}

// ✅ Check HTTP status separately
if (event.event?.response?.status === 500) {
  // HTTP 500 returned (script may have handled error)
}
```


## Serialization Considerations

`log.message` is `unknown[]` and may contain non-serializable objects:

```typescript
// ❌ May fail with circular references or BigInt
JSON.stringify(events);

// ✅ Safe serialization
const safePayload = events.map(event => ({
  ...event,
  logs: event.logs.map(log => ({
    ...log,
    message: log.message.map(m => {
      try {
        return JSON.parse(JSON.stringify(m));
      } catch {
        return String(m);
      }
    })
  }))
}));
```

**Common serialization issues:**
- Circular references in logged objects
- `BigInt` values (not JSON-serializable)
- Functions or symbols in console.log arguments
- Large objects exceeding body size limits

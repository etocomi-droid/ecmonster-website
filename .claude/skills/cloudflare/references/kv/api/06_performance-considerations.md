## Performance Considerations

### Type Selection

| Type | Use Case | Performance |
|------|----------|-------------|
| `stream` | Large values (>1MB) | Fastest - no buffering |
| `arrayBuffer` | Binary data | Fast - single allocation |
| `text` | String values | Medium |
| `json` | Objects (parse overhead) | Slowest - parsing cost |

### Parallel Reads

```typescript
// Efficient parallel reads with Promise.all()
const [user, settings, cache] = await Promise.all([
  env.USERS.get("user:123", "json"),
  env.SETTINGS.get("config:app", "json"),
  env.CACHE.get("data:latest")
]);
```


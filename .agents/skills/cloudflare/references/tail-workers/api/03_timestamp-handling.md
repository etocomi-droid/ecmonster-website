## Timestamp Handling

All timestamps are **epoch milliseconds**, not seconds:

```typescript
// ✅ CORRECT - use directly with Date
const date = new Date(event.eventTimestamp);

// ❌ WRONG - don't multiply by 1000
const date = new Date(event.eventTimestamp * 1000);
```


### 4. Timestamp Units

**Problem:** Dates off by 1000x  
**Cause:** Timestamps are epoch milliseconds, not seconds

```typescript
// ❌ WRONG: const date = new Date(event.eventTimestamp * 1000);
// ✅ CORRECT: const date = new Date(event.eventTimestamp);
```


### 3. Outcome vs HTTP Status

**Problem:** Filtering by wrong status  
**Cause:** `outcome` is script execution status, not HTTP status

```typescript
// ❌ WRONG
if (event.outcome === 500) { /* never matches */ }

// ✅ CORRECT
if (event.outcome === 'exception') { /* script threw */ }
if (event.event?.response?.status === 500) { /* HTTP 500 */ }
```


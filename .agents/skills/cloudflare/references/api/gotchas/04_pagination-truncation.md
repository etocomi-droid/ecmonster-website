## Pagination Truncation

**Problem:** Only getting first 20 results (default page size).

**Solution:** Use auto-pagination iterators.

```typescript
// ❌ WRONG - Only first page (20 items)
const page = await client.zones.list();

// ✅ CORRECT - All results
const zones = [];
for await (const zone of client.zones.list()) {
  zones.push(zone);
}
```


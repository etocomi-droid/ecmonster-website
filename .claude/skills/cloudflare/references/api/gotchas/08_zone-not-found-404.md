## Zone Not Found (404)

**Problem:** Zone ID valid but returns 404.

**Causes:**
- Zone not in account associated with token
- Zone deleted
- Wrong zone ID format

**Solution:**

```typescript
// List all zones to find correct ID
for await (const zone of client.zones.list()) {
  console.log(zone.id, zone.name);
}
```


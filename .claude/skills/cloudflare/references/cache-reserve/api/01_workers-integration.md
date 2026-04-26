## Workers Integration

```
┌────────────────────────────────────────────────────────────────┐
│ CRITICAL: Workers Cache API ≠ Cache Reserve                   │
│                                                                │
│ • Workers caches.default / cache.put() → edge cache ONLY      │
│ • Cache Reserve → zone-level setting, automatic, no per-req   │
│ • You CANNOT selectively write to Cache Reserve from Workers  │
│ • Cache Reserve works with standard fetch(), not cache.put()  │
└────────────────────────────────────────────────────────────────┘
```

Cache Reserve is a **zone-level configuration**, not a per-request API. It works automatically when enabled for the zone:

### Standard Fetch (Recommended)

```typescript
// Cache Reserve works automatically via standard fetch
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Standard fetch uses Cache Reserve automatically
    return await fetch(request);
  }
};
```

### Cache API Limitations

**IMPORTANT**: `cache.put()` is **NOT compatible** with Cache Reserve or Tiered Cache.

```typescript
// ❌ WRONG: cache.put() bypasses Cache Reserve
const cache = caches.default;
let response = await cache.match(request);
if (!response) {
  response = await fetch(request);
  await cache.put(request, response.clone()); // Bypasses Cache Reserve!
}

// ✅ CORRECT: Use standard fetch for Cache Reserve compatibility
return await fetch(request);

// ✅ CORRECT: Use Cache API only for custom cache namespaces
const customCache = await caches.open('my-custom-cache');
let response = await customCache.match(request);
if (!response) {
  response = await fetch(request);
  await customCache.put(request, response.clone()); // Custom cache OK
}
```


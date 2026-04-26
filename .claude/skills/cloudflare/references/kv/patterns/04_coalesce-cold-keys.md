## Coalesce Cold Keys

```typescript
// ❌ BAD: Many individual keys
await env.KV.put("user:123:name", "John");
await env.KV.put("user:123:email", "john@example.com");

// ✅ GOOD: Single coalesced object
await env.USERS.put("user:123:profile", JSON.stringify({
  name: "John",
  email: "john@example.com",
  role: "admin"
}));

// Benefits: Hot key cache, single read, reduced operations
// Trade-off: Harder to update individual fields
```


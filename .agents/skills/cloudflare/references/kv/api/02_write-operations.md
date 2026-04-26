## Write Operations

```typescript
// Basic put
await env.MY_KV.put("key", "value");
await env.MY_KV.put("config", JSON.stringify({ theme: "dark" }));

// With expiration (UNIX timestamp)
await env.MY_KV.put("session", token, {
  expiration: Math.floor(Date.now() / 1000) + 3600
});

// With TTL (seconds from now, min 60)
await env.MY_KV.put("cache", data, { expirationTtl: 300 });

// With metadata (max 1024 bytes)
await env.MY_KV.put("user:profile", userData, {
  metadata: { version: 2, lastUpdated: Date.now() }
});

// Combined
await env.MY_KV.put("temp", value, {
  expirationTtl: 3600,
  metadata: { temporary: true }
});
```


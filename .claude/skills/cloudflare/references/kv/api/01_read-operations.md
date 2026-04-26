## Read Operations

```typescript
// Single key (string)
const value = await env.MY_KV.get("user:123");

// JSON type (auto-parsed)
const config = await env.MY_KV.get<AppConfig>("config", "json");

// ArrayBuffer for binary
const buffer = await env.MY_KV.get("image", "arrayBuffer");

// Stream for large values
const stream = await env.MY_KV.get("large-file", "stream");

// With cache TTL (min 60s)
const value = await env.MY_KV.get("key", { type: "text", cacheTtl: 300 });

// Bulk get (max 100 keys, counts as 1 operation)
const keys = ["user:1", "user:2", "user:3", "missing:key"];
const results = await env.MY_KV.get(keys);
// Returns Map<string, string | null>

console.log(results.get("user:1"));     // "John" (if exists)
console.log(results.get("missing:key")); // null

// Process results with null handling
for (const [key, value] of results) {
  if (value !== null) {
    // Handle found keys
    console.log(`${key}: ${value}`);
  }
}

// TypeScript with generics (type-safe JSON parsing)
interface UserProfile { name: string; email: string; }
const profile = await env.USERS.get<UserProfile>("user:123", "json");
// profile is typed as UserProfile | null
if (profile) {
  console.log(profile.name); // Type-safe access
}

// Bulk get with type
const configs = await env.MY_KV.get<Config>(["config:app", "config:feature"], "json");
// Map<string, Config | null>
```


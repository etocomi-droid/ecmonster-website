## Prefix-Based Namespacing

```typescript
// Logical partitioning within single namespace
const PREFIXES = {
  users: "user:",
  sessions: "session:",
  cache: "cache:",
  features: "feature:"
} as const;

// Write with prefix
async function setUser(env: Env, id: string, data: any) {
  await env.KV.put(`${PREFIXES.users}${id}`, JSON.stringify(data));
}

// Read with prefix
async function getUser(env: Env, id: string) {
  return await env.KV.get(`${PREFIXES.users}${id}`, "json");
}

// List by prefix
async function listUserIds(env: Env): Promise<string[]> {
  const result = await env.KV.list({ prefix: PREFIXES.users });
  return result.keys.map(k => k.name.replace(PREFIXES.users, ""));
}

// Example hierarchy
"user:123:profile"
"user:123:settings"
"cache:api:users"
"session:abc-def"
"feature:flags:beta"
```


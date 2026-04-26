## Get with Metadata

```typescript
// Single key
const result = await env.MY_KV.getWithMetadata("user:profile");
// { value: string | null, metadata: any | null }

if (result.value && result.metadata) {
  const { version, lastUpdated } = result.metadata;
}

// Multiple keys (bulk)
const keys = ["key1", "key2", "key3"];
const results = await env.MY_KV.getWithMetadata(keys);
// Returns Map<string, { value, metadata, cacheStatus? }>

for (const [key, result] of results) {
  if (result.value) {
    console.log(`${key}: ${result.value}`);
    console.log(`Metadata: ${JSON.stringify(result.metadata)}`);
    // cacheStatus field indicates cache hit/miss (when available)
  }
}

// With type
const result = await env.MY_KV.getWithMetadata<UserData>("user:123", "json");
// result: { value: UserData | null, metadata: any | null, cacheStatus?: string }
```


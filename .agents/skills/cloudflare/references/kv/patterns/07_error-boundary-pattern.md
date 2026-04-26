## Error Boundary Pattern

```typescript
// Resilient get with fallback
async function resilientGet<T>(
  env: Env,
  key: string,
  fallback: T
): Promise<T> {
  try {
    const value = await env.KV.get<T>(key, "json");
    return value ?? fallback;
  } catch (err) {
    console.error(`KV error for ${key}:`, err);
    return fallback;
  }
}

// Usage
const config = await resilientGet(env, "config:app", {
  theme: "light",
  maxItems: 10
});
```

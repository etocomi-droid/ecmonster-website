## List Truncation

```typescript
// ❌ WRONG: Don't compare object count when using include
while (listed.objects.length < options.limit) { ... }

// ✅ CORRECT: Always use truncated property
while (listed.truncated) {
  const next = await env.MY_BUCKET.list({ cursor: listed.cursor });
  // ...
}
```

**Reason:** `include` with metadata may return fewer objects per page to fit metadata.


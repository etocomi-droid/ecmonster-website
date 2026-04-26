## LIST

```typescript
const listed = await env.MY_BUCKET.list({
  limit: 1000,
  prefix: 'photos/',
  cursor: cursorFromPrevious,
  delimiter: '/',
  include: ['httpMetadata', 'customMetadata']
});

// Pagination (always use truncated flag)
while (listed.truncated) {
  const next = await env.MY_BUCKET.list({ cursor: listed.cursor });
  listed.objects.push(...next.objects);
  listed.truncated = next.truncated;
  listed.cursor = next.cursor;
}
```


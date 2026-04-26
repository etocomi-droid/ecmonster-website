## Performance

```typescript
// ❌ Sequential
const user = await fetch('/api/user/1');
const posts = await fetch('/api/posts?user=1');

// ✅ Parallel
const [user, posts] = await Promise.all([fetch('/api/user/1'), fetch('/api/posts?user=1')]);
```


## Query Optimization

```typescript
// ✅ Use indexes in WHERE clauses
const users = await env.DB.prepare('SELECT * FROM users WHERE email = ?').bind(email).all();

// ✅ Limit result sets
const recentPosts = await env.DB.prepare('SELECT * FROM posts ORDER BY created_at DESC LIMIT 100').all();

// ✅ Use batch() for multiple independent queries
const [user, posts, comments] = await env.DB.batch([
  env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId),
  env.DB.prepare('SELECT * FROM posts WHERE user_id = ?').bind(userId),
  env.DB.prepare('SELECT * FROM comments WHERE user_id = ?').bind(userId)
]);

// ❌ Avoid N+1 queries
for (const post of posts) {
  const author = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(post.user_id).first(); // Bad: multiple round trips
}

// ✅ Use JOINs instead
const postsWithAuthors = await env.DB.prepare(`
  SELECT posts.*, users.name as author_name
  FROM posts
  JOIN users ON posts.user_id = users.id
`).all();
```


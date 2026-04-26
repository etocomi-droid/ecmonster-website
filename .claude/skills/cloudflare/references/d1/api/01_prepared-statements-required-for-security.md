## Prepared Statements (Required for Security)

```typescript
// ❌ NEVER: Direct string interpolation (SQL injection risk)
const result = await env.DB.prepare(`SELECT * FROM users WHERE id = ${userId}`).all();

// ✅ CORRECT: Prepared statements with bind()
const result = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).all();

// Multiple parameters
const result = await env.DB.prepare('SELECT * FROM users WHERE email = ? AND active = ?').bind(email, true).all();
```


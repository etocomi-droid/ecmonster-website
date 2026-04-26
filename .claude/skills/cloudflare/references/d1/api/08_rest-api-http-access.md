## REST API (HTTP) Access

Access D1 from external services (non-Worker contexts) using Cloudflare API.

```typescript
// Single query
const response = await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/d1/database/${DATABASE_ID}/query`,
  {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${CLOUDFLARE_API_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      sql: 'SELECT * FROM users WHERE id = ?',
      params: [userId]
    })
  }
);

const { result, success, errors } = await response.json();
// result: [{ results: [...], success: true, meta: {...} }]

// Batch queries via HTTP
const response = await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/d1/database/${DATABASE_ID}/query`,
  {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${CLOUDFLARE_API_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify([
      { sql: 'SELECT * FROM users WHERE id = ?', params: [1] },
      { sql: 'SELECT * FROM posts WHERE author_id = ?', params: [1] }
    ])
  }
);
```

**Use cases**: Server-side scripts, CI/CD migrations, administrative tools, non-Worker integrations


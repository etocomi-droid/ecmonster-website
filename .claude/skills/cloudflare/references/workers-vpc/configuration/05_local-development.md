## Local Development

Test with `wrangler dev`. Note: Local mode may not access private networks. Use public endpoints or mock servers for development:

```typescript
const config = process.env.NODE_ENV === 'dev' 
  ? { hostname: 'localhost', port: 5432 }  // Mock
  : { hostname: 'db.internal.example.com', port: 5432 };  // Production
```


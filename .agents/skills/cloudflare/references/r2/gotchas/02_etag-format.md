## ETag Format

```typescript
// ❌ WRONG: Using etag (unquoted) in headers
headers.set('etag', object.etag); // Missing quotes

// ✅ CORRECT: Use httpEtag (quoted)
headers.set('etag', object.httpEtag);
```


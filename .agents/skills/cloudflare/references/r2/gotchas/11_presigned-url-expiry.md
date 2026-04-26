## Presigned URL Expiry

```typescript
// ❌ WRONG: URL expires but no client validation
const url = await getSignedUrl(s3, command, { expiresIn: 60 });
// 61 seconds later: 403 Forbidden

// ✅ CORRECT: Return expiry to client
return Response.json({
  uploadUrl: url,
  expiresAt: new Date(Date.now() + 60000).toISOString()
});
```


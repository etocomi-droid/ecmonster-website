## S3 SDK Region Configuration

```typescript
// ❌ WRONG: Missing region breaks ALL S3 SDK calls
const s3 = new S3Client({
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: { ... }
});

// ✅ CORRECT: MUST set region='auto'
const s3 = new S3Client({
  region: 'auto', // REQUIRED
  endpoint: `https://${accountId}.r2.cloudflarestorage.com`,
  credentials: { ... }
});
```

**Reason:** S3 SDK requires region. R2 uses 'auto' as placeholder.


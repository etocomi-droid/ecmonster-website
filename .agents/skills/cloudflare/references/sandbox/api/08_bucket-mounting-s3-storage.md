## Bucket Mounting (S3 Storage)

```typescript
// Mount R2 bucket (production only, not wrangler dev)
await sandbox.mountBucket(env.DATA_BUCKET, '/data', {
  readOnly: false
});

// Access files in mounted bucket
await sandbox.exec('ls /data');
await sandbox.writeFile('/data/output.txt', 'result');

// Unmount
await sandbox.unmountBucket('/data');
```

**Note**: Bucket mounting only works in production. Mounted buckets are sandbox-scoped (visible to all sessions in that sandbox).


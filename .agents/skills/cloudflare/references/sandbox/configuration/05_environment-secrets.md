## Environment & Secrets

**wrangler.jsonc**:
```jsonc
{
  "vars": {
    "ENVIRONMENT": "production",
    "API_URL": "https://api.example.com"
  },
  "r2_buckets": [{
    "binding": "DATA_BUCKET",
    "bucket_name": "my-data-bucket"
  }]
}
```

**Usage**:
```typescript
const token = env.GITHUB_TOKEN;  // From wrangler secret
await sandbox.exec('git clone ...', {
  env: { GIT_TOKEN: token }
});
```


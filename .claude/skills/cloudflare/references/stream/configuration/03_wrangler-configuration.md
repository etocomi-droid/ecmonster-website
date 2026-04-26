## Wrangler Configuration

```jsonc
{
  "name": "stream-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01", // Use current date for new projects
  "vars": {
    "CF_ACCOUNT_ID": "your-account-id"
  }
  // Store secrets: wrangler secret put CF_API_TOKEN
  // wrangler secret put STREAM_KEY_ID
  // wrangler secret put STREAM_JWK
  // wrangler secret put WEBHOOK_SECRET
}
```


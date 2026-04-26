## Disable Catalog (If Needed)

```bash
npx wrangler r2 bucket catalog disable <BUCKET_NAME>
```

⚠️ **Warning:** Disabling does NOT delete tables/data. Files remain in bucket. Metadata becomes inaccessible until re-enabled.


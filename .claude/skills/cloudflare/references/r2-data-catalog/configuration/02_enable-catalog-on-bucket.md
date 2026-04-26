## Enable Catalog on Bucket

Choose one method:

### Via Wrangler (Recommended)

```bash
npx wrangler r2 bucket catalog enable <BUCKET_NAME>
```

**Output:**
```
✅ Data Catalog enabled for bucket 'my-bucket'
   Catalog URI: https://<account-id>.r2.cloudflarestorage.com/iceberg/my-bucket
   Warehouse: my-bucket
```

### Via Dashboard

1. Navigate to **R2** → Select your bucket → **Settings** tab
2. Scroll to "R2 Data Catalog" section → Click **Enable**
3. Note the **Catalog URI** and **Warehouse name** shown

**Result:**
- Catalog URI: `https://<account-id>.r2.cloudflarestorage.com/iceberg/<bucket-name>`
- Warehouse: `<bucket-name>` (same as bucket name)

### Via API (Programmatic)

```bash
curl -X POST \
  "https://api.cloudflare.com/client/v4/accounts/<account-id>/r2/buckets/<bucket>/catalog" \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "result": {
    "catalog_uri": "https://<account-id>.r2.cloudflarestorage.com/iceberg/<bucket>",
    "warehouse": "<bucket>"
  },
  "success": true
}
```


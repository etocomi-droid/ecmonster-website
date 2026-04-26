## Import Existing Resources

```bash
# Import worker
pulumi import cloudflare:index/workerScript:WorkerScript my-worker <account_id>/<worker_name>

# Import KV namespace
pulumi import cloudflare:index/workersKvNamespace:WorkersKvNamespace my-kv <namespace_id>

# Import R2 bucket
pulumi import cloudflare:index/r2Bucket:R2Bucket my-bucket <account_id>/<bucket_name>

# Import D1 database
pulumi import cloudflare:index/d1Database:D1Database my-db <account_id>/<database_id>

# Import DNS record
pulumi import cloudflare:index/dnsRecord:DnsRecord my-record <zone_id>/<record_id>
```


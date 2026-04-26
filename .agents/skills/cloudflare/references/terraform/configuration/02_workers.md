## Workers

### Simple Pattern (Legacy - Still Works)

```hcl
resource "cloudflare_workers_script" "api" {
  account_id = var.account_id; name = "api-worker"; content = file("worker.js")
  module = true; compatibility_date = "2025-01-01"
  kv_namespace_binding { name = "KV"; namespace_id = cloudflare_workers_kv_namespace.cache.id }
  r2_bucket_binding { name = "BUCKET"; bucket_name = cloudflare_r2_bucket.assets.name }
  d1_database_binding { name = "DB"; database_id = cloudflare_d1_database.app.id }
  secret_text_binding { name = "SECRET"; text = var.secret }
}
```

### Gradual Rollouts (Recommended for Production)

```hcl
resource "cloudflare_worker" "api" { account_id = var.account_id; name = "api-worker" }
resource "cloudflare_worker_version" "api_v1" {
  account_id = var.account_id; worker_name = cloudflare_worker.api.name
  content = file("worker.js"); content_sha256 = filesha256("worker.js")
  compatibility_date = "2025-01-01"
  bindings {
    kv_namespace { name = "KV"; namespace_id = cloudflare_workers_kv_namespace.cache.id }
    r2_bucket { name = "BUCKET"; bucket_name = cloudflare_r2_bucket.assets.name }
  }
}
resource "cloudflare_workers_deployment" "api" {
  account_id = var.account_id; worker_name = cloudflare_worker.api.name
  versions { version_id = cloudflare_worker_version.api_v1.id; percentage = 100 }
}
```

### Worker Binding Types (v5)

| Binding | Attribute | Example |
|---------|-----------|---------|
| KV | `kv_namespace_binding` | `{ name = "KV", namespace_id = "..." }` |
| R2 | `r2_bucket_binding` | `{ name = "BUCKET", bucket_name = "..." }` |
| D1 | `d1_database_binding` | `{ name = "DB", database_id = "..." }` |
| Service | `service_binding` | `{ name = "AUTH", service = "auth-worker" }` |
| Secret | `secret_text_binding` | `{ name = "API_KEY", text = "..." }` |
| Queue | `queue_binding` | `{ name = "QUEUE", queue_name = "..." }` |
| Vectorize | `vectorize_binding` | `{ name = "INDEX", index_name = "..." }` |
| Hyperdrive | `hyperdrive_binding` | `{ name = "DB", id = "..." }` |
| AI | `ai_binding` | `{ name = "AI" }` |
| Browser | `browser_binding` | `{ name = "BROWSER" }` |
| Analytics | `analytics_engine_binding` | `{ name = "ANALYTICS", dataset = "..." }` |
| mTLS | `mtls_certificate_binding` | `{ name = "CERT", certificate_id = "..." }` |

### Routes & Triggers

```hcl
resource "cloudflare_worker_route" "api" {
  zone_id = cloudflare_zone.example.id; pattern = "api.example.com/*"
  script_name = cloudflare_workers_script.api.name
}
resource "cloudflare_worker_cron_trigger" "task" {
  account_id = var.account_id; script_name = cloudflare_workers_script.api.name
  schedules = ["*/5 * * * *"]
}
```


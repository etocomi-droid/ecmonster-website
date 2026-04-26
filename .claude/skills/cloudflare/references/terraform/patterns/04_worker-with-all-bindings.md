## Worker with All Bindings

```hcl
locals { worker_name = "full-stack-worker" }
resource "cloudflare_workers_kv_namespace" "app" { account_id = var.account_id; title = "${local.worker_name}-kv" }
resource "cloudflare_r2_bucket" "app" { account_id = var.account_id; name = "${local.worker_name}-bucket" }
resource "cloudflare_d1_database" "app" { account_id = var.account_id; name = "${local.worker_name}-db" }

resource "cloudflare_worker_script" "app" {
  account_id = var.account_id; name = local.worker_name; content = file("worker.js"); module = true
  compatibility_date = "2025-01-01"
  kv_namespace_binding { name = "KV"; namespace_id = cloudflare_workers_kv_namespace.app.id }
  r2_bucket_binding { name = "BUCKET"; bucket_name = cloudflare_r2_bucket.app.name }
  d1_database_binding { name = "DB"; database_id = cloudflare_d1_database.app.id }
  secret_text_binding { name = "API_KEY"; text = var.api_key }
}
```


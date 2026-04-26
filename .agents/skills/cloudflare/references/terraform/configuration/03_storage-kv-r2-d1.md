## Storage (KV, R2, D1)

```hcl
# KV
resource "cloudflare_workers_kv_namespace" "cache" { account_id = var.account_id; title = "cache" }
resource "cloudflare_workers_kv" "config" {
  account_id = var.account_id; namespace_id = cloudflare_workers_kv_namespace.cache.id
  key_name = "config"; value = jsonencode({ version = "1.0" })
}

# R2
resource "cloudflare_r2_bucket" "assets" { account_id = var.account_id; name = "assets"; location = "WNAM" }

# D1 (migrations via wrangler) & Queues
resource "cloudflare_d1_database" "app" { account_id = var.account_id; name = "app-db" }
resource "cloudflare_queue" "events" { account_id = var.account_id; name = "events-queue" }
```


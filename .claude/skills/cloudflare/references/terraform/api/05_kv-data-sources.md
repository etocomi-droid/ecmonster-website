## KV Data Sources

```hcl
# Get KV namespace
data "cloudflare_workers_kv_namespace" "existing" {
  account_id = var.account_id
  namespace_id = "abc123"
}

# Use in worker binding
resource "cloudflare_workers_script" "api" {
  kv_namespace_binding {
    name = "KV"
    namespace_id = data.cloudflare_workers_kv_namespace.existing.id
  }
}
```


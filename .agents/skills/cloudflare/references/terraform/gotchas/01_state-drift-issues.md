## State Drift Issues

Some resources have known state drift. Add lifecycle blocks to prevent perpetual diffs:

| Resource | Drift Attributes | Workaround |
|----------|------------------|------------|
| `cloudflare_pages_project` | `deployment_configs.*` | `ignore_changes = [deployment_configs]` |
| `cloudflare_workers_script` | secrets returned as REDACTED | `ignore_changes = [secret_text_binding]` |
| `cloudflare_load_balancer` | `adaptive_routing`, `random_steering` | `ignore_changes = [adaptive_routing, random_steering]` |
| `cloudflare_workers_kv` | special chars in keys (< 5.16.0) | Upgrade to 5.16.0+ |

```hcl
# Example: Ignore secret drift
resource "cloudflare_workers_script" "api" {
  account_id = var.account_id
  name = "api-worker"
  content = file("worker.js")
  secret_text_binding { name = "API_KEY"; text = var.api_key }
  
  lifecycle {
    ignore_changes = [secret_text_binding]
  }
}
```


## Worker Data Sources

```hcl
# Get existing worker script (v5: cloudflare_workers_script)
data "cloudflare_workers_script" "existing" {
  account_id = var.account_id
  name = "existing-worker"
}

# Reference in service bindings
resource "cloudflare_workers_script" "consumer" {
  service_binding {
    name = "UPSTREAM"
    service = data.cloudflare_workers_script.existing.name
  }
}
```


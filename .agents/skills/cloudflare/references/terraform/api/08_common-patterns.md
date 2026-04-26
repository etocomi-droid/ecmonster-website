## Common Patterns

### Import ID Formats

| Resource | Import ID Format |
|----------|------------------|
| `cloudflare_zone` | `<zone-id>` |
| `cloudflare_dns_record` | `<zone-id>/<record-id>` |
| `cloudflare_workers_script` | `<account-id>/<script-name>` |
| `cloudflare_workers_kv_namespace` | `<account-id>/<namespace-id>` |
| `cloudflare_r2_bucket` | `<account-id>/<bucket-name>` |
| `cloudflare_d1_database` | `<account-id>/<database-id>` |
| `cloudflare_pages_project` | `<account-id>/<project-name>` |

```bash
# Example: Import DNS record
terraform import cloudflare_dns_record.example <zone-id>/<record-id>
```

### Reference Across Modules

```hcl
# modules/worker/main.tf
data "cloudflare_zone" "main" {
  name = var.domain
}

resource "cloudflare_worker_route" "api" {
  zone_id = data.cloudflare_zone.main.id
  pattern = "api.${var.domain}/*"
  script_name = cloudflare_worker_script.api.name
}
```

### Output Important Values

```hcl
output "zone_id" {
  value = cloudflare_zone.main.id
  description = "Zone ID for DNS management"
}

output "worker_url" {
  value = "https://${cloudflare_worker_domain.api.hostname}"
  description = "Worker API endpoint"
}

output "kv_namespace_id" {
  value = cloudflare_workers_kv_namespace.app.id
  sensitive = false
}

output "name_servers" {
  value = cloudflare_zone.main.name_servers
  description = "Name servers for domain registration"
}
```


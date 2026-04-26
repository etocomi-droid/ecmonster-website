## v5 Breaking Changes

Provider v5 is current (auto-generated from OpenAPI). v4→v5 has breaking changes:

**Resource Renames:**

| v4 Resource | v5 Resource | Notes |
|-------------|-------------|-------|
| `cloudflare_record` | `cloudflare_dns_record` | |
| `cloudflare_worker_script` | `cloudflare_workers_script` | Note: plural |
| `cloudflare_worker_*` | `cloudflare_workers_*` | All worker resources |
| `cloudflare_access_*` | `cloudflare_zero_trust_*` | Access → Zero Trust |

**Attribute Changes:**

| v4 Attribute | v5 Attribute | Resources |
|--------------|--------------|-----------|
| `zone` | `name` | zone |
| `account_id` | `account.id` | zone (object syntax) |
| `key` | `key_name` | KV |
| `location_hint` | `location` | R2 |

**State Migration:**

```bash
# Rename resources in state after v5 upgrade
terraform state mv cloudflare_record.example cloudflare_dns_record.example
terraform state mv cloudflare_worker_script.api cloudflare_workers_script.api
```


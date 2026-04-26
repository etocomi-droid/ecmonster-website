## Wrangler Integration

**CRITICAL**: Wrangler and Terraform must NOT manage same resources.

**Terraform**: Zones, DNS, security rules, Access, load balancers, worker deployments (CI/CD), KV/R2/D1 resource creation  
**Wrangler**: Local dev (`wrangler dev`), manual deploys, D1 migrations, KV bulk ops, log streaming (`wrangler tail`)

### CI/CD Pattern

```hcl
# Terraform creates infrastructure
resource "cloudflare_workers_kv_namespace" "app" { account_id = var.account_id; title = "app-kv" }
resource "cloudflare_d1_database" "app" { account_id = var.account_id; name = "app-db" }
output "kv_namespace_id" { value = cloudflare_workers_kv_namespace.app.id }
output "d1_database_id" { value = cloudflare_d1_database.app.id }
```

```yaml
# GitHub Actions: terraform apply → envsubst wrangler.jsonc.template → wrangler deploy
- run: terraform apply -auto-approve
- run: |
    export KV_NAMESPACE_ID=$(terraform output -raw kv_namespace_id)
    envsubst < wrangler.jsonc.template > wrangler.jsonc
- run: wrangler deploy
```


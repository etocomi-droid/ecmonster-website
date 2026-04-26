## Resource-Specific Gotchas

### R2 Location Case Sensitivity

**Problem:** Terraform creates R2 bucket but fails on subsequent applies  
**Cause:** Location must be UPPERCASE  
**Solution:** Use `WNAM`, `ENAM`, `WEUR`, `EEUR`, `APAC` (not `wnam`, `enam`, etc.)

```hcl
resource "cloudflare_r2_bucket" "assets" {
  account_id = var.account_id
  name = "assets"
  location = "WNAM"  # UPPERCASE required
}
```

### KV Special Characters (< 5.16.0)

**Problem:** Keys with `+`, `#`, `%` cause encoding issues  
**Cause:** URL encoding bug in provider < 5.16.0  
**Solution:** Upgrade to 5.16.0+ or avoid special chars in keys

### D1 Migrations

**Problem:** Terraform creates database but schema is empty  
**Cause:** Terraform only creates D1 resource, not schema  
**Solution:** Run migrations via wrangler after Terraform apply

```bash
# After terraform apply
wrangler d1 migrations apply <db-name>
```

### Worker Script Size Limit

**Problem:** Worker deployment fails with "script too large"  
**Cause:** Worker script + dependencies exceed 10 MB limit  
**Solution:** Use code splitting, external dependencies, or minification

### Pages Project Drift

**Problem:** Pages project shows perpetual diff on `deployment_configs`  
**Cause:** Cloudflare API adds default values not in Terraform state  
**Solution:** Add lifecycle ignore block (see State Drift table above)


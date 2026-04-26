## Pages

```hcl
resource "cloudflare_pages_project" "site" {
  account_id = var.account_id; name = "site"; production_branch = "main"
  deployment_configs {
    production {
      compatibility_date = "2025-01-01"
      environment_variables = { NODE_ENV = "production" }
      kv_namespaces = { KV = cloudflare_workers_kv_namespace.cache.id }
      d1_databases = { DB = cloudflare_d1_database.app.id }
    }
  }
  build_config { build_command = "npm run build"; destination_dir = "dist" }
  source { type = "github"; config { owner = "org"; repo_name = "site"; production_branch = "main" }}
}

resource "cloudflare_pages_domain" "custom" {
  account_id = var.account_id; project_name = cloudflare_pages_project.site.name; domain = "site.example.com"
}
```


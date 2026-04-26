## Use Cases

### Static Site + API Worker

```hcl
resource "cloudflare_pages_project" "frontend" {
  account_id = var.account_id; name = "frontend"; production_branch = "main"
  build_config { build_command = "npm run build"; destination_dir = "dist" }
}
resource "cloudflare_worker_script" "api" {
  account_id = var.account_id; name = "api"; content = file("api-worker.js")
  d1_database_binding { name = "DB"; database_id = cloudflare_d1_database.api_db.id }
}
resource "cloudflare_dns_record" "frontend" {
  zone_id = cloudflare_zone.main.id; name = "app"; content = cloudflare_pages_project.frontend.subdomain; type = "CNAME"; proxied = true
}
resource "cloudflare_worker_route" "api" {
  zone_id = cloudflare_zone.main.id; pattern = "api.example.com/*"; script_name = cloudflare_worker_script.api.name
}
```

### Multi-Region Load Balancing

```hcl
resource "cloudflare_load_balancer_pool" "us" {
  account_id = var.account_id; name = "us-pool"; monitor = cloudflare_load_balancer_monitor.http.id
  origins { name = "us-east"; address = var.us_east_ip }
}
resource "cloudflare_load_balancer_pool" "eu" {
  account_id = var.account_id; name = "eu-pool"; monitor = cloudflare_load_balancer_monitor.http.id
  origins { name = "eu-west"; address = var.eu_west_ip }
}
resource "cloudflare_load_balancer" "global" {
  zone_id = cloudflare_zone.main.id; name = "api.example.com"; steering_policy = "geo"
  default_pool_ids = [cloudflare_load_balancer_pool.us.id]
  region_pools { region = "WNAM"; pool_ids = [cloudflare_load_balancer_pool.us.id] }
  region_pools { region = "WEU"; pool_ids = [cloudflare_load_balancer_pool.eu.id] }
}
```

### Secure Admin with Access

```hcl
resource "cloudflare_pages_project" "admin" { account_id = var.account_id; name = "admin"; production_branch = "main" }
resource "cloudflare_access_application" "admin" {
  account_id = var.account_id; name = "Admin"; domain = "admin.example.com"; type = "self_hosted"; session_duration = "24h"
  allowed_idps = [cloudflare_access_identity_provider.google.id]
}
resource "cloudflare_access_policy" "allow" {
  account_id = var.account_id; application_id = cloudflare_access_application.admin.id
  name = "Allow admins"; decision = "allow"; precedence = 1; include { email = var.admin_emails }
}
```

### Reusable Module

```hcl
# modules/cloudflare-zone/main.tf
variable "account_id" { type = string }; variable "domain" { type = string }; variable "ssl_mode" { default = "strict" }
resource "cloudflare_zone" "main" { account = { id = var.account_id }; name = var.domain }
resource "cloudflare_zone_settings_override" "main" {
  zone_id = cloudflare_zone.main.id; settings { ssl = var.ssl_mode; always_use_https = "on" }
}
output "zone_id" { value = cloudflare_zone.main.id }

# Usage: module "prod" { source = "./modules/cloudflare-zone"; account_id = var.account_id; domain = "example.com" }
```


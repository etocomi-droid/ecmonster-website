## Load Balancers

```hcl
resource "cloudflare_load_balancer_monitor" "http" {
  account_id = var.account_id; type = "http"; path = "/health"; interval = 60; timeout = 5
}
resource "cloudflare_load_balancer_pool" "api" {
  account_id = var.account_id; name = "api-pool"; monitor = cloudflare_load_balancer_monitor.http.id
  origins { name = "api-1"; address = "192.0.2.1" }
  origins { name = "api-2"; address = "192.0.2.2" }
}
resource "cloudflare_load_balancer" "api" {
  zone_id = cloudflare_zone.example.id; name = "api.example.com"
  default_pool_ids = [cloudflare_load_balancer_pool.api.id]; steering_policy = "geo"
}
```


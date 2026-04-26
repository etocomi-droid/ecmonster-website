### 7. Multi-Origin Failover

High availability with load balancer.

**Terraform:**
```hcl
resource "cloudflare_load_balancer" "database_lb" {
  zone_id          = var.zone_id
  name             = "db-lb.example.com"
  default_pool_ids = [cloudflare_load_balancer_pool.db_primary.id]
  fallback_pool_id = cloudflare_load_balancer_pool.db_secondary.id
}

resource "cloudflare_load_balancer_pool" "db_primary" {
  name    = "db-primary-pool"
  origins { name = "db-1"; address = "192.0.2.1" }
  monitor = cloudflare_load_balancer_monitor.postgres_monitor.id
}

resource "cloudflare_load_balancer_pool" "db_secondary" {
  name    = "db-secondary-pool"
  origins { name = "db-2"; address = "192.0.2.2" }
  monitor = cloudflare_load_balancer_monitor.postgres_monitor.id
}

resource "cloudflare_load_balancer_monitor" "postgres_monitor" {
  type = "tcp"; port = 5432; interval = 30; timeout = 5
}

resource "cloudflare_spectrum_application" "postgres_ha" {
  zone_id     = var.zone_id
  protocol    = "tcp/5432"
  dns         { type = "CNAME"; name = "postgres.example.com" }
  origin_dns  { name = cloudflare_load_balancer.database_lb.name }
  origin_port = 5432
  tls         = "strict"
  ip_firewall = true
}
```

**Benefits:** Automatic failover, health monitoring, traffic distribution, zero-downtime deployments


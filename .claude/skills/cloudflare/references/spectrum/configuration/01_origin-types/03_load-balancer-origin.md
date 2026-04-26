### Load Balancer Origin

Use for high availability and failover.

**Terraform:**
```hcl
resource "cloudflare_load_balancer" "game_lb" {
  zone_id          = var.zone_id
  name             = "game-lb.example.com"
  default_pool_ids = [cloudflare_load_balancer_pool.game_pool.id]
}

resource "cloudflare_load_balancer_pool" "game_pool" {
  name    = "game-primary"
  origins { name = "game-1"; address = "192.0.2.1" }
  monitor = cloudflare_load_balancer_monitor.tcp_monitor.id
}

resource "cloudflare_load_balancer_monitor" "tcp_monitor" {
  type = "tcp"; port = 25565; interval = 60; timeout = 5
}

resource "cloudflare_spectrum_application" "game" {
  zone_id  = var.zone_id
  protocol = "tcp/25565"
  dns { type = "CNAME"; name = "game.example.com" }
  origin_dns { name = cloudflare_load_balancer.game_lb.name }
  origin_port = 25565
}
```


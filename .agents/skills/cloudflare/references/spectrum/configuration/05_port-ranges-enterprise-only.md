## Port Ranges (Enterprise Only)

```hcl
resource "cloudflare_spectrum_application" "game_cluster" {
  zone_id  = var.zone_id
  protocol = "tcp/25565-25575"

  dns {
    type = "CNAME"
    name = "games.example.com"
  }

  origin_direct = ["tcp://192.0.2.1"]
  
  origin_port {
    start = 25565
    end   = 25575
  }
}
```


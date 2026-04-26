### 1. SSH Server Protection

**Terraform:**
```hcl
resource "cloudflare_spectrum_application" "ssh" {
  zone_id  = var.zone_id
  protocol = "tcp/22"

  dns {
    type = "CNAME"
    name = "ssh.example.com"
  }

  origin_direct      = ["tcp://10.0.1.5:22"]
  ip_firewall        = true
  argo_smart_routing = true
}
```

**Benefits:** Hide origin IP, DDoS protection, IP firewall, Argo reduces latency


### 6. RDP (Remote Desktop)

**Requires IP firewall.**

**Terraform:**
```hcl
resource "cloudflare_spectrum_application" "rdp" {
  zone_id  = var.zone_id
  protocol = "tcp/3389"

  dns {
    type = "CNAME"
    name = "rdp.example.com"
  }

  origin_direct = ["tcp://windows-server.internal:3389"]
  tls           = "off"       # RDP has own encryption
  ip_firewall   = true        # REQUIRED
}
```

**Security:** ALWAYS `ip_firewall: true`, whitelist admin IPs, RDP is DDoS/brute-force target


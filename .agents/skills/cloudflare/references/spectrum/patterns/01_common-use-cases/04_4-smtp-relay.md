### 4. SMTP Relay

Email submission (port 587). **WARNING**: See [gotchas.md](gotchas.md#smtp-reverse-dns)

**Terraform:**
```hcl
resource "cloudflare_spectrum_application" "smtp" {
  zone_id  = var.zone_id
  protocol = "tcp/587"

  dns {
    type = "CNAME"
    name = "smtp.example.com"
  }

  origin_direct = ["tcp://mail-server.internal:587"]
  tls           = "full"  # STARTTLS support
}
```

**Limitations:**
- Spectrum IPs lack reverse DNS (PTR records)
- Many mail servers reject without valid rDNS
- Best for internal/trusted relay only


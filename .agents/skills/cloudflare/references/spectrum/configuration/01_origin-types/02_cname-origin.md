### CNAME Origin

Use when origin is a hostname (not static IP). Spectrum resolves DNS dynamically.

**TypeScript SDK:**
```typescript
const app = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/3306',
  dns: { type: 'CNAME', name: 'db.example.com' },
  origin_dns: { name: 'db-primary.internal.example.com' },
  origin_port: 3306,
  tls: 'full',
});
```

**Terraform:**
```hcl
resource "cloudflare_spectrum_application" "database" {
  zone_id  = var.zone_id
  protocol = "tcp/3306"

  dns {
    type = "CNAME"
    name = "db.example.com"
  }

  origin_dns {
    name = "db-primary.internal.example.com"
  }

  origin_port        = 3306
  tls                = "full"
  argo_smart_routing = true
}
```


### Direct IP Origin

Use when origin is a single server with static IP.

**TypeScript SDK:**
```typescript
const app = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/22',
  dns: { type: 'CNAME', name: 'ssh.example.com' },
  origin_direct: ['tcp://192.0.2.1:22'],
  ip_firewall: true,
  tls: 'off',
});
```

**Terraform:**
```hcl
resource "cloudflare_spectrum_application" "ssh" {
  zone_id  = var.zone_id
  protocol = "tcp/22"

  dns {
    type = "CNAME"
    name = "ssh.example.com"
  }

  origin_direct      = ["tcp://192.0.2.1:22"]
  ip_firewall        = true
  tls                = "off"
  argo_smart_routing = true
}
```


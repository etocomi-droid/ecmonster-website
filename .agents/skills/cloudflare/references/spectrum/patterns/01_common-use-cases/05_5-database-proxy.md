### 5. Database Proxy

MySQL/PostgreSQL. **Use with caution** - security critical.

**PostgreSQL:**
```typescript
const postgresApp = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/5432',
  dns: { type: 'CNAME', name: 'postgres.example.com' },
  origin_dns: { name: 'db-primary.internal.example.com' },
  origin_port: 5432,
  tls: 'strict',      // REQUIRED
  ip_firewall: true,  // REQUIRED
});
```

**MySQL:**
```hcl
resource "cloudflare_spectrum_application" "mysql" {
  zone_id  = var.zone_id
  protocol = "tcp/3306"

  dns {
    type = "CNAME"
    name = "mysql.example.com"
  }

  origin_dns {
    name = "mysql-primary.internal.example.com"
  }

  origin_port = 3306
  tls         = "strict"
  ip_firewall = true
}
```

**Security:**
- ALWAYS use `tls: "strict"`
- ALWAYS use `ip_firewall: true`
- Restrict to known IPs via zone firewall
- Use strong DB authentication
- Consider VPN or Cloudflare Access instead


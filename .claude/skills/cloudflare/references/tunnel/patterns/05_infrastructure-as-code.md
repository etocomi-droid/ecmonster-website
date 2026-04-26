## Infrastructure as Code

### Terraform

```hcl
resource "random_id" "tunnel_secret" {
  byte_length = 32
}

resource "cloudflare_tunnel" "app" {
  account_id = var.cloudflare_account_id
  name       = "app-tunnel"
  secret     = random_id.tunnel_secret.b64_std
}

resource "cloudflare_tunnel_config" "app" {
  account_id = var.cloudflare_account_id
  tunnel_id  = cloudflare_tunnel.app.id
  config {
    ingress_rule {
      hostname = "app.example.com"
      service  = "http://localhost:8000"
    }
    ingress_rule { service = "http_status:404" }
  }
}

resource "cloudflare_record" "app" {
  zone_id = var.cloudflare_zone_id
  name    = "app"
  value   = cloudflare_tunnel.app.cname
  type    = "CNAME"
  proxied = true
}

output "tunnel_token" {
  value     = cloudflare_tunnel.app.tunnel_token
  sensitive = true
}
```

### Pulumi

```typescript
import * as cloudflare from "@pulumi/cloudflare";
import * as random from "@pulumi/random";

const secret = new random.RandomId("secret", { byteLength: 32 });

const tunnel = new cloudflare.ZeroTrustTunnelCloudflared("tunnel", {
  accountId: accountId,
  name: "app-tunnel",
  secret: secret.b64Std,
});

const config = new cloudflare.ZeroTrustTunnelCloudflaredConfig("config", {
  accountId: accountId,
  tunnelId: tunnel.id,
  config: {
    ingressRules: [
      { hostname: "app.example.com", service: "http://localhost:8000" },
      { service: "http_status:404" },
    ],
  },
});

new cloudflare.Record("dns", {
  zoneId: zoneId,
  name: "app",
  value: tunnel.cname,
  type: "CNAME",
  proxied: true,
});
```


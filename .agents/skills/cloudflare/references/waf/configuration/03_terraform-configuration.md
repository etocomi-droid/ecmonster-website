## Terraform Configuration

```hcl
provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

resource "cloudflare_ruleset" "waf_custom" {
  zone_id = var.zone_id
  kind    = "zone"
  phase   = "http_request_firewall_custom"

  rules {
    action     = "block"
    expression = "cf.waf.score gt 50"
  }
}
```

**Managed Ruleset & Rate Limiting**:
```hcl
resource "cloudflare_ruleset" "waf_managed" {
  zone_id = var.zone_id
  name    = "Managed Ruleset"
  kind    = "zone"
  phase   = "http_request_firewall_managed"

  rules {
    action = "execute"
    action_parameters {
      id = "efb7b8c949ac4650a09736fc376e9aee"
      overrides {
        rules {
          id = "5de7edfa648c4d6891dc3e7f84534ffa"
          action = "log"
        }
      }
    }
    expression = "true"
  }
}

resource "cloudflare_ruleset" "rate_limiting" {
  zone_id = var.zone_id
  phase   = "http_ratelimit"

  rules {
    action = "block"
    expression = "http.request.uri.path starts_with \"/api\""
    ratelimit {
      characteristics     = ["cf.colo.id", "ip.src"]
      period              = 60
      requests_per_period = 100
      mitigation_timeout  = 600
    }
  }
}
```


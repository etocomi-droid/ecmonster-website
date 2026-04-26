## Terraform

```hcl
# Session identifier
resource "cloudflare_api_shield" "main" {
  zone_id = var.zone_id
  auth_id_characteristics {
    type = "header"
    name = "Authorization"
  }
}

# Add endpoint
resource "cloudflare_api_shield_operation" "users_get" {
  zone_id  = var.zone_id
  method   = "GET"
  host     = "api.example.com"
  endpoint = "/api/users/{id}"
}

# JWT validation rule
resource "cloudflare_ruleset" "jwt_validation" {
  zone_id = var.zone_id
  name    = "API JWT Validation"
  kind    = "zone"
  phase   = "http_request_firewall_custom"

  rules {
    action = "block"
    expression = "(http.host eq \"api.example.com\" and not is_jwt_valid(http.request.jwt.payload[\"{config_id}\"][0]))"
    description = "Block invalid JWTs"
  }
}
```


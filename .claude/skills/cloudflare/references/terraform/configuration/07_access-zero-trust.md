## Access (Zero Trust)

```hcl
resource "cloudflare_access_application" "admin" {
  account_id = var.account_id; name = "Admin"; domain = "admin.example.com"; type = "self_hosted"
  session_duration = "24h"; allowed_idps = [cloudflare_access_identity_provider.github.id]
}
resource "cloudflare_access_policy" "allow" {
  account_id = var.account_id; application_id = cloudflare_access_application.admin.id
  name = "Allow"; decision = "allow"; precedence = 1
  include { email = ["admin@example.com"] }
}
resource "cloudflare_access_identity_provider" "github" {
  account_id = var.account_id; name = "GitHub"; type = "github"
  config { client_id = var.github_id; client_secret = var.github_secret }
}
```


## Account Data Sources

```hcl
# List all accounts
data "cloudflare_accounts" "main" {
  name = "My Account"
}

# Use account ID
resource "cloudflare_worker_script" "api" {
  account_id = data.cloudflare_accounts.main.accounts[0].id
  # ...
}
```


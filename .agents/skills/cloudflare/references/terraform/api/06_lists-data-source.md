## Lists Data Source

```hcl
# Get IP lists for WAF rules
data "cloudflare_list" "blocked_ips" {
  account_id = var.account_id
  name = "blocked_ips"
}
```


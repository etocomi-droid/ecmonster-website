## Zone & DNS

```hcl
# Zone + settings
resource "cloudflare_zone" "example" { account = { id = var.account_id }; name = "example.com"; type = "full" }
resource "cloudflare_zone_settings_override" "example" {
  zone_id = cloudflare_zone.example.id
  settings { ssl = "strict"; always_use_https = "on"; min_tls_version = "1.2"; tls_1_3 = "on"; http3 = "on" }
}

# DNS records (A, CNAME, MX, TXT)
resource "cloudflare_dns_record" "www" {
  zone_id = cloudflare_zone.example.id; name = "www"; content = "192.0.2.1"; type = "A"; proxied = true
}
resource "cloudflare_dns_record" "mx" {
  for_each = { "10" = "mail1.example.com", "20" = "mail2.example.com" }
  zone_id = cloudflare_zone.example.id; name = "@"; content = each.value; type = "MX"; priority = each.key
}
```


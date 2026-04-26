## Rulesets (WAF, Redirects, Cache)

```hcl
# WAF
resource "cloudflare_ruleset" "waf" {
  zone_id = cloudflare_zone.example.id; name = "WAF"; kind = "zone"; phase = "http_request_firewall_custom"
  rules { action = "block"; enabled = true; expression = "(cf.client.bot) and not (cf.verified_bot)" }
}

# Redirects
resource "cloudflare_ruleset" "redirects" {
  zone_id = cloudflare_zone.example.id; name = "Redirects"; kind = "zone"; phase = "http_request_dynamic_redirect"
  rules {
    action = "redirect"; enabled = true; expression = "(http.request.uri.path eq \"/old\")"
    action_parameters { from_value { status_code = 301; target_url { value = "https://example.com/new" }}}
  }
}

# Cache rules
resource "cloudflare_ruleset" "cache" {
  zone_id = cloudflare_zone.example.id; name = "Cache"; kind = "zone"; phase = "http_request_cache_settings"
  rules {
    action = "set_cache_settings"; enabled = true; expression = "(http.request.uri.path matches \"\\.(jpg|png|css|js)$\")"
    action_parameters { cache = true; edge_ttl { mode = "override_origin"; default = 86400 }}
  }
}
```


### Terraform

```hcl
terraform {
  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4.0"
    }
  }
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

resource "cloudflare_zone_cache_reserve" "example" {
  zone_id = var.zone_id
  enabled = true
}

# Tiered Cache is required for Cache Reserve
resource "cloudflare_tiered_cache" "example" {
  zone_id    = var.zone_id
  cache_type = "smart"
}
```


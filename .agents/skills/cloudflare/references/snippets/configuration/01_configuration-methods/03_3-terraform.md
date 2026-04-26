### 3. Terraform
**Best for**: Infrastructure-as-code, multi-zone deployments

```hcl
# Configure Terraform provider
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

# Create snippet
resource "cloudflare_snippet" "security_headers" {
  zone_id = var.zone_id
  name    = "security_headers"
  
  main_module = "security_headers.js"
  files {
    name    = "security_headers.js"
    content = file("${path.module}/snippets/security_headers.js")
  }
}

# Create snippet rule
resource "cloudflare_snippet_rules" "security_rules" {
  zone_id = var.zone_id
  
  rules {
    description  = "Apply security headers to all requests"
    enabled      = true
    expression   = "true"
    snippet_name = cloudflare_snippet.security_headers.name
  }
}
```


## R2 State Backend

```hcl
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key = "cloudflare.tfstate"
    region = "auto"
    endpoints = { s3 = "https://<account_id>.r2.cloudflarestorage.com" }
    skip_credentials_validation = true
    skip_region_validation = true
    skip_requesting_account_id = true
    skip_metadata_api_check = true
    skip_s3_checksum = true
  }
}
```


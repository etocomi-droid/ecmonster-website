## Multi-Environment Setup

```hcl
# Directory: environments/{production,staging}/main.tf + modules/{zone,worker,pages}
module "zone" {
  source = "../../modules/zone"; account_id = var.account_id; zone_name = "example.com"; environment = "production"
}
module "api_worker" {
  source = "../../modules/worker"; account_id = var.account_id; zone_id = module.zone.zone_id
  name = "api-worker-prod"; script = file("../../workers/api.js"); environment = "production"
}
```


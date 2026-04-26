## Recommended Directory Structure

```
terraform/
├── environments/
│   ├── production/
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   └── staging/
│       ├── main.tf
│       └── terraform.tfvars
├── modules/
│   ├── zone/
│   ├── worker/
│   └── dns/
└── shared/          # Shared resources across envs
    └── main.tf
```

**Note:** Cloudflare recommends avoiding modules for provider resources due to v5 auto-generation complexity. Prefer environment directories + shared state instead.


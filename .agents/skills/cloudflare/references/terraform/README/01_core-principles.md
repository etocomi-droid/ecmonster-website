## Core Principles

- **Provider-first**: Use Terraform provider for ALL infrastructure - never mix with wrangler.jsonc for the same resources
- **State management**: Always use remote state (S3, Terraform Cloud, etc.) for team environments
- **Modular architecture**: Create reusable modules for common patterns (zones, workers, pages)
- **Version pinning**: Always pin provider version with `~>` for predictable upgrades
- **Secret management**: Use variables + environment vars for sensitive data - never hardcode API tokens


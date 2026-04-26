## Configuration Management

**Note on Smart Shield Evolution:** Argo Smart Routing is being integrated into Smart Shield. Configuration methods below remain valid; Terraform and IaC patterns unchanged.

### Infrastructure as Code (Terraform)

```hcl
# terraform/argo.tf
# Note: Use Cloudflare Terraform provider

resource "cloudflare_argo" "example" {
  zone_id        = var.zone_id
  smart_routing  = "on"
  tiered_caching = "on"
}

variable "zone_id" {
  description = "Cloudflare Zone ID"
  type        = string
}

output "argo_enabled" {
  value       = cloudflare_argo.example.smart_routing
  description = "Argo Smart Routing status"
}
```

### Environment-Based Configuration

```typescript
// config/argo.ts
interface ArgoEnvironmentConfig {
  enabled: boolean;
  tieredCache: boolean;
  monitoring: {
    usageAlerts: boolean;
    threshold: number;
  };
}

const configs: Record<string, ArgoEnvironmentConfig> = {
  production: {
    enabled: true,
    tieredCache: true,
    monitoring: {
      usageAlerts: true,
      threshold: 1000, // GB
    },
  },
  staging: {
    enabled: true,
    tieredCache: false,
    monitoring: {
      usageAlerts: false,
      threshold: 100, // GB
    },
  },
  development: {
    enabled: false,
    tieredCache: false,
    monitoring: {
      usageAlerts: false,
      threshold: 0,
    },
  },
};

export function getArgoConfig(env: string): ArgoEnvironmentConfig {
  return configs[env] || configs.development;
}
```

### Pulumi Configuration

```typescript
// pulumi/argo.ts
import * as cloudflare from '@pulumi/cloudflare';

const zone = new cloudflare.Zone('example-zone', {
  zone: 'example.com',
  plan: 'enterprise',
});

const argoSettings = new cloudflare.Argo('argo-config', {
  zoneId: zone.id,
  smartRouting: 'on',
  tieredCaching: 'on',
});

export const argoEnabled = argoSettings.smartRouting;
export const zoneId = zone.id;
```


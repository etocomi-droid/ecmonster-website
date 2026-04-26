## Alert Configuration

```typescript
interface DDoSAlertConfig {
  name: string;
  enabled: boolean;
  alert_type: "http_ddos_attack_alert" | "layer_3_4_ddos_attack_alert" 
    | "advanced_http_ddos_attack_alert" | "advanced_layer_3_4_ddos_attack_alert";
  filters?: {
    zones?: string[];
    hostnames?: string[];
    requests_per_second?: number;
    packets_per_second?: number;
    megabits_per_second?: number;
    ip_prefixes?: string[]; // CIDR
    ip_addresses?: string[];
    protocols?: string[];
  };
  mechanisms: {
    email?: Array<{ id: string }>;
    webhooks?: Array<{ id: string }>;
    pagerduty?: Array<{ id: string }>;
  };
}

// Create alert
await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${accountId}/alerting/v3/policies`,
  {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(alertConfig),
  }
);
```


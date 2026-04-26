## Multi-rule Tiered Protection (Enterprise Advanced)

```typescript
const config = {
  description: "Multi-tier DDoS protection",
  rules: [
    {
      expression: "not ip.src in $known_ips and not cf.bot_management.score gt 30",
      action: "execute",
      action_parameters: { id: managedRulesetId, overrides: { sensitivity_level: "default", action: "block" } },
    },
    {
      expression: "cf.bot_management.verified_bot",
      action: "execute",
      action_parameters: { id: managedRulesetId, overrides: { sensitivity_level: "medium", action: "managed_challenge" } },
    },
    {
      expression: "ip.src in $trusted_ips",
      action: "execute",
      action_parameters: { id: managedRulesetId, overrides: { sensitivity_level: "low" } },
    },
  ],
};
```


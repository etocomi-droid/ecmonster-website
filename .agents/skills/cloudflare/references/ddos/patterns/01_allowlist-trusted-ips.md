## Allowlist Trusted IPs

```typescript
const config = {
  description: "Allowlist trusted IPs",
  rules: [{
    expression: "ip.src in { 203.0.113.0/24 192.0.2.1 }",
    action: "execute",
    action_parameters: {
      id: managedRulesetId,
      overrides: { sensitivity_level: "eoff" },
    },
  }],
};

await client.accounts.rulesets.phases.entrypoint.update("ddos_l7", {
  account_id: accountId,
  ...config,
});
```


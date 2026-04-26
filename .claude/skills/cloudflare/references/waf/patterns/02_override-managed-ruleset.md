## Override Managed Ruleset

```typescript
await client.rulesets.create({
  zone_id: 'zone_id',
  phase: 'http_request_firewall_managed',
  rules: [{
    action: 'execute',
    action_parameters: {
      id: 'efb7b8c949ac4650a09736fc376e9aee',
      overrides: {
        // Override specific rules
        rules: [
          { id: '5de7edfa648c4d6891dc3e7f84534ffa', action: 'log' },
          { id: '75a0060762034b9dad4e883afc121b4c', enabled: false },
        ],
        // Override categories: wordpress, sqli, xss, rce, etc.
        categories: [
          { category: 'wordpress', enabled: false },
          { category: 'sqli', action: 'log' },
        ],
      },
    },
    expression: 'true',
  }],
});
```


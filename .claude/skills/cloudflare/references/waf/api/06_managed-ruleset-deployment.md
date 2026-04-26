## Managed Ruleset Deployment

```typescript
{
  action: 'execute',
  action_parameters: {
    id: 'efb7b8c949ac4650a09736fc376e9aee', // Cloudflare Managed
    overrides: {
      // Override specific rules
      rules: [
        { id: '5de7edfa648c4d6891dc3e7f84534ffa', action: 'log', enabled: true },
      ],
      // Override categories: 'wordpress', 'sqli', 'xss', 'rce', etc.
      categories: [
        { category: 'wordpress', enabled: false },
        { category: 'sqli', action: 'log' },
      ],
    },
  },
  expression: 'true',
  enabled: true,
}
```


## Route-specific Sensitivity

```typescript
const config = {
  description: "Route-specific protection",
  rules: [
    {
      expression: "not http.request.uri.path matches \"^/api/\"",
      action: "execute",
      action_parameters: {
        id: managedRulesetId,
        overrides: { sensitivity_level: "default", action: "block" },
      },
    },
    {
      expression: "http.request.uri.path matches \"^/api/\"",
      action: "execute",
      action_parameters: {
        id: managedRulesetId,
        overrides: { sensitivity_level: "low", action: "managed_challenge" },
      },
    },
  ],
};
```


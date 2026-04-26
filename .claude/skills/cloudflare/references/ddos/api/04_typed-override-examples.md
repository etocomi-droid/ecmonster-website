## Typed Override Examples

```typescript
// Override by category
interface CategoryOverride {
  action: "execute";
  expression: string;
  action_parameters: {
    id: string;
    overrides: {
      categories?: Array<{
        category: "http-flood" | "http-anomaly" | "udp-flood" | "syn-flood";
        sensitivity_level?: "default" | "medium" | "low" | "eoff";
        action?: "block" | "managed_challenge" | "challenge" | "log";
      }>;
    };
  };
}

// Override by rule ID
interface RuleOverride {
  action: "execute";
  expression: string;
  action_parameters: {
    id: string;
    overrides: {
      rules?: Array<{
        id: string;
        action?: "block" | "managed_challenge" | "challenge" | "log";
        sensitivity_level?: "default" | "medium" | "low" | "eoff";
      }>;
    };
  };
}

// Example: Override specific adaptive rule
const adaptiveOverride: RuleOverride = {
  action: "execute",
  expression: "true",
  action_parameters: {
    id: managedRulesetId,
    overrides: {
      rules: [
        { id: "...adaptive-origins-rule-id...", sensitivity_level: "low" },
      ],
    },
  },
};
```

See [patterns.md](./patterns.md) for complete implementation patterns.

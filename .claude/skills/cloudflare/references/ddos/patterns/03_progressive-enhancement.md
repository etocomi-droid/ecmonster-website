## Progressive Enhancement

```typescript
enum ProtectionLevel { MONITORING = "monitoring", LOW = "low", MEDIUM = "medium", HIGH = "high" }

const levelConfig = {
  [ProtectionLevel.MONITORING]: { action: "log", sensitivity: "eoff" },
  [ProtectionLevel.LOW]: { action: "managed_challenge", sensitivity: "low" },
  [ProtectionLevel.MEDIUM]: { action: "managed_challenge", sensitivity: "medium" },
  [ProtectionLevel.HIGH]: { action: "block", sensitivity: "default" },
} as const;

async function setProtectionLevel(zoneId: string, level: ProtectionLevel, rulesetId: string, client: Cloudflare) {
  const settings = levelConfig[level];
  return client.zones.rulesets.phases.entrypoint.update("ddos_l7", {
    zone_id: zoneId,
    rules: [{
      expression: "true",
      action: "execute",
      action_parameters: { id: rulesetId, overrides: { action: settings.action, sensitivity_level: settings.sensitivity } },
    }],
  });
}
```


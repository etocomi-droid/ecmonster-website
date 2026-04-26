## TypeScript SDK

**SDK Version**: Requires `cloudflare` >= 3.0.0 for ruleset phase methods.

```typescript
import Cloudflare from "cloudflare";

const client = new Cloudflare({ apiToken: process.env.CLOUDFLARE_API_TOKEN });

// STEP 1: Discover managed ruleset ID (required for overrides)
const allRulesets = await client.rulesets.list({ zone_id: zoneId });
const ddosRuleset = allRulesets.result.find(
  (r) => r.kind === "managed" && r.phase === "ddos_l7"
);
if (!ddosRuleset) throw new Error("DDoS managed ruleset not found");
const managedRulesetId = ddosRuleset.id;

// STEP 2: Get current HTTP DDoS configuration
const entrypointRuleset = await client.zones.rulesets.phases.entrypoint.get("ddos_l7", {
  zone_id: zoneId,
});

// STEP 3: Update HTTP DDoS ruleset with overrides
await client.zones.rulesets.phases.entrypoint.update("ddos_l7", {
  zone_id: zoneId,
  rules: [
    {
      action: "execute",
      expression: "true",
      action_parameters: {
        id: managedRulesetId, // From discovery step
        overrides: {
          sensitivity_level: "medium",
          action: "managed_challenge",
        },
      },
    },
  ],
});

// Network DDoS (account level, L3/4)
const l4Rulesets = await client.rulesets.list({ account_id: accountId });
const l4DdosRuleset = l4Rulesets.result.find(
  (r) => r.kind === "managed" && r.phase === "ddos_l4"
);
const l4Ruleset = await client.accounts.rulesets.phases.entrypoint.get("ddos_l4", {
  account_id: accountId,
});
```


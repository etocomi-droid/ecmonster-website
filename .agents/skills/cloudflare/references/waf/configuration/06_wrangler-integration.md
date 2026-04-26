## Wrangler Integration

WAF configuration is zone-level (not Worker-specific). Configuration methods:
- Dashboard UI
- Cloudflare API via SDK
- Terraform/Pulumi (IaC)

**Workers benefit from WAF automatically** - no Worker code changes needed.

**Example: Query WAF API from Worker**:
```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    return fetch(`https://api.cloudflare.com/client/v4/zones/${env.ZONE_ID}/rulesets`, {
      headers: { 'Authorization': `Bearer ${env.CF_API_TOKEN}` },
    });
  },
};
```
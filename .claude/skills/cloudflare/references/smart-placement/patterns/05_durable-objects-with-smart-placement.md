## Durable Objects with Smart Placement

**Key principle:** Smart Placement does NOT control WHERE Durable Objects run. DOs always run in their designated region (based on jurisdiction or smart location hints).

**What Smart Placement DOES affect:** The location of the coordinator Worker's `fetch` handler that makes calls to multiple DOs.

**Pattern:** Enable Smart Placement on coordinator Worker that aggregates data from multiple DOs:

```typescript
// Worker with Smart Placement - aggregates data from multiple DOs
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const userId = new URL(request.url).searchParams.get('user');
    
    // Get DO stubs
    const userDO = env.USER_DO.get(env.USER_DO.idFromName(userId));
    const analyticsID = env.ANALYTICS_DO.idFromName(`analytics-${userId}`);
    const analyticsDO = env.ANALYTICS_DO.get(analyticsID);
    
    // Fetch from multiple DOs
    const [userData, analyticsData] = await Promise.all([
      userDO.fetch(new Request('https://do/profile')),
      analyticsDO.fetch(new Request('https://do/stats'))
    ]);
    
    return Response.json({
      user: await userData.json(),
      analytics: await analyticsData.json()
    });
  }
};
```

```jsonc
// wrangler.jsonc
{
  "placement": { "mode": "smart" },
  "durable_objects": {
    "bindings": [
      { "name": "USER_DO", "class_name": "UserDO" },
      { "name": "ANALYTICS_DO", "class_name": "AnalyticsDO" }
    ]
  }
}
```

**When this helps:** 
- Worker's `fetch` handler runs closer to DO regions, reducing network latency for multiple DO calls
- Most beneficial when DOs are geographically concentrated or in specific jurisdictions
- Helps when coordinator makes many sequential or parallel DO calls

**When this DOESN'T help:**
- DOs are globally distributed (no single optimal Worker location)
- Worker only calls a single DO
- DO calls are infrequent or cached


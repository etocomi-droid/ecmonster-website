## Billing by Plan

```typescript
interface Env {
  DISPATCHER: DispatchNamespace;
  CUSTOMERS_KV: KVNamespace;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const userWorkerName = new URL(request.url).hostname.split(".")[0];
    const customerPlan = await env.CUSTOMERS_KV.get(userWorkerName);
    
    const plans = {
      enterprise: { cpuMs: 50, subRequests: 50 },
      pro: { cpuMs: 20, subRequests: 20 },
      free: { cpuMs: 10, subRequests: 5 },
    };
    const limits = plans[customerPlan as keyof typeof plans] || plans.free;
    
    const userWorker = env.DISPATCHER.get(userWorkerName, {}, { limits });
    return await userWorker.fetch(request);
  },
};
```


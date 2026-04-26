## 10. Multi-Tenant

```typescript
interface Env { TENANTS: KVNamespace; }

export default {
  async email(message, env, ctx) {
    const subdomain = message.to.split("@")[1].split(".")[0];
    const config = await env.TENANTS.get(subdomain, "json") as { forward: string } | null;
    
    if (!config) {
      message.setReject("Unknown tenant");
      return;
    }
    
    await message.forward(config.forward);
  }
} satisfies ExportedHandler<Env>;
```


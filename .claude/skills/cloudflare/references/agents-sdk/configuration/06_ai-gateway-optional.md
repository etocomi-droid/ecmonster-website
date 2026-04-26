## AI Gateway (Optional)

```typescript
// Enable caching/routing through AI Gateway
const response = await this.env.AI.run(
  "@cf/meta/llama-3.1-8b-instruct",
  { prompt },
  {
    gateway: {
      id: "my-gateway-id",
      skipCache: false,
      cacheTtl: 3600
    }
  }
);
```


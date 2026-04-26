## Debugging

```typescript
// Log request details
console.log('Request:', { method: request.method, url: request.url });
console.log('Env:', Object.keys(env));
console.log('Params:', params);
```

**View logs**: `npx wrangler pages deployment tail --project-name=my-project`


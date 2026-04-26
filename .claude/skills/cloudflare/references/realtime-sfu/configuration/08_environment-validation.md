## Environment Validation

Check credentials before first API call:

```typescript
if (!env.CALLS_APP_ID || !env.CALLS_APP_SECRET) {
  throw new Error('CALLS_APP_ID and CALLS_APP_SECRET required');
}
```

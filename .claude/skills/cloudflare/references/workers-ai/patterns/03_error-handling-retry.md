## Error Handling & Retry

```typescript
async function runWithRetry(env, model, input, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await env.AI.run(model, input);
    } catch (error) {
      if (error.message?.includes('7505') && attempt < maxRetries - 1) {
        await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 1000));
        continue;
      }
      throw error;
    }
  }
}
```


## Step Configuration

```typescript
// Basic step
const data = await step.do('step name', async () => ({ result: 'value' }));

// With retry config
await step.do('api call', {
  retries: {
    limit: 10,              // Default: 5, or Infinity
    delay: '10 seconds',    // Default: 10000ms
    backoff: 'exponential'  // constant | linear | exponential
  },
  timeout: '30 minutes'     // Per-attempt timeout (default: 10min)
}, async () => {
  const res = await fetch('https://api.example.com/data');
  if (!res.ok) throw new Error('Failed');
  return res.json();
});
```

### Parallel Steps
```typescript
const [user, settings] = await Promise.all([
  step.do('fetch user', async () => this.env.KV.get(`user:${id}`)),
  step.do('fetch settings', async () => this.env.KV.get(`settings:${id}`))
]);
```

### Conditional Steps
```typescript
const config = await step.do('fetch config', async () => 
  this.env.KV.get('flags', { type: 'json' })
);

// ✅ Deterministic (based on step output)
if (config.enableEmail) {
  await step.do('send email', async () => sendEmail());
}

// ❌ Non-deterministic (Date.now outside step)
if (Date.now() > deadline) { /* BAD */ }
```

### Dynamic Steps (Loops)
```typescript
const files = await step.do('list files', async () => 
  this.env.BUCKET.list()
);

for (const file of files.objects) {
  await step.do(`process ${file.key}`, async () => {
    const obj = await this.env.BUCKET.get(file.key);
    return processData(await obj.arrayBuffer());
  });
}
```


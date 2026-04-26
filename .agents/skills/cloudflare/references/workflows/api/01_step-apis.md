## Step APIs

```typescript
// step.do()
const result = await step.do('step name', async () => { /* logic */ });
const result = await step.do('step name', { retries, timeout }, async () => {});

// step.sleep()
await step.sleep('description', '1 hour');
await step.sleep('description', 5000); // ms

// step.sleepUntil()
await step.sleepUntil('description', Date.parse('2024-12-31'));

// step.waitForEvent()
const data = await step.waitForEvent<PayloadType>('wait', {event: 'webhook-type', timeout: '24h'}); // Default 24h, max 365d
try { const event = await step.waitForEvent('wait', { event: 'approval', timeout: '1h' }); } catch (e) { /* Timeout */ }
```


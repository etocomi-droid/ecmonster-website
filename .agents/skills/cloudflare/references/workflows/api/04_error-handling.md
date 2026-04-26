## Error Handling

```typescript
import { NonRetryableError } from 'cloudflare:workers';

// NonRetryableError
await step.do('validate', async () => {
  if (!event.payload.paymentMethod) throw new NonRetryableError('Payment method required');
  const res = await fetch('https://api.example.com/charge', { method: 'POST' });
  if (res.status === 401) throw new NonRetryableError('Invalid credentials'); // Don't retry
  if (!res.ok) throw new Error('Retryable failure'); // Will retry
  return res.json();
});

// Catching Errors
try { await step.do('risky op', async () => { throw new NonRetryableError('Failed'); }); } catch (e) { await step.do('cleanup', async () => {}); }

// Idempotency
await step.do('charge', async () => {
  const sub = await fetch(`https://api/subscriptions/${id}`).then(r => r.json());
  if (sub.charged) return sub; // Already done
  return await fetch(`https://api/subscriptions/${id}`, {method: 'POST', body: JSON.stringify({ amount: 10.0 })}).then(r => r.json());
});
```


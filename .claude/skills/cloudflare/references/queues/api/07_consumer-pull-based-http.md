## Consumer: Pull-based (HTTP)

```typescript
// Pull messages
const response = await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull`,
  {
    method: 'POST',
    headers: { 'authorization': `Bearer ${API_TOKEN}`, 'content-type': 'application/json' },
    body: JSON.stringify({ visibility_timeout_ms: 6000, batch_size: 50 })
  }
);

const data = await response.json();

// Acknowledge
await fetch(
  `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/queues/${QUEUE_ID}/messages/ack`,
  {
    method: 'POST',
    headers: { 'authorization': `Bearer ${API_TOKEN}`, 'content-type': 'application/json' },
    body: JSON.stringify({
      acks: [{ lease_id: msg.lease_id }],
      retries: [{ lease_id: msg2.lease_id, delay_seconds: 600 }]
    })
  }
);
```


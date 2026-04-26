## Testing

Add test endpoint to producer:

```typescript
export default {
  async fetch(request) {
    if (request.url.includes('/test')) {
      console.log('Test log');
      throw new Error('Test error');
    }
    return new Response('OK');
  }
};
```

Trigger: `curl https://producer.example.workers.dev/test`


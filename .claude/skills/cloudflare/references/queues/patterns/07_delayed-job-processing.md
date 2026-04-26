## Delayed Job Processing

```typescript
await env.EMAIL_QUEUE.send({ to, template, userId }, { delaySeconds: 3600 });
```


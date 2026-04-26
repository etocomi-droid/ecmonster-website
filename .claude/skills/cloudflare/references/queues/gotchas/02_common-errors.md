## Common Errors

### "Duplicate Message Processing"

**Problem:** Same message processed multiple times  
**Cause:** At-least-once delivery guarantee means duplicates are possible during retries  
**Solution:** Design consumers to be idempotent by tracking processed message IDs in KV with expiration TTL

```typescript
async queue(batch: MessageBatch, env: Env): Promise<void> {
  for (const msg of batch.messages) {
    const processed = await env.PROCESSED_KV.get(msg.id);
    if (processed) {
      msg.ack();
      continue;
    }
    
    await processMessage(msg.body);
    await env.PROCESSED_KV.put(msg.id, '1', { expirationTtl: 86400 });
    msg.ack();
  }
}
```

### "Pull Consumer Can't Decode Messages"

**Problem:** Pull consumer or dashboard shows unreadable message bodies  
**Cause:** Messages sent with `v8` content type are only decodable by Workers push consumers  
**Solution:** Use `json` content type for pull consumers or dashboard visibility

```typescript
// Use json for pull consumers
await env.MY_QUEUE.send(data, { contentType: 'json' });

// Use v8 only for push consumers with complex JS types
await env.MY_QUEUE.send({ date: new Date(), tags: new Set() }, { contentType: 'v8' });
```

### "Messages Not Being Delivered"

**Problem:** Messages sent but consumer not processing  
**Cause:** Queue paused, consumer not configured, or consumer errors  
**Solution:** Check queue status with `wrangler queues list`, verify consumer configured with `wrangler queues consumer add`, and check logs with `wrangler tail`

### "High Dead Letter Queue Rate"

**Problem:** Many messages ending up in DLQ  
**Cause:** Consumer repeatedly failing to process messages after max retries  
**Solution:** Review consumer error logs, check external dependency availability, verify message format matches expectations, or increase retry delay


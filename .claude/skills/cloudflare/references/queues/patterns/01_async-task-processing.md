## Async Task Processing

```typescript
// Producer: Accept request, queue work
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { userId, reportType } = await request.json();
    await env.REPORT_QUEUE.send({ userId, reportType, requestedAt: Date.now() });
    return Response.json({ message: 'Report queued', status: 'pending' });
  }
};

// Consumer: Process reports
export default {
  async queue(batch: MessageBatch, env: Env): Promise<void> {
    for (const msg of batch.messages) {
      const { userId, reportType } = msg.body;
      const report = await generateReport(userId, reportType, env);
      await env.REPORTS_BUCKET.put(`${userId}/${reportType}.pdf`, report);
      msg.ack();
    }
  }
};
```


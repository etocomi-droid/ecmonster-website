## TypeScript Types

```typescript
interface Env {
  MY_QUEUE: Queue<MessageBody>;
  ANALYTICS_QUEUE: Queue<AnalyticsEvent>;
}

interface MessageBody {
  id: string;
  action: 'create' | 'update' | 'delete';
  data: Record<string, any>;
}

export default {
  async queue(batch: MessageBatch<MessageBody>, env: Env): Promise<void> {
    for (const msg of batch.messages) {
      console.log(msg.body.action);
      msg.ack();
    }
  }
} satisfies ExportedHandler<Env>;
```


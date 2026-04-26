## Bindings

Workflows access Cloudflare bindings via `this.env`:

```typescript
type Env = {
  MY_WORKFLOW: Workflow;
  KV: KVNamespace;
  DB: D1Database;
  BUCKET: R2Bucket;
  AI: Ai;
  VECTORIZE: VectorizeIndex;
};

await step.do('use bindings', async () => {
  const kv = await this.env.KV.get('key');
  const db = await this.env.DB.prepare('SELECT * FROM users').first();
  const file = await this.env.BUCKET.get('file.txt');
  const ai = await this.env.AI.run('@cf/meta/llama-2-7b-chat-int8', { prompt: 'Hi' });
});
```


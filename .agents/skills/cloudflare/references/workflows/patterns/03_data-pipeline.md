## Data Pipeline

```typescript
export class DataPipelineWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event, step) {
    const rawData = await step.do('extract', {retries: { limit: 10, delay: '30s', backoff: 'exponential' }}, async () => {
      const res = await fetch(event.payload.sourceUrl);
      if (!res.ok) throw new Error('Fetch failed');
      return res.json();
    });
    const transformed = await step.do('transform', async () => 
      rawData.map(item => ({ id: item.id, normalized: normalizeData(item) }))
    );
    const dataRef = await step.do('store', async () => {
      const key = `processed/${Date.now()}.json`;
      await this.env.BUCKET.put(key, JSON.stringify(transformed));
      return { key };
    });
    await step.do('load', async () => {
      const data = await (await this.env.BUCKET.get(dataRef.key)).json();
      for (let i = 0; i < data.length; i += 100) {
        await this.env.DB.batch(data.slice(i, i + 100).map(item => 
          this.env.DB.prepare('INSERT INTO records VALUES (?, ?)').bind(item.id, item.normalized)
        ));
      }
    });
  }
}
```


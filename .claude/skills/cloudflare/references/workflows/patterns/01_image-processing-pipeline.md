## Image Processing Pipeline

```typescript
export class ImageProcessingWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event, step) {
    const imageData = await step.do('fetch', async () => (await this.env.BUCKET.get(event.payload.imageKey)).arrayBuffer());
    const description = await step.do('generate description', async () => 
      await this.env.AI.run('@cf/llava-hf/llava-1.5-7b-hf', {image: Array.from(new Uint8Array(imageData)), prompt: 'Describe this image', max_tokens: 50})
    );
    await step.waitForEvent('await approval', { event: 'approved', timeout: '24h' });
    await step.do('publish', async () => await this.env.BUCKET.put(`public/${event.payload.imageKey}`, imageData));
  }
}
```


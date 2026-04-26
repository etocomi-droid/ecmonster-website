## Streaming

```typescript
const stream = new ReadableStream({
  async start(controller) {
    for (let i = 0; i < 1000; i++) {
      controller.enqueue(new TextEncoder().encode(`Item ${i}\n`));
      if (i % 100 === 0) await new Promise(r => setTimeout(r, 0));
    }
    controller.close();
  }
});
```


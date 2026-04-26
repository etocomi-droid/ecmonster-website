## Transform Streams

```typescript
response.body.pipeThrough(new TextDecoderStream()).pipeThrough(
  new TransformStream({ transform(chunk, c) { c.enqueue(chunk.toUpperCase()); } })
).pipeThrough(new TextEncoderStream());
```


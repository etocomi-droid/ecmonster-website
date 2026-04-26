## Speech Recognition

```typescript
const audioArray = Array.from(new Uint8Array(await request.arrayBuffer()));
const result = await env.AI.run('@cf/openai/whisper', { audio: audioArray });
console.log(result.text);
```


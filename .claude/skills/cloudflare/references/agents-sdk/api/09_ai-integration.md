## AI Integration

```ts
// Workers AI
const r = await this.env.AI.run("@cf/meta/llama-3.1-8b-instruct", {prompt});

// Manual streaming (prefer AIChatAgent for auto-streaming)
const stream = await client.chat.completions.create({model: "gpt-4", messages, stream: true});
for await (const chunk of stream) {
  if (chunk.choices[0]?.delta?.content) conn.send(JSON.stringify({chunk: chunk.choices[0].delta.content}));
}
```


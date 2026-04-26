## Connections & AI

```ts
// Connections (type: Agent<Env, State, ConnState>)
this.connections.forEach(c => c.send(JSON.stringify(msg))); // Broadcast
conn.setState({userId:"123"}); conn.close(1000, "Goodbye");

// Workers AI
const r = await this.env.AI.run("@cf/meta/llama-3.1-8b-instruct", {prompt});

// Manual streaming (prefer AIChatAgent)
const stream = await client.chat.completions.create({model: "gpt-4", messages, stream: true});
for await (const chunk of stream) conn.send(JSON.stringify({chunk: chunk.choices[0].delta.content}));
```

**Type-safe state:** `Agent<Env, State, ConnState>` - third param types `conn.state`


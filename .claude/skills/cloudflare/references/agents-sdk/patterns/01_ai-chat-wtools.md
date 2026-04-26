## AI Chat w/Tools

**Server (AIChatAgent):**

```ts
import { AIChatAgent } from "agents";
import { openai } from "@ai-sdk/openai";
import { tool } from "ai";
import { z } from "zod";

export class ChatAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    return this.streamText({
      model: openai("gpt-4"),
      messages: this.messages, // Auto-managed
      tools: {
        getWeather: tool({
          description: "Get current weather",
          parameters: z.object({ city: z.string() }),
          execute: async ({ city }) => `Weather in ${city}: Sunny, 72°F`
        }),
        searchDocs: tool({
          description: "Search documentation",
          parameters: z.object({ query: z.string() }),
          execute: async ({ query }) => JSON.stringify(
            this.sql<{title, content}>`SELECT title, content FROM docs WHERE content LIKE ${'%' + query + '%'}`
          )
        })
      },
      onFinish,
    });
  }
}
```

**Client (React):**

```tsx
import { useAgent } from "agents/react";
import { useAgentChat } from "agents/ai-react";

function ChatUI() {
  const agent = useAgent({ agent: "ChatAgent" });
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useAgentChat({ agent });
  
  return (
    <div>
      {messages.map(m => <div key={m.id}>{m.role}: {m.content}</div>)}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} disabled={isLoading} />
        <button disabled={isLoading}>Send</button>
      </form>
    </div>
  );
}
```


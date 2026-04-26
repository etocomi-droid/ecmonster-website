## Agent Classes

### AIChatAgent

For AI chat with auto-streaming, message history, tools, resumable streaming.

```ts
import { AIChatAgent } from "agents";
import { openai } from "@ai-sdk/openai";

export class ChatAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    return this.streamText({
      model: openai("gpt-4"),
      messages: this.messages, // Auto-managed message history
      tools: {
        getWeather: {
          description: "Get weather",
          parameters: z.object({ city: z.string() }),
          execute: async ({ city }) => `Sunny, 72°F in ${city}`
        }
      },
      onFinish, // Persist response to this.messages
    });
  }
}
```

### Agent (Base Class)

Full control for custom logic, WebSockets, email, and SQL.

```ts
import { Agent } from "agents";

export class MyAgent extends Agent<Env, State> {
  // Lifecycle methods below
}
```

**Type params:** `Agent<Env, State, ConnState>` - Env bindings, agent state, connection state


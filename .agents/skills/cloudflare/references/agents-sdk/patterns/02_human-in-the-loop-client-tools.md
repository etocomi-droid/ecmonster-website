## Human-in-the-Loop (Client Tools)

Server defines tool, client executes:

```ts
// Server
export class ChatAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    return this.streamText({
      model: openai("gpt-4"),
      messages: this.messages,
      tools: {
        confirmAction: tool({
          description: "Ask user to confirm",
          parameters: z.object({ action: z.string() }),
          execute: "client", // Client-side execution
        })
      },
      onFinish,
    });
  }
}

// Client
const { messages } = useAgentChat({
  agent,
  onToolCall: async (toolCall) => {
    if (toolCall.toolName === "confirmAction") {
      return { confirmed: window.confirm(`Confirm: ${toolCall.args.action}?`) };
    }
  }
});
```


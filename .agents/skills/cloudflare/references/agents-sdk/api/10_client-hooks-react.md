## Client Hooks (React)

```ts
// useAgent() - WebSocket connection + RPC
import { useAgent } from "agents/react";
const agent = useAgent({ agent: "MyAgent", name: "user-123" }); // name for idFromName
const result = await agent.processTask({ text: "Hello" }); // Call @callable methods
// agent.readyState: 0=CONNECTING, 1=OPEN, 2=CLOSING, 3=CLOSED

// useAgentChat() - AI chat UI
import { useAgentChat } from "agents/ai-react";
const agent = useAgent({ agent: "ChatAgent" });
const { messages, input, handleInputChange, handleSubmit, isLoading, stop, clearHistory } = 
  useAgentChat({ 
    agent, 
    maxSteps: 5,        // Max tool iterations
    resume: true,       // Auto-resume on disconnect
    onToolCall: async (toolCall) => {
      // Client tools (human-in-the-loop)
      if (toolCall.toolName === "confirm") return { ok: window.confirm("Proceed?") };
    }
  });
// status: "ready" | "submitted" | "streaming" | "error"
```

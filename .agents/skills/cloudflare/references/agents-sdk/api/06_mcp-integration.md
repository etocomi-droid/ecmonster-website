## MCP Integration

Model Context Protocol for exposing tools:

```ts
// Register & use MCP server
await this.mcp.registerServer("github", {
  url: env.MCP_SERVER_URL,
  auth: { type: "oauth", clientId: env.GITHUB_CLIENT_ID, clientSecret: env.GITHUB_CLIENT_SECRET }
});
const tools = await this.mcp.getAITools(["github"]);
return this.streamText({ model: openai("gpt-4"), messages: this.messages, tools, onFinish });
```


### "MCP connection loss on hibernation"

**Cause:** MCP server connections don't survive hibernation  
**Solution:** Re-register servers in `onStart()` or check connection status:
```ts
onStart() {
  // Re-register MCP servers after hibernation
  await this.mcp.registerServer("github", { url: env.MCP_URL, auth: {...} });
}
```


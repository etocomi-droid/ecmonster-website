## MCP Configuration (Optional)

For exposing tools via Model Context Protocol:

```typescript
// wrangler.jsonc - Add MCP OAuth secrets
{
  "vars": {
    "MCP_SERVER_URL": "https://mcp.example.com"
  }
}

// Set secrets via CLI
// npx wrangler secret put GITHUB_CLIENT_ID
// npx wrangler secret put GITHUB_CLIENT_SECRET
```

Then register in agent code (see api.md MCP section).
